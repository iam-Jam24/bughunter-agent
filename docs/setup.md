# Setup

## Prerequisites

- Node.js 22.14 or later, Git, Python 3
- An OpenAI API key
- A Daytona API key with **Sandboxes** access and **Snapshots write** permission
- A GitHub token that can write to `iam-Jam24/shopkart-api` and `iam-Jam24/bughunter-agent`:
  - the repo owner can create a fine-grained token for both repos with Contents, Issues and Pull requests set to Read and write, or
  - a collaborator can create a classic token with the `repo` scope (fine-grained tokens cannot reach repos owned by another personal account)

## 1. Start TrueForge

```
npx @truefoundry/trueforge@latest
```

Open http://localhost:8790 and keep the terminal running.

## 2. Configure TrueForge (Settings)

1. **Models**: add the OpenAI provider and paste the key.
2. **Sandbox providers**: Daytona, paste the key.
3. **Connectors**: GitHub, paste the token.

## 3. Build the agent

1. **Build Agent**, pick the OpenAI model.
2. Paste [`agent/instructions.md`](../agent/instructions.md) into Instructions.
3. Add the `github` MCP server and set the approval shields from [`agent/config.md`](../agent/config.md). `merge_pull_request` must require approval.
4. Runtime Config: sandbox on, generative UI on, ask user questions on.
5. **Save Agent** as `bug-hunter`.

## 4. Run

```
Hunt for bugs in shopkart-api and fix them.
```

## 5. Reset the demo

After a run, fixes are merged into `shopkart-api`. Restore the buggy baseline with:

```
.\scripts\reset_target.ps1
```

Then close leftover issues and pull requests on GitHub.
