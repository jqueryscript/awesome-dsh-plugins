# Contribution guidelines

Thank you for helping maintain Awesome DeepSeek Harness Plugins. Meeting the Stars threshold does not guarantee inclusion. Each addition must be a real DSH plugin with code-level installation evidence.

## Before you submit

A new entry must satisfy every requirement:

- The link points to the canonical public GitHub repository.
- The repository has at least 100 GitHub Stars when the pull request opens.
- The repository is active, is not archived, and is not a mirror or minimally changed fork.
- A `package.json` declares `dsh.bundle`, either at the root or in an independently installable subpackage.
- The bundle patch identifies the Cordis or DSH plugin entry that the host loads.
- The repository documents a supported `dsh plugin` command or an installer that calls the official plugin manager.
- The plugin extends DSH directly. A topic tag, README claim, generic Skill, MCP server, standalone client, preset, or API wrapper does not qualify by itself.
- The description is factual and supported by the project's own files or documentation.

Search [`data/plugins.json`](data/plugins.json) before proposing an entry. Duplicate repositories, packages, and products are rejected.

## Add a plugin

Edit `data/plugins.json`. Do not edit the generated README ranking.

```json
{
  "name": "Project Name",
  "repo": "owner/repository",
  "package": "published-or-source-package",
  "category": "UI & Interfaces",
  "license": "MIT",
  "description": "A factual sentence that explains the plugin's DSH function.",
  "install_command": "dsh plugin --profile web add package-name",
  "manifest_path": "package.json",
  "entrypoint": "package-name",
  "stars": 123,
  "stars_at_addition": 123,
  "added_at": "2026-08-15",
  "verified_at": "2026-08-15"
}
```

Allowed categories are `Files & Runtime`, `Input & Navigation`, `Memory & Knowledge`, `Themes & Appearance`, `UI & Interfaces`, `Vision`, and `Workflow & Automation`.

Use the detected SPDX identifier when one exists. Use `No license detected` when the source is public but GitHub and the repository do not identify a license. Record the exact current Stars in both star fields; the maintenance workflow refreshes the current value later.

## Verification evidence

Include links to:

- The manifest that declares `dsh.bundle`.
- The bundle patch or Cordis configuration.
- The plugin source entry.
- The documented installation command.
- Compatibility information for the current DSH developer preview.

Describe any required companion app, service, credential, platform, or build step.

## Update or remove an entry

Submit corrections when a project moves, changes its package, loses its bundle, changes its license, becomes archived, or stops working with the current preview. An entry that later drops below 100 Stars stays listed until a maintainer reviews it.

## Validate your change

```sh
python scripts/update-stars.py --generate
python -m unittest discover -s tests -v
python scripts/update-stars.py --check
npx awesome-lint
```

The pull request checks also verify live repository status and Markdown links. Keep each pull request focused on one plugin or one related correction.

## Writing style

- Use standard American English.
- State what the plugin does in one sentence.
- End the description with a period.
- Avoid slogans, unsupported comparisons, feature dumps, and copied marketing text.
