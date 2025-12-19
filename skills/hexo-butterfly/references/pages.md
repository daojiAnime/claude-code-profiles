# 页面配置

> 来源：https://butterfly.js.org/posts/dc584b87/

## Front-Matter 配置

### 页面 Front-Matter

| 参数 | 必填 | 说明 |
|------|------|------|
| `title` | 是 | 页面标题 |
| `date` | 是 | 创建时间 |
| `type` | 是 | 页面类型（tags/categories/link） |
| `updated` | 否 | 更新时间 |
| `top_img` | 否 | 顶部图片 |
| `comments` | 否 | 开启评论（默认 true） |
| `aside` | 否 | 显示侧边栏（默认 true） |

### 文章 Front-Matter

```yaml
---
title: 文章标题
date: 2024-01-01 12:00:00
updated: 2024-01-02 12:00:00
tags:
  - 标签1
  - 标签2
categories:
  - 分类名
cover: /img/cover.jpg
toc: true
toc_number: true
comments: true
copyright: true
mathjax: false
katex: false
---
```

## 特殊页面

### 标签页

```bash
hexo new page tags
```

配置 `source/tags/index.md`：

```yaml
---
title: 标签
date: 2024-01-01 00:00:00
type: 'tags'
orderby: random
order: 1
---
```

**排序选项：**
- `orderby`: `random`（随机）、`name`（名称）、`length`（数量）
- `order`: `1`（升序）、`-1`（降序）

### 分类页

```bash
hexo new page categories
```

设置 `type: 'categories'`。

### 友情链接页

创建 `source/_data/link.yml`：

```yaml
- class_name: 友链分类
  link_list:
    - name: 网站名称
      link: https://example.com
      avatar: /img/avatar.jpg
      descr: 网站描述
```

页面 Front-Matter 设置 `type: 'link'`。

**随机排序：** 在 Front-Matter 添加 `random: true`

**远程加载：** 添加 `flink_url: https://xxx.json` 使用远程 JSON 数据

### 图库页面

使用 `galleryGroup` 标签外挂：

```markdown
{% galleryGroup '相册名' '描述' '/gallery/album1' /img/cover.jpg %}
```

子页面使用 `gallery` 标签显示图片。

### 说说页面（v5.0+）

创建 `source/_data/shuoshuo.yml` 或使用远程 JSON。

**限制显示：**
```yaml
limit:
  type: date
  value: 2024-06-20
```

或按数量限制：
```yaml
limit:
  type: num
  value: 10
```

## 数据管理

- **本地数据：** 存放于 `source/_data/` 目录
- **远程加载：** Front-Matter 添加 URL 参数
- **格式要求：** 远程数据需为 JSON 格式，结构与本地 YAML 对应

## 其他功能

- **404 页面：** 在配置文件启用并自定义副标题
- **代码高亮：** 可按页面配置展开行为
- **数学渲染：** 按文章开启 MathJax 或 KaTeX
- **版权模块：** 自定义作者署名和许可协议
