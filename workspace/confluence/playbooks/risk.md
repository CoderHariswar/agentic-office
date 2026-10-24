---
title: Security, Legal & Compliance Playbook
owner: chief-risk-officer
department: Security, Legal & Compliance
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Security, Legal & Compliance Playbook

**Owner:** Rajeev Sharma (Chief Risk, Legal & Compliance Officer) · **Version:** 1.0 · **Applies under:** Company OS (`CLAUDE.md`)

## Mission

Reduce legal, privacy, security and regulatory risk across every product while keeping the company able to move.

## Team

| Name | Role | Agent |
|---|---|---|
| Rajeev Sharma | Chief Risk, Legal & Compliance Officer | `chief-risk-officer` |
| Tenzin Wangchuk | Security & Privacy Analyst | `security-privacy-analyst` |
| Aparna Bhattacharya | Legal & Contracts Analyst | `legal-contracts-analyst` |
| Suresh Gowda | Compliance & Governance Analyst | `compliance-governance-analyst` |
| Fatima Siddiqui | Risk & Release Review Analyst | `risk-release-reviewer` |

Reporting: operationally coordinated by Meera Iyer (COO). Rajeev has a direct escalation line to the CEO.

## Workflow

Jira key: `RISK`. Statuses and their meaning:

| Status | Enters when | Exits when | Shared category |
|---|---|---|---|
| Requested | Review or question raised | Rajeev assigns scope and owner | Not Started |
| Assessment | Owner scoping and rating the risk | Plan agreed | Active |
| In Progress | Review, drafting or remediation under way | Findings ready for decision | Active |
| Awaiting Approval | Decision needed from Rajeev, counsel or CEO | Decision made | In Review |
| Approved / Rejected | Decision recorded | Follow-up tasks created | In Review |
| Completed | Evidence filed, register updated | — | Complete |

A task waiting on another team's fix is marked Blocked in its category field.

## Intake

- Requests through Meera, or directly from Product, Engineering, Sales or Marketing as `RISK` tasks.
- Every new product idea gets a light risk check before validation.
- Every planned release opens a release-review task for Fatima.
- Contracts, proposals and public claims go to Aparna before sending.

## Risk rating

Likelihood (Low, Medium, High) × Impact (Low, Medium, High):

| Rating | Meaning | Action |
|---|---|---|
| Critical | Active exploit, data exposure, legal breach | Stop work; Rajeev escalates to CEO at once |
| High | Likely serious harm if unaddressed | Blocks release; Rajeev decides; CEO accepts any residual |
| Medium | Real but contained | Fix within the sprint or accept with owner and date |
| Low | Minor | Log and batch |

## Escalation paths

- Critical: any team member → Rajeev → CEO directly, same session.
- Material legal questions: Aparna → Rajeev → qualified human counsel.
- Applicability of law: Suresh → Rajeev → qualified professional.
- Pressure to release with a failing mandatory gate: Fatima → Rajeev → CEO.

## Mandatory release gates

Fatima checks evidence for each before any production release:

1. Acceptance tests passed (Divya Krishnan).
2. Regression suite green (Manish Yadav).
3. Performance check for changed paths (Tanvi Hegde), where relevant.
4. Security tests and no open Critical/High findings (Imran Shaikh, Tenzin).
5. Privacy review for new data collection or use (Tenzin).
6. Legal review for new terms, claims or contracts (Aparna).
7. Compliance checklist current (Suresh).
8. Deployment and rollback plan (Gaurav Malhotra).
9. CEO approval filed in `workspace/approvals/`.

Mandatory gates cannot be waived to meet a deadline.

## Hand-offs

| From | To | What |
|---|---|---|
| Tenzin | Rahul Venkatesh | Remediation `ENG` tasks |
| Aparna | Raghav Saxena, Sameer Bhatia | Contract and proposal issue lists |
| Suresh | Deepak Chauhan, Simran Kaur | Disclosure and consent checks |
| Fatima | Meera / CEO | Release recommendation and approval file |

## Recurring rituals

- **Weekly:** open-findings review (Rajeev); release readiness at the Engineering & Quality review (Fatima).
- **Monthly:** risk register review; access review (Tenzin); compliance gap report (Suresh).
- **Quarterly:** policy review and incident runbook rehearsal.

## Standing rules

- All legal and compliance output is preliminary until a qualified professional confirms it.
- No unauthorized testing; Bash only for read-only local scans.
- Secrets are never copied into files or reports.

## Definition of done

- Risk rated with evidence; residual risk stated and accepted by the right person.
- Remediation tasks have owners and dates.
- Evidence filed; risk register updated; status Completed.
