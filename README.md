# Agentic Office

A whole company run from Claude Code. You are the CEO. The main Claude session is your Chief of Staff, Meera Iyer. 55 named agents across 9 departments do the work.

## Start

```bash
cd agentic-office
claude
```

Then talk to Meera in plain language, or use a command:

| Command | What it does |
|---|---|
| `/idea <your idea>` | Product turns it into an opportunity card and a next test |
| `/standup` | Daily status across all departments from the task files |
| `/weekly-review` | Wins, priorities, risks and decisions you need to make |
| `/approvals` | Everything waiting for your "approved" |
| `/pull-comments` | Brings your Jira and Trello comments into the tasks and acts on them |

You can also ask for a person directly: "Ask Neha Agarwal to draft pricing hypotheses for Product A."

## What is where

| Path | What it is |
|---|---|
| `CLAUDE.md` | Company OS: rules, approval rights, Meera's persona and routing |
| `ROSTER.md` | Everyone's name, role, manager and model |
| `.claude/agents/` | One file per employee: persona, job, process, collaborators, guardrails |
| `.claude/commands/` | The slash commands above |
| `workspace/jira/` | Tasks (local stand-in for Jira) |
| `workspace/confluence/` | Architecture, playbooks, PRDs, research, decisions, meetings |
| `workspace/approvals/` | Items waiting for your approval |
| `workspace/memory/` | Each agent's log of decisions and lessons |

## Jira

Every ticket, status move and discussion also shows up in Jira at https://jhaankitkumar12.atlassian.net. Same model as Trello below: task files stay the source of truth and `tools/jira_sync.py` mirrors them after every change.

Set up once:
1. In Jira, create a project (Kanban is simplest) and note its key, e.g. `OFFICE`.
2. Create an API token at https://id.atlassian.com/manage-profile/security/api-tokens.
3. `cp .env.example .env` and fill in `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY` (the site is already filled in).
4. `python3 tools/jira_sync.py check` confirms the login and shows the project's statuses.
5. `python3 tools/jira_sync.py sync` pushes the existing tasks.

Office statuses map to Jira: Not Started → To Do, Active → In Progress, In Review → In Review (or In Progress if the project has no review column), Complete → Done. Blocked tasks get a `blocked` label.

## Trello

Every ticket, status move and discussion shows up on a Trello board. Task files in `workspace/jira/` stay the source of truth, and a hook mirrors them after every change.

Set up once:
1. Create an empty Trello board.
2. `cp .env.example .env` and fill in the API key, token and board ID (instructions are in the file).
3. `python3 tools/trello_sync.py setup` creates the lists and labels.
4. `python3 tools/trello_sync.py sync` pushes the existing tasks.

| On Trello you see | Comes from |
|---|---|
| A card in Not Started / Active / Blocked / In Review / Complete | The task's `category` |
| Labels for department and priority | Task key and `priority` |
| Description with owner, status, goal, acceptance criteria | Task file |
| Comments starting with `[office]` | Ticket created, moved, owner changed, and every log entry |

Comment on a card yourself, then run `/pull-comments` (or `/standup`). Meera reads your comments into the task and acts on them.

## Approval gates

Agents never publish, deploy, spend money, contact real people or touch personal data on their own. They prepare the work, file it in `workspace/approvals/`, and wait for you. `.claude/settings.json` also makes push and deploy commands ask first and blocks reading `.env` files.

## Keeping Pro usage low

- Ask for specific people or one department at a time.
- Routine roles already run on `haiku` and most specialists on `sonnet`. Only the Product Lead, CTO and Chief Risk Officer use `opus`.
- Start a fresh session for each big topic.

## Connecting Jira and Confluence later

Add the Atlassian connector, then tell Meera to switch from `workspace/jira` and `workspace/confluence` to the real tools. Agent files list their tools in the frontmatter. Add the connector's tool names there for agents that need it.
