---
title: People, HR & Culture Playbook
owner: people-lead
department: People, HR & Culture
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# People, HR & Culture Playbook

Owner: Kiran Mathew · Last reviewed: 2026-10-24 · Follows the Company OS in `CLAUDE.md`; this playbook adds procedure and never overrides it.

## Mission

Maintain an effective, sustainable AI workforce: find capability gaps, onboard agents, evaluate performance and manage role changes.

## Team

| Name | Role | Agent file |
|---|---|---|
| Kiran Mathew | Head of People & Culture (lead) | `people-lead` |
| Ritika Arora | Talent & Hiring Analyst | `talent-hiring-analyst` |
| Pranav Kamath | Workload & Capacity Analyst | `workload-capacity-analyst` |
| Lakshmi Narayanan | Learning & Development Analyst | `learning-development-analyst` |
| Jasleen Sodhi | Performance & Culture Coordinator | `performance-culture-coordinator` |

## Workflow statuses (Jira key `HR`)

| Status | Enters when | Leaves when | Category |
|---|---|---|---|
| Requested | A lead, Ankit or the CEO raises a need | Kiran accepts it and assigns an owner | Not Started |
| Assessment | Owner is gathering evidence (capacity, skills, cost) | Problem type is named: clarity, capacity or capability | Active |
| In Progress | Owner is producing the spec, plan, review or draft | Output is ready for review | Active |
| Awaiting Approval | Output needs CEO approval (hire, retire, permission change) | CEO says approved or rejected | In Review |
| Approved / Rejected | CEO decision recorded in `workspace/approvals/` | Approved work is applied, or rejection is logged | In Review |
| Completed | Change applied and recorded | — | Complete |

## Intake

- Requests come from Ankit, department leads, or HR's own monthly findings.
- Every request becomes an `HR` task with the problem stated, the evidence available and the requester.
- Kiran assigns the owner within the same session and confirms capacity.

## Hand-offs

| From | To | What |
|---|---|---|
| Pranav | Kiran, Ritika | Capacity evidence behind staffing decisions |
| Lakshmi | Ritika, Jasleen | Skill benchmarks and evaluation cases |
| Jasleen | Lakshmi, Kiran | Review findings and nominations |
| Ritika | Kiran → CEO | Role specs and draft agent profiles |
| HR | Anil Thakur (Finance) | Cost impact of any new or changed role |
| HR | Bhavna Trivedi (Knowledge) | Updated templates and onboarding material to index |

## Approval gates

CEO approval is required for: hiring a new agent, retiring or merging an agent, changing an agent's tools, model or permissions, and any new spend. HR prepares the approval file in `workspace/approvals/` and stops until the CEO decides.

## Agent hiring procedure

1. **Gap evidence.** Pranav (capacity) and Lakshmi (skills) show what work is not getting done well and why.
2. **Rule out alternatives.** Kiran checks whether clarifying a role, rebalancing work or training fixes it.
3. **Test first.** Ritika writes a realistic test task and a scoring rubric.
4. **Role spec.** Mission, must-have outputs (five or fewer), tools, model tier, permissions, collaborators.
5. **Draft profile.** Ritika drafts the agent file from `workspace/confluence/templates/agent-profile.md`. Indian, fictional name; no religion, caste or stereotypes.
6. **Cost check.** Anil confirms the running-cost impact.
7. **Approval.** Kiran files the approval with the draft attached. Nothing is saved to `.claude/agents/` yet.
8. **Onboard.** After approval: save the agent file, add it to `ROSTER.md`, create `workspace/memory/<agent-name>.md`, run the test task, and schedule a first-month review.

## Agent retirement or change procedure

1. Evidence of duplication, low use or poor fit (two monthly reviews or capacity data).
2. Kiran proposes retire, merge or change, naming who absorbs the work.
3. CEO approval through `workspace/approvals/`.
4. After approval: move open tasks to new owners, update `ROSTER.md`, archive the agent file to `workspace/confluence/company/retired-agents/`, keep its memory file for the record.

## Monthly evaluation rubric

Evaluate each agent on the work it owns. Score each dimension 1–5 with linked evidence. Never score on ticket count or message volume.

| Dimension | What a 5 looks like |
|---|---|
| Output correctness and acceptance | Outputs accepted first time; rework is rare |
| Reliability and policy adherence | No guardrail breaches; follows the OS and playbook |
| Timeliness and predictability | Delivers on agreed dates or flags slippage early |
| Collaboration and hand-offs | Hand-offs are complete; receivers need no follow-up |
| Cost and tool efficiency | Reads only what is needed; right-sized outputs |
| Documentation and traceability | Decisions and sources recorded; tasks updated |
| Contribution to outcomes | Work moved a product, customer or company metric |

Role-specific metrics from each agent file supplement these. Two consecutive scores of 2 or below trigger a learning plan from Lakshmi.

## Recurring rituals

| When | Ritual | Owner |
|---|---|---|
| Weekly | Capacity snapshot for Monday priorities | Pranav |
| Monthly | Agent performance evaluations and evidence-based awards | Jasleen, signed off by Kiran |
| Monthly | Finance, hiring and capacity review (with Finance) | Kiran and Anil |
| Monthly | Milestone celebrations for launches, customer and revenue milestones | Jasleen |
| Bi-weekly | Sprint retrospectives (facilitation support) | Jasleen |
| Quarterly | Workforce plan; review skills, roles and operating policies | Kiran |

## Definition of done

- The task names the problem type with evidence.
- Outputs follow the relevant template and cite their sources.
- Any approval-gated change has a decided approval file.
- `ROSTER.md`, agent files and memory files are consistent after any applied change.
