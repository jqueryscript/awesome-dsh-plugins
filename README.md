# Awesome DeepSeek Harness Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A verified, star-ranked list of community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).

[![Quality](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml)
[![Update Stars](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml)

**Last verified:** 2026-08-17 | **Minimum at admission:** 50 stars | **Plugins:** 52

## Contents

- [What qualifies](#what-qualifies)
- [Ranked plugins](#ranked-plugins)
- [Install plugins carefully](#install-plugins-carefully)
- [Related resources](#related-resources)

## What qualifies

Every listed project has at least 50 GitHub Stars at admission and a public repository with an identifiable `dsh.bundle` manifest, bundle patch, plugin entry, and documented installation path. Multi-platform projects qualify only when they ship a separate DSH bundle.

The `dsh-plugin` GitHub topic is a discovery signal, not proof. This list excludes topic-only repositories, generic Skills, standalone clients without a bundle, MCP servers without a DSH package, API wrappers, presets, tutorials, Awesome lists, archived repositories, and minimally changed forks.

## Ranked plugins

Entries are sorted by exact live GitHub Stars. The displayed count is shortened only after sorting.

<!-- BEGIN GENERATED RANKING -->
- [iPolloWork Design Studio](https://github.com/Devin-AXIS/iPolloWork) - **4.1k stars** | `UI & Interfaces` | `Custom source-available`. A native DSH Design view for creating and editing visual documents inside the Harness conversation.
  - Install: `dsh plugin --profile web add deepseek-idesign`
- [DSH Web UI](https://github.com/zhu1090093659/dsh-web-ui) - **3.6k stars** | `UI & Interfaces` | `Apache-2.0`. A Web UI bundle with a task board, Git graph, remote access, live statistics, pets, skins, and image tools.
  - Install: `dsh plugin --profile web add @linxin666/dsh-web-ui-all`
- [Mirage DSH](https://github.com/strukto-ai/mirage) - **3.5k stars** | `Files & Runtime` | `Apache-2.0`. A DSH filesystem and shell provider that mounts remote and local resources inside one virtual workspace.
  - Install: `dsh plugin --profile web add @struktoai/mirage-dsh`
- [Modlens](https://github.com/liustack/modlens) - **2.5k stars** | `Vision` | `MIT`. A vision plugin that returns structured OCR, layout, and semantic evidence to text-only DSH models.
  - Install: `dsh plugin --profile web add @liustack/modlens@3.16.6`
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - **1.7k stars** | `UI & Interfaces` | `MIT`. A Web UI workbench with file editing, terminal access, Git tools, subagent views, and extension tabs.
  - Install: `dsh plugin --profile web add dsh-better-sidebar`
- [DSH TUI](https://github.com/ccch1mneyyy/dsh-TUI) - **1.6k stars** | `UI & Interfaces` | `MIT`. A full-screen terminal interface with streaming output, a status line, rollback controls, and context usage indicators.
  - Install: `dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui`
- [DSH Deep Whale](https://github.com/Small-tailqwq/dsh-deep-whale) - **1.1k stars** | `Themes & Appearance` | `CC-BY-NC-SA-4.0`. A maid-atelier whale character skin for the DSH Web interface.
  - Install: `git clone https://github.com/Small-tailqwq/dsh-deep-whale.git && dsh plugin --profile web add ./dsh-deep-whale/maid-atelier`
- [Working Activity](https://github.com/ccch1mneyyy/working-activity) - **646 stars** | `UI & Interfaces` | `MIT`. A live status line that shows model activity, running tools, elapsed time, and turn summaries in DSH.
  - Install: `dsh plugin --profile web add dsh-working-activity`
- [DSH Market](https://github.com/dsh-market/dsh-market) - **627 stars** | `UI & Interfaces` | `MIT`. A visual DSH plugin market for browsing, searching, installing, updating, and switching community plugins and themes.
  - Install: `dsh plugin --profile web add dshmarket`
- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) - **608 stars** | `Files & Runtime` | `Apache-2.0`. A DSH bundle that connects the managed-agents runtime through the official stdio MCP client.
  - Install: `npm ci && npm run build:runtime && npm link && dsh plugin --profile web add managed-agents`
- [DSH Vision Toolkit](https://github.com/Anionex/dsh-vision-toolkit) - **551 stars** | `Vision` | `MIT`. A native vision bundle for image questions, long-screenshot OCR, UI reconstruction, grounding, and pixel comparison.
  - Install: `dsh plugin --profile web add @anionex/dsh-vision-toolkit`
- [Graph Memory](https://github.com/adoresever/graph-memory) - **529 stars** | `Memory & Knowledge` | `MIT`. A graph-based memory plugin for cross-session recall, PageRank, communities, and vector search in DSH.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.1.tgz`
- [DSH Vision Router](https://github.com/ysr666/dsh-vision-router) - **467 stars** | `Vision` | `MIT`. A vision routing plugin with image questions, grounding, crops, pixel comparison, OCR, and screenshot tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router`
- [DSH Ads](https://github.com/Nagi-ovo/dsh-ads) - **465 stars** | `Themes & Appearance` | `BSD-3-Clause`. A parody Web UI plugin that adds fake banner ads, popups, and small games styled after early portal sites.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-ads`
- [Mnemon](https://github.com/mnemon-dev/mnemon) - **464 stars** | `Memory & Knowledge` | `Apache-2.0`. A persistent memory plugin that supplies graph-based recall and cross-session knowledge to DSH agents.
  - Install: `dsh plugin --profile web add dsh-mnemon`
- [DSH Agent Teams](https://github.com/NanmiCoder/dsh-agent-teams) - **432 stars** | `Workflow & Automation` | `MIT`. A team orchestration plugin that adds tools for creating agent groups, assigning work, and tracking shared state.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-agent-teams`
- [Treg DSH](https://github.com/superdesigndev/treg) - **428 stars** | `Workflow & Automation` | `Apache-2.0 + additional terms`. A DSH bundle that exposes the Treg tool registry as an optional MCP connector and packaged Skill.
  - Install: `dsh plugin --profile web add github:superdesigndev/treg`
- [DSH At File](https://github.com/omdsh-dev/dsh-at-file) - **278 stars** | `Input & Navigation` | `MIT`. A composer extension for searching workspace paths with at-file mentions and attaching file contents to prompts.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.6.0.tar.gz`
- [DSH Browser](https://github.com/Lum1104/dsh-browser) - **214 stars** | `UI & Interfaces` | `MIT`. A Chrome side-panel integration with a DSH bridge for reading pages and operating supported browser content.
  - Install: `curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash`
- [Whale Girl](https://github.com/vlln/whale-girl) - **200 stars** | `Themes & Appearance` | `MIT`. A draggable Web UI desktop pet with interaction, feeding, progress, and persistent state.
  - Install: `dsh plugin --profile web add github:vlln/whale-girl#main`
- [DSH Tianshu TUI](https://github.com/huiliyi37/dsh-tianshu-tui) - **194 stars** | `UI & Interfaces` | `Apache-2.0`. A terminal interface that adds Tianshu workflows, evidence gates, TDD controls, and optional vision modules.
  - Install: `dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui`
- [DSH Visualize](https://github.com/Nagi-ovo/dsh-visualize) - **160 stars** | `UI & Interfaces` | `BSD-3-Clause`. An inline visualization plugin that renders interactive HTML fragments as sandboxed cards in DSH conversations.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-visualize`
- [Engramory](https://github.com/tinqiao-oss/engramory) - **154 stars** | `Memory & Knowledge` | `MIT`. A file-based DSH memory plugin that keeps human-readable notes in a versioned store with deterministic limits.
  - Install: `dsh plugin --profile web add dsh-engramory`
- [DSH GenUI](https://github.com/omdsh-dev/dsh-genui) - **148 stars** | `UI & Interfaces` | `MIT`. A DSH rendering plugin for interactive UI components, charts, forms, quizzes, diagrams, and 3D scenes.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-genui.git`
- [DSH Notes](https://github.com/zhaoolee/notes) - **142 stars** | `Memory & Knowledge` | `MIT`. A DSH tool plugin that exports agent output into a self-hosted Notes service.
  - Install: `dsh plugin --profile web add @zhaoolee/dsh-notes`
- [Anime Find](https://github.com/cocofhu/anime-find) - **130 stars** | `Workflow & Automation` | `MIT`. A DSH Web search plugin that gathers anime results into cards with metadata, resource links, and optional streaming views.
  - Install: `dsh plugin --profile web add github:cocofhu/anime-find`
- [ModSearch](https://github.com/liustack/modsearch) - **115 stars** | `Workflow & Automation` | `MIT`. A DSH web-search plugin that adds search, X search, and focused page reading through the ModSearch engine chain.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest`
- [DSH Context](https://github.com/bowenliang123/dsh-context) - **113 stars** | `Memory & Knowledge` | `Apache-2.0`. A context dashboard and /context command that show how DSH messages, tools, injections, compactions, and token usage evolve.
  - Install: `dsh plugin --profile web add dsh-context`
- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) - **101 stars** | `UI & Interfaces` | `MIT`. An OpenPencil plugin that lets DSH agents preview, inspect, and edit real multi-frame design documents.
  - Install: `pnpm dlx --package=@deepseek-ai/dsh@0.1.0-rc.6 dsh plugin --profile web add @zseven-w/dsh-openpencil@latest`
- [Argo DSH](https://github.com/taxueseek/argo) - **94 stars** | `Workflow & Automation` | `MIT`. A DSH profile bundle that mounts Argo search MCP tools and an evidence-oriented research workflow.
  - Install: `dsh plugin --profile web add "github:taxueseek/argo#main&path:packages/dsh-plugin"`
- [DSH Noema](https://github.com/ZSeven-W/dsh-noema) - **90 stars** | `Memory & Knowledge` | `MIT`. Durable Noema-backed memory for DSH with recall tools, cross-agent imports, and a settings page.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-noema@latest`
- [DSH Super Injector](https://github.com/yjh051108/dsh-super-injector) - **86 stars** | `Workflow & Automation` | `BSD-3-Clause`. A DSH development plugin for injecting, hot-reloading, and removing local plugin packages without a restart.
  - Install: `dsh plugin --profile web add github:yjh051108/dsh-super-injector`
- [Odai DSH Plugin](https://github.com/orziz/odai) - **84 stars** | `Workflow & Automation` | `MIT`. A profile-wide DSH governance and routing bundle with an embedded Odai skill and runtime.
  - Install: `dsh plugin --profile web add odai-dsh-plugin`
- [DSH Auto Mode](https://github.com/NanmiCoder/dsh-auto-mode) - **74 stars** | `Workflow & Automation` | `MIT`. A fail-closed permission policy plugin that classifies DSH tool calls before automatic execution.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-auto-mode`
- [AnySearch DSH](https://github.com/anysearch-team/anysearch-dsh) - **73 stars** | `Workflow & Automation` | `MIT`. Web search for DSH with source discovery, vertical search, bounded batch queries, and cleaned page content.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @anysearch/anysearch-dsh`
- [GAL View](https://github.com/Ayase34/gal-view) - **73 stars** | `UI & Interfaces` | `MIT`. A DSH Web conversation view with a Galgame-style layout and an editor for scene elements.
  - Install: `dsh plugin --profile web add github:Ayase34/gal-view#main`
- [DSH Dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - **69 stars** | `Themes & Appearance` | `See ASSET_LICENSE.md`. A desktop companion that reacts to DSH session events with a floating BigFish character and configurable behaviors.
  - Install: `pnpm exec dsh plugin --profile web add dsh-dafeiyu@alpha`
- [DSH Annotation](https://github.com/omdsh-dev/dsh-annotation) - **67 stars** | `Input & Navigation` | `MIT`. A DSH Web selection tool that annotates assistant text and sends numbered annotation blocks with a message.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git`
- [ForkProbe DSH](https://github.com/Jayden-X-L/forkprobe) - **66 stars** | `Workflow & Automation` | `MIT`. A native DSH plugin for comparing Skills on the same task and choosing a winner from a local report.
  - Install: `dsh plugin --profile web add "github:Jayden-X-L/forkprobe"`
- [DSH Turn Rewind](https://github.com/Anionex/dsh-turn-rewind) - **65 stars** | `Memory & Knowledge` | `BSD-3-Clause`. A DSH recovery plugin that records workspace changes and restores a conversation turn through its Change Ledger.
  - Install: `dsh plugin --profile web add @anionex/dsh-turn-rewind`
- [DSH Liang Intensity Skin](https://github.com/kingOfSoySauce/dsh-liang-skin) - **64 stars** | `Themes & Appearance` | `No standard license`. An optional DSH Web skin that adds an adaptive reasoning-intensity slider and themed model-selection visuals.
  - Install: `dsh plugin --profile web add github:kingOfSoySauce/dsh-liang-skin#v0.1.4`
- [DSH Pet](https://github.com/PC2005-cloud/dsh-pet) - **63 stars** | `Themes & Appearance` | `MIT`. A floating DSH Web desktop pet with idle animations, random actions, screen wandering, and drag interactions.
  - Install: `dsh plugin --profile web add dsh-pet`
- [DSH Workflow](https://github.com/omdsh-dev/dsh_workflow) - **63 stars** | `Workflow & Automation` | `MIT`. A reusable DSH workflow layer for multi-agent runs with saved plans, approvals, background jobs, and resumable execution.
  - Install: `dsh plugin --profile web add github:dsh-external/dsh_workflow#main`
- [DSH Undo Savepoint](https://github.com/lire1131/dsh-undo-plugin) - **56 stars** | `Files & Runtime` | `MIT`. Crash recovery for DSH that snapshots configuration and plugin code for undo, redo, rollback, and safe-mode starts.
  - Install: `dsh plugin --profile web add github:lire1131/dsh-undo-plugin#master`
- [DSH Cost Meter](https://github.com/Han-1413141/dsh-cost-meter) - **55 stars** | `Workflow & Automation` | `MIT`. Session cost tracking for DSH with daily totals, history, budget views, and synchronized model pricing.
  - Install: `dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.3.1`
- [DSH Notification](https://github.com/omdsh-dev/dsh-notification) - **55 stars** | `UI & Interfaces` | `MIT`. Browser desktop notifications for completed DSH turns with outcome toggles and keyword include or exclude rules.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.2.tar.gz`
- [DSH Usage Stats](https://github.com/Ychris12138/dsh-usage-stats) - **55 stars** | `Workflow & Automation` | `MIT`. A DSH Web dashboard for token usage, provider balances, subscription quotas, and historical activity.
  - Install: `dsh plugin --profile web add github:Ychris12138/dsh-usage-stats`
- [DSH Vision](https://github.com/oil-oil/dsh-vision) - **55 stars** | `Vision` | `MIT`. Vision tools for DSH that preserve native image input and bridge text-only models to an external vision model.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision`
- [DSH QQ Bot](https://github.com/tencent-connect/dsh-qqbot) - **53 stars** | `Workflow & Automation` | `MIT`. A QQ Bot channel for DSH that handles messaging, QR-code login, session events, and agent replies.
  - Install: `npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot`
- [DSH Toy](https://github.com/c3ll256/dsh-toy) - **53 stars** | `Workflow & Automation` | `BSD-3-Clause`. Safety-bounded DSH control for Buttplug and Intiface devices with optional MonsterParty toy integration.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy`
- [DSH Reasoning Effort](https://github.com/HanaAyane/dsh-reasoning-effort) - **52 stars** | `UI & Interfaces` | `MIT`. Model and reasoning-effort controls for DSH with a slider, model-advertised levels, and themed selector views.
  - Install: `dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main`
- [DSH Web Plugin Manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - **52 stars** | `UI & Interfaces` | `MIT`. A DSH Web plugin manager with install guards, health checks, rollback, environment controls, and marketplace browsing.
  - Install: `dsh plugin --profile web add dsh-web-plugin-manager@latest`
<!-- END GENERATED RANKING -->

## Install plugins carefully

DSH plugins run third-party code with your account permissions. A plugin can read files, access environment variables, start processes, and use the network. Inclusion confirms the repository shape and installation evidence; it is not a security audit. Read the source and install unfamiliar plugins in an isolated workspace without production credentials.

## Related resources

- [DeepSeek Harness documentation](https://deepseek-harness.github.io/deepseek-harness/) - Official installation, configuration, and development guides.
- [Official `dsh-plugin` topic](https://github.com/topics/dsh-plugin) - A discovery feed that still requires code-level verification.
- [ScriptByAI](https://www.scriptbyai.com/) - AI tools, coding agents, and practical technical guides.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request. Additions must provide code-level DSH evidence and meet the admission threshold.
