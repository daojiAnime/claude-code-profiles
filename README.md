# Claude Code Profiles

[English](#english) | [中文](#中文)

---

## English

A collection of Claude Code configurations, custom commands, and skills for enhanced AI-assisted development.

### Overview

This repository contains reusable profiles for [Claude Code](https://claude.com/claude-code), including:

- **CLAUDE.md** - Global configuration file defining workflows, code standards, and MCP usage guidelines
- **Commands** - Custom slash commands for common development tasks
- **Skills** - Specialized knowledge modules that extend Claude's capabilities

### Structure

```
├── CLAUDE.md           # Global Claude Code configuration
├── commands/           # Custom commands
│   ├── catchup.md      # Review changes in current branch
│   └── pr.md           # Prepare and create pull requests
└── skills/             # Skill modules
    ├── confluence-macros/   # Confluence wiki macros
    ├── file-archiving/      # File organization (Johnny.Decimal)
    ├── hexo-butterfly/      # Hexo Butterfly theme
    ├── nb-log-skill/        # Python nb_log library
    ├── prompter/            # Prompt engineering best practices
    ├── seo-audit/           # SEO audit toolkit
    └── seo-specialist/      # SEO content optimization
```

### Commands

| Command | Description |
|---------|-------------|
| `/catchup` | Read all changed files in current git branch and provide a summary |
| `/pr` | Clean up code, stage changes, and create a pull request |

### Skills

| Skill | Description |
|-------|-------------|
| `confluence-macros` | Confluence wiki macro syntax and storage format |
| `file-archiving` | File organization using Johnny.Decimal system |
| `hexo-butterfly` | Hexo Butterfly theme configuration and customization |
| `nb-log-skill` | Python nb_log logging library usage guide |
| `prompter` | Prompt engineering techniques and best practices |
| `seo-audit` | Website SEO audit and analysis |
| `seo-specialist` | SEO content writing and optimization |

### Usage

1. Clone this repository
2. Copy `CLAUDE.md` to your project root or `~/.claude/CLAUDE.md` for global use
3. Copy desired commands to `~/.claude/commands/`
4. Copy desired skills to `~/.claude/skills/`

### Configuration Highlights

The `CLAUDE.md` configuration includes:

- **Workflow Guidelines** - Structured approach: Intake → Context Gathering → Planning → Execution → Verification → Handoff
- **Code Quality** - Python: ruff + mypy checks mandatory
- **Git Commit Spec** - Emoji-prefixed conventional commits
- **MCP Integration** - Guidelines for Context7, Fetch, and Serena MCP servers

---

## 中文

Claude Code 配置、自定义命令和技能的集合，用于增强 AI 辅助开发。

### 概述

本仓库包含 [Claude Code](https://claude.com/claude-code) 的可复用配置，包括：

- **CLAUDE.md** - 全局配置文件，定义工作流、代码规范和 MCP 使用指南
- **Commands** - 常见开发任务的自定义斜杠命令
- **Skills** - 扩展 Claude 能力的专业知识模块

### 目录结构

```
├── CLAUDE.md           # Claude Code 全局配置
├── commands/           # 自定义命令
│   ├── catchup.md      # 查看当前分支的变更
│   └── pr.md           # 准备并创建 Pull Request
└── skills/             # 技能模块
    ├── confluence-macros/   # Confluence Wiki 宏
    ├── file-archiving/      # 文件归档 (Johnny.Decimal)
    ├── hexo-butterfly/      # Hexo Butterfly 主题
    ├── nb-log-skill/        # Python nb_log 日志库
    ├── prompter/            # 提示词工程最佳实践
    ├── seo-audit/           # SEO 审计工具包
    └── seo-specialist/      # SEO 内容优化
```

### 命令

| 命令 | 描述 |
|------|------|
| `/catchup` | 读取当前 git 分支的所有变更文件并提供摘要 |
| `/pr` | 清理代码、暂存变更并创建 Pull Request |

### 技能

| 技能 | 描述 |
|------|------|
| `confluence-macros` | Confluence Wiki 宏语法和存储格式 |
| `file-archiving` | 使用 Johnny.Decimal 系统进行文件组织 |
| `hexo-butterfly` | Hexo Butterfly 主题配置和自定义 |
| `nb-log-skill` | Python nb_log 高性能日志库使用指南 |
| `prompter` | 提示词工程技术和最佳实践 |
| `seo-audit` | 网站 SEO 审计和分析 |
| `seo-specialist` | SEO 内容写作和优化 |

### 使用方法

1. 克隆本仓库
2. 将 `CLAUDE.md` 复制到项目根目录，或复制到 `~/.claude/CLAUDE.md` 作为全局配置
3. 将所需命令复制到 `~/.claude/commands/`
4. 将所需技能复制到 `~/.claude/skills/`

### 配置亮点

`CLAUDE.md` 配置包含：

- **工作流指南** - 结构化方法：接收 → 上下文收集 → 规划 → 执行 → 验证 → 交付
- **代码质量** - Python：必须通过 ruff + mypy 检查
- **Git 提交规范** - Emoji 前缀的约定式提交
- **MCP 集成** - Context7、Fetch 和 Serena MCP 服务器使用指南

---

## License

[MIT](LICENSE)
