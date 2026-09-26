# Demo script (3 minutes)

| Time | Show | Say |
| --- | --- | --- |
| 0:00-0:20 | `shopkart-api` on GitHub: no issues, green tests | "Tests pass and nobody has reported a bug. We give the agent only the repo." |
| 0:20-1:00 | Agent writes edge-case tests in the sandbox; 3 fail; issues appear on GitHub | "It finds bugs by itself, and every bug comes with a failing test as proof." |
| 1:00-1:50 | Discount bug: fix, all tests pass, guard OK, PR, merge approval card, Approve | "Nothing reaches main without a human. That's the irreversible step, so it stops." |
| 1:50-2:20 | `display_name` issue asking what is intended | "When the expected behavior isn't clear, it asks instead of guessing." |
| 2:20-2:40 | Guard blocking a fix that deletes a test (or the stop rules in the README) | "Hard-coded rules, not the AI, decide whether a fix can ship." |
| 2:40-3:00 | Summary card and the safety table | "Finds bugs, proves them, fixes them, and asks before it merges." |

## Likely questions

- **What if the model is wrong?** A fix needs a test that fails before and passes after, the guard blocks unsafe changes, and a human approves the merge.
- **Why not merge automatically?** Merging changes `main`, which is the irreversible action the brief says a human must own.
- **Does it scale to bigger repos?** The flow is the same; the next step is reading only files related to each function under test.
