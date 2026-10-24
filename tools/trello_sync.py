#!/usr/bin/env python3
"""Mirror workspace/jira task files to a Trello board.

Commands:
  setup        create the 5 status lists and the department/priority labels on the board
  sync [FILE]  push new/changed task files (all changed ones if no FILE)
  hook         same as sync, but never fails; called by Claude Code hooks
  pull         copy new human comments from Trello cards into the task logs

Config (env or .env in the office root): TRELLO_API_KEY, TRELLO_TOKEN, TRELLO_BOARD_ID.
TRELLO_DRY_RUN=1 prints API calls instead of sending them.
"""
import glob, hashlib, json, os, re, ssl, sys, urllib.parse, urllib.request
from datetime import datetime, timezone

try:  # python.org builds on macOS ship without CA certs; use certifi or the system bundle
    import certifi
    SSL = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if os.path.exists("/etc/ssl/cert.pem") else None)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JIRA = os.path.join(ROOT, "workspace", "jira")
STATE = os.environ.get("TRELLO_STATE") or os.path.join(JIRA, ".trello-state.json")
LOG = os.path.join(JIRA, ".trello-sync.log")
API = "https://api.trello.com/1"
BOT = "[office]"  # prefix on comments we write, so pull can tell them from human comments

LISTS = ["Not Started", "Active", "Blocked", "In Review", "Complete"]
DEPTS = {"OPS": ("COO / Finance & Ops", "black"), "PROD": ("Product", "blue"), "DES": ("Design", "pink"),
         "ENG": ("Engineering", "purple"), "MKT": ("Marketing", "orange"), "SALES": ("Sales", "lime"),
         "CS": ("Customer Success", "sky"), "RISK": ("Risk & Legal", "red"), "HR": ("People", "green")}
PRIOS = {"P0": "red", "P1": "orange", "P2": "yellow", "P3": "green"}


def load_env():
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            k, _, v = line.strip().partition("=")
            if k and not k.startswith("#"):
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def call(method, path, **params):
    if os.environ.get("TRELLO_DRY_RUN"):
        print(method, path, {k: (str(v)[:60]) for k, v in params.items()})
        return {"id": "dry-" + hashlib.md5((path + str(sorted(params.items()))).encode()).hexdigest()[:8]} if method != "GET" else []
    params.update(key=os.environ["TRELLO_API_KEY"], token=os.environ["TRELLO_TOKEN"])
    data = urllib.parse.urlencode(params).encode()
    url = API + path
    if method == "GET":
        url, data = url + "?" + data.decode(), None
    req = urllib.request.Request(url, data=data, method=method)
    with urllib.request.urlopen(req, timeout=20, context=SSL) as r:
        return json.loads(r.read() or "null")


def load_state():
    try:
        return json.load(open(STATE))
    except (OSError, ValueError):
        return {"lists": {}, "labels": {}, "cards": {}, "last_pull": None}


def save_state(s):
    json.dump(s, open(STATE, "w"), indent=1)


def roster():
    """agent-name -> person name, from ROSTER.md."""
    names = {"coo": "Meera Iyer", "ceo": "Ankit"}
    for line in open(os.path.join(ROOT, "ROSTER.md")):
        m = re.match(r"\| ([^|]+?) \| [^|]+ \| `([a-z0-9-]+)` \|", line)
        if m:
            names[m.group(2)] = m.group(1)
    return names


def parse(path):
    text = open(path).read()
    _, fm, body = text.split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.split("#")[0].strip()
    sections = dict(re.findall(r"^## (.+?)\n(.*?)(?=^## |\Z)", body, re.S | re.M))
    entries = []  # top-level "- " lines; indented lines belong to the entry above
    for line in sections.get("Notes / log", "").splitlines():
        if line.startswith("- "):
            entries.append(line[2:])
        elif line.strip() and entries:
            entries[-1] += "\n" + line.strip()
    return meta, sections, entries, hashlib.md5(text.encode()).hexdigest()


def who(agent, names):
    agent = (agent or "").strip()
    return f"{names[agent]} ({agent})" if agent in names else agent or "unassigned"


def describe(meta, sections, path, names):
    head = "\n".join([
        f"**Owner:** {who(meta.get('owner'), names)}",
        f"**Reporter:** {who(meta.get('reporter'), names)}",
        f"**Department status:** {meta.get('status', '')}",
        f"**Priority:** {meta.get('priority', '')} · **Type:** {meta.get('type', '')} · **Product:** {meta.get('product', '')}",
        f"**File:** `{os.path.relpath(path, ROOT)}`"])
    parts = [head] + [f"## {k}\n{sections[k].strip()}" for k in ("Goal", "Acceptance criteria", "Details", "Not in scope") if k in sections]
    return "\n\n".join(parts)[:16000]


def comment(card_id, text):
    call("POST", f"/cards/{card_id}/actions/comments", text=f"{BOT} {text}"[:16000])


def setup(s):
    board = os.environ["TRELLO_BOARD_ID"]
    have = {l["name"]: l["id"] for l in call("GET", f"/boards/{board}/lists") or []}
    for name in LISTS:
        s["lists"][name] = have.get(name) or call("POST", "/lists", name=name, idBoard=board, pos="bottom")["id"]
    have = {l["name"]: l["id"] for l in call("GET", f"/boards/{board}/labels") or []}
    for name, color in list(DEPTS.values()) + list(PRIOS.items()):
        s["labels"][name] = have.get(name) or call("POST", "/labels", name=name, color=color, idBoard=board)["id"]
    save_state(s)


def sync_file(path, s, names):
    meta, sections, entries, digest = parse(path)
    key = meta.get("key") or os.path.basename(path).split("-", 2)[0] + "-" + os.path.basename(path).split("-", 2)[1]
    card = s["cards"].get(key)
    if card and card["hash"] == digest:
        return
    cat = meta.get("category") if meta.get("category") in LISTS else "Not Started"
    labels = [s["labels"][n] for n in (DEPTS.get(key.split("-")[0], ("",))[0], meta.get("priority")) if n in s["labels"]]
    fields = dict(name=f"{key} · {meta.get('title', '')}", desc=describe(meta, sections, path, names),
                  idList=s["lists"][cat], idLabels=",".join(labels))
    if re.match(r"\d{4}-\d{2}-\d{2}$", meta.get("due", "")):
        fields["due"] = meta["due"] + "T12:00:00.000Z"
    if not card:
        card = s["cards"][key] = {"id": call("POST", "/cards", **fields)["id"], "log": 0}
        comment(card["id"], f"Ticket created by {who(meta.get('reporter'), names)}. Owner: {who(meta.get('owner'), names)}. Status: {meta.get('status')}.")
    else:
        call("PUT", f"/cards/{card['id']}", **fields)
        if card.get("category") != cat:
            comment(card["id"], f"Moved {card.get('category')} → {cat} (status: {meta.get('status')}).")
        elif card.get("status") != meta.get("status"):
            comment(card["id"], f"Status changed {card.get('status')} → {meta.get('status')}.")
        if card.get("owner") != meta.get("owner"):
            comment(card["id"], f"Owner changed {who(card.get('owner'), names)} → {who(meta.get('owner'), names)}.")
    for entry in entries[card["log"]:]:
        comment(card["id"], entry)
    card.update(log=len(entries), hash=digest, category=cat, status=meta.get("status"), owner=meta.get("owner"))
    save_state(s)


def task_files():
    return sorted(f for f in glob.glob(os.path.join(JIRA, "*-*.md")) if re.match(r"[A-Z]+-\d+-", os.path.basename(f)))


def sync(files, s):
    if not s["lists"]:
        setup(s)
    names = roster()
    for f in files or task_files():
        sync_file(os.path.abspath(f), s, names)


def pull(s):
    """Append human Trello comments to the task log so agents see them."""
    since = s.get("last_pull")
    now = datetime.now(timezone.utc).isoformat()
    for f in task_files():
        meta, _, entries, _ = parse(f)
        card = s["cards"].get(meta.get("key"))
        if not card:
            continue
        params = {"filter": "commentCard"} | ({"since": since} if since else {})
        new = [a for a in reversed(call("GET", f"/cards/{card['id']}/actions", **params) or [])
               if not a["data"]["text"].startswith(BOT)]
        if not new:
            continue
        with open(f, "a") as fh:
            for a in new:
                author = a.get("memberCreator", {}).get("fullName", "Trello user")
                fh.write(f"- {a['date'][:10]} · {author} (Trello comment): {a['data']['text'].strip()}\n")
                print(f"{meta['key']}: {author}: {a['data']['text'].strip()[:80]}")
        # Mark the pulled lines as synced so they are not echoed back as bot comments.
        _, _, entries, digest = parse(f)
        card.update(log=len(entries), hash=digest)
    s["last_pull"] = now
    save_state(s)


def main():
    load_env()
    cmd, args = (sys.argv[1:2] or ["sync"])[0], sys.argv[2:]
    configured = all(os.environ.get(k) for k in ("TRELLO_API_KEY", "TRELLO_TOKEN", "TRELLO_BOARD_ID"))
    if not configured and not os.environ.get("TRELLO_DRY_RUN"):
        if cmd == "hook":
            return  # Trello not set up yet: stay silent so the office still works
        sys.exit("Trello not configured: set TRELLO_API_KEY, TRELLO_TOKEN, TRELLO_BOARD_ID in .env")
    s = load_state()
    try:
        {"setup": lambda: setup(s), "pull": lambda: pull(s)}.get(cmd, lambda: sync(args, s))()
    except Exception as e:
        if cmd != "hook":
            raise
        with open(LOG, "a") as fh:  # hooks must never block the agents
            fh.write(f"{datetime.now().isoformat()} {type(e).__name__}: {e}\n")


if __name__ == "__main__":
    main()
