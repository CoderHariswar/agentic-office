# Example: tic-tac-toe

A real run of the office. The only later edit: the Chief of Staff, originally named Meera Iyer, was renamed Ankit Jha everywhere. The folder mirrors the office layout, so every path the agents wrote still resolves inside this example.

## The two requests

1. *"Build a simple tic-tac-toe game: two players on the same device, in a browser, shows whose turn it is, detects win and draw, restart button. Single HTML file. Run it through the normal process."*
2. *"Document the game like a proper company: overview, scope, functional spec, technical design, test cases, release notes, each written by its owner."*

## What came out

| File | Written by |
|---|---|
| [`products/tic-tac-toe/index.html`](products/tic-tac-toe/index.html) | Sneha Pillai (Frontend Engineer 1); bug fix after QA |
| [`workspace/jira/ENG-1-tic-tac-toe.md`](workspace/jira/ENG-1-tic-tac-toe.md) | Created by Ankit (COO). The log shows Rahul (CTO), Sneha and Divya (QA) handing off |
| [`workspace/jira/ENG-2-ttt-focus-lost-after-move.md`](workspace/jira/ENG-2-ttt-focus-lost-after-move.md) | Bug filed by Divya, fixed by Sneha |
| [`workspace/jira/PROD-1-tic-tac-toe-docs.md`](workspace/jira/PROD-1-tic-tac-toe-docs.md) | Documentation task, created by Ankit |
| [`…/overview.md`](workspace/confluence/products/tic-tac-toe/overview.md), [`scope.md`](workspace/confluence/products/tic-tac-toe/scope.md) | Priya Nair (Product Manager) |
| [`functional-spec.md`](workspace/confluence/products/tic-tac-toe/functional-spec.md) | Karthik Subramanian (Product Designer) |
| [`technical-design.md`](workspace/confluence/products/tic-tac-toe/technical-design.md) | Sneha Pillai, reviewed by Rahul Venkatesh (CTO) |
| [`test-cases.md`](workspace/confluence/products/tic-tac-toe/test-cases.md) | Divya Krishnan (QA): 29 cases |
| [`release-notes.md`](workspace/confluence/products/tic-tac-toe/release-notes.md) | Gaurav Malhotra (DevOps) |

Cost at API prices: $1.08 for the build and $2.00 for the docs. See [docs/cost-and-models.md](../../docs/cost-and-models.md).

## Worth noticing

- **The agents said what they could not verify.** The run did not allow them to execute code, so QA tested by reading the code and marked results "code-trace" rather than "pass". The maintainer later ran the game's logic checks separately, and they passed.
- **QA found a real bug** (keyboard focus lost after each move) that a quick review would miss.
- **Ankit corrected a subordinate's error** in the overview before reporting, and was added to that page as a contributor.

Play the game: open `products/tic-tac-toe/index.html` in a browser.
