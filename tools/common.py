"""Shared helpers for the Jira and Confluence sync scripts."""
import glob, hashlib, os, re, ssl

try:  # python.org builds on macOS ship without CA certs; use certifi or the system bundle
    import certifi
    SSL = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if os.path.exists("/etc/ssl/cert.pem") else None)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JIRA = os.path.join(ROOT, "workspace", "jira")
BOT = "[office]"  # prefix on comments we write, so pull can tell them from human comments


def load_env():
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            k, _, v = line.strip().partition("=")
            if k and not k.startswith("#"):
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def roster():
    """agent-name -> person name, from ROSTER.md."""
    names = {"coo": "Ankit Jha", "ceo": "CEO"}
    for line in open(os.path.join(ROOT, "ROSTER.md")):
        m = re.match(r"\| ([^|]+?) \| [^|]+ \| `([a-z0-9-]+)` \|", line)
        if m:
            names[m.group(2)] = m.group(1)
    return names


def parse(path):
    """Task file -> (frontmatter dict, sections dict, log entries, content hash)."""
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


def task_files():
    return sorted(f for f in glob.glob(os.path.join(JIRA, "*-*.md")) if re.match(r"[A-Z]+-\d+-", os.path.basename(f)))
