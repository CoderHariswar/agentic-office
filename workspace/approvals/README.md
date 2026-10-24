# CEO Approval Queue

Anything on the "CEO approval required" list in `CLAUDE.md` waits here until the CEO says "approved" in chat.

File name: `workspace/approvals/<YYYY-MM-DD>-<short-slug>.md`

```markdown
---
status: pending        # pending | approved | rejected
requested_by: <agent-name>
type: release          # spend | release | publish | data-access | hiring | new-product | other
task: ENG-7
requested: 2026-10-24
decided:
---

## What is being asked
## Why now
## Cost / risk
## What happens if approved
## What happens if rejected
## Evidence (links)
```

When the CEO decides, Meera sets `status`, fills `decided`, adds one line with the CEO's words, and updates the linked task.
