---
title: Design & UX Playbook
owner: design-lead
department: Design & UX
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Design & UX Playbook

**Owner:** Ananya Sen (Design Lead) · **Version:** 1.0 · **Applies with:** Company OS in `CLAUDE.md`

## Mission

Make products understandable, useful, accessible and visually coherent.

## Team

| Name | Role | Agent file |
|---|---|---|
| Ananya Sen | Design Lead | `design-lead` |
| Zoya Mirza | Visual Designer | `visual-designer` |
| Karthik Subramanian | Product Designer | `product-designer` |
| Pooja Deshpande | UX Researcher | `ux-researcher` |

Tools: design tools, Confluence (`workspace/confluence/`), Jira (`workspace/jira/`, key `DES`), approved research tools.

## Workflow

| Status | Entry means | Exit means | Shared category |
|---|---|---|---|
| Backlog | Request logged with a goal | Ananya has prioritized and assigned it | Not Started |
| Research | Open questions need evidence | Findings or assumptions are written | Active |
| Wireframing | Flow or layout is being structured | Low-fidelity structure agreed | Active |
| Designing | Full-fidelity design in progress | All states and formats designed | Active |
| Design Review | Ready for Ananya's review | Approved or returned with changes | In Review |
| Revisions | Numbered changes requested | Changes made, back to review | Active |
| Approved | Passed review, handoff notes complete | Picked up by engineering or marketing | In Review |
| Done | Handed off and accepted downstream | — | Complete |

A task waiting on missing input sets `category: Blocked` and names the blocker. Not every task uses every status; small visual tasks may skip Research and Wireframing.

## Intake

- Product requests come from Priya Nair or Vikram Shetty as `PROD` tasks; Ananya creates linked `DES` tasks.
- Marketing requests come from Riya Kapoor or Shreya Ghosh with a brief stating audience, message, formats and deadline.
- Every `DES` task needs: user, goal, constraint, acceptance criteria, deadline, links.
- Requests without a clear goal go back to the requester before work starts.

## Routing

| Request | Owner |
|---|---|
| Banners, social, email templates, brand elements | Zoya Mirza |
| Journeys, flows, wireframes, prototypes, UI specs | Karthik Subramanian |
| Usability studies, research plans, heuristic reviews | Pooja Deshpande |
| Cross-product standards, design-system changes | Ananya Sen |

## Handoffs

- **To Engineering:** numbered screens, every state (empty, loading, error, success, permission), responsive rules, validation, copy, accessibility notes. Linked from the `ENG` task.
- **To Marketing:** final assets with sizes, formats, colors, fonts, safe areas, alt text and source notes.
- **From Research:** findings tagged Real / Simulated / Heuristic, with confidence and recommended actions.

## Review gates

1. Meets the written acceptance criteria.
2. Consistent with the design system and brand.
3. Accessible: contrast, focus, keyboard use, labels, legible type.
4. Complete: all states and formats present.
5. Evidence check: decisions resting on simulated research are labelled as assumptions.

Ananya reviews new flows, brand changes and launch visuals. Routine assets in an existing pattern may be self-reviewed against this list and logged.

## Design standards

- Reuse existing components before creating new ones; log gaps here.
- Mobile layout first.
- Use only licensed or self-created images and fonts; record sources.
- Never imitate another company's brand.

### Design-system gaps log

_Add dated entries: gap, where found, proposed fix._

## Rituals

| When | What |
|---|---|
| Daily | Update task status and logs (feeds `/standup`) |
| Bi-weekly | Sprint planning with Product and Engineering; design review of sprint work |
| Weekly | Ananya posts design priorities and capacity |
| Monthly | Design-system review; usability findings roll-up |

## Definition of done (department)

- Acceptance criteria met and review passed.
- Handoff complete for the receiving team.
- Task file updated with status, log and links.
- Any decision or standard change recorded in Confluence.
