---
description: Bring new comments from Jira into the task files and act on them
---

As Ankit (COO):
1. Run `python3 tools/jira_sync.py pull` (skip if it says Jira is not configured). It appends every new human comment to the matching task's log and prints them.
2. For each comment: if it is a question, answer it (call the task owner if needed) and log the answer in the task file. If it is an instruction or decision from the CEO, act on it like any CEO request. If it says "approved" or "rejected" for an approval, follow `workspace/approvals/README.md`.
3. Report to the CEO in a few lines: which comments came in and what was done. Your log entries reach Jira automatically.
