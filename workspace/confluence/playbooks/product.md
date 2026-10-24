---
title: Product & Innovation Playbook
owner: product-lead
department: Product & Innovation
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Product & Innovation Playbook

Owner: Arjun Mehta (Product Lead / Portfolio Lead) · Version 1.0 · Follows the Company OS in `CLAUDE.md`, never overrides it.

## Mission

Find valuable problems, validate opportunities, keep a healthy product pipeline, and coordinate product priorities across the portfolio.

## Team

| Name | Role | Agent |
|---|---|---|
| Arjun Mehta | Product Lead / Portfolio Lead | `product-lead` |
| Kavya Raghunathan | Market Intelligence Researcher | `market-intelligence-researcher` |
| Farhan Qureshi | Customer Research Analyst | `customer-research-analyst` |
| Ishita Banerjee | Persona Simulation Researcher | `persona-simulation-researcher` |
| Rohan Kulkarni | Product Opportunity Scout | `product-opportunity-scout` |
| Neha Agarwal | Business Validation & Pricing Analyst | `business-validation-analyst` |
| Siddharth Rao | Product Analytics Analyst | `product-analytics-analyst` |
| Priya Nair | Business-Focused Product Manager | `business-product-manager` |
| Vikram Shetty | MVP & Experiment Product Manager | `mvp-product-manager` |

## Workflow statuses (`PROD` tasks)

| Status | Means | Leaves when | Shared category |
|---|---|---|---|
| Backlog | Captured, not yet looked at | Arjun picks it for research | Not Started |
| Researching | Evidence being gathered | Research brief or scan saved | Active |
| Validating | Commercial or user test running | Learning report written | Active |
| Prioritized | Ranked, with a portfolio decision | Scoped into a PRD with criteria | Not Started |
| Ready | PRD and criteria complete, owners agreed | Work starts in a sprint | Not Started |
| In Progress | Product work underway | Output ready for review | Active |
| Review | Arjun or a PM checks against criteria | Accepted or sent back | In Review |
| Done | Accepted and recorded | — | Complete |

Any status can move to **Blocked** (shared category Blocked) with the blocker and its owner written in the log.

## Intake

Work arrives in four ways:
1. **CEO idea** via `/idea`. Meera routes to Arjun, who has Rohan write an opportunity card.
2. **Signals** from research, analytics, sales objections and support themes.
3. **Requests** from other departments, filed as `PROD` tasks.
4. **Scheduled reviews** (weekly Product & Research review, monthly portfolio review).

Arjun triages everything within one working cycle: research, park, merge or reject, with the reason logged.

## Opportunity card format

File: `workspace/confluence/research/<date>-opportunity-<slug>.md`

- **Target user:** who exactly
- **Problem:** in the user's terms
- **Evidence:** linked, each labelled Fact / Estimate / Hypothesis / SIMULATED
- **Proposed value:** what changes for the user
- **Alternatives:** what they do today, competitors
- **Rough effort:** S / M / L with who estimated
- **Risks:** product, commercial, legal, technical
- **Why now**
- **Cheapest next test**

## Eight-week backlog policy

| Window | Must contain |
|---|---|
| Weeks 1–2 | Sprint-ready tasks with owners, acceptance criteria, dependencies, test plans |
| Weeks 3–4 | Refined stories, estimates, design direction, technical feasibility |
| Weeks 5–8 | Prioritized initiatives, hypotheses, outcomes, major dependencies, open questions |

Arjun checks backlog health weekly. New work never silently displaces sprint commitments: urgent interruptions record the reason and what they push out.

## Handoffs to other departments

| To | What Product sends | Gate before sending |
|---|---|---|
| Design (Ananya Sen) | Problem, user, PRD, criteria | PRD in Prioritized or Ready |
| Engineering (Rahul Venkatesh) | PRD, criteria, priority | Design direction agreed |
| QA (Divya Krishnan) | Acceptance criteria | Criteria numbered and testable |
| Marketing (Riya Kapoor) | Value proposition, launch scope | Go decision recorded |
| Sales (Sameer Bhatia) | Pricing hypotheses, use cases | Pricing labelled as hypothesis or approved |
| Risk (Rajeev Sharma) | Anything touching personal data, payments or AI governance | Before build starts |
| Finance (Hemant Goyal) | Cost and pricing assumptions | Before portfolio decision |

PMs create tasks in other departments; the receiving lead assigns the owner.

## Review gates

1. **Portfolio decision:** Arjun ranks; CEO approves new products or major budget.
2. **PRD ready:** problem, user, metric, scope in/out, testable criteria.
3. **Experiment launch:** card with fixed thresholds; CEO approval if real users or spend are involved.
4. **Go/no-go:** learning report plus decision record.

## Recurring rituals

| When | Ritual | Who |
|---|---|---|
| Daily | Update `PROD` tasks in the stand-up | Everyone |
| Weekly | Product & Research review: pipeline and backlog health | Arjun, PMs, researchers as needed |
| Bi-weekly | Sprint planning, review, refinement with Design and Engineering | Arjun, Priya, Vikram |
| Monthly | Portfolio review; forecast-vs-actual check | Arjun, Neha, Siddharth |
| Quarterly | Scale, maintain, pivot or retire each product | Arjun with CEO |

## Definition of done (department)

- Output meets the task's acceptance criteria.
- Evidence linked and labelled; SIMULATED work clearly separated.
- Decisions recorded in `workspace/confluence/decisions/`.
- Task status, category and log updated.
- Hand-offs named in the report.
