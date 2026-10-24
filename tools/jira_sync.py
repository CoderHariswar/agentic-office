#!/usr/bin/env python3
"""Mirror workspace/jira task files to a real Jira Cloud project.

Commands:
  check        verify credentials and project, list issue types and statuses
  sync [FILE]  push new/changed task files (all changed ones if no FILE)
  hook         same as sync, but never fails; called by Claude Code hooks
  pull         copy new human comments from Jira issues into the task logs

Config (env or .env in the office root): JIRA_SITE, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY.
JIRA_DRY_RUN=1 prints API calls instead of sending them.
"""
import base64, json, os, re, sys, urllib.error, urllib.request
from datetime import datetime

from trello_sync import BOT, JIRA, ROOT, SSL, load_env, parse, roster, task_files, who, describe

STATE = os.environ.get("JIRA_STATE") or os.path.join(JIRA, ".jira-state.json")
LOG = os.path.join(JIRA, ".jira-sync.log")
DEPTS = {"OPS": "ops", "PROD": "product", "DES": "design", "ENG": "engineering", "MKT": "marketing",
         "SALES": "sales", "CS": "customer-success", "RISK": "risk-legal", "HR": "people"}
# Office category -> Jira status names to try, in order (team- and company-managed defaults differ).
TARGETS = {"Not Started": ["To Do", "Backlog", "Open"], "Active": ["In Progress"],
           "Blocked": ["Blocked", "In Progress"], "In Review": ["In Review", "Review", "In Progress"],
           "Complete": ["Done", "Closed", "Resolved"]}
TYPES = {"bug": "Bug", "story": "Story", "epic": "Epic"}


def call(method, path, body=None):
    if os.environ.get("JIRA_DRY_RUN"):
        print(method, path, json.dumps(body)[:120] if body else "")
        return {"key": "DRY-1", "transitions": [], "comments": []}
    auth = base64.b64encode(f"{os.environ['JIRA_EMAIL']}:{os.environ['JIRA_API_TOKEN']}".encode()).decode()
    req = urllib.request.Request(os.environ["JIRA_SITE"].rstrip("/") + "/rest/api/3" + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Basic " + auth, "Accept": "application/json",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=SSL) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} -> {e.code}: {e.read()[:300].decode(errors='replace')}")


def adf(text):
    """Markdown-ish text -> Atlassian Document Format (headings + one paragraph per line)."""
    nodes = []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = re.match(r"(#{1,6}) (.*)", line)
        if m:
            nodes.append({"type": "heading", "attrs": {"level": 3}, "content": [{"type": "text", "text": m.group(2)}]})
        else:
            nodes.append({"type": "paragraph", "content": [{"type": "text", "text": line.replace("**", "")}]})
    return {"type": "doc", "version": 1, "content": nodes or [{"type": "paragraph", "content": []}]}


def plain(node):
    if node.get("type") == "text":
        return node.get("text", "")
    sep = "\n" if node.get("type") in ("doc",) else ""
    return sep.join(plain(c) for c in node.get("content", []))


def load_state():
    try:
        return json.load(open(STATE))
    except (OSError, ValueError):
        return {"issues": {}}


def save_state(s):
    json.dump(s, open(STATE, "w"), indent=1)


def comment(issue, text):
    call("POST", f"/issue/{issue}/comment", {"body": adf(f"{BOT} {text}"[:30000])})


READY = {"Ready", "Prioritized", "Brief Approved", "Approved", "Qualified", "Triaged"}  # dept statuses meaning "picked, not started"


def transition(issue, category, status=""):
    available = call("GET", f"/issue/{issue}/transitions")["transitions"]
    first = ["Selected for Development"] if category == "Not Started" and status in READY else []
    for name in first + TARGETS[category]:
        for t in available:
            if t["to"]["name"].lower() == name.lower():
                call("POST", f"/issue/{issue}/transitions", {"transition": {"id": t["id"]}})
                return t["to"]["name"]
    return None


def sync_file(path, s, names):
    meta, sections, entries, digest = parse(path)
    key = meta["key"]
    issue = s["issues"].get(key)
    if issue and issue["hash"] == digest:
        return
    cat = meta.get("category") if meta.get("category") in TARGETS else "Not Started"
    labels = ["office", "office-" + key, DEPTS.get(key.split("-")[0], "company")]
    labels += [p for p in [meta.get("priority")] if p] + (["blocked"] if cat == "Blocked" else [])
    fields = {"summary": f"[{key}] {meta.get('title', '')}"[:250], "labels": labels,
              "description": adf(describe(meta, sections, path, names) + f"\n**Due:** {meta.get('due') or 'none'}")}
    if not issue:
        fields |= {"project": {"key": os.environ["JIRA_PROJECT_KEY"]},
                   "issuetype": {"name": TYPES.get(meta.get("type"), "Task")}}
        try:
            created = call("POST", "/issue", {"fields": fields})
        except RuntimeError:  # project may not have Story/Bug/Epic: fall back to Task
            fields["issuetype"] = {"name": "Task"}
            created = call("POST", "/issue", {"fields": fields})
        issue = s["issues"][key] = {"key": created["key"], "log": 0}
        comment(issue["key"], f"Ticket created by {who(meta.get('reporter'), names)}. Owner: {who(meta.get('owner'), names)}. Status: {meta.get('status')}.")
        if cat != "Not Started":
            transition(issue["key"], cat, meta.get("status", ""))
    else:
        call("PUT", f"/issue/{issue['key']}", {"fields": fields})
        if issue.get("category") != cat:
            landed = transition(issue["key"], cat, meta.get("status", ""))
            comment(issue["key"], f"Moved {issue.get('category')} → {cat} (status: {meta.get('status')}"
                                  + (f"; Jira status: {landed})." if landed else "; no matching Jira transition)."))
        elif issue.get("status") != meta.get("status"):
            comment(issue["key"], f"Status changed {issue.get('status')} → {meta.get('status')}.")
        if issue.get("owner") != meta.get("owner"):
            comment(issue["key"], f"Owner changed {who(issue.get('owner'), names)} → {who(meta.get('owner'), names)}.")
    for entry in entries[issue["log"]:]:
        comment(issue["key"], entry)
    issue.update(log=len(entries), hash=digest, category=cat, status=meta.get("status"), owner=meta.get("owner"))
    save_state(s)


def sync(files, s):
    names = roster()
    for f in files or task_files():
        sync_file(os.path.abspath(f), s, names)


def pull(s):
    """Append human Jira comments to the task log so agents see them."""
    for f in task_files():
        meta, _, _, _ = parse(f)
        issue = s["issues"].get(meta.get("key"))
        if not issue:
            continue
        seen = set(issue.get("seen", []))
        new = [c for c in call("GET", f"/issue/{issue['key']}/comment?orderBy=created")["comments"]
               if c["id"] not in seen and not plain(c["body"]).startswith(BOT)]
        if not new:
            continue
        with open(f, "a") as fh:
            for c in new:
                author = c.get("author", {}).get("displayName", "Jira user")
                text = " ".join(plain(c["body"]).split())
                fh.write(f"- {c['created'][:10]} · {author} (Jira comment on {issue['key']}): {text}\n")
                print(f"{meta['key']} ({issue['key']}): {author}: {text[:80]}")
        # Mark pulled lines as synced so they are not echoed back as bot comments.
        _, _, entries, digest = parse(f)
        issue.update(log=len(entries), hash=digest, seen=sorted(seen | {c["id"] for c in new}))
    save_state(s)


def check():
    me = call("GET", "/myself")
    print("Signed in as", me.get("displayName"), me.get("emailAddress", ""))
    p = call("GET", f"/project/{os.environ['JIRA_PROJECT_KEY']}")
    print("Project", p["key"], "-", p["name"], "| issue types:", ", ".join(t["name"] for t in p.get("issueTypes", [])))
    statuses = {st["name"] for t in call("GET", f"/project/{p['key']}/statuses") for st in t["statuses"]}
    print("Statuses:", ", ".join(sorted(statuses)))


def main():
    load_env()
    cmd, args = (sys.argv[1:2] or ["sync"])[0], sys.argv[2:]
    configured = all(os.environ.get(k) for k in ("JIRA_SITE", "JIRA_EMAIL", "JIRA_API_TOKEN", "JIRA_PROJECT_KEY"))
    if not configured and not os.environ.get("JIRA_DRY_RUN"):
        if cmd == "hook":
            return  # Jira not set up yet: stay silent so the office still works
        sys.exit("Jira not configured: set JIRA_SITE, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY in .env")
    s = load_state()
    try:
        {"check": check, "pull": lambda: pull(s)}.get(cmd, lambda: sync(args, s))()
    except Exception as e:
        if cmd != "hook":
            raise
        with open(LOG, "a") as fh:  # hooks must never block the agents
            fh.write(f"{datetime.now().isoformat()} {type(e).__name__}: {e}\n")


if __name__ == "__main__":
    main()
