# Workspace instructions for GH-300

This repository currently contains only a top-level `README.md` and does not expose a build system, language-specific files, or test setup yet.

## What to do first

- Ask the user for the project language, framework, and intended purpose before implementing non-trivial code.
- If a new project structure is added, identify the build/test commands and update these instructions accordingly.
- Prefer minimal, safe changes until the repository contains actual source files.

## How to work in this repository

- Treat the current repository as a bootstrap / scaffold repository.
- Do not assume any particular toolchain, runtime, or package manager unless the user specifies it.
- If the user wants a starter project, ask whether they want:
  - a web app, API, library, CLI, or other project type
  - preferred language and framework
  - a package manager or build tool

## When to update this file

Add or revise workspace instructions when the repository gains:

- source code in a specific language
- CI or test configuration
- docs describing architecture, conventions, or runtime requirements
- domain-specific guidelines for frontend/backend/tests

## Example prompts to use with this repo

- "Create a minimal project structure for a new [language/framework] app in this repo."
- "Add a starter CI workflow and test script once the codebase exists."
- "Help me draft project architecture documentation for this repository."

## Notes

- If the repository later includes multiple areas (frontend/backend/tests), consider adding file-scoped instructions under `.github/instructions/` or custom agents under `.github/agents/`.
- Keep workspace instructions focused on discovery, project conventions, and how the agent should behave when the repo is still small.
