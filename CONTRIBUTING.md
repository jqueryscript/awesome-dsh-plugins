# Contribution guidelines

Thank you for helping maintain Awesome DeepSeek Harness Plugins. Each addition must be an installable DSH plugin with source code and documented installation instructions.

## Before you submit

A new entry must satisfy every requirement:

- The link points to the canonical public GitHub repository.
- The repository has at least 30 GitHub Stars when the pull request opens.
- The repository is active, is not archived, and is not a mirror or minimally changed fork.
- A `package.json` declares `dsh.bundle`, either at the root or in an independently installable subpackage.
- The bundle patch identifies the Cordis or DSH plugin entry that the host loads.
- The repository documents a reproducible `dsh plugin add` command, including any required profile or build step.
- The plugin extends DSH directly. A topic tag, README claim, generic Skill, MCP server, standalone client, preset, or API wrapper does not qualify by itself.
- The description is factual and supported by the project's own files or documentation.

Search [the list](README.md) before proposing an entry. Duplicate repositories, packages, and products are rejected.

## Add a plugin

Open a pull request that adds the plugin to the appropriate category in `README.md`. Include its current GitHub Star count, license, one-sentence description, and installation command. Follow the format of the surrounding entries:

```markdown
- [Project Name](https://github.com/owner/repository) - **123 stars** | `MIT`. A factual sentence that explains the plugin's DSH function.
  - Install: `dsh plugin --profile web add package-name`
```

Allowed categories are `Files & Runtime`, `Input & Navigation`, `Memory & Knowledge`, `Themes & Appearance`, `UI & Interfaces`, `Vision`, and `Workflow & Automation`.

Place the entry according to its exact current Star count, in descending order within its category. Use alphabetical order for ties. Star counts in the list are snapshots and are updated periodically.

Use the detected SPDX license identifier when one exists. Describe nonstandard terms or missing licenses plainly.

## Verification evidence

Include links in the pull request to:

- The manifest that declares `dsh.bundle`.
- The bundle patch or Cordis configuration.
- The plugin source entry.
- The documented installation command.
- Compatibility information for the DSH versions the plugin supports.

Describe any required companion app, service, credential, platform, or build step.

## Update or remove an entry

Submit corrections when a project moves, changes its package, loses its bundle, changes its license, becomes archived, or stops working with a supported DSH version. An entry that later drops below 30 Stars stays listed until a maintainer reviews it.

## Check your change

Check that the repository link and installation command are correct, the entry is in the appropriate category, and the description matches the source. Confirm that the entry is not already listed. Keep each pull request focused on one plugin or one related correction.

## Writing style

- Use standard American English.
- State what the plugin does in one sentence.
- End the description with a period.
- Avoid slogans, unsupported comparisons, feature dumps, and copied marketing text.
