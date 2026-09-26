# TrueForge agent configuration

| Setting | Value |
| --- | --- |
| Model | OpenAI (mini model while testing, largest model for the demo) |
| MCP servers | `github` (token with access to `iam-Jam24/shopkart-api` and `iam-Jam24/bughunter-agent`; see [setup](../docs/setup.md)) |
| Sandbox | On (Daytona) |
| Generative UI | On |
| Ask user questions | On |

## Approval shields (GitHub MCP tools)

| Tool | Approval | Why |
| --- | --- | --- |
| `list_issues`, `get_issue`, `get_file_contents`, `search_code` | Off | Read-only |
| `create_issue`, `add_issue_comment` | Off | Reporting a bug changes no code |
| `create_branch` | Off | Does not touch `main` |
| `create_or_update_file` / `push_files` | **On** | Writes code into the repo |
| `create_pull_request` | **On** | Proposes a change |
| `merge_pull_request` | **On** | Changes `main`: the irreversible action |
| Issue update / close tools | **On** | The agent must never close issues itself |
