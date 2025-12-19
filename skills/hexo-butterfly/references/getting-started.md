# 快速开始

> 来源：https://butterfly.js.org/posts/21cfbf15/

## 概述

Butterfly 是基于 hexo-theme-melody 的 Hexo 主题，提供简洁的卡片式设计。

## 安装方式

### Git 安装（推荐稳定版）

**GitHub：**
```bash
git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

**Gitee（国内用户）：**
```bash
git clone -b master https://gitee.com/immyw/hexo-theme-butterfly.git themes/butterfly
```

**开发版：**
```bash
git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
```

**升级：** 在主题目录执行 `git pull`

### NPM 安装

适用于 Hexo 5.0.0+：
```bash
npm install hexo-theme-butterfly
```

**注意：** NPM 安装会将文件放在 `node_modules` 而非 `themes` 文件夹。

**升级：** 执行 `npm update hexo-theme-butterfly`

## 配置步骤

### 1. 应用主题

修改 Hexo 根目录 `_config.yml`：
```yaml
theme: butterfly
```

### 2. 安装必要渲染器

```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

## 升级建议

在 Hexo 根目录创建 `_config.butterfly.yml` 文件，将主题 `_config.yml` 内容复制进去。

**优势：**
- 升级主题时保留自定义配置
- 避免文件意外删除
- Hexo 自动合并配置（`_config.butterfly.yml` 优先级更高）

**重要：** 不要删除主题目录内的原始 `_config.yml`。
