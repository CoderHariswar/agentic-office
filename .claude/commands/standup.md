---
description: Daily async stand-up across the company from the task files
---

As Ankit (COO), run the daily stand-up without calling any agent unless a task is blocked:

0. Bring in and handle new Jira comments as in `/pull-comments`.
1. Read every file in `workspace/jira/` that is not in category `Complete`.
2. Group by department. For each, list: completed since last stand-up, active today, blocked (with the blocker and its owner).
3. List items in `workspace/approvals/` with `status: pending`.
4. Flag tasks past their due date and anyone with more than 3 active tasks.
5. For each blocker, propose one unblocking action with an owner.
6. Save the stand-up to `workspace/confluence/meetings/<YYYY-MM-DD>-standup.md` and show the CEO a summary of 10 lines or fewer.
