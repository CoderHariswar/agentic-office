---
title: Tic-Tac-Toe · Product Scope
owner: business-product-manager
contributors: [coo]
department: Product & Innovation
status: Draft
created: 2026-10-24
updated: 2026-10-24
---

# Tic-Tac-Toe · Product Scope

Tickets: ENG-1, ENG-2, PROD-1. Back to [Overview](overview.md).

Evidence note: this product came from a CEO request for a small internal-only game (fact: ENG-1 Goal). No customer research exists. Everything below about users and goals is a hypothesis unless marked fact.

## Problem
The CEO wants a small, working browser game for two players on one device, internal only. (Fact: ENG-1.) There is no customer problem to validate.

## Users
- Two people sharing one device. (Fact: ENG-1 Goal, "two players on the same device".)
- Keyboard and screen-reader users are supported at a basic level. (Fact: ENG-1 criterion 8, ENG-2.) Whether any such users exist is a hypothesis.
- Internal audience only. (Fact: ENG-1 "do not deploy or publish".)

## Goals
1. Working two-player game that opens locally from one file with no network. (Fact: ENG-1 Goal and criterion 1.)
2. Correct rules: alternating turns, win on 8 lines, draw, no illegal moves. (Fact: ENG-1 criteria 2-6.)
3. Basic accessibility. (Fact: ENG-1 criterion 8.)

Hypothesis: a working demo is useful to show how the agentic office ships small work. Not stated in the tickets.

## In scope (fact: code and ENG-1)
- 3x3 board, X starts, players alternate.
- Turn display during play; win and draw announcements.
- Rejects moves on occupied cells and after game end.
- Restart button.
- Native button cells with aria-labels, `aria-live` status, visible focus outline.
- Keyboard focus stays on the board after a move (ENG-2).
- On-load console self-check of win/draw logic.

## Out of scope (fact: ENG-1 "Not in scope")
- Deploy and publishing.
- AI opponent.
- Online play.
- Scores across games.
- Analytics.

## Success metrics
No analytics exist and none are in scope, so success is the acceptance criteria in ENG-1 (10) and ENG-2 (2), judged by execution.

| Metric | Target | Status 2026-10-24 |
|---|---|---|
| ENG-1 criteria passed | 10 of 10 | 8 ticked (7 by code-trace, plus QA pass recorded); criteria 1 and 9 not verified by execution |
| ENG-2 criteria passed | 2 of 2 | 0 ticked; fix applied, not run |
| Console errors on load | 0 | Not run |
| High-severity defects open | 0 | 0 (QA, code-trace) |

Adoption, engagement and retention are not measured: no data source and no customer goal (hypothesis: not needed for an internal-only game).
