# Bug Hunter

![tests](https://github.com/iam-Jam24/bughunter-agent/actions/workflows/tests.yml/badge.svg)

**An agent that finds bugs by itself, proves each one with a failing test, fixes it, and never merges without a human's approval.**

Built on [TrueForge](https://github.com/truefoundry/trueforge) for the *Agents That Act* hackathon.

## Problem

Bugs hide in code paths that tests don't cover. Finding them takes hours, and AI coding tools make it worse when they "fix" things without proof or quietly weaken tests to go green.

## How it works

1. Reads the target repo, [`shopkart-api`](https://github.com/iam-Jam24/shopkart-api), through the GitHub MCP server.
2. In an isolated Daytona sandbox, writes edge-case tests for every function based on its docstring.
3. A failing test that contradicts the docstring is a confirmed bug: the agent opens a GitHub issue with the evidence.
4. If the intended behavior is unclear, the agent opens an issue asking a human instead of guessing.
5. Fixes one bug at a time until all tests pass (max 3 attempts).
6. [`guard/guard.py`](guard/guard.py) checks the fix against the stop rules.
7. Opens a PR with before/after test output, then requests the merge. A human approves or rejects.

See [docs/architecture.md](docs/architecture.md) for the flow diagram.

## Meeting the hackathon requirements

| Requirement | How Bug Hunter meets it |
| --- | --- |
| Reach a real system | Reads code, opens issues, branches and PRs on a real GitHub repo |
| Run generated code in a sandbox | Every generated test and fix runs in a Daytona sandbox with no secrets |
| Stop before irreversible actions | Committing, opening a PR and merging into `main` all wait for human approval |

## Safety model

| Action | Who decides |
| --- | --- |
| Read code, run tests in the sandbox | Agent (automatic) |
| Open an issue for a proven bug | Agent (automatic) |
| Unclear expected behavior | Agent stops and asks on an issue |
| Fix too large, tests weakened, no proof | Guard script blocks the PR |
| Commit code, open PR | Human approval |
| Merge into `main` | Human approval |

## Stop rules (enforced in code by `guard/guard.py`)

- No new failing test → no PR
- Existing tests deleted or weakened → no PR
- More than 2 source files changed → human decides
- Still failing after 3 attempts → human decides

## Repo layout

```
guard/guard.py              deterministic stop rules
tests/test_guard.py         unit tests for every rule
agent/instructions.md       TrueForge agent instructions
agent/config.md             model, tools, approval shields
scripts/reset_target.ps1    restore shopkart-api to its demo baseline
docs/                       architecture, setup, demo script, build story
```

## Getting started

Follow [docs/setup.md](docs/setup.md). Run the guard tests with:

```
pip install -r requirements-dev.txt
python -m pytest -v
```

## Demo

- Script: [docs/demo-script.md](docs/demo-script.md)
- Build story: [docs/build-story.md](docs/build-story.md)
- Screenshots and video: _TODO_

## Tech

TrueForge · GitHub MCP · Daytona sandbox · OpenAI · Python

## AI tools used

- Claude Code: helped plan the project and draft the guard script, demo repo and documentation.
- _Add any others the team used._

## Team

- [Aditya031906](https://github.com/Aditya031906)
- [iam-Jam24](https://github.com/iam-Jam24)
