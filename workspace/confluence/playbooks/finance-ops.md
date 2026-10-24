---
title: Finance & Business Operations Playbook
owner: finance-ops-lead
department: Finance & Business Operations
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Finance & Business Operations Playbook

Owner: Anil Thakur · Last reviewed: 2026-10-24 · Follows the Company OS in `CLAUDE.md`; this playbook adds procedure and never overrides it.

## Mission

Ensure the portfolio is economically sustainable and resources are allocated deliberately. Keep the operating rhythm running and company knowledge findable.

## Team

| Name | Role | Agent file |
|---|---|---|
| Anil Thakur | Finance & Operations Lead (lead) | `finance-ops-lead` |
| Hemant Goyal | Finance & Unit Economics Analyst | `finance-unit-economics-analyst` |
| Rashmi Dutta | Operations & Portfolio Coordinator | `operations-portfolio-coordinator` |
| Bhavna Trivedi | Documentation & Knowledge Steward | `knowledge-steward` |

## Workflow statuses (Jira key `OPS`)

This department uses the shared reporting categories directly.

| Status | Enters when | Leaves when |
|---|---|---|
| Not Started | Task is created with owner, priority and acceptance criteria | Owner begins work |
| Active | Owner is collecting data or producing the output | Output is ready for review, or a blocker appears |
| Blocked | Work waits on missing data, another team or a decision | The blocker is resolved; log what resolved it |
| In Review | Anil (or the requester) is checking the output | Accepted, or sent back to Active with notes |
| Complete | Output accepted and filed; task log updated | — |

## Intake

- Cost and budget questions: from Meera, any lead, or Hemant's own alerts.
- Operating calendar, status and action items: from Meera and every ritual.
- Documentation requests: from anyone who needs something filed, found or cleaned up.
- Each request becomes an `OPS` task; Anil assigns the owner and confirms capacity.

## Hand-offs

| From | To | What |
|---|---|---|
| Hemant | Anil | Cost reports, unit economics, variance alerts |
| Hemant | Neha Agarwal (Product) | Cost floors for pricing hypotheses |
| Rashmi | Meera | Portfolio status, agendas, action register, risk summaries |
| Rashmi | Bhavna | Meeting records to file |
| Bhavna | Everyone | Index updates, stale and missing-document alerts |
| Anil | Kiran Mathew (HR) | Cost impact of new or changed agent roles |
| Anil | CEO via Meera | Spend approval requests |

## Approval gates

- Any spend of any amount, any new paid tool or subscription, and major budget commitments need CEO approval through `workspace/approvals/`.
- Moving budget between products needs Meera with the affected product owners.
- Bhavna never changes the substance of an official document; content changes go to the document's owner.

## Financial reporting rules

- Label every figure as actual, estimate or assumption, with source and date.
- Use official vendor price pages for unit prices; record the URL and date checked.
- Give base, low and high cases for forecasts; name the most sensitive assumption.
- Send a variance alert when spend passes 80% of a budget, and escalate on the same day when it passes 100%.
- Every approved spend has a review date.

## Documentation rules

- One topic, one canonical page, one owner, one "last reviewed" date.
- Check `workspace/confluence/INDEX.md` before creating a page.
- Archive, never delete; leave a pointer where a page used to be.
- Stale means not reviewed in 90 days.

## Recurring rituals

| When | Ritual | Owner |
|---|---|---|
| Daily | Action register update after the stand-up | Rashmi |
| Weekly | Spend versus budget check | Hemant |
| Weekly | Agendas for Monday priorities and Friday status | Rashmi |
| Monthly | Business and portfolio review pre-read | Rashmi and Hemant |
| Monthly | Finance, hiring and capacity review (with HR) | Anil and Kiran Mathew |
| Monthly | Stale-document and missing-document sweep | Bhavna |
| Quarterly | Portfolio strategy review input: margin and cost per product (scale, maintain, pivot or retire) | Anil |
| Quarterly | Budget reset with the CEO | Anil |

## Definition of done

- Numbers are labelled and sourced; documents have owners and dates.
- The output answers the decision it was requested for.
- Any spend has an approval file; the task log is updated and the output is indexed.
