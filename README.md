# Awesome DeepSeek Harness Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A verified, category-organized list of community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), with exact GitHub Star counts.

[![Quality](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml)
[![Update Stars](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml)

**Last verified:** 2026-08-24 | **Minimum at admission:** 30 stars | **Plugins:** 174

## Contents

- [What qualifies](#what-qualifies)
- [Plugins by category](#plugins-by-category)
  - [Files & Runtime](#files--runtime)
  - [Input & Navigation](#input--navigation)
  - [Memory & Knowledge](#memory--knowledge)
  - [Themes & Appearance](#themes--appearance)
  - [UI & Interfaces](#ui--interfaces)
  - [Vision](#vision)
  - [Workflow & Automation](#workflow--automation)
- [Install plugins carefully](#install-plugins-carefully)
- [Related resources](#related-resources)

## What qualifies

Every listed project has at least 30 GitHub Stars at admission and a public repository with an identifiable `dsh.bundle` manifest, bundle patch, plugin entry, and documented installation path. Multi-platform projects qualify only when they ship a separate DSH bundle.

The `dsh-plugin` GitHub topic is a discovery signal, not proof. This list excludes topic-only repositories, generic Skills, standalone clients without a bundle, MCP servers without a DSH package, API wrappers, presets, tutorials, Awesome lists, archived repositories, and minimally changed forks.

## Plugins by category

Each category below contains the actual plugin entries. Entries within a category are sorted by exact live GitHub Stars.

<!-- BEGIN GENERATED CATEGORY LIST -->
### Files & Runtime

- [OpenDesign DSH Runtime](https://github.com/nexu-io/open-design) - **90.8k stars** | `Apache-2.0`. A DeepSeek Harness profile bundle that connects OpenDesign to a user-installed DSH runtime through a structured stdio protocol.
  - Install: `pnpm --filter @open-design/dsh-runtime build && pnpm -C packages/dsh-runtime pack --pack-destination <temporary-directory> && dsh plugin --profile open-design add <temporary-directory>/open-design-dsh-runtime-0.1.0.tgz`

- [Mirage DSH](https://github.com/strukto-ai/mirage) - **3.6k stars** | `Apache-2.0`. A DSH filesystem and shell provider that mounts remote and local resources inside one virtual workspace.
  - Install: `dsh plugin --profile web add @struktoai/mirage-dsh`

- [API Relay Audit DSH](https://github.com/toby-bridges/api-relay-audit) - **801 stars** | `AGPL-3.0-only`. A DeepSeek Harness bundle for auditing API relays for prompt injection, model substitution, tool-call rewriting, SSE anomalies, and error leakage.
  - Install: `dsh plugin --profile web add "github:toby-bridges/api-relay-audit#v2.4.0"`

- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) - **630 stars** | `Apache-2.0`. A DSH bundle that connects the managed-agents runtime through the official stdio MCP client.
  - Install: `npm ci && npm run build:runtime && npm link && dsh plugin --profile web add managed-agents`

- [AgentGuard DSH](https://github.com/GoPlusSecurity/agentguard) - **458 stars** | `MIT`. A DeepSeek Harness bundle for scanning plugin sources and reporting or enforcing runtime tool-call security policies.
  - Install: `dsh plugin --profile web add @goplus/agentguard`

- [DSH Git Bash Preset](https://github.com/liceses/dsh-gitbash-preset) - **135 stars** | `MIT`. A DeepSeek Harness preset that configures Git Bash support and a ready-to-use terminal environment.
  - Install: `dsh plugin --profile web add @icelily/dsh-gitbash-preset`

- [Invoice Downloader DSH](https://github.com/EthanYoQ/Invoice-Downloader) - **133 stars** | `Apache-2.0`. A DSH bundle for local IMAP invoice downloads, OCR, archiving, and Excel summaries from a Web sidebar.
  - Install: `dsh plugin --profile web add @ethanyoq/dsh-invoice-downloader`

- [DSH Undo Savepoint](https://github.com/lire1131/dsh-undo-savepoint) - **120 stars** | `MIT`. Crash recovery for DSH that snapshots configuration and plugin code for undo, redo, rollback, and safe-mode starts.
  - Install: `dsh plugin --profile web add github:lire1131/dsh-undo-savepoint#master`

- [Univer Office DSH](https://github.com/dream-num/dsh-univer-office) - **95 stars** | `Apache-2.0`. A DSH office bundle for creating and editing spreadsheets, documents, presentations, tables, canvases, and existing office files.
  - Install: `dsh plugin --profile web add dsh-univer-office`

- [Multica DSH Runtime](https://github.com/multica-ai/dsh-multica-runtime) - **56 stars** | `No standard license`. A local DSH runtime bridge for Multica that exposes a versioned stdio protocol without patching the Harness source.
  - Install: `dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime`

- [Local Shell MCP](https://github.com/fwerkor/local-shell-mcp) - **53 stars** | `MIT`. A DSH bridge for local-shell-mcp that exposes shell, files, browser, and remote-worker tools through per-session connections.
  - Install: `dsh plugin --profile web add 'github:fwerkor/local-shell-mcp#main'`

- [DSH Codex Shell](https://github.com/Ephemeral-AI-Lab/dsh-plugins) - **47 stars** | `MIT`. A shell plugin that adds interactive exec_command and write_stdin tools to DSH profiles.
  - Install: `dsh plugin --profile web add dsh-codex-shell@0.1.2`

- [DSH Benign Exit](https://github.com/sunruize93-cmyk/dsh-benign-exit) - **43 stars** | `MIT`. A DeepSeek Harness bundle that provides a controlled exit command for completed or canceled tasks.
  - Install: `dsh plugin --profile web add dsh-benign-exit`

- [DSH MinerU](https://github.com/HuanLinOTO/dsh-plugin-mineru) - **41 stars** | `AGPL-3.0`. MinerU-backed document parsing tools that convert PDF, images, DOCX, PPTX, and XLSX files into structured Markdown or JSON.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-mineru`

- [DSH Remote](https://github.com/flymysql/dsh-remote) - **35 stars** | `MIT`. A DeepSeek Harness bundle for connecting the client to a remote runtime.
  - Install: `dsh plugin --profile web add dsh-remote`

- [DSH Plugin Guard](https://github.com/lxzy-7/dsh-plugin-guard) - **31 stars** | `MIT`. A DeepSeek Harness bundle that snapshots plugin and profile changes, guards boot, and rolls back failed installations.
  - Install: `dsh plugin --profile web add github:lxzy-7/dsh-plugin-guard`

### Input & Navigation

- [BrowserSkill DSH Plugin](https://github.com/Tencent/BrowserSkill) - **1.3k stars** | `MIT`. A DeepSeek Harness bundle that exposes BrowserSkill browser automation tools for sessions, navigation, snapshots, clicks, forms, and screenshots.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/browser-skill-dsh-plugin`

- [DSH Pocket](https://github.com/shaobeichen/dsh-pocket) - **552 stars** | `GPL-2.0`. A Web plugin that mirrors DSH sessions to a phone over a local network or a password-protected Cloudflare tunnel.
  - Install: `dsh plugin --profile web add dsh-pocket -w`

- [DSH At File](https://github.com/FSMargoo/dsh-at-file) - **462 stars** | `MIT`. A composer extension for searching workspace paths with at-file mentions and attaching file contents to prompts.
  - Install: `dsh plugin --profile web add https://github.com/FSMargoo/dsh-at-file/archive/refs/tags/v0.6.0.tar.gz`

- [DSH Mobile](https://github.com/saya-ch/dsh-mobile) - **137 stars** | `Apache-2.0`. A DeepSeek Harness mobile bundle with touch-friendly navigation and a compact conversation layout.
  - Install: `dsh plugin --profile web add dsh-mobile@alpha`

- [DSH Annotation](https://github.com/omdsh-dev/dsh-annotation) - **94 stars** | `MIT`. A DSH Web selection tool that annotates assistant text and sends numbered annotation blocks with a message.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git`

- [DSH Turn Delete](https://github.com/hanshenmesen/dsh-turn-delete) - **64 stars** | `MIT`. A DSH Web plugin for deleting one complete closed conversation turn while preserving the Session and later turns.
  - Install: `dsh plugin --profile web add dsh-turn-delete`

- [DSH Claude UX](https://github.com/eri64/dsh-claude-ux) - **63 stars** | `MIT`. A Web plugin that adds reversible region risk controls and automatic conversation termination for abusive interactions.
  - Install: `dsh plugin --profile web add github:eri64/dsh-claude-ux`

- [DSH Harness Remote](https://github.com/liguobao/deepseek-harness-remote) - **62 stars** | `MIT`. A DeepSeek Harness bundle that adds encrypted remote access for continuing sessions from desktop, Web, and Android clients.
  - Install: `dsh plugin --profile web add ds-harness-remote@0.3.29`

- [DSH Navbar](https://github.com/vlln/dsh-navbar) - **59 stars** | `MIT`. A conversation node bar that lets users jump quickly between user messages in the DSH Web view.
  - Install: `dsh plugin --profile web add @vlln/dsh-navbar`

- [DSH EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) - **55 stars** | `MIT`. A DSH Web editing plugin for recalling, rewriting, versioning, and restoring user messages.
  - Install: `dsh plugin --profile web add dsh-easyrewrite`

- [Open in VS Code](https://github.com/omdsh-dev/dsh-open-in-vscode) - **54 stars** | `MIT`. Adds a workspace-row action that opens the selected DSH directory in VS Code or another configured editor.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz`

- [DSH Free Search](https://github.com/DDDMUC/dsh-free-search) - **53 stars** | `MIT`. A multi-engine DSH search provider with free backends, automatic fallback, settings, and platform search.
  - Install: `git clone https://github.com/DDDMUC/dsh-free-search.git && dsh plugin --profile web add ./dsh-free-search`

- [DSH Meme](https://github.com/yyh-001/dsh-meme) - **50 stars** | `MIT`. A DSH meme plugin with searchable image packs, learned memes, emotion-based sending, and a composer picker.
  - Install: `dsh plugin --profile web add dsh-meme`

- [DSH Prompt Enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) - **46 stars** | `No standard license`. A DeepSeek Harness bundle that adds prompt editing helpers and reusable input enhancements.
  - Install: `dsh plugin --profile web add github:Fishsb/dsh-prompt-enhancer#v3.3.1`

- [DSH Message Edit](https://github.com/Moeblack/dsh-message-edit) - **42 stars** | `MIT`. A conversation plugin for branching, editing, rerolling, retrying, and reviewing DSH message versions.
  - Install: `dsh plugin --profile web add dsh-message-edit`

### Memory & Knowledge

- [OpenViking Memory](https://github.com/volcengine/OpenViking) - **32.6k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle with OpenViking auto-recall, session capture, protected viking:// URIs, and MCP tools.
  - Install: `dsh plugin --profile web add @openviking/dsh-memory-plugin`

- [Hindsight Coding Agents](https://github.com/vectorize-io/hindsight) - **21k stars** | `MIT`. A DeepSeek Harness memory bundle with automatic recall, session capture, knowledge pages, and per-repository memory banks.
  - Install: `dsh plugin --profile web add @vectorize-io/hindsight-coding-agents`

- [WeKnora Knowledge](https://github.com/Tencent/WeKnora) - **20.5k stars** | `MIT`. A DeepSeek Harness bundle for semantic knowledge search, document reading, and RAG answers over user-managed knowledge bases.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/dsh-weknora`

- [EverOS Memory](https://github.com/EverMind-AI/EverOS) - **12.4k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle that provides automatic cross-session recall through a local EverOS service.
  - Install: `dsh plugin --profile web add @evermind-ai/dsh-plugin`

- [MemOS Local Memory](https://github.com/MemTensor/MemOS) - **10.9k stars** | `MIT`. A local MemOS memory bundle for DeepSeek Harness with layered recall, reflection, policy induction, and skill crystallization.
  - Install: `curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/main/apps/memos-local-plugin/install.sh | bash -s -- --agent dsh --profile web`

- [ReMe](https://github.com/agentscope-ai/ReMe) - **3.3k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle with recall, capture, settings, and skill guidance for TypeScript agent workflows.
  - Install: `dsh plugin --profile web add @agentscope-ai/reme`

- [MemSearch](https://github.com/zilliztech/memsearch) - **2.5k stars** | `MIT`. A DeepSeek Harness memory bundle that captures shared Markdown notes, injects context before steps, and reviews candidate skills.
  - Install: `dsh plugin --profile web add @zilliz/memsearch-dsh`

- [mem9](https://github.com/mem9-ai/mem9) - **1.2k stars** | `Apache-2.0`. A persistent memory bundle for DeepSeek Harness with automatic recall, background ingest, and five memory tools.
  - Install: `dsh plugin --profile web add @mem9/dsh-plugin`

- [DSH Context](https://github.com/bowenliang123/dsh-context) - **966 stars** | `Apache-2.0`. A context dashboard and /context command that show how DSH messages, tools, injections, compactions, and token usage evolve.
  - Install: `dsh plugin --profile web add dsh-context`

- [Graph Memory](https://github.com/adoresever/graph-memory) - **569 stars** | `MIT`. A graph-based memory plugin for cross-session recall, PageRank, communities, and vector search in DSH.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.1.tgz`

- [Mnemon](https://github.com/mnemon-dev/mnemon) - **513 stars** | `Apache-2.0`. A persistent memory plugin that supplies graph-based recall and cross-session knowledge to DSH agents.
  - Install: `dsh plugin --profile web add dsh-mnemon`

- [Flowix Memory](https://github.com/text2future/flowix) - **346 stars** | `MIT`. A config-only DSH bundle that exposes Flowix notebook memos and artifact tools through a local stdio MCP server.
  - Install: `dsh plugin --profile web add ./app/flowix-dsh-host/bundles/dsh-flowix-memory`

- [DSH Memory Evolve](https://github.com/csyangwen/dsh-memory-evolve) - **234 stars** | `MIT`. A Web DSH memory and workflow plugin with cross-session recall, skill management, todos, session search, and external-agent dispatch.
  - Install: `dsh plugin --profile web add github:csyangwen/dsh-memory-evolve`

- [Mnemon DSH Plugin](https://github.com/omdsh-dev/dsh-mnemon) - **193 stars** | `MIT`. A DeepSeek Harness memory plugin with a three-tier control plane for storing and retrieving project context.
  - Install: `dsh plugin --profile web add dsh-mnemon`

- [Engramory](https://github.com/tinqiao-oss/engramory) - **171 stars** | `MIT`. A file-based DSH memory plugin that keeps human-readable notes in a versioned store with deterministic limits.
  - Install: `dsh plugin --profile web add dsh-engramory`

- [DSH Notes](https://github.com/zhaoolee/notes) - **150 stars** | `MIT`. A DSH tool plugin that exports agent output into a self-hosted Notes service.
  - Install: `dsh plugin --profile web add @zhaoolee/dsh-notes`

- [DSH Noema](https://github.com/ZSeven-W/dsh-noema) - **124 stars** | `MIT`. Durable Noema-backed memory for DSH with recall tools, cross-agent imports, and a settings page.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-noema@latest`

- [DSH Turn Rewind](https://github.com/Anionex/dsh-turn-rewind) - **100 stars** | `BSD-3-Clause`. A DSH recovery plugin that records workspace changes and restores a conversation turn through its Change Ledger.
  - Install: `dsh plugin --profile web add @anionex/dsh-turn-rewind`

- [DSH Chat Import](https://github.com/Nwflower/dsh-chat-import) - **97 stars** | `MIT`. A conversation migration plugin that imports histories from external agent tools into resumable DSH sessions and exports them back.
  - Install: `dsh plugin --profile web add dsh-chat-import`

- [DSH Git Memory](https://github.com/seriousz158/dsh-memory) - **68 stars** | `MIT`. A Git-backed long-term memory plugin that stores durable DSH memory locally, exposes settings controls, and optionally synchronizes idle sessions.
  - Install: `dsh plugin --profile web add github:seriousz158/dsh-memory`

- [DSH Memento](https://github.com/PerryLink/dsh-memento) - **60 stars** | `Apache-2.0`. A bounded cross-session memory service for DSH with approval-gated writes, audit trails, local SQLite storage, and recall tools.
  - Install: `dsh plugin --profile web add dsh-memento`

### Themes & Appearance

- [DSH Deep Whale](https://github.com/Small-tailqwq/dsh-deep-whale) - **1.6k stars** | `CC-BY-NC-SA-4.0`. A maid-atelier whale character skin for the DSH Web interface.
  - Install: `git clone https://github.com/Small-tailqwq/dsh-deep-whale.git && dsh plugin --profile web add ./dsh-deep-whale/maid-atelier`

- [DSH Balance Whale](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) - **751 stars** | `MIT`. A Web UI widget that displays DeepSeek account balance in a draggable whale companion.
  - Install: `dsh plugin --profile web add link:./dsh-whale-widget`

- [DSH Ads](https://github.com/Nagi-ovo/dsh-ads) - **554 stars** | `BSD-3-Clause`. A parody Web UI plugin that adds fake banner ads, popups, and small games styled after early portal sites.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-ads`

- [DSH Pet](https://github.com/PC2005-cloud/dsh-pet) - **377 stars** | `MIT`. A floating DSH Web desktop pet with idle animations, random actions, screen wandering, and drag interactions.
  - Install: `dsh plugin --profile web add dsh-pet`

- [DSH Transparent UI](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - **370 stars** | `MIT`. A Web UI theme with adjustable glass effects, fluid or wallpaper backgrounds, and appearance controls for the DSH interface.
  - Install: `dsh plugin --profile web add dsh-client-ui-aqua`

- [Whale Girl](https://github.com/vlln/whale-girl) - **274 stars** | `MIT`. A draggable Web UI desktop pet with interaction, feeding, progress, and persistent state.
  - Install: `dsh plugin --profile web add github:vlln/whale-girl#main`

- [DSH Dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - **249 stars** | `See ASSET_LICENSE.md`. A desktop companion that reacts to DSH session events with a floating BigFish character and configurable behaviors.
  - Install: `pnpm exec dsh plugin --profile web add dsh-dafeiyu@alpha`

- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) - **187 stars** | `MIT`. A DeepSeek Harness skin that applies the Open Sea visual theme to the conversation interface.
  - Install: `dsh plugin --profile web add github:d-dev0101/open-sea-skin#v1.2.1`

- [DSH Wallpaper Engine](https://github.com/elysia395/dsh-wallpaper-engine) - **168 stars** | `MIT`. A DeepSeek Harness theme bundle for setting animated wallpapers and managing visual backgrounds.
  - Install: `dsh plugin --profile web add dsh-plugin-wallpaper-engine`

- [DSH Liang Intensity Skin](https://github.com/kingOfSoySauce/dsh-liang-skin) - **135 stars** | `No standard license`. An optional DSH Web skin that adds an adaptive reasoning-intensity slider and themed model-selection visuals.
  - Install: `dsh plugin --profile web add github:kingOfSoySauce/dsh-liang-skin#v0.1.4`

- [Deep Whale Day/Night Theme](https://github.com/GGBond2424648901/deep-whale-day-night-theme) - **104 stars** | `CC-BY-NC-SA-4.0`. A DeepSeek Harness theme bundle with coordinated Deep Whale day and night interface styles.
  - Install: `dsh plugin --profile web add github:GGBond2424648901/deep-whale-day-night-theme#runtime`

- [DSH Dream Skin](https://github.com/RevolutionLA/dsh-dream-skin) - **95 stars** | `MIT`. A Web UI skin pack with animated themes, wallpapers, accents, import/export, and persistent per-user appearance settings.
  - Install: `dsh plugin --profile web add dsh-dream-skin`

- [DSH Skin Market](https://github.com/kingOfSoySauce/dsh-skin-market) - **84 stars** | `MIT`. A DSH Web marketplace plugin for browsing, installing, updating, disabling, and removing community skins.
  - Install: `dsh plugin --profile web add dsh-skin-market@0.1.36`

- [BeautiCode](https://github.com/starsstreaming/beautiCode) - **61 stars** | `MIT`. A DeepSeek Harness theme bundle that adds BeautiCode visual styling to the client interface.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add beauticode-dsh`

- [DSH Endfield UI](https://github.com/rison114514/dsh-endfield-ui) - **30 stars** | `MIT`. An unofficial Endfield-inspired DSH Web theme plugin that uses the standard bundle and client theme extension points.
  - Install: `dsh plugin --profile web add @rison/dsh-endfield-ui@0.7.0`

### UI & Interfaces

- [DSH Web UI](https://github.com/zhu1090093659/dsh-web-ui) - **5.8k stars** | `Apache-2.0`. A Web UI bundle with a task board, Git graph, remote access, live statistics, pets, skins, and image tools.
  - Install: `dsh plugin --profile web add @linxin666/dsh-web-ui-all`

- [iPolloWork Design Studio](https://github.com/Devin-AXIS/iPolloWork) - **4.7k stars** | `Custom source-available`. A native DSH Design view for creating and editing visual documents inside the Harness conversation.
  - Install: `dsh plugin --profile web add deepseek-idesign`

- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - **2.7k stars** | `MIT`. A Web UI workbench with file editing, terminal access, Git tools, subagent views, and extension tabs.
  - Install: `dsh plugin --profile web add dsh-better-sidebar`

- [DSH TUI](https://github.com/ccch1mneyyy/dsh-TUI) - **2.4k stars** | `MIT`. A full-screen terminal interface with streaming output, a status line, rollback controls, and context usage indicators.
  - Install: `dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui`

- [DSH Market](https://github.com/dsh-market/dsh-market) - **2.1k stars** | `MIT`. A visual DSH plugin market for browsing, searching, installing, updating, and switching community plugins and themes.
  - Install: `dsh plugin --profile web add dshmarket`

- [Working Activity](https://github.com/ccch1mneyyy/working-activity) - **653 stars** | `MIT`. A live status line that shows model activity, running tools, elapsed time, and turn summaries in DSH.
  - Install: `dsh plugin --profile web add dsh-working-activity`

- [DSH Browser](https://github.com/Lum1104/dsh-browser) - **413 stars** | `MIT`. A Chrome side-panel integration with a DSH bridge for reading pages and operating supported browser content.
  - Install: `curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash`

- [DeepSeek PPT Studio](https://github.com/Devin-AXIS/deepseek-design) - **369 stars** | `Custom source-available`. A native DSH conversation view for creating, editing, templating, and exporting presentation slides.
  - Install: `dsh plugin --profile web add deepseek-ippt`

- [DSH GenUI](https://github.com/omdsh-dev/dsh-genui) - **312 stars** | `MIT`. A DSH rendering plugin for interactive UI components, charts, forms, quizzes, diagrams, and 3D scenes.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-genui.git`

- [Pilot Harness Bundles](https://github.com/op7418/pilot-harness) - **252 stars** | `MIT`. A suite of separately installable DSH Web bundles for a CodePilot-style theme, workspace file tree, schedule summary, and session-log export.
  - Install: `dsh plugin --profile web add https://github.com/op7418/pilot-harness/releases/latest/download/deepseek-ai-dsh-ui-worktree-0.1.0-rc.5.tgz`

- [DSH Tianshu TUI](https://github.com/huiliyi37/dsh-tianshu-tui) - **232 stars** | `Apache-2.0`. A terminal interface that adds Tianshu workflows, evidence gates, TDD controls, and optional vision modules.
  - Install: `dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui`

- [DSH iOS](https://github.com/ZSeven-W/dsh-ios) - **227 stars** | `MIT`. An iOS companion bundle for DeepSeek Harness with native mobile controls and a Cordis client bridge.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-ios@latest`

- [DSH Visualize](https://github.com/Nagi-ovo/dsh-visualize) - **208 stars** | `BSD-3-Clause`. An inline visualization plugin that renders interactive HTML fragments as sandboxed cards in DSH conversations.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-visualize`

- [DSH Synapse](https://github.com/liangmianya/dsh-synapse) - **191 stars** | `MIT`. A DeepSeek Harness bundle that adds a visual synapse workspace for navigating related context and tools.
  - Install: `corepack pnpm dsh plugin --profile web add github:liangmianya/dsh-synapse`

- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) - **149 stars** | `MIT`. An OpenPencil plugin that lets DSH agents preview, inspect, and edit real multi-frame design documents.
  - Install: `pnpm dlx --package=@deepseek-ai/dsh@0.1.0-rc.6 dsh plugin --profile web add @zseven-w/dsh-openpencil@latest`

- [DSH Oil Creator](https://github.com/oil-oil/dsh-oil-creator) - **131 stars** | `MIT`. A DeepSeek Harness creative bundle for generating and organizing Oil-style visual content.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-oil-creator`

- [GAL View](https://github.com/Ayase34/gal-view) - **125 stars** | `MIT`. A DSH Web conversation view with a Galgame-style layout and an editor for scene elements.
  - Install: `dsh plugin --profile web add github:Ayase34/gal-view#main`

- [DSH Damage Pulse](https://github.com/wssfk12138/dsh-damage-pulse) - **111 stars** | `MIT`. A DSH Web plugin that tracks token usage, account balance, session costs, and peak/off-peak pricing with a whale companion.
  - Install: `dsh plugin --profile web add github:wssfk12138/dsh-damage-pulse`

- [DSH Reasoning Effort](https://github.com/HanaAyane/dsh-reasoning-effort) - **106 stars** | `MIT`. Model and reasoning-effort controls for DSH with a slider, model-advertised levels, and themed selector views.
  - Install: `dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main`

- [DSH Android](https://github.com/ZSeven-W/dsh-android) - **104 stars** | `MIT`. A DeepSeek Harness bundle for controlling Android emulators or USB devices with ADB, live streaming, UI actions, builds, logs, and OCR.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-android@latest`

- [DSH Web UI Market](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - **100 stars** | `MIT`. A Web UI marketplace for browsing the curated DSH catalog and installing or removing plugins from a profile.
  - Install: `dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin`

- [DSH Skill & MCP Panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) - **98 stars** | `MIT`. A Web settings panel for managing DSH Skills and MCP servers through profile configuration.
  - Install: `dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.1/dsh-skill-mcp-panel-2.0.1.tgz`

- [Tabbit Browser](https://github.com/Tabbit-Browser/dsh-tabbit) - **96 stars** | `MIT`. A DSH bundle that exposes Tabbit Browser skills and host tools through the Web profile.
  - Install: `dsh plugin --profile web add github:Tabbit-Browser/dsh-tabbit`

- [DeepSeek Harness GenUI](https://github.com/pengyue-polaron/deepseek-harness-genui) - **95 stars** | `MIT`. A DSH bundle that lets agents create focused React interfaces for complex tasks and carry user selections into later turns.
  - Install: `dsh plugin --profile web add dsh-plugin-genui`

- [ZAT DSH Engine](https://github.com/mishibeikejie/zat-dsh-engine) - **79 stars** | `MIT`. A Web UI marketplace for searching, installing, updating, and rolling back community DSH plugins.
  - Install: `dsh plugin --profile web add github:mishibeikejie/zat-dsh-engine`

- [DSH Popout Sidebar](https://github.com/e2mcc/dsh-popout-sidebar) - **78 stars** | `MIT`. A DeepSeek Harness bundle that opens the sidebar as a separate popout panel.
  - Install: `dsh plugin --profile web add github:e2mcc/dsh-popout-sidebar`

- [DSH Notification](https://github.com/omdsh-dev/dsh-notification) - **72 stars** | `MIT`. Browser desktop notifications for completed DSH turns with outcome toggles and keyword include or exclude rules.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.2.tar.gz`

- [DSH Plugin Console](https://github.com/Noob-stupid/dsh-plugin-hub) - **69 stars** | `MIT`. A DSH settings panel for enabling, disabling, inspecting, and installing community plugins from multiple sources.
  - Install: `dsh plugin --profile web add github:Noob-stupid/dsh-plugin-hub`

- [DSH Web Plugin Manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - **67 stars** | `MIT`. A DSH Web plugin manager with install guards, health checks, rollback, environment controls, and marketplace browsing.
  - Install: `dsh plugin --profile web add dsh-web-plugin-manager@latest`

- [DSH Plugin Store](https://github.com/ZASENJC/dsh-plugins-store) - **65 stars** | `MIT`. A Web plugin that lets users browse, validate, install, update, and remove community DSH plugins after confirmation.
  - Install: `dsh plugin --profile web add npm:dsh-plugins-store`

- [DSH Stock Watch](https://github.com/Awu12277/dsh-stock-watch) - **61 stars** | `MIT`. A Web UI stock monitor with watchlists, groups, intraday and candlestick charts, target prices, and a draggable panel.
  - Install: `dsh plugin --profile web add dsh-stock-watch`

- [SeekTTY](https://github.com/Hilbert-beinghappy/seektty) - **61 stars** | `MIT`. A keyboard-first terminal workspace for DeepSeek Harness with session controls, a plugin center, themes, and workflow commands.
  - Install: `dsh plugin --profile tui add https://github.com/Hilbert-beinghappy/seektty/releases/download/v1.2.0/seektty-1.2.0.tgz`

- [DSH Thin Plugin Console](https://github.com/vlln/plugin-registry) - **56 stars** | `MIT`. A Web settings panel for installing, inspecting, updating, enabling, and disabling profile plugins without manual patch editing.
  - Install: `dsh plugin --profile web add @vlln/plugin-console@0.1.0`

- [OpenMA DSH TUI](https://github.com/openma-ai/Martty) - **56 stars** | `MIT`. A terminal-native DSH profile with an ACP plugin tree, streamed sessions, themes, overlays, and native TUI rendering.
  - Install: `dsh plugin --profile tui add @openma/deepseek-harness-tui@latest`

- [DSH Smooth Stream](https://github.com/Laplace-bit/dsh-smooth-stream) - **52 stars** | `MIT`. A DSH Web rendering plugin for smoother streaming output and scrolling across Markdown, code, tables, and tool results.
  - Install: `dsh plugin --profile web add dsh-smooth-stream`

- [DSH Status Rotator](https://github.com/01Virex/dsh-status-rotator) - **51 stars** | `MIT`. A DeepSeek Harness bundle that rotates status messages while a task is running.
  - Install: `dsh plugin --profile web add dsh-status-rotator`

- [DSH Web Mobile](https://github.com/mexiaosqwq/dsh-web-mobile) - **51 stars** | `MIT`. A responsive Web UI plugin that adapts the DSH interface for narrow and portrait-oriented screens.
  - Install: `dsh plugin --profile web add github:mexiaosqwq/dsh-web-mobile`

- [DSH Session Manager](https://github.com/dream12347/dsh-session-manager) - **48 stars** | `MIT`. A DSH Web session manager for archived sessions, trash recovery, activity statistics, forking, workspace grouping, and context settings.
  - Install: `dsh plugin --profile web add github:dream12347/dsh-session-manager#v0.2.2`

- [DSH Auto Collapse](https://github.com/a179-sanae/dsh-auto-collapse) - **45 stars** | `MIT`. A DSH Web client plugin that folds tool cards and reasoning blocks into compact summaries.
  - Install: `dsh plugin --profile web add dsh-auto-collapse`

- [DSH Trace Compare](https://github.com/lamost423/dsh-trace-compare) - **44 stars** | `MIT`. A DSH Web trace viewer for aligning session runs, comparing branches, inspecting failures, and exporting visual reports.
  - Install: `dsh plugin --profile web add dsh-trace-compare`

- [DSH Status Label](https://github.com/alingalingling/ui-status-label) - **40 stars** | `MIT`. Configurable running-turn status text for DSH Web, with a settings row and conversation-status provider.
  - Install: `dsh plugin --profile web add dsh-ui-status-label`

### Vision

- [Modlens](https://github.com/liustack/modlens) - **3.6k stars** | `MIT`. A vision plugin that returns structured OCR, layout, and semantic evidence to text-only DSH models.
  - Install: `dsh plugin --profile web add @liustack/modlens@3.16.6`

- [DSH Vision Router](https://github.com/ysr666/dsh-vision-router) - **950 stars** | `MIT`. A vision routing plugin with image questions, grounding, crops, pixel comparison, OCR, and screenshot tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router`

- [DSH Vision Toolkit](https://github.com/Anionex/dsh-vision-toolkit) - **818 stars** | `MIT`. A native vision bundle for image questions, long-screenshot OCR, UI reconstruction, grounding, and pixel comparison.
  - Install: `dsh plugin --profile web add @anionex/dsh-vision-toolkit`

- [DSH Image Gen](https://github.com/shanliuling/dsh-image-gen) - **158 stars** | `MIT`. A Web plugin that adds image-generation tools and settings to DeepSeek Harness conversations.
  - Install: `dsh plugin --profile web add dsh-image-gen`

- [DSH Vision](https://github.com/oil-oil/dsh-vision) - **87 stars** | `MIT`. Vision tools for DSH that preserve native image input and bridge text-only models to an external vision model.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision`

- [PictureReader](https://github.com/jing-hy/picturereader) - **34 stars** | `MIT`. A DeepSeek Harness vision bundle for reading and describing information from images.
  - Install: `dsh plugin --profile web add picturereader`

### Workflow & Automation

- [Reactive Resume DSH Plugin](https://github.com/amruthpillai/reactive-resume) - **41.6k stars** | `MIT`. A DeepSeek Harness bundle that connects Reactive Resume to a session for reading, creating, and editing resumes and job applications.
  - Install: `dsh plugin --profile web add dsh-plugin-reactive-resume`

- [Ouroboros](https://github.com/Q00/ouroboros) - **5.6k stars** | `MIT`. A DeepSeek Harness bundle that exposes the Ouroboros spec-first development workflow as native tools and chat commands.
  - Install: `dsh plugin --profile web add "github:Q00/ouroboros#main&path:integrations/dsh-plugin"`

- [Codex Taskboard DSH Integration](https://github.com/chuspeeism/dashi-taskboard) - **2.5k stars** | `Apache-2.0`. A DeepSeek Harness bundle that adds a Taskboard sidebar entry and opens the installed Codex Taskboard runtime.
  - Install: `dsh plugin --profile web add /absolute/path/to/codex-taskboard/integrations/deepseek-harness`

- [Chorus DSH](https://github.com/Chorus-AIDLC/Chorus) - **1.1k stars** | `AGPL-3.0`. A native DeepSeek Harness bundle for Chorus lifecycle automation, prompt behavior, MCP access, and AI-DLC skills.
  - Install: `dsh plugin --profile web add @chorus-aidlc/chorus-dsh -w`

- [Aegis](https://github.com/GanyuanRan/Aegis) - **1.1k stars** | `MIT`. A DeepSeek Harness bundle for the Aegis agent's guarded filesystem and skill workflows.
  - Install: `dsh plugin --profile web add github:GanyuanRan/Aegis`

- [TongFlow DSH Plugin](https://github.com/tong-io/tongflow) - **918 stars** | `AGPL-3.0-only`. A multimodal workflow studio for generating and reviewing image, audio, video, and 3D assets from saved workflows inside DSH.
  - Install: `dsh plugin --profile web add dsh-tongflow`

- [DSH Agent Teams](https://github.com/NanmiCoder/dsh-agent-teams) - **914 stars** | `MIT`. A team orchestration plugin that adds tools for creating agent groups, assigning work, and tracking shared state.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-agent-teams`

- [DSH IM](https://github.com/xmanrui/dsh-im) - **706 stars** | `MIT`. A single DSH settings plugin for connecting Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord, and WhatsApp bots.
  - Install: `dsh plugin --profile web add @xmanrui/dsh-im`

- [Treg DSH](https://github.com/superdesigndev/treg) - **574 stars** | `Apache-2.0 + additional terms`. A DSH bundle that exposes the Treg tool registry as an optional MCP connector and packaged Skill.
  - Install: `dsh plugin --profile web add github:superdesigndev/treg`

- [EasyEDA Agent DSH](https://github.com/zhoushoujianwork/easyeda-agent) - **286 stars** | `MIT`. A DeepSeek Harness bundle that adds EasyEDA Pro schematic and PCB automation through typed tools and an agent skill.
  - Install: `dsh plugin --profile web add "github:zhoushoujianwork/easyeda-agent#<tag>"`

- [DSH Plugin Subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - **256 stars** | `MIT`. An OAuth-based provider plugin that connects ChatGPT, Claude, and Grok subscriptions to DSH without separate API keys.
  - Install: `dsh plugin --profile web add dsh-plugin-subscriptions`

- [ModSearch](https://github.com/liustack/modsearch) - **237 stars** | `MIT`. A DSH web-search plugin that adds search, X search, and focused page reading through the ModSearch engine chain.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest`

- [AnySearch DSH](https://github.com/anysearch-team/anysearch-dsh) - **230 stars** | `MIT`. Web search for DSH with source discovery, vertical search, bounded batch queries, and cleaned page content.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @anysearch/anysearch-dsh`

- [DSH Pentest](https://github.com/howmp/dsh-pentest) - **224 stars** | `MIT`. A DSH security workflow plugin that records penetration-test targets, clues, proposals, decisions, and reports in the Web UI.
  - Install: `dsh plugin --profile web add https://github.com/howmp/dsh-pentest/releases/latest/download/dsh-pentest.tar.gz`

- [DSH Agent RP](https://github.com/hewzhew/dsh-agent-rp) - **182 stars** | `MIT`. A DeepSeek Harness roleplay bundle with SillyTavern migration, agent personas, and conversation workflow tools.
  - Install: `npx -p @deepseek-ai/dsh@latest dsh plugin --profile web add github:hewzhew/dsh-agent-rp#main`

- [DSH Cost Meter](https://github.com/Han-1413141/dsh-cost-meter) - **171 stars** | `MIT`. Session cost tracking for DSH with daily totals, history, budget views, and synchronized model pricing.
  - Install: `dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.3.1`

- [DSH Data Agent](https://github.com/omdsh-dev/dsh-data-agent) - **160 stars** | `MIT`. Database connections, masked forms, SQL tools, and a shared data-analysis preset for DSH Web and TUI.
  - Install: `dsh plugin --profile web add @yejiming/dsh-data-agent`

- [Oh Story DSH](https://github.com/worldwonderer/oh-story-dsh) - **160 stars** | `MIT`. A DSH plugin for fiction and short-drama production with writing skills, specialist roles, workspace routing, and previews.
  - Install: `dsh plugin --profile web add @oh-story/dsh@0.1.2`

- [Anime Find](https://github.com/cocofhu/anime-find) - **159 stars** | `MIT`. A DSH Web search plugin that gathers anime results into cards with metadata, resource links, and optional streaming views.
  - Install: `dsh plugin --profile web add github:cocofhu/anime-find`

- [pi2dsh](https://github.com/weijiafu14/pi2dsh) - **158 stars** | `MIT`. A DeepSeek Harness bundle that brings the pi coding agent's workflow and tools into DSH.
  - Install: `dsh plugin --profile web add pi2dsh`

- [DSH Super Injector](https://github.com/yjh051108/dsh-super-injector) - **144 stars** | `BSD-3-Clause`. A DSH development plugin for injecting, hot-reloading, and removing local plugin packages without a restart.
  - Install: `dsh plugin --profile web add github:yjh051108/dsh-super-injector`

- [TokenLedger](https://github.com/zh667/TokenLedger) - **141 stars** | `MIT`. A DeepSeek Harness bundle for tracking token usage and recording session cost data.
  - Install: `dsh plugin --profile web add "github:zh667/TokenLedger"`

- [DSH Remote Web Gateway](https://github.com/summer1238/dsh-remote-web-gateway) - **134 stars** | `MIT`. A DSH Web plugin for phone and tablet access with QR pairing, per-device authorization, revocation, and a Cloudflare Quick Tunnel.
  - Install: `dsh plugin --profile web add dsh-remote-web-gateway`

- [DSH Auto Mode](https://github.com/NanmiCoder/dsh-auto-mode) - **123 stars** | `MIT`. A fail-closed permission policy plugin that classifies DSH tool calls before automatic execution.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-auto-mode`

- [DSH Agent Team GUI](https://github.com/toolclub/dsh-agent-team-gui) - **121 stars** | `MIT`. Persistent multi-model teams for DSH with durable orchestration, DAG workflows, run history, and provider-reported usage.
  - Install: `dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v0.5.0`

- [DSH Plugin Bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - **119 stars** | `MIT`. A session migration plugin that previews a bounded handoff to another preset while leaving the original session unchanged.
  - Install: `dsh plugin --profile web add dsh-plugin-bridge`

- [DSH Usage Stats](https://github.com/Ychris12138/dsh-usage-stats) - **113 stars** | `MIT`. A DSH Web dashboard for token usage, provider balances, subscription quotas, and historical activity.
  - Install: `dsh plugin --profile web add github:Ychris12138/dsh-usage-stats`

- [DSH Taskboard](https://github.com/shengsheng90/DSH-taskboard) - **110 stars** | `Apache-2.0`. A DeepSeek Harness taskboard bundle for organizing tasks and monitoring workflow progress.
  - Install: `dsh plugin --profile web add -w /absolute/path/to/shengsheng-dsh-taskboard-<version>.tgz`

- [Argo DSH](https://github.com/taxueseek/argo) - **108 stars** | `MIT`. A DSH profile bundle that mounts Argo search MCP tools and an evidence-oriented research workflow.
  - Install: `dsh plugin --profile web add "github:taxueseek/argo#main&path:packages/dsh-plugin"`

- [DSH Crew](https://github.com/ZSeven-W/dsh-crew) - **105 stars** | `MIT`. A DSH hub for dispatching work to native subagents, tracking progress, and bridging Claude Code or Codex workers.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-crew@latest`

- [DSH Agent Workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) - **104 stars** | `MIT`. A Web UI plugin that presents model requests, responses, and tool calls as a navigable workflow for each DSH conversation.
  - Install: `dsh plugin --profile web add github:xuanyuanzhifeng/dsh-plugin-agent-workflow#v0.1.0 --workspace-root`

- [DSH Workflow](https://github.com/omdsh-dev/dsh_workflow) - **99 stars** | `MIT`. A reusable DSH workflow layer for multi-agent runs with saved plans, approvals, background jobs, and resumable execution.
  - Install: `dsh plugin --profile web add github:dsh-external/dsh_workflow#main`

- [Odai DSH Plugin](https://github.com/orziz/odai) - **95 stars** | `MIT`. A profile-wide DSH governance and routing bundle with an embedded Odai skill and runtime.
  - Install: `dsh plugin --profile web add odai-dsh-plugin`

- [DSH CommandCode Provider](https://github.com/Mars-Sea/dsh-commandcode-provider) - **93 stars** | `MIT`. An LLM provider plugin that adds a live Command Code model catalog, reasoning controls, and a Models-page card to DSH.
  - Install: `dsh plugin --profile web add @mars-sea/dsh-commandcode-provider`

- [DSH Auto Review](https://github.com/PerryLink/dsh-auto-review) - **90 stars** | `Apache-2.0`. A read-only reviewer subagent that returns structured allow or deny verdicts for DSH approval requests and fails closed by default.
  - Install: `dsh plugin --profile web add dsh-auto-review`

- [Superpowers DSH](https://github.com/LayneChai/superpowers-dsh) - **84 stars** | `MIT`. A DeepSeek Harness bundle that packages the Superpowers development workflow as native DSH skills.
  - Install: `dsh plugin --profile web add github:LayneChai/superpowers-dsh`

- [DSH Evolve Modes](https://github.com/GraySilver/dsh-evolve-modes) - **82 stars** | `MIT`. A DSH Web plugin for composing agent modes, quality gates, and self-evolution rules from the conversation input area.
  - Install: `dsh plugin --profile web add https://github.com/GraySilver/dsh-evolve-modes/releases/download/v0.3.1/graysilver-dsh-evolve-modes-0.3.1.tgz`

- [DSH Plugin Finder](https://github.com/awesome-dsh-plugin/dsh-find-plugin) - **82 stars** | `MIT`. Searches GitHub's DSH plugin ecosystem from inside a session and returns ranked results with ready-to-run install commands.
  - Install: `dsh plugin --profile web add dsh-find-plugin`

- [Dockyard DSH](https://github.com/AITabby/dockyard-dsh) - **77 stars** | `MIT`. A native DSH provider plugin with account pools, OAuth sign-in, model catalogs, quota status, and provider-specific requests.
  - Install: `dsh plugin --profile web add github:AITabby/dockyard-dsh`

- [DSH Automation](https://github.com/titanwings/dsh-automation) - **74 stars** | `MIT`. Scheduled coding runs for DSH with Web and agent controls, durable history, and guarded execution boundaries.
  - Install: `dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.6`

- [DSH QQ Bot](https://github.com/tencent-connect/dsh-qqbot) - **73 stars** | `MIT`. A QQ Bot channel for DSH that handles messaging, QR-code login, session events, and agent replies.
  - Install: `npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot`

- [DSH Reverse Skill](https://github.com/dhicoc/dsh-reverse-skill) - **70 stars** | `MIT`. A DeepSeek Harness bundle for reverse-engineering software behavior into reusable development skills.
  - Install: `dsh plugin --profile web add github:dhicoc/dsh-reverse-skill`

- [ForkProbe DSH](https://github.com/Jayden-X-L/forkprobe) - **70 stars** | `MIT`. A native DSH plugin for comparing Skills on the same task and choosing a winner from a local report.
  - Install: `dsh plugin --profile web add "github:Jayden-X-L/forkprobe"`

- [DSH Harness Wallet](https://github.com/feibi-mochi/deepseek-harness-control-center) - **62 stars** | `MIT`. A DSH Web plugin for account balances, usage tracking, completion alerts, recharge actions, and session controls.
  - Install: `dsh plugin --profile web add deepseek-harness-wallet`

- [DSH Notifier](https://github.com/THEWOLFWALKER/dsh-notifier) - **62 stars** | `MIT`. A notification and remote-approval layer for DSH with one notify API, multiple channel adapters, and optional mobile controls.
  - Install: `dsh plugin add dsh-notifier --profile web`

- [DSH Toy](https://github.com/c3ll256/dsh-toy) - **62 stars** | `BSD-3-Clause`. Safety-bounded DSH control for Buttplug and Intiface devices with optional MonsterParty toy integration.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy`

- [DSH Auth In One](https://github.com/Stormycry-cryp/dsh-AuthInOne) - **61 stars** | `MIT`. A DeepSeek Harness authentication bundle that manages common sign-in and profile setup flows.
  - Install: `dsh plugin --profile web add github:Stormycry-cryp/dsh-AuthInOne#v0.2.0-alpha.4`

- [DSH Balance Monitor](https://github.com/yxxbc/dsh-balance-plugin) - **55 stars** | `MIT`. Balance monitoring, usage statistics, and third-party plugin management in the DSH Web interface.
  - Install: `dsh plugin --profile web add github:yxxbc/dsh-balance-plugin`

- [SpecFusion](https://github.com/wxkingstar/SpecFusion) - **55 stars** | `MIT`. A DSH plugin for searching enterprise API documentation and returning interface details while the agent writes code.
  - Install: `dsh plugin --profile web add @wxkingstar/specfusion-dsh`

- [Morning Star DSH](https://github.com/btspoony/mstar-harness) - **53 stars** | `MIT`. In-process DSH workflow gates that validate status, control dispatch, and expose the Morning Star engine through refusal-aware channels.
  - Install: `dsh plugin --profile web add @mstar-harness/dsh`

- [OpenBiliClaw](https://github.com/whiteguo233/dsh-openbiliclaw) - **52 stars** | `BSD-3-Clause`. A DeepSeek Harness bundle for OpenBiliClaw workflows and related content tools.
  - Install: `dsh plugin --profile web add @openbiliclaw/dsh-plugin`

- [DeepSeek Flow](https://github.com/kanghelyu/dsh-deepseek-flow) - **50 stars** | `MIT`. A Markdown-first workflow editor for DSH with a synchronized canvas, Boolean gates, reviewable changes, and AI-assisted workflow maintenance.
  - Install: `dsh plugin --profile web add "github:kanghelyu/dsh-deepseek-flow#main"`

- [DSH Remote QR](https://github.com/xgone/dsh-remote) - **43 stars** | `MIT`. A DSH Web remote-access plugin with account login, MFA, browser-side workspace selection, and protected WebSocket access.
  - Install: `dsh plugin --profile web add @xgone/dsh-remote@0.1.1`

- [DSH Lark](https://github.com/omdsh-dev/dsh-lark) - **41 stars** | `BSD-3-Clause`. A Feishu/Lark channel for sending tasks to DSH agents and returning replies, approvals, and cards to chat.
  - Install: `dsh plugin --profile web add dsh-lark-channel@latest`

- [DSH Auto Continue](https://github.com/HsiangNianian/dsh-auto-continue) - **36 stars** | `MIT`. A DeepSeek Harness bundle that automatically continues a task after an interaction reaches its limit.
  - Install: `dsh plugin --profile web add dsh-client-auto-continue`

- [AX Feishu Bridge](https://github.com/AX1202/ax-feishu-bridge) - **35 stars** | `MIT`. A Feishu/Lark bridge that lets users chat with Pi or DeepSeek Harness from the same messaging workspace.
  - Install: `dsh plugin --profile web add ax-feishu-bridge --ignore-scripts`

- [DSH Lark Bridge](https://github.com/bihangchi9-creator/dsh-lark-bridge) - **35 stars** | `MIT`. A DeepSeek Harness bundle that connects Feishu and Lark group chats to isolated agent sessions and project directories.
  - Install: `dsh plugin --profile web add link:/path/to/dsh-lark-bridge`

- [DSH Usage Plugin](https://github.com/feiyang-dev/dsh-usage-plugin) - **35 stars** | `MIT`. A DeepSeek Harness bundle for viewing usage statistics and token consumption during sessions.
  - Install: `dsh plugin --profile web add @feiyang666/dsh-usage-plugin`

- [DSH Interconnect](https://github.com/Chinesezjc/dsh-interconnect) - **34 stars** | `MIT`. Cross-instance DSH messaging and event handoff with host services, model-facing tools, and shared-token authentication.
  - Install: `dsh plugin --profile web add dsh-interconnect`

- [DSH Save Money](https://github.com/zhu168/dsh-save-money) - **33 stars** | `MIT`. A DeepSeek Harness bundle for tracking model usage and helping reduce unnecessary token spending.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-save-money`
<!-- END GENERATED CATEGORY LIST -->

## Install plugins carefully

DSH plugins run third-party code with your account permissions. A plugin can read files, access environment variables, start processes, and use the network. Inclusion confirms the repository shape and installation evidence; it is not a security audit. Read the source and install unfamiliar plugins in an isolated workspace without production credentials.

## Related resources

- [DeepSeek Harness documentation](https://deepseek-harness.github.io/deepseek-harness/) - Official installation, configuration, and development guides.
- [Official `dsh-plugin` topic](https://github.com/topics/dsh-plugin) - A discovery feed that still requires code-level verification.
- [ScriptByAI](https://www.scriptbyai.com/) - AI tools, coding agents, and practical technical guides.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request. Additions must provide code-level DSH evidence and meet the admission threshold.
