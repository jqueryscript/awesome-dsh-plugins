# Awesome DeepSeek Harness Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A verified, category-organized list of community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), with exact GitHub Star counts.

[![Quality](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/quality.yml)
[![Update Stars](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml/badge.svg)](https://github.com/jqueryscript/awesome-dsh-plugins/actions/workflows/update-stars.yml)

**Last verified:** 2026-09-02 | **Minimum at admission:** 30 stars | **Plugins:** 285

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

- [OpenDesign DSH Runtime](https://github.com/nexu-io/open-design) - **92.3k stars** | `Apache-2.0`. A DeepSeek Harness profile bundle that connects OpenDesign to a user-installed DSH runtime through a structured stdio protocol.
  - Install: `pnpm --filter @open-design/dsh-runtime build && pnpm -C packages/dsh-runtime pack --pack-destination <temporary-directory> && dsh plugin --profile open-design add <temporary-directory>/open-design-dsh-runtime-0.1.0.tgz`

- [Mirage DSH](https://github.com/strukto-ai/mirage) - **3.6k stars** | `Apache-2.0`. A DSH filesystem and shell provider that mounts remote and local resources inside one virtual workspace.
  - Install: `dsh plugin --profile web add @struktoai/mirage-dsh`

- [API Relay Audit DSH](https://github.com/toby-bridges/api-relay-audit) - **816 stars** | `AGPL-3.0-only`. A DeepSeek Harness bundle for auditing API relays for prompt injection, model substitution, tool-call rewriting, SSE anomalies, and error leakage.
  - Install: `dsh plugin --profile web add "github:toby-bridges/api-relay-audit#v2.4.0"`

- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) - **635 stars** | `Apache-2.0`. A DSH bundle that connects the managed-agents runtime through the official stdio MCP client.
  - Install: `npm ci && npm run build:runtime && npm link && dsh plugin --profile web add managed-agents`

- [AgentGuard DSH](https://github.com/GoPlusSecurity/agentguard) - **457 stars** | `MIT`. A DeepSeek Harness bundle for scanning plugin sources and reporting or enforcing runtime tool-call security policies.
  - Install: `dsh plugin --profile web add @goplus/agentguard`

- [DSH Purge](https://github.com/YuJunZhiXue/dsh-purge) - **257 stars** | `MIT`. Adds a DSH settings panel for managing prompt rules, permission policies, and tool-limit patches.
  - Install: `dsh plugin --profile web add https://github.com/YuJunZhiXue/dsh-purge/archive/refs/heads/master.zip`

- [Invoice Downloader DSH](https://github.com/EthanYoQ/Invoice-Downloader) - **233 stars** | `Apache-2.0`. A DSH bundle for local IMAP invoice downloads, OCR, archiving, and Excel summaries from a Web sidebar.
  - Install: `dsh plugin --profile web add @ethanyoq/dsh-invoice-downloader`

- [Univer Office DSH](https://github.com/dream-num/dsh-univer-office) - **186 stars** | `Apache-2.0`. A DSH office bundle for creating and editing spreadsheets, documents, presentations, tables, canvases, and existing office files.
  - Install: `dsh plugin --profile web add dsh-univer-office`

- [DSH Git Bash Preset](https://github.com/liceses/dsh-gitbash-preset) - **138 stars** | `MIT`. A DeepSeek Harness preset that configures Git Bash support and a ready-to-use terminal environment.
  - Install: `dsh plugin --profile web add @icelily/dsh-gitbash-preset`

- [DSH Undo Savepoint](https://github.com/lire1131/dsh-undo-savepoint) - **132 stars** | `MIT`. Crash recovery for DSH that snapshots configuration and plugin code for undo, redo, rollback, and safe-mode starts.
  - Install: `dsh plugin --profile web add github:lire1131/dsh-undo-savepoint#master`

- [DSH Standard Adapter](https://github.com/Yan-Zero/dsh-std) - **114 stars** | `MIT`. A DeepSeek Harness adapter that discovers standard plugin manifests and activates negotiated server and browser contributions.
  - Install: `dsh plugin --profile web add @dsh-std/adapter-dsh`

- [DSH Network Settings](https://github.com/kanneiren/dsh-network-settings) - **86 stars** | `MIT`. A DeepSeek Harness Web bundle for configuring network endpoints, proxies, health checks, and connection settings.
  - Install: `dsh plugin --profile web add dsh-network-settings`

- [DSH Permission Rules](https://github.com/PerryLink/dsh-permission-rules) - **79 stars** | `Apache-2.0`. A DeepSeek Harness bundle for declarative tool permissions and process-level network policy with a settings editor.
  - Install: `dsh plugin --profile web add github:PerryLink/dsh-permission-rules#main`

- [Multica DSH Runtime](https://github.com/multica-ai/dsh-multica-runtime) - **57 stars** | `No standard license`. A local DSH runtime bridge for Multica that exposes a versioned stdio protocol without patching the Harness source.
  - Install: `dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime`

- [Local Shell MCP](https://github.com/fwerkor/local-shell-mcp) - **56 stars** | `MIT`. A DSH bridge for local-shell-mcp that exposes shell, files, browser, and remote-worker tools through per-session connections.
  - Install: `dsh plugin --profile web add 'github:fwerkor/local-shell-mcp#main'`

- [DSH Codex Shell](https://github.com/Ephemeral-AI-Lab/dsh-plugins) - **48 stars** | `MIT`. A shell plugin that adds interactive exec_command and write_stdin tools to DSH profiles.
  - Install: `dsh plugin --profile web add dsh-codex-shell@0.1.2`

- [DSH MinerU](https://github.com/HuanLinOTO/dsh-plugin-mineru) - **43 stars** | `AGPL-3.0`. MinerU-backed document parsing tools that convert PDF, images, DOCX, PPTX, and XLSX files into structured Markdown or JSON.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-mineru`

- [DSH Benign Exit](https://github.com/sunruize93-cmyk/dsh-benign-exit) - **42 stars** | `MIT`. A DeepSeek Harness bundle that provides a controlled exit command for completed or canceled tasks.
  - Install: `dsh plugin --profile web add dsh-benign-exit`

- [DSH WSL Workspace](https://github.com/6Mikao9/dsh-wsl-workspace) - **41 stars** | `MIT`. A DeepSeek Harness bundle that provides WSL-backed filesystem and shell access for Windows workspaces.
  - Install: `dsh plugin --profile web add dsh-wsl-workspace`

- [DSH Config Manager](https://github.com/xiajiajun516/dsh-config-manager) - **40 stars** | `MIT`. A DSH plugin for backing up, restoring, migrating, and syncing DSH settings, plugins, MCP servers, skills, and workspaces.
  - Install: `dsh plugin --profile web add dsh-config-manager@latest`

- [DSH Sandbox Escalation Fix](https://github.com/HakureiMonika/dsh-sandbox-escalation-fix) - **40 stars** | `MIT`. A compatibility plugin for DSH sandbox escalation, tool permissions, and third-party model sessions.
  - Install: `dsh plugin --profile web add github:HakureiMonika/dsh-sandbox-escalation-fix`

- [DSH Remote](https://github.com/flymysql/dsh-remote) - **39 stars** | `MIT`. A DeepSeek Harness bundle for connecting the client to a remote runtime.
  - Install: `dsh plugin --profile web add dsh-remote`

- [DSH Plugin Guard](https://github.com/lxzy-7/dsh-plugin-guard) - **35 stars** | `MIT`. A DeepSeek Harness bundle that snapshots plugin and profile changes, guards boot, and rolls back failed installations.
  - Install: `dsh plugin --profile web add github:lxzy-7/dsh-plugin-guard`

- [DSH Files](https://github.com/taxueseek/dsh-files) - **30 stars** | `MIT`. A DSH bundle for isolated file uploads, document reading, and cached text extraction across common file formats.
  - Install: `dsh plugin --profile web add git+https://github.com/taxueseek/dsh-files.git`

### Input & Navigation

- [OpenGUI DSH](https://github.com/Core-Mate/OpenGUI) - **1.6k stars** | `MIT`. A DSH plugin for controlling authorized Android phones and a managed local browser through delegated tasks.
  - Install: `dsh plugin --profile web add ./deepseek-harness-plugin`

- [BrowserSkill DSH Plugin](https://github.com/Tencent/BrowserSkill) - **1.5k stars** | `MIT`. A DeepSeek Harness bundle that exposes BrowserSkill browser automation tools for sessions, navigation, snapshots, clicks, forms, and screenshots.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/browser-skill-dsh-plugin`

- [DSH Pocket](https://github.com/shaobeichen/dsh-pocket) - **770 stars** | `GPL-2.0`. A Web plugin that mirrors DSH sessions to a phone over a local network or a password-protected Cloudflare tunnel.
  - Install: `dsh plugin --profile web add dsh-pocket -w`

- [DSH At File](https://github.com/FSMargoo/dsh-at-file) - **489 stars** | `MIT`. A composer extension for searching workspace paths with at-file mentions and attaching file contents to prompts.
  - Install: `dsh plugin --profile web add https://github.com/FSMargoo/dsh-at-file/archive/refs/tags/v0.6.0.tar.gz`

- [DSH Mobile](https://github.com/saya-ch/dsh-mobile) - **171 stars** | `Apache-2.0`. A DeepSeek Harness mobile bundle with touch-friendly navigation and a compact conversation layout.
  - Install: `dsh plugin --profile web add dsh-mobile@alpha`

- [DSH Harness Remote](https://github.com/liguobao/deepseek-harness-remote) - **121 stars** | `MIT`. A DeepSeek Harness bundle that adds encrypted remote access for continuing sessions from desktop, Web, and Android clients.
  - Install: `dsh plugin --profile web add ds-harness-remote@0.3.29`

- [Humanizer RU DSH](https://github.com/Vladimir-Human/humanizer-ru) - **117 stars** | `MIT`. A Russian text-humanization bundle for DSH with reusable writing skills.
  - Install: `dsh plugin --profile web add "github:Vladimir-Human/humanizer-ru#path:/dsh"`

- [DSH Turn Delete](https://github.com/hanshenmesen/dsh-turn-delete) - **106 stars** | `MIT`. A DSH Web plugin for deleting one complete closed conversation turn while preserving the Session and later turns.
  - Install: `dsh plugin --profile web add dsh-turn-delete`

- [DSH Annotation](https://github.com/omdsh-dev/dsh-annotation) - **101 stars** | `MIT`. A DSH Web selection tool that annotates assistant text and sends numbered annotation blocks with a message.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git`

- [DSH EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) - **96 stars** | `MIT`. A DSH Web editing plugin for recalling, rewriting, versioning, and restoring user messages.
  - Install: `dsh plugin --profile web add dsh-easyrewrite`

- [DSH Free Search](https://github.com/DDDMUC/dsh-free-search) - **79 stars** | `MIT`. A multi-engine DSH search provider with free backends, automatic fallback, settings, and platform search.
  - Install: `git clone https://github.com/DDDMUC/dsh-free-search.git && dsh plugin --profile web add ./dsh-free-search`

- [DSH Omi Voice](https://github.com/PolinniZhong/dsh-omi-voice) - **70 stars** | `MIT`. A DSH Web voice plugin for click-to-read and automatic conversation narration through Omi.
  - Install: `dsh plugin --profile web add "github:PolinniZhong/dsh-omi-voice#v0.1.2&path:/"`

- [DSH Claude UX](https://github.com/eri64/dsh-claude-ux) - **67 stars** | `MIT`. A Web plugin that adds reversible region risk controls and automatic conversation termination for abusive interactions.
  - Install: `dsh plugin --profile web add github:eri64/dsh-claude-ux`

- [DSH Meme](https://github.com/yyh-001/dsh-meme) - **65 stars** | `MIT`. A DSH meme plugin with searchable image packs, learned memes, emotion-based sending, and a composer picker.
  - Install: `dsh plugin --profile web add dsh-meme`

- [Web Search Pro DSH](https://github.com/anweat/dsh-web-search-pro) - **60 stars** | `MIT`. A Web search bundle with multiple providers, persistent caching, site-specific search, and Playwright rendering tools.
  - Install: `dsh plugin --profile web add @anweat/dsh-browser@^0.1.8 dsh-web-search-pro@^0.1.8`

- [DSH Navbar](https://github.com/vlln/dsh-navbar) - **59 stars** | `MIT`. A conversation node bar that lets users jump quickly between user messages in the DSH Web view.
  - Install: `dsh plugin --profile web add @vlln/dsh-navbar`

- [DSH Prompt Enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) - **54 stars** | `No standard license`. A DeepSeek Harness bundle that adds prompt editing helpers and reusable input enhancements.
  - Install: `dsh plugin --profile web add github:Fishsb/dsh-prompt-enhancer#v3.3.1`

- [Open in VS Code](https://github.com/omdsh-dev/dsh-open-in-vscode) - **54 stars** | `MIT`. Adds a workspace-row action that opens the selected DSH directory in VS Code or another configured editor.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz`

- [DSH Message Edit](https://github.com/Moeblack/dsh-message-edit) - **44 stars** | `MIT`. A conversation plugin for branching, editing, rerolling, retrying, and reviewing DSH message versions.
  - Install: `dsh plugin --profile web add dsh-message-edit`

- [DSH Built-in Browser](https://github.com/wqty123/dsh-browser) - **40 stars** | `MIT`. A DeepSeek Harness plugin that gives agents a shared real browser for navigation and user-visible interaction.
  - Install: `dsh plugin --profile web add dsh-builtin-browser`

- [OpenCues DSH](https://github.com/opencues/opencues) - **39 stars** | `MIT`. A DSH composer plugin for word alternatives, underscore-gated fill-ins, and passive rewrite cues.
  - Install: `dsh plugin --profile web add @opencues/dsh`

- [DSH Chat Timeline](https://github.com/jjxjjjjiik-bot/dsh-chat-timeline) - **34 stars** | `MIT`. A DeepSeek Harness Web plugin that adds a conversation navigation panel with bookmarks and rollback links.
  - Install: `dsh plugin --profile web add dsh-chat-timeline`

- [DSH Computer Use](https://github.com/Anionex/dsh-computer-use) - **34 stars** | `MIT`. A macOS DeepSeek Harness bundle for scoped observation and foreground-app keyboard control with explicit permissions.
  - Install: `dsh plugin --profile web add @anionex/dsh-computer-use`

- [DSH Full Remote](https://github.com/JUANWANG-BUAA/dsh-full-remote) - **32 stars** | `MIT`. Adds a mobile-friendly remote control panel for a DeepSeek Harness Web profile.
  - Install: `dsh plugin --profile web add dsh-full-remote`

- [DSH Voice Scribe](https://github.com/PensiveFei/dsh-voice-scribe) - **31 stars** | `MIT`. A DSH voice input plugin that transcribes spoken prompts into the composer with optional OpenAI-compatible ASR.
  - Install: `dsh plugin --profile web add dsh-voice-scribe`

### Memory & Knowledge

- [OpenViking Memory](https://github.com/volcengine/OpenViking) - **34.1k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle with OpenViking auto-recall, session capture, protected viking:// URIs, and MCP tools.
  - Install: `dsh plugin --profile web add @openviking/dsh-memory-plugin`

- [Hindsight Coding Agents](https://github.com/vectorize-io/hindsight) - **21.6k stars** | `MIT`. A DeepSeek Harness memory bundle with automatic recall, session capture, knowledge pages, and per-repository memory banks.
  - Install: `dsh plugin --profile web add @vectorize-io/hindsight-coding-agents`

- [WeKnora Knowledge](https://github.com/Tencent/WeKnora) - **20.9k stars** | `MIT`. A DeepSeek Harness bundle for semantic knowledge search, document reading, and RAG answers over user-managed knowledge bases.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/dsh-weknora`

- [EverOS Memory](https://github.com/EverMind-AI/EverOS) - **12.5k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle that provides automatic cross-session recall through a local EverOS service.
  - Install: `dsh plugin --profile web add @evermind-ai/dsh-plugin`

- [MemOS Local Memory](https://github.com/MemTensor/MemOS) - **11.1k stars** | `MIT`. A local MemOS memory bundle for DeepSeek Harness with layered recall, reflection, policy induction, and skill crystallization.
  - Install: `curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/main/apps/memos-local-plugin/install.sh | bash -s -- --agent dsh --profile web`

- [ReMe](https://github.com/agentscope-ai/ReMe) - **3.4k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle with recall, capture, settings, and skill guidance for TypeScript agent workflows.
  - Install: `dsh plugin --profile web add @agentscope-ai/reme`

- [MemSearch](https://github.com/zilliztech/memsearch) - **2.5k stars** | `MIT`. A DeepSeek Harness memory bundle that captures shared Markdown notes, injects context before steps, and reviews candidate skills.
  - Install: `dsh plugin --profile web add @zilliz/memsearch-dsh`

- [mem9](https://github.com/mem9-ai/mem9) - **1.2k stars** | `Apache-2.0`. A persistent memory bundle for DeepSeek Harness with automatic recall, background ingest, and five memory tools.
  - Install: `dsh plugin --profile web add @mem9/dsh-plugin`

- [DSH Context](https://github.com/bowenliang123/dsh-context) - **1.1k stars** | `Apache-2.0`. A context dashboard and /context command that show how DSH messages, tools, injections, compactions, and token usage evolve.
  - Install: `dsh plugin --profile web add dsh-context`

- [Deja-vu DSH](https://github.com/vshulcz/deja-vu) - **734 stars** | `MIT`. A local session-history plugin that indexes other coding agents for recall, digests, file history, and optional automatic context.
  - Install: `dsh plugin --profile web add dsh-deja`

- [Graph Memory](https://github.com/adoresever/graph-memory) - **579 stars** | `MIT`. A graph-based memory plugin for cross-session recall, PageRank, communities, and vector search in DSH.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.1.tgz`

- [Mnemon](https://github.com/mnemon-dev/mnemon) - **534 stars** | `Apache-2.0`. A persistent memory plugin that supplies graph-based recall and cross-session knowledge to DSH agents.
  - Install: `dsh plugin --profile web add dsh-mnemon`

- [MisakaNet DSH](https://github.com/Ikalus1988/MisakaNet) - **430 stars** | `Apache-2.0`. A DSH plugin for searching and sharing verified debugging lessons from a local, Git-backed knowledge base.
  - Install: `dsh plugin add git+https://github.com/Ikalus1988/MisakaNet.git`

- [Flowix Memory](https://github.com/text2future/flowix) - **376 stars** | `MIT`. A config-only DSH bundle that exposes Flowix notebook memos and artifact tools through a local stdio MCP server.
  - Install: `dsh plugin --profile web add ./app/flowix-dsh-host/bundles/dsh-flowix-memory`

- [Mnemon DSH Plugin](https://github.com/omdsh-dev/dsh-mnemon) - **275 stars** | `MIT`. A DeepSeek Harness memory plugin with a three-tier control plane for storing and retrieving project context.
  - Install: `dsh plugin --profile web add dsh-mnemon`

- [DSH Memory Evolve](https://github.com/csyangwen/dsh-memory-evolve) - **256 stars** | `MIT`. A Web DSH memory and workflow plugin with cross-session recall, skill management, todos, session search, and external-agent dispatch.
  - Install: `dsh plugin --profile web add github:csyangwen/dsh-memory-evolve`

- [Polaris DSH Integration](https://github.com/ZJU-REAL/Polaris) - **213 stars** | `Apache-2.0`. A DSH bundle that connects Polaris MCP tools and native agent skills to a configured Polaris account.
  - Install: `cd integrations/deepseek-harness && npm ci && npm run check && dsh plugin --profile web add "$PWD"`

- [Engramory](https://github.com/tinqiao-oss/engramory) - **176 stars** | `MIT`. A file-based DSH memory plugin that keeps human-readable notes in a versioned store with deterministic limits.
  - Install: `dsh plugin --profile web add dsh-engramory`

- [DSH Notes](https://github.com/zhaoolee/notes) - **154 stars** | `MIT`. A DSH tool plugin that exports agent output into a self-hosted Notes service.
  - Install: `dsh plugin --profile web add @zhaoolee/dsh-notes`

- [DSH Noema](https://github.com/ZSeven-W/dsh-noema) - **127 stars** | `MIT`. Durable Noema-backed memory for DSH with recall tools, cross-agent imports, and a settings page.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-noema@latest`

- [DSH Git Memory](https://github.com/seriousz158/dsh-memory) - **123 stars** | `MIT`. A Git-backed long-term memory plugin that stores durable DSH memory locally, exposes settings controls, and optionally synchronizes idle sessions.
  - Install: `dsh plugin --profile web add github:seriousz158/dsh-memory`

- [DSH Chat Import](https://github.com/Nwflower/dsh-chat-import) - **120 stars** | `MIT`. A conversation migration plugin that imports histories from external agent tools into resumable DSH sessions and exports them back.
  - Install: `dsh plugin --profile web add dsh-chat-import`

- [DSH Mimir](https://github.com/1692775560/dsh-Mimir-Academic-research) - **109 stars** | `MIT`. A research assistant suite for DSH with literature search, a research wiki, LaTeX compilation, and subagent review.
  - Install: `dsh plugin --profile web add dsh-mimir@latest`

- [DSH Turn Rewind](https://github.com/Anionex/dsh-turn-rewind) - **105 stars** | `BSD-3-Clause`. A DSH recovery plugin that records workspace changes and restores a conversation turn through its Change Ledger.
  - Install: `dsh plugin --profile web add @anionex/dsh-turn-rewind`

- [Meow Memory](https://github.com/Phant0Meow/dsh-meow-memory) - **73 stars** | `MIT`. A cross-session memory bundle with layered storage, BM25 retrieval, session capture, and a configurable Web panel.
  - Install: `dsh plugin --profile web add github:Phant0Meow/dsh-meow-memory`

- [OpenContext DSH](https://github.com/melandlabs/opencontext) - **69 stars** | `Apache-2.0`. A DSH plugin for durable agent memory and retrieval-augmented context through OpenContext.
  - Install: `dsh plugin --profile web add dsh-opencontext`

- [DSH Memento](https://github.com/PerryLink/dsh-memento) - **68 stars** | `Apache-2.0`. A bounded cross-session memory service for DSH with approval-gated writes, audit trails, local SQLite storage, and recall tools.
  - Install: `dsh plugin --profile web add dsh-memento`

- [DSH Mneme](https://github.com/modusensus/dsh-mneme) - **63 stars** | `MIT`. A DSH memory plugin for persistent project knowledge and recall across sessions.
  - Install: `dsh plugin --profile web add @modusensus/dsh-mneme`

- [DSH Memory](https://github.com/FuRongJun-1999/dsh-memory) - **53 stars** | `MIT`. A DSH plugin that provides persistent cross-session memory for multiple agents.
  - Install: `dsh plugin --profile web add @furongjun1999/dsh-memory`

- [Billion Context DSH](https://github.com/Tyan66666/billion-context-dsh) - **52 stars** | `MIT`. A DSH memory plugin for large-context retrieval, persistence, and project knowledge.
  - Install: `dsh plugin --profile web add billion-context-dsh`

- [Causal Memory DSH Plugin](https://github.com/JingxuanC/causal-memory) - **51 stars** | `Apache-2.0`. A local causal-memory bridge that exposes a native DSH bundle for structured recall and memory tools.
  - Install: `cd <causal-memory-repo> && dsh plugin --profile web add "$PWD/dsh-plugin"`

- [Jingling DSH](https://github.com/Yi-111-a/dsh-jingling) - **51 stars** | `MIT`. A DeepSeek Harness companion bundle for local memory, guided reflection, and an optional desktop pet.
  - Install: `dsh plugin --profile web add dsh-jingling`

- [DSH DeepRead](https://github.com/xiehuan123/dsh-deepread) - **41 stars** | `MIT`. A DSH research-reading plugin for collecting sources, notes, evidence, and structured reading progress.
  - Install: `dsh plugin --profile web add dsh-deepread`

- [SkillRoute DSH](https://github.com/erichare/skillroute) - **39 stars** | `MIT`. A DSH bundle that connects SkillRoute's skill router and MCP tools to DeepSeek Harness agents.
  - Install: `dsh plugin --profile web add @skillroute/dsh-plugin`

- [Industry Research DSH](https://github.com/PerryLink/dsh-industry-research) - **34 stars** | `Apache-2.0`. A research bundle for industry maps, company timelines, evidence cards, and auditable reports in DSH.
  - Install: `dsh plugin --profile demo add dsh-industry-research`

- [Chinese Traditional Wisdom DSH](https://github.com/dhicoc/dsh-chinese-traditional-wisdom-skill) - **30 stars** | `MIT`. A DeepSeek Harness bundle that packages a local-first Chinese traditional wisdom consultation workflow.
  - Install: `dsh plugin add github:dhicoc/dsh-chinese-traditional-wisdom-skill`

- [DSH Research Report](https://github.com/PerryLink/dsh-research-report) - **30 stars** | `Apache-2.0`. A DeepSeek Harness bundle for producing evidence-linked research reports with verification states and audit artifacts.
  - Install: `dsh plugin --profile demo add dsh-research-report`

### Themes & Appearance

- [DSH Deep Whale](https://github.com/Small-tailqwq/dsh-deep-whale) - **1.8k stars** | `CC-BY-NC-SA-4.0`. A maid-atelier whale character skin for the DSH Web interface.
  - Install: `git clone https://github.com/Small-tailqwq/dsh-deep-whale.git && dsh plugin --profile web add ./dsh-deep-whale/maid-atelier`

- [DSH Balance Whale](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) - **1.2k stars** | `MIT`. A Web UI widget that displays DeepSeek account balance in a draggable whale companion.
  - Install: `dsh plugin --profile web add link:./dsh-whale-widget`

- [OpenPets DSH](https://github.com/alvinunreal/openpets) - **1.1k stars** | `MIT`. Adds an OpenPets desktop companion that reacts to DSH lifecycle events through a local Cordis bundle.
  - Install: `dsh plugin --profile <profile> add @open-pets/dsh`

- [DSH Ads](https://github.com/Nagi-ovo/dsh-ads) - **581 stars** | `BSD-3-Clause`. A parody Web UI plugin that adds fake banner ads, popups, and small games styled after early portal sites.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-ads`

- [DSH Pet](https://github.com/PC2005-cloud/dsh-pet) - **462 stars** | `MIT`. A floating DSH Web desktop pet with idle animations, random actions, screen wandering, and drag interactions.
  - Install: `dsh plugin --profile web add dsh-pet`

- [DSH Transparent UI](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - **388 stars** | `MIT`. A Web UI theme with adjustable glass effects, fluid or wallpaper backgrounds, and appearance controls for the DSH interface.
  - Install: `dsh plugin --profile web add dsh-client-ui-aqua`

- [Whale Girl](https://github.com/vlln/whale-girl) - **297 stars** | `MIT`. A draggable Web UI desktop pet with interaction, feeding, progress, and persistent state.
  - Install: `dsh plugin --profile web add github:vlln/whale-girl#main`

- [DSH Dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - **272 stars** | `See ASSET_LICENSE.md`. A desktop companion that reacts to DSH session events with a floating BigFish character and configurable behaviors.
  - Install: `pnpm exec dsh plugin --profile web add dsh-dafeiyu@alpha`

- [DSH Wallpaper Engine](https://github.com/elysia395/dsh-wallpaper-engine) - **202 stars** | `MIT`. A DeepSeek Harness theme bundle for setting animated wallpapers and managing visual backgrounds.
  - Install: `dsh plugin --profile web add dsh-plugin-wallpaper-engine`

- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) - **192 stars** | `MIT`. A DeepSeek Harness skin that applies the Open Sea visual theme to the conversation interface.
  - Install: `dsh plugin --profile web add github:d-dev0101/open-sea-skin#v1.2.1`

- [DSH Liang Intensity Skin](https://github.com/kingOfSoySauce/dsh-liang-skin) - **148 stars** | `No standard license`. An optional DSH Web skin that adds an adaptive reasoning-intensity slider and themed model-selection visuals.
  - Install: `dsh plugin --profile web add github:kingOfSoySauce/dsh-liang-skin#v0.1.4`

- [DSH Dream Skin](https://github.com/RevolutionLA/dsh-dream-skin) - **125 stars** | `MIT`. A Web UI skin pack with animated themes, wallpapers, accents, import/export, and persistent per-user appearance settings.
  - Install: `dsh plugin --profile web add dsh-dream-skin`

- [Deep Whale Day/Night Theme](https://github.com/GGBond2424648901/deep-whale-day-night-theme) - **107 stars** | `CC-BY-NC-SA-4.0`. A DeepSeek Harness theme bundle with coordinated Deep Whale day and night interface styles.
  - Install: `dsh plugin --profile web add github:GGBond2424648901/deep-whale-day-night-theme#runtime`

- [DSH Skin Market](https://github.com/kingOfSoySauce/dsh-skin-market) - **105 stars** | `MIT`. A DSH Web marketplace plugin for browsing, installing, updating, disabling, and removing community skins.
  - Install: `dsh plugin --profile web add dsh-skin-market@0.1.36`

- [DSH Custom Skin](https://github.com/SLin-code/dsh-custom-skin) - **97 stars** | `MIT`. A DeepSeek Harness Web bundle that adds configurable wallpapers and translucent interface skins.
  - Install: `pnpm dsh plugin --profile web add github:SLin-code/dsh-custom-skin`

- [BeautiCode](https://github.com/starsstreaming/beautiCode) - **66 stars** | `MIT`. A DeepSeek Harness theme bundle that adds BeautiCode visual styling to the client interface.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add beauticode-dsh`

- [DSH Endfield Theme](https://github.com/ymh0000123/dsh-theme-endfield) - **57 stars** | `MIT`. A DSH Web theme plugin with Endfield-inspired tokens, styles, and configurable appearance settings.
  - Install: `dsh plugin --profile web add github:ymh0000123/dsh-theme-endfield`

- [DSH Endfield UI](https://github.com/rison114514/dsh-endfield-ui) - **48 stars** | `MIT`. An unofficial Endfield-inspired DSH Web theme plugin that uses the standard bundle and client theme extension points.
  - Install: `dsh plugin --profile web add @rison/dsh-endfield-ui@0.7.0`

- [DSH Whale Musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) - **44 stars** | `MIT`. A DSH Web mascot plugin with a whale-girl companion, task reactions, and interactive status animations.
  - Install: `dsh plugin --profile web add github:Sutera-Diffusus/dsh-whale-musume`

- [DeepSeek Pet](https://github.com/keleus/deepseek-pet) - **42 stars** | `MIT`. A DSH Web pet plugin with an animated desktop companion and agent activity reactions.
  - Install: `dsh plugin --profile web add github:keleus/deepseek-pet`

- [DSH Pet Remielle](https://github.com/Gin-7/dsh-pet-remielle) - **34 stars** | `MIT`. A DSH Web pet plugin with animated companions, settings controls, and optional desktop presentation modes.
  - Install: `dsh plugin --profile web add dsh-pet-remielle`

### UI & Interfaces

- [Archify DSH](https://github.com/tt-a1i/archify) - **26.6k stars** | `MIT`. A DSH skill bundle for generating verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams.
  - Install: `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0`

- [DSH Web UI](https://github.com/zhu1090093659/dsh-web) - **6.4k stars** | `Apache-2.0`. A Web UI bundle with a task board, Git graph, remote access, live statistics, pets, skins, and image tools.
  - Install: `dsh plugin --profile web add @linxin666/dsh-web-all@latest`

- [iPolloWork Design Studio](https://github.com/Devin-AXIS/iPolloWork) - **5k stars** | `Custom source-available`. A native DSH Design view for creating and editing visual documents inside the Harness conversation.
  - Install: `dsh plugin --profile web add deepseek-idesign`

- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - **3.1k stars** | `MIT`. A Web UI workbench with file editing, terminal access, Git tools, subagent views, and extension tabs.
  - Install: `dsh plugin --profile web add dsh-better-sidebar`

- [DSH Market](https://github.com/dsh-market/dsh-market) - **2.7k stars** | `MIT`. A visual DSH plugin market for browsing, searching, installing, updating, and switching community plugins and themes.
  - Install: `dsh plugin --profile web add dshmarket`

- [DSH TUI](https://github.com/ccch1mneyyy/dsh-TUI) - **2.7k stars** | `MIT`. A full-screen terminal interface with streaming output, a status line, rollback controls, and context usage indicators.
  - Install: `dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui`

- [Working Activity](https://github.com/ccch1mneyyy/working-activity) - **655 stars** | `MIT`. A live status line that shows model activity, running tools, elapsed time, and turn summaries in DSH.
  - Install: `dsh plugin --profile web add dsh-working-activity`

- [DeepSeek PPT Studio](https://github.com/Devin-AXIS/deepseek-design) - **606 stars** | `Custom source-available`. A native DSH conversation view for creating, editing, templating, and exporting presentation slides.
  - Install: `dsh plugin --profile web add deepseek-ippt`

- [DSH Browser](https://github.com/Lum1104/dsh-browser) - **503 stars** | `MIT`. A Chrome side-panel integration with a DSH bridge for reading pages and operating supported browser content.
  - Install: `curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash`

- [DSH GenUI](https://github.com/omdsh-dev/dsh-genui) - **362 stars** | `MIT`. A DSH rendering plugin for interactive UI components, charts, forms, quizzes, diagrams, and 3D scenes.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-genui.git`

- [DSH Worktable](https://github.com/Aisland-SJL/dsh-worktable) - **328 stars** | `MIT`. A DSH sidebar worktable for organizing projects, agent windows, terminals, browsers, and task status.
  - Install: `dsh plugin --profile web add "https://github.com/Aisland-SJL/dsh-worktable/releases/latest/download/dsh-worktable.tgz"`

- [DSH iOS](https://github.com/ZSeven-W/dsh-ios) - **264 stars** | `MIT`. An iOS companion bundle for DeepSeek Harness with native mobile controls and a Cordis client bridge.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-ios@latest`

- [Pilot Harness Bundles](https://github.com/op7418/pilot-harness) - **261 stars** | `MIT`. A suite of separately installable DSH Web bundles for a CodePilot-style theme, workspace file tree, schedule summary, and session-log export.
  - Install: `dsh plugin --profile web add https://github.com/op7418/pilot-harness/releases/latest/download/deepseek-ai-dsh-ui-worktree-0.1.0-rc.5.tgz`

- [DSH Synapse](https://github.com/liangmianya/dsh-synapse) - **247 stars** | `MIT`. A DeepSeek Harness bundle that adds a visual synapse workspace for navigating related context and tools.
  - Install: `corepack pnpm dsh plugin --profile web add github:liangmianya/dsh-synapse`

- [DSH Tianshu TUI](https://github.com/huiliyi37/dsh-tianshu-tui) - **246 stars** | `Apache-2.0`. A terminal interface that adds Tianshu workflows, evidence gates, TDD controls, and optional vision modules.
  - Install: `dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui`

- [DSH Visualize](https://github.com/Nagi-ovo/dsh-visualize) - **225 stars** | `BSD-3-Clause`. An inline visualization plugin that renders interactive HTML fragments as sandboxed cards in DSH conversations.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-visualize`

- [DSH Oil Creator](https://github.com/oil-oil/dsh-oil-creator) - **160 stars** | `MIT`. A DeepSeek Harness creative bundle for generating and organizing Oil-style visual content.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-oil-creator`

- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) - **154 stars** | `MIT`. An OpenPencil plugin that lets DSH agents preview, inspect, and edit real multi-frame design documents.
  - Install: `pnpm dlx --package=@deepseek-ai/dsh@0.1.0-rc.6 dsh plugin --profile web add @zseven-w/dsh-openpencil@latest`

- [DSH Damage Pulse](https://github.com/wssfk12138/dsh-damage-pulse) - **140 stars** | `MIT`. A DSH Web plugin that tracks token usage, account balance, session costs, and peak/off-peak pricing with a whale companion.
  - Install: `dsh plugin --profile web add github:wssfk12138/dsh-damage-pulse`

- [DSH Popout Sidebar](https://github.com/e2mcc/dsh-popout-sidebar) - **137 stars** | `MIT`. A DeepSeek Harness bundle that opens the sidebar as a separate popout panel.
  - Install: `dsh plugin --profile web add github:e2mcc/dsh-popout-sidebar`

- [GAL View](https://github.com/Ayase34/gal-view) - **132 stars** | `MIT`. A DSH Web conversation view with a Galgame-style layout and an editor for scene elements.
  - Install: `dsh plugin --profile web add github:Ayase34/gal-view#main`

- [DSH Android](https://github.com/ZSeven-W/dsh-android) - **123 stars** | `MIT`. A DeepSeek Harness bundle for controlling Android emulators or USB devices with ADB, live streaming, UI actions, builds, logs, and OCR.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-android@latest`

- [DSH Reasoning Effort](https://github.com/HanaAyane/dsh-reasoning-effort) - **118 stars** | `MIT`. Model and reasoning-effort controls for DSH with a slider, model-advertised levels, and themed selector views.
  - Install: `dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main`

- [DSH Skill & MCP Panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) - **108 stars** | `MIT`. A Web settings panel for managing DSH Skills and MCP servers through profile configuration.
  - Install: `dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.1/dsh-skill-mcp-panel-2.0.1.tgz`

- [DeepSeek Harness GenUI](https://github.com/pengyue-polaron/deepseek-harness-genui) - **107 stars** | `MIT`. A DSH bundle that lets agents create focused React interfaces for complex tasks and carry user selections into later turns.
  - Install: `dsh plugin --profile web add dsh-plugin-genui`

- [DSH Web UI Market](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - **103 stars** | `MIT`. A Web UI marketplace for browsing the curated DSH catalog and installing or removing plugins from a profile.
  - Install: `dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin`

- [SeekTTY](https://github.com/Hilbert-beinghappy/seektty) - **99 stars** | `MIT`. A keyboard-first terminal workspace for DeepSeek Harness with session controls, a plugin center, themes, and workflow commands.
  - Install: `dsh plugin --profile tui add https://github.com/Hilbert-beinghappy/seektty/releases/download/v1.2.0/seektty-1.2.0.tgz`

- [Tabbit Browser](https://github.com/Tabbit-Browser/dsh-tabbit) - **96 stars** | `MIT`. A DSH bundle that exposes Tabbit Browser skills and host tools through the Web profile.
  - Install: `dsh plugin --profile web add github:Tabbit-Browser/dsh-tabbit`

- [DSH GitHub](https://github.com/PivotStackIntelligence/dsh-github) - **93 stars** | `MIT`. Adds a VS Code-style Git and GitHub repository panel to DeepSeek Harness.
  - Install: `pnpm install && dsh plugin --profile web add .`

- [DSH Market Sidebar](https://github.com/2BingLing/dsh-market) - **88 stars** | `MIT`. A DeepSeek Harness sidebar market for discovering, searching, and installing community plugins.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @dsh-market/plugin`

- [ZAT DSH Engine](https://github.com/mishibeikejie/zat-dsh-engine) - **79 stars** | `MIT`. A Web UI marketplace for searching, installing, updating, and rolling back community DSH plugins.
  - Install: `dsh plugin --profile web add github:mishibeikejie/zat-dsh-engine`

- [DSH Notification](https://github.com/omdsh-dev/dsh-notification) - **76 stars** | `MIT`. Browser desktop notifications for completed DSH turns with outcome toggles and keyword include or exclude rules.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.2.tar.gz`

- [DSH Plugin Hub](https://github.com/dshplugin/dsh-plugin-hub) - **75 stars** | `MIT`. A DeepSeek Harness Web marketplace for browsing, searching, and installing curated community plugins.
  - Install: `dsh plugin --profile web add dsh-plugin`

- [DSH Plugin Console](https://github.com/Noob-stupid/dsh-plugin-hub) - **73 stars** | `MIT`. A DSH settings panel for enabling, disabling, inspecting, and installing community plugins from multiple sources.
  - Install: `dsh plugin --profile web add github:Noob-stupid/dsh-plugin-hub`

- [DSH Usage Dock](https://github.com/Aisland-SJL/dsh-usage) - **73 stars** | `MIT`. A DeepSeek Harness Web bundle with a persistent usage dock, balance panel, activity heatmap, and local channel comparison.
  - Install: `dsh plugin --profile web add github:Aisland-SJL/dsh-usage`

- [DSH Stock Watch](https://github.com/Awu12277/dsh-stock-watch) - **68 stars** | `MIT`. A Web UI stock monitor with watchlists, groups, intraday and candlestick charts, target prices, and a draggable panel.
  - Install: `dsh plugin --profile web add dsh-stock-watch`

- [DSH Plugin Store](https://github.com/ZASENJC/dsh-plugins-store) - **67 stars** | `MIT`. A Web plugin that lets users browse, validate, install, update, and remove community DSH plugins after confirmation.
  - Install: `dsh plugin --profile web add npm:dsh-plugins-store`

- [DSH Strata](https://github.com/jsdvjx/dsh-strata) - **67 stars** | `MIT`. A DeepSeek Harness Web plugin that maps conversations onto a persistent spatial navigation rail.
  - Install: `dsh plugin --profile web add dsh-strata`

- [DSH Web Mobile](https://github.com/mexiaosqwq/dsh-web-mobile) - **67 stars** | `MIT`. A responsive Web UI plugin that adapts the DSH interface for narrow and portrait-oriented screens.
  - Install: `dsh plugin --profile web add github:mexiaosqwq/dsh-web-mobile`

- [DSH Web Plugin Manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - **67 stars** | `MIT`. A DSH Web plugin manager with install guards, health checks, rollback, environment controls, and marketplace browsing.
  - Install: `dsh plugin --profile web add dsh-web-plugin-manager@latest`

- [Jacky Creator](https://github.com/Jackywxsz/DSH-Creator) - **65 stars** | `MIT`. Adds a content and operations workspace to DSH for drafting, planning, and idea management.
  - Install: `dsh plugin --profile web add jacky-creator`

- [OpenMA DSH TUI](https://github.com/openma-ai/Martty) - **65 stars** | `MIT`. A terminal-native DSH profile with an ACP plugin tree, streamed sessions, themes, overlays, and native TUI rendering.
  - Install: `dsh plugin --profile tui add @openma/deepseek-harness-tui@latest`

- [DSH Talk Map](https://github.com/Tasihi89/dsh-talk-map) - **64 stars** | `MIT`. A DeepSeek Harness Web plugin that lays out sessions on a movable conversation map with digest and fork actions.
  - Install: `dsh plugin --profile web add github:Tasihi89/dsh-talk-map`

- [DSH Smooth Stream](https://github.com/Laplace-bit/dsh-smooth-stream) - **60 stars** | `MIT`. A DSH Web rendering plugin for smoother streaming output and scrolling across Markdown, code, tables, and tool results.
  - Install: `dsh plugin --profile web add dsh-smooth-stream`

- [DSH Maze](https://github.com/lamost423/dsh-maze) - **57 stars** | `MIT`. A DSH Web plugin for viewing agent execution timelines, data tracks, deterministic analysis, and multi-session comparisons.
  - Install: `dsh plugin --profile web add dsh-maze`

- [DSH Status Rotator](https://github.com/01Virex/dsh-status-rotator) - **57 stars** | `MIT`. A DeepSeek Harness bundle that rotates status messages while a task is running.
  - Install: `dsh plugin --profile web add dsh-status-rotator`

- [DSH Thin Plugin Console](https://github.com/vlln/plugin-registry) - **57 stars** | `MIT`. A Web settings panel for installing, inspecting, updating, enabling, and disabling profile plugins without manual patch editing.
  - Install: `dsh plugin --profile web add @vlln/plugin-console@0.1.0`

- [DSH Session Manager](https://github.com/dream12347/dsh-session-manager) - **54 stars** | `MIT`. A DSH Web session manager for archived sessions, trash recovery, activity statistics, forking, workspace grouping, and context settings.
  - Install: `dsh plugin --profile web add github:dream12347/dsh-session-manager#v0.2.2`

- [DSH Auto Collapse](https://github.com/a179-sanae/dsh-auto-collapse) - **52 stars** | `MIT`. A DSH Web client plugin that folds tool cards and reasoning blocks into compact summaries.
  - Install: `dsh plugin --profile web add dsh-auto-collapse`

- [DSH MCP Panel](https://github.com/PerryLink/dsh-mcp-panel) - **52 stars** | `Apache-2.0`. A DeepSeek Harness settings bundle for adding, editing, testing, and monitoring MCP servers.
  - Install: `dsh plugin --profile web add dsh-mcp-panel`

- [Context Editor DSH](https://github.com/jermaine123123/agent-context-editor) - **46 stars** | `MIT`. Adds search, filtering, editing, hiding, restoring, and undo controls for plain-text DSH messages.
  - Install: `dsh plugin --profile <profile> add ./context-editor-deepseek-harness-0.3.0.tgz`

- [DSH Codex UI](https://github.com/MichengAI/dsh-codex-ui) - **42 stars** | `Apache-2.0`. A Codex-style DSH Web sidebar plugin with workspace navigation, search, conversation controls, and turn navigation.
  - Install: `dsh plugin --profile web add @michengai/dsh-codex-ui@latest --registry=https://registry.npmjs.org/`

- [DSH Status Label](https://github.com/alingalingling/ui-status-label) - **42 stars** | `MIT`. Configurable running-turn status text for DSH Web, with a settings row and conversation-status provider.
  - Install: `dsh plugin --profile web add dsh-ui-status-label`

- [DSH Emoji](https://github.com/hellodigua/dsh-emoji) - **41 stars** | `MIT`. A DSH Web plugin that renders semantic inline emoji and supports switchable custom emoji packs.
  - Install: `dsh plugin --profile web add dsh-emoji`

- [DSH Raw HTML](https://github.com/plolpl789/dsh-raw-html) - **40 stars** | `MIT`. A DeepSeek Harness Web plugin for rendering controlled HTML, SVG, charts, formulas, and interactive VCP cards.
  - Install: `node <absolute-path-to-dsh-raw-html>/patch/install-all.cjs && dsh plugin --profile web add <absolute-path-to-dsh-raw-html>`

- [DSH Gov Portal](https://github.com/ExElectron/dsh-gov-portal) - **38 stars** | `MIT`. A DeepSeek Harness Web UI bundle that provides a government-style portal for sessions, models, permissions, and usage views.
  - Install: `dsh plugin --profile web add link:<absolute-path-to-dsh-gov-portal>`

- [DSH Archive Manager](https://github.com/MichengAI/dsh-archive-manager) - **35 stars** | `Apache-2.0`. A DSH Web plugin for browsing, restoring, and managing archived sessions with sidebar controls.
  - Install: `dsh plugin --profile web add @michengai/dsh-archive-manager@latest --registry=https://registry.npmjs.org/`

- [DSH Share](https://github.com/hellodigua/dsh-share) - **35 stars** | `MIT`. A DSH plugin for sharing selected conversations and groups as images or Markdown.
  - Install: `dsh plugin --profile web add dsh-share`

- [DSH Sidebar QA](https://github.com/ChenRuoT/dsh-sidebar-qa) - **35 stars** | `MIT`. A DSH Web sidebar plugin for selecting conversation text and opening nested follow-up sessions in a dedicated panel.
  - Install: `dsh plugin --profile web add dsh-sidebar-qa`

- [Meow Smooth](https://github.com/Phant0Meow/dsh-meow-smooth) - **34 stars** | `MIT`. A DSH notification and mobile UI bundle with smooth streaming views and configurable message presentation.
  - Install: `dsh plugin --profile web add github:Phant0Meow/dsh-meow-smooth`

- [DSH Office Preview](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) - **33 stars** | `AGPL-3.0`. An optional DSH Web bundle that adds DOCX, XLSX, and PPTX previews to DSH Better Sidebar.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-better-sidebar-plugin-office`

- [OpenMAIC DSH](https://github.com/THU-MAIC/dsh-openmaic) - **33 stars** | `MIT`. A DeepSeek Harness plugin that lets agents generate and render OpenMAIC-style interactive widgets in sandboxed cards.
  - Install: `dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git`

- [DSH Sticky Note](https://github.com/Meredith2328/dsh-sticky-note) - **32 stars** | `MIT`. A DSH Web sidebar note panel for saving ideas, reminders, and TODO items to the local archive.
  - Install: `dsh plugin --profile web add dsh-sticky-note`

- [DSH-Code](https://github.com/UNLINEARITY/dsh-code) - **32 stars** | `MIT`. A terminal coding interface that runs as an out-of-tree DeepSeek Harness bundle with the official agent and tool ecosystem.
  - Install: `dsh plugin --profile cli add dsh-code@1.0.2`

- [DSH File Review](https://github.com/left0ver/dsh-file-review) - **31 stars** | `MIT`. A DeepSeek Harness Web plugin that reviews files changed during an agent turn and presents the findings in the conversation.
  - Install: `dsh plugin --profile web add dsh-file-review`

- [DSH TUI Front End](https://github.com/dsh-tui/dsh-tui) - **31 stars** | `MIT`. A terminal front end for DeepSeek Harness agents with streaming Markdown, tool-call cards, approvals, and session controls.
  - Install: `dsh plugin --profile tui add @dsh-tui/dsh-tui`

- [DSH Timeline](https://github.com/houyanchao/dsh-timeline) - **30 stars** | `GPL-3.0-or-later`. A DSH Web session timeline with navigation, bookmarks, exports, prompt storage, and quick notes.
  - Install: `dsh plugin --profile web add dsh-timeline`

### Vision

- [Modlens](https://github.com/liustack/modlens) - **3.7k stars** | `MIT`. A vision plugin that returns structured OCR, layout, and semantic evidence to text-only DSH models.
  - Install: `dsh plugin --profile web add @liustack/modlens@3.16.6`

- [DSH Vision Router](https://github.com/ysr666/dsh-vision-router) - **1k stars** | `MIT`. A vision routing plugin with image questions, grounding, crops, pixel comparison, OCR, and screenshot tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router`

- [DSH Vision Toolkit](https://github.com/Anionex/dsh-vision-toolkit) - **837 stars** | `MIT`. A native vision bundle for image questions, long-screenshot OCR, UI reconstruction, grounding, and pixel comparison.
  - Install: `dsh plugin --profile web add @anionex/dsh-vision-toolkit`

- [DSH Image Gen](https://github.com/shanliuling/dsh-image-gen) - **269 stars** | `MIT`. A Web plugin that adds image-generation tools and settings to DeepSeek Harness conversations.
  - Install: `dsh plugin --profile web add dsh-image-gen`

- [DSH Vision](https://github.com/oil-oil/dsh-vision) - **88 stars** | `MIT`. Vision tools for DSH that preserve native image input and bridge text-only models to an external vision model.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision`

- [DSH ImageGen](https://github.com/dickpy/dsh-imagegen) - **42 stars** | `Apache-2.0`. A DeepSeek Harness image workspace with provider settings, in-chat generation, editing, templates, and an asset gallery.
  - Install: `dsh plugin --profile web add @dickpy/dsh-imagegen`

- [PictureReader](https://github.com/jing-hy/picturereader) - **35 stars** | `MIT`. A DeepSeek Harness vision bundle for reading and describing information from images.
  - Install: `dsh plugin --profile web add picturereader`

- [DSH ComfyUI](https://github.com/fandc520/dsh-comfyui) - **30 stars** | `MIT`. A DSH plugin for driving ComfyUI to generate and process images and videos with workflow and asset panels.
  - Install: `dsh plugin --profile web add dsh-comfyui`

### Workflow & Automation

- [Reactive Resume DSH Plugin](https://github.com/amruthpillai/reactive-resume) - **41.9k stars** | `MIT`. A DeepSeek Harness bundle that connects Reactive Resume to a session for reading, creating, and editing resumes and job applications.
  - Install: `dsh plugin --profile web add dsh-plugin-reactive-resume`

- [Ouroboros](https://github.com/Q00/ouroboros) - **5.7k stars** | `MIT`. A DeepSeek Harness bundle that exposes the Ouroboros spec-first development workflow as native tools and chat commands.
  - Install: `dsh plugin --profile web add "github:Q00/ouroboros#main&path:integrations/dsh-plugin"`

- [LoopX DSH](https://github.com/huangruiteng/loopx) - **5.3k stars** | `Apache-2.0`. A DSH plugin for bootstrapping LoopX, running governed same-session workflows, and displaying a local GoalBar.
  - Install: `dsh plugin --profile web add dsh-loopx-plugin`

- [Codex Taskboard DSH Integration](https://github.com/chuspeeism/dashi-taskboard) - **2.7k stars** | `Apache-2.0`. A DeepSeek Harness bundle that adds a Taskboard sidebar entry and opens the installed Codex Taskboard runtime.
  - Install: `dsh plugin --profile web add /absolute/path/to/codex-taskboard/integrations/deepseek-harness`

- [DSH Agent Teams](https://github.com/NanmiCoder/dsh-agent-teams) - **1.2k stars** | `MIT`. A team orchestration plugin that adds tools for creating agent groups, assigning work, and tracking shared state.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-agent-teams`

- [Chorus DSH](https://github.com/Chorus-AIDLC/Chorus) - **1.1k stars** | `AGPL-3.0`. A native DeepSeek Harness bundle for Chorus lifecycle automation, prompt behavior, MCP access, and AI-DLC skills.
  - Install: `dsh plugin --profile web add @chorus-aidlc/chorus-dsh -w`

- [Aegis](https://github.com/GanyuanRan/Aegis) - **1.1k stars** | `MIT`. A DeepSeek Harness bundle for the Aegis agent's guarded filesystem and skill workflows.
  - Install: `dsh plugin --profile web add github:GanyuanRan/Aegis`

- [AgentRQ DSH Plugin](https://github.com/agentrq/agentrq) - **1.1k stars** | `Apache-2.0`. A DeepSeek Harness plugin that connects AgentRQ task workspaces to supervised sessions and MCP-backed task tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @agentrq/dsh-plugin-agentrq`

- [CloudBase DSH](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) - **1.1k stars** | `MIT`. A DSH plugin for building full-stack applications with CloudBase database, storage, authentication, and deployment tools.
  - Install: `dsh plugin --profile web add @cloudbase/dsh-plugin`

- [TongFlow DSH Plugin](https://github.com/tong-io/tongflow) - **963 stars** | `AGPL-3.0-only`. A multimodal workflow studio for generating and reviewing image, audio, video, and 3D assets from saved workflows inside DSH.
  - Install: `dsh plugin --profile web add dsh-tongflow`

- [DSH IM](https://github.com/xmanrui/dsh-im) - **949 stars** | `MIT`. A single DSH settings plugin for connecting Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord, and WhatsApp bots.
  - Install: `dsh plugin --profile web add @xmanrui/dsh-im`

- [Infinite Gen 3 DSH](https://github.com/Minglink/dsh-infinite-gen-3) - **801 stars** | `MIT`. A DSH prompt preset with an activation status bar and profile migration scripts for the Infinite Gen 3 workflow.
  - Install: `bash install.sh`

- [Treg DSH](https://github.com/superdesigndev/treg) - **682 stars** | `Apache-2.0 + additional terms`. A DSH bundle that exposes the Treg tool registry as an optional MCP connector and packaged Skill.
  - Install: `dsh plugin --profile web add github:superdesigndev/treg`

- [AgentSight DSH](https://github.com/alibaba/anolisa) - **614 stars** | `Apache-2.0`. A DeepSeek Harness observability plugin that records and presents agent activity for inspection.
  - Install: `cd src/agentsight/dsh-plugin && pnpm install && pnpm run build && dsh plugin --profile web add .`

- [Infinite Gen 2 DSH](https://github.com/Minglink/dsh-infinite-gen-2) - **586 stars** | `MIT`. A DSH plugin that adds the Infinite Gen 2 prompt preset and an on-screen activation status bar.
  - Install: `./install.sh`

- [AI Novel Writer DSH](https://github.com/EthanYoQ/AI-Novel-Writer) - **502 stars** | `MIT`. A DeepSeek Harness bundle for planning, drafting, and revising long-form fiction inside a novel project.
  - Install: `dsh plugin --profile web add @ethanyoq/dsh-ai-novel-writer`

- [DeepSec DSH Security Suite](https://github.com/Unclecheng-li/DeepSec) - **354 stars** | `MIT`. A pair of DSH security bundles for defensive code audits and authorized penetration-testing workflows.
  - Install: `dsh plugin --profile web add ./dsh-plugins/deepsec-shield && dsh plugin --profile web add ./dsh-plugins/deepsec-spear`

- [Harmony Next DSH](https://github.com/linhay/harmony-next.skills) - **342 stars** | `MIT`. A DSH plugin that provides HarmonyOS NEXT development skills and offline reference materials.
  - Install: `dsh plugin --profile demo add github:linhay/harmony-next.skills`

- [AnySearch DSH](https://github.com/anysearch-team/anysearch-dsh) - **324 stars** | `MIT`. Web search for DSH with source discovery, vertical search, bounded batch queries, and cleaned page content.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @anysearch/anysearch-dsh`

- [DSH Pentest](https://github.com/howmp/dsh-pentest) - **311 stars** | `MIT`. A DSH security workflow plugin that records penetration-test targets, clues, proposals, decisions, and reports in the Web UI.
  - Install: `dsh plugin --profile web add https://github.com/howmp/dsh-pentest/releases/latest/download/dsh-pentest.tar.gz`

- [EasyEDA Agent DSH](https://github.com/zhoushoujianwork/easyeda-agent) - **311 stars** | `MIT`. A DeepSeek Harness bundle that adds EasyEDA Pro schematic and PCB automation through typed tools and an agent skill.
  - Install: `dsh plugin --profile web add "github:zhoushoujianwork/easyeda-agent#<tag>"`

- [ModSearch](https://github.com/liustack/modsearch) - **309 stars** | `MIT`. A DSH web-search plugin that adds search, X search, and focused page reading through the ModSearch engine chain.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest`

- [DSH Plugin Subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - **292 stars** | `MIT`. An OAuth-based provider plugin that connects ChatGPT, Claude, and Grok subscriptions to DSH without separate API keys.
  - Install: `dsh plugin --profile web add dsh-plugin-subscriptions`

- [DSH Cost Meter](https://github.com/Han-1413141/dsh-cost-meter) - **216 stars** | `MIT`. Session cost tracking for DSH with daily totals, history, budget views, and synchronized model pricing.
  - Install: `dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.3.1`

- [Oh Story DSH](https://github.com/zenstory-ai/oh-story-dsh) - **211 stars** | `MIT`. A DSH plugin for fiction and short-drama production with writing skills, specialist roles, workspace routing, and previews.
  - Install: `dsh plugin --profile web add @oh-story/dsh@0.1.4`

- [DSH Agent RP](https://github.com/hewzhew/dsh-agent-rp) - **197 stars** | `MIT`. A DeepSeek Harness roleplay bundle with SillyTavern migration, agent personas, and conversation workflow tools.
  - Install: `npx -p @deepseek-ai/dsh@latest dsh plugin --profile web add github:hewzhew/dsh-agent-rp#main`

- [DSH Taskboard](https://github.com/shengsheng90/DSH-taskboard) - **187 stars** | `Apache-2.0`. A DeepSeek Harness taskboard bundle for organizing tasks and monitoring workflow progress.
  - Install: `dsh plugin --profile web add -w /absolute/path/to/shengsheng-dsh-taskboard-<version>.tgz`

- [TokenLedger](https://github.com/zh667/TokenLedger) - **184 stars** | `MIT`. A DeepSeek Harness bundle for tracking token usage and recording session cost data.
  - Install: `dsh plugin --profile web add "github:zh667/TokenLedger"`

- [DSH Data Agent](https://github.com/omdsh-dev/dsh-data-agent) - **181 stars** | `MIT`. Database connections, masked forms, SQL tools, and a shared data-analysis preset for DSH Web and TUI.
  - Install: `dsh plugin --profile web add @yejiming/dsh-data-agent`

- [pi2dsh](https://github.com/weijiafu14/pi2dsh) - **171 stars** | `MIT`. A DeepSeek Harness bundle that brings the pi coding agent's workflow and tools into DSH.
  - Install: `dsh plugin --profile web add pi2dsh`

- [Anime Find](https://github.com/cocofhu/anime-find) - **163 stars** | `MIT`. A DSH Web search plugin that gathers anime results into cards with metadata, resource links, and optional streaming views.
  - Install: `dsh plugin --profile web add github:cocofhu/anime-find`

- [DSH Evolve Modes](https://github.com/GraySilver/dsh-evolve-modes) - **157 stars** | `MIT`. A DSH Web plugin for composing agent modes, quality gates, and self-evolution rules from the conversation input area.
  - Install: `dsh plugin --profile web add https://github.com/GraySilver/dsh-evolve-modes/releases/download/v0.3.1/graysilver-dsh-evolve-modes-0.3.1.tgz`

- [DSH Plugin Bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - **157 stars** | `MIT`. A session migration plugin that previews a bounded handoff to another preset while leaving the original session unchanged.
  - Install: `dsh plugin --profile web add dsh-plugin-bridge`

- [DSH Remote Web Gateway](https://github.com/summer1238/dsh-remote-web-gateway) - **155 stars** | `MIT`. A DSH Web plugin for phone and tablet access with QR pairing, per-device authorization, revocation, and a Cloudflare Quick Tunnel.
  - Install: `dsh plugin --profile web add dsh-remote-web-gateway`

- [DSH Agent Team GUI](https://github.com/toolclub/dsh-agent-team-gui) - **153 stars** | `MIT`. Persistent multi-model teams for DSH with durable orchestration, DAG workflows, run history, and provider-reported usage.
  - Install: `dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v0.5.0`

- [DSH Super Injector](https://github.com/yjh051108/dsh-super-injector) - **152 stars** | `BSD-3-Clause`. A DSH development plugin for injecting, hot-reloading, and removing local plugin packages without a restart.
  - Install: `dsh plugin --profile web add github:yjh051108/dsh-super-injector`

- [DSH Auto Mode](https://github.com/NanmiCoder/dsh-auto-mode) - **133 stars** | `MIT`. A fail-closed permission policy plugin that classifies DSH tool calls before automatic execution.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-auto-mode`

- [DSH Usage Stats](https://github.com/Ychris12138/dsh-usage-stats) - **129 stars** | `MIT`. A DSH Web dashboard for token usage, provider balances, subscription quotas, and historical activity.
  - Install: `dsh plugin --profile web add github:Ychris12138/dsh-usage-stats`

- [Market Research Dashboard DSH](https://github.com/theBigGavin/marketingdashboard) - **129 stars** | `MIT`. A DeepSeek Harness bundle that exposes market quotes, sector rankings, futures, news, and money-flow tools through a remote MCP endpoint.
  - Install: `dsh plugin --profile web add github:theBigGavin/marketingdashboard`

- [DSH Agent Workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) - **124 stars** | `MIT`. A Web UI plugin that presents model requests, responses, and tool calls as a navigable workflow for each DSH conversation.
  - Install: `dsh plugin --profile web add github:xuanyuanzhifeng/dsh-plugin-agent-workflow#v0.1.0 --workspace-root`

- [DSH Crew](https://github.com/ZSeven-W/dsh-crew) - **118 stars** | `MIT`. A DSH hub for dispatching work to native subagents, tracking progress, and bridging Claude Code or Codex workers.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-crew@latest`

- [DSH CommandCode Provider](https://github.com/Mars-Sea/dsh-commandcode-provider) - **116 stars** | `MIT`. An LLM provider plugin that adds a live Command Code model catalog, reasoning controls, and a Models-page card to DSH.
  - Install: `dsh plugin --profile web add @mars-sea/dsh-commandcode-provider`

- [DSH Auto Review](https://github.com/PerryLink/dsh-auto-review) - **115 stars** | `Apache-2.0`. A read-only reviewer subagent that returns structured allow or deny verdicts for DSH approval requests and fails closed by default.
  - Install: `dsh plugin --profile web add dsh-auto-review`

- [Argo DSH](https://github.com/taxueseek/argo) - **113 stars** | `MIT`. A DSH profile bundle that mounts Argo search MCP tools and an evidence-oriented research workflow.
  - Install: `dsh plugin --profile web add "github:taxueseek/argo#main&path:packages/dsh-plugin"`

- [Volcengine Ark DSH Plugins](https://github.com/volcengine/ark-cli) - **112 stars** | `Apache-2.0`. A pair of DeepSeek Harness bundles for Volcengine Ark model routes and cloud Managed Agents.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @volcengine/ark-plan-api && npx -y @deepseek-ai/dsh plugin --profile web add @volcengine/ark-managed-agents`

- [DSH Workflow](https://github.com/omdsh-dev/dsh_workflow) - **109 stars** | `MIT`. A reusable DSH workflow layer for multi-agent runs with saved plans, approvals, background jobs, and resumable execution.
  - Install: `dsh plugin --profile web add github:dsh-external/dsh_workflow#main`

- [Superpowers DSH](https://github.com/LayneChai/superpowers-dsh) - **106 stars** | `MIT`. A DeepSeek Harness bundle that packages the Superpowers development workflow as native DSH skills.
  - Install: `dsh plugin --profile web add github:LayneChai/superpowers-dsh`

- [DSH Plugin Finder](https://github.com/awesome-dsh-plugin/dsh-find-plugin) - **103 stars** | `MIT`. Searches GitHub's DSH plugin ecosystem from inside a session and returns ranked results with ready-to-run install commands.
  - Install: `dsh plugin --profile web add dsh-find-plugin`

- [Odai DSH Plugin](https://github.com/orziz/odai) - **103 stars** | `MIT`. A profile-wide DSH governance and routing bundle with an embedded Odai skill and runtime.
  - Install: `dsh plugin --profile web add odai-dsh-plugin`

- [DSH Redteam Model](https://github.com/SeaOf0/dsh-redteam-model) - **102 stars** | `MIT`. A DSH security-research suite with authorized red-team modes, campaign memory, asset hunting, and managed runtime plugins.
  - Install: `dsh plugin --profile web add github:SeaOf0/dsh-redteam-model`

- [DSH Auth In One](https://github.com/Stormycry-cryp/dsh-AuthInOne) - **101 stars** | `MIT`. A DeepSeek Harness authentication bundle that manages common sign-in and profile setup flows.
  - Install: `dsh plugin --profile web add github:Stormycry-cryp/dsh-AuthInOne#v0.2.0-alpha.4`

- [DSH Reverse Skill](https://github.com/dhicoc/dsh-reverse-skill) - **89 stars** | `MIT`. A DeepSeek Harness bundle for reverse-engineering software behavior into reusable development skills.
  - Install: `dsh plugin --profile web add github:dhicoc/dsh-reverse-skill`

- [DSH Automation](https://github.com/titanwings/dsh-automation) - **83 stars** | `MIT`. Scheduled coding runs for DSH with Web and agent controls, durable history, and guarded execution boundaries.
  - Install: `dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.6`

- [DSH QQ Bot](https://github.com/tencent-connect/dsh-qqbot) - **81 stars** | `MIT`. A QQ Bot channel for DSH that handles messaging, QR-code login, session events, and agent replies.
  - Install: `npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot`

- [DSH Bridge](https://github.com/wenbin-wb/dsh-bridge) - **80 stars** | `MIT`. A DSH remote-access bridge for QR connections, tunnels, mobile clients, and chat-bot channels.
  - Install: `dsh plugin --profile web add @wenbin_wb/dsh-bridge@2.6.1`

- [DSH Notifier](https://github.com/THEWOLFWALKER/dsh-notifier) - **80 stars** | `MIT`. A notification and remote-approval layer for DSH with one notify API, multiple channel adapters, and optional mobile controls.
  - Install: `dsh plugin add dsh-notifier --profile web`

- [Dockyard DSH](https://github.com/AITabby/dockyard-dsh) - **79 stars** | `MIT`. A native DSH provider plugin with account pools, OAuth sign-in, model catalogs, quota status, and provider-specific requests.
  - Install: `dsh plugin --profile web add github:AITabby/dockyard-dsh`

- [Russian Marketplace DSH](https://github.com/Vladimir-Human/ru-marketplace-mcp) - **77 stars** | `MIT`. A DeepSeek Harness bundle that exposes Russian software marketplaces through searchable MCP tools and local skill retrieval.
  - Install: `dsh plugin --profile web add github:Vladimir-Human/ru-marketplace-mcp#path:/dsh`

- [ForkProbe DSH](https://github.com/Jayden-X-L/forkprobe) - **71 stars** | `MIT`. A native DSH plugin for comparing Skills on the same task and choosing a winner from a local report.
  - Install: `dsh plugin --profile web add "github:Jayden-X-L/forkprobe"`

- [Capability Menu DSH](https://github.com/PKUfudawei/dsh-capability-menu) - **70 stars** | `Apache-2.0`. A DeepSeek Harness bundle that catalogs tools and skills and controls their resident, on-demand, or blocked exposure.
  - Install: `dsh plugin --profile web add @daweifu/capability-menu`

- [DSH Preset Plus](https://github.com/Rain-kl/dsh-preset-plus) - **70 stars** | `MIT`. Adds a scoped preset mode that injects configurable preset context into DSH requests.
  - Install: `dsh plugin --profile web add @rain-kl/dsh-preset-plus`

- [Rapid MLX DSH Provider](https://github.com/raullenchai/rapid-mlx-dsh-provider) - **70 stars** | `Apache-2.0`. A DeepSeek Harness provider bundle that connects Rapid-MLX servers and adapts their model context limits for compaction.
  - Install: `dsh plugin --profile web add @raullenchai/dsh-provider`

- [DSH Harness Wallet](https://github.com/feibi-mochi/deepseek-harness-control-center) - **66 stars** | `MIT`. A DSH Web plugin for account balances, usage tracking, completion alerts, recharge actions, and session controls.
  - Install: `dsh plugin --profile web add deepseek-harness-wallet`

- [DSH Toy](https://github.com/c3ll256/dsh-toy) - **63 stars** | `BSD-3-Clause`. Safety-bounded DSH control for Buttplug and Intiface devices with optional MonsterParty toy integration.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy`

- [DSH Codex Connect](https://github.com/franksong2702/dsh-codex-connect) - **61 stars** | `MIT`. A DSH integration for using Codex models and image generation through ChatGPT OAuth.
  - Install: `dsh plugin --profile web add dsh-codex-connect@alpha`

- [Custom First Control Prompt](https://github.com/WM-CODER/custom-first-control-prompt) - **59 stars** | `MIT`. A DSH Web plugin for configuring the initial control prompt through a settings panel and profile patch.
  - Install: `dsh plugin --profile web add @wm-coders/dsh-custom-first-control-prompt`

- [SpecFusion](https://github.com/wxkingstar/SpecFusion) - **58 stars** | `MIT`. A DSH plugin for searching enterprise API documentation and returning interface details while the agent writes code.
  - Install: `dsh plugin --profile web add @wxkingstar/specfusion-dsh`

- [DeepSeek Flow](https://github.com/kanghelyu/dsh-deepseek-flow) - **57 stars** | `MIT`. A Markdown-first workflow editor for DSH with a synchronized canvas, Boolean gates, reviewable changes, and AI-assisted workflow maintenance.
  - Install: `dsh plugin --profile web add "github:kanghelyu/dsh-deepseek-flow#main"`

- [DSH Balance Monitor](https://github.com/yxxbc/dsh-balance-plugin) - **57 stars** | `MIT`. Balance monitoring, usage statistics, and third-party plugin management in the DSH Web interface.
  - Install: `dsh plugin --profile web add github:yxxbc/dsh-balance-plugin`

- [Morning Star DSH](https://github.com/btspoony/mstar-harness) - **56 stars** | `MIT`. In-process DSH workflow gates that validate status, control dispatch, and expose the Morning Star engine through refusal-aware channels.
  - Install: `dsh plugin --profile web add @mstar-harness/dsh`

- [OpenBiliClaw](https://github.com/whiteguo233/dsh-openbiliclaw) - **55 stars** | `BSD-3-Clause`. A DeepSeek Harness bundle for OpenBiliClaw workflows and related content tools.
  - Install: `dsh plugin --profile web add @openbiliclaw/dsh-plugin`

- [AgentDebugX DSH](https://github.com/AgentDebugX/AgentDebugX) - **52 stars** | `MIT`. A DSH plugin for diagnosing live and saved Harness trajectories with AgentDebugX.
  - Install: `dsh plugin --profile web add dsh-agentdebugx`

- [Recruiting Copilot DSH](https://github.com/Viy1204/recruiting-copilot) - **52 stars** | `MIT`. A recruiting workflow bundle with job intake, candidate sourcing, resume review, and a browser panel for DSH.
  - Install: `dsh plugin --profile web add git+https://github.com/Viy1204/recruiting-copilot.git`

- [DSH Remote QR](https://github.com/xgone/dsh-remote) - **51 stars** | `MIT`. A DSH Web remote-access plugin with account login, MFA, browser-side workspace selection, and protected WebSocket access.
  - Install: `dsh plugin --profile web add @xgone/dsh-remote@0.1.1`

- [DSH Secure Audit](https://github.com/PensiveFei/dsh-secure-audit) - **51 stars** | `MIT`. A read-only DSH security and compliance plugin for prompt-injection detection, PII redaction, and local configuration audits.
  - Install: `dsh plugin add dsh-secure-audit`

- [DSH Codex](https://github.com/Yan-Zero/dsh-codex) - **50 stars** | `MIT`. A DSH plugin that brings Codex model access, task controls, and related tools into DeepSeek Harness.
  - Install: `dsh plugin --profile web add dsh-codex`

- [DSH All-in-One Suite](https://github.com/whyihaveyou/dsh-suite) - **49 stars** | `MIT`. An all-in-one DSH plugin suite bundling a store, notifications, session export, team board, presets, and themes.
  - Install: `dsh plugin --profile web add @dsh-suite/all`

- [DSH Lark](https://github.com/omdsh-dev/dsh-lark) - **47 stars** | `BSD-3-Clause`. A Feishu/Lark channel for sending tasks to DSH agents and returning replies, approvals, and cards to chat.
  - Install: `dsh plugin --profile web add dsh-lark-channel@latest`

- [Run2Skill](https://github.com/qkycir-123/dsh-run2skill) - **47 stars** | `MIT`. A DSH Web bundle that turns successful sessions into reusable, reviewable Agent Skills.
  - Install: `dsh plugin --profile web add dsh-run2skill@0.3.1`

- [Lowtide DSH](https://github.com/KelaoHu/dsh-lowtide) - **46 stars** | `MIT`. A DeepSeek Harness plugin that schedules model work around configured prices and availability with semi-automatic or full-automatic runs.
  - Install: `dsh plugin --profile web add https://github.com/KelaoHu/dsh-lowtide/releases/latest/download/dsh-lowtide.tgz`

- [DSH IM Gateway](https://github.com/zhuiyueya/dsh-im-gateway) - **44 stars** | `MIT`. An IM gateway bundle for connecting DSH agents to WeChat, Feishu, Telegram, Discord, and other messaging channels.
  - Install: `dsh plugin --profile web add dsh-im-gateway`

- [DSH Auto Continue](https://github.com/HsiangNianian/dsh-auto-continue) - **42 stars** | `MIT`. A DeepSeek Harness bundle that automatically continues a task after an interaction reaches its limit.
  - Install: `dsh plugin --profile web add dsh-client-auto-continue`

- [DSH Tavern](https://github.com/chen731215-dev/dsh-tavern) - **40 stars** | `CC-BY-NC-SA-4.0`. A DSH roleplay plugin for managing character cards, worldbooks, presets, and story memories.
  - Install: `dsh plugin add dsh-tavern`

- [DSH with ChatGPT](https://github.com/BeforeWave/dsh-with-chatgpt) - **39 stars** | `MIT`. A DSH plugin that connects ChatGPT reasoning to local coding sessions through a guided setup flow.
  - Install: `dsh plugin --profile web add dsh-with-chatgpt`

- [AX Feishu Bridge](https://github.com/AX1202/ax-feishu-bridge) - **38 stars** | `MIT`. A Feishu/Lark bridge that lets users chat with Pi or DeepSeek Harness from the same messaging workspace.
  - Install: `dsh plugin --profile web add ax-feishu-bridge --ignore-scripts`

- [MattSkillsDeck DSH](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - **37 stars** | `MIT`. A DSH bundle that packages Matt Pocock's skills as an agent skill deck with a Web settings panel.
  - Install: `dsh plugin --profile web add dsh-mattpocock-skills-deck`

- [DSH Lark Bot](https://github.com/PlutoKeating/dsh-lark-bot) - **36 stars** | `AGPL-3.0`. A DSH profile bundle that connects DeepSeek Harness to Feishu and Lark with workspaces, parallel tasks, notifications, and guarded recovery.
  - Install: `dsh plugin --profile dsh-lark add dsh-lark-bot`

- [DSH Lark Bridge](https://github.com/bihangchi9-creator/dsh-lark-bridge) - **36 stars** | `MIT`. A DeepSeek Harness bundle that connects Feishu and Lark group chats to isolated agent sessions and project directories.
  - Install: `dsh plugin --profile web add link:/path/to/dsh-lark-bridge`

- [DSH Usage Plugin](https://github.com/feiyang-dev/dsh-usage-plugin) - **36 stars** | `MIT`. A DeepSeek Harness bundle for viewing usage statistics and token consumption during sessions.
  - Install: `dsh plugin --profile web add @feiyang666/dsh-usage-plugin`

- [DSH Lark Link](https://github.com/amlyczz/dsh-lark-link) - **35 stars** | `MIT`. A Feishu/Lark bridge with QR login, multi-agent modes, media exchange, and reusable DSH Web sessions.
  - Install: `dsh plugin --profile web add dsh-lark-link@latest --ignore-scripts`

- [DSH Save Money](https://github.com/zhu168/dsh-save-money) - **35 stars** | `MIT`. A DeepSeek Harness bundle for tracking model usage and helping reduce unnecessary token spending.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-save-money`

- [DSH Interconnect](https://github.com/Chinesezjc/dsh-interconnect) - **34 stars** | `MIT`. Cross-instance DSH messaging and event handoff with host services, model-facing tools, and shared-token authentication.
  - Install: `dsh plugin --profile web add dsh-interconnect`

- [DSH AGY Link](https://github.com/amlyczz/dsh-agy-link) - **33 stars** | `MIT`. A provider bundle that connects DSH to the Google Antigravity agy CLI with streaming output, model selection, and usage settings.
  - Install: `dsh plugin --profile web add dsh-agy-link`

- [DSH Claude Provider](https://github.com/MoFeng2223/dsh-claude-provider) - **33 stars** | `MIT`. A DSH provider plugin for connecting Claude models to DeepSeek Harness.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @mofeng2223/dsh-claude-provider`

- [DSH Model Config](https://github.com/MarvekG/deepseek-harness-model-config) - **33 stars** | `MIT`. A DeepSeek Harness Web bundle for custom model endpoints and per-model reasoning and capacity settings.
  - Install: `dsh plugin --profile web add github:MarvekG/deepseek-harness-model-config`

- [Cloader DSH Taskboard](https://github.com/cloader/dsh-taskboard) - **32 stars** | `Apache-2.0`. A DSH Web taskboard with sidebar navigation, task status tracking, and zero-configuration local storage.
  - Install: `dsh plugin --profile web add dsh-taskboard`

- [DSH Codex Subscription](https://github.com/WSL043/dsh-codex-subscription) - **32 stars** | `MIT`. A DSH bundle for connecting ChatGPT and Codex subscriptions with OAuth, model access, usage, search, and image tools.
  - Install: `dsh plugin --profile web add dsh-codex-subscription`

- [DSH Plugin Guide](https://github.com/PerryLink/dsh-plugin-guide) - **32 stars** | `Apache-2.0`. A DSH bundle with plugin-development documentation, a scaffolder, a static checker, and a pack verifier.
  - Install: `dsh plugin --profile web add dsh-plugin-guide`

- [DSH Science](https://github.com/biociao/dsh-science) - **32 stars** | `MIT`. A research and remote-compute bundle with experiment tracking, SSH/HPC jobs, evidence artifacts, and a Web settings panel.
  - Install: `dsh plugin --profile web add dsh-science`

- [DSH Whale Report](https://github.com/SenmuuuuW/dsh-whale-report) - **31 stars** | `MIT`. A DSH reporting plugin that generates daily, weekly, monthly, yearly, or custom-range reports from session event logs.
  - Install: `dsh plugin --profile web add github:SenmuuuuW/dsh-whale-report`

- [Helmd](https://github.com/ADWMC/helm-d) - **31 stars** | `MIT`. A DeepSeek Harness security-analysis bundle with routing, evidence, and tools for Android, Web, Native, Protocol, Malware, and AI-Security work.
  - Install: `dsh plugin --profile web add https://github.com/ADWMC/helm-d/releases/latest/download/helmd.tgz`

- [DSH Pipeline Kernel](https://github.com/not-big-dog/DSH-pipeline-kernel) - **30 stars** | `MIT`. A DSH workflow bundle with pipeline tools, task routing, scheduled wakeups, and recovery for stalled jobs.
  - Install: `dsh plugin --profile web add .`

- [DSH Toolbox Suite](https://github.com/HiWhaleW/dsh-toolbox) - **30 stars** | `PolyForm Noncommercial 1.0.0`. A suite of DSH bundles for product research, context switching, plugin preflight checks, and compatibility monitoring.
  - Install: `dsh plugin --profile toolbox add ./dist/dsh-toolbox-product-research-workbench-0.2.1.tgz && dsh plugin --profile toolbox add ./dist/dsh-toolbox-context-switchboard-0.2.1.tgz && dsh plugin --profile toolbox add ./dist/dsh-toolbox-plugin-preflight-0.2.1.tgz && dsh plugin --profile toolbox add ./dist/dsh-toolbox-compatibility-radar-0.2.1.tgz`
<!-- END GENERATED CATEGORY LIST -->

## Install plugins carefully

DSH plugins run third-party code with your account permissions. A plugin can read files, access environment variables, start processes, and use the network. Inclusion confirms the repository shape and installation evidence; it is not a security audit. Read the source and install unfamiliar plugins in an isolated workspace without production credentials.

## Related resources

- [DeepSeek Harness documentation](https://deepseek-harness.github.io/deepseek-harness/) - Official installation, configuration, and development guides.
- [Official `dsh-plugin` topic](https://github.com/topics/dsh-plugin) - A discovery feed that still requires code-level verification.
- [ScriptByAI](https://www.scriptbyai.com/) - AI tools, coding agents, and practical technical guides.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) before opening a pull request. Additions must provide code-level DSH evidence and meet the admission threshold.
