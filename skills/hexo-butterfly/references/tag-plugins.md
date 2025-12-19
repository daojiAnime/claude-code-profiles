# 标签外挂（Tag Plugins）

> 来源：https://butterfly.js.org/posts/ceeb73f/

标签外挂是 Hexo 独有的功能，可扩展 Markdown 语法。Butterfly 主题提供了丰富的标签外挂。

---

## Note 提示框

Bootstrap 风格的提示框，用于强调重要内容。

**语法：**
```markdown
{% note [class] [no-icon] [style] %}
内容（支持 Markdown）
{% endnote %}
```

| 参数 | 可选值 | 说明 |
|------|--------|------|
| class | `default` `primary` `success` `info` `warning` `danger` | 提示框类型 |
| no-icon | `no-icon` | 不显示图标 |
| style | `simple` `modern` `flat` `disabled` | 样式风格 |

**示例：**
```markdown
{% note info flat %}
这是一条信息提示
{% endnote %}

{% note warning modern %}
这是一条警告提示
{% endnote %}

{% note danger simple %}
这是一条危险提示
{% endnote %}

{% note success no-icon %}
不带图标的成功提示
{% endnote %}
```

**带自定义图标：**
```markdown
{% note info fa-solid fa-lightbulb flat %}
带自定义图标的提示
{% endnote %}
```

---

## Tabs 选项卡

创建可切换的分页内容，适合展示多种实现方式或对比内容。

**语法：**
```markdown
{% tabs 唯一ID [, 默认索引] %}
<!-- tab 标签名[@图标] -->
内容1
<!-- endtab -->
<!-- tab 标签名2[@图标] -->
内容2
<!-- endtab -->
{% endtabs %}
```

| 参数 | 说明 |
|------|------|
| 唯一ID | 选项卡的唯一标识，同一页面不可重复 |
| 默认索引 | 默认显示的选项卡（从1开始），-1 表示不选中任何 |
| @图标 | FontAwesome 图标（可选） |

**示例：**
```markdown
{% tabs 代码示例 %}
<!-- tab Python@fab fa-python -->
```python
print("Hello World")
```
<!-- endtab -->
<!-- tab JavaScript@fab fa-js -->
```javascript
console.log("Hello World")
```
<!-- endtab -->
<!-- tab Go@fas fa-code -->
```go
fmt.Println("Hello World")
```
<!-- endtab -->
{% endtabs %}
```

**指定默认选项卡：**
```markdown
{% tabs test, 2 %}
<!-- tab Tab1 -->
内容1
<!-- endtab -->
<!-- tab Tab2 -->
内容2（默认显示）
<!-- endtab -->
{% endtabs %}
```

---

## Mermaid 图表

支持流程图、时序图、甘特图、状态图、饼图、ER 图等。

**语法：**
```markdown
{% mermaid %}
图表代码
{% endmermaid %}
```

### 流程图
```markdown
{% mermaid %}
graph TD
    A[开始] --> B{条件判断}
    B -->|是| C[执行操作]
    B -->|否| D[跳过]
    C --> E[结束]
    D --> E
{% endmermaid %}
```

### 时序图
```markdown
{% mermaid %}
sequenceDiagram
    participant Client as 客户端
    participant Server as 服务器
    participant DB as 数据库
    Client->>Server: 发送请求
    Server->>DB: 查询数据
    DB-->>Server: 返回结果
    Server-->>Client: 响应数据
{% endmermaid %}
```

### 甘特图
```markdown
{% mermaid %}
gantt
    title 项目计划
    dateFormat  YYYY-MM-DD
    section 开发阶段
    需求分析 :a1, 2024-01-01, 7d
    编码实现 :a2, after a1, 14d
    section 测试阶段
    单元测试 :b1, after a2, 7d
    集成测试 :b2, after b1, 5d
{% endmermaid %}
```

### 类图
```markdown
{% mermaid %}
classDiagram
    class BaseDesensitizer {
        +strategy: MaskStrategy
        +recognize_entities()*
        +mask_text()
        +desensitize()
    }
    class RegexDesensitizer {
        +PATTERNS: dict
        +recognize_entities()
    }
    class NLPDesensitizer {
        +TAG_MAPPING: dict
        +recognize_entities()
    }
    BaseDesensitizer <|-- RegexDesensitizer
    BaseDesensitizer <|-- NLPDesensitizer
{% endmermaid %}
```

### 饼图
```markdown
{% mermaid %}
pie title 技术栈占比
    "Python" : 40
    "JavaScript" : 30
    "Go" : 20
    "其他" : 10
{% endmermaid %}
```

**配置启用：**
```yaml
mermaid:
  enable: true
  code_write: true  # 支持代码块写法
  theme:
    light: default
    dark: dark
```

---

## Gallery 图库

响应式图片画廊，支持 fancybox 灯箱效果。

**本地语法：**
```markdown
{% gallery [lazyload],[rowHeight],[limit] %}
![描述](图片URL)
![描述](图片URL)
{% endgallery %}
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| lazyload | true | 是否懒加载 |
| rowHeight | 220 | 行高度 |
| limit | 10 | 每次加载数量 |

**示例：**
```markdown
{% gallery true,220,10 %}
![图1](/img/1.jpg)
![图2](/img/2.jpg)
![图3](/img/3.jpg)
{% endgallery %}
```

**远程 JSON：**
```markdown
{% gallery url,[link],[lazyload],[rowHeight],[limit] %}
{% endgallery %}
```

---

## Tag-hide 隐藏内容

### 行内隐藏
```markdown
{% hideInline 隐藏内容, 显示文字, 颜色 %}
```

### 块级隐藏
```markdown
{% hideBlock 显示文字, 颜色 %}
隐藏的块级内容
{% endhideBlock %}
```

### 折叠面板（推荐）
```markdown
{% hideToggle 标题, 颜色 %}
可折叠的内容（支持 Markdown）
{% endhideToggle %}
```

**颜色选项：** `default` `blue` `pink` `red` `purple` `orange` `green`

**示例：**
```markdown
这是 {% hideInline 答案是42, 点击查看答案, blue %} 的问题。

{% hideToggle 点击展开详细说明, green %}
这里是详细的说明内容...
支持 **Markdown** 语法
{% endhideToggle %}
```

---

## Button 按钮

**语法：**
```markdown
{% btn [url], [text], [icon], [color] [style] [layout] [position] [size] %}
```

| 参数 | 说明 |
|------|------|
| url | 链接地址 |
| text | 按钮文字 |
| icon | FontAwesome 图标 |
| color | `default` `blue` `pink` `red` `purple` `orange` `green` |
| style | `outline` 镂空样式 |
| layout | `block` 块级 / `line` 行内 |
| size | `larger` 大号 |

**示例：**
```markdown
{% btn https://github.com, GitHub, fab fa-github, blue %}

{% btn https://example.com, 下载文件, fas fa-download, green larger %}

{% btn /, 首页, fas fa-home, purple outline %}
```

---

## Label 行内标签

高亮文字背景色。

**语法：**
```markdown
{% label 文字 颜色 %}
```

**颜色选项：** `default` `blue` `pink` `red` `purple` `orange` `green`

**示例：**
```markdown
这是 {% label 重要 red %} 内容，需要 {% label 特别注意 orange %}。

支持的颜色：{% label default default %} {% label 蓝色 blue %} {% label 粉色 pink %} {% label 红色 red %} {% label 紫色 purple %} {% label 橙色 orange %} {% label 绿色 green %}
```

---

## Timeline 时间线

展示时间序列内容。

**语法：**
```markdown
{% timeline 标题, 颜色 %}
<!-- timeline 时间节点 -->
内容描述（支持 Markdown）
<!-- endtimeline -->
<!-- timeline 时间节点2 -->
内容描述2
<!-- endtimeline -->
{% endtimeline %}
```

**颜色选项：** `default` `blue` `pink` `red` `purple` `orange` `green`

**示例：**
```markdown
{% timeline 项目里程碑, blue %}
<!-- timeline 2024-01-01 -->
**项目启动**
- 完成需求分析
- 确定技术栈
<!-- endtimeline -->
<!-- timeline 2024-03-15 -->
**MVP 版本发布**
- 核心功能实现
- 基础测试通过
<!-- endtimeline -->
{% endtimeline %}
```

---

## InlineImg 行内图片

在文字中插入小图片/表情。

**语法：**
```markdown
{% inlineImg [src] [height] %}
```

**示例：**
```markdown
这是一个表情 {% inlineImg /img/emoji.png 20px %}，很可爱吧！
```

---

## Flink 友链

在任意位置插入友链列表。

**语法：**
```markdown
{% flink %}
- class_name: 分类名
  class_desc: 分类描述
  link_list:
    - name: 网站名
      link: https://example.com
      avatar: /img/avatar.jpg
      descr: 网站描述
{% endflink %}
```

---

## ABCJS 乐谱

渲染 ABC 记谱法。

**语法：**
```markdown
{% score %}
X:1
T:音乐标题
M:4/4
L:1/8
K:C
CDEF GABc|
{% endscore %}
```

**配置：**
```yaml
abcjs:
  enable: true
  per_page: true
```

---

## Series 文章系列

显示同系列文章列表。

**文章 Front-matter：**
```yaml
series: 系列标识
```

**使用：**
```markdown
{% series 系列标识 %}
```

---

## Chartjs 图表

使用 Chart.js 创建各类图表。

**语法：**
```markdown
{% chart [width],[height] %}
{
  "type": "图表类型",
  "data": { ... },
  "options": { ... }
}
{% endchart %}
```

**支持类型：** `bar` `line` `pie` `doughnut` `radar` `polarArea` `bubble` `scatter`

**示例：**
```markdown
{% chart 90%,300 %}
{
  "type": "bar",
  "data": {
    "labels": ["一月", "二月", "三月", "四月"],
    "datasets": [{
      "label": "销售额",
      "data": [65, 59, 80, 81],
      "backgroundColor": ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0"]
    }]
  }
}
{% endchart %}
```

**配置：**
```yaml
chartjs:
  enable: true
  fontColor:
    light: "rgba(0, 0, 0, 0.8)"
    dark: "rgba(255, 255, 255, 0.8)"
```

---

## 配置启用

在 `_config.butterfly.yml` 中配置：

```yaml
# Note 提示框
note:
  style: flat  # simple / modern / flat / disabled
  icons: true
  border_radius: 3
  light_bg_offset: 0

# Mermaid 图表
mermaid:
  enable: true
  code_write: true
  theme:
    light: default
    dark: dark

# Chart.js 图表
chartjs:
  enable: true

# ABCJS 乐谱
abcjs:
  enable: true
  per_page: true
```

---

## 最佳实践

1. **代码对比** → 使用 `Tabs` 选项卡
2. **重要提示** → 使用 `Note` 提示框
3. **架构图/流程图** → 使用 `Mermaid`
4. **时间序列** → 使用 `Timeline`
5. **关键词高亮** → 使用 `Label`
6. **详细说明** → 使用 `hideToggle` 折叠
7. **外部链接** → 使用 `Button`
