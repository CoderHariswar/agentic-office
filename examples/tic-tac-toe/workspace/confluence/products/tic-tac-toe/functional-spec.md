---
title: Tic-Tac-Toe · Functional Specification
owner: product-designer
department: Design & UX
status: Draft
created: 2026-10-24
updated: 2026-10-24
---

# Tic-Tac-Toe · Functional Specification

Describes what `products/tic-tac-toe/index.html` (63 lines, one file, no dependencies) does today. Source of truth is the code, read 2026-10-24. Nothing here is a proposal.

- Tickets: ENG-1 (build), ENG-2 (keyboard focus loss after a move).
- Sibling pages: [Product Scope](scope.md), [Technical Design](technical-design.md).

**Verification status (fact vs not verified):**
- FACT (code-read): every behaviour below is traced from the source.
- NOT VERIFIED: nobody has run the file in a browser or node (ENG-1 log: QA and COO were blocked). That covers the ENG-2 focus fix, all keyboard and screen-reader behaviour, and the on-load self-check. Items marked **[unverified]** depend on browser behaviour.

## 1. Features

1. 3x3 board of nine buttons, two players on one device, X always starts.
2. Status line showing whose turn it is, or the result.
3. Win detection on all 8 lines (3 rows, 3 columns, 2 diagonals).
4. Draw detection (board full, no winning line).
5. Moves rejected on occupied cells and after the game ends.
6. Restart button, usable at any time.
7. On-load self-check of the win/draw function (`console.assert`, 5 cases). It only logs to the console and never blocks play.

Not in the code (do not assume): AI opponent, scores, move history, undo, player names, online play, sound, animation, winning-line highlight, persistence.

## 2. Screen layout

Single screen, top to bottom, centred:

| # | Element | Notes |
|---|---|---|
| S1 | Heading `Tic-Tac-Toe` (h1) | Static |
| S2 | Status line (`#status`) | `aria-live="polite"`, min-height 1.5em so layout does not jump |
| S3 | Board (`#board`), 9 cells | Grid 3 columns, 8px gap |
| S4 | `Restart` button (`#restart`) | Always enabled |

Cell order is row by row, left to right: cell 1 top-left, cell 5 centre, cell 9 bottom-right. Tab order follows DOM order: cells 1 to 9, then Restart. **[unverified]**

## 3. Rules

1. X moves first. Players alternate X, O, X, O.
2. A move places the current player's mark in an empty cell, then the turn passes.
3. A player wins by owning all three cells of any of these lines (1-based cell numbers): 1-2-3, 4-5-6, 7-8-9, 1-4-7, 2-5-8, 3-6-9, 1-5-9, 3-5-7.
4. If all nine cells are filled and no line is complete, the game is a draw.
5. The win check runs before the draw check, so a winning 9th move is a win, not a draw.
6. Once the game has a result, no further moves are accepted until Restart.

## 4. States

### Game state (derived on every render from the board)

| State | Condition | Status text |
|---|---|---|
| In progress, X to move | No result, turn = X | `X's turn` |
| In progress, O to move | No result, turn = O | `O's turn` |
| X wins | A line is all X | `X wins!` |
| O wins | A line is all O | `O wins!` |
| Draw | Board full, no line | `It's a draw!` |

On load and after Restart the game is "In progress, X to move" with an empty board.

### Cell state

| State | Content | `aria-disabled` | `aria-label` | Accepts a click |
|---|---|---|---|---|
| Empty, game in progress | blank | `false` | `Cell N, empty` | Yes |
| Occupied (X or O) | `X` or `O` | `true` | `Cell N, X` / `Cell N, O` | No |
| Locked (empty cell, game over) | blank | `true` | `Cell N, empty` | No |
| Occupied, game over | `X` or `O` | `true` | `Cell N, X` / `Cell N, O` | No |

N is 1 to 9. Cells use `aria-disabled`, not the `disabled` attribute (ENG-2 fix). So occupied and locked cells stay focusable and can still be activated; `play()` ignores the activation.

Other states from the standard checklist: loading, error, partial and permission-denied do not exist (no network, no data, no accounts). Empty = the fresh board.

## 5. User flows

All flows start at: page loaded, board empty, status `X's turn`.

### F1. Play a game to a win
1. Player X activates an empty cell. Cell shows `X`, status becomes `O's turn`.
2. Player O activates an empty cell. Cell shows `O`, status becomes `X's turn`.
3. Players alternate until one completes a line.
4. On that move the cell shows the mark, status becomes `X wins!` or `O wins!`, every cell becomes `aria-disabled="true"`.
5. Further cell clicks do nothing. Exit: Restart (F4).

### F2. Play a game to a draw
1. Players alternate as in F1 until the ninth cell is filled with no complete line.
2. Status becomes `It's a draw!`, all cells `aria-disabled="true"`.
3. Further cell clicks do nothing. Exit: Restart (F4).

### F3. Restart mid-game
1. At any point with a game in progress, activate `Restart`.
2. Board clears, turn resets to X, status becomes `X's turn`, all cells `aria-disabled="false"`. Marks already played are discarded; no confirmation prompt.

### F4. Restart after the game ended
1. Activate `Restart` while status shows a result.
2. Same outcome as F3: empty board, `X's turn`, all cells playable again.

## 6. Exact UI text (as in code)

| Where | Text |
|---|---|
| Page title / h1 | `Tic-Tac-Toe` |
| Status, X to move | `X's turn` |
| Status, O to move | `O's turn` |
| Status, win | `X wins!` / `O wins!` |
| Status, draw | `It's a draw!` |
| Cell content | `X`, `O`, or empty |
| Cell aria-label | `Cell N, empty` / `Cell N, X` / `Cell N, O` (format: `Cell ` + number + `, ` + content) |
| Restart button | `Restart` |

The apostrophe in `X's turn` and `It's a draw!` is a straight ASCII apostrophe.

## 7. Edge cases

| # | Case | Behaviour |
|---|---|---|
| E1 | Click an occupied cell | Ignored. Mark and turn unchanged, status unchanged. |
| E2 | Click any cell after the game ended | Ignored (win or draw). Nothing changes. |
| E3 | Winning move is the 9th move | Shown as a win (`X wins!`), not a draw. X is the only player who can make a 9th move, so in practice this is `X wins!`. |
| E4 | Restart pressed on a fresh board | Harmless; board stays empty, `X's turn`. |
| E5 | Rapid double click on an empty cell | Second click lands on an occupied cell and is ignored (E1). |
| E6 | Keyboard activation (Enter/Space) on a cell with `aria-disabled="true"` | Button still fires click; `play()` guards, so no change. **[unverified]** |
| E7 | Page reload | Game is lost; nothing is stored. |

## 8. Accessibility

Facts from code; browser and assistive-tech behaviour is **[unverified]**.

1. **Cells are native `<button type="button">`**, so they are keyboard-focusable and respond to Enter and Space by default. **[unverified in browser]**
2. **aria-label** on every cell, rewritten each render: `Cell N, empty` or `Cell N, X|O`. The visible text (`X`/`O`) is also set, but the label takes precedence for screen readers.
3. **Status is `aria-live="polite"`**. Each move rewrites the text, so turn changes and results should be announced without stealing focus. **[unverified]**
4. **`aria-disabled`** (not `disabled`) on occupied and locked cells, per ENG-2. Intent: the clicked cell keeps keyboard focus after the move instead of focus dropping to the page start. **ENG-2 fix not reproduced or re-verified in a browser; QA retest pending. Both ENG-2 acceptance boxes are unticked.**
5. **Focus indicator:** `:focus-visible` on cells and Restart shows a 3px solid `#0057d9` outline with 2px offset.
6. **Restart button** has `min-height: 44px`. Width follows its padding and text; no explicit minimum width.
7. **Responsive width:** board width is `min(90vw, 320px)`; cells are square (`aspect-ratio: 1`) and scale with the board. Viewport meta is set. At 320px the cells are about 101px; at a 360px-wide phone the board is 320px (90vw = 324px, capped at 320px). Mark font size is fixed at 2.5rem. **[unverified visually]**
8. **Contrast:** text `#111` on white; focus outline `#0057d9` on white. Ratios not measured here.
9. **Language:** `<html lang="en">`.

## 9. Gaps and ambiguities noticed in the code

Reported, not designed. Decisions belong to the PM and Ananya.

1. **Restart gives no feedback when the status text does not change.** After restarting from `X's turn` mid-game with X to move, the live region text is identical, so a screen reader may announce nothing. **[unverified]**
2. **Focus after Restart is not managed.** Focus stays on Restart. Restart is after the cells in tab order, so reaching cell 1 again takes nine Shift+Tab presses (or Tab out and around the page). **[unverified]**
3. **Occupied cells are only visually distinct by their glyph.** `aria-disabled` styling sets `cursor: default` and `color: #111`, which matches the default; there is no visual "locked" appearance. X and O share the same colour.
4. **No winning-line highlight**; the result is only in the status text.
5. **A screen reader may announce occupied cells as "dimmed/unavailable"** because of `aria-disabled="true"`, yet they remain in the tab order. This is the ENG-2 trade-off. **[unverified]**
6. **Initial status is set during script run on load**, so a live region that was empty at page load may not announce the first `X's turn`. **[unverified]**
7. **Self-check only logs.** A failing assert prints to the console and the game still runs; ENG-1 criterion for "passes with no errors" is unticked because it was never executed.
8. **ENG-2 body is stale:** it describes `disabled = true` as the current code; the code now uses `aria-disabled`. Suggest the ticket text be read together with its log entry.

## 10. Open assumptions and proposed tests

| # | Assumption | Source | Proposed test |
|---|---|---|---|
| A1 | Focus stays on the played cell after a move | Code read only (ENG-2 fix) | Browser: Tab to cell 1, Enter, check `document.activeElement`; repeat through a win and a draw |
| A2 | Enter and Space both place a mark | Browser default for buttons | Keyboard walk-through of a full game |
| A3 | Status changes are announced politely | `aria-live` in code | VoiceOver and one more screen reader, one game each |
| A4 | Layout holds at 320px and 360px widths | CSS read only | Resize in browser devtools |
| A5 | Self-check asserts pass on load | Hand-traced by QA | Open file with console open; expect no assertion messages |

No real-user research exists for this product; all assumptions above are hypotheses, not findings from users or personas.
