# Jira (local stand-in)

One Markdown file per task: `workspace/jira/<KEY>-<number>-<short-slug>.md`, for example `PROD-12-pricing-hypotheses.md`.

## Project keys

| Key | Department |
|---|---|
| OPS | COO / Finance & Business Operations |
| PROD | Product & Innovation |
| DES | Design & UX |
| ENG | Engineering & Quality |
| MKT | Marketing & Growth |
| SALES | Sales & Partnerships |
| CS | Customer Success & Support |
| RISK | Security, Legal & Compliance |
| HR | People, HR & Culture |

Number tasks per key in order (check the highest existing number first).

## Task file format

```markdown
---
key: PROD-12
title: Draft pricing hypotheses for Product A
type: task            # task | story | bug | epic | approval
product: Product A    # or "Company"
status: Not Started   # department status, see the playbook
category: Not Started # Not Started | Active | Blocked | In Review | Complete
priority: P2          # P0 urgent · P1 high · P2 normal · P3 low
owner: business-validation-analyst
reporter: business-product-manager
created: 2026-10-24
due: 2026-10-31
links: [workspace/confluence/prds/product-a.md]
---

## Goal
## Acceptance criteria
- [ ] ...
## Notes / log
- 2026-10-24 · <agent>: <update>
```

## Rules

- Every task has exactly one owner, a priority and acceptance criteria.
- Update `status`, `category` and the log whenever work changes.
- Urgent interruptions record the reason and what they displace.
