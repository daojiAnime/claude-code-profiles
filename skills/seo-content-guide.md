# SEO 内容写作规范

> 本规范用于指导 DaojiBlog 博客文章的 SEO 优化写作

---

## Front Matter 必填字段

### 1. description (文章摘要)

**要求**：
- 长度：50-160 字符（中文约 50-80 字）
- 包含主关键词
- 能够概括文章核心内容
- 避免与 title 完全重复

**示例**：
```yaml
# ✅ 优秀示例
description: '本文详细介绍 Python 类型检查工具 mypy 的使用方法，包含安装配置、类型注解语法和最佳实践，帮助你编写更健壮的代码。'

# ❌ 不良示例
description: 'Python mypy 教程'
```

### 2. keywords (关键词)

**要求**：
- 数量：3-5 个
- 格式：逗号分隔，使用单引号包裹
- 包含长尾关键词

**示例**：
```yaml
# ✅ 优秀示例
keywords: 'Python类型检查, mypy教程, 类型注解, Python静态分析, 代码质量'

# ❌ 不良示例
keywords: 'Python, 教程, 代码'
```

### 3. cover (封面图)

**要求**：
- 推荐尺寸：1200x630 像素（2:1.05 比例）
- 用于 og:image 社交分享
- 建议使用有意义的图片而非装饰图
- 可使用相对路径或 CDN URL

**示例**：
```yaml
cover: '/assets/images/python-mypy-cover.png'
# 或
cover: 'https://example.com/images/cover.png'
```

---

## 内容结构规范

### 标题层级

| 层级 | 用途 | 数量建议 |
|------|------|----------|
| H1 | 仅用于文章标题（Front Matter 的 title） | 1 个 |
| H2 | 主要章节 | 3-7 个 |
| H3 | 子章节 | 按需使用 |

**注意**：避免跳级（如 H2 直接到 H4）

### 首段优化

- 前 150 字内包含主关键词
- 概述文章要解决的问题
- 吸引读者继续阅读

**示例**：
```markdown
在 Python 开发中，**类型检查**已经成为提升代码质量的重要手段。本文将介绍如何使用 **mypy** 这个强大的静态类型检查工具，帮助你在运行前发现潜在的类型错误...
```

### 图片优化

1. **文件命名**：使用描述性文件名
   - ✅ `python-mypy-type-checking.png`
   - ❌ `image1.png`

2. **Alt 文本**：为图片添加描述
   ```markdown
   ![Python mypy 类型检查示例](image.png)
   ```

3. **图片压缩**：推荐 < 200KB

---

## 关键词策略

### 分类关键词参考

| 分类 | 推荐关键词 |
|------|-----------|
| Python | Python教程, FastAPI, Django, 类型检查, mypy, 数据处理 |
| AI | LLM, RAG, Agent, 大模型, 提示词, MCP |
| 前端 | Vue3, React, TypeScript, CSS, 组件开发 |
| 面试题 | Golang面试, 操作系统, 数据结构, 算法 |
| Linux | Shell脚本, 服务器配置, Docker, 运维 |

### 长尾关键词技巧

1. **问题型**：如何使用 Python mypy 进行类型检查
2. **对比型**：mypy vs pyright 哪个更好
3. **教程型**：Python mypy 完整教程
4. **最佳实践型**：Python 类型注解最佳实践

---

## 内部链接策略

### 相关文章引用

在文章中适当引用相关文章：

```markdown
相关阅读：
- [Python 类型系统详解](/posts/xxxxx.html)
- [FastAPI 项目最佳实践](/posts/xxxxx.html)
```

### 锚文本优化

使用描述性锚文本而非"点击这里"：

```markdown
# ✅ 优秀示例
了解更多关于 [Python 异步编程](/posts/async.html) 的内容

# ❌ 不良示例
[点击这里](/posts/async.html) 了解更多
```

---

## SEO 检查清单

发布前确认以下项目：

- [ ] title 包含主关键词，长度 < 60 字符
- [ ] description 长度 50-160 字符，包含关键词
- [ ] keywords 包含 3-5 个相关关键词
- [ ] 首段 150 字内包含主关键词
- [ ] 使用 H2/H3 组织内容结构
- [ ] 图片添加 alt 描述
- [ ] 内部链接使用描述性锚文本
- [ ] 文章长度 > 500 字（技术文章建议 > 1000 字）

---

## 使用示例

### 完整的 Front Matter 示例

```yaml
---
title: Python mypy 类型检查完整指南：从入门到精通
date: 2025-12-08 10:00:00
updated: 2025-12-08 10:00:00
tags:
  - Python
  - 类型检查
  - mypy
  - 代码质量
categories:
  - Python
  - 开发工具
keywords: 'Python类型检查, mypy教程, 类型注解, Python静态分析, 代码质量工具'
description: '全面介绍 Python mypy 类型检查工具的使用方法，涵盖安装配置、类型注解语法、常见错误处理和项目最佳实践，助你提升 Python 代码质量。'
cover: '/assets/images/python-mypy-guide.png'
toc: true
toc_number: true
comments: true
---
```

---

**最后更新**：2025-12-08
