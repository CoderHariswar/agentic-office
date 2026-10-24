---
title: Sales & Partnerships Playbook
owner: sales-lead
department: Sales & Partnerships
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Sales & Partnerships Playbook

**Owner:** Sameer Bhatia (Sales Lead) · **Version:** 1.0 · **Applies under:** Company OS in `CLAUDE.md`. This playbook adds procedure; it never overrides company rules.

## Mission

Turn qualified demand into customers, partnerships and predictable revenue, spending effort only where there is real fit.

## Team

| Name | Role | Agent file |
|---|---|---|
| Sameer Bhatia | Sales Lead | `sales-lead` |
| Nandini Prasad | Prospect Researcher | `prospect-researcher` |
| Abhishek Pandey | Lead Qualification Agent | `lead-qualification` |
| Simran Kaur | Outreach & Follow-up Agent | `outreach-followup` |
| Raghav Saxena | Demo & Proposal Agent | `demo-proposal` |
| Prachi Patil | CRM & Pipeline Analyst | `crm-pipeline-analyst` |

## Workflow statuses

Jira key: `SALES`. Deals live in `workspace/confluence/sales/pipeline/register.md`; work on them is tracked as `SALES` tasks.

| Status | Enters when | Exits when | Shared category |
|---|---|---|---|
| Lead Identified | Nandini records a prospect with sources and fit score | Abhishek completes qualification | Not Started |
| Qualified | Scoring table complete with recommendation "pursue" | First outreach approved by the CEO | Active |
| Outreach | Approved messages are in progress | Prospect agrees to a meeting, or the sequence ends | Active |
| Meeting | A meeting or demo is scheduled or held | Buyer asks for a proposal, or deal is lost | Active |
| Proposal | Raghav is preparing or has delivered a proposal | Buyer responds with terms or a decision | In Review |
| Negotiation | Terms, pricing or contract under discussion | Signed (Won) or declined (Lost) | In Review |
| Won / Lost | Outcome confirmed by the deal owner | Won: handed to Customer Success. Lost: reason recorded | Complete |

Stalled deals (no next step or no movement in 14 days) set `category: Blocked` with the reason.

## Qualification standard

Abhishek scores every lead on five criteria: **fit** (matches the ideal customer profile), **need** (a stated or evidenced problem we solve), **urgency** (a trigger or deadline), **budget signals** and **decision process** (who decides and how). Each is strong, partial, none or unknown.

- **Pursue:** fit strong and at least two others strong or partial.
- **Nurture:** fit strong but need or urgency unknown.
- **Drop:** fit weak or none.

The ideal customer profile per product lives in `workspace/confluence/sales/plan-<product>.md`, owned by Sameer.

## Intake

- **From the CEO or Meera:** routed to Sameer, who creates a `SALES` task.
- **From Marketing:** inbound leads go to Abhishek for qualification.
- **From Product Managers:** PMs may create `SALES` tasks (for example, a pilot customer search); Sameer assigns the owner.

## Standard flow and handoffs

1. Nandini researches prospects from permitted public sources.
2. Abhishek qualifies and hands "pursue" leads to Simran with context.
3. Simran drafts outreach and files the CEO approval request. Nothing is sent before approval.
4. Interested prospects go to Raghav for the demo and proposal.
5. Raghav confirms capability claims with Priya Nair and pricing with Hemant Goyal.
6. Prachi keeps the register current and reports weekly.
7. Won deals go to Swati Chaturvedi (Customer Success) with a context note. Lost deals record the reason.

## Review and approval gates

| Gate | Who | What is checked |
|---|---|---|
| Qualification | Abhishek, Sameer for borderline cases | Score and recommendation |
| Outreach | **CEO** | Every message to a real person, filed in `workspace/approvals/` |
| Capability claims | Priya Nair (Business PM) | Only shipped features presented as available |
| Pricing within range | Sameer with Hemant Goyal | Margin and consistency |
| Pricing outside range, custom terms | **CEO** | Filed in `workspace/approvals/` |
| Contract language | Aparna Bhattacharya, with qualified human counsel for material terms | Terms, liability, data processing |

## Rules specific to Sales

- Prospect data comes only from permitted public sources. No personal contact details, no bought lists without CEO approval.
- Respect consent, anti-spam rules and opt-outs. Check `workspace/confluence/sales/opt-outs.md` before any outreach. Opt-outs are permanent.
- Never promise features, dates or terms that Product and the CEO have not approved.
- Forecasts state their basis and confidence.

## Recurring rituals

| When | Ritual | Owner |
|---|---|---|
| Weekly | Pipeline hygiene report | Prachi |
| Weekly | Pipeline review and forecast | Sameer |
| Weekly | Growth & Customer review (with Marketing and Customer Success) | Sameer |
| Monthly | Win/loss review and ideal customer profile update | Sameer |

## Definition of done (Sales task)

- Acceptance criteria met; outputs saved in `workspace/confluence/sales/`.
- Pipeline register updated with stage, next step, date and owner.
- Approvals filed for any outreach, pricing exception or terms.
- Handoffs made with context notes.
- Task status, category and log updated.
