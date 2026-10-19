# AGENTS.md

## Repo state

- Task 1 of 6 (project skeleton) is done: Django 5.2.18 project exists (`manage.py`, `config/`, `core/`, `bva/`, `dirty_strings/`) on branch `project-skeleton-core-layout` (based on `develop`). Shared layout + dark/light theme are implemented; feature logic is not.
- Remaining tasks: `req_docs/qa_toolkit_release_1_2_spec.md` … `qa_toolkit_release_1_6_spec.md` — treat the relevant spec file as source of truth for each task.
- `.venv/` is set up (Django installed, `requirements.txt` pinned). Use `.venv/bin/python manage.py …`.
- Verification commands: `.venv/bin/python manage.py check` / `migrate`, then runserver smoke test (`/` 302→`/bva/`, `/bva/` and `/dirty-strings/` 200).
- `README.md` is a placeholder (a stray `tstwrld` line, likely accidental).

## Project: QA Toolkit (Django)

- Python 3.11+ (system python3 is 3.12; `.venv/` exists but is empty — install Django yourself, it's not there).
- Django 5.2.18 (pinned in `requirements.txt`), Django templates + Tailwind via CDN + vanilla JS/Alpine.js. **No Node.js build pipeline** — don't add one.
- Structure: `manage.py`, `config/` (settings/urls/wsgi/asgi), `core/` (shared base/header/sidebar templates, `/` redirects to `/bva/`), `bva/` (Boundary Value Analysis), `dirty_strings/` (Special & Dirty Strings). Theme: pre-paint JS in `base.html`, `qa-theme` localStorage key, Tailwind `darkMode: "class"`, single Alpine scope on `<html>`.
- Key convention: business logic lives in `bva/services.py` and `dirty_strings/presets.py`, decoupled from views, so it stays unit-testable. BVA uses the standard 7-point boundary model with a `step` parameter.

## Working style

- This repo uses the Kilo code-authoring pipeline (`.kilo/skills/code-authoring-pipeline/`, sub-agents in `.kilo/agent/`): DRIVER owns branches; only CODER edits code; planner/reviewer are read-only.
- Domain skills exist in `.kilo/skills/` (django-patterns, django-tdd, django-verification, python-patterns) — load the relevant one before writing Django code.
