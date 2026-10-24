---
title: Engineering & Quality Playbook
owner: cto
department: Engineering & Quality
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Engineering & Quality Playbook

**Owner:** Rahul Venkatesh (CTO) · **Version:** 1.0 · **Applies with:** Company OS in `CLAUDE.md`

## Mission

Build reliable, maintainable, secure products and release them safely.

## Team

| Name | Role | Agent file |
|---|---|---|
| Rahul Venkatesh | CTO / Engineering Lead | `cto` |
| Aditya Joshi | Backend Engineer 1 (APIs & data) | `backend-engineer-1` |
| Harpreet Singh Gill | Backend Engineer 2 (integrations & performance) | `backend-engineer-2` |
| Sneha Pillai | Frontend Engineer 1 (UI & accessibility) | `frontend-engineer-1` |
| Nikhil Bhatt | Frontend Engineer 2 (state & performance) | `frontend-engineer-2` |
| Divya Krishnan | QA 1: Functional & Acceptance | `qa-functional` |
| Manish Yadav | QA 2: Automation & Regression | `qa-automation` |
| Tanvi Hegde | QA 3: Performance & Reliability | `qa-performance` |
| Imran Shaikh | QA 4: Security & Edge Cases | `qa-security` |
| Gaurav Malhotra | DevOps / Release Engineer | `devops-release-engineer` |

Tools: Jira (`workspace/jira/`, key `ENG`), Confluence (`workspace/confluence/`), version control, CI/CD, monitoring, testing and security tools.

## Workflow

| Status | Entry means | Exit means | Shared category |
|---|---|---|---|
| Backlog | Task logged | Refined with acceptance criteria, estimate and owner | Not Started |
| Ready | Criteria, test plan and dependencies clear | Engineer starts work | Not Started |
| In Progress | Code being written with tests | Tests pass locally, notes written | Active |
| Code Review | Change ready for review | Approved by Rahul or a peer | In Review |
| QA | Build ready for testing | Accepted, or defects returned | In Review |
| Done | Accepted and merged locally; release handled separately | — | Complete |

Blocked work sets `category: Blocked` and names the blocker and its owner.

## Intake

- Product work arrives as `PROD` tasks from Priya Nair or Vikram Shetty; Rahul creates `ENG` tasks with owners.
- Bugs come from QA, Customer Support (Arnav Das) or monitoring as `ENG` tasks with `type: bug`.
- A task is Ready only when it has acceptance criteria, a test plan, an estimate range and known dependencies.

## Routing

| Work | Owner |
|---|---|
| APIs, data models, business logic | Aditya Joshi |
| Integrations, background jobs, backend performance | Harpreet Singh Gill |
| UI components, layouts, accessibility | Sneha Pillai |
| Client state, API wiring, frontend performance | Nikhil Bhatt |
| Acceptance and functional testing | Divya Krishnan |
| Test automation, CI gates, flaky tests | Manish Yadav |
| Load, latency, resilience | Tanvi Hegde |
| Permissions, validation, abuse cases | Imran Shaikh |
| CI/CD, environments, releases, monitoring | Gaurav Malhotra |

## Handoffs

- **Design → Engineering:** handoff notes with all states; gaps go back to Karthik Subramanian as questions.
- **Engineering → QA:** build plus notes on what changed and what to focus on.
- **QA → Engineering:** defects with steps, expected, actual, severity, evidence.
- **Engineering → Risk:** release evidence to Fatima Siddiqui; security-sensitive designs to Tenzin Wangchuk early.

## Code review policy

- Every change is reviewed before QA. Architecture-affecting changes are reviewed by Rahul.
- Reviewers check: correctness, tests, readability, security, and that nothing extra was added.
- New dependencies need Rahul's approval.

## Defect severity

| Severity | Meaning |
|---|---|
| S1 | Data loss, security breach, or core flow unusable |
| S2 | Major feature broken, no workaround |
| S3 | Feature impaired, workaround exists |
| S4 | Cosmetic or minor |

## Release gates

A production release needs all of these, in order:

1. Acceptance criteria met; QA 1 recommends acceptance; no open S1/S2 defects.
2. Automated regression suite passes (QA 2).
3. Performance within budget for expected load (QA 3), when the change affects performance.
4. Security and edge-case testing done (QA 4); security review by Tenzin Wangchuk for sensitive changes.
5. Risk & release review recommendation from Fatima Siddiqui.
6. Rollback plan and monitoring confirmed (Gaurav Malhotra).
7. **CEO approval** filed in `workspace/approvals/` by Gaurav and approved in chat.

Mandatory gates are never waived to meet a deadline. Low-risk changes may use a shorter evidence write-up, but every gate is still answered.

## Hard rules

- No agent pushes, deploys, runs migrations against shared or production systems, or reads secrets.
- No testing against production, real user accounts or third-party services without CEO approval.
- No paid services or cloud resources without CEO approval.

## Rituals

| When | What |
|---|---|
| Daily | Update task status and logs (feeds `/standup`) |
| Weekly | Engineering & Quality review: architecture, incidents, testing, release readiness |
| Bi-weekly | Sprint planning, review/demo, retrospective, backlog refinement |
| Monthly | Tech-debt and reliability review; test-suite health report |

## Definition of done (department)

- Acceptance criteria met and covered by tests.
- Code reviewed; QA accepted.
- Docs and implementation notes written.
- Task updated; decisions recorded as ADRs in `workspace/confluence/decisions/`.
