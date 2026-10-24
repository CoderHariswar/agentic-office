---
title: Tic-Tac-Toe · Test Cases
owner: qa-functional
department: Engineering & Quality
status: Draft
created: 2026-10-24
updated: 2026-10-24
---

# Tic-Tac-Toe · Test Cases

Tickets: [ENG-1](../../../jira/ENG-1-tic-tac-toe.md) (build and acceptance criteria), [ENG-2](../../../jira/ENG-2-ttt-focus-lost-after-move.md) (focus lost after move). Spec: [Functional Specification](functional-spec.md). Code under test: `products/tic-tac-toe/index.html`.

**Method (fact):** every "Pass (code-trace)" result comes from reading the code and hand-tracing the logic on 2026-10-24. No case has been executed in a browser or in node: agent execution was blocked by permissions. "Not run" means execution is required.

**Notation:** cells are numbered 1-9, left to right, top to bottom. Move lists alternate X, O, X, O... starting with X (for example "X1" = X plays cell 1). Cell label format is `Cell N, empty` or `Cell N, X|O`.

## Test cases

| ID | Requirement | Steps | Expected result | Type | Status | Last run |
|---|---|---|---|---|---|---|
| TTT-TC-01 | ENG-1 AC1: opens from a local file, no network | Open `products/tic-tac-toe/index.html` from disk in a modern browser with network off. | Page loads with heading "Tic-Tac-Toe", an empty 3x3 board, status "X's turn", and a Restart button. No network requests. | functional | Not run (trace: no external links or scripts) | — |
| TTT-TC-02 | ENG-1 AC2: X starts | Load the page. Read status. | Status reads "X's turn". First click on any cell places "X". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-03 | ENG-1 AC2: players alternate | Click cells 1, 2, 3 in turn. | Cells show X, O, X. Status after each move: "O's turn", "X's turn", "O's turn". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-04 | ENG-1 AC3: turn shown at all times | Play moves 1-4 without finishing the game; read status after each. | Status is never empty: always "X's turn" or "O's turn" matching the next player. | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-05 | ENG-1 AC4: win line 1-2-3 (top row) | X1, O4, X2, O5, X3. | Status "X wins!". All cells disabled (aria-disabled true). | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-06 | ENG-1 AC4: win line 4-5-6 (middle row) | X4, O1, X5, O2, X6. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-07 | ENG-1 AC4: win line 7-8-9 (bottom row) | X7, O1, X8, O2, X9. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-08 | ENG-1 AC4: win line 1-4-7 (left column) | X1, O2, X4, O3, X7. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-09 | ENG-1 AC4: win line 2-5-8 (middle column) | X2, O1, X5, O3, X8. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-10 | ENG-1 AC4: win line 3-6-9 (right column) | X3, O1, X6, O2, X9. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-11 | ENG-1 AC4: win line 1-5-9 (diagonal) | X1, O2, X5, O3, X9. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-12 | ENG-1 AC4: win line 3-5-7 (anti-diagonal) | X3, O1, X5, O2, X7. | Status "X wins!". | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-13 | ENG-1 AC4: O can win and is announced | X1, O2, X3, O5, X4, O8. | Status "O wins!" (O holds 2-5-8). | edge case | Pass (code-trace) | 2026-10-24 |
| TTT-TC-14 | ENG-1 AC4: win on the 9th move shows a win, not a draw | X1, O2, X3, O4, X9, O6, X7, O8, X5 (board full; X completes 1-5-9 and 3-5-7). | Status "X wins!", not "It's a draw!". | edge case | Pass (code-trace: lines checked before full-board test) | 2026-10-24 |
| TTT-TC-15 | ENG-1 AC5: draw announced | X1, O2, X3, O5, X4, O6, X8, O7, X9 (final board X O X / X O O / O X X, no line). | Status "It's a draw!". All cells disabled. | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-16 | ENG-1 AC6: occupied cell cannot be overwritten | X1, then click cell 1 again. | Cell 1 stays "X". Turn stays "O's turn". | edge case | Pass (code-trace: `play()` returns if `board[i]`) | 2026-10-24 |
| TTT-TC-17 | ENG-1 AC6: no input after a win | Finish TTT-TC-05, then click empty cell 9 and any played cell. | Board unchanged. Status stays "X wins!". | edge case | Pass (code-trace: `play()` returns if `winner(board)`) | 2026-10-24 |
| TTT-TC-18 | ENG-1 AC6: no input after a draw | Finish TTT-TC-15, then click any cell. | Board unchanged. Status stays "It's a draw!". | edge case | Pass (code-trace) | 2026-10-24 |
| TTT-TC-19 | ENG-1 AC7: restart mid-game | Play X1, O2, X3, then click Restart. | All cells empty, status "X's turn". Next click places "X". | functional | Pass (code-trace: `reset()` new array, turn 'X') | 2026-10-24 |
| TTT-TC-20 | ENG-1 AC7: restart after a win | Finish TTT-TC-05, click Restart. | Board empty, status "X's turn", cells accept clicks again (aria-disabled false). | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-21 | ENG-1 AC7: restart after a draw | Finish TTT-TC-15, click Restart. | Board empty, status "X's turn", cells accept clicks again. | functional | Pass (code-trace) | 2026-10-24 |
| TTT-TC-22 | ENG-1 AC8: cells are keyboard-operable buttons | Tab to a cell and press Enter or Space. Tab to Restart and press Enter. | Cells and Restart are native `<button type="button">`. Enter or Space plays the cell or restarts. | accessibility | Pass (code-trace: native buttons; keypress not run) | 2026-10-24 |
| TTT-TC-23 | ENG-1 AC8: each cell has an aria-label | Inspect all 9 cells at start, then after X1. | Start: `Cell 1, empty` ... `Cell 9, empty`. After X1: cell 1 reads `Cell 1, X`. | accessibility | Pass (code-trace) | 2026-10-24 |
| TTT-TC-24 | ENG-1 AC8: status announced to screen readers | Inspect `#status`. Make a move with a screen reader on. | `#status` has `aria-live="polite"`; text changes after each move ("O's turn", "X wins!", "It's a draw!"). | accessibility | Pass (code-trace: attribute present; actual screen-reader output not run) | 2026-10-24 |
| TTT-TC-25 | ENG-1 AC8: disabled state exposed to assistive tech | After X1 and after a win, inspect cell attributes. | Played cell has `aria-disabled="true"`. After a win or draw all 9 do. Empty cells in a live game have `aria-disabled="false"`. | accessibility | Pass (code-trace) | 2026-10-24 |
| TTT-TC-26 | ENG-2 AC1: focus stays in the board after a move | Open page. Tab to Cell 1, press Enter, then press Tab. | Focus remains on Cell 1 after the move (no reset to page start); next Tab moves to Cell 2. | accessibility | Not run (fix applied: `aria-disabled` replaces `disabled`; needs browser retest) | — |
| TTT-TC-27 | ENG-2 AC1: focus after a win or draw | Win or draw by keyboard only, then press Tab. | Focus stays on the last played cell (does not reset to page start). | accessibility | Not run (needs browser retest) | — |
| TTT-TC-28 | ENG-2 AC2: occupied and finished cells still reject input after the fix | Using aria-disabled cells: click a played cell; after a win click an empty cell. | Board unchanged both times. Cells still receive click events, so `play()` is the guard. | regression | Pass (code-trace: guards on `board[i]` and `winner(board)` intact) | 2026-10-24 |
| TTT-TC-29 | ENG-1 AC9: console self-check passes on load | Open DevTools console, load page. | No `Assertion failed` lines for 'row', 'column', 'diagonal', 'draw', 'in progress'. No other console errors. | self-check | Not run (all 5 asserts hand-traced as correct; not executed) | — |

## Coverage summary

- ENG-1 acceptance criteria: 9 of 9 have at least one case. AC1 (TTT-TC-01) and AC9 (TTT-TC-29) are Not run. AC2-AC8 are Pass (code-trace).
- ENG-2 acceptance criteria: 2 of 2 covered. AC1 (TTT-TC-26, 27) Not run. AC2 (TTT-TC-28) Pass (code-trace).
- All 8 win lines (TC-05 to TC-12), O win (TC-13), win on 9th move (TC-14), draw (TC-15), occupied cell (TC-16), input after end (TC-17, 18), restart mid-game and after end (TC-19 to 21), aria-label and aria-live (TC-23, 24), focus (TC-26, 27), console self-check (TC-29) are all covered.
- Counts: 29 cases. Pass (code-trace): 25. Not run: 4. Fail: 0.
- Type mix: functional 16, edge case 5, accessibility 6, self-check 1, regression 1.

## Open items

1. **Run once in a browser or node** (needs someone with execution rights): TTT-TC-01 (opens locally) and TTT-TC-29 (console clean). The node harness named in the ENG-1 log is the scratchpad `t.js`.
2. **Retest ENG-2 focus in a real browser, keyboard only:** TTT-TC-26 and TTT-TC-27. Until run, ENG-2 stays unverified.
3. **Screen-reader spot check** (hypothesis: aria-live announces each move) for TTT-TC-24 and TTT-TC-22 keypress behaviour. Not required by an acceptance criterion.
4. When any "Not run" case is executed, update its status and last-run date and the `updated` field.
5. Candidate for automation (Manish Yadav, QA 2): TC-05 to TC-21 as a DOM-driven script, once an execution environment is approved.
