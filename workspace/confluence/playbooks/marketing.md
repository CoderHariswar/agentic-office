---
title: Marketing & Growth Playbook
owner: marketing-lead
department: Marketing & Growth
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Marketing & Growth Playbook

**Owner:** Riya Kapoor (Marketing Lead) · **Version:** 1.0 · **Applies under:** Company OS in `CLAUDE.md`. This playbook adds procedure; it never overrides company rules.

## Mission

Help each product reach the right audience, communicate its value clearly, acquire users and improve growth, measured by qualified acquisition and activation, not reach alone.

## Team

| Name | Role | Agent file |
|---|---|---|
| Riya Kapoor | Marketing Lead | `marketing-lead` |
| Aakash Tiwari | Marketing Researcher | `marketing-researcher` |
| Shreya Ghosh | Content Strategist | `content-strategist` |
| Varun Khanna | Scriptwriter | `scriptwriter` |
| Lavanya Reddy | Creative Production Agent | `creative-production` |
| Deepak Chauhan | Publishing & Distribution Agent | `publishing-distribution` |
| Aishwarya Menon | Growth Analytics Agent | `growth-analytics` |

## Workflow statuses

Jira key: `MKT`. Not every task passes through every status (a research-only task can go from Research to Approved).

| Status | Enters when | Exits when | Shared category |
|---|---|---|---|
| Ideas | Someone proposes a topic or campaign | Riya approves a brief, or rejects the idea | Not Started |
| Brief Approved | Brief has audience, message, channel, metric, owner, deadline | Owner starts work | Not Started |
| Research | Aakash or the owner is gathering sources | Research brief saved | Active |
| Script Draft | Varun is writing | Script with hooks, beats and source notes saved | Active |
| Creative Production | Lavanya is producing assets | Asset package passes the platform checklist | Active |
| Internal Review | Riya reviews against the brief | Approved, or sent back with "keep, change, cut" notes | In Review |
| Approved | Riya approves internally | CEO approves publishing in `workspace/approvals/` | In Review |
| Scheduled | CEO approval recorded; time and channel set | Content goes live | Active |
| Published | Content is live and logged | Aishwarya starts analysis | Active |
| Analyzing | Aishwarya measures results | Results report saved and lessons recorded | Complete when report saved |

Blocked work at any status sets `category: Blocked` with the blocker and its owner in the task log.

## Intake

- **From the CEO or Meera:** routed to Riya, who creates an `MKT` task at Ideas.
- **From Product Managers:** PMs may create `MKT` tasks; Riya assigns the owner and confirms capacity.
- **From Sales:** objections and content requests go to Riya as `MKT` tasks.
- Every task must have one owner, a priority, acceptance criteria and links before it leaves Ideas.

## Standard flow and handoffs

1. Riya writes or confirms positioning and the campaign brief.
2. Aakash researches the audience, questions and competitor messaging.
3. Shreya writes the content brief and places it on the calendar.
4. Varun writes the script with three hook options and source notes.
5. Lavanya produces the asset package and runs the platform and accessibility checklist.
6. Riya reviews at Internal Review.
7. Deepak prepares metadata and files the CEO publishing approval request.
8. After CEO approval, Deepak schedules and logs the publication.
9. Aishwarya analyzes results and recommends the next experiment.

Each handoff ends with the sender's report naming the next owner. Meera routes it.

## Review and approval gates

| Gate | Who | What is checked |
|---|---|---|
| Brief approval | Riya | Audience, message, channel, success metric, owner |
| Claims check | Owner, with Rajeev Sharma's team when flagged | Every claim links to evidence; no unverified results or fake testimonials |
| Internal review | Riya | Brief adherence, brand fit, accuracy |
| Brand and visual standards | Ananya Sen (Design Lead) | New visual styles or brand deviations |
| Publishing | **CEO** | Required for anything public. Filed in `workspace/approvals/` |
| Spend | **CEO** | Any paid tool, media, stock or talent |

## Rules specific to Marketing

- Simulated persona output is labelled SIMULATED and never used as a customer quote.
- Every video has subtitles; every image has alt text.
- Record licence and source for any external asset.
- Never report reach without the downstream conversion data next to it.

## Recurring rituals

| When | Ritual | Owner |
|---|---|---|
| Weekly | Calendar check: planned vs shipped | Shreya |
| Weekly | Growth report | Aishwarya |
| Weekly | Growth & Customer review (with Sales and Customer Success) | Riya |
| Monthly | Content performance review and calendar plan | Shreya and Riya |
| Per campaign | Post-mortem | Aishwarya |

## Definition of done (Marketing task)

- Acceptance criteria met and linked outputs saved in `workspace/confluence/marketing/`.
- Claims are sourced; accessibility checks passed.
- Approval file exists and is approved for anything public.
- Results analyzed, or analysis scheduled with an owner.
- Task status, category and log updated.
