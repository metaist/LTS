# Project-Specific ({{NAME}})

**Goal**: {{DESCRIPTION}}

## Development Commands

| Command   | Purpose                                                                   |
| --------- | ------------------------------------------------------------------------- |
| `ds dev`  | **Must pass before every commit** — lint, type check, tests, spell check  |
| `ds test` | Run tests only                                                            |
| `ds lint` | Run linters only                                                          |
| `ds docs` | Build documentation                                                       |

## Validation Rules

**`ds dev` is mandatory before commits.** Check the **full output**, not just the last few lines.

Common issues caught by `ds dev`:

- **cspell**: Unknown words → add to `.cspell.json`
- **ruff**: Python lint/format issues
- **ty/pyrefly/pyright/mypy**: Type errors
- **pytest**: Test failures

If `ds dev` fails, fix the issue before committing. Don't assume CI will catch it.

---

{{INCLUDE:_all/AGENTS.md}}
