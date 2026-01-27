# Preferences

Tools, systems, and environment choices — with timelines based on git history and file timestamps. Newest first.

---

## Operating Systems

| Period  | Choice                  | Notes                   |
| ------- | ----------------------- | ----------------------- |
| ~2012+  | [Xubuntu] LTS           | Primary desktop         |
| current | [Ubuntu] LTS (minimal)  | Servers, when available |
| current | [macOS]                 | iOS development only    |
| ~2012   | [Windows] with [WSL]    | Brief                   |
| earlier | [Windows] with [Cygwin] |                         |

[Cygwin]: https://www.cygwin.com/
[macOS]: https://en.wikipedia.org/wiki/MacOS
[Ubuntu]: https://ubuntu.com/
[Windows]: https://www.microsoft.com/en-us/windows
[WSL]: https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux
[Xubuntu]: https://xubuntu.org/

---

## Shell

| Context | Choice |
| ------- | ------ |
| Linux   | [bash] |
| macOS   | [zsh]  |

### Preferred Commands

| Period   | Instead of | Use   | Notes                                 |
| -------- | ---------- | ----- | ------------------------------------- |
| 2026-01+ | —          | [fzf] | Fuzzy finding                         |
| 2025+    | `grep`     | [rg]  | Faster, respects `.gitignore`         |
| 2025+    | `find`     | [fd]  | Respects `.gitignore`, simpler syntax |

[bash]: https://www.gnu.org/software/bash/
[fd]: https://github.com/sharkdp/fd
[fzf]: https://github.com/junegunn/fzf
[rg]: https://github.com/BurntSushi/ripgrep
[zsh]: https://www.zsh.org/

---

## Editors

| Period       | Choice         | Notes                              |
| ------------ | -------------- | ---------------------------------- |
| 2018-06+     | [VS Code]      | Ported TODO syntax                 |
| 2015-06      | [Sublime Text] | Ported TODO syntax; config in repo |
| ~2003 - 2015 | [Notepad++]    | Windows; created TODO syntax ~2008 |
| 2004 - 2006  | [Emacs]        |                                    |

On servers: [nano]

[Emacs]: https://www.gnu.org/software/emacs/
[nano]: https://www.nano-editor.org/
[Notepad++]: https://notepad-plus-plus.org/
[Sublime Text]: https://www.sublimetext.com/
[VS Code]: https://code.visualstudio.com/

---

## Version Control

| Period      | Choice           | Notes                        |
| ----------- | ---------------- | ---------------------------- |
| 2012-02+    | [git] + [GitHub] | Account created 2012-02-26   |
| 2011 - 2012 | [Mercurial]      | .hg directories from 2011-02 |
| earlier     | [Subversion]     |                              |
| earlier     | [CVS]            |                              |
| earlier     | [RCS]            |                              |

Private hosting: [GitLab] (self-hosted)

[CVS]: https://en.wikipedia.org/wiki/Concurrent_Versions_System
[git]: https://git-scm.com/
[GitHub]: https://github.com/
[GitLab]: https://about.gitlab.com/
[Mercurial]: https://www.mercurial-scm.org/
[RCS]: https://en.wikipedia.org/wiki/Revision_Control_System
[Subversion]: https://subversion.apache.org/

---

## Python

### Package Management

| Period      | Choice                                         | Notes                       |
| ----------- | ---------------------------------------------- | --------------------------- |
| 2024-08+    | [uv]                                           | Fast, replaced pip/pdm/venv |
| 2023 - 2024 | [pdm]                                          | For dev scripts             |
| 2021 - 2024 | [pip] + [`pyproject.toml`][pyproject.toml]     | PEP 517/518                 |
| 2018 - 2021 | [pipenv] + [`Pipfile`][Pipfile]                |                             |
| 2012 - 2018 | [pip] + [`requirements.txt`][requirements.txt] |                             |

[Pipfile]: https://pipenv.pypa.io/en/latest/pipfile.html
[pyproject.toml]: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
[requirements.txt]: https://pip.pypa.io/en/stable/reference/requirements-file-format/
[pdm]: https://pdm-project.org/
[pip]: https://pip.pypa.io/
[pipenv]: https://pipenv.pypa.io/
[uv]: https://github.com/astral-sh/uv

### Build Backend

| Period      | Choice       | Notes                                   |
| ----------- | ------------ | --------------------------------------- |
| 2025-11+    | [uv_build]   | Faster builds                           |
| 2020 - 2025 | [setuptools] | With [`pyproject.toml`][pyproject.toml] |
| 2012 - 2020 | [distutils]  | Original Python packaging               |

[distutils]: https://docs.python.org/3/library/distutils.html
[setuptools]: https://setuptools.pypa.io/
[uv_build]: https://github.com/astral-sh/uv

### Linting

| Period      | Choice                          | Notes                    |
| ----------- | ------------------------------- | ------------------------ |
| 2023-05+    | [ruff]                          | Replaced pylint, flake8  |
| 2018 - 2023 | [pylint] + [flake8]             | Dropped coala            |
| 2012 - 2018 | [pylint] + [pep8]/[pycodestyle] | Plus coala-bears briefly |

[flake8]: https://flake8.pycqa.org/
[pep8]: https://pep8.readthedocs.io/
[pycodestyle]: https://pycodestyle.pycqa.org/
[pylint]: https://pylint.readthedocs.io/
[ruff]: https://github.com/astral-sh/ruff

### Formatting

| Period            | Choice        | Notes                         |
| ----------------- | ------------- | ----------------------------- |
| 2023-05+          | [ruff] format | Formatting + linting combined |
| 2020-02 - 2023-05 | [black]       | First formatter adoption      |

[black]: https://black.readthedocs.io/

### Type Checking

| Period   | Choice                                | Notes                           |
| -------- | ------------------------------------- | ------------------------------- |
| 2025-12+ | [ty] + [pyrefly] + [pyright] + [mypy] | Multiple checkers               |
| 2024-07+ | [mypy] + [pyright]                    | Added pyright (ds)              |
| 2023-05+ | [mypy] `--strict`                     | First strict typing ([attrbox]) |

[attrbox]: https://github.com/metaist/attrbox
[mypy]: https://mypy.readthedocs.io/
[pyrefly]: https://github.com/facebook/pyrefly
[pyright]: https://github.com/microsoft/pyright
[ty]: https://github.com/astral-sh/ty

### Testing

| Period      | Choice   | Notes                       |
| ----------- | -------- | --------------------------- |
| 2022+       | [pytest] | Standard by 2023-05         |
| 2012 - 2022 | [nose]   | Used in [hebphonics] (2012) |

[hebphonics]: https://github.com/metaist/hebphonics
[nose]: https://nose.readthedocs.io/
[pytest]: https://pytest.org/

### Dev Scripts / Build Tools

| Period      | Choice        | Notes                                 |
| ----------- | ------------- | ------------------------------------- |
| 2024-07+    | [ds]          |                                       |
| 2024        | [rye]         | Brief usage before ds                 |
| 2023 - 2024 | [pdm] scripts | In pyproject.toml                     |
| 2016 - 2023 | `dev` script  | Custom bash ([idempotent-bash] style) |
| 2013        | [ant]         | build.xml for Python projects         |

[ant]: https://ant.apache.org/
[ds]: https://github.com/metaist/ds
[idempotent-bash]: https://github.com/metaist/idempotent-bash
[rye]: https://rye.astral.sh/

### Documentation

| Period      | Choice            | Notes                     |
| ----------- | ----------------- | ------------------------- |
| 2026-01+    | [mkdocs-material] | For project documentation |
| 2023 - 2025 | [pdoc3]           | API docs from docstrings  |

[mkdocs-material]: https://squidfunk.github.io/mkdocs-material/
[pdoc3]: https://pdoc3.github.io/pdoc/

---

## JavaScript

### Runtime

| Period   | Choice | Notes                  |
| -------- | ------ | ---------------------- |
| 2023-09+ | [bun]  | ~/.bun created 2023-09 |
| earlier  | [node] |                        |

[bun]: https://bun.sh/
[node]: https://nodejs.org/

### Package Management

| Period      | Choice | Notes                      |
| ----------- | ------ | -------------------------- |
| 2023-05+    | [pnpm] | Global dir created 2023-05 |
| 2018 - 2023 | [yarn] | First tried 2018-05-17     |
| 2015 - 2018 | [npm]  | Cache created 2015-09      |

[npm]: https://www.npmjs.com/
[pnpm]: https://pnpm.io/
[yarn]: https://yarnpkg.com/

### Build Tools

| Period      | Choice   | Notes                       |
| ----------- | -------- | --------------------------- |
| 2023+       | [rollup] |                             |
| 2018        | [gulp]   | [duil.js]                   |
| 2013 - 2014 | [grunt]  | [jdb.js], [jquery.superdom] |

[duil.js]: https://github.com/metaist/duil.js
[grunt]: https://gruntjs.com/
[gulp]: https://gulpjs.com/
[jdb.js]: https://github.com/metaist/jdb.js
[jquery.superdom]: https://github.com/metaist/jquery.superdom
[rollup]: https://rollupjs.org/

### Testing

| Period      | Choice   | Notes                       |
| ----------- | -------- | --------------------------- |
| 2023+       | [vitest] |                             |
| 2018        | [tape]   | [duil.js]                   |
| 2013 - 2014 | [qunit]  | [jdb.js], [jquery.superdom] |

[qunit]: https://qunitjs.com/
[tape]: https://github.com/ljharb/tape
[vitest]: https://vitest.dev/

---

## Web Stack

### Backend

| Period   | Choice             | Notes               |
| -------- | ------------------ | ------------------- |
| 2017-03+ | [Flask]            | First: [fullrss.py] |
| current  | [uwsgi]            | App server          |
| earlier  | [PHP]              |                     |
| earlier  | [ASP]              |                     |
| (work)   | [Spring Framework] | Not fun             |

Under consideration: [FastAPI]

[ASP]: https://en.wikipedia.org/wiki/Active_Server_Pages
[FastAPI]: https://fastapi.tiangolo.com/
[Flask]: https://flask.palletsprojects.com/
[fullrss.py]: https://github.com/metaist/fullrss.py
[PHP]: https://www.php.net/
[Spring Framework]: https://spring.io/projects/spring-framework
[uwsgi]: https://uwsgi-docs.readthedocs.io/

### Frontend

| Period      | Choice            | Notes                  |
| ----------- | ----------------- | ---------------------- |
| ~2016+      | [Bulma]           | Bulma released 2016-01 |
| ~2010+      | [Less]            | Less released 2010-02  |
| earlier     | [Material Design] |                        |
| 2011 - 2016 | [Bootstrap]       | Used heavily at work   |
| earlier     | [jQuery]          |                        |

[Bootstrap]: https://getbootstrap.com/
[Bulma]: https://bulma.io/
[jQuery]: https://jquery.com/
[Less]: https://lesscss.org/
[Material Design]: https://m3.material.io/

### HTTP Server / Reverse Proxy

| Period       | Choice   | Notes                 |
| ------------ | -------- | --------------------- |
| 2025-03+     | [Caddy]  | Current for all sites |
| ~2015 - 2025 | [NGINX]  |                       |
| earlier      | [Apache] | httpd and Tomcat      |
| earlier      | [IIS]    |                       |
| earlier      | [XAMPP]  | Windows dev stack     |

[Apache]: https://httpd.apache.org/
[Caddy]: https://caddyserver.com/
[IIS]: https://en.wikipedia.org/wiki/Internet_Information_Services
[NGINX]: https://nginx.org/
[XAMPP]: https://www.apachefriends.org/

### Template Languages

| Context         | Choice     |
| --------------- | ---------- |
| Python          | [Jinja2]   |
| Node            | [Nunjucks] |
| Code generation | [cog]      |

[cog]: https://nedbatchelder.com/code/cog/
[Jinja2]: https://jinja.palletsprojects.com/
[Nunjucks]: https://mozilla.github.io/nunjucks/

---

## Mobile Apps

| Period   | Choice               | Notes          |
| -------- | -------------------- | -------------- |
| 2021-10+ | [Ionic]              |                |
| 2021-10+ | [capacitor-oauth2]   | Auth           |
| 2017-04  | [PhoneGap]/[Cordova] | [30Apps30Days] |

[30Apps30Days]: https://github.com/30Apps30Days
[generic-oauth2]: https://github.com/capacitor-community/generic-oauth2
[Cordova]: https://cordova.apache.org/
[Ionic]: https://ionicframework.com/
[PhoneGap]: https://en.wikipedia.org/wiki/Apache_Cordova

---

## Database

| Period   | Choice             | Notes               |
| -------- | ------------------ | ------------------- |
| current  | [SQLite]           | Local development   |
| 2021-10+ | [PostgreSQL]       | Production          |
| ~2013    | [Elasticsearch]    | Fast, but lost data |
| ~2013    | [MongoDB]          |                     |
| earlier  | [Microsoft Access] | With VBA for UI     |

[Elasticsearch]: https://www.elastic.co/elasticsearch/
[Microsoft Access]: https://en.wikipedia.org/wiki/Microsoft_Access
[MongoDB]: https://www.mongodb.com/
[PostgreSQL]: https://www.postgresql.org/
[SQLite]: https://www.sqlite.org/

---

## Configuration

| Period  | Choice          | Notes  |
| ------- | --------------- | ------ |
| current | [TOML]          | Format |
| current | [attrbox]       | Loader |
| earlier | [python-dotenv] |        |
| earlier | [YAML]          |        |
| earlier | [INI] files     |        |

[python-dotenv]: https://github.com/theskumar/python-dotenv
[TOML]: https://toml.io/
[YAML]: https://yaml.org/
[INI]: https://en.wikipedia.org/wiki/INI_file

---

## Cloud / Hosting

| Period  | Choice         | Notes           |
| ------- | -------------- | --------------- |
| 2017+   | [GCP]          | Work & Personal |
| earlier | [DigitalOcean] | Personal        |
| (work)  | [AWS]          |                 |

[AWS]: https://aws.amazon.com/
[DigitalOcean]: https://www.digitalocean.com/
[GCP]: https://cloud.google.com/

---

## CI/CD

| Period      | Choice           | Notes                |
| ----------- | ---------------- | -------------------- |
| 2021-08+    | [GitHub Actions] | First: [ezq]         |
| 2013 - 2018 | [Travis CI]      | First CI (xurlcheck) |
| (work)      | [Jenkins]        | Work                 |

[ezq]: https://github.com/metaist/ezq
[GitHub Actions]: https://github.com/features/actions
[Jenkins]: https://www.jenkins.io/
[Travis CI]: https://www.travis-ci.com/

---

## DNS / Domains

| Period       | Choice           | Notes                         |
| ------------ | ---------------- | ----------------------------- |
| 2023+        | [Squarespace]    | Forced transition from Google |
| ~2015 - 2023 | [Google Domains] | Best experience               |
| earlier      | [GoDaddy]        |                               |

Under consideration: [Cloudflare]

[Cloudflare]: https://www.cloudflare.com/products/registrar/
[GoDaddy]: https://www.godaddy.com/
[Google Domains]: https://en.wikipedia.org/wiki/Google_Domains
[Squarespace]: https://www.squarespace.com/

---

## Secrets Management

| Period  | Choice        | Context       |
| ------- | ------------- | ------------- |
| 2026+   | [direnv]      | Per-directory |
| ~2002+  | [pwsafe]      | Personal      |
| current | [VaultWarden] | Work          |

[direnv]: https://direnv.net/
[pwsafe]: https://pwsafe.org/
[VaultWarden]: https://github.com/dani-garcia/vaultwarden

---

## Backups

Monthly backups to external drive. Architecture under revision.

---

## Monitoring / Logging

Currently: nothing formal.

---

## Issue Tracking

| Context  | Choice                   |
| -------- | ------------------------ |
| Projects | [GitHub]/[GitLab] Issues |
| Private  | plain text TODO Syntax   |

---

## AI / Large Language Models

| Period       | Choice    | Notes                            |
| ------------ | --------- | -------------------------------- |
| 2026+        | [pi]      | after brief use of [Claude Code] |
| 2026+        | [Claude]  | Opus 4.5 for agent work          |
| 2023 - 2025+ | [ChatGPT] | for discussing ideas via audio   |
| 2025         | [Gemini]  | for OCR                          |

See [Coding Agents Interview](https://metaist.com/blog/2026/01/coding-agents-interview.html)

[ChatGPT]: https://chatgpt.com/
[Claude]: https://www.anthropic.com/claude
[Claude Code]: https://claude.com/product/claude-code
[Gemini]: https://gemini.google.com/
[pi]: https://shittycodingagent.ai/
