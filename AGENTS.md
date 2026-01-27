# LTS Project Guidelines

**Goal**: Project templates and tooling preferences for Metaist projects.

## Development Commands

| Command   | Purpose                                                                  |
| --------- | ------------------------------------------------------------------------ |
| `ds dev`  | **Must pass before every commit** — lint, type check, tests, spell check |
| `ds test` | Run tests only                                                           |
| `ds lint` | Run linters only                                                         |
| `ds docs` | Build documentation                                                      |

## Validation Rules

**`ds dev` is mandatory before commits.** Check the **full output**, not just the last few lines.

## Creating Projects from Templates

```bash
cd /path/to/LTS

# Create a Python project
uv run -m lts.create_project python myproject ../myproject

# Preview without creating files
uv run -m lts.create_project --dry-run python myproject

# Add to existing project
uv run -m lts.create_project --force common myproject ../myproject
```

### Available Templates

Run `uv run -m lts.create_project --help` to see available templates.

### After Running the Script

Fill in these placeholders in the generated files:

| Variable          | Description                                  |
| ----------------- | -------------------------------------------- |
| `{{DESCRIPTION}}` | One-line description                         |
| `{{KEYWORDS}}`    | Comma-separated quoted strings: `"a", "b"`   |
| `{{PURPOSE}}`     | Why this project exists                      |
| `{{EXAMPLE}}`     | Example usage code                           |

Then:

1. Add project-specific words to `.cspell.json`
2. `git init && git add . && git commit -m 'initial commit'`
3. For Python: `uv sync && ds dev`

## Template Structure

Templates live in `templates/`. The `_all/` directory contains shared files copied to all projects; template-specific directories can override them.

Variable markers:

- `{{VAR}}` — general substitution (markdown, TOML, YAML)
- `__VAR__` — Python identifiers
- `{{INCLUDE:path}}` — inline files from `templates/`

## Adding New Templates

1. Create directory under `templates/`
2. Add template files (can override `_all/`)
3. Use variable markers as needed
4. Update docs: `docs/project-templates/`

---

# General Principles

## Preflight

Before starting any task:

1. Confirm you have the tools to do the work _and_ verify it succeeded
2. Identify the goal and immediate task; restate if conversation is long or after compaction
3. Check for relevant GitHub issues; add comments for significant progress
4. Clarify: **quick experiment** (user will check) or **deep dive** (use judgment)?

## Working Style

- Default to minimal changes; propose scope before larger refactors
- Don't delete files you didn't create (others may be working in same directory)
- Don't delete build artifacts needlessly; prefer idempotent approaches
- Follow existing patterns in the codebase
- Prefer editing existing files over creating new ones
- Don't add unnecessary comments or docstrings to unchanged code

## Communication

- Number items in summaries so user can reference specifics
- Present meaningful alternatives and wait—unless this is a deep dive
- If solving a different problem than started, stop and check in
- For long-running commands: `cmd 2>&1 | tee /tmp/build.log`
- If something hangs, investigate rather than waiting silently
- Notify when long-running tasks complete

## Shell Commands

| Instead of | Use  | Why                                   |
| ---------- | ---- | ------------------------------------- |
| `find`     | `fd` | Respects `.gitignore`, simpler syntax |
| `grep`     | `rg` | Faster, respects `.gitignore`         |
| `pip`      | `uv` | Faster, better dependency resolution  |

## Code Style

- Type hints with modern syntax (`Path | None` not `Optional[Path]`)
- Require 100% test coverage; task isn't complete without it
- `# pragma: no cover` only for trivial `if __name__ == "__main__"` or truly unreachable code
- Test observable behavior, not implementation details

## Workflow

1. Create an issue before implementing non-trivial changes
2. Add comments to issues when scope expands or for significant progress
3. Discuss structural/organizational changes before implementing
4. **Run validation commands and check full output** before committing
5. Commit frequently, but **do not push until asked**
6. Pushing to `main` triggers CI; batch commits to limit runs

## Commit Messages

Format: `prefix: description (#issue)`

| Prefix      | Use for                                    |
| ----------- | ------------------------------------------ |
| `add:`      | New features, files, capabilities          |
| `fix:`      | Bug fixes, corrections                     |
| `update:`   | Changes to existing functionality, docs    |
| `remove:`   | Deletions                                  |
| `refactor:` | Code restructuring without behavior change |

Rules:

- Lowercase titles, sentence fragments (no trailing period)
- Backticks for code: `` fix: bug in `keep_going` parsing ``
- Reference issues: `(#123)` or `(closes #123)`
- Include `Co-Authored-By: {Model Name + Version} <noreply@anthropic.com>` in body

## GitHub Issues and Comments

- Same prefix convention as commits
- Lowercase titles; backticks for code references
- Add `aigen` label for AI-generated issues
- Start body: "Created by {Model Name + Version} during {context}..."
- Prefer flat hierarchy in markdown; use bolding appropriately

## Conventions

- Dates: ISO 8601 (`YYYY-MM-DD`)
- Prefer well-adopted standards where they exist
