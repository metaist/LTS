#!/usr/bin/env python3
"""Create a new project from a template.

Usage:
    python create_project.py [options] [<template>] [<name>] [<destination>]

Arguments:
    template        Template to use (default: common)
    name            Project name (default: current directory name)
    destination     Where to create project (default: current directory)

Example:
    python create_project.py python myproject ../myproject
    python create_project.py --dry-run python
    python create_project.py  # common template in current directory
    python create_project.py --force common  # overwrite existing files

Templates available:
    - common: Shared files only (gitignore, license, etc.)
    - python: Python project with PyPI publishing

Options:
    --dry-run       Show what would be copied without actually copying
    --force         Overwrite existing files in non-empty directories

Variables that will be substituted (use {{VAR}} format in templates):
    {{NAME}}        - Project name
    {{YEAR}}        - Current year (auto-filled)
    {{DATE}}        - Current date in ISO format (auto-filled)

Variables that agents should fill in after creation:
    {{DESCRIPTION}} - One-line description of the project
    {{KEYWORDS}}    - Replace with comma-separated quoted keywords
    {{PURPOSE}}     - Why does this project exist? (for README)
    {{EXAMPLE}}     - Example usage (for README)
"""

from __future__ import annotations

import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"
ALL_DIR = TEMPLATES_DIR / "_all"

# Files that should NOT have variable substitution (binary, etc.)
NO_SUBSTITUTE = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf"}


def substitute(content: str, variables: dict[str, str]) -> str:
    """Replace variable patterns with values from variables dict.

    Supports multiple marker styles for different contexts:
        {{VAR}}  - for general use (markdown, TOML, YAML)
        __VAR__  - for Python identifiers (import __NAME__, etc.)
    """
    for key, value in variables.items():
        content = content.replace(f"{{{{{key}}}}}", value)  # {{VAR}}
        content = content.replace(f"__{key}__", value)  # __VAR__
    return content


def process_includes(content: str, variables: dict[str, str]) -> str:
    """Process {{INCLUDE:path}} markers by inlining file contents.

    Paths are relative to the templates directory.
    Included content also gets variable substitution.
    """
    import re

    pattern = r"\{\{INCLUDE:([^}]+)\}\}"
    while True:
        match = re.search(pattern, content)
        if not match:
            break
        include_path = match.group(1).strip()
        full_path = TEMPLATES_DIR / include_path
        if full_path.exists():
            included = full_path.read_text()
            included = substitute(included, variables)
            included = process_includes(included, variables)  # recursive
        else:
            included = f"<!-- INCLUDE NOT FOUND: {include_path} -->"
        content = content[: match.start()] + included + content[match.end() :]
    return content


def copy_template(
    template_dir: Path,
    dest_dir: Path,
    variables: dict[str, str],
    dry_run: bool = False,
) -> None:
    """Copy template directory to destination, substituting variables."""
    for src_path in template_dir.rglob("*"):
        if src_path.is_dir():
            continue

        # Calculate relative path and substitute in path names
        rel_path = src_path.relative_to(template_dir)
        rel_path_str = substitute(str(rel_path), variables)
        dest_path = dest_dir / rel_path_str

        print(f"  {rel_path_str}")

        if dry_run:
            continue

        # Create parent directories
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Copy file, substituting content if it's a text file
        if src_path.suffix in NO_SUBSTITUTE:  # pragma: no cover
            shutil.copy2(src_path, dest_path)
        else:
            try:
                content = src_path.read_text()
                content = substitute(content, variables)
                content = process_includes(content, variables)
                dest_path.write_text(content)
            except UnicodeDecodeError:  # pragma: no cover
                # Binary file, just copy
                shutil.copy2(src_path, dest_path)


def create_project(
    template: str,
    name: str,
    destination: str,
    dry_run: bool = False,
    force: bool = False,
) -> None:
    """Create a new project from a template."""
    template_dir = TEMPLATES_DIR / template
    if not template_dir.exists():
        available = [
            d.name for d in TEMPLATES_DIR.iterdir() if d.is_dir() and d.name != "all"
        ]
        print(f"Error: Template '{template}' not found.")
        print(f"Available templates: {', '.join(sorted(available))}")
        sys.exit(1)

    dest_dir = Path(destination)
    if not dry_run and not force and dest_dir.exists() and any(dest_dir.iterdir()):
        # Check if it only contains hidden files or is effectively empty
        non_hidden = [f for f in dest_dir.iterdir() if not f.name.startswith(".")]
        if non_hidden:
            print(
                f"Error: Destination '{destination}' already exists and is not empty."
            )
            print("Use --force to overwrite existing files.")
            sys.exit(1)

    # Build variables
    now = datetime.now(timezone.utc)
    variables = {
        "NAME": name,
        "YEAR": str(now.year),
        "DATE": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    if dry_run:
        msg = f"[DRY RUN] Would create project '{name}' from template '{template}'"
        if force:
            msg += " (force mode)"
        print(msg)
    else:
        print(f"Creating project '{name}' from template '{template}'...")
    print(f"Destination: {dest_dir.resolve()}")
    print()

    # Copy all (shared) files first
    print("All files:" if dry_run else "Copying shared files:")
    copy_template(ALL_DIR, dest_dir, variables, dry_run=dry_run)
    print()

    # Copy template-specific files (may override shared)
    print(f"{template} template:" if dry_run else f"Copying {template} template:")
    copy_template(template_dir, dest_dir, variables, dry_run=dry_run)
    print()

    if dry_run:
        print("[DRY RUN] No files were created.")
        return

    print("Done!")
    print()
    print("Next steps:")
    print(f"  1. cd {destination}")
    print("  2. Fill in the remaining variables in the files:")
    print("     - {{DESCRIPTION}} (one-line description)")
    print("     - {{KEYWORDS}} (comma-separated quoted strings)")
    print("     - {{PURPOSE}} (why this project exists)")
    print("     - {{EXAMPLE}} (example usage code)")
    print("  3. git init && git add . && git commit -m 'initial commit'")
    if template == "python":
        print("  4. uv sync")
        print("  5. ds dev")


def main() -> None:
    args = sys.argv[1:]
    dry_run = False
    force = False

    if "--dry-run" in args:
        dry_run = True
        args.remove("--dry-run")

    if "--force" in args:
        force = True
        args.remove("--force")

    if "-h" in args or "--help" in args:
        print(__doc__)
        sys.exit(0)

    # Defaults
    cwd = Path.cwd()
    template = args[0] if len(args) > 0 else "common"
    name = args[1] if len(args) > 1 else cwd.name
    destination = args[2] if len(args) > 2 else "."

    create_project(template, name, destination, dry_run=dry_run, force=force)


if __name__ == "__main__":  # pragma: no cover
    main()
