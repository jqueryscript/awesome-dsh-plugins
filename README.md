# Awesome DeepSeek Harness Plugins [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A verified, category-organized list of community plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), with exact GitHub Star counts.

**Last verified:** 2026-09-28 | **Minimum at admission:** 30 stars | **Plugins:** 631

**Latest additions:** 2026-10-25. Existing entries retain their previous Star snapshots.

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

Each category below contains the actual plugin entries. Entries within a category are sorted by recorded GitHub Stars.

<!-- BEGIN GENERATED CATEGORY LIST -->
### Files & Runtime

- [OpenDesign DSH Runtime](https://github.com/nexu-io/open-design) - **98.5k stars** | `Apache-2.0`. A DeepSeek Harness profile bundle that connects OpenDesign to a user-installed DSH runtime through a structured stdio protocol.
  - Install: `pnpm --filter @open-design/dsh-runtime build && pnpm -C packages/dsh-runtime pack --pack-destination <temporary-directory> && dsh plugin --profile open-design add <temporary-directory>/open-design-dsh-runtime-0.1.0.tgz`

- [Mirage DSH](https://github.com/strukto-ai/mirage) - **3.7k stars** | `Apache-2.0`. A DSH filesystem and shell provider that mounts remote and local resources inside one virtual workspace.
  - Install: `dsh plugin --profile web add @struktoai/mirage-dsh`

- [DSH Purge](https://github.com/YuJunZhiXue/dsh-purge) - **2.5k stars** | `MIT`. Adds a DSH settings panel for managing prompt rules, permission policies, and tool-limit patches.
  - Install: `dsh plugin --profile web add https://github.com/YuJunZhiXue/dsh-purge/archive/refs/heads/master.zip`

- [API Relay Audit DSH](https://github.com/toby-bridges/api-relay-audit) - **860 stars** | `AGPL-3.0-only`. A DeepSeek Harness bundle for auditing API relays for prompt injection, model substitution, tool-call rewriting, SSE anomalies, and error leakage.
  - Install: `dsh plugin --profile web add "github:toby-bridges/api-relay-audit#v2.4.0"`

- [Our Free Model DSH](https://github.com/zouyuxuan122/dsh-our-free-model) - **713 stars** | `MIT`. Add an upstream model gateway, availability checks, usage charts, and a local forwarding endpoint to DSH.
  - Install: `dsh plugin --profile web add /absolute/path/to/dsh-our-free-model`

- [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) - **675 stars** | `Apache-2.0`. A DSH bundle that connects the managed-agents runtime through the official stdio MCP client.
  - Install: `npm ci && npm run build:runtime && npm link && dsh plugin --profile web add managed-agents`

- [DSH k8e Sandbox](https://github.com/xiaods/k8e) - **498 stars** | `Apache-2.0`. A DeepSeek Harness sandbox bundle that routes filesystem and subprocess services through the k8e sandbox runtime.
  - Install: `dsh plugin --profile <name> add @k8e-sandbox/dsh-k8e-sandbox-bundle`

- [DSH Git Worktree Bundle](https://github.com/vibeinging/dsh-desktop) - **483 stars** | `BSD-3-Clause`. Manage Git worktrees through official DSH Web slots with separate workspaces and sessions for each checkout.
  - Install: `dsh plugin --profile web add -w /absolute/path/to/dsh-desktop/packages/dsh-worktree`

- [AgentGuard DSH](https://github.com/GoPlusSecurity/agentguard) - **463 stars** | `MIT`. A DeepSeek Harness bundle for scanning plugin sources and reporting or enforcing runtime tool-call security policies.
  - Install: `dsh plugin --profile web add @goplus/agentguard`

- [Invoice Downloader DSH](https://github.com/EthanYoQ/Invoice-Downloader) - **462 stars** | `Apache-2.0`. A DSH bundle for local IMAP invoice downloads, OCR, archiving, and Excel summaries from a Web sidebar.
  - Install: `dsh plugin --profile web add @ethanyoq/dsh-invoice-downloader`

- [Univer Office DSH](https://github.com/dream-num/dsh-univer-office) - **429 stars** | `Apache-2.0`. A DSH office bundle for creating and editing spreadsheets, documents, presentations, tables, canvases, and existing office files.
  - Install: `dsh plugin --profile web add dsh-univer-office`

- [DSH DeepSeek Web Login](https://github.com/cv-superding/dsh-deepseek-web-login) - **178 stars** | `Apache-2.0`. Use chat.deepseek.com web models as a DSH language model provider.
  - Install: `dsh plugin --profile desktop add dsh-deepseek-web-login`

- [DSH Undo Savepoint](https://github.com/lire1131/dsh-undo-savepoint) - **166 stars** | `MIT`. Crash recovery for DSH that snapshots configuration and plugin code for undo, redo, rollback, and safe-mode starts.
  - Install: `dsh plugin --profile web add github:lire1131/dsh-undo-savepoint#master`

- [DSH Privacy Router](https://github.com/LYiHub/pub-dsh-privacy-router) - **163 stars** | `MIT`. Route model requests between local and cloud providers through configurable privacy gates.
  - Install: `dsh plugin --profile web add github:LYiHub/pub-dsh-privacy-router`

- [DSH Standard Adapter](https://github.com/Yan-Zero/dsh-std) - **137 stars** | `MIT`. A DeepSeek Harness adapter that discovers standard plugin manifests and activates negotiated server and browser contributions.
  - Install: `dsh plugin --profile web add @dsh-std/adapter-dsh`

- [DSH Config Manager](https://github.com/xiajiajun516/dsh-config-manager) - **134 stars** | `MIT`. A DSH plugin for backing up, restoring, migrating, and syncing DSH settings, plugins, MCP servers, skills, and workspaces.
  - Install: `dsh plugin --profile web add dsh-config-manager@latest`

- [DSH Git Bash Preset](https://github.com/liceses/dsh-gitbash-preset) - **129 stars** | `MIT`. A DeepSeek Harness preset that configures Git Bash support and a ready-to-use terminal environment.
  - Install: `dsh plugin --profile web add @icelily/dsh-gitbash-preset`

- [DSH Permission Rules](https://github.com/PerryLink/dsh-permission-rules) - **115 stars** | `Apache-2.0`. A DeepSeek Harness bundle for declarative tool permissions and process-level network policy with a settings editor.
  - Install: `dsh plugin --profile web add github:PerryLink/dsh-permission-rules#main`

- [DSH Network Settings](https://github.com/kanneiren/dsh-network-settings) - **107 stars** | `MIT`. A DeepSeek Harness Web bundle for configuring network endpoints, proxies, health checks, and connection settings.
  - Install: `dsh plugin --profile web add dsh-network-settings`

- [DSH Remote](https://github.com/flymysql/dsh-remote) - **101 stars** | `MIT`. A DeepSeek Harness bundle for connecting the client to a remote runtime.
  - Install: `dsh plugin --profile web add dsh-remote`

- [DSH Whale Catch](https://github.com/Rosynb666/dsh-whale-catch) - **99 stars** | `MIT`. Collect session output files in a sidebar with previews, change comparisons, ZIP export, and archiving.
  - Install: `dsh plugin --profile web add dsh-whale-catch@0.2.0`

- [DSH Win32](https://github.com/sjh9714/dsh-win32) - **87 stars** | `MIT`. A Windows-focused DSH bundle with PowerShell execution, preset management, and sandbox-aware runtime checks.
  - Install: `dsh plugin --profile web add dsh-win32`

- [Local Shell MCP](https://github.com/fwerkor/local-shell-mcp) - **78 stars** | `MIT`. A DSH bridge for local-shell-mcp that exposes shell, files, browser, and remote-worker tools through per-session connections.
  - Install: `dsh plugin --profile web add 'github:fwerkor/local-shell-mcp#main'`

- [DSH Cline Pass](https://github.com/yhshzh/dsh-cline-pass) - **75 stars** | `MIT`. Register Cline Pass subscription models through the DSH model-provider interface.
  - Install: `dsh plugin --profile web add dsh-cline-pass`

- [Multica DSH Runtime](https://github.com/multica-ai/dsh-multica-runtime) - **66 stars** | `No standard license`. A local DSH runtime bridge for Multica that exposes a versioned stdio protocol without patching the Harness source.
  - Install: `dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime`

- [DSH Ops](https://github.com/T-Auto/dsh-ops) - **62 stars** | `MIT AND Apache-2.0`. Add Windows shell, file, and background-job tools with Bash, PowerShell, and Rust components.
  - Install: `dsh plugin --profile web add dsh-ops@0.2.4`

- [DSH OpenCode Go](https://github.com/Duskriver/dsh-opencode-go) - **59 stars** | `MIT`. Connect OpenCode Go models to the DSH model provider interface.
  - Install: `dsh plugin --profile web add dsh-opencode-go@0.1.12`

- [DSH Environment Inspector](https://github.com/webkubor/dsh-env-inspector) - **56 stars** | `MIT`. Inspect installed runtimes, command-line tools, plugins, credential presence, and occupied development ports.
  - Install: `dsh plugin --profile web add @dsh-plugins/dsh-env-inspector@0.2.8`

- [DSH Sandbox Escalation Fix](https://github.com/HakureiMonika/dsh-sandbox-escalation-fix) - **56 stars** | `MIT`. A compatibility plugin for DSH sandbox escalation, tool permissions, and third-party model sessions.
  - Install: `dsh plugin --profile web add github:HakureiMonika/dsh-sandbox-escalation-fix`

- [DSH WSL Workspace](https://github.com/6Mikao9/dsh-wsl-workspace) - **53 stars** | `MIT`. A DeepSeek Harness bundle that provides WSL-backed filesystem and shell access for Windows workspaces.
  - Install: `dsh plugin --profile web add dsh-wsl-workspace`

- [DSH Codex Shell](https://github.com/Ephemeral-AI-Lab/dsh-plugins) - **49 stars** | `MIT`. A shell plugin that adds interactive exec_command and write_stdin tools to DSH profiles.
  - Install: `dsh plugin --profile web add dsh-codex-shell@0.1.2`

- [DSH MinerU](https://github.com/HuanLinOTO/dsh-plugin-mineru) - **47 stars** | `AGPL-3.0`. MinerU-backed document parsing tools that convert PDF, images, DOCX, PPTX, and XLSX files into structured Markdown or JSON.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-mineru`

- [DSH Benign Exit](https://github.com/sunruize93-cmyk/dsh-benign-exit) - **44 stars** | `MIT`. A DeepSeek Harness bundle that provides a controlled exit command for completed or canceled tasks.
  - Install: `dsh plugin --profile web add dsh-benign-exit`

- [DSH Plugin Guard](https://github.com/lxzy-7/dsh-plugin-guard) - **44 stars** | `MIT`. A DeepSeek Harness bundle that snapshots plugin and profile changes, guards boot, and rolls back failed installations.
  - Install: `dsh plugin --profile web add github:lxzy-7/dsh-plugin-guard`

- [DSH Filesnap](https://github.com/extracurricular-ai/dsh-filesnap) - **43 stars** | `Apache-2.0`. A DeepSeek Harness rewind bundle that restores conversation state and changed files without requiring a Git repository.
  - Install: `dsh plugin --profile web add dsh-filesnap`

- [DSH CLI Provider](https://github.com/ClapEcho233/dsh-cli-provider) - **39 stars** | `MIT`. Use locally authenticated Codex CLI and Claude Code accounts as DSH model providers.
  - Install: `npm install && npm run build && dsh plugin --profile web add .`

- [DSH Trae Connect](https://github.com/dingminhua/dsh-connect-trae) - **38 stars** | `MIT`. Use locally signed-in Trae model accounts in DSH with usage and credit controls.
  - Install: `dsh plugin --profile desktop add dsh-connect-trae`

- [DSH WorkBuddy Account Pool](https://github.com/XDTrees/dsh-workbuddy-xdpool) - **38 stars** | `MIT`. Pool locally signed-in WorkBuddy accounts with failover, usage information, and model discovery.
  - Install: `dsh plugin --profile desktop add dsh-workbuddy-xdpool`

- [DSH Files](https://github.com/taxueseek/dsh-files) - **37 stars** | `MIT`. A DSH bundle for isolated file uploads, document reading, and cached text extraction across common file formats.
  - Install: `dsh plugin --profile web add git+https://github.com/taxueseek/dsh-files.git`

- [DeepSeek Harness ACP](https://github.com/openma-ai/deepseek-harness-acp) - **36 stars** | `Apache-2.0`. A DeepSeek Harness bundle that exposes sessions, tools, skills, and persistence through the Agent Client Protocol.
  - Install: `dsh plugin --profile acp add @openma/deepseek-harness-acp@latest`

- [DSH ChatGPT Subscription](https://github.com/Aa728848/dsh-chatgpt-subscription) - **35 stars** | `MIT`. Connect a ChatGPT subscription as a model provider in DSH.
  - Install: `dsh plugin --profile web add @eddyskywalker/dsh-chatgpt-subscription`

- [DSH Better Edit](https://github.com/Rianico/dsh-better-edit) - **34 stars** | `MIT`. A DeepSeek Harness bundle that provides hash-addressed read and edit tools for verified file changes.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-better-edit`

- [DSH Token Compression](https://github.com/vibe-any/dsh-plugin-save-token) - **34 stars** | `MIT`. Compress structured context and tool results with configurable encoding and summarization policies.
  - Install: `dsh plugin --profile web add dsh-plugin-save-token@2.4.1`

- [DSH Better DeepSeek Bridge](https://github.com/EdgeTypE/dsh-better-deepseek) - **33 stars** | `MIT`. Connect the Better-DeepSeek browser extension to DeepSeek Harness through a bridge plugin.
  - Install: `dsh plugin --profile web add -w dsh-better-deepseek`

- [DSH CommandCode Go Provider](https://github.com/Ajwyunsx/dsh-cmdgo-provider) - **33 stars** | `MIT`. Connect CommandCode Go accounts to DSH with account rotation and subscription usage displays.
  - Install: `dsh plugin --profile web add dsh-cmdgo-provider`

- [DSH Backup and Migration](https://github.com/xiaoyuyu6420/dsh-backup) - **32 stars** | `MIT`. Back up, restore, and migrate DSH data with scheduled snapshots and recovery tools.
  - Install: `dsh plugin --profile web add @xiaoyuyu6420/dsh-backup@0.13.4`

- [DSH Thinking Loop Guard](https://github.com/MrWeiCodes/dsh-loop-guard) - **32 stars** | `MIT`. Detect repeated reasoning or output, interrupt stalled model calls, and analyze recorded DSH sessions.
  - Install: `dsh plugin --profile web add @mrweicodes/dsh-loop-guard@1.0.10`

- [DSH Web Tokens Bridge](https://github.com/xinyuquan985-coder/DSH-webtokens) - **32 stars** | `No license detected`. Connect browser-backed model sessions to DeepSeek Harness through a dedicated bridge bundle.
  - Install: `dsh plugin --profile web add "git+https://github.com/xinyuquan985-coder/DSH-webtokens.git#v0.2.15-deepseek"`

- [DSH Git Bash Shell](https://github.com/KannaKuron/dsh-gitbash-shell) - **31 stars** | `MIT`. Run agent shell commands through Git Bash on Windows and manage the shell settings in DSH.
  - Install: `dsh plugin --profile web add dsh-gitbash-shell@0.34.2`

- [DSH LSP Actions](https://github.com/PerryLink/dsh-lsp-actions) - **31 stars** | `Apache-2.0`. Use language servers for diagnostics, formatting, completion, code actions, symbols, signatures, inlay hints, and renaming.
  - Install: `dsh plugin --profile web add dsh-lsp-actions@0.5.15`

- [DSH Remote SSH](https://github.com/ZhangFengshun/dsh-remote-ssh) - **31 stars** | `MIT`. Connect remote workspaces over SSH with file browsing, editing, and integrated terminals in DSH.
  - Install: `dsh plugin --profile web add @zhangfengshun/dsh-remote-ssh@2.4.27`

- [Community DSH Toolkit](https://github.com/omdsh-dev/dsh-toolkit) - **30 stars** | `MIT`. Register time, encoding, JSON, calculation, CSV, regex, Markdown, diff, file-stat, and schema tools for DSH 0.1 hosts.
  - Install: `dsh plugin --profile web add github:omdsh-dev/dsh-toolkit`

- [DSH Checkpoint Rewind](https://github.com/PerryLink/dsh-checkpoint-rewind) - **30 stars** | `Apache-2.0`. Capture session, workspace, and configuration checkpoints with rollback commands and a settings timeline.
  - Install: `dsh plugin --profile web add dsh-checkpoint-rewind@0.6.34`

- [DSH Jev Interceptor](https://github.com/AskTheWay/dsh-jev-interceptor) - **30 stars** | `MIT`. Review tool calls and recalled session messages through a configurable Jev guard with approval controls.
  - Install: `dsh plugin --profile web add dsh-jev-interceptor@0.5.0`

- [DSH Office Tools](https://github.com/kw78/dsh-office-tools) - **30 stars** | `MIT`. Create, read, and update Word, Excel, and PowerPoint files with tools targeting the DSH 0.1.2 package family.
  - Install: `dsh plugin --profile web add dsh-office-tools@1.0.6`

- [DSH SSH Ops](https://github.com/caoyiwei850/dsh-ssh-ops) - **30 stars** | `MIT`. Add remote SSH operations, database tools, and a terminal panel for the DSH 0.1.2 package family.
  - Install: `dsh plugin --profile web add dsh-ssh-ops@0.3.20`

### Input & Navigation

- [BrowserSkill DSH Plugin](https://github.com/Tencent/BrowserSkill) - **7.7k stars** | `MIT`. A DeepSeek Harness bundle that exposes BrowserSkill browser automation tools for sessions, navigation, snapshots, clicks, forms, and screenshots.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/browser-skill-dsh-plugin`

- [OpenGUI DSH](https://github.com/Core-Mate/OpenGUI) - **1.8k stars** | `MIT`. A DSH plugin for controlling authorized Android phones and a managed local browser through delegated tasks.
  - Install: `dsh plugin --profile web add ./deepseek-harness-plugin`

- [DSH Pocket](https://github.com/shaobeichen/dsh-pocket) - **1.4k stars** | `GPL-2.0`. A Web plugin that mirrors DSH sessions to a phone over a local network or a password-protected Cloudflare tunnel.
  - Install: `dsh plugin --profile web add dsh-pocket -w`

- [DSH AionUI Panel](https://github.com/ningbainb/deepseek-harness-desktop) - **764 stars** | `Apache-2.0`. Browse workspace files, Git changes, and document previews in a DSH right-side panel.
  - Install: `dsh plugin --profile web add @linxin666/dsh-client-ui-aionui-panel`

- [DSH Antibrow](https://github.com/antibrow/dsh-antibrow) - **577 stars** | `MIT`. A DeepSeek Harness browser plugin with persistent identities, per-profile cookies and passkeys, and optional residential proxy egress.
  - Install: `dsh plugin --profile <name> add dsh-antibrow`

- [DSH At File](https://github.com/FSMargoo/dsh-at-file) - **512 stars** | `MIT`. A composer extension for searching workspace paths with at-file mentions and attaching file contents to prompts.
  - Install: `dsh plugin --profile web add https://github.com/FSMargoo/dsh-at-file/archive/refs/tags/v0.6.0.tar.gz`

- [DSH Mobile](https://github.com/saya-ch/dsh-mobile) - **329 stars** | `Apache-2.0`. A DeepSeek Harness mobile bundle with touch-friendly navigation and a compact conversation layout.
  - Install: `dsh plugin --profile web add dsh-mobile@alpha`

- [DSH Ego Browser](https://github.com/Fisfzy/dsh-ego-browser) - **321 stars** | `MIT`. Run browser automation tools through the bundled Ego runtime and watch browser activity in a live panel.
  - Install: `dsh plugin --profile web add dsh-ego-browser@0.9.2`

- [DSH Free Search](https://github.com/DDDMUC/dsh-free-search) - **269 stars** | `MIT`. A multi-engine DSH search provider with free backends, automatic fallback, settings, and platform search.
  - Install: `git clone https://github.com/DDDMUC/dsh-free-search.git && dsh plugin --profile web add ./dsh-free-search`

- [DSH Harness Remote](https://github.com/liguobao/ds-harness-remote) - **234 stars** | `MIT`. A DeepSeek Harness bundle that adds encrypted remote access for continuing sessions from desktop, Web, and Android clients.
  - Install: `dsh plugin --profile web add ds-harness-remote@0.3.29`

- [DSH WeChat Channel](https://github.com/xcisxc29/dsh-wechat) - **153 stars** | `MIT`. Control a desktop DSH agent from WeChat through a dedicated messaging channel bundle.
  - Install: `dsh plugin --profile desktop add dsh-wechat-plugin@0.43.1`

- [DSH Annotation](https://github.com/omdsh-dev/dsh-annotation) - **129 stars** | `MIT`. A DSH Web selection tool that annotates assistant text and sends numbered annotation blocks with a message.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git`

- [Humanizer RU DSH](https://github.com/Vladimir-Human/humanizer-ru) - **126 stars** | `MIT`. A Russian text-humanization bundle for DSH with reusable writing skills.
  - Install: `dsh plugin --profile web add "github:Vladimir-Human/humanizer-ru#path:/dsh"`

- [DSH EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) - **118 stars** | `MIT`. A DSH Web editing plugin for recalling, rewriting, versioning, and restoring user messages.
  - Install: `dsh plugin --profile web add dsh-easyrewrite`

- [DSH Meme](https://github.com/yyh-001/dsh-meme) - **112 stars** | `MIT`. A DSH meme plugin with searchable image packs, learned memes, emotion-based sending, and a composer picker.
  - Install: `dsh plugin --profile web add dsh-meme`

- [BrowserMCP DSH Bundle](https://github.com/jackwener/BrowserMCP) - **109 stars** | `Apache-2.0`. Connect a configured BrowserMCP Chrome service to DSH through a dedicated native MCP client bundle.
  - Install: `npm install -g @jackwener/browsermcp@0.0.33 && browsermcp setup && dsh plugin --profile web add @jackwener/browsermcp@0.0.33`

- [DSH Turn Delete](https://github.com/hanshenmesen/dsh-turn-delete) - **108 stars** | `MIT`. A DSH Web plugin for deleting one complete closed conversation turn while preserving the Session and later turns.
  - Install: `dsh plugin --profile web add dsh-turn-delete`

- [DSH Web Voice Bridge](https://github.com/Yuuyuko-uu/dsh-tts-bridge) - **101 stars** | `MIT`. Read DSH conversation messages through an authenticated DeepSeek web session in the user's browser.
  - Install: `dsh plugin --profile web add github:Yuuyuko-uu/dsh-tts-bridge`

- [DSH Remote Control](https://github.com/SCSpotato/dsh-remote) - **98 stars** | `GPL-3.0`. Control a DSH agent from a phone through a minimal HTTP and server-sent event interface.
  - Install: `dsh plugin --profile web add <path-to-dsh-remote>/remote-control`

- [DSH Browser Crossplatform](https://github.com/youbaiyun/dsh-browser-crossplatform) - **93 stars** | `MIT`. Connect a browser extension to DSH for browser control, page interaction, and image interpretation.
  - Install: `dsh plugin --profile web add dsh-browser-crossplatform@0.38.5`

- [DSH Prompt Optimizer](https://github.com/WestFox-AwA/dsh-prompt-optimizer) - **92 stars** | `BSD-3-Clause`. A DeepSeek Harness bundle that analyzes and rewrites prompts with configurable optimization steps before model requests.
  - Install: `dsh plugin --profile web add https://github.com/WestFox-AwA/dsh-prompt-optimizer/releases/latest/download/dsh-external-dsh-prompt-optimizer.tgz`

- [DSH Built-in Browser](https://github.com/wqty123/dsh-browser) - **83 stars** | `MIT`. A DeepSeek Harness plugin that gives agents a shared real browser for navigation and user-visible interaction.
  - Install: `dsh plugin --profile web add dsh-builtin-browser`

- [DSH Prompt Enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) - **77 stars** | `No standard license`. A DeepSeek Harness bundle that adds prompt editing helpers and reusable input enhancements.
  - Install: `dsh plugin --profile web add github:Fishsb/dsh-prompt-enhancer#v3.3.1`

- [DSH Omi Voice](https://github.com/PolinniZhong/dsh-omi-voice) - **74 stars** | `MIT`. A DSH Web voice plugin for click-to-read and automatic conversation narration through Omi.
  - Install: `dsh plugin --profile web add "github:PolinniZhong/dsh-omi-voice#v0.1.2&path:/"`

- [Web Search Pro DSH](https://github.com/anweat/dsh-web-search-pro) - **72 stars** | `MIT`. A Web search bundle with multiple providers, persistent caching, site-specific search, and Playwright rendering tools.
  - Install: `dsh plugin --profile web add @anweat/dsh-browser@^0.1.8 dsh-web-search-pro@^0.1.8`

- [DSH Claude UX](https://github.com/eri64/dsh-claude-ux) - **69 stars** | `MIT`. A Web plugin that adds reversible region risk controls and automatic conversation termination for abusive interactions.
  - Install: `dsh plugin --profile web add github:eri64/dsh-claude-ux`

- [DSH QQ Conversation Bridge](https://github.com/Yuuyuko-uu/dsh-qq-bridge) - **69 stars** | `MIT`. Forward messages between DSH conversations and QQ through a OneBot 11 HTTP connection.
  - Install: `dsh plugin --profile desktop add github:Yuuyuko-uu/dsh-qq-bridge`

- [DSH Pilot](https://github.com/momasiku/dsh-pilot) - **67 stars** | `MIT`. Control Windows applications through screenshots, mouse and keyboard actions, and native automation tools.
  - Install: `dsh plugin --profile web add @momasiku/dsh-pilot@0.6.4`

- [OpenCues DSH](https://github.com/opencues/opencues) - **59 stars** | `MIT`. A DSH composer plugin for word alternatives, underscore-gated fill-ins, and passive rewrite cues.
  - Install: `dsh plugin --profile web add @opencues/dsh`

- [DSH Sticky Prompt](https://github.com/oil-oil/dsh-oil-sticky-prompt) - **53 stars** | `MIT`. Pin the nearest user prompt above the conversation transcript.
  - Install: `dsh plugin --profile web add github:oil-oil/dsh-oil-sticky-prompt`

- [Open in VS Code](https://github.com/omdsh-dev/dsh-open-in-vscode) - **53 stars** | `MIT`. Adds a workspace-row action that opens the selected DSH directory in VS Code or another configured editor.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz`

- [DSH Tether](https://github.com/zexadev/dsh-tether) - **52 stars** | `MIT`. A DeepSeek Harness remote-access bundle that connects to Android and iOS clients over a peer-to-peer iroh transport.
  - Install: `dsh plugin --profile web add .`

- [DSH Navbar](https://github.com/vlln/dsh-navbar) - **51 stars** | `MIT`. A conversation node bar that lets users jump quickly between user messages in the DSH Web view.
  - Install: `dsh plugin --profile web add @vlln/dsh-navbar`

- [DSH Message Edit](https://github.com/Moeblack/dsh-message-edit) - **49 stars** | `MIT`. A conversation plugin for branching, editing, rerolling, retrying, and reviewing DSH message versions.
  - Install: `dsh plugin --profile web add dsh-message-edit`

- [DSH Web Startup Auth](https://github.com/GDWhisper/dsh-web-startup-auth) - **47 stars** | `MIT`. A DSH Web bundle that adds authenticated remote startup and configurable access controls for the local server.
  - Install: `dsh plugin --profile web add dsh-web-startup-auth@latest`

- [DSH Computer Use](https://github.com/Anionex/dsh-computer-use) - **46 stars** | `MIT`. A macOS DeepSeek Harness bundle for scoped observation and foreground-app keyboard control with explicit permissions.
  - Install: `dsh plugin --profile web add @anionex/dsh-computer-use`

- [DSH Full Remote](https://github.com/JUANWANG-BUAA/dsh-full-remote) - **45 stars** | `MIT`. Adds a mobile-friendly remote control panel for a DeepSeek Harness Web profile.
  - Install: `dsh plugin --profile web add dsh-full-remote`

- [DSH Voice Companion](https://github.com/beiyege-01/dsh-voice-ai-girlfriend-plugin) - **44 stars** | `MIT`. Add voice input, streamed speech replies, and conversation controls through a separate DSH companion bundle.
  - Install: `npm install --ignore-scripts && node build.mjs && dsh plugin --profile web-v021 add /absolute/path/to/dsh-voice-ai-girlfriend-plugin`

- [DSH Mobile Gateway](https://github.com/Clarklevis1995/dsh-plugin-mobile-gateway) - **43 stars** | `MIT`. A DeepSeek Harness Web bundle that provides authenticated mobile gateway access with session control, events, files, and device pairing.
  - Install: `dsh plugin --profile web add dsh-plugin-mobile-gateway@latest`

- [DSH Browser Extension Control](https://github.com/angelky7/dsh-browser-control) - **42 stars** | `AGPL-3.0-only`. Control browser tabs through a local WebSocket bridge, browser extension, and native DSH tools.
  - Install: `dsh plugin --profile web add @angelky7/dsh-browser-control@1.1.0`

- [DSH Voice Reader](https://github.com/1624318455/dsh-plugin-tts) - **40 stars** | `MIT`. Read DSH messages aloud with configurable Edge TTS, RVC, Index-TTS2, CosyVoice, or Google Cloud voices.
  - Install: `dsh plugin --profile web add @memef1f1y/dsh-plugin-tts@0.6.7`

- [DSH Computer Use macOS](https://github.com/988hj7tczd-oss/dsh-computer-use) - **39 stars** | `MIT`. A macOS desktop-control DSH bundle with scoped screen observation, input actions, app launching, and safety checks.
  - Install: `./install.sh`

- [DSH Remote Suite](https://github.com/Blank-not-black/dsh-Remote) - **39 stars** | `MIT`. A DSH remote-access suite with a profile plugin, gateway, mobile client, and Web management panel.
  - Install: `dsh plugin --profile web add dsh-remote-plugin`

- [DSH Windows Computer Use](https://github.com/Yu-tao-Li/dsh-computer-use-win) - **38 stars** | `MIT`. Control Windows applications through a bundled MCP bridge with UI Automation, screenshots, OCR, and input tools.
  - Install: `dsh plugin --profile web add dsh-computer-use-win@0.2.6`

- [DSH Knit](https://github.com/PolinniZhong/dsh-knit) - **37 stars** | `MIT`. Find workspace documents and media in a sidebar ranked by relevance to the current conversation.
  - Install: `dsh plugin --profile web add dsh-knit`

- [DSH QQ Bot Plus](https://github.com/zaofan-make/dsh-qqbot) - **36 stars** | `MIT`. Connect QQ to DSH with scheduled messages, media libraries, multiple bot instances, and a visual settings panel.
  - Install: `dsh plugin --profile web add @zaofan/dsh-qqbot@1.10.10`

- [DSH Web LAN Access](https://github.com/AcidGr/dsh-web-lan-access) - **35 stars** | `MIT`. A DSH Web bundle that exposes the service on a local network with dynamic LAN and VPN trust handling.
  - Install: `dsh plugin --profile web add dsh-web-lan-access`

- [DSH Voice Scribe](https://github.com/PensiveFei/dsh-voice-scribe) - **34 stars** | `MIT`. A DSH voice input plugin that transcribes spoken prompts into the composer with optional OpenAI-compatible ASR.
  - Install: `dsh plugin --profile web add dsh-voice-scribe`

- [DSH IM Connect](https://github.com/MichengAI/dsh-im-connect) - **33 stars** | `Apache-2.0`. Connect messaging platforms to local DSH sessions for sending tasks, receiving replies, and handling questions and approvals.
  - Install: `dsh plugin --profile web add @michengai/dsh-im-connect@latest --registry=https://registry.npmjs.org/`

- [DSH Skill Picker](https://github.com/a735624258/dsh-skill-picker) - **33 stars** | `MIT`. Search installed skills from the message composer and insert a selected skill command.
  - Install: `dsh plugin --profile web add dsh-skill-picker@0.5.28`

- [DSH Workspace Explorer](https://github.com/Jiyr0119/dsh-workspace-explorer) - **33 stars** | `MIT`. Browse workspace files in a sidebar with search, previews, and click or drag file references.
  - Install: `dsh plugin --profile web add -w @jiyr0119/dsh-workspace-explorer@latest`

- [DSH Chat Timeline](https://github.com/jjxjjjjiik-bot/dsh-chat-timeline) - **32 stars** | `MIT`. A DeepSeek Harness Web plugin that adds a conversation navigation panel with bookmarks and rollback links.
  - Install: `dsh plugin --profile web add dsh-chat-timeline`

- [DSH Think Chinese](https://github.com/Len7183/DSH-Think-zh) - **32 stars** | `MIT`. Request Simplified Chinese reasoning through a switch in DSH general settings.
  - Install: `dsh plugin --profile web add github:Len7183/DSH-Think-zh`

- [DSH QQ Channel](https://github.com/xcisxc29/dsh-qq-plugin) - **31 stars** | `MIT`. Control local DSH conversations from QQ through the official QQ bot platform and a dedicated settings panel.
  - Install: `dsh plugin --profile desktop add dsh-qq-plugin@1.0.5`

- [DSH Remote Mobile](https://github.com/IceApriler/dsh-remote-mobile) - **31 stars** | `MIT`. Access the DSH Web interface through a remote gateway with mobile layouts and connection controls.
  - Install: `dsh plugin --profile web add dsh-remote-mobile@1.9.1`

- [DSH Xiaomi and Doubao TTS](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) - **31 stars** | `MIT`. Read messages through Xiaomi MiMo or Doubao voices with browser speech fallback and optional interface sounds.
  - Install: `dsh plugin --profile web add dsh-xiaomi-tts@4.2.2`

- [DSH Better Input](https://github.com/DIAG5/dsh-better-input) - **30 stars** | `MIT`. Add voice input, prompt editing, and local file-to-Markdown input to the DSH composer.
  - Install: `dsh plugin --profile web add dsh-better-input`

- [DSH Browser Control](https://github.com/caob23/dsh-browser-control) - **30 stars** | `AGPL-3.0-only`. Connect a Chrome extension to DSH for browser control through a local WebSocket bridge.
  - Install: `dsh plugin --profile web add @caob23/dsh-browser-control@1.0.17`

- [DSH Playwright Browser](https://github.com/anweat/dsh-browser) - **30 stars** | `MIT`. Provide browser automation through bundled Playwright and OpenCLI dependencies for DSH 0.2.0-rc.2.
  - Install: `dsh plugin --profile web add @anweat/dsh-browser@0.2.1`

### Memory & Knowledge

- [Hindsight Coding Agents](https://github.com/vectorize-io/hindsight) - **40.5k stars** | `MIT`. A DeepSeek Harness memory bundle with automatic recall, session capture, knowledge pages, and per-repository memory banks.
  - Install: `dsh plugin --profile web add @vectorize-io/hindsight-coding-agents`

- [OpenViking Memory](https://github.com/volcengine/OpenViking) - **38.9k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle with OpenViking auto-recall, session capture, protected viking:// URIs, and MCP tools.
  - Install: `dsh plugin --profile web add @openviking/dsh-memory-plugin`

- [WeKnora Knowledge](https://github.com/Tencent/WeKnora) - **30.9k stars** | `MIT`. A DeepSeek Harness bundle for semantic knowledge search, document reading, and RAG answers over user-managed knowledge bases.
  - Install: `dsh plugin --profile web add @wxg-prc-cpg/dsh-weknora`

- [EverOS Memory](https://github.com/EverMind-AI/EverOS) - **13.3k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle that provides automatic cross-session recall through a local EverOS service.
  - Install: `dsh plugin --profile web add @evermind-ai/dsh-plugin`

- [MemOS Local Memory](https://github.com/MemTensor/MemOS) - **11.6k stars** | `MIT`. A local MemOS memory bundle for DeepSeek Harness with layered recall, reflection, policy induction, and skill crystallization.
  - Install: `curl -fsSL https://raw.githubusercontent.com/MemTensor/MemOS/main/apps/memos-local-plugin/install.sh | bash -s -- --agent dsh --profile web`

- [ReMe](https://github.com/agentscope-ai/ReMe) - **3.5k stars** | `Apache-2.0`. A DeepSeek Harness memory bundle with recall, capture, settings, and skill guidance for TypeScript agent workflows.
  - Install: `dsh plugin --profile web add @agentscope-ai/reme`

- [MemSearch](https://github.com/zilliztech/memsearch) - **2.7k stars** | `MIT`. A DeepSeek Harness memory bundle that captures shared Markdown notes, injects context before steps, and reviews candidate skills.
  - Install: `dsh plugin --profile web add @zilliz/memsearch-dsh`

- [SAG DSH](https://github.com/Zleap-AI/SAG) - **2.6k stars** | `MIT`. Search and read a SAG knowledge base, upload documents, and manage stored content through native DSH tools.
  - Install: `dsh plugin --profile web add @zleap-ai/dsh-sag@0.2.0`

- [DSH Context](https://github.com/bowenliang123/dsh-context) - **1.6k stars** | `Apache-2.0`. A context dashboard and /context command that show how DSH messages, tools, injections, compactions, and token usage evolve.
  - Install: `dsh plugin --profile web add dsh-context`

- [mem9](https://github.com/mem9-ai/mem9) - **1.2k stars** | `Apache-2.0`. A persistent memory bundle for DeepSeek Harness with automatic recall, background ingest, and five memory tools.
  - Install: `dsh plugin --profile web add @mem9/dsh-plugin`

- [Deja-vu DSH](https://github.com/vshulcz/deja-vu) - **1.1k stars** | `MIT`. A local session-history plugin that indexes other coding agents for recall, digests, file history, and optional automatic context.
  - Install: `dsh plugin --profile web add dsh-deja`

- [ClearAI DSH](https://github.com/Clearailhc/clearai-dsh) - **769 stars** | `Apache-2.0`. Add an epistemic loop and local knowledge exploration to DeepSeek Harness.
  - Install: `dsh plugin --profile web add clearai-dsh`

- [Graph Memory](https://github.com/adoresever/graph-memory) - **631 stars** | `MIT`. A graph-based memory plugin for cross-session recall, PageRank, communities, and vector search in DSH.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.1.tgz`

- [DSH-X Sync](https://github.com/yyh-001/DSH-X) - **626 stars** | `MIT`. Sync DSH sessions, attachments, skills, settings, and memory to storage services or local archives.
  - Install: `dsh plugin --profile web add -w <path-to-DSH-X>/plugins/dsh-x-sync --config.auto-install-peers=false`

- [Mnemon](https://github.com/mnemon-dev/mnemon) - **598 stars** | `Apache-2.0`. A persistent memory plugin that supplies graph-based recall and cross-session knowledge to DSH agents.
  - Install: `dsh plugin --profile web add dsh-mnemon`

- [Obelisk DSH](https://github.com/tommy0103/obelisk) - **571 stars** | `AGPL-3.0-only`. Load the packaged Obelisk agent skill through a dedicated DSH bundle with context-window integration.
  - Install: `npm ci && npm run build:core && npm run build --workspace @obelisk/dsh-obelisk-plugin && dsh plugin --profile web add --workspace-root ./packages/dsh-plugin`

- [DSH Mimir](https://github.com/1692775560/dsh-Mimir-Academic-research) - **541 stars** | `MIT`. A research assistant suite for DSH with literature search, a research wiki, LaTeX compilation, and subagent review.
  - Install: `dsh plugin --profile web add dsh-mimir@latest`

- [Bailian Knowledge DSH](https://github.com/modelstudioai/cli) - **537 stars** | `Apache-2.0`. A DeepSeek Harness bundle that connects agents to Aliyun Model Studio knowledge bases through search and grounded Q&A tools.
  - Install: `dsh plugin --profile web add bailian-kb-dsh`

- [MisakaNet DSH](https://github.com/Ikalus1988/MisakaNet) - **514 stars** | `Apache-2.0`. A DSH plugin for searching and sharing verified debugging lessons from a local, Git-backed knowledge base.
  - Install: `dsh plugin add git+https://github.com/Ikalus1988/MisakaNet.git`

- [Billion Context Native DSH](https://github.com/ranxianglei/billion-context) - **475 stars** | `MIT`. Compress session context and preserve task history through a native DSH bundle.
  - Install: `dsh plugin --profile web add billion-context`

- [Flowix Memory](https://github.com/text2future/flowix) - **441 stars** | `MIT`. A config-only DSH bundle that exposes Flowix notebook memos and artifact tools through a local stdio MCP server.
  - Install: `dsh plugin --profile web add ./app/flowix-dsh-host/bundles/dsh-flowix-memory`

- [Molio DSH Knowledge](https://github.com/zhuzhaoyun/Molio) - **434 stars** | `Modified Apache-2.0 (commercial service and branding restrictions)`. Search, browse, and read a local Molio knowledge base from DSH conversations.
  - Install: `dsh plugin --profile web add dsh-plugin-molio@0.1.0`

- [Mnemon DSH Plugin](https://github.com/omdsh-dev/dsh-mnemon) - **418 stars** | `MIT`. A DeepSeek Harness memory plugin with a three-tier control plane for storing and retrieving project context.
  - Install: `dsh plugin --profile web add dsh-mnemon`

- [DSH Memory Evolve](https://github.com/csyangwen/dsh-memory-evolve) - **338 stars** | `MIT`. A Web DSH memory and workflow plugin with cross-session recall, skill management, todos, session search, and external-agent dispatch.
  - Install: `dsh plugin --profile web add github:csyangwen/dsh-memory-evolve`

- [PLUR DSH](https://github.com/plur-ai/plur) - **296 stars** | `Apache-2.0`. A DeepSeek Harness memory plugin that injects PLUR engrams into prompts without an MCP tool call.
  - Install: `dsh plugin add @plur-ai/dsh`

- [CortexDB DSH Memory](https://github.com/liliang-cn/cortexdb) - **285 stars** | `MIT`. Connect DSH conversations to CortexDB for persistent memory storage and retrieval.
  - Install: `dsh plugin --profile web add cortexdb-dsh-memory@2.125.0`

- [DSH Memory](https://github.com/FuRongJun-1999/dsh-memory) - **278 stars** | `MIT`. A DSH plugin that provides persistent cross-session memory for multiple agents.
  - Install: `dsh plugin --profile web add @furongjun1999/dsh-memory`

- [Polaris DSH Integration](https://github.com/ZJU-REAL/Polaris) - **248 stars** | `Apache-2.0`. A DSH bundle that connects Polaris MCP tools and native agent skills to a configured Polaris account.
  - Install: `cd integrations/deepseek-harness && npm ci && npm run check && dsh plugin --profile web add "$PWD"`

- [Hypatia DSH](https://github.com/MarchLiu/hypatia) - **239 stars** | `MIT`. A DSH bundle that adds Hypatia skills, memory helpers, and a configurable auto-approval answerer to a profile.
  - Install: `dsh plugin --profile web add dsh-hypatia`

- [DSH Chat Import](https://github.com/Nwflower/dsh-chat-import) - **204 stars** | `MIT`. A conversation migration plugin that imports histories from external agent tools into resumable DSH sessions and exports them back.
  - Install: `dsh plugin --profile web add dsh-chat-import`

- [Engramory](https://github.com/tinqiao-oss/engramory) - **191 stars** | `MIT`. A file-based DSH memory plugin that keeps human-readable notes in a versioned store with deterministic limits.
  - Install: `dsh plugin --profile web add dsh-engramory`

- [DSH Fish Memory](https://github.com/Yuuyuko-uu/dsh-fish-memory) - **186 stars** | `MIT`. Keep timestamped conversation memories with gradual forgetting and configurable recall.
  - Install: `dsh plugin --profile web add github:Yuuyuko-uu/dsh-fish-memory`

- [DSH Research Report](https://github.com/PerryLink/dsh-research-report) - **182 stars** | `Apache-2.0`. A DeepSeek Harness bundle for producing evidence-linked research reports with verification states and audit artifacts.
  - Install: `dsh plugin --profile demo add dsh-research-report`

- [DSH Git Memory](https://github.com/seriousz158/dsh-memory) - **181 stars** | `MIT`. A Git-backed long-term memory plugin that stores durable DSH memory locally, exposes settings controls, and optionally synchronizes idle sessions.
  - Install: `dsh plugin --profile web add github:seriousz158/dsh-memory`

- [Industry Research DSH](https://github.com/PerryLink/dsh-industry-research) - **179 stars** | `Apache-2.0`. A research bundle for industry maps, company timelines, evidence cards, and auditable reports in DSH.
  - Install: `dsh plugin --profile demo add dsh-industry-research`

- [DSH Notes](https://github.com/zhaoolee/notes) - **173 stars** | `MIT`. A DSH tool plugin that exports agent output into a self-hosted Notes service.
  - Install: `dsh plugin --profile web add @zhaoolee/dsh-notes`

- [DSH Bili Humanism](https://github.com/InariNGT-Ofiicial/dsh-bili-humanism) - **157 stars** | `MIT`. Read Bilibili subtitles and sampled frames, keep private viewing notes, and maintain configurable persona records.
  - Install: `dsh plugin --profile web add https://github.com/InariNGT-Ofiicial/dsh-bili-humanism/releases/download/v1.10.0/dsh-bili-humanism-1.10.0.tgz`

- [DSH NextTavern](https://github.com/a86582751/dsh-nexttavern) - **136 stars** | `GPL-3.0-only`. Run long-form roleplay with character cards, persistent memory, world state, and SillyTavern imports.
  - Install: `dsh plugin --profile web add dsh-nexttavern`

- [BibiGPT DSH](https://github.com/JimmyLv/bibigpt-skill) - **128 stars** | `MIT`. Summarize online videos, podcasts, and audio through the BibiGPT DSH integration.
  - Install: `dsh plugin --profile web add "github:JimmyLv/bibigpt-skill#path:/dsh-plugin"`

- [DSH Noema](https://github.com/ZSeven-W/dsh-noema) - **128 stars** | `MIT`. Durable Noema-backed memory for DSH with recall tools, cross-agent imports, and a settings page.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-noema@latest`

- [DSH Mneme](https://github.com/slow-stack/mneme) - **127 stars** | `MIT`. A DSH memory plugin for persistent project knowledge and recall across sessions.
  - Install: `dsh plugin --profile web add @modusensus/dsh-mneme`

- [Meow Memory](https://github.com/Phant0Meow/dsh-meow-memory) - **126 stars** | `MIT`. A cross-session memory bundle with layered storage, BM25 retrieval, session capture, and a configurable Web panel.
  - Install: `dsh plugin --profile web add github:Phant0Meow/dsh-meow-memory`

- [DSH Memento](https://github.com/PerryLink/dsh-memento) - **124 stars** | `Apache-2.0`. A bounded cross-session memory service for DSH with approval-gated writes, audit trails, local SQLite storage, and recall tools.
  - Install: `dsh plugin --profile web add dsh-memento`

- [DSH Turn Rewind](https://github.com/Anionex/dsh-turn-rewind) - **120 stars** | `BSD-3-Clause`. A DSH recovery plugin that records workspace changes and restores a conversation turn through its Change Ledger.
  - Install: `dsh plugin --profile web add @anionex/dsh-turn-rewind`

- [Billion Context DSH](https://github.com/Tyan66666/billion-context-dsh) - **114 stars** | `MIT`. A DSH memory plugin for large-context retrieval, persistence, and project knowledge.
  - Install: `dsh plugin --profile web add billion-context-dsh`

- [DSH Project Brain](https://github.com/yj-liuzepeng/dsh-project-brain) - **103 stars** | `MIT`. Store project architecture and cross-session context for DSH agents.
  - Install: `dsh plugin --profile web add github:yj-liuzepeng/dsh-project-brain#v0.7.0-beta.2`

- [Scientific Figure Library DSH](https://github.com/xuzhougeng/ScientificFigureLibrary) - **98 stars** | `MIT`. Search a local figure-and-code library through native DeepSeek Harness tools.
  - Install: `dsh plugin --profile web add scientific-figure-library`

- [StrataGate DSH Memory](https://github.com/diqierjia/StrataGate-AgentMemory) - **97 stars** | `MIT`. A DeepSeek Harness memory bundle for capturing sessions, building evidence-linked local memory, and reviewing recalled context.
  - Install: `dsh plugin --profile web add stratagate-dsh`

- [Causal Memory DSH Plugin](https://github.com/JingxuanC/causal-memory) - **81 stars** | `Apache-2.0`. A local causal-memory bridge that exposes a native DSH bundle for structured recall and memory tools.
  - Install: `cd <causal-memory-repo> && dsh plugin --profile web add "$PWD/dsh-plugin"`

- [OpenContext DSH](https://github.com/melandlabs/opencontext) - **76 stars** | `Apache-2.0`. A DSH plugin for durable agent memory and retrieval-augmented context through OpenContext.
  - Install: `dsh plugin --profile web add dsh-opencontext`

- [DSH Evolve in Git](https://github.com/Kytolly/dsh-evolve-in-git) - **73 stars** | `MIT`. A DSH bundle for Git-backed memory, skill evolution, privacy filtering, and repository-aware workflow tools.
  - Install: `dsh plugin --profile web add github:Kytolly/dsh-evolve-in-git`

- [DSH Auto Memory](https://github.com/AskTheWay/dsh-auto-memory) - **69 stars** | `MIT`. Store typed memory files and inject a workspace memory index into the system prompt.
  - Install: `dsh plugin --profile demo add dsh-auto-memory`

- [Operator Memory DSH](https://github.com/aerovato/operator-memory) - **69 stars** | `BSD-3-Clause`. Recall stored context and update persistent memory through the Operator Memory DSH adapter.
  - Install: `dsh plugin --profile web add @aerovato/operator-deepseek`

- [Memory Eternal DSH](https://github.com/EternalNight996/memory-eternal) - **65 stars** | `MIT`. Save conversation knowledge to a local Markdown vault with recall tools, search, and a knowledge graph.
  - Install: `dsh plugin --profile web add memory-eternal@0.17.0`

- [DSH Sieve](https://github.com/Sev7eEn7/dsh-sieve) - **62 stars** | `MIT`. Filter tool output, prune conversation history, and control skill disclosure with an optional Web settings panel.
  - Install: `dsh plugin --profile web add dsh-sieve@0.2.0 dsh-sieve-web@0.2.0`

- [DSH Fund Research](https://github.com/PerryLink/dsh-fund-research) - **57 stars** | `Apache-2.0`. A DeepSeek Harness bundle for producing traceable fund research reports from sealed market snapshots.
  - Install: `dsh plugin --profile web add dsh-fund-research`

- [DSH DeepRead](https://github.com/xiehuan123/dsh-deepread) - **56 stars** | `MIT`. A DSH research-reading plugin for collecting sources, notes, evidence, and structured reading progress.
  - Install: `dsh plugin --profile web add dsh-deepread`

- [DSH Knowledge](https://github.com/Soren-ABT/dsh-knowledge) - **56 stars** | `AGPL-3.0`. A DSH knowledge bundle for document management, chunking, embeddings, retrieval, and a Web administration panel.
  - Install: `dsh plugin --profile <name> add dsh-knowledge`

- [Jingling DSH](https://github.com/Yi-111-a/dsh-jingling) - **54 stars** | `MIT`. A DeepSeek Harness companion bundle for local memory, guided reflection, and an optional desktop pet.
  - Install: `dsh plugin --profile web add dsh-jingling`

- [StudyHub](https://github.com/EricWang1358/dsh-web-studyhub) - **53 stars** | `MIT`. Create source-linked flashcards and quizzes from course materials and recordings, then review them with spaced repetition.
  - Install: `dsh plugin --profile web add https://github.com/EricWang1358/dsh-web-studyhub/releases/download/v2.7.1/ericwang1358-dsh-daily-flashcard-2.7.1.tgz`

- [Hacker News DSH](https://github.com/heartleo/hn-cli) - **51 stars** | `MIT`. Read Hacker News feeds, comment trees, user profiles, and Algolia search results through DSH tools.
  - Install: `dsh plugin --profile web add -w dsh-hacker-news`

- [DSH Scholar](https://github.com/lzszq/dsh-scholar) - **46 stars** | `BSD-3-Clause`. A DeepSeek Harness research workspace for evidence-linked investigations, project context, review stages, and durable research artifacts.
  - Install: `pnpm install --frozen-lockfile && pnpm run build && dsh plugin --profile web add /absolute/path/to/dsh-scholar`

- [NylonME DSH Memory](https://github.com/nylon-memory/NylonME) - **46 stars** | `MIT`. Recall and store session context through a self-hosted NylonME memory engine.
  - Install: `dsh plugin --profile web add <path-to-NylonME>/plugins/dsh-nylonme-memory`

- [Project Orrery DSH Adapter](https://github.com/ItIsMixian/Orrery) - **45 stars** | `MIT`. A DeepSeek Harness adapter that exposes Project Orrery's traceable Markdown documentation workflow as a packaged skill.
  - Install: `dsh plugin --profile orrery-test add <adapter-directory-or-tarball>`

- [Chinese Traditional Wisdom DSH](https://github.com/dhicoc/dsh-chinese-traditional-wisdom-skill) - **44 stars** | `MIT`. A DeepSeek Harness bundle that packages a local-first Chinese traditional wisdom consultation workflow.
  - Install: `dsh plugin add github:dhicoc/dsh-chinese-traditional-wisdom-skill`

- [SkillRoute DSH](https://github.com/erichare/skillroute) - **41 stars** | `MIT`. A DSH bundle that connects SkillRoute's skill router and MCP tools to DeepSeek Harness agents.
  - Install: `dsh plugin --profile web add @skillroute/dsh-plugin`

- [DSH-KRouter](https://github.com/398894496-arch/DSH-KRouter) - **39 stars** | `MIT`. A DeepSeek Harness bundle for an Obsidian-backed knowledge system with recall, daily distillation, and self-evolution controls.
  - Install: `dsh plugin --profile web add github:398894496-arch/runtime36`

- [Qiaomu RSS DSH](https://github.com/joeseesun/qiaomu-rss-dsh) - **37 stars** | `GPL-3.0-only`. Read RSS feeds in a DSH panel with translation, rewriting assistance, and agent tools.
  - Install: `npm pack && dsh plugin --profile desktop add ./qiaomu-rss-dsh-0.7.1.tgz`

- [DSH Agent Soul](https://github.com/cyanwell/dsh-agent-soul) - **36 stars** | `MIT`. Maintain layered agent memories, a structured persona directory, and configurable internal state through native DSH tools.
  - Install: `dsh plugin --profile web add link:/absolute/path/to/dsh-agent-soul`

- [DSH Engram](https://github.com/kenz1117/dsh-engram) - **34 stars** | `MIT`. Recall cross-session memories from SQLite with keyword and local-vector search, provenance, and spaced repetition.
  - Install: `dsh plugin --profile web add @kenz1117/dsh-engram@0.11.0`

- [DSH Model Context Catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - **34 stars** | `MIT`. A DSH plugin that catalogs model context limits and displays provider metadata in a Web settings panel.
  - Install: `dsh plugin --profile web add dsh-model-context-catalog`

- [DSH User Mirror](https://github.com/webkubor/dsh-mirror) - **34 stars** | `MIT`. Remember user preferences and working principles across sessions with memory decay and token-budgeted retrieval.
  - Install: `dsh plugin --profile web add @dsh-plugins/dsh-user-mirror@0.8.6`

- [DSH Host RSI Memory](https://github.com/pk14742952-AD/dsh-host-rsi) - **32 stars** | `MIT`. Store user corrections and task outcomes as persistent lessons with retrieval and repeated-loop checks.
  - Install: `dsh plugin --profile web add github:pk14742952-AD/dsh-host-rsi`

- [AI4Scholar](https://github.com/literaf/dsh-ai4scholar) - **31 stars** | `MIT`. Search academic literature, retrieve paper text, and generate citations through native DSH tools backed by AI4Scholar.
  - Install: `dsh plugin --profile web add dsh-ai4scholar`

- [DSH Memoir](https://github.com/Qinling-Melon-Farmers/dsh-memoir) - **31 stars** | `Apache-2.0`. Keep local project memory available across DSH sessions.
  - Install: `dsh plugin --profile web add dsh-memoir@0.8.0`

- [PRTS Terrarchive](https://github.com/HTian-qwq/prts-terrarchive) - **31 stars** | `SEE LICENSE IN THIRD_PARTY_NOTICES.md`. Browse the PRTS.chat corpus with local or cloud search and a Rhine Lab workspace.
  - Install: `dsh plugin --profile web add prts-terrarchive@0.2.1`

- [CiteCiter DSH](https://github.com/kirkchinese/CiteCiter) - **30 stars** | `MIT`. Organize source-based topics with manual drafts, permissions, visual boards, and learning cards.
  - Install: `dsh plugin --profile web add @kirkchinese/dsh-citeciter@0.9.0-alpha.3`

- [DSH Cross-Session Memory](https://github.com/hr98w/dsh-memory) - **30 stars** | `MIT`. Maintain long-term memory across DSH conversations with project and user context.
  - Install: `dsh plugin --profile web add @hr98w/dsh-memory@0.1.4`

- [DSH Obsidian](https://github.com/mingzeng21/dsh-obsidian) - **30 stars** | `MIT`. Search, read, write, move, and trash notes in a local Obsidian vault through native DSH tools.
  - Install: `dsh plugin --profile web add dsh-obsidian@0.2.6`

- [DSH Zotero](https://github.com/Vncntvx/dsh-zotero) - **30 stars** | `MIT`. Search a local Zotero library, read notes and annotations, extract evidence, and generate academic citations.
  - Install: `dsh plugin --profile web add dsh-zotero`

- [Miliastra Knowledge DSH](https://github.com/1475505/dsh-plugin-miliastra-toolbox) - **30 stars** | `MIT`. Search Miliastra node references, guides, tutorials, and client scripting documentation through native DSH tools.
  - Install: `dsh plugin --profile web add github:1475505/dsh-plugin-miliastra-toolbox`

### Themes & Appearance

- [DSH Balance Whale](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) - **3.3k stars** | `MIT`. A Web UI widget that displays DeepSeek account balance in a draggable whale companion.
  - Install: `dsh plugin --profile web add link:./dsh-whale-widget`

- [DSH Deep Whale](https://github.com/Small-tailqwq/dsh-deep-whale) - **2.2k stars** | `CC-BY-NC-SA-4.0`. A maid-atelier whale character skin for the DSH Web interface.
  - Install: `git clone https://github.com/Small-tailqwq/dsh-deep-whale.git && dsh plugin --profile web add ./dsh-deep-whale/maid-atelier`

- [DSH Pet](https://github.com/PC2005-cloud/dsh-pet) - **824 stars** | `MIT`. A floating DSH Web desktop pet with idle animations, random actions, screen wandering, and drag interactions.
  - Install: `dsh plugin --profile web add dsh-pet`

- [DSH Ads](https://github.com/Nagi-ovo/dsh-ads) - **636 stars** | `BSD-3-Clause`. A parody Web UI plugin that adds fake banner ads, popups, and small games styled after early portal sites.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-ads`

- [DSH Transparent UI](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - **406 stars** | `MIT`. A Web UI theme with adjustable glass effects, fluid or wallpaper backgrounds, and appearance controls for the DSH interface.
  - Install: `dsh plugin --profile web add dsh-client-ui-aqua`

- [DSH Wallpaper Engine](https://github.com/elysia395/dsh-wallpaper-engine) - **384 stars** | `MIT`. A DeepSeek Harness theme bundle for setting animated wallpapers and managing visual backgrounds.
  - Install: `dsh plugin --profile web add dsh-plugin-wallpaper-engine`

- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) - **380 stars** | `MIT`. A DeepSeek Harness skin that applies the Open Sea visual theme to the conversation interface.
  - Install: `dsh plugin --profile web add github:d-dev0101/open-sea-skin#v1.2.1`

- [DSH Dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - **362 stars** | `See ASSET_LICENSE.md`. A desktop companion that reacts to DSH session events with a floating BigFish character and configurable behaviors.
  - Install: `pnpm exec dsh plugin --profile web add dsh-dafeiyu@alpha`

- [Whale Girl](https://github.com/vlln/whale-girl) - **338 stars** | `MIT`. A draggable Web UI desktop pet with interaction, feeding, progress, and persistent state.
  - Install: `dsh plugin --profile web add github:vlln/whale-girl#main`

- [DSH Liang Intensity Skin](https://github.com/kingOfSoySauce/dsh-liang-skin) - **222 stars** | `No standard license`. An optional DSH Web skin that adds an adaptive reasoning-intensity slider and themed model-selection visuals.
  - Install: `dsh plugin --profile web add github:kingOfSoySauce/dsh-liang-skin#v0.1.4`

- [DSH Boot Animation](https://github.com/NativeDog1/dsh-boot-animation) - **207 stars** | `BSD-3-Clause`. Play a full-window introduction on DSH launch and when entering pinned conversations.
  - Install: `dsh plugin --profile web add github:NativeDog1/dsh-boot-animation`

- [DSH Dream Skin](https://github.com/RevolutionLA/dsh-dream-skin) - **191 stars** | `MIT`. A Web UI skin pack with animated themes, wallpapers, accents, import/export, and persistent per-user appearance settings.
  - Install: `dsh plugin --profile web add dsh-dream-skin`

- [DSH Skin Market](https://github.com/kingOfSoySauce/dsh-skin-market) - **165 stars** | `MIT`. A DSH Web marketplace plugin for browsing, installing, updating, disabling, and removing community skins.
  - Install: `dsh plugin --profile web add dsh-skin-market@0.1.36`

- [Deep Whale Day/Night Theme](https://github.com/GGBond2424648901/deep-whale-day-night-theme) - **117 stars** | `CC-BY-NC-SA-4.0`. A DeepSeek Harness theme bundle with coordinated Deep Whale day and night interface styles.
  - Install: `dsh plugin --profile web add github:GGBond2424648901/deep-whale-day-night-theme#runtime`

- [DSH Endfield Theme](https://github.com/ymh0000123/dsh-theme-endfield) - **105 stars** | `MIT`. A DSH Web theme plugin with Endfield-inspired tokens, styles, and configurable appearance settings.
  - Install: `dsh plugin --profile web add github:ymh0000123/dsh-theme-endfield`

- [DSH Custom Skin](https://github.com/SLin-code/dsh-custom-skin) - **100 stars** | `MIT`. A DeepSeek Harness Web bundle that adds configurable wallpapers and translucent interface skins.
  - Install: `pnpm dsh plugin --profile web add github:SLin-code/dsh-custom-skin`

- [DSH Feiyu Mood](https://github.com/Yuuyuko-uu/dsh-feiyu-mood) - **96 stars** | `MIT`. Track a conversation companion's configurable mood with a visible widget and event timeline.
  - Install: `dsh plugin --profile desktop add github:Yuuyuko-uu/dsh-feiyu-mood`

- [DSH Whale Musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) - **89 stars** | `MIT`. A DSH Web mascot plugin with a whale-girl companion, task reactions, and interactive status animations.
  - Install: `dsh plugin --profile web add github:Sutera-Diffusus/dsh-whale-musume`

- [BeautiCode](https://github.com/starsstreaming/beautiCode) - **83 stars** | `MIT`. A DeepSeek Harness theme bundle that adds BeautiCode visual styling to the client interface.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add beauticode-dsh`

- [DSH Claude Style](https://github.com/Nwflower/dsh-claude-style) - **76 stars** | `MIT`. Apply a Claude Code Desktop-inspired appearance and interaction layout to DSH Web.
  - Install: `dsh plugin --profile web add dsh-claude-style`

- [DSH Endfield UI](https://github.com/rison114514/dsh-endfield-ui) - **74 stars** | `MIT`. An unofficial Endfield-inspired DSH Web theme plugin that uses the standard bundle and client theme extension points.
  - Install: `dsh plugin --profile web add @rison/dsh-endfield-ui@0.7.0`

- [OpenQuantum Web Branding](https://github.com/xi-zhao/OpenQuantum) - **74 stars** | `MIT`. Apply OpenQuantum branding and Progressive Web App metadata to the native DSH interface.
  - Install: `dsh plugin --profile web add github:xi-zhao/OpenQuantum#path:/packages/openquantum-web-branding`

- [DSH 550C Boot](https://github.com/yannicksong0106/dsh-550c-boot) - **60 stars** | `MIT`. Play a configurable 550C launch animation with a short logo mode or a full introduction.
  - Install: `dsh plugin --profile web add github:yannicksong0106/dsh-550c-boot`

- [DSH Token Pet](https://github.com/Jimmy0123-ux/dsh-token-pet) - **56 stars** | `MIT`. A DSH Web companion that displays token usage and task status as a configurable animated pet.
  - Install: `dsh plugin --profile web add dsh-token-pet`

- [Catppuccin DSH Theme](https://github.com/NoNameLeGo/dsh-catppuccin-theme) - **49 stars** | `MIT`. A DeepSeek Harness Web theme plugin with Latte, Frappé, Macchiato, and Mocha palettes plus optional glass effects.
  - Install: `dsh plugin --profile web add @nonamelego/dsh-catppuccin`

- [DSH Multi-Pet Companions](https://github.com/zhu1090093659/dsh-pet) - **48 stars** | `Apache-2.0`. Display configurable floating pets that respond to model activity with names, feeding, and affinity tracking.
  - Install: `dsh plugin --profile web add @linxin666/dsh-pet@0.4.8`

- [DeepSeek Pet](https://github.com/keleus/deepseek-pet) - **47 stars** | `MIT`. A DSH Web pet plugin with an animated desktop companion and agent activity reactions.
  - Install: `dsh plugin --profile web add github:keleus/deepseek-pet`

- [DSH Pet Remielle](https://github.com/Gin-7/dsh-pet-remielle) - **46 stars** | `MIT`. A DSH Web pet plugin with animated companions, settings controls, and optional desktop presentation modes.
  - Install: `dsh plugin --profile web add dsh-pet-remielle`

- [DSH Bloom Theme](https://github.com/webkubor/dsh-bloom-theme) - **45 stars** | `MIT`. A DeepSeek Harness Web theme bundle with Bloom palettes, configurable appearance settings, and a live client skin.
  - Install: `dsh plugin add @kubor/dsh-bloom-theme`

- [Denia DSH Skin](https://github.com/Ewnscat-ya/dsh-client-ui-skin-denia) - **43 stars** | `CC-BY-NC-SA-4.0`. A DSH Web skin bundle with the Denia visual theme and a configurable client roster entry.
  - Install: `dsh plugin --profile web add ../dsh-client-ui-skin-denia`

- [DSH Cyrene Theme](https://github.com/berhbro/dsh-cyrene-theme) - **43 stars** | `MIT`. Customize DSH with a pink glass theme, editable persona settings, stickers, and rotating backgrounds.
  - Install: `dsh plugin --profile web add dsh-cyrene-theme@0.2.0`

- [DSH Live Theme Editor](https://github.com/oil-oil/dsh-theme) - **43 stars** | `MIT`. Edit DSH interface colors and typography with selectable palettes and live theme controls.
  - Install: `dsh plugin --profile web add github:oil-oil/dsh-theme`

- [DSH Pixel Whale](https://github.com/lhh010/dsh-ui-whale) - **41 stars** | `BSD-3-Clause`. Add a pixel whale companion that reacts to conversation activity in the DSH Web interface.
  - Install: `dsh plugin --profile web add "@dsh-external/dsh-ui-whale@github:lhh010/dsh-ui-whale#v0.3.27"`

- [DSH Chat Wallpaper](https://github.com/LeeRolling/dsh-chat-wallpaper) - **40 stars** | `MIT`. Customize a fullscreen opening video, chat wallpaper, and large text banner in the DSH interface.
  - Install: `dsh plugin --profile web add link:/absolute/path/to/dsh-chat-wallpaper`

- [DSH Kimino Theme](https://github.com/niiang/dsh-kimino-theme) - **40 stars** | `MIT`. A DeepSeek Harness Web theme inspired by Kimi no Na wa with switchable visual styles that restore cleanly when removed.
  - Install: `dsh plugin --profile web add dsh-kimino-theme`

- [DSH NekoWhale Stickers](https://github.com/Loping151/dsh-nekowhale-stickers) - **40 stars** | `Apache-2.0 AND CC-BY-NC-4.0`. Search character stickers and render local meme templates through DSH tools.
  - Install: `dsh plugin --profile web add dsh-nekowhale-stickers@1.1.0`

- [DSH Startup Screen](https://github.com/6shenhonghong9/dsh-startup-screen) - **40 stars** | `MIT`. Add a startup animation with interactive authorization screens, sound effects, and configurable identity text.
  - Install: `dsh plugin --profile web add https://github.com/6shenhonghong9/dsh-startup-screen/releases/download/v1.1.0/dsh-startup-screen-1.1.0.tgz`

- [DSH Whale Girl Live2D](https://github.com/Andersen216/dsh-whale-girl-live2d) - **39 stars** | `MIT`. Add a Live2D companion that reacts to agent activity and sends messages to DSH 0.2 conversations.
  - Install: `dsh plugin --profile web add github:Andersen216/dsh-whale-girl-live2d`

- [DSH Maid Whale UI](https://github.com/yunxiiQwQ/dsh-maid-whale-UI) - **38 stars** | `BSD-3-Clause`. Apply a whale-maid theme to DSH Web or Desktop with an optional Windows companion.
  - Install: `cd maid-whale-webui && pnpm install --frozen-lockfile && pnpm build && dsh plugin --profile web add .`

- [DSH Splash Animation](https://github.com/KDDKBD/DeepSeek-splash-animation) - **38 stars** | `MIT`. Play a startup video with a fade transition and configurable video selection in DSH settings.
  - Install: `dsh plugin --profile web add github:KDDKBD/DeepSeek-splash-animation`

- [Custom DSH UI](https://github.com/yoli-mi/dsh-client-ui-custom) - **37 stars** | `MIT`. Customize wallpaper, colors, translucent panels, and keyboard shortcuts in DSH Web.
  - Install: `dsh plugin --profile web add git+https://github.com/yoli-mi/dsh-client-ui-custom.git`

- [DSH OpenCode Palette](https://github.com/FeatherHunter/dsh-opencode-palette) - **36 stars** | `MIT`. A DeepSeek Harness Web bundle that adds 38 OpenCode-inspired color themes with one-click switching.
  - Install: `dsh plugin --profile web add dsh-opencode-palette`

- [DSH Video Skin](https://github.com/Something11235/dsh-video-skin) - **36 stars** | `MIT`. Apply looping video backgrounds and a skippable startup video with adjustable transparency.
  - Install: `dsh plugin --profile plugindev add link:/absolute/path/to/dsh-video-skin`

- [DSH Any Background](https://github.com/Tkingxiao/dsh-any-background) - **35 stars** | `MIT`. A DeepSeek Harness Web appearance bundle for theme colors, image or video wallpapers, and per-surface opacity and blur.
  - Install: `dsh plugin --profile web add dsh-any-background`

- [DSH Live2D Pet](https://github.com/A8Chann/dsh-pet-live2d) - **35 stars** | `MIT; bundled model CC-BY-NC-SA-4.0; Live2D terms`. Add a draggable Live2D pet with cursor tracking, character interactions, outfits, and reactions to DSH session events.
  - Install: `dsh plugin --profile web add dsh-pet-live2d`

- [DSH Boot Animation Pro](https://github.com/Yiheng-guo/dsh-boot-animation-pro) - **34 stars** | `BSD-3-Clause`. Configure startup videos with playback controls, session triggers, clip libraries, overlay effects, and time-based selection.
  - Install: `dsh plugin --profile web add github:Yiheng-guo/dsh-boot-animation-pro`

- [DSH UI Skin Theme](https://github.com/chouxiaohuai/dsh-uiskin-theme) - **33 stars** | `No standard license`. A DeepSeek Harness Web bundle that adds an ocean-themed interface, light and dark switching, and live thinking-time display.
  - Install: `dsh plugin --profile web add github:chouxiaohuai/dsh-uiskin-theme#main`

- [DSH Whale Galgame](https://github.com/JAdpp/dsh-whale-galgame) - **33 stars** | `SEE LICENSE IN LICENSE.md`. Add a multi-character visual novel interface and an optional desktop companion to DSH Web.
  - Install: `dsh plugin --profile web add dsh-whale-galgame`

- [DSH Piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - **31 stars** | `MIT`. Raise a virtual pig in the DSH interface with feeding, growth, jobs, travel, and optional game expansions.
  - Install: `dsh plugin --profile web add dsh-piggy@0.37.0`

- [DSH Firefly Theme](https://github.com/Liu-ZA-81/dsh-theme-firefly) - **30 stars** | `MIT`. Apply a Firefly character wallpaper, green interface accents, and a launch animation to DSH.
  - Install: `dsh plugin --profile web add dsh-theme-firefly`

- [DSH Live2D Pets](https://github.com/cyanfish-x/dsh-live2d-pets) - **30 stars** | `MIT; model and Live2D terms apply`. Add a Live2D companion with session-state reactions, selectable personas, and support for user-supplied models.
  - Install: `dsh plugin --profile web add dsh-live2d-pets`

- [DSH QQ2006 Skin](https://github.com/LaplaceYoung/dsh-qq2006) - **30 stars** | `MIT`. Apply a classic QQ2006-inspired blue-frame interface to DeepSeek Harness.
  - Install: `dsh plugin --profile web add https://github.com/LaplaceYoung/dsh-qq2006`

- [DSH Terraria Theme](https://github.com/10086ggqq/dsh_theme_terraria) - **30 stars** | `MIT`. Apply a Terraria-inspired pixel interface and desktop skin to the DSH Web interface.
  - Install: `dsh plugin --profile web add github:10086ggqq/dsh_theme_terraria`

- [DSH Wallpaper Share](https://github.com/YRN-playmaker/dsh-wallpaper_share) - **30 stars** | `GPL-3.0`. A DeepSeek Harness bundle that synchronizes Wallpaper Engine scenes and exposes the current wallpaper to DSH workflows.
  - Install: `dsh plugin --profile web add dsh-wallpaper_share`

- [DSH Whale Persona](https://github.com/OMGLogic/dsh-whale-persona) - **30 stars** | `MIT`. Toggle and edit a shared whale-character persona across DSH conversations.
  - Install: `dsh plugin --profile web add github:OMGLogic/dsh-whale-persona`

- [DSH Whale Widget Plus](https://github.com/louke6572/dsh-whale-widget-plus) - **30 stars** | `MIT`. Display an animated whale companion with selectable expressions, custom messages, and provider balance indicators.
  - Install: `dsh plugin --profile web add link:/absolute/path/to/dsh-whale-widget-plus`

- [ProjectKaren](https://github.com/2huy4n/ProjectKaren) - **30 stars** | `AGPL-3.0-or-later`. Give a DSH roleplay character sleep schedules, greetings, idle actions, and proactive conversation.
  - Install: `dsh plugin --profile web add git+https://github.com/2huy4n/ProjectKaren#v0.2.4`

- [OpenPets DSH](https://github.com/alvinunreal/openpets) - **0 stars** | `MIT`. Adds an OpenPets desktop companion that reacts to DSH lifecycle events through a local Cordis bundle.
  - Install: `dsh plugin --profile <profile> add @open-pets/dsh`

### UI & Interfaces

- [Archify DSH](https://github.com/tt-a1i/archify) - **73.4k stars** | `MIT`. A DSH skill bundle for generating verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams.
  - Install: `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0`

- [DSH Web UI](https://github.com/zhu1090093659/dsh-web) - **8.1k stars** | `Apache-2.0`. A Web UI bundle with a task board, Git graph, remote access, live statistics, pets, skins, and image tools.
  - Install: `dsh plugin --profile web add @linxin666/dsh-web-all@latest`

- [iPolloWork Design Studio](https://github.com/Devin-AXIS/iPolloWork) - **6.8k stars** | `Custom source-available`. A native DSH Design view for creating and editing visual documents inside the Harness conversation.
  - Install: `dsh plugin --profile web add deepseek-idesign`

- [DSH Market](https://github.com/dsh-market/dsh-market) - **4.8k stars** | `MIT`. A visual DSH plugin market for browsing, searching, installing, updating, and switching community plugins and themes.
  - Install: `dsh plugin --profile web add dshmarket`

- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - **3.9k stars** | `MIT`. A Web UI workbench with file editing, terminal access, Git tools, subagent views, and extension tabs.
  - Install: `dsh plugin --profile web add dsh-better-sidebar`

- [DSH TUI](https://github.com/ccch1mneyyy/dsh-TUI) - **3.7k stars** | `MIT`. A full-screen terminal interface with streaming output, a status line, rollback controls, and context usage indicators.
  - Install: `dsh plugin --profile dsh-tui add @deepseek-harness-tui/dsh-tui`

- [Answer Me with HTML DSH](https://github.com/QingYunA/answer-me-with-html) - **3.3k stars** | `MIT`. Register a bundled skill that creates self-contained HTML explanations with diagrams and formatted mathematics.
  - Install: `dsh plugin --profile web add github:QingYunA/answer-me-with-html`

- [DeepSeek PPT Studio](https://github.com/Devin-AXIS/deepseek-design) - **1.6k stars** | `Custom source-available`. A native DSH conversation view for creating, editing, templating, and exporting presentation slides.
  - Install: `dsh plugin --profile web add deepseek-ippt`

- [DSH Plugin Shop](https://github.com/LivXue/dsh-plugin-shop) - **950 stars** | `Apache-2.0`. A DeepSeek Harness Web bundle for browsing, installing, enabling, and updating community plugins from a settings panel.
  - Install: `dsh plugin --profile web add dsh-plugin-shop@0.8.2`

- [DSH Browser](https://github.com/omdsh-dev/dsh-browser) - **737 stars** | `MIT`. A Chrome side-panel integration with a DSH bridge for reading pages and operating supported browser content.
  - Install: `curl -fsSL https://raw.githubusercontent.com/omdsh-dev/dsh-browser/refs/heads/main/scripts/install.sh | bash`

- [DSH Worktable](https://github.com/Aisland-SJL/dsh-worktable) - **681 stars** | `MIT`. A DSH sidebar worktable for organizing projects, agent windows, terminals, browsers, and task status.
  - Install: `dsh plugin --profile web add "https://github.com/Aisland-SJL/dsh-worktable/releases/latest/download/dsh-worktable.tgz"`

- [Working Activity](https://github.com/ccch1mneyyy/working-activity) - **661 stars** | `MIT`. A live status line that shows model activity, running tools, elapsed time, and turn summaries in DSH.
  - Install: `dsh plugin --profile web add dsh-working-activity`

- [ccteam DSH](https://github.com/firstintent/ccteam) - **618 stars** | `MIT`. Manage cross-harness session trees and conversations through a DSH workbench connected to the ccteam daemon.
  - Install: `dsh plugin --profile web add @ccteam/ccteam-ui`

- [EvalDock DSH Top100](https://github.com/evaldock/dsh-top100) - **495 stars** | `MIT`. Browse, install, and manage EvalDock plugins and skills from a DSH settings panel.
  - Install: `dsh plugin --profile web add @evaldock/dsh-top100-plugin@1.3.14`

- [ThoughtDAG](https://github.com/chenxiachan/thoughtdag) - **495 stars** | `MIT`. An editable conversation graph that lets DSH users choose and shape the context sent with each turn.
  - Install: `dsh plugin --profile web add dsh-thoughtdag`

- [DSH GenUI](https://github.com/omdsh-dev/dsh-genui) - **485 stars** | `MIT`. A DSH rendering plugin for interactive UI components, charts, forms, quizzes, diagrams, and 3D scenes.
  - Install: `dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-genui.git`

- [DSH Synapse](https://github.com/liangmianya/dsh-synapse) - **445 stars** | `MIT`. A DeepSeek Harness bundle that adds a visual synapse workspace for navigating related context and tools.
  - Install: `corepack pnpm dsh plugin --profile web add github:liangmianya/dsh-synapse`

- [DSH iOS](https://github.com/ZSeven-W/dsh-ios) - **308 stars** | `MIT`. An iOS companion bundle for DeepSeek Harness with native mobile controls and a Cordis client bridge.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-ios@latest`

- [DSH Tianshu TUI](https://github.com/huiliyi37/dsh-tianshu-tui) - **284 stars** | `Apache-2.0`. A terminal interface that adds Tianshu workflows, evidence gates, TDD controls, and optional vision modules.
  - Install: `dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui`

- [DSH Visualize](https://github.com/Nagi-ovo/dsh-visualize) - **281 stars** | `BSD-3-Clause`. An inline visualization plugin that renders interactive HTML fragments as sandboxed cards in DSH conversations.
  - Install: `dsh plugin --profile web add github:Nagi-ovo/dsh-visualize`

- [Pilot Harness Bundles](https://github.com/op7418/pilot-harness) - **277 stars** | `MIT`. A suite of separately installable DSH Web bundles for a CodePilot-style theme, workspace file tree, schedule summary, and session-log export.
  - Install: `dsh plugin --profile web add https://github.com/op7418/pilot-harness/releases/latest/download/deepseek-ai-dsh-ui-worktree-0.1.0-rc.5.tgz`

- [DSH Damage Pulse](https://github.com/wssfk12138/dsh-damage-pulse) - **213 stars** | `MIT`. A DSH Web plugin that tracks token usage, account balance, session costs, and peak/off-peak pricing with a whale companion.
  - Install: `dsh plugin --profile web add github:wssfk12138/dsh-damage-pulse`

- [DSH Popout Sidebar](https://github.com/e2mcc/dsh-popout-sidebar) - **209 stars** | `MIT`. A DeepSeek Harness bundle that opens the sidebar as a separate popout panel.
  - Install: `dsh plugin --profile web add github:e2mcc/dsh-popout-sidebar`

- [MobileVC DSH](https://github.com/JayCRL/MobileVC) - **206 stars** | `MIT`. Access live DSH sessions through a mobile interface with Progressive Web App support.
  - Install: `dsh plugin --profile web add github:JayCRL/MobileVC`

- [SeekTTY](https://github.com/Hilbert-beinghappy/seektty) - **197 stars** | `MIT`. A keyboard-first terminal workspace for DeepSeek Harness with session controls, a plugin center, themes, and workflow commands.
  - Install: `dsh plugin --profile tui add https://github.com/Hilbert-beinghappy/seektty/releases/download/v1.2.0/seektty-1.2.0.tgz`

- [EchoCat Skill Panel](https://github.com/VDERR/dsh-echocat-skill-panel) - **196 stars** | `MIT`. Audit skill calls and manage installed skills from the DSH interface.
  - Install: `dsh plugin --profile web add dsh-echocat-skill-panel`

- [GAL View](https://github.com/Ayase34/gal-view) - **193 stars** | `MIT`. A DSH Web conversation view with a Galgame-style layout and an editor for scene elements.
  - Install: `dsh plugin --profile web add github:Ayase34/gal-view#main`

- [DSH Oil Creator](https://github.com/oil-oil/dsh-oil-creator) - **192 stars** | `MIT`. A DeepSeek Harness creative bundle for generating and organizing Oil-style visual content.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-oil-creator`

- [DSH OpenPencil](https://github.com/ZSeven-W/dsh-openpencil) - **180 stars** | `MIT`. An OpenPencil plugin that lets DSH agents preview, inspect, and edit real multi-frame design documents.
  - Install: `pnpm dlx --package=@deepseek-ai/dsh@0.1.0-rc.6 dsh plugin --profile web add @zseven-w/dsh-openpencil@latest`

- [DSH Plugins Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - **169 stars** | `MIT`. A Web plugin market for discovering, installing, updating, and removing community DSH plugins from the settings interface.
  - Install: `dsh plugin --profile web install bradeGithub/DSH-Plugins-Marketplace`

- [DSH Android](https://github.com/ZSeven-W/dsh-android) - **163 stars** | `MIT`. A DeepSeek Harness bundle for controlling Android emulators or USB devices with ADB, live streaming, UI actions, builds, logs, and OCR.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-android@latest`

- [DSH Reasoning Effort](https://github.com/HanaAyane/dsh-reasoning-effort) - **160 stars** | `MIT`. Model and reasoning-effort controls for DSH with a slider, model-advertised levels, and themed selector views.
  - Install: `dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main`

- [DSH Skill & MCP Panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) - **154 stars** | `MIT`. A Web settings panel for managing DSH Skills and MCP servers through profile configuration.
  - Install: `dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.1/dsh-skill-mcp-panel-2.0.1.tgz`

- [CreatPPT DSH](https://github.com/seekskyworld/CreatPPT) - **148 stars** | `Apache-2.0`. Create web presentations in an agent workspace and export editable PowerPoint files.
  - Install: `dsh plugin --profile web add @seekskyworld/creatppt`

- [Fylar Office Editor DSH](https://github.com/FylarOpen/dsh-fylar-office-editor) - **144 stars** | `Custom license (see vendor/office-sdk/legal.txt)`. Open and edit office files inside the DSH Web interface with the Fylar Office SDK.
  - Install: `dsh plugin --profile web add @fylar/dsh-fylar-office-editor`

- [DSH Plugin Hub](https://github.com/dshplugin/dsh-plugin-hub) - **135 stars** | `MIT`. A DeepSeek Harness Web marketplace for browsing, searching, and installing curated community plugins.
  - Install: `dsh plugin --profile web add dsh-plugin`

- [DSH Market Sidebar](https://github.com/2BingLing/dsh-market) - **125 stars** | `MIT`. A DeepSeek Harness sidebar market for discovering, searching, and installing community plugins.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @dsh-market/plugin`

- [DSH Personal Center](https://github.com/PolinniZhong/dsh-personal-center) - **120 stars** | `MIT`. A DeepSeek Harness Web plugin that adds usage and cost views, custom instructions, font settings, a session overview, and desktop-pet skins.
  - Install: `dsh plugin --profile web add github:PolinniZhong/dsh-personal-center`

- [DeepSeek Harness GenUI](https://github.com/pengyue-polaron/deepseek-harness-genui) - **114 stars** | `MIT`. A DSH bundle that lets agents create focused React interfaces for complex tasks and carry user selections into later turns.
  - Install: `dsh plugin --profile web add dsh-plugin-genui`

- [DSH Usage Dock](https://github.com/Aisland-SJL/dsh-usage) - **109 stars** | `MIT`. A DeepSeek Harness Web bundle with a persistent usage dock, balance panel, activity heatmap, and local channel comparison.
  - Install: `dsh plugin --profile web add github:Aisland-SJL/dsh-usage`

- [DSH Web Mobile](https://github.com/mexiaosqwq/dsh-web-mobile) - **105 stars** | `MIT`. A responsive Web UI plugin that adapts the DSH interface for narrow and portrait-oriented screens.
  - Install: `dsh plugin --profile web add github:mexiaosqwq/dsh-web-mobile`

- [DSH Browser Desktop](https://github.com/runzhliu/deepseek-harness-docker) - **104 stars** | `MIT`. Add a visible Chromium desktop and human takeover interface to DSH browser automation.
  - Install: `npm pack ./plugins/dsh-browser-desktop --pack-destination <temporary-directory> && dsh plugin --profile web add <temporary-directory>/runzhliu-dsh-browser-desktop-0.1.4.tgz`

- [Jacky Creator](https://github.com/Jackywxsz/DSH-Creator) - **104 stars** | `MIT`. Adds a content and operations workspace to DSH for drafting, planning, and idea management.
  - Install: `dsh plugin --profile web add jacky-creator`

- [DSH Web UI Market](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - **103 stars** | `MIT`. A Web UI marketplace for browsing the curated DSH catalog and installing or removing plugins from a profile.
  - Install: `dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin`

- [DSH Codex UI](https://github.com/MichengAI/dsh-codex-ui) - **102 stars** | `Apache-2.0`. A Codex-style DSH Web sidebar plugin with workspace navigation, search, conversation controls, and turn navigation.
  - Install: `dsh plugin --profile web add @michengai/dsh-codex-ui@latest --registry=https://registry.npmjs.org/`

- [DSH Strata](https://github.com/jsdvjx/dsh-strata) - **102 stars** | `MIT`. A DeepSeek Harness Web plugin that maps conversations onto a persistent spatial navigation rail.
  - Install: `dsh plugin --profile web add dsh-strata`

- [Tabbit Browser](https://github.com/Tabbit-Browser/dsh-tabbit) - **101 stars** | `MIT`. A DSH bundle that exposes Tabbit Browser skills and host tools through the Web profile.
  - Install: `dsh plugin --profile web add github:Tabbit-Browser/dsh-tabbit`

- [DSH Oil UI](https://github.com/oil-oil/dsh-oil-ui) - **100 stars** | `MIT`. Explore interface design directions, review previews, and refine HTML pages through a native DSH design workflow.
  - Install: `dsh plugin --profile web add github:oil-oil/dsh-oil-ui`

- [DSH Watcher](https://github.com/aa2246740/dsh-watcher) - **98 stars** | `MIT`. A DSH Web plugin that shows live working activity, tool progress, and turn summaries in the conversation interface.
  - Install: `dsh plugin --profile web add github:aa2246740/dsh-watcher`

- [DSH GitHub](https://github.com/PivotStackIntelligence/dsh-github) - **97 stars** | `MIT`. Adds a VS Code-style Git and GitHub repository panel to DeepSeek Harness.
  - Install: `pnpm install && dsh plugin --profile web add .`

- [DSH Orb](https://github.com/mini-yifan/dsh-orb-cordis) - **93 stars** | `MIT`. Add a floating interface and a computer-use agent preset through a Cordis bundle.
  - Install: `pnpm install && pnpm build && pnpm --filter dsh-orb pack && dsh plugin --profile web add ./dsh-orb-0.0.0.tgz`

- [DSH Plugin Hub Console](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - **92 stars** | `MIT`. A DeepSeek Harness Web bundle for viewing installed plugins, toggling profile rows, checking compatibility, and finding installable packages.
  - Install: `dsh plugin --profile web add @noob-stupid/dsh-plugin-console`

- [DSH Status Rotator](https://github.com/01Virex/dsh-status-rotator) - **92 stars** | `MIT`. A DeepSeek Harness bundle that rotates status messages while a task is running.
  - Install: `dsh plugin --profile web add dsh-status-rotator`

- [DSH Talk Map](https://github.com/Tasihi89/dsh-talk-map) - **92 stars** | `MIT`. A DeepSeek Harness Web plugin that lays out sessions on a movable conversation map with digest and fork actions.
  - Install: `dsh plugin --profile web add github:Tasihi89/dsh-talk-map`

- [DSH Archive Manager](https://github.com/MichengAI/dsh-archive-manager) - **86 stars** | `Apache-2.0`. A DSH Web plugin for browsing, restoring, and managing archived sessions with sidebar controls.
  - Install: `dsh plugin --profile web add @michengai/dsh-archive-manager@latest --registry=https://registry.npmjs.org/`

- [DSH Notification](https://github.com/omdsh-dev/dsh-notification) - **85 stars** | `MIT`. Browser desktop notifications for completed DSH turns with outcome toggles and keyword include or exclude rules.
  - Install: `dsh plugin --profile web add https://github.com/omdsh-dev/dsh-notification/archive/refs/tags/v0.1.2.tar.gz`

- [DSH Maze](https://github.com/lamost423/dsh-maze) - **84 stars** | `MIT`. A DSH Web plugin for viewing agent execution timelines, data tracks, deterministic analysis, and multi-session comparisons.
  - Install: `dsh plugin --profile web add dsh-maze`

- [DSH Stock Watch](https://github.com/Awu12277/dsh-stock-watch) - **83 stars** | `MIT`. A Web UI stock monitor with watchlists, groups, intraday and candlestick charts, target prices, and a draggable panel.
  - Install: `dsh plugin --profile web add dsh-stock-watch`

- [OpenMAIC DSH](https://github.com/THU-MAIC/dsh-openmaic) - **83 stars** | `MIT`. A DeepSeek Harness plugin that lets agents generate and render OpenMAIC-style interactive widgets in sandboxed cards.
  - Install: `dsh plugin --profile web add git+https://github.com/THU-MAIC/dsh-openmaic.git`

- [RDSH Agent UI Bundle](https://github.com/jimoto-no-llm/rustdsh) - **83 stars** | `MIT`. Render charts, tables, choices, diffs, and test results inside DSH conversations and return selections to the same session.
  - Install: `dsh plugin --profile web add /absolute/path/to/rustdsh/plugins/rdsh-agent-ui`

- [ZAT DSH Engine](https://github.com/mishibeikejie/zat-dsh-engine) - **79 stars** | `MIT`. A Web UI marketplace for searching, installing, updating, and rolling back community DSH plugins.
  - Install: `dsh plugin --profile web add github:mishibeikejie/zat-dsh-engine`

- [OpenMA DSH TUI](https://github.com/openma-ai/Martty) - **78 stars** | `MIT`. A terminal-native DSH profile with an ACP plugin tree, streamed sessions, themes, overlays, and native TUI rendering.
  - Install: `dsh plugin --profile tui add @openma/deepseek-harness-tui@latest`

- [DSH Raw HTML](https://github.com/plolpl789/dsh-raw-html) - **76 stars** | `MIT`. A DeepSeek Harness Web plugin for rendering controlled HTML, SVG, charts, formulas, and interactive VCP cards.
  - Install: `node <absolute-path-to-dsh-raw-html>/patch/install-all.cjs && dsh plugin --profile web add <absolute-path-to-dsh-raw-html>`

- [DSH Smooth Stream](https://github.com/Laplace-bit/dsh-smooth-stream) - **76 stars** | `MIT`. A DSH Web rendering plugin for smoother streaming output and scrolling across Markdown, code, tables, and tool results.
  - Install: `dsh plugin --profile web add dsh-smooth-stream`

- [DSH Better Display](https://github.com/aa2246740/dsh-better-display) - **74 stars** | `MIT`. A DeepSeek Harness Web bundle that adds improved message rendering, session display controls, and related conversation UI features.
  - Install: `dsh plugin --profile web add github:aa2246740/dsh-better-display`

- [DSH Skills Manager](https://github.com/MichengAI/dsh-skills-manager) - **74 stars** | `Apache-2.0`. A DeepSeek Harness Web plugin for loading, organizing, and safely managing local Agent Skills.
  - Install: `dsh plugin --profile web add @michengai/dsh-skills-manager@latest --registry=https://registry.npmjs.org/`

- [DSH Plugin Store](https://github.com/ZASENJC/dsh-plugins-store) - **69 stars** | `MIT`. A Web plugin that lets users browse, validate, install, update, and remove community DSH plugins after confirmation.
  - Install: `dsh plugin --profile web add npm:dsh-plugins-store`

- [DSH Web Plugin Manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) - **69 stars** | `MIT`. A DSH Web plugin manager with install guards, health checks, rollback, environment controls, and marketplace browsing.
  - Install: `dsh plugin --profile web add dsh-web-plugin-manager@latest`

- [DSH MCP Panel](https://github.com/PerryLink/dsh-mcp-panel) - **68 stars** | `Apache-2.0`. A DeepSeek Harness settings bundle for adding, editing, testing, and monitoring MCP servers.
  - Install: `dsh plugin --profile web add dsh-mcp-panel`

- [DSH Session Manager](https://github.com/dream12347/dsh-session-manager) - **68 stars** | `MIT`. A DSH Web session manager for archived sessions, trash recovery, activity statistics, forking, workspace grouping, and context settings.
  - Install: `dsh plugin --profile web add github:dream12347/dsh-session-manager#v0.2.2`

- [DSH Auto Collapse](https://github.com/a179-sanae/dsh-auto-collapse) - **64 stars** | `MIT`. A DSH Web client plugin that folds tool cards and reasoning blocks into compact summaries.
  - Install: `dsh plugin --profile web add dsh-auto-collapse`

- [Context Editor DSH](https://github.com/jermaine123123/agent-context-editor) - **63 stars** | `MIT`. Adds search, filtering, editing, hiding, restoring, and undo controls for plain-text DSH messages.
  - Install: `dsh plugin --profile <profile> add ./context-editor-deepseek-harness-0.3.0.tgz`

- [MultiVibe DSH Companion](https://github.com/thibautrey/multivibe) - **62 stars** | `Apache-2.0`. Connect DSH to a MultiVibe gateway and display available models and connection status in a sidebar panel.
  - Install: `dsh plugin add https://github.com/thibautrey/multivibe/releases/download/dsh-multivibe-v0.1.0/dsh-multivibe-0.1.0.tgz`

- [DSH Codex Effort Slider](https://github.com/Microqian2th/dsh-codex-effort-slider) - **61 stars** | `MIT`. Adjust Codex reasoning effort from a slider in the DSH conversation interface.
  - Install: `dsh plugin --profile web add link:/absolute/path/to/dsh-codex-effort-slider`

- [DSH Usage Billing](https://github.com/kenz1117/dsh-ui-usage-billing) - **61 stars** | `MIT`. A DeepSeek Harness Web dashboard plugin that aggregates usage, provider pricing, balances, and estimated session costs.
  - Install: `dsh plugin add npm:@kenz1117/dsh-ui-usage-billing@stable`

- [DSH Generative UI](https://github.com/MindLab-Research/dsh-generative-ui) - **58 stars** | `Apache-2.0`. Render agent-authored TSX interfaces inside DSH conversations and a canvas panel.
  - Install: `dsh plugin --profile web add dsh-generative-ui@0.2.0`

- [DSH Thin Plugin Console](https://github.com/vlln/plugin-registry) - **58 stars** | `MIT`. A Web settings panel for installing, inspecting, updating, enabling, and disabling profile plugins without manual patch editing.
  - Install: `dsh plugin --profile web add @vlln/plugin-console@0.1.0`

- [DSH Raw HTML v2](https://github.com/plolpl789/dsh-raw-html-v2) - **55 stars** | `MIT`. A DSH Web bundle that renders raw HTML documents in a sandboxed panel for agent-generated output.
  - Install: `dsh plugin --profile web add <built dsh-raw-html-v2 package path>`

- [CodingNS DSH Workbench](https://github.com/jingyi0605/Codingns4DSH) - **54 stars** | `GPL-3.0-or-later`. Manage projects, coding agents, terminals, and remote access in a dedicated DSH workbench.
  - Install: `dsh plugin --profile web add @jingyi0605/codingns4dsh@0.2.1-beta.15`

- [DSH LLM Hub](https://github.com/webkubor/dsh-llm-hub) - **54 stars** | `MIT`. Add gateway checks, model discovery, provider balance readouts, and model settings to DSH.
  - Install: `dsh plugin --profile web add @dsh-plugins/dsh-llm-hub@1.9.5`

- [Meow Smooth](https://github.com/Phant0Meow/dsh-meow-smooth) - **53 stars** | `MIT`. A DSH notification and mobile UI bundle with smooth streaming views and configurable message presentation.
  - Install: `dsh plugin --profile web add github:Phant0Meow/dsh-meow-smooth`

- [DSH Office Preview](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) - **51 stars** | `AGPL-3.0`. An optional DSH Web bundle that adds DOCX, XLSX, and PPTX previews to DSH Better Sidebar.
  - Install: `dsh plugin --profile web add @huanlin/dsh-plugin-better-sidebar-plugin-office`

- [DSH Session Workbench](https://github.com/PolinniZhong/dsh-session-workbench) - **51 stars** | `MIT`. A DeepSeek Harness Web bundle for searching sessions, browsing full-text results, and inserting cross-session references into the composer.
  - Install: `dsh plugin --profile web add dsh-session-workbench`

- [DSH Gov Portal](https://github.com/ExElectron/dsh-gov-portal) - **50 stars** | `MIT`. A DeepSeek Harness Web UI bundle that provides a government-style portal for sessions, models, permissions, and usage views.
  - Install: `dsh plugin --profile web add link:<absolute-path-to-dsh-gov-portal>`

- [DSH Status Label](https://github.com/alingalingling/ui-status-label) - **49 stars** | `MIT`. Configurable running-turn status text for DSH Web, with a settings row and conversation-status provider.
  - Install: `dsh plugin --profile web add dsh-ui-status-label`

- [DSH Sticky Note](https://github.com/Meredith2328/dsh-sticky-note) - **48 stars** | `MIT`. A DSH Web sidebar note panel for saving ideas, reminders, and TODO items to the local archive.
  - Install: `dsh plugin --profile web add dsh-sticky-note`

- [DSH Sidebar QA](https://github.com/ChenRuoT/dsh-sidebar-qa) - **46 stars** | `MIT`. A DSH Web sidebar plugin for selecting conversation text and opening nested follow-up sessions in a dedicated panel.
  - Install: `dsh plugin --profile web add dsh-sidebar-qa`

- [DSH Emoji](https://github.com/hellodigua/dsh-emoji) - **45 stars** | `MIT`. A DSH Web plugin that renders semantic inline emoji and supports switchable custom emoji packs.
  - Install: `dsh plugin --profile web add dsh-emoji`

- [DSH Open Plugin Market](https://github.com/polang233/dsh-plugin-index) - **45 stars** | `GPL-3.0-only`. Browse and install community plugins through a DSH market focused on recent activity and growth.
  - Install: `dsh plugin --profile web add dsh-open-market@0.2.1`

- [DSH File Review](https://github.com/left0ver/dsh-file-review) - **43 stars** | `MIT`. A DeepSeek Harness Web plugin that reviews files changed during an agent turn and presents the findings in the conversation.
  - Install: `dsh plugin --profile web add dsh-file-review`

- [DSH-Code](https://github.com/UNLINEARITY/dsh-code) - **42 stars** | `MIT`. A terminal coding interface that runs as an out-of-tree DeepSeek Harness bundle with the official agent and tool ecosystem.
  - Install: `dsh plugin --profile cli add dsh-code@1.0.2`

- [DSH IDE](https://github.com/chenw2759-wq/dsh-IDE) - **41 stars** | `BSD-3-Clause`. A DeepSeek Harness IDE suite with a file tree, code editor, diff views, terminal, and SSH workspace plugins for the Web interface.
  - Install: `pnpm install && pnpm --filter ./packages/dsh-aionui-panel build && pnpm --filter ./packages/dsh-ssh build && pnpm --filter ./packages/dsh-easyssh build && dsh plugin --profile web add file:<absolute-path>/packages/dsh-aionui-panel && dsh plugin --profile web add file:<absolute-path>/packages/dsh-ssh && dsh plugin --profile web add file:<absolute-path>/packages/dsh-easyssh`

- [DSH Web UI Suite](https://github.com/CAPTAIN1275/dsh-ui-web) - **40 stars** | `Apache-2.0`. A DSH Web UI suite that bundles task boards, Git views, usage panels, SSH tools, pets, and selectable skins.
  - Install: `dsh plugin --profile web add @captain1275/dsh-web-ui-all`

- [DSH Bottom Info Bar](https://github.com/songoao25/dsh-bottom-info-bar) - **39 stars** | `MIT`. A DeepSeek Harness information bar that shows the active provider and model, live balance, pricing status, and persisted session spending.
  - Install: `dsh plugin --profile web add dsh-bottom-info-bar`

- [DSH Timeline](https://github.com/houyanchao/dsh-timeline) - **39 stars** | `GPL-3.0-or-later`. A DSH Web session timeline with navigation, bookmarks, exports, prompt storage, and quick notes.
  - Install: `dsh plugin --profile web add dsh-timeline`

- [Beyond Simulator DSH](https://github.com/1475505/miliastra-beyond-simulator) - **38 stars** | `GPL-3.0-only`. Edit and preview Miliastra Beyond game interfaces through a DSH simulator plugin.
  - Install: `dsh plugin --profile web add dsh-plugin-beyond-simulator`

- [Whale Craft DSH](https://github.com/yzi1b/whale-craft) - **38 stars** | `MIT`. Let DSH agents explore, build, and chat on Minecraft servers through native game tools.
  - Install: `dsh plugin --profile web add whale_craft@0.2.0-beta.2`

- [DSH BTW Side Questions](https://github.com/MichengAI/dsh-btw) - **37 stars** | `Apache-2.0`. Ask a separate read-only question about the current conversation context in an independent response bubble.
  - Install: `dsh plugin --profile web add @michengai/dsh-btw@1.0.8`

- [DSH Plugins Collection](https://github.com/sjtuszh/dsh-plugins) - **37 stars** | `MIT`. A collection of DeepSeek Harness Web bundles for cost panels, file actions, and related interface utilities.
  - Install: `dsh plugin --profile web add dsh-cost-panel`

- [DSH Better Reasoning Effort](https://github.com/HaoyueQin/dsh-better-reasoning-effort) - **36 stars** | `MIT`. Set reasoning effort levels for third-party models in the DSH Models page.
  - Install: `dsh plugin --profile web add dsh-better-reasoning-effort`

- [DSH Thinking Translation](https://github.com/UncleK/dsh-think-translate) - **36 stars** | `MIT`. Translate displayed reasoning, task cards, and answers through configurable translation providers.
  - Install: `dsh plugin --profile web add dsh-think-translate@1.2.10`

- [fnOS DSH Integration](https://github.com/FNOSP/fnos-dsh) - **36 stars** | `Apache-2.0`. Connect DSH 0.2.0-rc.2 to fnOS themes, authorized NAS folders, file-opening actions, and application windows.
  - Install: `dsh plugin --profile web add @tnnevol/dsh-fnos@0.2.0-rc.2.5`

- [Meow Cache Billing](https://github.com/Phant0Meow/dsh-meow-cachebilling) - **36 stars** | `MIT`. Display estimated input, output, and cache costs beside context usage with configurable rates.
  - Install: `dsh plugin --profile web add github:Phant0Meow/dsh-meow-cachebilling`

- [Oh My DSH Workbench](https://github.com/gulagala001/oh-my-dsh) - **36 stars** | `No standard license; third-party terms apply`. Extend DSH 0.2.1-rc.2 with task management, computer controls, sidebar annotations, themes, memory, and context tools.
  - Install: `dsh plugin --profile web add https://github.com/gulagala001/oh-my-dsh/releases/download/v0.2.1-rc.2.omd.0.18.8/trisoul_x-0.2.1-rc.2.omd.0.18.8.tgz`

- [DSH Context Doctor](https://github.com/Zhenyu98/dsh-context-doctor) - **34 stars** | `BSD-3-Clause`. Audit context token costs, duplicate instructions, skill catalogs, and tool schemas in a DSH panel.
  - Install: `dsh plugin --profile web add "github:Zhenyu98/dsh-context-doctor#main"`

- [DSH Notify Me](https://github.com/chromoany/dsh-notify-me) - **34 stars** | `MIT`. Receive desktop, sound, title-bar, and optional webhook alerts for approvals, questions, and completed replies.
  - Install: `dsh plugin --profile web add dsh-notify-me@1.7.0`

- [DSH Share](https://github.com/hellodigua/dsh-share) - **34 stars** | `MIT`. A DSH plugin for sharing selected conversations and groups as images or Markdown.
  - Install: `dsh plugin --profile web add dsh-share`

- [DSH Workbench](https://github.com/loadingvx/deepseek-harness-workbench-plugin) - **34 stars** | `MIT`. A DeepSeek Harness Web workbench plugin with an editor, file and Git tools, session inspection, and workspace panels.
  - Install: `dsh plugin --profile web add dsh-workbench-plugin@0.1.32`

- [DSH Chat Archive Manager](https://github.com/WSL043/dsh-chat-manager) - **33 stars** | `MIT`. Search archived chats, restore conversations, and manage session deletion through a dedicated DSH interface.
  - Install: `dsh plugin --profile web add dsh-chat-manager@1.5.18`

- [DSH Minigames](https://github.com/lhh010/dsh-minigames) - **33 stars** | `BSD-3-Clause`. A DSH Web bundle that adds a floating mini-games panel without changing the core conversation flow.
  - Install: `dsh plugin --profile web add '@dsh-external/dsh-minigames@github:lhh010/dsh-minigames#v0.3.18'`

- [DSH Toolbox UI](https://github.com/Imzl-zl/dsh-toolbox-ui) - **33 stars** | `MIT`. Manage MCP connections and skills across global and project scopes through a floating DSH toolbox.
  - Install: `dsh plugin --profile web add dsh-toolbox-ui@1.8.2`

- [DSH TUI Front End](https://github.com/dsh-tui/dsh-tui) - **33 stars** | `MIT`. A terminal front end for DeepSeek Harness agents with streaming Markdown, tool-call cards, approvals, and session controls.
  - Install: `dsh plugin --profile tui add @dsh-tui/dsh-tui`

- [HTML Workbench DSH](https://github.com/alienzhou/html-workbench) - **33 stars** | `MIT`. Preview and visually edit agent-generated HTML in the DSH right sidebar.
  - Install: `dsh plugin --profile web add @vibe-x/dsh-html-workbench`

- [DSH GenUI Components](https://github.com/lhuans/dsh-genui) - **32 stars** | `MIT`. Render interactive charts, forms, calculators, and small applications inline with actions returned to the model.
  - Install: `dsh plugin --profile web add dsh-genui@0.3.1`

- [DSH Session Delete](https://github.com/lsz-asd/dsh-plugin-session-delete) - **32 stars** | `MIT`. A DeepSeek Harness Web plugin for deleting sessions with confirmation, running-agent handling, and sidebar refresh.
  - Install: `dsh plugin --profile <profile> add file:C:/path/to/dsh-plugin-session-delete`

- [DSH Feishu](https://github.com/PGZXB/dsh-feishu) - **31 stars** | `MIT`. Control DSH from a Feishu panel with buttons for agent commands.
  - Install: `npx @deepseek-ai/dsh plugin --profile feishu add @dsh-feishu/dsh-feishu@latest --allow-build=protobufjs`

- [DSH Free Models Hub](https://github.com/yu-wenchao/dsh-free-models-hub) - **31 stars** | `MIT`. Browse a model directory and configure providers through a DSH sidebar backed by a self-hosted PHP and SQLite service.
  - Install: `dsh plugin --profile web add dsh-free-models-hub@0.3.1`

- [DSH Chinese Pro](https://github.com/magian1127/deepseek-harness-zh_pro) - **30 stars** | `MIT`. Add interface styling, layout controls, and prompt injection to DeepSeek Harness.
  - Install: `dsh plugin --profile web add deepseek-harness-zh_pro`

- [DSH Effort Slider](https://github.com/yuhub233/dsh-effort-slider) - **30 stars** | `MIT`. Adjust model reasoning effort through a visual slider with orchestration controls and subagent token-rate readouts.
  - Install: `dsh plugin add github:yuhub233/dsh-effort-slider`

- [DSH Gomoku](https://github.com/omdsh-dev/dsh-gomoku) - **30 stars** | `MIT`. Play Gomoku against an agent or watch agents compete through an interactive DSH conversation board.
  - Install: `dsh plugin --profile web add @yejiming/dsh-gomoku@0.0.3`

- [DSH IM Companion](https://github.com/FeatherHunter/dsh-im-companion) - **30 stars** | `MIT`. View assistant availability and move assistants between workspaces through an interface for the DSH IM plugin.
  - Install: `dsh plugin --profile web add dsh-im && dsh plugin --profile web add dsh-im-companion@0.2.25`

- [DSH KLine](https://github.com/FTShare-Lab/dsh_kline) - **30 stars** | `MIT`. A DeepSeek Harness Web bundle for market data, candlestick charts, technical indicators, and FTShare-backed research tools.
  - Install: `dsh plugin --profile web add github:FTShare-Lab/dsh_kline`

- [DSH MCP Studio](https://github.com/functy23/dsh-mcp-studio) - **30 stars** | `MIT`. Manage MCP services and skills, import agent configurations, and access an optional embedded plugin market.
  - Install: `dsh plugin --profile web add dsh-mcp-studio@1.0.6`

- [DSH Motion UI](https://github.com/Scorp1o117/dsh-motion-ui) - **30 stars** | `MIT`. Create interactive components, HTML and SVG canvases, diagrams, and animations inside DSH conversations.
  - Install: `dsh plugin --profile web add dsh-motion-ui@0.8.7`

- [DSH Russian Language](https://github.com/GooDAnDReaDY/dsh-russian-lang) - **30 stars** | `MIT`. Add Russian interface translations, locale overrides, and translation controls to DSH.
  - Install: `dsh plugin --profile web add @goodandready/dsh-russian-lang@0.3.41`

- [DSH Session Notifications](https://github.com/dingyi222666/dsh-session-notification) - **30 stars** | `BSD-3-Clause`. Notify users about completed or failed sessions, questions, and permission requests with configurable sounds.
  - Install: `dsh plugin --profile web add @dingyi222666/dsh-session-notification@0.2.6`

- [DSH Session Trash](https://github.com/xohmai/dsh-session-delete) - **30 stars** | `Apache-2.0`. Search and delete DSH sessions in bulk with a restorable trash area and protection for running sessions.
  - Install: `dsh plugin --profile web add github:xohmai/dsh-session-delete`

- [DSH Sessions Manager](https://github.com/TOBYCAI/dsh-sessions-manager) - **30 stars** | `MIT`. Archive, move, restore, inspect, and manage DSH sessions and workspaces through a dedicated interface.
  - Install: `dsh plugin --profile desktop add github:TOBYCAI/dsh-sessions-manager`

### Vision

- [DSH Shared Image Generation](https://github.com/dataelement/dsh-desktop) - **14.7k stars** | `MIT`. Generate images through OpenAI or Seedream with shared conversation, presentation, and document assets in compatible DSH hosts.
  - Install: `npm pack ./packages/dsh-image-generation --pack-destination /absolute/output/directory && dsh plugin --profile web add /absolute/output/directory/dsh-image-generation-0.1.0.tgz`

- [Modlens](https://github.com/liustack/modlens) - **4.1k stars** | `MIT`. A vision plugin that returns structured OCR, layout, and semantic evidence to text-only DSH models.
  - Install: `dsh plugin --profile web add @liustack/modlens@3.16.6`

- [DSH Vision Router](https://github.com/ysr666/dsh-vision-router) - **1.1k stars** | `MIT`. A vision routing plugin with image questions, grounding, crops, pixel comparison, OCR, and screenshot tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-vision-router`

- [DSH Vision Toolkit](https://github.com/Anionex/dsh-vision-toolkit) - **884 stars** | `MIT`. A native vision bundle for image questions, long-screenshot OCR, UI reconstruction, grounding, and pixel comparison.
  - Install: `dsh plugin --profile web add @anionex/dsh-vision-toolkit`

- [DSH Image Gen](https://github.com/shanliuling/dsh-image-gen) - **513 stars** | `MIT`. A Web plugin that adds image-generation tools and settings to DeepSeek Harness conversations.
  - Install: `dsh plugin --profile web add dsh-image-gen`

- [GeoChat DSH Geometry](https://github.com/tiwe0/GeoChat) - **121 stars** | `Apache-2.0`. Create and manipulate GeoGebra geometry through a dedicated tools and sidebar bundle for DSH 0.2.0-rc.2.
  - Install: `dsh plugin --profile web add https://github.com/tiwe0/GeoChat/releases/download/dsh-plugin-v0.1.5/dsh-geochat-plugin-0.1.5.tgz`

- [BrewReel DSH](https://github.com/Finderchangchang/brewreel) - **114 stars** | `Apache-2.0`. Create vertical promotional videos from storyboard JSON through a DSH video production bundle.
  - Install: `dsh plugin --profile web add dsh-brewreel`

- [DSH ImageGen](https://github.com/dickpy/dsh-imagegen) - **93 stars** | `Apache-2.0`. A DeepSeek Harness image workspace with provider settings, in-chat generation, editing, templates, and an asset gallery.
  - Install: `dsh plugin --profile web add @dickpy/dsh-imagegen`

- [DSH ComfyUI](https://github.com/fandc520/dsh-comfyui) - **89 stars** | `MIT`. A DSH plugin for driving ComfyUI to generate and process images and videos with workflow and asset panels.
  - Install: `dsh plugin --profile web add dsh-comfyui`

- [DSH Vision](https://github.com/oil-oil/dsh-vision) - **89 stars** | `MIT`. Vision tools for DSH that preserve native image input and bridge text-only models to an external vision model.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:oil-oil/dsh-vision`

- [DSH Video Director](https://github.com/chiphoton/DeepSeek-Harness-Video-Director) - **74 stars** | `MIT`. Plan and produce videos with project-scoped multimodal tools inside DeepSeek Harness.
  - Install: `pnpm install --frozen-lockfile && pnpm run build && dsh plugin --profile web add .`

- [DSH Design QA](https://github.com/sunxin-ai/dsh-design-qa) - **44 stars** | `MIT`. A DeepSeek Harness plugin for on-demand image inspection, design-fidelity checks, and a reproducible visual defect benchmark.
  - Install: `dsh plugin --profile web add dsh-design-qa`

- [DSH Stable Diffusion Bridge Guard](https://github.com/savinglighting/dsh-sd-bridge-guard) - **41 stars** | `MIT`. Connect a local Stable Diffusion WebUI to DSH for image generation, editing, and model management.
  - Install: `dsh plugin add link:/absolute/path/to/dsh-sd-bridge-guard`

- [DSH Blender](https://github.com/CheshireJCat/blender) - **39 stars** | `MIT`. Control Blender production tasks, scene reconstruction, validation, and exports through DSH tools.
  - Install: `dsh plugin --profile web add dsh-blender`

- [PictureReader](https://github.com/jing-hy/picturereader) - **36 stars** | `MIT`. A DeepSeek Harness vision bundle for reading and describing information from images.
  - Install: `dsh plugin --profile web add picturereader`

- [Game Material Master](https://github.com/universe-st/dsh-game-material-master) - **33 stars** | `MIT`. Generate character turn videos and extract directional sprite images in a DSH game-asset workbench.
  - Install: `dsh plugin --profile web add dsh-game-material-master`

- [DSH DrawAI](https://github.com/fourzkw/dsh-drawai) - **31 stars** | `MIT`. Edit native draw.io diagrams in a sidebar canvas with agent-assisted changes, layout, and undo controls.
  - Install: `dsh plugin --profile web add dsh-drawai@0.3.2`

- [DSH Image and Video Studio](https://github.com/q253595422/dsh-imagegen-video) - **30 stars** | `Apache-2.0`. Generate images and videos on a shared canvas with asynchronous video jobs, video nodes, and clip stitching.
  - Install: `dsh plugin --profile web add https://github.com/q253595422/dsh-imagegen-video/releases/download/v1.7.6/q253595422-dsh-imagegen-video-1.7.6.tgz`

- [DSH Short Video Studio](https://github.com/fengyungithub/dsh-short-video-studio) - **30 stars** | `Apache-2.0`. Create images, animations, and short-video projects on a DSH canvas backed by a local ComfyUI service.
  - Install: `dsh plugin --profile web add dsh-short-video-studio@1.11.0`

### Workflow & Automation

- [Reactive Resume DSH Plugin](https://github.com/reactive-resume/reactive-resume) - **43.5k stars** | `MIT`. A DeepSeek Harness bundle that connects Reactive Resume to a session for reading, creating, and editing resumes and job applications.
  - Install: `dsh plugin --profile web add dsh-plugin-reactive-resume`

- [Reasonix DSH Subagent](https://github.com/esengine/DeepSeek-Reasonix) - **35.9k stars** | `MIT`. Connect an installed Reasonix agent to DSH 0.2.1-rc.2 through the native ACP subagent provider.
  - Install: `reasonix setup && dsh plugin --profile web add "github:esengine/DeepSeek-Reasonix#path:/integrations/dsh-plugin"`

- [Planning with Files DSH](https://github.com/OthmanAdi/planning-with-files) - **27.3k stars** | `MIT`. Maintain file-based task plans with per-turn reminders, compaction recovery, and completion checks.
  - Install: `cd .dsh/packages/dsh-planning-with-files && npm install --ignore-scripts && npm run build && dsh plugin --profile web add .`

- [Ouroboros](https://github.com/Q00/ouroboros) - **6.1k stars** | `MIT`. A DeepSeek Harness bundle that exposes the Ouroboros spec-first development workflow as native tools and chat commands.
  - Install: `dsh plugin --profile web add "github:Q00/ouroboros#main&path:integrations/dsh-plugin"`

- [LoopX DSH](https://github.com/loopx-project/loopx) - **6.1k stars** | `Apache-2.0`. A DSH plugin for bootstrapping LoopX, running governed same-session workflows, and displaying a local GoalBar.
  - Install: `dsh plugin --profile web add dsh-loopx-plugin`

- [CCG DSH](https://github.com/fengshao1227/ccg-workflow) - **5.9k stars** | `MIT`. Delegate analysis, design, coding, debugging, optimization, review, and testing to role-specific model tools.
  - Install: `dsh plugin --profile web add <path-to-ccg-workflow>/dsh-ccg`

- [SkillHub DSH](https://github.com/iflytek/skillhub) - **5.3k stars** | `Apache-2.0`. Browse, install, upgrade, and remove SkillHub skills through DSH 0.2.0-rc.2 sidebar and conversation tools.
  - Install: `dsh --profile skillhub-test --from-default-profile web --dump-config && dsh plugin --profile skillhub-test add @astron-team/skillhub-dsh@0.2.1 --ignore-scripts`

- [Matt Pocock Chinese Skills DSH](https://github.com/vinvcn/mattpocock-skills-zh-CN) - **4.6k stars** | `MIT`. Register Chinese translations of Matt Pocock development skills with distinct prefixed names.
  - Install: `dsh plugin --profile web add @vinvcn/dsh-mattpocock-skills-zh`

- [DS Bot Team](https://github.com/Fei2411/DS-Bot) - **3.8k stars** | `Apache-2.0`. Run persistent DSH bots with individual contexts, bot-to-bot messages, group chats, and shared task coordination.
  - Install: `dsh plugin --profile web add ds-bot@0.2.2`

- [Treg DSH](https://github.com/superdesigndev/treg) - **3.7k stars** | `Apache-2.0 + additional terms`. A DSH bundle that exposes the Treg tool registry as an optional MCP connector and packaged Skill.
  - Install: `dsh plugin --profile web add github:superdesigndev/treg`

- [Codex Taskboard DSH Integration](https://github.com/chuspeeism/dashi-taskboard) - **3.2k stars** | `Apache-2.0`. A DeepSeek Harness bundle that adds a Taskboard sidebar entry and opens the installed Codex Taskboard runtime.
  - Install: `dsh plugin --profile web add /absolute/path/to/codex-taskboard/integrations/deepseek-harness`

- [OpenBitFun DSH](https://github.com/GCWing/OpenBitFun) - **2.4k stars** | `MIT`. Expose OpenBitFun Agent SDK Host operations as native DeepSeek Harness tools.
  - Install: `dsh plugin --profile web add /absolute/path/to/extensions/dsh-openbitfun`

- [DSH Infinite Gen 4](https://github.com/Minglink/dsh-infinite-gen-4) - **2.1k stars** | `MIT`. A DeepSeek Harness bundle for controlled red-team prompt evaluation with system-prompt injection and a live client status bar.
  - Install: `bash install.sh`

- [DSH Agent Teams](https://github.com/NanmiCoder/dsh-agent-teams) - **1.8k stars** | `MIT`. A team orchestration plugin that adds tools for creating agent groups, assigning work, and tracking shared state.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-agent-teams`

- [DSH IM](https://github.com/xmanrui/dsh-im) - **1.5k stars** | `MIT`. A single DSH settings plugin for connecting Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord, and WhatsApp bots.
  - Install: `dsh plugin --profile web add @xmanrui/dsh-im`

- [Agents Anywhere DSH Bridge](https://github.com/anywhere-labs/Agents-Anywhere) - **1.4k stars** | `MIT`. Connect DSH sessions to Agents Anywhere with connector management and an event-driven session bridge.
  - Install: `dsh plugin --profile desktop add @agents-anywhere/dsh-bridge-next`

- [OMA DSH](https://github.com/first-fluke/oh-my-agent) - **1.3k stars** | `MIT`. Run configured OMA validation hooks around DSH tool calls and turn completion in an initialized OMA project.
  - Install: `dsh plugin --profile web add ./integrations/dsh --ignore-scripts`

- [Aegis](https://github.com/GanyuanRan/Aegis) - **1.3k stars** | `MIT`. A DeepSeek Harness bundle for the Aegis agent's guarded filesystem and skill workflows.
  - Install: `dsh plugin --profile web add github:GanyuanRan/Aegis`

- [Chorus DSH](https://github.com/Chorus-AIDLC/Chorus) - **1.2k stars** | `AGPL-3.0`. A native DeepSeek Harness bundle for Chorus lifecycle automation, prompt behavior, MCP access, and AI-DLC skills.
  - Install: `dsh plugin --profile web add @chorus-aidlc/chorus-dsh -w`

- [AI Novel Writer DSH](https://github.com/EthanYoQ/AI-Novel-Writer) - **1.2k stars** | `MIT`. A DeepSeek Harness bundle for planning, drafting, and revising long-form fiction inside a novel project.
  - Install: `dsh plugin --profile web add @ethanyoq/dsh-ai-novel-writer`

- [AgentRQ DSH Plugin](https://github.com/agentrq/agentrq) - **1.1k stars** | `Apache-2.0`. A DeepSeek Harness plugin that connects AgentRQ task workspaces to supervised sessions and MCP-backed task tools.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @agentrq/dsh-plugin-agentrq`

- [Alibaba Skill-Up DSH](https://github.com/alibaba/skill-up) - **1.1k stars** | `Apache-2.0`. Test and iteratively revise agent skills through the Skill-Up DeepSeek Harness bundle.
  - Install: `cd plugins/dsh-skill-up && npm ci --ignore-scripts && npm pack && dsh plugin --profile web add ./alibaba-dsh-skill-up-0.1.0-alpha.1.tgz`

- [CloudBase DSH](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) - **1.1k stars** | `MIT`. A DSH plugin for building full-stack applications with CloudBase database, storage, authentication, and deployment tools.
  - Install: `dsh plugin --profile web add @cloudbase/dsh-plugin`

- [TongFlow DSH Plugin](https://github.com/tong-io/tongflow) - **1k stars** | `AGPL-3.0-only`. A multimodal workflow studio for generating and reviewing image, audio, video, and 3D assets from saved workflows inside DSH.
  - Install: `dsh plugin --profile web add dsh-tongflow`

- [StudyMate DSH](https://github.com/Miaotofu01/Study-Mate) - **916 stars** | `MIT`. Add learning and question-answering presets, study materials, and progress tracking for math and computer science.
  - Install: `dsh plugin --profile web add @yunmiao/studymate@2.0.1`

- [OpenWrite DSH](https://github.com/LiPu-jpg/Openwrite) - **763 stars** | `Apache-2.0`. An interactive DeepSeek Harness writing suite for planning, drafting, and revising long-form fiction in a Web profile.
  - Install: `dsh plugin --profile web add -w dsh-openwrite@latest`

- [AgentSight DSH](https://github.com/agentic-os-org/ANOLISA) - **658 stars** | `Apache-2.0`. A DeepSeek Harness observability plugin that records and presents agent activity for inspection.
  - Install: `cd src/agentsight/dsh-plugin && pnpm install && pnpm run build && dsh plugin --profile web add .`

- [DSH Redteam Model](https://github.com/SeaOf0/dsh-redteam-model) - **643 stars** | `MIT`. A DSH security-research suite with authorized red-team modes, campaign memory, asset hunting, and managed runtime plugins.
  - Install: `dsh plugin --profile web add github:SeaOf0/dsh-redteam-model`

- [Avernet BCN DSH](https://github.com/inclusionAI/Avernet) - **627 stars** | `Apache-2.0`. Connect DeepSeek Harness to the Avernet Bot Collaboration Network through a dedicated channel bundle.
  - Install: `dsh plugin --profile web add @avernet-plugin/deepseek-harness-channel-bcn`

- [Superdesign DSH](https://github.com/superdesigndev/superdesign-skill) - **610 stars** | `MIT`. A DeepSeek Harness bundle that brings Superdesign's code-aware interface design workflow into an agent session.
  - Install: `dsh plugin --profile <name> add github:superdesigndev/superdesign-skill`

- [ModSearch](https://github.com/liustack/modsearch) - **565 stars** | `MIT`. A DSH web-search plugin that adds search, X search, and focused page reading through the ModSearch engine chain.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/modsearch@latest`

- [DSH Pentest](https://github.com/howmp/dsh-pentest) - **560 stars** | `MIT`. A DSH security workflow plugin that records penetration-test targets, clues, proposals, decisions, and reports in the Web UI.
  - Install: `dsh plugin --profile web add https://github.com/howmp/dsh-pentest/releases/latest/download/dsh-pentest.tar.gz`

- [EasyEDA Agent DSH](https://github.com/zhoushoujianwork/easyeda-agent) - **560 stars** | `MIT`. A DeepSeek Harness bundle that adds EasyEDA Pro schematic and PCB automation through typed tools and an agent skill.
  - Install: `dsh plugin --profile web add "github:zhoushoujianwork/easyeda-agent#<tag>"`

- [DSH Tavern Suite](https://github.com/flizzywine/dsh-tavern) - **541 stars** | `AGPL-3.0-only`. A DeepSeek Harness profile for Tavern workflows with character-card editing, scenario support, and asset extraction.
  - Install: `curl -fsSL https://cdn.jsdelivr.net/gh/flizzywine/dsh-tavern@main/install.sh | DSH_TAVERN_HOST=cli sh`

- [Postiz DSH](https://github.com/gitroomhq/postiz-agent) - **499 stars** | `AGPL-3.0`. Connect DSH to Postiz for channel discovery, posting rules, drafts, scheduling, and publishing.
  - Install: `dsh plugin --profile web add dsh-postiz`

- [DSH Hub Agent Tools](https://github.com/pax-beehive/dsh-hub-cli) - **458 stars** | `MIT`. A DeepSeek Harness bundle that gives agents tools for inspecting, planning, applying, and rolling back reproducible plugin and profile installations.
  - Install: `dsh plugin --profile web add @dsh-plugin-hub/dsh-plugin`

- [DeepSec DSH Security Suite](https://github.com/Unclecheng-li/DeepSec) - **450 stars** | `MIT`. A pair of DSH security bundles for defensive code audits and authorized penetration-testing workflows.
  - Install: `dsh plugin --profile web add ./dsh-plugins/deepsec-shield && dsh plugin --profile web add ./dsh-plugins/deepsec-spear`

- [AnySearch DSH](https://github.com/anysearch-team/anysearch-dsh) - **432 stars** | `MIT`. Web search for DSH with source discovery, vertical search, bounded batch queries, and cleaned page content.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @anysearch/anysearch-dsh`

- [Oh Story DSH](https://github.com/zenstory-ai/oh-story-dsh) - **421 stars** | `MIT`. A DSH plugin for fiction and short-drama production with writing skills, specialist roles, workspace routing, and previews.
  - Install: `dsh plugin --profile web add @oh-story/dsh@0.1.4`

- [DeepWatch DSH](https://github.com/oxbshw/watch-skill) - **409 stars** | `MIT`. Add media perception, retrieval, and outcome-checking tools through the DeepWatch agent bundle.
  - Install: `pip install 'watch-skill[standard,ocr]>=1.4.3' && dsh plugin --profile web add @deepwatch/dsh-bundle`

- [Humanizer RU by Ilyautov](https://github.com/ilyautov/humanizer-ru) - **406 stars** | `MIT`. Register a Russian writing skill that revises common signs of machine-generated prose.
  - Install: `dsh plugin --profile web add humanizer-ru`

- [DSH Plugin Subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - **399 stars** | `MIT`. An OAuth-based provider plugin that connects ChatGPT, Claude, and Grok subscriptions to DSH without separate API keys.
  - Install: `dsh plugin --profile web add dsh-plugin-subscriptions`

- [Harmony Next DSH](https://github.com/linhay/harmony-next.skills) - **355 stars** | `MIT`. A DSH plugin that provides HarmonyOS NEXT development skills and offline reference materials.
  - Install: `dsh plugin --profile demo add github:linhay/harmony-next.skills`

- [DSH Cost Meter](https://github.com/Han-1413141/dsh-cost-meter) - **344 stars** | `MIT`. Session cost tracking for DSH with daily totals, history, budget views, and synchronized model pricing.
  - Install: `dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.3.1`

- [DSH CommandCode Provider](https://github.com/Mars-Sea/dsh-commandcode-provider) - **340 stars** | `MIT`. An LLM provider plugin that adds a live Command Code model catalog, reasoning controls, and a Models-page card to DSH.
  - Install: `dsh plugin --profile web add @mars-sea/dsh-commandcode-provider`

- [DSH Taskboard](https://github.com/shengsheng90/DSH-taskboard) - **330 stars** | `Apache-2.0`. A DeepSeek Harness taskboard bundle for organizing tasks and monitoring workflow progress.
  - Install: `dsh plugin --profile web add -w /absolute/path/to/shengsheng-dsh-taskboard-<version>.tgz`

- [DSH Agent Team GUI](https://github.com/toolclub/dsh-agent-team-gui) - **281 stars** | `MIT`. Persistent multi-model teams for DSH with durable orchestration, DAG workflows, run history, and provider-reported usage.
  - Install: `dsh plugin --profile web add -w github:toolclub/dsh-agent-team-gui#v0.5.0`

- [Jev DSH Decision Engine](https://github.com/Devin-AXIS/jev-dsh-decision) - **272 stars** | `No standard license`. A DeepSeek Harness bundle that adds structured decisions for choosing tools, skills, task owners, and output-quality checks.
  - Install: `git clone https://github.com/Devin-AXIS/jev-dsh-decision.git && dsh plugin --profile web add ./jev-dsh-decision`

- [Market Research Dashboard DSH](https://github.com/theBigGavin/marketingdashboard) - **261 stars** | `MIT`. A DeepSeek Harness bundle that exposes market quotes, sector rankings, futures, news, and money-flow tools through a remote MCP endpoint.
  - Install: `dsh plugin --profile web add github:theBigGavin/marketingdashboard`

- [DSH Agent RP](https://github.com/hewzhew/dsh-agent-rp) - **221 stars** | `MIT`. A DeepSeek Harness roleplay bundle with SillyTavern migration, agent personas, and conversation workflow tools.
  - Install: `npx -p @deepseek-ai/dsh@latest dsh plugin --profile web add github:hewzhew/dsh-agent-rp#main`

- [DSH WorkBuddy Connect](https://github.com/corrinehu/dsh-workbuddy-connect) - **218 stars** | `MIT`. A DeepSeek Harness provider plugin that connects the models available in the WorkBuddy desktop app without separate model configuration.
  - Install: `dsh plugin --profile web add dsh-workbuddy-connect`

- [DSH Trading Terminal](https://github.com/zhu1090093659/dsh-trading) - **216 stars** | `PolyForm Noncommercial 1.0.0`. An agent-native trading terminal for DeepSeek Harness with market data connectors, research roles, chart context, and approval-gated execution.
  - Install: `dsh plugin --profile trading-web add @dshtrading/base @dshtrading/crypto @dshtrading/us @dshtrading/cn @dshtrading/hk`

- [DSH Auto Review](https://github.com/PerryLink/dsh-auto-review) - **211 stars** | `Apache-2.0`. A read-only reviewer subagent that returns structured allow or deny verdicts for DSH approval requests and fails closed by default.
  - Install: `dsh plugin --profile web add dsh-auto-review`

- [pi2dsh](https://github.com/weijiafu14/pi2dsh) - **206 stars** | `MIT`. A DeepSeek Harness bundle that brings the pi coding agent's workflow and tools into DSH.
  - Install: `dsh plugin --profile web add pi2dsh`

- [TokenLedger](https://github.com/zh667/TokenLedger) - **202 stars** | `MIT`. A DeepSeek Harness bundle for tracking token usage and recording session cost data.
  - Install: `dsh plugin --profile web add "github:zh667/TokenLedger"`

- [Jev DSH](https://github.com/luobosibing2/dsh-jev-plugin) - **201 stars** | `MIT`. Add Jev agent supervision, shared findings, interjections, and approval controls for DSH 0.1.7-rc.2.
  - Install: `pnpm install --frozen-lockfile --ignore-scripts && pnpm run build && mkdir -p dist && pnpm -C packages/jev pack --pack-destination ../../dist && dsh --profile jev --from-default-profile web --dump-default-config && dsh plugin --profile jev add ./dist/dsh-jev-plugin-0.1.0.tgz`

- [SandBase Skills DSH](https://github.com/sandbaseai/sandbase-skills) - **201 stars** | `Apache-2.0`. Install SandBase agent skills into DeepSeek Harness projects through a dedicated bundle.
  - Install: `dsh plugin --profile web add github:sandbaseai/sandbase-skills`

- [DSH Evolve Modes](https://github.com/GraySilver/dsh-evolve-modes) - **199 stars** | `MIT`. A DSH Web plugin for composing agent modes, quality gates, and self-evolution rules from the conversation input area.
  - Install: `dsh plugin --profile web add https://github.com/GraySilver/dsh-evolve-modes/releases/download/v0.3.1/graysilver-dsh-evolve-modes-0.3.1.tgz`

- [DSH Data Agent](https://github.com/omdsh-dev/dsh-data-agent) - **198 stars** | `MIT`. Database connections, masked forms, SQL tools, and a shared data-analysis preset for DSH Web and TUI.
  - Install: `dsh plugin --profile web add @yejiming/dsh-data-agent`

- [DSH Model Router](https://github.com/Alice-Marx/dsh-model-router) - **198 stars** | `MIT`. Plan dependent tasks, compare model costs, and route work through configured model APIs or supported coding-agent CLIs.
  - Install: `dsh plugin --profile web add @ljwei-stak/dsh-model-router@0.22.2`

- [DSH Capsule](https://github.com/whDonline/dsh-capsule) - **195 stars** | `MIT`. A DeepSeek Harness capability-guard bundle for observing and governing sandbox escalation leases, managed capabilities, and audit events.
  - Install: `git clone https://github.com/whDonline/dsh-capsule.git && dsh plugin --profile web add ./dsh-capsule/adapter`

- [AgentDescent DSH](https://github.com/Birfy/agentdescent) - **182 stars** | `MIT`. Run parallel improvement tasks for skills, prompts, agent definitions, and code through an AgentDescent DSH bundle.
  - Install: `pip install "agentdescent[mcp]" && dsh plugin --profile web add link:/absolute/path/to/agentdescent/integrations/dsh-agentdescent`

- [DSH Bridge](https://github.com/wenbin-wb/dsh-bridge) - **177 stars** | `MIT`. A DSH remote-access bridge for QR connections, tunnels, mobile clients, and chat-bot channels.
  - Install: `dsh plugin --profile web add @wenbin_wb/dsh-bridge@2.6.1`

- [Anime Find](https://github.com/cocofhu/anime-find) - **173 stars** | `MIT`. A DSH Web search plugin that gathers anime results into cards with metadata, resource links, and optional streaming views.
  - Install: `dsh plugin --profile web add github:cocofhu/anime-find`

- [DSH Agent Workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) - **173 stars** | `MIT`. A Web UI plugin that presents model requests, responses, and tool calls as a navigable workflow for each DSH conversation.
  - Install: `dsh plugin --profile web add github:xuanyuanzhifeng/dsh-plugin-agent-workflow#v0.1.0 --workspace-root`

- [DSH Reverse Skill](https://github.com/dhicoc/dsh-reverse-skill) - **173 stars** | `MIT`. A DeepSeek Harness bundle for reverse-engineering software behavior into reusable development skills.
  - Install: `dsh plugin --profile web add github:dhicoc/dsh-reverse-skill`

- [Lowtide DSH](https://github.com/KelaoHu/dsh-lowtide) - **170 stars** | `MIT`. A DeepSeek Harness plugin that schedules model work around configured prices and availability with semi-automatic or full-automatic runs.
  - Install: `dsh plugin --profile web add https://github.com/KelaoHu/dsh-lowtide/releases/latest/download/dsh-lowtide.tgz`

- [DSH Usage Stats](https://github.com/Ychris12138/dsh-usage-stats) - **168 stars** | `MIT`. A DSH Web dashboard for token usage, provider balances, subscription quotas, and historical activity.
  - Install: `dsh plugin --profile web add github:Ychris12138/dsh-usage-stats`

- [DSH Plugin Bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - **165 stars** | `MIT`. A session migration plugin that previews a bounded handoff to another preset while leaving the original session unchanged.
  - Install: `dsh plugin --profile web add dsh-plugin-bridge`

- [DSH Super Injector](https://github.com/yjh051108/dsh-super-injector) - **165 stars** | `BSD-3-Clause`. A DSH development plugin for injecting, hot-reloading, and removing local plugin packages without a restart.
  - Install: `dsh plugin --profile web add github:yjh051108/dsh-super-injector`

- [DSH Auto Mode](https://github.com/NanmiCoder/dsh-auto-mode) - **164 stars** | `MIT`. A fail-closed permission policy plugin that classifies DSH tool calls before automatic execution.
  - Install: `dsh plugin --profile web add @nanmicoder/dsh-auto-mode`

- [DSH Council](https://github.com/a1exsun/dsh-council) - **158 stars** | `MIT`. A multi-model deliberation bundle for running bounded councils inside DeepSeek Harness sessions.
  - Install: `npx -p @deepseek-ai/dsh@latest dsh plugin --profile web add @a1exsun/dsh-council@0.1.0`

- [DSH Plugin Finder](https://github.com/awesome-dsh-plugin/dsh-find-plugin) - **154 stars** | `MIT`. Searches GitHub's DSH plugin ecosystem from inside a session and returns ranked results with ready-to-run install commands.
  - Install: `dsh plugin --profile web add dsh-find-plugin`

- [DSH Remote Web Gateway](https://github.com/summer1238/dsh-remote-web-gateway) - **154 stars** | `MIT`. A DSH Web plugin for phone and tablet access with QR pairing, per-device authorization, revocation, and a Cloudflare Quick Tunnel.
  - Install: `dsh plugin --profile web add dsh-remote-web-gateway`

- [Argo DSH](https://github.com/taxueseek/argo) - **153 stars** | `MIT`. A DSH profile bundle that mounts Argo search MCP tools and an evidence-oriented research workflow.
  - Install: `dsh plugin --profile web add "github:taxueseek/argo#main&path:packages/dsh-plugin"`

- [DSH Crew](https://github.com/ZSeven-W/dsh-crew) - **153 stars** | `MIT`. A DSH hub for dispatching work to native subagents, tracking progress, and bridging Claude Code or Codex workers.
  - Install: `dsh plugin --profile web add @zseven-w/dsh-crew@latest`

- [DSH Preset Plus](https://github.com/Rain-kl/dsh-preset-plus) - **146 stars** | `MIT`. Adds a scoped preset mode that injects configurable preset context into DSH requests.
  - Install: `dsh plugin --profile web add @rain-kl/dsh-preset-plus`

- [Volcengine Ark DSH Plugins](https://github.com/volcengine/ark-cli) - **138 stars** | `Apache-2.0`. A pair of DeepSeek Harness bundles for Volcengine Ark model routes and cloud Managed Agents.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add @volcengine/ark-plan-api && npx -y @deepseek-ai/dsh plugin --profile web add @volcengine/ark-managed-agents`

- [DSH SEV](https://github.com/Buzzso/dsh-sev) - **137 stars** | `MIT`. A DeepSeek Harness plugin for managing a headless DSH server through SSH tunnels, remote session controls, and a browser interface.
  - Install: `dsh plugin --profile web add dsh-sev`

- [DSH Wish Specializer](https://github.com/WestFox-AwA/dsh-wish-specializer) - **131 stars** | `BSD-3-Clause`. Add task requirements, intent checks, and a Wish preset before submitting work to a DSH agent.
  - Install: `dsh --profile po061 --from-default-profile web --dump-config && dsh plugin --profile po061 add https://github.com/WestFox-AwA/dsh-wish-specializer/releases/download/v0.9.0-beta-1/dsh-external-dsh-wish-specializer-0.9.0-beta-1.tgz`

- [DSH Workflow](https://github.com/omdsh-dev/dsh_workflow) - **131 stars** | `MIT`. A reusable DSH workflow layer for multi-agent runs with saved plans, approvals, background jobs, and resumable execution.
  - Install: `dsh plugin --profile web add github:dsh-external/dsh_workflow#main`

- [Consensus Pipeline DSH](https://github.com/fangqian616/consensus-pipeline) - **125 stars** | `MIT`. A DeepSeek Harness plugin for multi-agent research pipelines with department debates, progress updates, and report previews.
  - Install: `npx -p @deepseek-ai/dsh dsh plugin --profile web add file:./consensus-pipeline/dsh-plugin`

- [Baro DSH](https://github.com/jigjoy-ai/baro) - **124 stars** | `MIT`. Delegate multi-story tasks to Baro subagents with independent review and a live run panel.
  - Install: `dsh plugin --profile web add baro-dsh`

- [DSH Codex Connect](https://github.com/franksong2702/dsh-codex-connect) - **124 stars** | `MIT`. A DSH integration for using Codex models and image generation through ChatGPT OAuth.
  - Install: `dsh plugin --profile web add dsh-codex-connect@alpha`

- [Russian Marketplace DSH](https://github.com/Vladimir-Human/ru-marketplace-mcp) - **122 stars** | `MIT`. A DeepSeek Harness bundle that exposes Russian software marketplaces through searchable MCP tools and local skill retrieval.
  - Install: `dsh plugin --profile web add github:Vladimir-Human/ru-marketplace-mcp#path:/dsh`

- [DSH Auto Continue](https://github.com/HsiangNianian/dsh-auto-continue) - **120 stars** | `MIT`. A DeepSeek Harness bundle that automatically continues a task after an interaction reaches its limit.
  - Install: `dsh plugin --profile web add dsh-client-auto-continue`

- [DSH XD Pool](https://github.com/XDTrees/dsh-xdpool) - **119 stars** | `MIT`. Combine model providers and WorkBuddy accounts in a shared DSH pool with routing, failover, and usage controls.
  - Install: `dsh plugin --profile desktop add dsh-xdpool@2.2.1`

- [Odai DSH Plugin](https://github.com/orziz/odai) - **118 stars** | `MIT`. A profile-wide DSH governance and routing bundle with an embedded Odai skill and runtime.
  - Install: `dsh plugin --profile web add odai-dsh-plugin`

- [DSH LikeTavern](https://github.com/Amakurai/dsh-liketavern) - **112 stars** | `MIT`. A DeepSeek Harness roleplay frontend with character cards, prompt presets, lorebooks, personas, long-term memory, and rollback support.
  - Install: `dsh plugin --profile web add github:Amakurai/dsh-liketavern`

- [DSH QQ Bot](https://github.com/tencent-connect/dsh-qqbot) - **112 stars** | `MIT`. A QQ Bot channel for DSH that handles messaging, QR-code login, session events, and agent replies.
  - Install: `npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot`

- [DSH Unrestricted Mode](https://github.com/yexi-by/dsh-unrestricted) - **111 stars** | `MIT`. Toggle execution-rule additions across supported agent presets and subagent prompts.
  - Install: `dsh plugin --profile web add github:yexi-by/dsh-unrestricted#v0.2.1`

- [DSH Bili Whale](https://github.com/Alterssss/dsh-bili-whale) - **110 stars** | `MIT`. Schedule Bilibili video reviews, maintain reading diaries, and manage comment replies through a DSH settings panel.
  - Install: `dsh plugin --profile desktop add link:/absolute/path/to/dsh-bili-whale`

- [Run2Skill](https://github.com/qkycir-123/dsh-run2skill) - **109 stars** | `MIT`. A DSH Web bundle that turns successful sessions into reusable, reviewable Agent Skills.
  - Install: `dsh plugin --profile web add dsh-run2skill@0.3.1`

- [SBTD DSH](https://github.com/KunoLu/sbtd-plugins) - **108 stars** | `Apache-2.0`. Run planning and development workflows through the SBTD DeepSeek Harness bundle.
  - Install: `dsh plugin --profile web add @kunolu/dsh-sbtd@next`

- [DSH Auth In One](https://github.com/Stormycry-cryp/dsh-AuthInOne) - **104 stars** | `MIT`. A DeepSeek Harness authentication bundle that manages common sign-in and profile setup flows.
  - Install: `dsh plugin --profile web add github:Stormycry-cryp/dsh-AuthInOne#v0.2.0-alpha.4`

- [DSH Codex Subscription](https://github.com/WSL043/dsh-codex-subscription) - **102 stars** | `MIT`. A DSH bundle for connecting ChatGPT and Codex subscriptions with OAuth, model access, usage, search, and image tools.
  - Install: `dsh plugin --profile web add dsh-codex-subscription`

- [JevCore DSH](https://github.com/PerryLink/jevcore) - **102 stars** | `Apache-2.0`. Expose Jev reasoning tools and a Cordis service with an offline mock provider by default.
  - Install: `dsh plugin --profile web add jevcore-dsh`

- [DSH Automation](https://github.com/titanwings/dsh-automation) - **101 stars** | `MIT`. Scheduled coding runs for DSH with Web and agent controls, durable history, and guarded execution boundaries.
  - Install: `dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.6`

- [OpenCLI MCP DSH](https://github.com/jackwener/opencli-mcp) - **99 stars** | `Apache-2.0`. Connect Chrome-backed OpenCLI browser automation and optional site adapters to DSH.
  - Install: `npx opencli-mcp setup --clients none && dsh plugin --profile web add opencli-mcp`

- [DSH Rewind](https://github.com/SiriLee/dsh-rewind) - **98 stars** | `MIT`. A DeepSeek Harness bundle for rewinding conversation turns and restoring the associated workspace changes.
  - Install: `dsh plugin --profile web add dsh-rewind-plugin`

- [Superpowers DSH](https://github.com/LayneChai/superpowers-dsh) - **95 stars** | `MIT`. A DeepSeek Harness bundle that packages the Superpowers development workflow as native DSH skills.
  - Install: `dsh plugin --profile web add github:LayneChai/superpowers-dsh`

- [ARC DSH](https://github.com/tririver/arc) - **94 stars** | `MIT`. Load the ARC agent workflow into a dedicated DeepSeek Harness profile.
  - Install: `dsh plugin --profile arc add github:tririver/arc`

- [OpenCode2DSH](https://github.com/FishBottle7/opencode2dsh) - **92 stars** | `MIT`. A DeepSeek Harness bundle that connects OpenCode Zen models through a native llm-pi-ai adapter without an API key.
  - Install: `dsh plugin --profile web add @opencode2dsh/dsh-plugin`

- [DSH Speak Up](https://github.com/Yuuyuko-uu/dsh-speak-up) - **89 stars** | `MIT`. Start occasional DSH conversation turns during idle periods with configurable timing and local probability checks.
  - Install: `dsh plugin --profile desktop add github:Yuuyuko-uu/dsh-speak-up`

- [MattSkillsDeck DSH](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - **88 stars** | `MIT`. A DSH bundle that packages Matt Pocock's skills as an agent skill deck with a Web settings panel.
  - Install: `dsh plugin --profile web add dsh-mattpocock-skills-deck`

- [DSH AGY Link](https://github.com/amlyczz/dsh-agy-link) - **87 stars** | `MIT`. A provider bundle that connects DSH to the Google Antigravity agy CLI with streaming output, model selection, and usage settings.
  - Install: `dsh plugin --profile web add dsh-agy-link`

- [Capability Menu DSH](https://github.com/PKUfudawei/dsh-capability-menu) - **86 stars** | `Apache-2.0`. A DeepSeek Harness bundle that catalogs tools and skills and controls their resident, on-demand, or blocked exposure.
  - Install: `dsh plugin --profile web add @daweifu/capability-menu`

- [DSH Secure Audit](https://github.com/PensiveFei/dsh-secure-audit) - **85 stars** | `MIT`. A read-only DSH security and compliance plugin for prompt-injection detection, PII redaction, and local configuration audits.
  - Install: `dsh plugin add dsh-secure-audit`

- [Helmd](https://github.com/ADWMC/helm-d) - **85 stars** | `MIT`. A DeepSeek Harness security-analysis bundle with routing, evidence, and tools for Android, Web, Native, Protocol, Malware, and AI-Security work.
  - Install: `dsh plugin --profile web add https://github.com/ADWMC/helm-d/releases/latest/download/helmd.tgz`

- [You.com DSH](https://github.com/youdotcom-oss/agent-skills) - **82 stars** | `MIT`. Add You.com skills, MCP connections, and web search or fetch providers through a DSH bundle.
  - Install: `dsh plugin --profile web add @youdotcom-oss/dsh-plugin`

- [Sealos Skills](https://github.com/labring/sealos-skills) - **81 stars** | `MIT`. A DeepSeek Harness bundle that registers Sealos Cloud deployment, database, object-storage, and canvas skills through the native skill catalog.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add github:labring/sealos-skills`

- [DSH Personal Directive](https://github.com/liucaimao2026/dsh-personal-directive) - **80 stars** | `MIT`. Load repository prompt instructions with a live enable or disable switch in the top bar.
  - Install: `dsh plugin --profile web add github:liucaimao2026/dsh-personal-directive`

- [Dockyard DSH](https://github.com/AITabby/dockyard-dsh) - **79 stars** | `MIT`. A native DSH provider plugin with account pools, OAuth sign-in, model catalogs, quota status, and provider-specific requests.
  - Install: `dsh plugin --profile web add github:AITabby/dockyard-dsh`

- [DSH Approval Gate](https://github.com/moon09300731/dsh-approval-gate) - **79 stars** | `MIT`. A DSH Web plugin that adds approval gates and configurable permission presets for tool execution.
  - Install: `dsh plugin --profile web add dsh-approval-gate`

- [Recruiting Copilot DSH](https://github.com/Viy1204/recruiting-copilot) - **77 stars** | `MIT`. A recruiting workflow bundle with job intake, candidate sourcing, resume review, and a browser panel for DSH.
  - Install: `dsh plugin --profile web add git+https://github.com/Viy1204/recruiting-copilot.git`

- [Custom First Control Prompt](https://github.com/WM-CODER/custom-first-control-prompt) - **75 stars** | `MIT`. A DSH Web plugin for configuring the initial control prompt through a settings panel and profile patch.
  - Install: `dsh plugin --profile web add @wm-coders/dsh-custom-first-control-prompt`

- [DeepSeek Flow](https://github.com/kanghelyu/dsh-deepseek-flow) - **74 stars** | `MIT`. A Markdown-first workflow editor for DSH with a synchronized canvas, Boolean gates, reviewable changes, and AI-assisted workflow maintenance.
  - Install: `dsh plugin --profile web add "github:kanghelyu/dsh-deepseek-flow#main"`

- [DSH Agency Agents](https://github.com/MichengAI/dsh-agency-agents) - **72 stars** | `Apache-2.0`. A DeepSeek Harness bundle with 271 summonable specialist agents for research, engineering, writing, and other tasks.
  - Install: `dsh plugin --profile web add @michengai/dsh-agency-agents@latest --registry=https://registry.npmjs.org/`

- [DSH Harness Wallet](https://github.com/feibi-mochi/deepseek-harness-control-center) - **72 stars** | `MIT`. A DSH Web plugin for account balances, usage tracking, completion alerts, recharge actions, and session controls.
  - Install: `dsh plugin --profile web add deepseek-harness-wallet`

- [ForkProbe DSH](https://github.com/Jayden-X-L/forkprobe) - **72 stars** | `MIT`. A native DSH plugin for comparing Skills on the same task and choosing a winner from a local report.
  - Install: `dsh plugin --profile web add "github:Jayden-X-L/forkprobe"`

- [Gongwen DSH](https://github.com/linhut/gongwen-skill) - **70 stars** | `MIT`. Check and revise Chinese official-document formatting and generate document templates.
  - Install: `dsh plugin --profile web add -w gongwen-skill`

- [Rapid MLX DSH Provider](https://github.com/raullenchai/rapid-mlx-dsh-provider) - **70 stars** | `Apache-2.0`. A DeepSeek Harness provider bundle that connects Rapid-MLX servers and adapts their model context limits for compaction.
  - Install: `dsh plugin --profile web add @raullenchai/dsh-provider`

- [DSH Codex](https://github.com/Yan-Zero/dsh-codex) - **69 stars** | `MIT`. A DSH plugin that brings Codex model access, task controls, and related tools into DeepSeek Harness.
  - Install: `dsh plugin --profile web add dsh-codex`

- [DSH Novel Writer](https://github.com/akira399/dsh-novel-writer) - **68 stars** | `MIT`. A DeepSeek Harness writing suite for planning, drafting, and revising novels with a Web sidebar and project workflow.
  - Install: `dsh plugin --profile web add <latest dsh-novel-writer release tarball path>`

- [SpecFusion](https://github.com/wxkingstar/SpecFusion) - **68 stars** | `MIT`. A DSH plugin for searching enterprise API documentation and returning interface details while the agent writes code.
  - Install: `dsh plugin --profile web add @wxkingstar/specfusion-dsh`

- [DSH Normify](https://github.com/yan-mc/dsh-normify) - **66 stars** | `MIT`. A DeepSeek Harness bundle that enforces architecture rules, bilingual naming, and validation workflows for agent-written projects.
  - Install: `dsh plugin --profile web-desktop add <dsh-normify-directory>`

- [DSH Remote QR](https://github.com/xgone/dsh-remote) - **66 stars** | `MIT`. A DSH Web remote-access plugin with account login, MFA, browser-side workspace selection, and protected WebSocket access.
  - Install: `dsh plugin --profile web add @xgone/dsh-remote@0.1.1`

- [DSH Toy](https://github.com/c3ll256/dsh-toy) - **66 stars** | `BSD-3-Clause`. Safety-bounded DSH control for Buttplug and Intiface devices with optional MonsterParty toy integration.
  - Install: `npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy`

- [DSH RedTeam Mode](https://github.com/Jueze-2019/dsh-redteam-mode) - **65 stars** | `MIT`. Install red-team agent roles, security testing skills, and a persistent operation console.
  - Install: `dsh plugin --profile web add dsh-redteam-mode`

- [DSH Balance Monitor](https://github.com/yxxbc/dsh-balance-plugin) - **64 stars** | `MIT`. Balance monitoring, usage statistics, and third-party plugin management in the DSH Web interface.
  - Install: `dsh plugin --profile web add github:yxxbc/dsh-balance-plugin`

- [DSH Flash Presets](https://github.com/LarryE135/dsh-flash-presets) - **64 stars** | `MIT`. Add Flash-oriented agent presets for DSH 0.2.1 with configured planning, compaction, and delegation policies.
  - Install: `dsh plugin --profile web add dsh-flash-presets@0.2.4`

- [DSH Passwords](https://github.com/slywalker2006/dsh-passwords) - **63 stars** | `GPL-3.0-only`. A DeepSeek Harness gateway plugin for login protection, per-user permissions and quotas, rate limits, audit logs, and automatic HTTPS.
  - Install: `curl -fsSL https://raw.githubusercontent.com/slywalker2006/dsh-passwords/main/install.sh | bash`

- [Morning Star DSH](https://github.com/btspoony/mstar-harness) - **62 stars** | `MIT`. In-process DSH workflow gates that validate status, control dispatch, and expose the Morning Star engine through refusal-aware channels.
  - Install: `dsh plugin --profile web add @mstar-harness/dsh`

- [AgentDebugX DSH](https://github.com/AgentDebugX/AgentDebugX) - **60 stars** | `MIT`. A DSH plugin for diagnosing live and saved Harness trajectories with AgentDebugX.
  - Install: `dsh plugin --profile web add dsh-agentdebugx`

- [DSH Bilibili Reports](https://github.com/c1overzz/dsh-bili-scroll) - **59 stars** | `MIT`. Search Bilibili videos, review subtitles, and write scheduled Markdown reports with optional comment notifications.
  - Install: `dsh plugin --profile web add dsh-bili-scroll@0.1.5`

- [OpenBiliClaw](https://github.com/whiteguo233/dsh-openbiliclaw) - **59 stars** | `BSD-3-Clause`. A DeepSeek Harness bundle for OpenBiliClaw workflows and related content tools.
  - Install: `dsh plugin --profile web add @openbiliclaw/dsh-plugin`

- [DSH All-in-One Suite](https://github.com/whyihaveyou/dsh-suite) - **57 stars** | `MIT`. An all-in-one DSH plugin suite bundling a store, notifications, session export, team board, presets, and themes.
  - Install: `dsh plugin --profile web add @dsh-suite/all`

- [DSH Prompt Market](https://github.com/yi-yezhiqiu/dsh-prompt-market) - **57 stars** | `MIT`. Browse, search, favorite, and insert prompts through a panel beside the DSH conversation composer.
  - Install: `dsh plugin --profile desktop add dsh-prompt-market@0.1.3`

- [Cloader DSH Taskboard](https://github.com/cloader/dsh-taskboard) - **56 stars** | `Apache-2.0`. A DSH Web taskboard with sidebar navigation, task status tracking, and zero-configuration local storage.
  - Install: `dsh plugin --profile web add dsh-taskboard`

- [Contexera Agent Team](https://github.com/Contexera/dsh-agent-team) - **56 stars** | `MIT`. Coordinate persistent agents with shared channels, tasks, notes, and memory across DSH sessions.
  - Install: `dsh plugin --profile web add @contexera/dsh-agent-team@0.2.2`

- [Unity DSH Plugin](https://github.com/opdsh/unity-plugin) - **56 stars** | `MIT`. A DeepSeek Harness bundle for controlling the Unity Editor, creating scenes, attaching scripts, importing assets, and running builds.
  - Install: `dsh plugin --profile <name> add @opdsh/unity-plugin`

- [DSH Lark](https://github.com/omdsh-dev/dsh-lark) - **55 stars** | `BSD-3-Clause`. A Feishu/Lark channel for sending tasks to DSH agents and returning replies, approvals, and cards to chat.
  - Install: `dsh plugin --profile web add dsh-lark-channel@latest`

- [DSH YOLO](https://github.com/hanshanyike/dsh-yolo) - **55 stars** | `MIT`. A DSH assistant that tracks todos, deadlines, milestones, reminders, and cross-session changes in a Web dashboard.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-plugin-yolo@0.5.0`

- [Free AI DSH Providers](https://github.com/AppsGanin/ai-free-vscode) - **55 stars** | `MIT`. Connect browser-authenticated Qwen, DeepSeek, Kimi, and Z.ai accounts as model providers for DSH 0.2.1-rc.2.
  - Install: `dsh plugin --profile web add dsh-plugin-free-ai@0.1.2`

- [DSH Notifier](https://github.com/THEWOLFWALKER/dsh-notifier) - **54 stars** | `MIT`. A notification and remote-approval layer for DSH with one notify API, multiple channel adapters, and optional mobile controls.
  - Install: `dsh plugin add dsh-notifier --profile web`

- [WorkBuddy DSH](https://github.com/Axiaohungry/dsh-llm-workbuddy) - **54 stars** | `MIT`. A DSH Web plugin that connects WorkBuddy model providers and account management to the profile settings interface.
  - Install: `dsh plugin --profile web add @axiaohungry/dsh-llm-workbuddy@latest`

- [DSH with ChatGPT](https://github.com/BeforeWave/dsh-with-chatgpt) - **53 stars** | `MIT`. A DSH plugin that connects ChatGPT reasoning to local coding sessions through a guided setup flow.
  - Install: `dsh plugin --profile web add dsh-with-chatgpt`

- [OpenGuardrails DSH](https://github.com/openguardrails/openguardrails) - **50 stars** | `Apache-2.0`. A DeepSeek Harness bundle that evaluates model-loop steps before and after generation, redacts local secrets, and routes approvals through verdicts.
  - Install: `dsh plugin --profile web add @openguardrails/dsh`

- [AX Feishu Bridge](https://github.com/AX1202/ax-feishu-bridge) - **49 stars** | `MIT`. A Feishu/Lark bridge that lets users chat with Pi or DeepSeek Harness from the same messaging workspace.
  - Install: `dsh plugin --profile web add ax-feishu-bridge --ignore-scripts`

- [DSH Nested Followups](https://github.com/sluminositys/dsh-nested-followups) - **49 stars** | `MIT`. A DSH Web plugin for creating isolated follow-up branches from any answer and continuing them at arbitrary depth.
  - Install: `dsh plugin --profile web add dsh-nested-followups`

- [DSH AGY](https://github.com/chaos-03x/dsh-agy) - **48 stars** | `MIT`. A DeepSeek Harness provider plugin for Google Antigravity OAuth login, model access, and multi-account rotation.
  - Install: `dsh plugin --profile web add dsh-agy`

- [DSH IM Gateway](https://github.com/zhuiyueya/dsh-im-gateway) - **48 stars** | `MIT`. An IM gateway bundle for connecting DSH agents to WeChat, Feishu, Telegram, Discord, and other messaging channels.
  - Install: `dsh plugin --profile web add dsh-im-gateway`

- [IoT Thinking Compression](https://github.com/Roninton/IoT-items-of-thoughts) - **48 stars** | `MIT`. Compress completed model reasoning blocks into labeled thought nodes through the DSH streaming pipeline.
  - Install: `dsh plugin --profile web add /absolute/path/to/IoT-items-of-thoughts/dsh-plugin-iot-thinking`

- [fnOS DSH Apps](https://github.com/tnnevol/fn-os-apps) - **45 stars** | `AGPL-3.0-only`. A suite of fnOS DSH bundles for CodeBuddy, Codex authentication, and fnOS integration in Web profiles.
  - Install: `dsh plugin --profile web add @tnnevol/dsh-codebuddy@rc && dsh plugin --profile web add @tnnevol/dsh-codex-auth@rc && dsh plugin --profile web add @tnnevol/dsh-fnos@rc`

- [DSH Data Quality](https://github.com/PerryLink/dsh-data-quality) - **44 stars** | `Apache-2.0`. A DeepSeek Harness bundle for profiling, cleaning, and verifying CSV, TSV, JSON, and JSONL datasets with stored reports.
  - Install: `dsh plugin --profile web add dsh-data-quality`

- [DSH Doublecheck](https://github.com/PerryLink/dsh-doublecheck) - **44 stars** | `Apache-2.0`. A DeepSeek Harness bundle that adds requirement review, test-evidence gates, adversarial delivery review, and durable handoff reports.
  - Install: `dsh plugin --profile web add dsh-doublecheck`

- [DSH Writing Guard](https://github.com/xmutfyh/dsh-plugin-writing-guard) - **43 stars** | `MIT`. A DeepSeek Harness plugin for scientific writing checks, journal-fit guidance, and deterministic DOCX integrity validation.
  - Install: `dsh plugin add dsh-plugin-writing-guard`

- [DSH Model Fusion](https://github.com/aa2246740/dsh-model-fusion) - **42 stars** | `Apache-2.0`. Pair a lead model for planning and review with a second model for coding through one DSH model entry.
  - Install: `dsh plugin --profile web add dsh-model-fusion@0.2.6`

- [DSH WorkBuddy Connector](https://github.com/dingminhua/dsh-connect-workbuddy) - **42 stars** | `MIT`. A DeepSeek Harness bundle that connects signed-in WorkBuddy accounts as selectable model providers and shows read-only account status.
  - Install: `dsh plugin --profile web add dsh-connect-workbuddy`

- [DSH Lark Bot](https://github.com/PlutoKeating/dsh-lark-bot) - **41 stars** | `AGPL-3.0`. A DSH profile bundle that connects DeepSeek Harness to Feishu and Lark with workspaces, parallel tasks, notifications, and guarded recovery.
  - Install: `dsh plugin --profile dsh-lark add dsh-lark-bot`

- [DSH Persona Library](https://github.com/huaizhuanghub/dsh-persona-dafeiyu) - **41 stars** | `MIT`. Choose built-in personas, import custom personas, and switch the active persona without restarting DSH.
  - Install: `dsh plugin --profile web add dsh-persona-dafeiyu@0.4.1`

- [DSH Plugin Guide](https://github.com/PerryLink/dsh-plugin-guide) - **41 stars** | `Apache-2.0`. A DSH bundle with plugin-development documentation, a scaffolder, a static checker, and a pack verifier.
  - Install: `dsh plugin --profile web add dsh-plugin-guide`

- [DSH PUA Task Controls](https://github.com/MichengAI/dsh-pua) - **41 stars** | `Apache-2.0`. Configure task persistence, personas, acceptance loops, and live task status cards in DSH.
  - Install: `dsh plugin --profile web add @michengai/dsh-pua@1.0.3`

- [DSH Science](https://github.com/biociao/dsh-science) - **41 stars** | `MIT`. A research and remote-compute bundle with experiment tracking, SSH/HPC jobs, evidence artifacts, and a Web settings panel.
  - Install: `dsh plugin --profile web add dsh-science`

- [TapTap Maker DSH](https://github.com/taptap/instant-games-open-mcp) - **41 stars** | `MIT`. Register the TapTap Maker MCP server and install game-building workflow skills in DSH.
  - Install: `dsh plugin --profile web add @taptap/dsh-maker`

- [VibeGuard DSH](https://github.com/majiayu000/vibeguard) - **41 stars** | `MIT`. Forward DSH Bash events to an installed VibeGuard Rust runtime for command policy checks and outcome logging.
  - Install: `dsh plugin --profile demo add @vibeguard-ai/dsh@0.1.0`

- [DSH Lark Link](https://github.com/amlyczz/dsh-lark-link) - **40 stars** | `MIT`. A Feishu/Lark bridge with QR login, multi-agent modes, media exchange, and reusable DSH Web sessions.
  - Install: `dsh plugin --profile web add dsh-lark-link@latest --ignore-scripts`

- [DSH Model Config](https://github.com/MarvekG/deepseek-harness-model-config) - **40 stars** | `MIT`. A DeepSeek Harness Web bundle for custom model endpoints and per-model reasoning and capacity settings.
  - Install: `dsh plugin --profile web add github:MarvekG/deepseek-harness-model-config`

- [DSH Persistent Agent Team](https://github.com/wowyuarm/dsh-agent-team) - **40 stars** | `MIT`. A DeepSeek Harness Web bundle for persistent agent teams with member memory, workspaces, channels, and task threads.
  - Install: `dsh plugin --profile web add @wowyuarm/dsh-agent-team`

- [DSH Qoder Connect](https://github.com/masknull/dsh-qoder-connect) - **40 stars** | `MIT`. Connect Qoder subscription models to DSH 0.2.1 with separate regional credentials, provider cards, and model catalogs.
  - Install: `dsh plugin --profile web add dsh-qoder-connect@0.2.8`

- [DSH Plugin Kit](https://github.com/hyzyn/dsh-plugin-kit) - **39 stars** | `Apache-2.0`. Install a bundle of DSH tools for profiles, prompts, MCP settings, search, and more.
  - Install: `dsh plugin --profile web add @hyzyn/dsh-plugin-kit`

- [DSH Visual Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - **39 stars** | `MIT`. Build and inspect visual agent orchestration workflows inside DeepSeek Harness.
  - Install: `dsh plugin --profile web add "github:GZX2211/dsh-Visual-Workflow#main"`

- [DSH Agent Team](https://github.com/limuyang2/agent-team) - **38 stars** | `MIT`. A DeepSeek Harness plugin for coordinating multi-agent teams with per-agent models, tools, skills, and a shared workspace.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @limuyang2/dsh-agent-team`

- [DSH OpenCode Zen Free Models](https://github.com/jiesou/dsh-opencode-zen-free-provider) - **38 stars** | `MIT`. Register OpenCode Zen free model providers in DSH with configurable model routing.
  - Install: `dsh plugin --profile web add @jiesou/dsh-opencode-zen-free-provider@0.1.28`

- [Logion DSH Plugin](https://github.com/nicolasmelo1/logion) - **38 stars** | `MIT`. A DSH bundle that registers Logion artifact acquisition, inventory, and reconciliation tools in a profile.
  - Install: `dsh plugin --profile <name> add @logionsh/dsh-plugin`

- [DSH Multitask](https://github.com/Senguk520/dsh-multitask) - **37 stars** | `MIT`. Coordinate delegated workers through a focused agent preset with file metadata tools and approval controls.
  - Install: `dsh plugin --profile web add dsh-multitask@1.2.22`

- [DSH Todo Plus](https://github.com/shuxidemosheng/dsh-tool-todo-plus) - **37 stars** | `MIT`. Add priority tags, Markdown checklist rendering, and a floating task panel alongside the built-in todo tool.
  - Install: `dsh plugin --profile web add dsh-tool-todo-plus@0.7.3`

- [DSH Trading](https://github.com/maddogfinance/dsh-trading) - **37 stars** | `MIT`. A DeepSeek Harness trading bundle with market data, analysis tools, risk guards, verdicts, and Web chart support.
  - Install: `export DSH_HOME=~/.dsh-trading && dsh plugin --profile trading add @dsh-trading/bundle`

- [DSH Pentester](https://github.com/fb0sh/dsh-pentester) - **36 stars** | `MIT`. Run a PTES-based penetration testing workflow through a root orchestrator and specialist presets.
  - Install: `dsh plugin --profile web add dsh-pentester@latest`

- [DSH REA Integration](https://github.com/czcdr/dsh-plugin-rea) - **36 stars** | `MIT`. Provision REA, Java, and Ghidra dependencies and connect the REA MCP server to native DSH tools.
  - Install: `dsh plugin --profile web add dsh-plugin-rea@2.0.12`

- [DSH Tavern](https://github.com/chen731215-dev/dsh-tavern) - **36 stars** | `CC-BY-NC-SA-4.0`. A DSH roleplay plugin for managing character cards, worldbooks, presets, and story memories.
  - Install: `dsh plugin add dsh-tavern`

- [DSH Thinking Effort](https://github.com/hytime/dsh-thinking-effort) - **36 stars** | `MIT`. A DeepSeek Harness bundle that adds reasoning-effort settings for models and default effort controls for subagents.
  - Install: `dsh plugin --profile web add @hytime/dsh-thinking-effort`

- [DSH UltraMath](https://github.com/Andiii208/dsh-ultramath) - **36 stars** | `MIT`. Install mathematical modeling agent presets, model references, paper templates, and review scripts.
  - Install: `dsh plugin --profile web add github:Andiii208/dsh-ultramath`

- [DSH Usage Plugin](https://github.com/feiyang-dev/dsh-usage-plugin) - **36 stars** | `MIT`. A DeepSeek Harness bundle for viewing usage statistics and token consumption during sessions.
  - Install: `dsh plugin --profile web add @feiyang666/dsh-usage-plugin`

- [DirectorX](https://github.com/LaplaceYoung/dsh-directorx) - **35 stars** | `Apache-2.0`. Plan video projects on a storyboard canvas and use native DSH tools for media generation, editing, and FFmpeg quality checks.
  - Install: `dsh plugin --profile web add /absolute/path/to/dsh-directorx`

- [DSH Prompt](https://github.com/FeatherHunter/dsh-prompt) - **35 stars** | `MIT`. Insert preset and custom prompt templates into DSH conversations through a prompt toolbox.
  - Install: `dsh plugin --profile web add dsh-prompt@0.4.13`

- [DSH QA Skills](https://github.com/fishzjp/qa-skills) - **35 stars** | `MIT`. Register testing skills for requirements, test planning, automation, regression, and bug analysis.
  - Install: `dsh plugin --profile web add dsh-qa-skills`

- [DSH Recall Plugin](https://github.com/limbo947/dsh-recall-plugin) - **35 stars** | `MIT`. A DeepSeek Harness bundle that returns a conversation to the state captured when a message was sent.
  - Install: `dsh plugin --profile web add dsh-recall-plugin`

- [Tencent SkillHub DSH](https://github.com/Tencent/skillhub) - **35 stars** | `MIT`. Search, install, and manage SkillHub skills from a DeepSeek Harness conversation.
  - Install: `dsh plugin --profile web add github:Tencent/skillhub#path:dsh-plugin`

- [Amadeus for DSH](https://github.com/yyxcnasd/amadeus-for-dsh) - **34 stars** | `MIT`. A DeepSeek Harness Web bundle that adds an Amadeus assistant modeled on Makise Kurisu from Steins;Gate 0.
  - Install: `dsh plugin --profile web add github:yyxcnasd/amadeus-for-dsh`

- [DSH Agent Studio](https://github.com/thissensen/dsh-agent-studio) - **34 stars** | `MIT`. Configure agent prompts, tools, skills, subagents, and fallback models through a visual DSH interface.
  - Install: `dsh plugin --profile web add dsh-agent-studio@0.1.5`

- [DSH Interconnect](https://github.com/Chinesezjc/dsh-interconnect) - **34 stars** | `MIT`. Cross-instance DSH messaging and event handoff with host services, model-facing tools, and shared-token authentication.
  - Install: `dsh plugin --profile web add dsh-interconnect`

- [DSH MCP Connector](https://github.com/duhu2000/dsh-mcp-connector) - **34 stars** | `MIT`. Manage MCP server connections and search tools across active connections in DSH.
  - Install: `dsh plugin --profile web add dsh-mcp-connector`

- [DSH Personal Workbench](https://github.com/Dely0/dsh-personal-workbench) - **34 stars** | `MIT`. Manage a calendar and hierarchical tasks with agent-assisted planning, execution, and reviews.
  - Install: `dsh plugin --profile web add @dely0/dsh-personal-workbench`

- [DSH Save Money](https://github.com/zhu168/dsh-save-money) - **34 stars** | `MIT`. A DeepSeek Harness bundle for tracking model usage and helping reduce unnecessary token spending.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add dsh-save-money`

- [DSH Web Tools](https://github.com/A3Boy/dsh-web-tools) - **34 stars** | `MIT`. Search the web through multiple providers and fetch pages with configurable fallbacks.
  - Install: `dsh plugin --profile web add github:A3Boy/dsh-web-tools`

- [DSH Scheduled Coding Tasks](https://github.com/MichengAI/dsh-automation) - **33 stars** | `Apache-2.0`. Schedule coding tasks in separate DSH sessions and review run history through settings or conversation tools.
  - Install: `dsh plugin --profile web add @michengai/dsh-automation@1.0.5`

- [DSH Vibe Mathematics](https://github.com/ChongCyrus/Vibe-Mathematics) - **33 stars** | `MIT`. Install mathematical problem-solving presets for collaborative reasoning and verification.
  - Install: `dsh plugin --profile web add dsh-vibe-math`

- [Lark Agent Bridge DSH](https://github.com/bihangchi9-creator/lark-agent-bridge) - **33 stars** | `MIT`. A DeepSeek Harness bundle that connects Feishu and Lark chats to isolated local agent workspaces and persistent sessions.
  - Install: `dsh plugin --profile web add link:/path/to/lark-agent-bridge`

- [Marketing Mindset DSH](https://github.com/axelfreeman/marketing-mindset) - **33 stars** | `MIT`. A DSH bundle that adds the Marketing Mindset skill and workflow guidance to a Harness profile.
  - Install: `dsh plugin --profile <name> add github:axelfreeman/marketing-mindset`

- [WorkBuddy to DSH](https://github.com/Ianzhyh/workbuddy-to-dsh) - **33 stars** | `MIT`. Connect WorkBuddy accounts and models to DSH through a local bridge, native adapter, and settings panel.
  - Install: `dsh plugin --profile web add github:Ianzhyh/workbuddy-to-dsh`

- [DSH Decision Review](https://github.com/ninetyhe-90/dsh-decision-review) - **32 stars** | `MIT`. Ask an independent reviewer model for advice while the primary DSH model retains control of decisions.
  - Install: `dsh plugin --profile web add github:ninetyhe-90/dsh-decision-review`

- [DSH Devin Search](https://github.com/mimimaster/dsh-devin-search) - **32 stars** | `MIT`. Add Devin web and code search with account authentication for DSH 0.2.0-rc.2 and 0.2.1-alpha.1 hosts.
  - Install: `dsh plugin --profile web add dsh-devin-search@0.2.9`

- [DSH Godot Skill](https://github.com/akira399/dsh-godot-skill) - **32 stars** | `MIT`. Register a Godot 4 development skill for game scripting, graphics, physics, and export tasks.
  - Install: `dsh plugin --profile web add github:akira399/dsh-godot-skill`

- [DSH AgentRouter Provider](https://github.com/aqiu817/dsh-llm-agentrouter) - **31 stars** | `MIT`. Connect AgentRouter models to DSH with endpoint switching and request compatibility settings.
  - Install: `dsh plugin --profile web add dsh-llm-agentrouter@2.5.0`

- [DSH Claude Provider](https://github.com/MoFeng2223/dsh-claude-provider) - **31 stars** | `MIT`. A DSH provider plugin for connecting Claude models to DeepSeek Harness.
  - Install: `npx @deepseek-ai/dsh plugin --profile web add @mofeng2223/dsh-claude-provider`

- [DSH Flow](https://github.com/rootkiller6788/dsh-flow) - **31 stars** | `MIT`. Inspect requirements, agent teams, conversation links, and task dependencies on one canvas.
  - Install: `dsh plugin --profile web add github:rootkiller6788/dsh-flow`

- [DSH Preset Enhance](https://github.com/bychv/dsh-preset-enhance) - **31 stars** | `MIT`. Import and edit SillyTavern presets, preview prompt messages, and manage tool settings for DSH modes and sessions.
  - Install: `dsh plugin --profile web add dsh-preset-enhance@0.3.4-rc.2`

- [DSH Prompt Hardener](https://github.com/ffyfox/dsh-prompt-hardener) - **31 stars** | `MIT`. Add configurable prompt rules and checks for coding tasks in DSH.
  - Install: `dsh plugin --profile web add dsh-prompt-hardener@0.4.0`

- [DSH QA Workbench](https://github.com/naodeng/dsh-qa) - **31 stars** | `PolyForm-Noncommercial-1.0.0`. Manage requirements, test cases, risks, execution evidence, and QA conversations in a local DSH workbench.
  - Install: `dsh plugin --profile web add dsh-qa@0.7.2`

- [DSH SkillHub](https://github.com/aa2246740/dsh-skillhub) - **31 stars** | `MIT`. Manage local skill visibility and MCP server switches from a DSH settings panel.
  - Install: `dsh plugin --profile web add @aa2246740/dsh-skillhub@1.0.7`

- [Garmin Connect DSH](https://github.com/Likenttt/garmin-connect-plugin-for-dsh) - **31 stars** | `MIT`. Access Garmin Connect activity and health data through a dedicated DSH bundle with browser-based account authentication.
  - Install: `dsh plugin --profile web add dsh-plugin-garmin-connect@0.1.13`

- [Godot Bridge DSH](https://github.com/Smalldy/godot-bridge) - **31 stars** | `MIT`. Launch and control Godot 4 games through native DSH tools and an in-game TCP server.
  - Install: `dsh plugin --profile web add github:Smalldy/godot-bridge`

- [Minecraft Development DSH](https://github.com/sikadi233-hub/minecraft-dev) - **31 stars** | `MIT`. Register Minecraft development skills, build tools, presets, and specialist agents for server plugins and mods.
  - Install: `dsh plugin --profile web add minecraft-dev@0.10.1`

- [Clutch DSH Worktree](https://github.com/Cerbur/clutch-dsh) - **30 stars** | `MIT`. Create and manage Git worktrees through a dedicated DeepSeek Harness bundle.
  - Install: `dsh plugin --profile web add @cerbur/clutch-dsh-worktree`

- [DeepCanary](https://github.com/Oscar-Williams/dsh-deepcanary) - **30 stars** | `MIT`. Track tasks that need attention with a local inbox, grouped notifications, quiet hours, and reminder controls.
  - Install: `dsh plugin --profile web add dsh-deepcanary@0.1.4-rc.1`

- [DSH Advisor](https://github.com/omdsh-dev/dsh-advisor) - **30 stars** | `MIT`. Run an independent reviewer model alongside each DSH session for turn-by-turn feedback and suggested next prompts.
  - Install: `dsh plugin --profile web add dsh-advisor@0.6.0`

- [DSH OriginLab](https://github.com/Fantasality/dsh-origin-plugin) - **30 stars** | `MIT`. Import data and control OriginLab scientific plots through a dedicated DSH bundle and MCP tools.
  - Install: `dsh plugin --profile web add dsh-origin-plugin@2.7.3`

- [DSH Pipeline Kernel](https://github.com/not-big-dog/DSH-pipeline-kernel) - **30 stars** | `MIT`. A DSH workflow bundle with pipeline tools, task routing, scheduled wakeups, and recovery for stalled jobs.
  - Install: `dsh plugin --profile web add .`

- [DSH Plugin Hub Suite](https://github.com/wingsky-1/dsh-plugin-hub) - **30 stars** | `MIT`. Install a suite for LAN access, notifications, provider usage, MCP management, and isolated plugin verification.
  - Install: `dsh plugin --profile web add @wingsky-1/dsh-plugins-all@0.2.10`

- [DSH Search Engine Fallback](https://github.com/MochiNek0/dsh-web-search-free) - **30 stars** | `MIT`. Search and fetch web pages through configurable search providers with engine fallback and API-key rotation.
  - Install: `dsh plugin --profile web add dsh-web-search-free@1.8.0`

- [DSH Skill Hub](https://github.com/cheshireez/dsh-skill-hub) - **30 stars** | `MIT`. Browse, enable, inspect, troubleshoot, and create skills through the DSH settings interface.
  - Install: `dsh plugin --profile web add dsh-skill-hub@0.3.23`

- [DSH Skills Management](https://github.com/weibaohui/skills-management) - **30 stars** | `MIT`. Browse, install, remove, and manage skill visibility across DSH and other coding-agent skill directories.
  - Install: `dsh plugin --profile web add @weibaohui/skills-management@0.9.1 -w`

- [DSH Stock Analysis](https://github.com/Weaxs/stock-analysis-plugin) - **30 stars** | `MIT`. Analyze stocks, screen markets, and backtest strategies through a separately packaged DSH tool and skill bundle.
  - Install: `dsh plugin --profile web add @weaxs/dsh-stock-analysis@0.2.9`

- [DSH Whale Report](https://github.com/SenmuuuuW/dsh-whale-report) - **30 stars** | `MIT`. A DSH reporting plugin that generates daily, weekly, monthly, yearly, or custom-range reports from session event logs.
  - Install: `dsh plugin --profile web add github:SenmuuuuW/dsh-whale-report`

- [Novel Writer DSH](https://github.com/sailoumili/novel-writer) - **30 stars** | `MIT`. Install a novel-writing agent preset with a conductor and specialist subagents.
  - Install: `dsh plugin --profile web add novel-writer`

- [OpenCode Zen DSH Adapter](https://github.com/xiaozhe7772222/dsh-opencode-zen) - **30 stars** | `MIT`. Register an OpenCode Zen model adapter for the DSH 0.1 package family.
  - Install: `dsh plugin --profile web add github:xiaozhe7772222/dsh-opencode-zen`

- [REA DSH Bundle](https://github.com/Fanqi89/dsh-rea) - **30 stars** | `MIT`. Register the REA reverse-engineering server through the built-in DSH MCP client in a separate profile bundle.
  - Install: `dsh plugin --profile web add github:Fanqi89/dsh-rea`

- [Upstash DSH](https://github.com/upstash/skills) - **30 stars** | `MIT`. Register Upstash SDK skills and its local MCP server through a dedicated DSH bundle with managed credentials.
  - Install: `dsh plugin --profile web add github:upstash/skills`

- [DSH Toolbox Suite](https://github.com/HiWhaleW/dsh-toolbox) - **29 stars** | `PolyForm Noncommercial 1.0.0`. A suite of DSH bundles for product research, context switching, plugin preflight checks, and compatibility monitoring.
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
