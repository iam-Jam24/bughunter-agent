# Architecture

Bug Hunter runs on the TrueForge agent harness. The model decides what to do; TrueForge executes it through the GitHub MCP server and the Daytona sandbox, and pauses for a human before anything changes `main`.

```mermaid
flowchart TD
    A[Read shopkart-api code<br/>GitHub MCP] --> B[Sandbox: write edge-case tests<br/>from docstrings]
    B --> C{Test fails?}
    C -- no --> Z[No bug: move on]
    C -- yes --> D{Docstring clear?}
    D -- no --> Q[Open issue asking the human<br/>STOP, do not fix]
    D -- yes --> E[Open bug issue<br/>with failing test]
    E --> F[Sandbox: fix until all tests pass<br/>max 3 attempts]
    F --> G{guard.py verdict}
    G -- STOP --> H[Show reasons, ask the human]
    G -- OK --> I[Human approval: commit + open PR]
    I --> J[Human approval: merge]
    J --> K[Issue auto-closed by 'Fixes #N']
```

## Components

| Component | Role |
| --- | --- |
| TrueForge | Agent harness: runs the agent loop, holds the GitHub token, enforces approval shields |
| GitHub MCP server | The agent's access to the real system: read code, open issues, branches, PRs, merge |
| Daytona sandbox | Isolated machine where generated tests and fixes run; holds no secrets |
| `guard/guard.py` | Deterministic stop rules checked before any PR |
| OpenAI model | Reasons about the code and decides the next tool call |

## Why the sandbox never clones the repo

Secrets stay in the harness. The sandbox has no GitHub token, so the agent reads files through the GitHub MCP tools and writes them into the sandbox. Even if generated code misbehaves, it cannot reach our credentials.
