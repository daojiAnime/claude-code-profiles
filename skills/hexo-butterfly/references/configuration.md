# 主题配置

> 来源：https://butterfly.js.org/posts/4aa8abbe/

## 导航与布局

### 导航菜单

```yaml
menu:
  首页: / || fas fa-home
  归档: /archives/ || fas fa-archive
  标签: /tags/ || fas fa-tags
  分类: /categories/ || fas fa-folder-open
  友链: /link/ || fas fa-link
  关于: /about/ || fas fa-heart
```

### 导航栏设置

```yaml
nav:
  logo: /img/logo.png
  display_title: true
  fixed: true  # 固定导航栏
```

### 侧边栏位置

```yaml
aside:
  enable: true
  position: right  # left 或 right
```

## 代码显示

```yaml
highlight_theme: mac  # darker, pale night, light, ocean, mac, mac-light
code_copy: true
code_lang: true
code_height_limit: 300  # 代码块高度限制
code_word_wrap: false   # 自动换行
```

## 视觉元素

### 头像

```yaml
avatar:
  img: /img/avatar.jpg
  effect: true  # 旋转效果
```

### 顶部图片

```yaml
index_img: /img/index.jpg  # 首页顶图
default_top_img: /img/default.jpg  # 默认顶图
archive_img: /img/archive.jpg
tag_img: /img/tag.jpg
category_img: /img/category.jpg
```

### 文章封面

```yaml
cover:
  index_enable: true
  aside_enable: true
  archives_enable: true
  position: both  # left, right, both
  default_cover:
    - /img/cover1.jpg
    - /img/cover2.jpg
```

### 背景

```yaml
background: url(/img/bg.jpg)
# 或纯色
background: '#f5f5f5'
```

### 页脚

```yaml
footer:
  owner:
    enable: true
    since: 2020
  custom_text: 自定义文本
  copyright: true
```

## 文章功能

### 目录（TOC）

```yaml
toc:
  post: true
  page: false
  number: true
  expand: false
  style_simple: false
  scroll_percent: true
```

### 版权声明

```yaml
post_copyright:
  enable: true
  decode: false
  author_href:
  license: CC BY-NC-SA 4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/
```

### 相关推荐

```yaml
related_post:
  enable: true
  limit: 6
  date_type: created  # created 或 updated
```

### 过期提醒

```yaml
noticeOutdate:
  enable: true
  style: flat  # simple 或 flat
  limit_day: 365
  position: top  # top 或 bottom
  message_prev: 本文最后更新于
  message_next: 天前，内容可能已过时
```

### 文章分页

```yaml
post_pagination: 1  # 1: 上一篇在左 2: 上一篇在右 false: 关闭
```

## 侧边栏模块

```yaml
aside:
  enable: true
  card_author:
    enable: true
    description: 个人简介
    button:
      enable: true
      icon: fab fa-github
      text: Follow
      link: https://github.com/xxx
  card_announcement:
    enable: true
    content: 公告内容
  card_recent_post:
    enable: true
    limit: 5
  card_categories:
    enable: true
    limit: 8
  card_tags:
    enable: true
    limit: 40
  card_archives:
    enable: true
    type: monthly  # monthly 或 yearly
    limit: 8
  card_webinfo:
    enable: true
    post_count: true
    last_push_date: true
```

## 评论系统

```yaml
comments:
  use: Valine  # Disqus, Gitalk, Valine, Waline, Giscus, Twikoo 等
  lazyload: true
  count: true

# Valine 配置示例
valine:
  appId: xxx
  appKey: xxx
  avatar: mp
  serverURLs:
  visitor: true
  option:
```

## 搜索功能

```yaml
local_search:
  enable: true
  preload: false
  CDN:
```

## 统计分析

```yaml
# 百度统计
baidu_analytics: xxx

# Google Analytics
google_analytics: UA-xxx

# 网站运行时间
runtimeshow:
  enable: true
  publish_date: 2020/1/1 00:00:00
```

## 视觉效果

```yaml
# 背景特效
canvas_ribbon:
  enable: false
  size: 150
  alpha: 0.6

canvas_nest:
  enable: false
  color: '0,0,255'

# 点击特效
fireworks:
  enable: false
  zIndex: 9999

click_heart:
  enable: false

# 打字机效果
subtitle:
  enable: true
  effect: true
  sub:
    - 第一行文字
    - 第二行文字
```

## 主题色

```yaml
theme_color:
  enable: true
  main: '#49B1F5'
  paginator: '#00c4b6'
  button_hover: '#FF7242'
  text_selection: '#00c4b6'
  link_color: '#99a9bf'
  hr_color: '#A4D8FA'
  card_bg: '#fff'
  headline_color: '#414141'
```

## 深色模式

```yaml
darkmode:
  enable: true
  button: true
  autoChangeMode: false  # 1: 跟随系统 2: 定时切换
```
