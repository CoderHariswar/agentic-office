# Contributing

Thanks for helping. This project is meant to be a practical, honest starting point for multi-agent work in Claude Code. Small, focused contributions are the most useful.

## Good first contributions

- Fix a confusing sentence in an agent profile, playbook or doc.
- Add an example run under `examples/` (a real run, unedited, with its tasks and docs).
- Pick an item from the [roadmap](README.md#roadmap) and open an issue to discuss your approach first.
- Report a bug in the sync scripts with the command, the error, and your Python version.

## Ground rules

1. **Keep it dependency-free.** Scripts use the Python standard library only. Docs and agents are Markdown.
2. **Never weaken safety by default.** Approval gates, the `.env` read block and the "ask before push or deploy" rules stay on. Make loosening them an explicit, documented opt-in.
3. **No secrets, no personal data.** Don't commit `.env`, state files, real customer data or real people's details.
4. **Be honest about results.** Examples and docs should say what was verified and what was not. Don't present simulated research or unrun tests as real.

## Persona rules (for agent profiles)

- Names are Indian and fictional; backgrounds are tech-startup careers; never use real companies or real people.
- Never mention religion, caste or ethnicity, and never write regional stereotypes.
- Follow the section order of [`workspace/confluence/templates/agent-profile.md`](workspace/confluence/templates/agent-profile.md), including the report format.
- A persona describes how someone works. It never grants permissions; those come from the Company OS and the `tools` list.

## Testing your change

- **Agent or command changes:** open the project in Claude Code, run `/agents` to confirm it loads, and run one small task that uses the changed agent. Mention the task and outcome in your pull request.
- **Model config:** `python3 tools/set_models.py --show` must succeed; run `python3 tools/set_models.py` and check that `git diff` only touches the `model:` lines you expected.
- **Sync scripts:** run them in dry-run mode, which prints the API calls instead of sending them:
  ```bash
  JIRA_DRY_RUN=1 JIRA_STATE=/tmp/j.json python3 tools/jira_sync.py sync
  CONFLUENCE_DRY_RUN=1 CONFLUENCE_SPACE_KEY=TEST CONFLUENCE_STATE=/tmp/c.json python3 tools/confluence_sync.py sync
  ```
  If you have a test Atlassian site, run against it too and say so in the pull request.

## Pull requests

- One topic per pull request.
- Say what changed, why, and how you tested it.
- Update the README or `docs/` when behavior changes.
- By contributing you agree your work is released under the [MIT License](LICENSE).

## Code of conduct

Be kind, assume good intent, and keep discussion about the work. Harassment or personal attacks are not tolerated.
