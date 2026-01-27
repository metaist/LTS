# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Sections order is: `Fixed`, `Changed`, `Added`, `Deprecated`, `Removed`, `Security`.

## [Unreleased]

These are changes that are on `main` that are not yet tagged.

---

## [1.0.0] - 2026-01-27T21:42:39Z

Initial release.

### Added

- [#9] templates and preferences
  - `common` template: minimal shared files (gitignore, license, editorconfig, AGENTS.md)
  - `python` template: Python project with PyPI publishing, pytest, mkdocs, CI/CD
  - `create_project.py`: project creation script with `--dry-run` and `--force` options
  - Preferences documentation: tools, systems, environment with historical timelines

[#9]: https://github.com/metaist/LTS/issues/9
[Unreleased]: https://github.com/metaist/LTS/compare/1.0.0...HEAD
[1.0.0]: https://github.com/metaist/LTS/releases/tag/1.0.0
