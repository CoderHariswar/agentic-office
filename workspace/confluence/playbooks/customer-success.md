---
title: Customer Success & Support Playbook
owner: customer-success-lead
department: Customer Success & Support
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Customer Success & Support Playbook

**Owner:** Swati Chaturvedi (Customer Success Lead) · **Version:** 1.0 · **Applies under:** Company OS (`CLAUDE.md`)

## Mission

Help customers succeed, resolve issues, improve retention and turn feedback into product learning.

## Team

| Name | Role | Agent |
|---|---|---|
| Swati Chaturvedi | Customer Success Lead | `customer-success-lead` |
| Arnav Das | Customer Support Agent | `customer-support` |
| Meghna Bose | Onboarding & Education Agent | `onboarding-education` |
| Yusuf Ansari | Feedback Classification Agent | `feedback-classification` |
| Pallavi Jain | Retention & Customer Health Analyst | `retention-health-analyst` |

## Workflow

Jira key: `CS`. Statuses and their meaning:

| Status | Enters when | Exits when | Shared category |
|---|---|---|---|
| New | Request or task created | Someone starts triage | Not Started |
| Triaged | Product, area, severity and owner set | Owner starts work | Not Started |
| Investigating | Owner is working on it | Answer found, or waiting on someone | Active |
| Waiting for Customer | Need information from the customer | Customer replies or 7 days pass | Blocked |
| Escalated | Sent to Swati, Product, Engineering or Risk | Escalation owner responds | Blocked |
| Resolved | Answer or fix delivered (draft approved) | Confirmed or 3 days pass | In Review |
| Closed | Done, logged, linked | — | Complete |

## Intake

- CEO or COO requests arrive through Meera and become `CS` tasks.
- Customer messages and feedback files are placed in `workspace/confluence/research/` and turned into tasks by Arnav.
- Sales hands off each new customer with a note to Swati.
- Release notes from Product trigger a content-freshness check by Meghna.

## Severity levels

| Level | Meaning | Response target |
|---|---|---|
| S1 | Product down, data loss or security/privacy concern for a customer | Escalate to Swati and Rajeev Sharma at once |
| S2 | Core workflow broken for a customer, no workaround | Escalate to Swati same day |
| S3 | Problem with a workaround, or how-to question | Arnav handles within the day |
| S4 | Cosmetic issue, feature request, general feedback | Batch for Yusuf |

## Escalation paths

- Anything outside approved answers, refunds, credits, policy questions: Arnav → Swati.
- Bugs: reproducible report → `ENG` task → Divya Krishnan (QA) and Rahul Venkatesh's team.
- Product gaps: Yusuf or Swati → `PROD` task → Priya Nair.
- Privacy, data requests, legal threats, security: → Rajeev Sharma immediately.
- Any message to a real customer: → approval file → CEO.

## Approved answers

Arnav may answer only from this list. Swati adds entries; each entry has a date and source.

| Question | Approved answer | Source | Added |
|---|---|---|---|
| _(empty until products launch)_ | | | |

## Feedback taxonomy

Type: bug · request · confusion · praise · churn signal · other/new.
Area: onboarding · core workflow · billing · performance · integrations · account · other.

## Customer health score

Owned by Pallavi Jain. Definition goes here once agreed with Siddharth Rao: signals, weights, thresholds, last back-test date.

## Hand-offs

| From | To | What |
|---|---|---|
| Arnav | Yusuf | Tagged tickets for clustering |
| Arnav | Meghna | Repeat how-to questions |
| Yusuf | Priya Nair | `PROD` tasks with counts and quotes |
| Pallavi | Swati | Risk flags with interventions |
| Meghna | Karthik Subramanian | Flows too confusing to document |

## Review gates

- Every customer-facing draft is reviewed by Swati, then approved by the CEO before it goes out.
- Help content is checked against current product behavior before publishing.
- Health-score changes are back-tested before use.

## Recurring rituals

- **Daily:** triage of new `CS` tasks; S1/S2 review.
- **Weekly:** feedback cluster report (Yusuf); escalation review (Swati); input to the Growth & Customer review.
- **Monthly:** customer health report (Pallavi); content freshness check (Meghna).

## Definition of done

- Task has owner, severity, outcome and links.
- Customer communication approved before sending.
- Product-impacting issues linked to a `PROD` or `ENG` task.
- Status set to Closed and the log updated.
