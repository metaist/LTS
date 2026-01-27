# Project Templates

Templates for creating new projects with consistent structure and tooling.

## Usage

```bash
cd /path/to/LTS
uv run -m lts.create_project [options] [<template>] [<name>] [<destination>]
```

| Argument      | Default                | Description                |
| ------------- | ---------------------- | -------------------------- |
| `template`    | `common`               | Template to use            |
| `name`        | current directory name | Project name               |
| `destination` | `.`                    | Where to create project    |

| Option      | Description                                        |
| ----------- | -------------------------------------------------- |
| `--dry-run` | Show what would be copied without actually copying |
| `--force`   | Overwrite existing files in non-empty directories  |

## Available Templates

<!--[[[cog
from pathlib import Path
for d in sorted(Path("templates").iterdir()):
    if d.is_dir() and not d.name.startswith("_"):
        cog.outl(f"- [`{d.name}`](https://github.com/metaist/LTS/tree/main/templates/{d.name})")
]]]-->
- [`common`](https://github.com/metaist/LTS/tree/main/templates/common)
- [`python`](https://github.com/metaist/LTS/tree/main/templates/python)
<!--[[[end]]]-->

Shared files in [`_all`](https://github.com/metaist/LTS/tree/main/templates/_all) are copied to every project first; template-specific files can override them.

## How It Works

1. Copies `templates/_all/` to destination (shared files)
2. Copies `templates/<template>/` to destination (may override shared)
3. Substitutes variables in file names and content

## Variables

Two marker styles for different contexts:

| Style     | Use for                          | Example            |
| --------- | -------------------------------- | ------------------ |
| `{{VAR}}` | General (markdown, TOML, YAML)   | `# {{NAME}}`       |
| `__VAR__` | Python identifiers               | `import __NAME__`  |

### Auto-filled

| Variable   | Value                 |
| ---------- | --------------------- |
| `{{NAME}}` | Project name          |
| `{{YEAR}}` | Current year          |
| `{{DATE}}` | Current ISO timestamp |

### Fill after creation

| Variable          | Description                        |
| ----------------- | ---------------------------------- |
| `{{DESCRIPTION}}` | One-line description               |
| `{{KEYWORDS}}`    | Comma-separated quoted strings     |
| `{{PURPOSE}}`     | Why this project exists            |
| `{{EXAMPLE}}`     | Example usage code                 |

## File Includes

Use `{{INCLUDE:path}}` to inline another file's contents (path relative to `templates/`):

```markdown
{{INCLUDE:_all/AGENTS.md}}
```

Included content also gets variable substitution.
