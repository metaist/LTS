"""Tests for create_project.py."""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from lts.create_project import ALL_DIR
from lts.create_project import copy_template
from lts.create_project import create_project
from lts.create_project import main
from lts.create_project import process_includes
from lts.create_project import substitute
from lts.create_project import TEMPLATES_DIR


class TestSubstitute:
    """Tests for variable substitution."""

    def test_curly_brace_markers(self) -> None:
        """Test {{VAR}} style markers."""
        result = substitute("Hello {{NAME}}!", {"NAME": "World"})
        assert result == "Hello World!"

    def test_dunder_markers(self) -> None:
        """Test __VAR__ style markers."""
        result = substitute("import __NAME__", {"NAME": "myproject"})
        assert result == "import myproject"

    def test_both_markers_same_variable(self) -> None:
        """Test both marker styles in same content."""
        content = "# {{NAME}}\nimport __NAME__"
        result = substitute(content, {"NAME": "foo"})
        assert result == "# foo\nimport foo"

    def test_multiple_variables(self) -> None:
        """Test multiple different variables."""
        content = "{{NAME}} by {{AUTHOR}} in {{YEAR}}"
        result = substitute(content, {"NAME": "proj", "AUTHOR": "me", "YEAR": "2026"})
        assert result == "proj by me in 2026"

    def test_repeated_variable(self) -> None:
        """Test same variable appearing multiple times."""
        content = "{{NAME}}/{{NAME}}/{{NAME}}"
        result = substitute(content, {"NAME": "x"})
        assert result == "x/x/x"

    def test_no_variables(self) -> None:
        """Test content with no variables."""
        content = "plain text"
        result = substitute(content, {"NAME": "ignored"})
        assert result == "plain text"

    def test_empty_content(self) -> None:
        """Test empty content."""
        result = substitute("", {"NAME": "test"})
        assert result == ""

    def test_empty_variables(self) -> None:
        """Test with no variables dict."""
        result = substitute("{{NAME}}", {})
        assert result == "{{NAME}}"

    def test_variable_in_path(self) -> None:
        """Test variable substitution works for paths."""
        result = substitute("src/{{NAME}}/__init__.py", {"NAME": "mymod"})
        assert result == "src/mymod/__init__.py"


class TestProcessIncludes:
    """Tests for include processing."""

    def test_include_existing_file(self) -> None:
        """Test including an existing file."""
        content = "Before\n{{INCLUDE:_all/LICENSE.md}}\nAfter"
        result = process_includes(content, {"YEAR": "2026"})
        assert "Before" in result
        assert "After" in result
        assert "MIT" in result or "Copyright" in result
        assert "{{INCLUDE:" not in result

    def test_include_missing_file(self) -> None:
        """Test including a non-existent file."""
        content = "{{INCLUDE:nonexistent/file.md}}"
        result = process_includes(content, {})
        assert "INCLUDE NOT FOUND" in result

    def test_include_with_substitution(self) -> None:
        """Test that included content gets variable substitution."""
        content = "{{INCLUDE:_all/LICENSE.md}}"
        result = process_includes(content, {"YEAR": "2099"})
        assert "2099" in result

    def test_nested_includes(self, tmp_path: Path) -> None:
        """Test that includes can be nested (recursive)."""
        # This tests the recursive call in process_includes
        # The _all/AGENTS.md doesn't have includes, so this is a basic test
        content = "{{INCLUDE:_all/AGENTS.md}}"
        result = process_includes(content, {})
        assert "General Principles" in result

    def test_multiple_includes(self) -> None:
        """Test multiple includes in same file."""
        content = "A{{INCLUDE:_all/.gitattributes}}B{{INCLUDE:_all/.editorconfig}}C"
        result = process_includes(content, {})
        assert "A" in result
        assert "B" in result
        assert "C" in result
        assert "text=auto" in result  # from .gitattributes
        assert "root = true" in result  # from .editorconfig


class TestCopyTemplate:
    """Tests for copy_template function."""

    def test_dry_run_creates_no_files(self, tmp_path: Path) -> None:
        """Test dry run doesn't create files."""
        dest = tmp_path / "dest"
        copy_template(ALL_DIR, dest, {"NAME": "test"}, dry_run=True)
        assert not dest.exists()

    def test_copies_files(self, tmp_path: Path) -> None:
        """Test files are copied."""
        dest = tmp_path / "dest"
        copy_template(ALL_DIR, dest, {"NAME": "test", "YEAR": "2026"}, dry_run=False)
        assert dest.exists()
        assert (dest / ".gitignore").exists()
        assert (dest / ".editorconfig").exists()
        assert (dest / "LICENSE.md").exists()

    def test_substitutes_content(self, tmp_path: Path) -> None:
        """Test variable substitution in file content."""
        dest = tmp_path / "dest"
        copy_template(
            ALL_DIR, dest, {"NAME": "testproj", "YEAR": "2026"}, dry_run=False
        )
        license_content = (dest / "LICENSE.md").read_text()
        assert "2026" in license_content
        assert "{{YEAR}}" not in license_content

    def test_substitutes_paths(self, tmp_path: Path) -> None:
        """Test variable substitution in file/directory names."""
        dest = tmp_path / "dest"
        python_template = TEMPLATES_DIR / "python"
        copy_template(python_template, dest, {"NAME": "mymod"}, dry_run=False)
        assert (dest / "src" / "mymod" / "__init__.py").exists()
        assert not (dest / "src" / "{{NAME}}").exists()


class TestCreateProject:
    """Tests for create_project function."""

    def test_invalid_template_exits(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test invalid template name exits with error."""
        with pytest.raises(SystemExit) as exc_info:
            create_project("nonexistent", "test", str(tmp_path / "dest"))
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "not found" in captured.out
        assert "Available templates" in captured.out

    def test_nonempty_dest_exits(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test non-empty destination exits with error."""
        dest = tmp_path / "dest"
        dest.mkdir()
        (dest / "existing.txt").write_text("content")
        with pytest.raises(SystemExit) as exc_info:
            create_project("common", "test", str(dest))
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "not empty" in captured.out
        assert "--force" in captured.out

    def test_force_overwrites_existing(self, tmp_path: Path) -> None:
        """Test --force allows overwriting files in non-empty directory."""
        dest = tmp_path / "dest"
        dest.mkdir()
        (dest / "existing.txt").write_text("keep this")
        (dest / "LICENSE.md").write_text("old license")

        create_project("common", "test", str(dest), force=True)

        # Existing file preserved
        assert (dest / "existing.txt").read_text() == "keep this"
        # Template file overwrites
        assert "MIT" in (dest / "LICENSE.md").read_text()
        # New files created
        assert (dest / ".gitignore").exists()

    def test_force_with_dry_run(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test --force with --dry-run shows force mode."""
        dest = tmp_path / "dest"
        dest.mkdir()
        (dest / "existing.txt").write_text("content")

        create_project("common", "test", str(dest), dry_run=True, force=True)

        captured = capsys.readouterr()
        assert "force mode" in captured.out
        # Files not actually created
        assert not (dest / ".gitignore").exists()

    def test_hidden_files_allowed(self, tmp_path: Path) -> None:
        """Test destination with only hidden files is allowed."""
        dest = tmp_path / "dest"
        dest.mkdir()
        (dest / ".git").mkdir()  # Hidden directory
        # Should not raise - actually create files to cover the branch
        create_project("common", "test", str(dest))
        assert (dest / ".gitignore").exists()

    def test_dry_run_no_files(self, tmp_path: Path) -> None:
        """Test dry run creates no files."""
        dest = tmp_path / "dest"
        create_project("common", "test", str(dest), dry_run=True)
        assert not dest.exists()

    def test_common_template(self, tmp_path: Path) -> None:
        """Test common template creates expected files."""
        dest = tmp_path / "dest"
        create_project("common", "myproj", str(dest))
        assert (dest / ".gitignore").exists()
        assert (dest / "README.md").exists()
        assert (dest / "LICENSE.md").exists()
        assert (dest / "AGENTS.md").exists()

    def test_python_template(self, tmp_path: Path) -> None:
        """Test python template creates expected structure."""
        dest = tmp_path / "dest"
        create_project("python", "myproj", str(dest))
        # Shared files
        assert (dest / ".gitignore").exists()
        assert (dest / "LICENSE.md").exists()
        # Python-specific files
        assert (dest / "pyproject.toml").exists()
        assert (dest / "src" / "myproj" / "__init__.py").exists()
        assert (dest / "src" / "myproj" / "py.typed").exists()
        assert (dest / "test" / "test_myproj.py").exists()
        assert (dest / "mkdocs.yml").exists()
        assert (dest / ".github" / "workflows" / "ci.yaml").exists()

    def test_substitution_in_pyproject(self, tmp_path: Path) -> None:
        """Test variables are substituted in pyproject.toml."""
        dest = tmp_path / "dest"
        create_project("python", "coolproject", str(dest))
        content = (dest / "pyproject.toml").read_text()
        assert 'name = "coolproject"' in content
        assert 'module-name = "coolproject"' in content
        assert "{{NAME}}" not in content

    def test_substitution_in_test_file(self, tmp_path: Path) -> None:
        """Test Python identifier substitution in test file."""
        dest = tmp_path / "dest"
        create_project("python", "mymod", str(dest))
        content = (dest / "test" / "test_mymod.py").read_text()
        assert "import mymod" in content
        assert "mymod.__version__" in content
        assert "__NAME__" not in content

    def test_year_substitution(self, tmp_path: Path) -> None:
        """Test year is substituted in LICENSE."""
        dest = tmp_path / "dest"
        create_project("common", "test", str(dest))
        content = (dest / "LICENSE.md").read_text()
        assert "{{YEAR}}" not in content
        # Should contain current year (or at least a 4-digit year)
        import re

        assert re.search(r"20\d{2}", content)


class TestMain:
    """Tests for main() argument parsing."""

    def test_help_flag(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test --help shows usage."""

        with patch.object(sys, "argv", ["create_project.py", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "Usage:" in captured.out

    def test_defaults(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test default arguments."""
        # Change to tmp directory
        test_dir = tmp_path / "myproject"
        test_dir.mkdir()
        monkeypatch.chdir(test_dir)

        with patch.object(sys, "argv", ["create_project.py", "--dry-run"]):
            main()

        # Should use: template=common, name=myproject (dir name), dest=.

    def test_dry_run_flag_position(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test --dry-run works in different positions."""
        # At start
        with patch.object(
            sys, "argv", ["prog", "--dry-run", "common", "test", str(tmp_path)]
        ):
            main()
        assert not (tmp_path / ".gitignore").exists()

        # At end
        with patch.object(
            sys, "argv", ["prog", "common", "test", str(tmp_path), "--dry-run"]
        ):
            main()
        assert not (tmp_path / ".gitignore").exists()

    def test_force_flag(self, tmp_path: Path) -> None:
        """Test --force flag is parsed correctly."""
        dest = tmp_path / "dest"
        dest.mkdir()
        (dest / "existing.txt").write_text("content")

        with patch.object(
            sys, "argv", ["prog", "--force", "common", "test", str(dest)]
        ):
            main()

        assert (dest / ".gitignore").exists()
        assert (dest / "existing.txt").read_text() == "content"

    def test_force_and_dry_run_flags(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Test --force and --dry-run together."""
        dest = tmp_path / "dest"
        dest.mkdir()
        (dest / "existing.txt").write_text("content")

        with patch.object(
            sys, "argv", ["prog", "--dry-run", "--force", "common", "test", str(dest)]
        ):
            main()

        captured = capsys.readouterr()
        assert "force mode" in captured.out
        assert not (dest / ".gitignore").exists()
