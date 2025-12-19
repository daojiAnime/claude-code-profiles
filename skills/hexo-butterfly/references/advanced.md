# 进阶教程

> 来源：https://butterfly.js.org/posts/4073eda/

## 文件存放建议

**不要**在主题的 `source` 文件夹存放个人文件。

**推荐做法：** 在 Hexo 根目录的 `source` 文件夹创建专用文件夹，引用路径为 `/文件夹名称/文件名`。

## 音乐播放器

### 使用 hexo-tag-aplayer

**安装：**
```bash
npm install hexo-tag-aplayer --save
```

**配置 `_config.yml`：**
```yaml
aplayer:
  meting: true
  asset_inject: false
```

**使用 MetingJS：**
```markdown
{% meting "60198" "netease" "playlist" %}
```

**参数说明：**
- 第一个参数：歌曲/歌单 ID
- 第二个参数：平台（netease, tencent, kugou, xiami, baidu）
- 第三个参数：类型（song, playlist, album, artist）

### 全局播放器

在 `_config.butterfly.yml` 中配置：

```yaml
# 注入全局 Aplayer
inject:
  head:
    - <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css">
  bottom:
    - <script src="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.js"></script>
    - <script src="https://cdn.jsdelivr.net/npm/meting@2/dist/Meting.min.js"></script>
```

## 图标系统

### Font Awesome

主题内置 Font Awesome V5，包含 1,588 个免费图标。

**使用：**
```yaml
menu:
  首页: / || fas fa-home
  标签: /tags/ || fas fa-tags
```

**图标查找：** https://fontawesome.com/icons

### iconfont（国内推荐）

**配置步骤：**

1. 在 iconfont.cn 创建项目并选择图标
2. 生成在线链接
3. 在 `_config.butterfly.yml` 配置：

```yaml
inject:
  head:
    - <link rel="stylesheet" href="//at.alicdn.com/t/font_xxx.css">
```

**使用：**
```yaml
menu:
  首页: / || iconfont icon-home
```

## 代码配色

自定义代码高亮配色：

```yaml
highlight_theme: mac

# 自定义配色
highlight_theme_custom:
  light:
    background: '#f6f8fa'
    foreground: '#24292e'
  dark:
    background: '#1e1e1e'
    foreground: '#d4d4d4'
```

## 侧边栏自定义

```yaml
aside:
  card_author:
    enable: true
    description: |
      <p>自定义 HTML 内容</p>
      <a href="https://example.com">链接</a>
```

## 图片压缩推荐

### tinypng（在线）

网址：https://tinypng.com/

支持 PNG 和 JPEG，压缩效果好。

### caesium（桌面软件）

开源免费，支持批量压缩。

下载：https://github.com/Lymphatus/caesium-image-compressor

### imgbot（GitHub 自动化）

自动为仓库中的图片创建压缩 PR。

配置 `.imgbotconfig`：
```json
{
  "schedule": "weekly",
  "ignoredFiles": [
    "*.svg"
  ]
}
```

## 推荐插件

### hexo-abbrlink

生成短链接，替代默认的长路径。

**安装：**
```bash
npm install hexo-abbrlink --save
```

**配置 `_config.yml`：**
```yaml
permalink: posts/:abbrlink.html
abbrlink:
  alg: crc32
  rep: hex
```

### hexo-generator-feed

生成 RSS 订阅源。

**安装：**
```bash
npm install hexo-generator-feed --save
```

**配置：**
```yaml
feed:
  type: atom
  path: atom.xml
  limit: 20
```

### hexo-filter-nofollow

为外部链接添加 `rel="nofollow"`，SEO 优化。

**安装：**
```bash
npm install hexo-filter-nofollow --save
```

**配置：**
```yaml
nofollow:
  enable: true
  field: site
  exclude:
    - 'example.com'
```

### hexo-generator-sitemap

生成网站地图。

**安装：**
```bash
npm install hexo-generator-sitemap --save
```

**配置：**
```yaml
sitemap:
  path: sitemap.xml
  rel: false
```

## PWA 支持

安装 hexo-offline 或 hexo-pwa：

```bash
npm install hexo-offline --save
```

配置 `_config.butterfly.yml`：

```yaml
pwa:
  enable: true
  manifest: /manifest.json
  theme_color: '#49b1f5'
```

## 性能优化

### 图片懒加载

```yaml
lazyload:
  enable: true
  field: site  # site 或 post
  placeholder: /img/loading.gif
  blur: false
```

### 预加载

```yaml
preloader:
  enable: true
  source: 1  # 1: 全部 2: 首页
```

### CDN 加速

```yaml
CDN:
  main_css: /css/index.css
  main: /js/main.js
  utils: /js/utils.js
```

使用外部 CDN：
```yaml
CDN:
  main_css: https://cdn.jsdelivr.net/npm/hexo-theme-butterfly@latest/source/css/index.min.css
```
