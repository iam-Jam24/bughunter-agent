# Build story

All code in this repo and in `shopkart-api` was written on hackathon day, 26 Sep. Before the event we only learned how TrueForge works on a separate throwaway repo, which the rules allow ("prior research and reading the TrueForge documentation are allowed").

## Learning TrueForge (before the event, throwaway repo)

| Problem | Cause | Fix |
| --- | --- | --- |
| Daytona rejected the API key | A Groq model key was pasted into the sandbox settings | Each provider needs its own key; Daytona keys also need Snapshots write permission |
| `401 Incorrect API key` | Groq key added under the built-in OpenAI provider | Add Groq through Add Custom Provider with its own base URL |
| `400 reasoning_content is unsupported` | Groq rejects the reasoning field sent back for reasoning models | Switch model or provider |
| `429 limit: 0` on Gemini Pro | Pro has no free tier | Use a Flash model |
| `429 limit: 5` on Gemini Flash | Agents make many calls per task | Paid credits for the real build |
| Agent asked "which issue?" with no tools | Config was lost after New Chat | Save Agent before testing |

## Hackathon day (26 Sep)

- Chose a GitHub-only agent over an AWS cost-cleanup agent to keep setup risk low.
- Upgraded from "fix the issue a human wrote" to "find the bugs yourself", with merge kept behind human approval.
- Wrote `guard.py` so stop rules are enforced in code, not only in the prompt.

_Add entries as the day goes on._
