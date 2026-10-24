---
title: Tic-Tac-Toe · Technical Design
owner: frontend-engineer-1
contributors: [cto]
department: Engineering & Quality
status: Approved
created: 2026-10-24
updated: 2026-10-24
---

# Tic-Tac-Toe · Technical Design

Tickets: ENG-1 (`workspace/jira/ENG-1-tic-tac-toe.md`, build), ENG-2 (`workspace/jira/ENG-2-ttt-focus-lost-after-move.md`, focus fix).
Related pages: [Functional Specification](functional-spec.md), [Test Cases](test-cases.md).
Code: `products/tic-tac-toe/index.html` (63 lines). Line numbers below refer to that file as of 2026-10-24.

## 1. Architecture

- One static HTML file. CSS is inline in `<style>` (lines 7-15), JS inline in one classic `<script>` (lines 22-61).
- No dependencies, no CDN links, no build step, no network requests, no storage (no cookies, localStorage, or URL state). Reloading resets the game.
- Designed to open from a local file (not yet confirmed by execution; see section 6). Internal only; not deployed or published.
- Static markup (lines 18-21): `<h1>`, `<p id="status" aria-live="polite">`, empty `<div id="board">`, `<button id="restart">`. The nine cells are created by JS at load.
- Mobile-first CSS: board is a 3-column grid, `width: min(90vw, 320px)`, square cells via `aspect-ratio: 1`. Restart button has `min-height: 44px`. Visible focus ring via `:focus-visible` (3px `#0057d9`).

## 2. Data model

Two top-level variables (line 35), both set by `reset()`:

| Name | Type | Meaning |
|---|---|---|
| `board` | array of 9 items, each `'X'`, `'O'` or `null` | Index 0-8, row by row (0 1 2 / 3 4 5 / 6 7 8) |
| `turn` | `'X'` or `'O'` | Player to move. X starts. |

Winner/draw is not stored. It is derived each time by `winner(board)`.

## 3. Key functions

| Function (line) | What it does |
|---|---|
| `LINES` (23) | The 8 winning index triples: 3 rows, 3 columns, 2 diagonals. |
| `winner(b)` (24-27) | Pure. Returns `'X'` or `'O'` if a line is held by one player, else `'draw'` if all 9 cells are filled, else `null`. Lines are checked before the full-board test, so a win on the 9th move is a win, not a draw. |
| `$` (36) | Helper: `id => document.getElementById(id)`. |
| `render()` (37-45) | Sets the status text ("X's turn", "O's turn", "X wins!", "It's a draw!"). For each of the 9 existing cell buttons: sets text to the mark (or empty), sets `aria-disabled` to true if the cell is filled or the game is over, and sets `aria-label` to `Cell N, X|O|empty` (N is 1-9). Does not recreate buttons. |
| `play(i)` (46-51) | Ignores the move if `board[i]` is filled or `winner(board)` is non-null. Otherwise writes `turn` into the cell, flips `turn`, calls `render()`. |
| `reset()` (52) | New empty array, `turn = 'X'`, `render()`. Also used for the initial render (line 60). |
| Cell creation loop (53-58) | Creates 9 `<button type="button" class="cell">`, binds `onclick = () => play(i)`, appends to `#board`. Runs once. |
| Restart wiring (59) | `$('restart').onclick = reset`. |

## 4. On-load self-check (lines 28-33)

Five `console.assert` calls run on load against `winner()`. A failure prints an "Assertion failed" message to the console; it does not stop the page.

| # | Label | Input board | Expected |
|---|---|---|---|
| 1 | row | `X X X / . O O / . . .` | `'X'` |
| 2 | column | `O X . / O X . / O . .` | `'O'` |
| 3 | diagonal | `X O . / O X . / . . X` | `'X'` |
| 4 | draw | `X O X / X O O / O X X` | `'draw'` |
| 5 | in progress | `X . . / . O . / . . .` | `null` |

Coverage is partial: one row, one column, one diagonal (the 0-4-8 one; the 2-4-6 line is not asserted).

## 5. Decisions

| Decision | Reason | Source |
|---|---|---|
| Single file, inline CSS/JS, vanilla JS, no dependencies or CDN | Smallest thing that meets "no build, no network"; CTO guidance | ENG-1 log, Rahul, 2026-10-24 |
| No ADR | MVP-class, not core platform | ENG-1 log, Rahul |
| Board as a 9-item array | Simple index-to-cell mapping; CTO guidance | ENG-1 log, Rahul |
| One pure `winner(board)` returning `'X' \| 'O' \| 'draw' \| null` | Testable without the DOM; single source of truth for game end | ENG-1 log, Rahul |
| Cells are native `<button>`s with `aria-label`s | Keyboard operable by default (native HTML before custom widgets) | ENG-1 log, Rahul |
| Status in `aria-live="polite"` region | Screen readers hear turn and result changes | ENG-1 log, Rahul |
| Console-assert self-check of `winner()` on load | Cheap regression check with no test runner | ENG-1 log, Rahul |
| `aria-disabled` instead of `disabled` on cells | Per the ENG-2 report (not re-tested), `disabled` made browsers drop keyboard focus to page start after every move. `aria-disabled` keeps the button focusable; `play()` still rejects occupied or finished-game moves, so behaviour is unchanged for input. CSS targets `.cell[aria-disabled="true"]` (line 11). | ENG-2 |

## 6. Limits and known issues

Verification status (fact, as of 2026-10-24):
- The file has not been executed in node or in a browser. QA (Divya) verified by code-trace only.
- ENG-1 criterion 1 (opens locally, no network) and criterion 9 (self-check passes with no console errors) are unverified by execution.
- The ENG-2 fix has not been re-tested. Focus retention after a move, and rejection of input on filled or finished cells, still need a browser check. ENG-2 acceptance boxes are unticked.
- No keyboard-only or screen-reader run has been done.

Limits seen in the code (fact, from reading):
- `aria-disabled` does not stop events. Filled cells remain tab stops and Enter/Space still fire `onclick`; only the `play()` guard blocks them. Removing that guard would break the game.
- Filled cells give no visual "disabled" styling beyond `cursor: default` (line 11; the `color: #111` there matches body text and is not a disabled cue). The mark itself is the cue.
- Self-check asserts only log; they do not block or show anything on the page. Diagonal 2-4-6 is not asserted.
- `board`, `turn`, `LINES`, `winner`, `render`, `play`, `reset` and `$` are globals of a classic script. Fine for one page; not safe to reuse in a larger page.
- The initial status text is set by JS on load; whether a screen reader announces it on first load is not tested (hypothesis: usually not announced, which is acceptable).
- No win-line highlight, scores, undo, AI or persistence. Out of scope per ENG-1.
- Behaviour on old browsers is untested. Uses `aspect-ratio`, `min()`, `:focus-visible`, spread, destructuring and arrow functions (modern browsers only).
- No frontend test file exists; the only test is the on-load self-check.

## 7. Review

- Reviewer: cto (Rahul Venkatesh), 2026-10-24.
- Verdict: Approved as an accurate description of the code. Checked against `products/tic-tac-toe/index.html` (63 lines): all line ranges, `LINES`, function behaviour, the five self-check cases (draw board re-checked: no line held) and the decisions match the code and the ENG-1 CTO guidance. No invented features. Approval covers the document only; it does not verify the product.
- Changes made: (1) "Opens from a local file" restated as designed-to, unconfirmed, since criterion 1 is unexecuted. (2) ENG-2 `disabled` focus-loss reason marked as per the ENG-2 report, not re-tested. (3) Noted that `color: #111` on line 11 is not a disabled cue. (4) Removed reference to a "node harness" that is not part of the code or this page.
- Still open (product, not page): one execution check, opening the file in a browser with the console visible, to close ENG-1 criteria 1 and 9 and retest ENG-2 (focus retention, rejection of input on filled or finished cells). Add the 2-4-6 diagonal assert when next touching the file.
