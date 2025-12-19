# 常见问题 FAQ

> 来源：https://butterfly.js.org/posts/98d20436/

## 渲染问题

### 页面显示代码而非正常渲染

**原因：** 缺少渲染器

**解决：**
```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

### 代码块渲染异常

**原因：** cheerio 版本不兼容

**解决：** 检查并更新 cheerio 版本

## 配置错误

### 友情链接配置报错

**原因：** `link.yml` 文件格式错误，通常是缩进空格问题

**解决：** 检查 YAML 缩进，确保使用空格而非 Tab

**正确格式：**
```yaml
- class_name: 友链
  link_list:
    - name: 网站名
      link: https://example.com
      avatar: /img/avatar.jpg
      descr: 描述
```

### 升级后运行报错

**原因：** 主题配置文件缺少新增配置项

**解决：**
1. 对比新版 `_config.yml` 与你的 `_config.butterfly.yml`
2. 添加缺失的配置项

## 插件问题

### 字数统计功能失效

**原因：** 缺少 hexo-wordcount 插件

**解决：**
```bash
npm install hexo-wordcount --save
```

### 本地搜索无法使用

**原因：** 缺少搜索插件

**解决：**
```bash
npm install hexo-generator-search --save
```

## 部署问题

### 本地正常但部署后异常

**解决：**
```bash
hexo clean
hexo generate
hexo deploy
```

### 搜索栏位置错误

**解决：** 同上，清理缓存后重新生成

### CSS/JS 资源加载失败

**可能原因：**
1. CDN 配置错误
2. 路径配置问题

**解决：** 检查 `_config.yml` 中的 `url` 和 `root` 配置

## 版本兼容

### Hexo 版本要求

Butterfly 主题需要 **Hexo 4.0+** 版本。

检查版本：
```bash
hexo version
```

升级 Hexo：
```bash
npm update hexo
```

### 升级到 2.0.0 后 gallery 报错

**原因：** gallery 语法变更

**旧写法：**
```markdown
{% gallery %}
/img/1.jpg
/img/2.jpg
{% endgallery %}
```

**新写法：**
```markdown
{% gallery %}
![](/img/1.jpg)
![](/img/2.jpg)
{% endgallery %}
```

## 样式问题

### 图片无法显示

**检查：**
1. 图片路径是否正确
2. 图片文件是否存在
3. 使用绝对路径 `/img/xxx.jpg` 或相对路径

### 字体加载缓慢

**解决：** 使用国内 CDN 或本地字体

```yaml
font:
  global_font_size:
  code_font_size:
  font_family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto
  code_font_family: Consolas, Monaco, "Courier New", monospace
```

## 功能问题

### 评论系统不显示

**检查：**
1. 评论系统配置是否正确
2. 是否在 Front-Matter 中禁用了评论
3. 浏览器控制台是否有错误

### 深色模式不生效

**检查：**
```yaml
darkmode:
  enable: true
  button: true
```

## 调试方法

1. **查看浏览器控制台**：F12 打开开发者工具
2. **清理缓存**：`hexo clean`
3. **检查配置格式**：YAML 语法敏感
4. **对比默认配置**：与主题原始 `_config.yml` 对比
