---
key: ENG-1
title: Build simple two-player tic-tac-toe (single HTML file)
type: story
product: Tic-Tac-Toe
status: In Review
category: In Review
priority: P2
owner: frontend-engineer-1
reporter: coo
created: 2026-10-24
due: 2026-10-24
links: [products/tic-tac-toe/index.html]
---

## Goal
CEO request (2026-10-24): a small browser tic-tac-toe game for two players on the same device. Single HTML file, no dependencies, no build step. Internal only: do not deploy or publish.

## Acceptance criteria
- [ ] Opens in a modern browser from a local file (`products/tic-tac-toe/index.html`), no network needed.
- [x] Two players alternate X and O on a 3x3 board; X starts. (code-trace)
- [x] Shows whose turn it is at all times during play. (code-trace)
- [x] Detects a win on all 8 lines and announces the winner. (code-trace)
- [x] Detects a draw (full board, no winner) and announces it. (code-trace)
- [x] No moves accepted after the game ends; occupied cells cannot be overwritten. (code-trace)
- [x] Restart button clears the board and returns to X's turn. (code-trace)
- [x] Basic accessibility: cells are keyboard-operable buttons; status is announced to screen readers. (code-trace; see ENG-2 for focus loss)
- [ ] Built-in self-check of win/draw logic (console asserts, runs on load) passes with no errors.
- [x] QA functional pass recorded below.

## Not in scope
Deploy, publishing, AI opponent, online play, scores across games, analytics.

## Notes / log
- 2026-10-24 · coo (Ankit): Task created from CEO request. Routed to CTO for assignment.
- 2026-10-24 · cto (Rahul): Assigned build to frontend-engineer-1 (Sneha Pillai, UI & accessibility); QA to qa-functional. Path confirmed: `products/tic-tac-toe/index.html`. Guidance: MVP-class, not core platform, so no ADR. One file, inline CSS/JS, vanilla JS, no dependencies or CDN links. Board state as a 9-item array; one pure `winner(board)` function checking the 8 lines, returning 'X' | 'O' | 'draw' | null. Cells are `<button>`s with aria-labels; status in an `aria-live="polite"` region. Add a small `console.assert` self-check of `winner()` (row, column, diagonal, draw, in-progress) that runs on load. Est. 0.5–1 hr build, 0.5 hr QA.
- 2026-10-24 · frontend-engineer-1 (Sneha): Built `products/tic-tac-toe/index.html` (63 lines, one file, no deps). 9-item board, pure `winner()`, button cells with aria-labels, aria-live status, Restart, on-load console.assert self-check (5 cases). Mobile-first grid, focus-visible outlines. NOT run: node execution was blocked by permissions, so logic is verified by reading only; a harness exists at scratchpad t.js (stubbed DOM) for QA/Rahul to run. Not browser-tested or keyboard-tested. Moved to In Review; QA criterion left unticked.
- 2026-10-24 · qa-functional (Divya): QA pass. METHOD: code-trace only. Running the harness (node t.js) was blocked by permissions (needs approval); no browser run. Results per criterion:
  - Opens locally, no network: NOT VERIFIED by execution. Trace: no external links/scripts. Left unticked.
  - Alternate X/O, X starts: PASS (reset sets turn='X'; play flips turn).
  - Turn display: PASS (render sets "X's turn"/"O's turn" every render).
  - 8 win lines: PASS. LINES has 3 rows, 3 columns, 2 diagonals, all indices correct. Win on 9th move: PASS, winner() checks lines before the full-board draw test, so a winning last move shows the win.
  - Draw: PASS (full board, no line, returns 'draw'; hand-checked the self-check draw board against all 8 lines).
  - No moves after end / no overwrite: PASS (cells disabled, and play() also guards board[i] and winner()).
  - Restart: PASS (new array, turn='X', render re-enables all cells).
  - Accessibility: PASS with defect. Cells are native buttons with aria-labels, status is aria-live=polite. DEFECT ENG-2 (S4 low, P3): disabling the clicked cell drops keyboard focus to page start after every move.
  - Self-check asserts on load: all 5 cases hand-traced as correct, NOT VERIFIED by execution. Left unticked.
  - RECOMMENDATION: ACCEPT with conditions. No high-severity defects. Before close, someone with node/browser access should run `node <scratchpad>/t.js products/tic-tac-toe/index.html` and open the file once to confirm criteria 1 and 9 (console clean). ENG-2 may be fixed or deferred at Rahul/Priya's call. Status left In Review for COO to close.
- 2026-10-24 · coo (Ankit): ENG-2 focus fix applied by frontend-engineer-1 (cells use aria-disabled; play() still guards). COO re-read diff: correct. Not closed: criteria 1 and 9 need one execution check (node/browser blocked for agents). Stays In Review pending CEO opening the file once. Not deployed or published.
