#!/usr/bin/env python3
"""Apply config/models.json to every agent file, ROSTER.md and the main session.

  python3 tools/set_models.py                  apply the current config
  python3 tools/set_models.py --preset budget  switch preset (saved in the config), then apply
  python3 tools/set_models.py --show           print each agent's model without changing anything
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "config", "models.json")
AGENTS = os.path.join(ROOT, ".claude", "agents")
ALIASES = {"opus", "sonnet", "haiku", "fable", "inherit"}


def valid(model):
    return model in ALIASES or re.fullmatch(r"claude-[a-z0-9-]+", model or "")


def plan(cfg):
    """agent name -> model, and the main-session model, from the config."""
    preset = cfg["presets"].get(cfg["preset"])
    if not preset:
        sys.exit(f"Unknown preset '{cfg['preset']}'. Choose one of: {', '.join(cfg['presets'])}")
    agents = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(AGENTS, "*.md")))
    named = set(cfg["tiers"]["strategic"]) | set(cfg["tiers"]["routine"]) | set(cfg["overrides"])
    unknown = named - set(agents)
    if unknown:
        sys.exit(f"Not an agent in .claude/agents/: {', '.join(sorted(unknown))}")
    result = {}
    for a in agents:
        tier = "strategic" if a in cfg["tiers"]["strategic"] else "routine" if a in cfg["tiers"]["routine"] else "standard"
        result[a] = cfg["overrides"].get(a) or preset[tier]
    bad = {a: m for a, m in result.items() if not valid(m)}
    if bad or (preset["main_session"] and not valid(preset["main_session"])):
        sys.exit(f"Invalid model value(s): {bad or preset['main_session']}. Use opus, sonnet, haiku, fable, inherit or a claude-... model ID.")
    return result, preset["main_session"]


def apply(models, main):
    for agent, model in models.items():
        path = os.path.join(AGENTS, agent + ".md")
        text = open(path, encoding="utf-8").read()
        new = re.sub(r"^model: .*$", f"model: {model}", text, count=1, flags=re.M)
        if "\nmodel: " not in new.split("---", 2)[1]:  # no model line yet: add one to the frontmatter
            new = new.replace("\n---", f"\nmodel: {model}\n---", 1)
        open(path, "w", encoding="utf-8").write(new)

    roster = os.path.join(ROOT, "ROSTER.md")
    lines = []
    for line in open(roster, encoding="utf-8"):
        m = re.match(r"(\| [^|]+ \| [^|]+ \| `([a-z0-9-]+)` \| [^|]+ \| )[^|]+( \|)$", line.rstrip("\n"))
        lines.append(f"{m.group(1)}{models[m.group(2)]}{m.group(3)}\n" if m and m.group(2) in models else line)
    open(roster, "w", encoding="utf-8").write("".join(lines))

    settings_path = os.path.join(ROOT, ".claude", "settings.json")
    settings = json.load(open(settings_path, encoding="utf-8"))
    if main:
        settings["model"] = main
    else:
        settings.pop("model", None)
    open(settings_path, "w", encoding="utf-8").write(json.dumps(settings, indent=2) + "\n")


def main():
    cfg = json.load(open(CONFIG, encoding="utf-8"))
    args = sys.argv[1:]
    if args[:1] == ["--preset"] and len(args) == 2:
        cfg["preset"] = args[1]
        plan(cfg)  # validate before saving
        open(CONFIG, "w", encoding="utf-8").write(json.dumps(cfg, indent=2) + "\n")
    models, main_model = plan(cfg)
    counts = {}
    for m in models.values():
        counts[m] = counts.get(m, 0) + 1
    if args[:1] == ["--show"]:
        for a, m in models.items():
            print(f"{a:36} {m}")
    else:
        apply(models, main_model)
        for a, m in models.items():  # self-check: every file now carries its planned model
            assert re.search(rf"^model: {re.escape(m)}$", open(os.path.join(AGENTS, a + '.md'), encoding="utf-8").read(), re.M), a
    print(f"Preset '{cfg['preset']}': " + ", ".join(f"{n} agents on {m}" for m, n in sorted(counts.items()))
          + f". Main session: {main_model or 'your Claude Code default'}.")


if __name__ == "__main__":
    main()
