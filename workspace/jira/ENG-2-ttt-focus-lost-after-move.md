---
key: ENG-2
title: Tic-tac-toe: keyboard focus is lost after every move
type: bug
product: Tic-Tac-Toe
status: In Review
category: In Review
priority: P3
owner: frontend-engineer-1
reporter: qa-functional
created: 2026-10-24
due:
links: [workspace/jira/ENG-1-tic-tac-toe.md, products/tic-tac-toe/index.html]
---

## Goal
Keyboard and screen-reader users keep their place on the board after a move.

## Details
Severity: S4 low (usability, workaround exists). Priority: P3. Found by code-trace (not executed in a browser; reproduce in a browser before fixing).

Steps:
1. Open index.html. Tab to Cell 1, press Enter.
2. Press Tab again.

Expected: focus stays on the board (or moves to the next cell).
Actual (expected from code): `render()` sets `disabled = true` on the played cell. Browsers drop focus from a disabled button, so focus resets to the page start. Every move forces the user to Tab through the page again. Same after a win or draw: all cells become disabled.

Impact: keyboard-only play is slow and tiring; does not break the acceptance criterion "keyboard-operable buttons".

Suggested fix (for Sneha to decide): use `aria-disabled` plus the guard in `play()` instead of `disabled`, or move focus to the Restart button at game end.

## Acceptance criteria
- [ ] After a move, focus stays within the board.
- [ ] Occupied cells and finished-game cells still reject input.

## Notes / log
- 2026-10-24 · qa-functional (Divya): Filed from ENG-1 QA pass.
- 2026-10-24 · frontend-engineer-1 (Sneha): Fix: render() now sets aria-disabled instead of disabled on cells; CSS selector changed to .cell[aria-disabled="true"]. play() already rejects occupied/finished moves. Not run in a browser or node (not reproduced or re-verified); QA to retest focus. Acceptance boxes left unticked.
