---
title: Documentation Standard
owner: knowledge-steward
department: Finance & Business Operations
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Documentation Standard

Every durable document lives in `workspace/confluence/` and is mirrored to the Confluence space automatically: each folder becomes a Confluence folder, each `.md` file a page. Bhavna Trivedi (Knowledge Steward) owns this standard and the folder structure.

## Every document starts with this header

```markdown
---
title: Tic-Tac-Toe · Product Scope
owner: business-product-manager
contributors: [cto, product-designer]
department: Product & Innovation
status: Draft
created: 2026-10-24
updated: 2026-10-24
---
```

- **owner** is the agent who created the document, by agent name (e.g. `business-product-manager`). It never changes when someone else edits; editors add themselves to `contributors`.
- **title** must be unique across the whole space. Product docs start with the product name: `Tic-Tac-Toe · Test Cases`.
- **status:** `Draft` → `In Review` → `Approved` → `Archived`. Only the owner or their lead moves a doc to Approved.
- **updated** changes on every edit.

Confluence shows these fields in a panel at the top of every page, with the owner's full name.

## Where documents go

| Folder | What goes there | Typical owner |
|---|---|---|
| `company/` | Architecture, standards, company-wide policies | COO, Knowledge Steward |
| `playbooks/` | One playbook per department | Department lead |
| `products/<product>/` | Everything about one product (see below) | Product Manager |
| `research/` | Market scans, customer research, opportunity cards | Product researchers |
| `decisions/` | Decision records: `YYYY-MM-DD-<slug>.md` | Whoever made the decision |
| `meetings/` | Stand-ups, weekly reviews, retros | COO |
| `marketing/`, `sales/`, `design/` | Department working docs | Department members |
| `templates/` | Templates for profiles, docs and tasks | People Lead, Knowledge Steward |

Create a new folder only when at least two documents need it.

## The product document set

Every product gets a folder `products/<product-slug>/` with these pages:

| File | Title | Owner |
|---|---|---|
| `overview.md` | `<Product> · Overview` (what it is, status, links to every page below and the Jira tickets) | Business Product Manager |
| `scope.md` | `<Product> · Product Scope` (problem, users, goals, in scope, out of scope, success metrics) | Business Product Manager |
| `functional-spec.md` | `<Product> · Functional Specification` (features, user flows, rules, states, edge cases, accessibility) | Product Designer |
| `technical-design.md` | `<Product> · Technical Design` (architecture, data model, key functions, decisions, limits) | The engineer who built it, reviewed by the CTO |
| `test-cases.md` | `<Product> · Test Cases` (numbered cases: ID, requirement, steps, expected result, type, status, last run) | QA Functional |
| `release-notes.md` | `<Product> · Release Notes` (versions, what changed, known issues) | DevOps / Release Engineer |

Each page links its Jira tickets by office key (e.g. ENG-1).

## Rules

1. If it matters after this week, write it down here, not only in a task log.
2. One topic per page. Link instead of copying.
3. Mark facts, estimates and hypotheses. Date anything that can go stale.
4. Never delete a page. Set `status: Archived` and say what replaced it.
5. The Knowledge Steward reviews the space monthly for stale, duplicate or owner-less pages.
