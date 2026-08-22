# Awesome DeepSeek Harness Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A verified, star-ranked list of community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).

[![Quality](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml)
[![Update Stars](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml)

**Last verified:** 2026-08-22 | **Minimum at admission:** 30 stars | **Plugins:** 139

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
- [OpenViking Memory](https://github.com/volcengine/OpenViking) - **31.7k stars** | `Memory & Knowledge` | `Apache-2.0`. A DeepSeek Harness memory bundle with OpenViking auto-recall, session capture, protected viking:// URIs, and MCP tools.
  - Install: `dsh plugin --profile web add @openviking/dsh-memory-plugin`
- [WeKnora Knowledge](https://github.com/Tencent/WeKnora) - **20.3k stars** | `Memory & Knowledge` | `MIT`. A DeepSeek Harness bundle for semantic knowledge search, document reading, and RAG answers over user-managed knowledge bases.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/dsh-weknora`
- [EverOS Memory](https://github.com/EverMind-AI/EverOS) - **12.3k stars** | `Memory & Knowledge` | `Apache-2.0`. A DeepSeek Harness memory bundle that provides automatic cross-session recall through a local EverOS service.
  - Install: `dsh plugin --profile web add @evermind-ai/dsh-plugin`
- [MemOS Local Memory](https://github.com/MemTensor/MemOS) - **10.9k stars** | `Memory & Knowledge` | `MIT`. A local MemOS memory bundle for DeepSeek Harness with layered recall, reflection, policy induction, and skill crystallization.
  - Install: `curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/main/apps/memos-local-plugin/install.sh | bash -s -- --agent dsh --profile web`
- [Ouroboros](https://github.com/Q00/ouroboros) - **5.6k stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle that exposes the Ouroboros spec-first development workflow as native tools and chat commands.
  - Install: `dsh plugin --profile web add "github:Q00/ouroboros#main&path:integrations/dsh-plugin"`
- [DSH Web UI](https://github.com/zhu1090093659/dsh-web-ui) - **5.4k stars** | `UI & Interfaces` | `Apache-2.0`. A Web UI bundle with a task board, Git graph, remote access, live statistics, pets, skins, and image tools.
  - Install: `dsh plugin --profile web add @linxin666/dsh-web-ui-all`
- [iPolloWork Design Studio](https://github.com/Devin-AXIS/iPolloWork) - **4.4k stars** | `UI & Interfaces` | `Custom source-available`. A native DSH Design view for creating and editing visual documents inside the Harness conversation.
  - Install: `dsh plugin --profile web add deepseek-idesign`
- [Mirage DSH](https://github.com/strukto-ai/mirage) - **3.5k stars** | `Files & Runtime` | `Apache-2.0`. A DSH filesystem and shell provider that mounts remote and local resources inside one virtual workspace.
  - Install: `dsh plugin --profile web add @struktoai/mirage-dsh`
- [Modlens](https://github.com/liustack/modlens) - **3.5k stars** | `Vision` | `MIT`. A vision plugin that returns structured OCR, layout, and semantic evidence to text-only DSH models.
  - Install: `dsh plugin --profile web add @liustack/modlens@3.16.6`
- [ReMe](https://github.com/agentscope-ai/ReMe) - **3.3k stars** | `Memory & Knowledge` | `Apache-2.0`. A DeepSeek Harness memory bundle with recall, capture, settings, and skill guidance for TypeScript agent workflows.
  - Install: `dsh plugin --profile web add @agentscope-ai/reme`
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - **2.6k stars** | `UI & Interfaces` | `MIT`. A Web UI workbench with file editing, terminal access, Git tools, subagent views, and extension tabs.
  - Install: `dsh plugin --profile web add dsh-better-sidebar`
- [MemSearch](https://github.com/zilliztech/memsearch) - **2.5k stars** | `Memory & Knowledge` | `MIT`. A DeepSeek Harness memory bundle that captures shared Markdown notes, injects context before steps, and reviews candidate skills.
  - Install: `dsh plugin --profile web add @zilliz/memsearch-dsh`
- [Codex Taskboard DSH Integration](https://github.com/chuspeeism/dashi-taskboard) - **2.4k stars** | `Workflow & Automation` | `Apache-2.0`. A DeepSeek Harness bundle that adds a Taskboard sidebar entry and opens the installed Codex Taskboard runtime.
  - Install: `dsh plugin --profile web add /absolute/path/to/codex-taskboard/integrations/deepseek-harness`
- [DSH TUI](https://github.com/ccch1mneyyy/dsh-TUI) - **2.3k stars** | `UI & Interfaces` | `MIT`. A full-screen terminal interface with streaming output, a status line, rollback controls, and context usage indicators.
  - Install: `dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui`
- [DSH Market](https://github.com/dsh-market/dsh-market) - **1.7k stars** | `UI & Interfaces` | `MIT`. A visual DSH plugin market for browsing, searching, installing, updating, and switching community plugins and themes.
  - Install: `dsh plugin --profile web add dshmarket`
- [DSH Deep Whale](https://github.com/Small-tailqwq/dsh-deep-whale) - **1.6k stars** | `Themes & Appearance` | `CC-BY-NC-SA-4.0`. A maid-atelier whale character skin for the DSH Web interface.
  - Install: `git clone https://github.com/Small-tailqwq/dsh-deep-whale.git && dsh plugin --profile web add ./dsh-deep-whale/maid-atelier`
- [mem9](https://github.com/mem9-ai/mem9) - **1.2k stars** | `Memory & Knowledge` | `Apache-2.0`. A persistent memory bundle for DeepSeek Harness with automatic recall, background ingest, and five memory tools.
  - Install: `dsh plugin --profile web add @mem9/dsh-plugin`
- [Chorus DSH](https://github.com/Chorus-AIDLC/Chorus) - **1.1k stars** | `Workflow & Automation` | `AGPL-3.0`. A native DeepSeek Harness bundle for Chorus lifecycle automation, prompt behavior, MCP access, and AI-DLC skills.
  - Install: `dsh plugin --profile web add @chorus-aidlc/chorus-dsh -w`
- [Aegis](https://github.com/GanyuanRan/Aegis) - **1.1k stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle for the Aegis agent's guarded filesystem and skill workflows.
  - Install: `dsh plugin --profile web add github:GanyuanRan/Aegis`
- [DSH Vision Router](https://github.com/ysr666/dsh-vision-router) - **932 stars** | `Vision` | `MIT`. A vision routing plugin with image questions, grounding, crops, pixel comparison, OCR, and screenshot tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router`
- [TongFlow DSH Plugin](https://github.com/tong-io/tongflow) - **911 stars** | `Workflow & Automation` | `AGPL-3.0-only`. A multimodal workflow studio for generating and reviewing image, audio, video, and 3D assets from saved workflows inside DSH.
  - Install: `dsh plugin --profile web add dsh-tongflow`
- [DSH Vision Toolkit](https://github.com/Anionex/dsh-vision-toolkit) - **806 stars** | `Vision` | `MIT`. A native vision bundle for image questions, long-screenshot OCR, UI reconstruction, grounding, and pixel comparison.
  - Install: `dsh plugin --profile web add @anionex/dsh-vision-toolkit`
- [DSH Context](https://github.com/bowenliang123/dsh-context) - **768 stars** | `Memory & Knowledge` | `Apache-2.0`. A context dashboard and /context command that show how DSH messages, tools, injections, compactions, and token usage evolve.
  - Install: `dsh plugin --profile web add dsh-context`
- [DSH Agent Teams](https://github.com/NanmiCoder/dsh-agent-teams) - **764 stars** | `Workflow & Automation` | `MIT`. A team orchestration plugin that adds tools for creating agent groups, assigning work, and tracking shared state.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-agent-teams`
- [Working Activity](https://github.com/ccch1mneyyy/working-activity) - **654 stars** | `UI & Interfaces` | `MIT`. A live status line that shows model activity, running tools, elapsed time, and turn summaries in DSH.
  - Install: `dsh plugin --profile web add dsh-working-activity`
- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) - **628 stars** | `Files & Runtime` | `Apache-2.0`. A DSH bundle that connects the managed-agents runtime through the official stdio MCP client.
  - Install: `npm ci && npm run build:runtime && npm link && dsh plugin --profile web add managed-agents`
- [Graph Memory](https://github.com/adoresever/graph-memory) - **565 stars** | `Memory & Knowledge` | `MIT`. A graph-based memory plugin for cross-session recall, PageRank, communities, and vector search in DSH.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.1.tgz`
- [Treg DSH](https://github.com/superdesigndev/treg) - **555 stars** | `Workflow & Automation` | `Apache-2.0 + additional terms`. A DSH bundle that exposes the Treg tool registry as an optional MCP connector and packaged Skill.
  - Install: `dsh plugin --profile web add github:superdesigndev/treg`
- [DSH Ads](https://github.com/Nagi-ovo/dsh-ads) - **528 stars** | `Themes & Appearance` | `BSD-3-Clause`. A parody Web UI plugin that adds fake banner ads, popups, and small games styled after early portal sites.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-ads`
- [Mnemon](https://github.com/mnemon-dev/mnemon) - **501 stars** | `Memory & Knowledge` | `Apache-2.0`. A persistent memory plugin that supplies graph-based recall and cross-session knowledge to DSH agents.
  - Install: `dsh plugin --profile web add dsh-mnemon`
- [DSH At File](https://github.com/FSMargoo/dsh-at-file) - **449 stars** | `Input & Navigation` | `MIT`. A composer extension for searching workspace paths with at-file mentions and attaching file contents to prompts.
  - Install: `dsh plugin --profile web add https://github.com/FSMargoo/dsh-at-file/archive/refs/tags/v0.6.0.tar.gz`
- [DSH IM](https://github.com/xmanrui/dsh-im) - **430 stars** | `Workflow & Automation` | `MIT`. A single DSH settings plugin for connecting Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord, and WhatsApp bots.
  - Install: `dsh plugin --profile web add @xmanrui/dsh-im`
- [DSH Browser](https://github.com/Lum1104/dsh-browser) - **374 stars** | `UI & Interfaces` | `MIT`. A Chrome side-panel integration with a DSH bridge for reading pages and operating supported browser content.
  - Install: `curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash`
- [DSH Balance Whale](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) - **365 stars** | `Themes & Appearance` | `MIT`. A Web UI widget that displays DeepSeek account balance in a draggable whale companion.
  - Install: `dsh plugin --profile web add link:./dsh-whale-widget`
- [DSH Transparent UI](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - **359 stars** | `Themes & Appearance` | `MIT`. A Web UI theme with adjustable glass effects, fluid or wallpaper backgrounds, and appearance controls for the DSH interface.
  - Install: `dsh plugin --profile web add dsh-client-ui-aqua`
- [DSH Pocket](https://github.com/shaobeichen/dsh-pocket) - **354 stars** | `Input & Navigation` | `GPL-2.0`. A Web plugin that mirrors DSH sessions to a phone over a local network or a password-protected Cloudflare tunnel.
  - Install: `dsh plugin --profile web add dsh-pocket -w`
- [Flowix Memory](https://github.com/text2future/flowix) - **338 stars** | `Memory & Knowledge` | `MIT`. A config-only DSH bundle that exposes Flowix notebook memos and artifact tools through a local stdio MCP server.
  - Install: `dsh plugin --profile web add ./app/flowix-dsh-host/bundles/dsh-flowix-memory`
- [DSH Pet](https://github.com/PC2005-cloud/dsh-pet) - **294 stars** | `Themes & Appearance` | `MIT`. A floating DSH Web desktop pet with idle animations, random actions, screen wandering, and drag interactions.
  - Install: `dsh plugin --profile web add dsh-pet`
- [DSH GenUI](https://github.com/omdsh-dev/dsh-genui) - **287 stars** | `UI & Interfaces` | `MIT`. A DSH rendering plugin for interactive UI components, charts, forms, quizzes, diagrams, and 3D scenes.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-genui.git`
- [DeepSeek PPT Studio](https://github.com/Devin-AXIS/deepseek-design) - **264 stars** | `UI & Interfaces` | `Custom source-available`. A native DSH conversation view for creating, editing, templating, and exporting presentation slides.
  - Install: `dsh plugin --profile web add deepseek-ippt`
- [Whale Girl](https://github.com/vlln/whale-girl) - **261 stars** | `Themes & Appearance` | `MIT`. A draggable Web UI desktop pet with interaction, feeding, progress, and persistent state.
  - Install: `dsh plugin --profile web add github:vlln/whale-girl#main`
- [Pilot Harness Bundles](https://github.com/op7418/pilot-harness) - **251 stars** | `UI & Interfaces` | `MIT`. A suite of separately installable DSH Web bundles for a CodePilot-style theme, workspace file tree, schedule summary, and session-log export.
  - Install: `dsh plugin --profile web add https://github.com/op7418/pilot-harness/releases/latest/download/deepseek-ai-dsh-ui-worktree-0.1.0-rc.5.tgz`
- [DSH Tianshu TUI](https://github.com/huiliyi37/dsh-tianshu-tui) - **228 stars** | `UI & Interfaces` | `Apache-2.0`. A terminal interface that adds Tianshu workflows, evidence gates, TDD controls, and optional vision modules.
  - Install: `dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui`
- [DSH Plugin Subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - **225 stars** | `Workflow & Automation` | `MIT`. An OAuth-based provider plugin that connects ChatGPT, Claude, and Grok subscriptions to DSH without separate API keys.
  - Install: `dsh plugin --profile web add dsh-plugin-subscriptions`
- [DSH Dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - **223 stars** | `Themes & Appearance` | `See ASSET_LICENSE.md`. A desktop companion that reacts to DSH session events with a floating BigFish character and configurable behaviors.
  - Install: `pnpm exec dsh plugin --profile web add dsh-dafeiyu@alpha`
- [DSH Memory Evolve](https://github.com/csyangwen/dsh-memory-evolve) - **215 stars** | `Memory & Knowledge` | `MIT`. A Web DSH memory and workflow plugin with cross-session recall, skill management, todos, session search, and external-agent dispatch.
  - Install: `dsh plugin --profile web add github:csyangwen/dsh-memory-evolve`
- [ModSearch](https://github.com/liustack/modsearch) - **211 stars** | `Workflow & Automation` | `MIT`. A DSH web-search plugin that adds search, X search, and focused page reading through the ModSearch engine chain.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest`
- [DSH Visualize](https://github.com/Nagi-ovo/dsh-visualize) - **200 stars** | `UI & Interfaces` | `BSD-3-Clause`. An inline visualization plugin that renders interactive HTML fragments as sandboxed cards in DSH conversations.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-visualize`
- [AnySearch DSH](https://github.com/anysearch-team/anysearch-dsh) - **185 stars** | `Workflow & Automation` | `MIT`. Web search for DSH with source discovery, vertical search, bounded batch queries, and cleaned page content.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @anysearch/anysearch-dsh`
- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) - **185 stars** | `Themes & Appearance` | `MIT`. A DeepSeek Harness skin that applies the Open Sea visual theme to the conversation interface.
  - Install: `dsh plugin --profile web add github:d-dev0101/open-sea-skin#v1.2.1`
- [DSH iOS](https://github.com/ZSeven-W/dsh-ios) - **181 stars** | `UI & Interfaces` | `MIT`. An iOS companion bundle for DeepSeek Harness with native mobile controls and a Cordis client bridge.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-ios@latest`
- [DSH Pentest](https://github.com/howmp/dsh-pentest) - **177 stars** | `Workflow & Automation` | `MIT`. A DSH security workflow plugin that records penetration-test targets, clues, proposals, decisions, and reports in the Web UI.
  - Install: `dsh plugin --profile web add https://github.com/howmp/dsh-pentest/releases/latest/download/dsh-pentest.tar.gz`
- [DSH Agent RP](https://github.com/hewzhew/dsh-agent-rp) - **171 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness roleplay bundle with SillyTavern migration, agent personas, and conversation workflow tools.
  - Install: `npx -p @deepseek-ai/dsh@latest dsh plugin --profile web add github:hewzhew/dsh-agent-rp#main`
- [Engramory](https://github.com/tinqiao-oss/engramory) - **167 stars** | `Memory & Knowledge` | `MIT`. A file-based DSH memory plugin that keeps human-readable notes in a versioned store with deterministic limits.
  - Install: `dsh plugin --profile web add dsh-engramory`
- [Mnemon DSH Plugin](https://github.com/omdsh-dev/dsh-mnemon) - **165 stars** | `Memory & Knowledge` | `MIT`. A DeepSeek Harness memory plugin with a three-tier control plane for storing and retrieving project context.
  - Install: `dsh plugin --profile web add dsh-mnemon`
- [Anime Find](https://github.com/cocofhu/anime-find) - **157 stars** | `Workflow & Automation` | `MIT`. A DSH Web search plugin that gathers anime results into cards with metadata, resource links, and optional streaming views.
  - Install: `dsh plugin --profile web add github:cocofhu/anime-find`
- [pi2dsh](https://github.com/weijiafu14/pi2dsh) - **155 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle that brings the pi coding agent's workflow and tools into DSH.
  - Install: `dsh plugin --profile web add pi2dsh`
- [DSH Notes](https://github.com/zhaoolee/notes) - **149 stars** | `Memory & Knowledge` | `MIT`. A DSH tool plugin that exports agent output into a self-hosted Notes service.
  - Install: `dsh plugin --profile web add @zhaoolee/dsh-notes`
- [DSH Synapse](https://github.com/liangmianya/dsh-synapse) - **148 stars** | `UI & Interfaces` | `MIT`. A DeepSeek Harness bundle that adds a visual synapse workspace for navigating related context and tools.
  - Install: `corepack pnpm dsh plugin --profile web add github:liangmianya/dsh-synapse`
- [DSH Cost Meter](https://github.com/Han-1413141/dsh-cost-meter) - **147 stars** | `Workflow & Automation` | `MIT`. Session cost tracking for DSH with daily totals, history, budget views, and synchronized model pricing.
  - Install: `dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.3.1`
- [DSH Wallpaper Engine](https://github.com/elysia395/dsh-wallpaper-engine) - **140 stars** | `Themes & Appearance` | `MIT`. A DeepSeek Harness theme bundle for setting animated wallpapers and managing visual backgrounds.
  - Install: `dsh plugin --profile web add dsh-plugin-wallpaper-engine`
- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) - **138 stars** | `UI & Interfaces` | `MIT`. An OpenPencil plugin that lets DSH agents preview, inspect, and edit real multi-frame design documents.
  - Install: `pnpm dlx --package=@deepseek-ai/dsh@0.1.0-rc.6 dsh plugin --profile web add @zseven-w/dsh-openpencil@latest`
- [DSH Super Injector](https://github.com/yjh051108/dsh-super-injector) - **136 stars** | `Workflow & Automation` | `BSD-3-Clause`. A DSH development plugin for injecting, hot-reloading, and removing local plugin packages without a restart.
  - Install: `dsh plugin --profile web add github:yjh051108/dsh-super-injector`
- [DSH Git Bash Preset](https://github.com/liceses/dsh-gitbash-preset) - **135 stars** | `Files & Runtime` | `MIT`. A DeepSeek Harness preset that configures Git Bash support and a ready-to-use terminal environment.
  - Install: `dsh plugin --profile web add @icelily/dsh-gitbash-preset`
- [TokenLedger](https://github.com/zh667/TokenLedger) - **130 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle for tracking token usage and recording session cost data.
  - Install: `dsh plugin --profile web add "github:zh667/TokenLedger"`
- [DSH Image Gen](https://github.com/shanliuling/dsh-image-gen) - **126 stars** | `Vision` | `MIT`. A Web plugin that adds image-generation tools and settings to DeepSeek Harness conversations.
  - Install: `dsh plugin --profile web add dsh-image-gen`
- [DSH Liang Intensity Skin](https://github.com/kingOfSoySauce/dsh-liang-skin) - **124 stars** | `Themes & Appearance` | `No standard license`. An optional DSH Web skin that adds an adaptive reasoning-intensity slider and themed model-selection visuals.
  - Install: `dsh plugin --profile web add github:kingOfSoySauce/dsh-liang-skin#v0.1.4`
- [DSH Noema](https://github.com/ZSeven-W/dsh-noema) - **121 stars** | `Memory & Knowledge` | `MIT`. Durable Noema-backed memory for DSH with recall tools, cross-agent imports, and a settings page.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-noema@latest`
- [GAL View](https://github.com/Ayase34/gal-view) - **120 stars** | `UI & Interfaces` | `MIT`. A DSH Web conversation view with a Galgame-style layout and an editor for scene elements.
  - Install: `dsh plugin --profile web add github:Ayase34/gal-view#main`
- [DSH Agent Team GUI](https://github.com/toolclub/dsh-agent-team-gui) - **116 stars** | `Workflow & Automation` | `MIT`. Persistent multi-model teams for DSH with durable orchestration, DAG workflows, run history, and provider-reported usage.
  - Install: `dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v0.5.0`
- [DSH Auto Mode](https://github.com/NanmiCoder/dsh-auto-mode) - **115 stars** | `Workflow & Automation` | `MIT`. A fail-closed permission policy plugin that classifies DSH tool calls before automatic execution.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-auto-mode`
- [DSH Undo Savepoint](https://github.com/lire1131/dsh-undo-savepoint) - **112 stars** | `Files & Runtime` | `MIT`. Crash recovery for DSH that snapshots configuration and plugin code for undo, redo, rollback, and safe-mode starts.
  - Install: `dsh plugin --profile web add github:lire1131/dsh-undo-savepoint#master`
- [DSH Oil Creator](https://github.com/oil-oil/dsh-oil-creator) - **110 stars** | `UI & Interfaces` | `MIT`. A DeepSeek Harness creative bundle for generating and organizing Oil-style visual content.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-oil-creator`
- [Argo DSH](https://github.com/taxueseek/argo) - **105 stars** | `Workflow & Automation` | `MIT`. A DSH profile bundle that mounts Argo search MCP tools and an evidence-oriented research workflow.
  - Install: `dsh plugin --profile web add "github:taxueseek/argo#main&path:packages/dsh-plugin"`
- [DSH Data Agent](https://github.com/omdsh-dev/dsh-data-agent) - **105 stars** | `Workflow & Automation` | `MIT`. Database connections, masked forms, SQL tools, and a shared data-analysis preset for DSH Web and TUI.
  - Install: `dsh plugin --profile web add @yejiming/dsh-data-agent`
- [DSH Usage Stats](https://github.com/Ychris12138/dsh-usage-stats) - **102 stars** | `Workflow & Automation` | `MIT`. A DSH Web dashboard for token usage, provider balances, subscription quotas, and historical activity.
  - Install: `dsh plugin --profile web add github:Ychris12138/dsh-usage-stats`
- [DSH Reasoning Effort](https://github.com/HanaAyane/dsh-reasoning-effort) - **98 stars** | `UI & Interfaces` | `MIT`. Model and reasoning-effort controls for DSH with a slider, model-advertised levels, and themed selector views.
  - Install: `dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main`
- [DSH Web UI Market](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - **98 stars** | `UI & Interfaces` | `MIT`. A Web UI marketplace for browsing the curated DSH catalog and installing or removing plugins from a profile.
  - Install: `dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin`
- [Deep Whale Day/Night Theme](https://github.com/GGBond2424648901/deep-whale-day-night-theme) - **97 stars** | `Themes & Appearance` | `CC-BY-NC-SA-4.0`. A DeepSeek Harness theme bundle with coordinated Deep Whale day and night interface styles.
  - Install: `dsh plugin --profile web add github:GGBond2424648901/deep-whale-day-night-theme#runtime`
- [DSH Mobile](https://github.com/saya-ch/dsh-mobile) - **97 stars** | `Input & Navigation` | `Apache-2.0`. A DeepSeek Harness mobile bundle with touch-friendly navigation and a compact conversation layout.
  - Install: `dsh plugin --profile web add dsh-mobile@alpha`
- [DSH Taskboard](https://github.com/shengsheng90/DSH-taskboard) - **97 stars** | `Workflow & Automation` | `Apache-2.0`. A DeepSeek Harness taskboard bundle for organizing tasks and monitoring workflow progress.
  - Install: `dsh plugin --profile web add -w /absolute/path/to/shengsheng-dsh-taskboard-<version>.tgz`
- [Odai DSH Plugin](https://github.com/orziz/odai) - **95 stars** | `Workflow & Automation` | `MIT`. A profile-wide DSH governance and routing bundle with an embedded Odai skill and runtime.
  - Install: `dsh plugin --profile web add odai-dsh-plugin`
- [DSH Workflow](https://github.com/omdsh-dev/dsh_workflow) - **94 stars** | `Workflow & Automation` | `MIT`. A reusable DSH workflow layer for multi-agent runs with saved plans, approvals, background jobs, and resumable execution.
  - Install: `dsh plugin --profile web add github:dsh-external/dsh_workflow#main`
- [DSH Crew](https://github.com/ZSeven-W/dsh-crew) - **93 stars** | `Workflow & Automation` | `MIT`. A DSH hub for dispatching work to native subagents, tracking progress, and bridging Claude Code or Codex workers.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-crew@latest`
- [DSH Turn Rewind](https://github.com/Anionex/dsh-turn-rewind) - **93 stars** | `Memory & Knowledge` | `BSD-3-Clause`. A DSH recovery plugin that records workspace changes and restores a conversation turn through its Change Ledger.
  - Install: `dsh plugin --profile web add @anionex/dsh-turn-rewind`
- [Tabbit Browser](https://github.com/Tabbit-Browser/dsh-tabbit) - **92 stars** | `UI & Interfaces` | `MIT`. A DSH bundle that exposes Tabbit Browser skills and host tools through the Web profile.
  - Install: `dsh plugin --profile web add github:Tabbit-Browser/dsh-tabbit`
- [DSH Skill & MCP Panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) - **89 stars** | `UI & Interfaces` | `MIT`. A Web settings panel for managing DSH Skills and MCP servers through profile configuration.
  - Install: `dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.1/dsh-skill-mcp-panel-2.0.1.tgz`
- [DSH Annotation](https://github.com/omdsh-dev/dsh-annotation) - **87 stars** | `Input & Navigation` | `MIT`. A DSH Web selection tool that annotates assistant text and sends numbered annotation blocks with a message.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git`
- [DSH Chat Import](https://github.com/Nwflower/dsh-chat-import) - **87 stars** | `Memory & Knowledge` | `MIT`. A conversation migration plugin that imports histories from external agent tools into resumable DSH sessions and exports them back.
  - Install: `dsh plugin --profile web add dsh-chat-import`
- [DSH CommandCode Provider](https://github.com/Mars-Sea/dsh-commandcode-provider) - **86 stars** | `Workflow & Automation` | `MIT`. An LLM provider plugin that adds a live Command Code model catalog, reasoning controls, and a Models-page card to DSH.
  - Install: `dsh plugin --profile web add @mars-sea/dsh-commandcode-provider`
- [DSH Vision](https://github.com/oil-oil/dsh-vision) - **83 stars** | `Vision` | `MIT`. Vision tools for DSH that preserve native image input and bridge text-only models to an external vision model.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision`
- [DSH Agent Workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) - **82 stars** | `Workflow & Automation` | `MIT`. A Web UI plugin that presents model requests, responses, and tool calls as a navigable workflow for each DSH conversation.
  - Install: `dsh plugin --profile web add github:xuanyuanzhifeng/dsh-plugin-agent-workflow#v0.1.0 --workspace-root`
- [ZAT DSH Engine](https://github.com/mishibeikejie/zat-dsh-engine) - **77 stars** | `UI & Interfaces` | `MIT`. A Web UI marketplace for searching, installing, updating, and rolling back community DSH plugins.
  - Install: `dsh plugin --profile web add github:mishibeikejie/zat-dsh-engine`
- [DSH Dream Skin](https://github.com/RevolutionLA/dsh-dream-skin) - **76 stars** | `Themes & Appearance` | `MIT`. A Web UI skin pack with animated themes, wallpapers, accents, import/export, and persistent per-user appearance settings.
  - Install: `dsh plugin --profile web add dsh-dream-skin`
- [Superpowers DSH](https://github.com/LayneChai/superpowers-dsh) - **75 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle that packages the Superpowers development workflow as native DSH skills.
  - Install: `dsh plugin --profile web add github:LayneChai/superpowers-dsh`
- [Dockyard DSH](https://github.com/AITabby/dockyard-dsh) - **74 stars** | `Workflow & Automation` | `MIT`. A native DSH provider plugin with account pools, OAuth sign-in, model catalogs, quota status, and provider-specific requests.
  - Install: `dsh plugin --profile web add github:AITabby/dockyard-dsh`
- [DSH Plugin Finder](https://github.com/awesome-dsh-plugin/dsh-find-plugin) - **74 stars** | `Workflow & Automation` | `MIT`. Searches GitHub's DSH plugin ecosystem from inside a session and returns ranked results with ready-to-run install commands.
  - Install: `dsh plugin --profile web add dsh-find-plugin`
- [DSH Notification](https://github.com/omdsh-dev/dsh-notification) - **70 stars** | `UI & Interfaces` | `MIT`. Browser desktop notifications for completed DSH turns with outcome toggles and keyword include or exclude rules.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.2.tar.gz`
- [DSH QQ Bot](https://github.com/tencent-connect/dsh-qqbot) - **70 stars** | `Workflow & Automation` | `MIT`. A QQ Bot channel for DSH that handles messaging, QR-code login, session events, and agent replies.
  - Install: `npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot`
- [DSH Automation](https://github.com/titanwings/dsh-automation) - **69 stars** | `Workflow & Automation` | `MIT`. Scheduled coding runs for DSH with Web and agent controls, durable history, and guarded execution boundaries.
  - Install: `dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.6`
- [ForkProbe DSH](https://github.com/Jayden-X-L/forkprobe) - **69 stars** | `Workflow & Automation` | `MIT`. A native DSH plugin for comparing Skills on the same task and choosing a winner from a local report.
  - Install: `dsh plugin --profile web add "github:Jayden-X-L/forkprobe"`
- [DSH Plugin Console](https://github.com/Noob-stupid/dsh-plugin-hub) - **64 stars** | `UI & Interfaces` | `MIT`. A DSH settings panel for enabling, disabling, inspecting, and installing community plugins from multiple sources.
  - Install: `dsh plugin --profile web add github:Noob-stupid/dsh-plugin-hub`
- [DSH Plugin Store](https://github.com/ZASENJC/dsh-plugins-store) - **63 stars** | `UI & Interfaces` | `MIT`. A Web plugin that lets users browse, validate, install, update, and remove community DSH plugins after confirmation.
  - Install: `dsh plugin --profile web add npm:dsh-plugins-store`
- [DSH Web Plugin Manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - **62 stars** | `UI & Interfaces` | `MIT`. A DSH Web plugin manager with install guards, health checks, rollback, environment controls, and marketplace browsing.
  - Install: `dsh plugin --profile web add dsh-web-plugin-manager@latest`
- [DSH Claude UX](https://github.com/eri64/dsh-claude-ux) - **60 stars** | `Input & Navigation` | `MIT`. A Web plugin that adds reversible region risk controls and automatic conversation termination for abusive interactions.
  - Install: `dsh plugin --profile web add github:eri64/dsh-claude-ux`
- [DSH Harness Wallet](https://github.com/feibi-mochi/deepseek-harness-control-center) - **60 stars** | `Workflow & Automation` | `MIT`. A DSH Web plugin for account balances, usage tracking, completion alerts, recharge actions, and session controls.
  - Install: `dsh plugin --profile web add deepseek-harness-wallet`
- [DSH Reverse Skill](https://github.com/dhicoc/dsh-reverse-skill) - **59 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle for reverse-engineering software behavior into reusable development skills.
  - Install: `dsh plugin --profile web add github:dhicoc/dsh-reverse-skill`
- [DSH Toy](https://github.com/c3ll256/dsh-toy) - **58 stars** | `Workflow & Automation` | `BSD-3-Clause`. Safety-bounded DSH control for Buttplug and Intiface devices with optional MonsterParty toy integration.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy`
- [DSH Stock Watch](https://github.com/Awu12277/dsh-stock-watch) - **57 stars** | `UI & Interfaces` | `MIT`. A Web UI stock monitor with watchlists, groups, intraday and candlestick charts, target prices, and a draggable panel.
  - Install: `dsh plugin --profile web add dsh-stock-watch`
- [DSH Thin Plugin Console](https://github.com/vlln/plugin-registry) - **57 stars** | `UI & Interfaces` | `MIT`. A Web settings panel for installing, inspecting, updating, enabling, and disabling profile plugins without manual patch editing.
  - Install: `dsh plugin --profile web add @vlln/plugin-console@0.1.0`
- [DSH Notifier](https://github.com/THEWOLFWALKER/dsh-notifier) - **55 stars** | `Workflow & Automation` | `MIT`. A notification and remote-approval layer for DSH with one notify API, multiple channel adapters, and optional mobile controls.
  - Install: `dsh plugin add dsh-notifier --profile web`
- [DSH Auth In One](https://github.com/Stormycry-cryp/dsh-AuthInOne) - **53 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness authentication bundle that manages common sign-in and profile setup flows.
  - Install: `dsh plugin --profile web add github:Stormycry-cryp/dsh-AuthInOne#v0.2.0-alpha.4`
- [DSH Balance Monitor](https://github.com/Francis-Xavier-code/dsh-balance-plugin) - **53 stars** | `Workflow & Automation` | `MIT`. Balance monitoring, usage statistics, and third-party plugin management in the DSH Web interface.
  - Install: `dsh plugin --profile web add github:Francis-Xavier-code/dsh-balance-plugin`
- [Local Shell MCP](https://github.com/fwerkor/local-shell-mcp) - **53 stars** | `Files & Runtime` | `MIT`. A DSH bridge for local-shell-mcp that exposes shell, files, browser, and remote-worker tools through per-session connections.
  - Install: `dsh plugin --profile web add 'github:fwerkor/local-shell-mcp#main'`
- [Multica DSH Runtime](https://github.com/multica-ai/dsh-multica-runtime) - **53 stars** | `Files & Runtime` | `No standard license`. A local DSH runtime bridge for Multica that exposes a versioned stdio protocol without patching the Harness source.
  - Install: `dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime`
- [Open in VS Code](https://github.com/omdsh-dev/dsh-open-in-vscode) - **53 stars** | `Input & Navigation` | `MIT`. Adds a workspace-row action that opens the selected DSH directory in VS Code or another configured editor.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz`
- [BeautiCode](https://github.com/starsstreaming/beautiCode) - **52 stars** | `Themes & Appearance` | `MIT`. A DeepSeek Harness theme bundle that adds BeautiCode visual styling to the client interface.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add beauticode-dsh`
- [DSH Navbar](https://github.com/vlln/dsh-navbar) - **52 stars** | `Input & Navigation` | `MIT`. A conversation node bar that lets users jump quickly between user messages in the DSH Web view.
  - Install: `dsh plugin --profile web add @vlln/dsh-navbar`
- [Morning Star DSH](https://github.com/btspoony/mstar-harness) - **52 stars** | `Workflow & Automation` | `MIT`. In-process DSH workflow gates that validate status, control dispatch, and expose the Morning Star engine through refusal-aware channels.
  - Install: `dsh plugin --profile web add @mstar-harness/dsh`
- [OpenBiliClaw](https://github.com/whiteguo233/dsh-openbiliclaw) - **50 stars** | `Workflow & Automation` | `BSD-3-Clause`. A DeepSeek Harness bundle for OpenBiliClaw workflows and related content tools.
  - Install: `dsh plugin --profile web add @openbiliclaw/dsh-plugin`
- [DeepSeek Flow](https://github.com/kanghelyu/dsh-deepseek-flow) - **49 stars** | `Workflow & Automation` | `MIT`. A Markdown-first workflow editor for DSH with a synchronized canvas, Boolean gates, reviewable changes, and AI-assisted workflow maintenance.
  - Install: `dsh plugin --profile web add "github:kanghelyu/dsh-deepseek-flow#main"`
- [OpenMA DSH TUI](https://github.com/openma-ai/Martty) - **47 stars** | `UI & Interfaces` | `MIT`. A terminal-native DSH profile with an ACP plugin tree, streamed sessions, themes, overlays, and native TUI rendering.
  - Install: `dsh plugin --profile tui add @openma/deepseek-harness-tui@latest`
- [DSH Codex Shell](https://github.com/Ephemeral-AI-Lab/dsh-plugins) - **45 stars** | `Files & Runtime` | `MIT`. A shell plugin that adds interactive exec_command and write_stdin tools to DSH profiles.
  - Install: `dsh plugin --profile web add dsh-codex-shell@0.1.2`
- [DSH Status Rotator](https://github.com/01Virex/dsh-status-rotator) - **44 stars** | `UI & Interfaces` | `MIT`. A DeepSeek Harness bundle that rotates status messages while a task is running.
  - Install: `dsh plugin --profile web add dsh-status-rotator`
- [DSH Popout Sidebar](https://github.com/e2mcc/dsh-popout-sidebar) - **42 stars** | `UI & Interfaces` | `MIT`. A DeepSeek Harness bundle that opens the sidebar as a separate popout panel.
  - Install: `dsh plugin --profile web add github:e2mcc/dsh-popout-sidebar`
- [DSH Web Mobile](https://github.com/mexiaosqwq/dsh-web-mobile) - **41 stars** | `UI & Interfaces` | `MIT`. A responsive Web UI plugin that adapts the DSH interface for narrow and portrait-oriented screens.
  - Install: `dsh plugin --profile web add github:mexiaosqwq/dsh-web-mobile`
- [DSH Lark](https://github.com/omdsh-dev/dsh-lark) - **40 stars** | `Workflow & Automation` | `BSD-3-Clause`. A Feishu/Lark channel for sending tasks to DSH agents and returning replies, approvals, and cards to chat.
  - Install: `dsh plugin --profile web add dsh-lark-channel@latest`
- [DSH Prompt Enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) - **40 stars** | `Input & Navigation` | `No standard license`. A DeepSeek Harness bundle that adds prompt editing helpers and reusable input enhancements.
  - Install: `dsh plugin --profile web add github:Fishsb/dsh-prompt-enhancer#v3.3.1`
- [DSH MinerU](https://github.com/HuanLinOTO/dsh-plugin-mineru) - **39 stars** | `Files & Runtime` | `AGPL-3.0`. MinerU-backed document parsing tools that convert PDF, images, DOCX, PPTX, and XLSX files into structured Markdown or JSON.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-mineru`
- [DSH Status Label](https://github.com/alingalingling/ui-status-label) - **39 stars** | `UI & Interfaces` | `MIT`. Configurable running-turn status text for DSH Web, with a settings row and conversation-status provider.
  - Install: `dsh plugin --profile web add dsh-ui-status-label`
- [DSH Benign Exit](https://github.com/sunruize93-cmyk/dsh-benign-exit) - **36 stars** | `Files & Runtime` | `MIT`. A DeepSeek Harness bundle that provides a controlled exit command for completed or canceled tasks.
  - Install: `dsh plugin --profile web add dsh-benign-exit`
- [DSH Message Edit](https://github.com/Moeblack/dsh-message-edit) - **35 stars** | `Input & Navigation` | `MIT`. A conversation plugin for branching, editing, rerolling, retrying, and reviewing DSH message versions.
  - Install: `dsh plugin --profile web add dsh-message-edit`
- [AX Feishu Bridge](https://github.com/AX1202/ax-feishu-bridge) - **34 stars** | `Workflow & Automation` | `MIT`. A Feishu/Lark bridge that lets users chat with Pi or DeepSeek Harness from the same messaging workspace.
  - Install: `dsh plugin --profile web add ax-feishu-bridge --ignore-scripts`
- [DSH Interconnect](https://github.com/Chinesezjc/dsh-interconnect) - **34 stars** | `Workflow & Automation` | `MIT`. Cross-instance DSH messaging and event handoff with host services, model-facing tools, and shared-token authentication.
  - Install: `dsh plugin --profile web add dsh-interconnect`
- [DSH Auto Continue](https://github.com/HsiangNianian/dsh-auto-continue) - **33 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle that automatically continues a task after an interaction reaches its limit.
  - Install: `dsh plugin --profile web add dsh-client-auto-continue`
- [DSH Save Money](https://github.com/zhu168/dsh-save-money) - **33 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle for tracking model usage and helping reduce unnecessary token spending.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-save-money`
- [DSH Usage Plugin](https://github.com/feiyang-dev/dsh-usage-plugin) - **33 stars** | `Workflow & Automation` | `MIT`. A DeepSeek Harness bundle for viewing usage statistics and token consumption during sessions.
  - Install: `dsh plugin --profile web add @feiyang666/dsh-usage-plugin`
- [DSH Remote](https://github.com/flymysql/dsh-remote) - **31 stars** | `Files & Runtime` | `MIT`. A DeepSeek Harness bundle for connecting the client to a remote runtime.
  - Install: `dsh plugin --profile web add dsh-remote`
- [PictureReader](https://github.com/jing-hy/picturereader) - **31 stars** | `Vision` | `MIT`. A DeepSeek Harness vision bundle for reading and describing information from images.
  - Install: `dsh plugin --profile web add picturereader`
<!-- END GENERATED RANKING -->

## Install plugins carefully

DSH plugins run third-party code with your account permissions. A plugin can read files, access environment variables, start processes, and use the network. Inclusion confirms the repository shape and installation evidence; it is not a security audit. Read the source and install unfamiliar plugins in an isolated workspace without production credentials.

## Related resources

- [DeepSeek Harness documentation](https://deepseek-harness.github.io/deepseek-harness/) - Official installation, configuration, and development guides.
- [Official `dsh-plugin` topic](https://github.com/topics/dsh-plugin) - A discovery feed that still requires code-level verification.
- [ScriptByAI](https://www.scriptbyai.com/) - AI tools, coding agents, and practical technical guides.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request. Additions must provide code-level DSH evidence and meet the admission threshold.
