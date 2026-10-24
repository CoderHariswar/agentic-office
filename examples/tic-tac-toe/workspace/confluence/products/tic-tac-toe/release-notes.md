---
title: Tic-Tac-Toe · Release Notes
owner: devops-release-engineer
department: Engineering & Quality
status: Draft
created: 2026-10-24
updated: 2026-10-24
---

# Tic-Tac-Toe · Release Notes

Jira: ENG-1 (`workspace/jira/ENG-1-tic-tac-toe.md`), ENG-2 (`workspace/jira/ENG-2-ttt-focus-lost-after-move.md`). Test cases: `workspace/confluence/products/tic-tac-toe/test-cases.md`.

## Release status (as of 2026-10-24)

**Nothing has been deployed or released.** There is no production release of Tic-Tac-Toe. The one entry below is an internal build only. ENG-1 scope is internal: no deploy, no publishing.

## 0.1.0 (internal, unreleased) · 2026-10-24

**Artifact:** `products/tic-tac-toe/index.html` (single file, inline CSS and JS, no dependencies, no build step).
**Version reference:** none. This code is not under version control, so there is no tag or commit to cite. Not invented here. Identify the build by file path and date until a repository exists.

### What it contains (ENG-1, as in the code)
- Two players on one device alternate X and O on a 3x3 board; X starts.
- Status line shows whose turn it is, or the result.
- Win detection on all 8 lines (3 rows, 3 columns, 2 diagonals) via a pure `winner(board)` function; draw detection on a full board with no winner.
- No moves after the game ends; occupied cells cannot be overwritten (guard in `play()`).
- Restart button clears the board and returns to X's turn.
- Accessibility: cells are `<button>` elements with aria-labels; status is an `aria-live="polite"` region; visible focus outlines.
- On-load `console.assert` self-check of `winner()` (row, column, diagonal, draw, in-progress).

### What changed (ENG-2)
- Fixed keyboard focus loss after each move. Cells now use `aria-disabled` instead of the `disabled` attribute, so focus is no longer dropped from the played cell. CSS selector changed to `.cell[aria-disabled="true"]`. `play()` still rejects occupied-cell and finished-game moves.

### Known issues / not verified
- ENG-1 criterion 1 (opens from a local file, no network): NOT verified by execution. Code-trace only.
- ENG-1 criterion 9 (on-load self-check runs with no console errors): NOT verified by execution. All 5 cases hand-traced as correct only.
- ENG-2 fix: NOT verified by execution. Not reproduced or re-tested in a browser; focus behaviour after a move is unconfirmed. Acceptance boxes unticked.
- Other criteria were passed by code-trace, not by running the page. No browser or keyboard test has been done.
- ENG-1 and ENG-2 are both still In Review.

### Rollback
Not deployed, so there is nothing to roll back. If this file is ever published, rollback is to restore the previous published file. No previous version exists today.

## Release gates not yet met

- Execution check of ENG-1 criteria 1 and 9 (node harness and/or one browser open) not done.
- ENG-2 focus fix not retested by QA in a browser.
- ENG-1 and ENG-2 not closed (In Review).
- No version control, tag or commit reference for the code.
- Risk review and the remaining gates in the engineering playbook not recorded.

**Any production release requires CEO approval, requested only after all release gates pass.** No approval request has been filed.
