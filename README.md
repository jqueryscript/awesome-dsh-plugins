# Awesome DeepSeek Harness Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A verified, star-ranked list of community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).

[![Quality](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml)
[![Update Stars](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml)

**Last verified:** 2026-08-19 | **Minimum at admission:** 30 stars | **Plugins:** 91

## Contents

- [What qualifies](#what-qualifies)
- [Ranked plugins](#ranked-plugins)
- [Install plugins carefully](#install-plugins-carefully)
- [Related resources](#related-resources)

## What qualifies

Every listed project has at least 30 GitHub Stars at admission and a public repository with an identifiable `dsh.bundle` manifest, bundle patch, plugin entry, and documented installation path. Multi-platform projects qualify only when they ship a separate DSH bundle.

The `dsh-plugin` GitHub topic is a discovery signal, not proof. This list excludes topic-only repositories, generic Skills, standalone clients without a bundle, MCP servers without a DSH package, API wrappers, presets, tutorials, Awesome lists, archived repositories, and minimally changed forks.

## Ranked plugins

Entries are sorted by exact live GitHub Stars. The displayed count is shortened only after sorting.

<!-- BEGIN GENERATED RANKING -->
- [DSH Web UI](https://github.com/zhu1090093659/dsh-web-ui) - **4.6k stars** | `UI & Interfaces` | `Apache-2.0`. A Web UI bundle with a task board, Git graph, remote access, live statistics, pets, skins, and image tools.
  - Install: `dsh plugin --profile web add @linxin666/dsh-web-ui-all`
- [iPolloWork Design Studio](https://github.com/Devin-AXIS/iPolloWork) - **4.2k stars** | `UI & Interfaces` | `Custom source-available`. A native DSH Design view for creating and editing visual documents inside the Harness conversation.
  - Install: `dsh plugin --profile web add deepseek-idesign`
- [Mirage DSH](https://github.com/strukto-ai/mirage) - **3.5k stars** | `Files & Runtime` | `Apache-2.0`. A DSH filesystem and shell provider that mounts remote and local resources inside one virtual workspace.
  - Install: `dsh plugin --profile web add @struktoai/mirage-dsh`
- [Modlens](https://github.com/liustack/modlens) - **3.1k stars** | `Vision` | `MIT`. A vision plugin that returns structured OCR, layout, and semantic evidence to text-only DSH models.
  - Install: `dsh plugin --profile web add @liustack/modlens@3.16.6`
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - **2.2k stars** | `UI & Interfaces` | `MIT`. A Web UI workbench with file editing, terminal access, Git tools, subagent views, and extension tabs.
  - Install: `dsh plugin --profile web add dsh-better-sidebar`
- [DSH TUI](https://github.com/ccch1mneyyy/dsh-TUI) - **2k stars** | `UI & Interfaces` | `MIT`. A full-screen terminal interface with streaming output, a status line, rollback controls, and context usage indicators.
  - Install: `dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui`
- [DSH Deep Whale](https://github.com/Small-tailqwq/dsh-deep-whale) - **1.4k stars** | `Themes & Appearance` | `CC-BY-NC-SA-4.0`. A maid-atelier whale character skin for the DSH Web interface.
  - Install: `git clone https://github.com/Small-tailqwq/dsh-deep-whale.git && dsh plugin --profile web add ./dsh-deep-whale/maid-atelier`
- [DSH Market](https://github.com/dsh-market/dsh-market) - **1.1k stars** | `UI & Interfaces` | `MIT`. A visual DSH plugin market for browsing, searching, installing, updating, and switching community plugins and themes.
  - Install: `dsh plugin --profile web add dshmarket`
- [DSH Vision Router](https://github.com/ysr666/dsh-vision-router) - **771 stars** | `Vision` | `MIT`. A vision routing plugin with image questions, grounding, crops, pixel comparison, OCR, and screenshot tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router`
- [DSH Vision Toolkit](https://github.com/Anionex/dsh-vision-toolkit) - **711 stars** | `Vision` | `MIT`. A native vision bundle for image questions, long-screenshot OCR, UI reconstruction, grounding, and pixel comparison.
  - Install: `dsh plugin --profile web add @anionex/dsh-vision-toolkit`
- [Working Activity](https://github.com/ccch1mneyyy/working-activity) - **653 stars** | `UI & Interfaces` | `MIT`. A live status line that shows model activity, running tools, elapsed time, and turn summaries in DSH.
  - Install: `dsh plugin --profile web add dsh-working-activity`
- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) - **621 stars** | `Files & Runtime` | `Apache-2.0`. A DSH bundle that connects the managed-agents runtime through the official stdio MCP client.
  - Install: `npm ci && npm run build:runtime && npm link && dsh plugin --profile web add managed-agents`
- [DSH Agent Teams](https://github.com/NanmiCoder/dsh-agent-teams) - **569 stars** | `Workflow & Automation` | `MIT`. A team orchestration plugin that adds tools for creating agent groups, assigning work, and tracking shared state.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-agent-teams`
- [Graph Memory](https://github.com/adoresever/graph-memory) - **550 stars** | `Memory & Knowledge` | `MIT`. A graph-based memory plugin for cross-session recall, PageRank, communities, and vector search in DSH.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.1.tgz`
- [DSH Ads](https://github.com/Nagi-ovo/dsh-ads) - **500 stars** | `Themes & Appearance` | `BSD-3-Clause`. A parody Web UI plugin that adds fake banner ads, popups, and small games styled after early portal sites.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-ads`
- [Mnemon](https://github.com/mnemon-dev/mnemon) - **484 stars** | `Memory & Knowledge` | `Apache-2.0`. A persistent memory plugin that supplies graph-based recall and cross-session knowledge to DSH agents.
  - Install: `dsh plugin --profile web add dsh-mnemon`
- [Treg DSH](https://github.com/superdesigndev/treg) - **477 stars** | `Workflow & Automation` | `Apache-2.0 + additional terms`. A DSH bundle that exposes the Treg tool registry as an optional MCP connector and packaged Skill.
  - Install: `dsh plugin --profile web add github:superdesigndev/treg`
- [DSH Context](https://github.com/bowenliang123/dsh-context) - **413 stars** | `Memory & Knowledge` | `Apache-2.0`. A context dashboard and /context command that show how DSH messages, tools, injections, compactions, and token usage evolve.
  - Install: `dsh plugin --profile web add dsh-context`
- [DSH At File](https://github.com/omdsh-dev/dsh-at-file) - **393 stars** | `Input & Navigation` | `MIT`. A composer extension for searching workspace paths with at-file mentions and attaching file contents to prompts.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.6.0.tar.gz`
- [DSH Browser](https://github.com/Lum1104/dsh-browser) - **302 stars** | `UI & Interfaces` | `MIT`. A Chrome side-panel integration with a DSH bridge for reading pages and operating supported browser content.
  - Install: `curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash`
- [DSH Transparent UI](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - **295 stars** | `Themes & Appearance` | `MIT`. A Web UI theme with adjustable glass effects, fluid or wallpaper backgrounds, and appearance controls for the DSH interface.
  - Install: `dsh plugin --profile web add dsh-client-ui-aqua`
- [Whale Girl](https://github.com/vlln/whale-girl) - **240 stars** | `Themes & Appearance` | `MIT`. A draggable Web UI desktop pet with interaction, feeding, progress, and persistent state.
  - Install: `dsh plugin --profile web add github:vlln/whale-girl#main`
- [DSH GenUI](https://github.com/omdsh-dev/dsh-genui) - **224 stars** | `UI & Interfaces` | `MIT`. A DSH rendering plugin for interactive UI components, charts, forms, quizzes, diagrams, and 3D scenes.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-genui.git`
- [DSH Tianshu TUI](https://github.com/huiliyi37/dsh-tianshu-tui) - **216 stars** | `UI & Interfaces` | `Apache-2.0`. A terminal interface that adds Tianshu workflows, evidence gates, TDD controls, and optional vision modules.
  - Install: `dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui`
- [Pilot Harness Bundles](https://github.com/op7418/pilot-harness) - **191 stars** | `UI & Interfaces` | `MIT`. A suite of separately installable DSH Web bundles for a CodePilot-style theme, workspace file tree, schedule summary, and session-log export.
  - Install: `dsh plugin --profile web add https://github.com/op7418/pilot-harness/releases/latest/download/deepseek-ai-dsh-ui-worktree-0.1.0-rc.5.tgz`
- [DSH Visualize](https://github.com/Nagi-ovo/dsh-visualize) - **180 stars** | `UI & Interfaces` | `BSD-3-Clause`. An inline visualization plugin that renders interactive HTML fragments as sandboxed cards in DSH conversations.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-visualize`
- [Engramory](https://github.com/tinqiao-oss/engramory) - **160 stars** | `Memory & Knowledge` | `MIT`. A file-based DSH memory plugin that keeps human-readable notes in a versioned store with deterministic limits.
  - Install: `dsh plugin --profile web add dsh-engramory`
- [DSH Pet](https://github.com/PC2005-cloud/dsh-pet) - **159 stars** | `Themes & Appearance` | `MIT`. A floating DSH Web desktop pet with idle animations, random actions, screen wandering, and drag interactions.
  - Install: `dsh plugin --profile web add dsh-pet`
- [DSH Dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - **158 stars** | `Themes & Appearance` | `See ASSET_LICENSE.md`. A desktop companion that reacts to DSH session events with a floating BigFish character and configurable behaviors.
  - Install: `pnpm exec dsh plugin --profile web add dsh-dafeiyu@alpha`
- [ModSearch](https://github.com/liustack/modsearch) - **152 stars** | `Workflow & Automation` | `MIT`. A DSH web-search plugin that adds search, X search, and focused page reading through the ModSearch engine chain.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest`
- [Anime Find](https://github.com/cocofhu/anime-find) - **149 stars** | `Workflow & Automation` | `MIT`. A DSH Web search plugin that gathers anime results into cards with metadata, resource links, and optional streaming views.
  - Install: `dsh plugin --profile web add github:cocofhu/anime-find`
- [DSH Notes](https://github.com/zhaoolee/notes) - **147 stars** | `Memory & Knowledge` | `MIT`. A DSH tool plugin that exports agent output into a self-hosted Notes service.
  - Install: `dsh plugin --profile web add @zhaoolee/dsh-notes`
- [DSH Plugin Subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - **129 stars** | `Workflow & Automation` | `MIT`. An OAuth-based provider plugin that connects ChatGPT, Claude, and Grok subscriptions to DSH without separate API keys.
  - Install: `dsh plugin --profile web add dsh-plugin-subscriptions`
- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) - **119 stars** | `UI & Interfaces` | `MIT`. An OpenPencil plugin that lets DSH agents preview, inspect, and edit real multi-frame design documents.
  - Install: `pnpm dlx --package=@deepseek-ai/dsh@0.1.0-rc.6 dsh plugin --profile web add @zseven-w/dsh-openpencil@latest`
- [DSH Super Injector](https://github.com/yjh051108/dsh-super-injector) - **116 stars** | `Workflow & Automation` | `BSD-3-Clause`. A DSH development plugin for injecting, hot-reloading, and removing local plugin packages without a restart.
  - Install: `dsh plugin --profile web add github:yjh051108/dsh-super-injector`
- [AnySearch DSH](https://github.com/anysearch-team/anysearch-dsh) - **113 stars** | `Workflow & Automation` | `MIT`. Web search for DSH with source discovery, vertical search, bounded batch queries, and cleaned page content.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @anysearch/anysearch-dsh`
- [DSH Noema](https://github.com/ZSeven-W/dsh-noema) - **110 stars** | `Memory & Knowledge` | `MIT`. Durable Noema-backed memory for DSH with recall tools, cross-agent imports, and a settings page.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-noema@latest`
- [DSH Auto Mode](https://github.com/NanmiCoder/dsh-auto-mode) - **103 stars** | `Workflow & Automation` | `MIT`. A fail-closed permission policy plugin that classifies DSH tool calls before automatic execution.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-auto-mode`
- [DSH Liang Intensity Skin](https://github.com/kingOfSoySauce/dsh-liang-skin) - **103 stars** | `Themes & Appearance` | `No standard license`. An optional DSH Web skin that adds an adaptive reasoning-intensity slider and themed model-selection visuals.
  - Install: `dsh plugin --profile web add github:kingOfSoySauce/dsh-liang-skin#v0.1.4`
- [Argo DSH](https://github.com/taxueseek/argo) - **101 stars** | `Workflow & Automation` | `MIT`. A DSH profile bundle that mounts Argo search MCP tools and an evidence-oriented research workflow.
  - Install: `dsh plugin --profile web add "github:taxueseek/argo#main&path:packages/dsh-plugin"`
- [GAL View](https://github.com/Ayase34/gal-view) - **101 stars** | `UI & Interfaces` | `MIT`. A DSH Web conversation view with a Galgame-style layout and an editor for scene elements.
  - Install: `dsh plugin --profile web add github:Ayase34/gal-view#main`
- [DSH Cost Meter](https://github.com/Han-1413141/dsh-cost-meter) - **97 stars** | `Workflow & Automation` | `MIT`. Session cost tracking for DSH with daily totals, history, budget views, and synchronized model pricing.
  - Install: `dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.3.1`
- [Odai DSH Plugin](https://github.com/orziz/odai) - **89 stars** | `Workflow & Automation` | `MIT`. A profile-wide DSH governance and routing bundle with an embedded Odai skill and runtime.
  - Install: `dsh plugin --profile web add odai-dsh-plugin`
- [DSH Web UI Market](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - **87 stars** | `UI & Interfaces` | `MIT`. A Web UI marketplace for browsing the curated DSH catalog and installing or removing plugins from a profile.
  - Install: `dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin`
- [Tabbit Browser](https://github.com/Tabbit-Browser/dsh-plugin) - **86 stars** | `UI & Interfaces` | `MIT`. A DSH bundle that exposes Tabbit Browser skills and host tools through the Web profile.
  - Install: `dsh plugin --profile web add github:Tabbit-Browser/dsh-plugin`
- [DSH Undo Savepoint](https://github.com/lire1131/dsh-undo-plugin) - **85 stars** | `Files & Runtime` | `MIT`. Crash recovery for DSH that snapshots configuration and plugin code for undo, redo, rollback, and safe-mode starts.
  - Install: `dsh plugin --profile web add github:lire1131/dsh-undo-plugin#master`
- [DSH Agent Team GUI](https://github.com/toolclub/dsh-agent-team-gui) - **83 stars** | `Workflow & Automation` | `MIT`. Persistent multi-model teams for DSH with durable orchestration, DAG workflows, run history, and provider-reported usage.
  - Install: `dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v0.5.0`
- [DSH Turn Rewind](https://github.com/Anionex/dsh-turn-rewind) - **83 stars** | `Memory & Knowledge` | `BSD-3-Clause`. A DSH recovery plugin that records workspace changes and restores a conversation turn through its Change Ledger.
  - Install: `dsh plugin --profile web add @anionex/dsh-turn-rewind`
- [DSH Reasoning Effort](https://github.com/HanaAyane/dsh-reasoning-effort) - **82 stars** | `UI & Interfaces` | `MIT`. Model and reasoning-effort controls for DSH with a slider, model-advertised levels, and themed selector views.
  - Install: `dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main`
- [DSH Workflow](https://github.com/omdsh-dev/dsh_workflow) - **82 stars** | `Workflow & Automation` | `MIT`. A reusable DSH workflow layer for multi-agent runs with saved plans, approvals, background jobs, and resumable execution.
  - Install: `dsh plugin --profile web add github:dsh-external/dsh_workflow#main`
- [DSH Annotation](https://github.com/omdsh-dev/dsh-annotation) - **76 stars** | `Input & Navigation` | `MIT`. A DSH Web selection tool that annotates assistant text and sends numbered annotation blocks with a message.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git`
- [DSH Usage Stats](https://github.com/Ychris12138/dsh-usage-stats) - **75 stars** | `Workflow & Automation` | `MIT`. A DSH Web dashboard for token usage, provider balances, subscription quotas, and historical activity.
  - Install: `dsh plugin --profile web add github:Ychris12138/dsh-usage-stats`
- [ZAT DSH Engine](https://github.com/mishibeikejie/zat-dsh-engine) - **73 stars** | `UI & Interfaces` | `MIT`. A Web UI marketplace for searching, installing, updating, and rolling back community DSH plugins.
  - Install: `dsh plugin --profile web add github:mishibeikejie/zat-dsh-engine`
- [DSH Chat Import](https://github.com/Nwflower/dsh-chat-import) - **71 stars** | `Memory & Knowledge` | `MIT`. A conversation migration plugin that imports histories from external agent tools into resumable DSH sessions and exports them back.
  - Install: `dsh plugin --profile web add dsh-chat-import`
- [Dockyard DSH](https://github.com/AITabby/dockyard-dsh) - **69 stars** | `Workflow & Automation` | `MIT`. A native DSH provider plugin with account pools, OAuth sign-in, model catalogs, quota status, and provider-specific requests.
  - Install: `dsh plugin --profile web add github:AITabby/dockyard-dsh`
- [DSH Vision](https://github.com/oil-oil/dsh-vision) - **68 stars** | `Vision` | `MIT`. Vision tools for DSH that preserve native image input and bridge text-only models to an external vision model.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision`
- [ForkProbe DSH](https://github.com/Jayden-X-L/forkprobe) - **67 stars** | `Workflow & Automation` | `MIT`. A native DSH plugin for comparing Skills on the same task and choosing a winner from a local report.
  - Install: `dsh plugin --profile web add "github:Jayden-X-L/forkprobe"`
- [DSH Skill & MCP Panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) - **66 stars** | `UI & Interfaces` | `MIT`. A Web settings panel for managing DSH Skills and MCP servers through profile configuration.
  - Install: `dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.1/dsh-skill-mcp-panel-2.0.1.tgz`
- [DSH Image Gen](https://github.com/shanliuling/dsh-image-gen) - **63 stars** | `Vision` | `MIT`. A Web plugin that adds image-generation tools and settings to DeepSeek Harness conversations.
  - Install: `dsh plugin --profile web add dsh-image-gen`
- [DSH CommandCode Provider](https://github.com/Mars-Sea/dsh-commandcode-provider) - **62 stars** | `Workflow & Automation` | `MIT`. An LLM provider plugin that adds a live Command Code model catalog, reasoning controls, and a Models-page card to DSH.
  - Install: `dsh plugin --profile web add @mars-sea/dsh-commandcode-provider`
- [DSH QQ Bot](https://github.com/tencent-connect/dsh-qqbot) - **62 stars** | `Workflow & Automation` | `MIT`. A QQ Bot channel for DSH that handles messaging, QR-code login, session events, and agent replies.
  - Install: `npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot`
- [DSH Notification](https://github.com/omdsh-dev/dsh-notification) - **61 stars** | `UI & Interfaces` | `MIT`. Browser desktop notifications for completed DSH turns with outcome toggles and keyword include or exclude rules.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.2.tar.gz`
- [DSH Crew](https://github.com/ZSeven-W/dsh-crew) - **59 stars** | `Workflow & Automation` | `MIT`. A DSH hub for dispatching work to native subagents, tracking progress, and bridging Claude Code or Codex workers.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-crew@latest`
- [DSH Automation](https://github.com/titanwings/dsh-automation) - **58 stars** | `Workflow & Automation` | `MIT`. Scheduled coding runs for DSH with Web and agent controls, durable history, and guarded execution boundaries.
  - Install: `dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.6`
- [DSH Dream Skin](https://github.com/RevolutionLA/dsh-dream-skin) - **58 stars** | `Themes & Appearance` | `MIT`. A Web UI skin pack with animated themes, wallpapers, accents, import/export, and persistent per-user appearance settings.
  - Install: `dsh plugin --profile web add dsh-dream-skin`
- [DSH Plugin Finder](https://github.com/awesome-dsh-plugin/dsh-find-plugin) - **58 stars** | `Workflow & Automation` | `MIT`. Searches GitHub's DSH plugin ecosystem from inside a session and returns ranked results with ready-to-run install commands.
  - Install: `dsh plugin --profile web add dsh-find-plugin`
- [DSH Web Plugin Manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - **58 stars** | `UI & Interfaces` | `MIT`. A DSH Web plugin manager with install guards, health checks, rollback, environment controls, and marketplace browsing.
  - Install: `dsh plugin --profile web add dsh-web-plugin-manager@latest`
- [DSH Plugin Store](https://github.com/ZASENJC/dsh-plugins-store) - **56 stars** | `UI & Interfaces` | `MIT`. A Web plugin that lets users browse, validate, install, update, and remove community DSH plugins after confirmation.
  - Install: `dsh plugin --profile web add npm:dsh-plugins-store`
- [DSH Toy](https://github.com/c3ll256/dsh-toy) - **56 stars** | `Workflow & Automation` | `BSD-3-Clause`. Safety-bounded DSH control for Buttplug and Intiface devices with optional MonsterParty toy integration.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy`
- [DSH Data Agent](https://github.com/omdsh-dev/dsh-data-agent) - **55 stars** | `Workflow & Automation` | `MIT`. Database connections, masked forms, SQL tools, and a shared data-analysis preset for DSH Web and TUI.
  - Install: `dsh plugin --profile web add @yejiming/dsh-data-agent`
- [DSH IM](https://github.com/xmanrui/dsh-im) - **54 stars** | `Workflow & Automation` | `MIT`. A single DSH settings plugin for connecting Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord, and WhatsApp bots.
  - Install: `dsh plugin --profile web add @xmanrui/dsh-im`
- [DSH Plugin Console](https://github.com/Noob-stupid/dsh-plugin-hub) - **54 stars** | `UI & Interfaces` | `MIT`. A DSH settings panel for enabling, disabling, inspecting, and installing community plugins from multiple sources.
  - Install: `dsh plugin --profile web add github:Noob-stupid/dsh-plugin-hub`
- [Local Shell MCP](https://github.com/fwerkor/local-shell-mcp) - **50 stars** | `Files & Runtime` | `MIT`. A DSH bridge for local-shell-mcp that exposes shell, files, browser, and remote-worker tools through per-session connections.
  - Install: `dsh plugin --profile web add 'github:fwerkor/local-shell-mcp#main'`
- [Open in VS Code](https://github.com/omdsh-dev/dsh-open-in-vscode) - **50 stars** | `Input & Navigation` | `MIT`. Adds a workspace-row action that opens the selected DSH directory in VS Code or another configured editor.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz`
- [DSH Stock Watch](https://github.com/Awu12277/dsh-stock-watch) - **49 stars** | `UI & Interfaces` | `MIT`. A Web UI stock monitor with watchlists, groups, intraday and candlestick charts, target prices, and a draggable panel.
  - Install: `dsh plugin --profile web add dsh-stock-watch`
- [Morning Star DSH](https://github.com/btspoony/mstar-harness) - **49 stars** | `Workflow & Automation` | `MIT`. In-process DSH workflow gates that validate status, control dispatch, and expose the Morning Star engine through refusal-aware channels.
  - Install: `dsh plugin --profile web add @mstar-harness/dsh`
- [DSH Agent Workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) - **48 stars** | `Workflow & Automation` | `MIT`. A Web UI plugin that presents model requests, responses, and tool calls as a navigable workflow for each DSH conversation.
  - Install: `dsh plugin --profile web add github:xuanyuanzhifeng/dsh-plugin-agent-workflow#v0.1.0 --workspace-root`
- [DSH Balance Monitor](https://github.com/Francis-Xavier-code/dsh-balance-plugin) - **48 stars** | `Workflow & Automation` | `MIT`. Balance monitoring, usage statistics, and third-party plugin management in the DSH Web interface.
  - Install: `dsh plugin --profile web add github:Francis-Xavier-code/dsh-balance-plugin`
- [Multica DSH Runtime](https://github.com/multica-ai/dsh-multica-runtime) - **48 stars** | `Files & Runtime` | `No standard license`. A local DSH runtime bridge for Multica that exposes a versioned stdio protocol without patching the Harness source.
  - Install: `dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime`
- [DSH Notifier](https://github.com/THEWOLFWALKER/dsh-notifier) - **43 stars** | `Workflow & Automation` | `MIT`. A notification and remote-approval layer for DSH with one notify API, multiple channel adapters, and optional mobile controls.
  - Install: `dsh plugin add dsh-notifier --profile web`
- [DSH Harness Wallet](https://github.com/feibi-mochi/deepseek-harness-control-center) - **42 stars** | `Workflow & Automation` | `MIT`. A DSH Web plugin for account balances, usage tracking, completion alerts, recharge actions, and session controls.
  - Install: `dsh plugin --profile web add deepseek-harness-wallet`
- [DeepSeek Flow](https://github.com/kanghelyu/dsh-deepseek-flow) - **41 stars** | `Workflow & Automation` | `MIT`. A Markdown-first workflow editor for DSH with a synchronized canvas, Boolean gates, reviewable changes, and AI-assisted workflow maintenance.
  - Install: `dsh plugin --profile web add "github:kanghelyu/dsh-deepseek-flow#main"`
- [DSH Navbar](https://github.com/vlln/dsh-navbar) - **41 stars** | `Input & Navigation` | `MIT`. A conversation node bar that lets users jump quickly between user messages in the DSH Web view.
  - Install: `dsh plugin --profile web add @vlln/dsh-navbar`
- [OpenMA DSH TUI](https://github.com/openma-ai/deepseek-harness-tui) - **41 stars** | `UI & Interfaces` | `MIT`. A terminal-native DSH profile with an ACP plugin tree, streamed sessions, themes, overlays, and native TUI rendering.
  - Install: `npm install --global @openma/deepseek-harness-tui && dsh plugin --profile tui add @openma/deepseek-harness-tui`
- [DSH Status Label](https://github.com/alingalingling/ui-status-label) - **38 stars** | `UI & Interfaces` | `MIT`. Configurable running-turn status text for DSH Web, with a settings row and conversation-status provider.
  - Install: `dsh plugin --profile web add dsh-ui-status-label`
- [DSH MinerU](https://github.com/HuanLinOTO/dsh-plugin-mineru) - **37 stars** | `Files & Runtime` | `AGPL-3.0`. MinerU-backed document parsing tools that convert PDF, images, DOCX, PPTX, and XLSX files into structured Markdown or JSON.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-mineru`
- [DSH Interconnect](https://github.com/Chinesezjc/dsh-interconnect) - **34 stars** | `Workflow & Automation` | `MIT`. Cross-instance DSH messaging and event handoff with host services, model-facing tools, and shared-token authentication.
  - Install: `dsh plugin --profile web add dsh-interconnect`
- [DSH Lark](https://github.com/omdsh-dev/dsh-lark) - **34 stars** | `Workflow & Automation` | `BSD-3-Clause`. A Feishu/Lark channel for sending tasks to DSH agents and returning replies, approvals, and cards to chat.
  - Install: `dsh plugin --profile web add dsh-lark-channel@latest`
- [AX Feishu Bridge](https://github.com/AX1202/ax-feishu-bridge) - **32 stars** | `Workflow & Automation` | `MIT`. A Feishu/Lark bridge that lets users chat with Pi or DeepSeek Harness from the same messaging workspace.
  - Install: `dsh plugin --profile web add ax-feishu-bridge --ignore-scripts`
- [DSH Message Edit](https://github.com/Moeblack/dsh-message-edit) - **32 stars** | `Input & Navigation` | `MIT`. A conversation plugin for branching, editing, rerolling, retrying, and reviewing DSH message versions.
  - Install: `dsh plugin --profile web add dsh-message-edit`
- [DSH Web Mobile](https://github.com/mexiaosqwq/dsh-web-mobile) - **31 stars** | `UI & Interfaces` | `MIT`. A responsive Web UI plugin that adapts the DSH interface for narrow and portrait-oriented screens.
  - Install: `dsh plugin --profile web add github:mexiaosqwq/dsh-web-mobile`
<!-- END GENERATED RANKING -->

## Install plugins carefully

DSH plugins run third-party code with your account permissions. A plugin can read files, access environment variables, start processes, and use the network. Inclusion confirms the repository shape and installation evidence; it is not a security audit. Read the source and install unfamiliar plugins in an isolated workspace without production credentials.

## Related resources

- [DeepSeek Harness documentation](https://deepseek-harness.github.io/deepseek-harness/) - Official installation, configuration, and development guides.
- [Official `dsh-plugin` topic](https://github.com/topics/dsh-plugin) - A discovery feed that still requires code-level verification.
- [ScriptByAI](https://www.scriptbyai.com/) - AI tools, coding agents, and practical technical guides.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request. Additions must provide code-level DSH evidence and meet the admission threshold.
