# Customizing the office

Everything is plain Markdown and JSON. Change what you like; these are the common changes.

## Make it your company

- **Company OS:** edit `CLAUDE.md`. It holds the rules every agent follows, the approval table, the routing table and Ankit's persona. Keep the approval gates unless you have a reason to loosen them.
- **Architecture:** `workspace/confluence/company/architecture.md` is the design document the office was built from. Update it when you change how the company works.
- **Products:** code goes in `products/<name>/`, product docs in `workspace/confluence/products/<name>/`.

## Edit an agent

Each agent is one file in `.claude/agents/`. The frontmatter controls Claude Code:

```yaml
---
name: backend-engineer-1          # must match the file name; used to call the agent
description: Aditya Joshi, ...    # Claude Code reads this to decide when to delegate
tools: Read, Grep, Glob, Write, Edit, Bash, WebSearch, WebFetch
model: sonnet                     # managed by tools/set_models.py
---
```

The body is the persona and job description. Keep the section order from [the agent profile template](../workspace/confluence/templates/agent-profile.md), so every agent reports in the same format.

- **Tools** decide what an agent can do. Leave out `Bash` for roles that don't need to run commands, and leave out `WebSearch`/`WebFetch` for roles that shouldn't browse.
- **The `description`** matters most for delegation. Name concrete situations: "Use for API design, database schema changes and backend bug fixes."

## Add an agent ("hire")

1. Copy the agent profile template to `.claude/agents/<agent-name>.md` and fill it in. Follow the persona rules in the template: a fictional Indian name, a tech-startup career, no religion, caste or stereotypes.
2. Add a row to `ROSTER.md` (name, role, `` `agent-name` ``, manager, model).
3. If the agent should not be `standard` tier, add it to `tiers` in `config/models.json`, then run `python3 tools/set_models.py`.
4. Add it to the collaborator table of anyone who works with it, and to the routing table in `CLAUDE.md` if it leads a department.

Inside the office, ask Kiran Mathew (People Lead) to hire. He drafts the profile and files it for your approval.

## Remove an agent ("retire")

1. Delete `.claude/agents/<agent-name>.md`.
2. Remove its row from `ROSTER.md` and any mention in `config/models.json`.
3. Search for its name in other agents' collaborator tables and the playbooks: `grep -rn "agent-name" .claude workspace/confluence`.

## Change permissions

`.claude/settings.json` controls what runs without asking:

- **`allow`**: commands agents may run freely. Add test runners here so QA can execute tests, e.g. `"Bash(npm test:*)"`, `"Bash(node:*)"`, `"Bash(npx playwright test:*)"`.
- **`ask`**: commands that always need your OK (push, deploy, curl).
- **`deny`**: what agents may never touch (`.env`, secrets).

See the [Claude Code settings docs](https://code.claude.com/docs/en/settings).

## Add a slash command

Create `.claude/commands/<name>.md` with a `description` in the frontmatter and instructions written to Ankit. Look at `.claude/commands/standup.md` for the style.

## Change a department's workflow

Each department's statuses, review gates and rituals are in `workspace/confluence/playbooks/<department>.md`. Every status must still map to one of the five shared categories (Not Started, Active, Blocked, In Review, Complete), because the Jira sync and the stand-up use them.
