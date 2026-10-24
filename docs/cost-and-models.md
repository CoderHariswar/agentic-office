# Cost and models

How much the office costs to run, where the money goes, and how to change models.

## Measured runs

Both runs used the `balanced` preset, with the main session (Meera) on Opus. Figures are Claude Code's own usage report for the run, priced at API rates.

**Run A: "Build a simple tic-tac-toe game"** (COO, CTO, frontend engineer, QA; one bug found and fixed; about 3 minutes)

| Model | Input | Cache writes | Cache reads | Output | Cost |
|---|---|---|---|---|---|
| Opus (main session + CTO) | 40 | 66,730 | 940,947 | 8,012 | $0.83 |
| Sonnet (engineer, QA) | 36 | 43,522 | 268,993 | 11,365 | $0.25 |
| Haiku (Claude Code housekeeping) | 1,296 | 0 | 0 | 21 | <$0.01 |
| **Total** | | | **~1.34 M tokens** | **~19 K** | **$1.08** |

**Run B: "Write the full product documentation"** (COO + 6 agents, 6 documents; about 3 minutes)

| Model | Input | Cache writes | Cache reads | Output | Cost |
|---|---|---|---|---|---|
| Opus | 52 | 96,260 | 1,763,003 | 20,009 | $1.45 |
| Sonnet | 34 | 110,776 | 233,600 | 24,513 | $0.55 |
| Haiku | 1,450 | 0 | 0 | 23 | <$0.01 |
| **Total** | | | **~2.25 M tokens** | **~45 K** | **$2.00** |

## What this tells you

- **Cache reads dominate.** Every turn re-reads the Company OS, the agent's profile and the conversation so far. Claude Code caches this, so it is billed at a fraction of normal input price. That is how 1.3 M tokens cost about a dollar.
- **The main session is the biggest cost.** Meera reads every agent's report and keeps the whole conversation, so about 75% of the cost was the main session. Moving only the main session from Opus to Sonnet is the single biggest saving.
- **Agents are cheap per task.** A specialist on Sonnet doing one focused job cost $0.05–0.15.

## 10 small tasks a day

Assuming every task looks like Run A:

| | Per day | Per month (30 days) |
|---|---|---|
| Tokens processed | ~13.4 M, of which ~200 K output | ~400 M |
| `balanced`, main session on Opus (measured rate) | ~$11 | ~$325 |
| `balanced`, main session on Sonnet (estimate) | ~$7.50 | ~$230 |
| `budget` preset (estimate) | ~$5.50 | ~$165 |

The two estimates reprice Run A's token counts at the cheaper models' list prices. They assume the cheaper models use a similar number of tokens, which is not guaranteed: a weaker model can need more turns. Measure your own runs; Claude Code shows usage with `/cost` (API) or `/usage` (subscription).

**Subscriptions:** Pro costs $20/month and Max $100 or $200/month. Anthropic does not publish their limits in tokens, so we can't say exactly how many tasks fit. Expect Pro to run out after a few tasks a day. More importantly, subscriptions are meant for ordinary individual use; see [Subscription or API key](../README.md#subscription-or-api-key).

## Changing models

All model choices live in [`config/models.json`](../config/models.json).

```bash
python3 tools/set_models.py --show             # who runs on what
python3 tools/set_models.py --preset budget    # switch preset
python3 tools/set_models.py                    # apply after editing the file
```

The config has four parts:

- **`preset`**: which preset is active.
- **`presets`**: for each preset, the model for the main session and for each tier. `main_session: null` leaves your Claude Code default alone.
- **`tiers`**: which agents are `strategic` and `routine`. Everyone else is `standard`.
- **`overrides`**: individual agents that should ignore the preset.

Accepted model values: `opus`, `sonnet`, `haiku`, `fable`, `inherit` (same as the main session), or a full model ID such as `claude-sonnet-5-5`. The script rejects anything else.

You can add your own preset, for example one for a design-heavy week:

```json
"design-week": { "main_session": "sonnet", "strategic": "opus", "standard": "haiku", "routine": "haiku" }
```

…and give the designers more power with overrides:

```json
"overrides": { "product-designer": "opus", "ux-researcher": "sonnet" }
```

**One model for everything, temporarily:** set these environment variables before starting Claude Code. They override every agent file without changing it.

```bash
export CLAUDE_CODE_SUBAGENT_MODEL=haiku
export CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1
```

## Habits that keep cost down

1. Ask for specific people or one department, not "everyone".
2. Give tight briefs with file paths, so agents read only what they need.
3. Start a fresh session for each topic. Long sessions re-read more history on every turn.
4. Keep routine roles on Haiku; their work is classification, formatting and tracking.
5. Set a monthly spend limit in the [Claude Console](https://platform.claude.com/).
