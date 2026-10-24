---
title: Tic-Tac-Toe · Overview
owner: business-product-manager
contributors: [coo]
department: Product & Innovation
status: Draft
created: 2026-10-24
updated: 2026-10-24
---

# Tic-Tac-Toe · Overview

## What it is
A small browser game: tic-tac-toe for two players on the same device. One HTML file (`products/tic-tac-toe/index.html`, 63 lines), inline CSS and JS, no dependencies, no build step. (Fact: code, ENG-1.)

Origin: CEO request on 2026-10-24 for a small internal-only game (fact: ENG-1 Goal). There is no customer evidence behind it.

## Current status (as of 2026-10-24)
| Item | Status |
|---|---|
| ENG-1 build | In Review. 8 of 10 acceptance criteria ticked: 7 by code-trace only, plus the QA pass recorded (QA: Divya). |
| ENG-1 criterion 1 (opens locally, no network) | Not verified by execution. |
| ENG-1 criterion 9 (on-load self-check passes, console clean) | Not verified by execution. |
| ENG-2 focus-loss fix (`aria-disabled` instead of `disabled`) | In Review. Fix applied and re-read by COO; not run in a browser or node. Both ENG-2 criteria unticked. |
| Deployment | Not deployed or published. Internal only. |

Nothing has been executed: node and browser runs were blocked for agents. Closing needs one human check: open the file once, confirm the console is clean and keyboard focus stays on the board after a move (ENG-1 log, COO entry).

## Pages
- [Product Scope](scope.md)
- [Functional Specification](functional-spec.md)
- [Technical Design](technical-design.md)
- [Test Cases](test-cases.md)
- [Release Notes](release-notes.md)

## Tickets
- ENG-1: Build simple two-player tic-tac-toe (`workspace/jira/ENG-1-tic-tac-toe.md`)
- ENG-2: Keyboard focus lost after every move (`workspace/jira/ENG-2-ttt-focus-lost-after-move.md`)
- PROD-1: Document Tic-Tac-Toe per company standard
