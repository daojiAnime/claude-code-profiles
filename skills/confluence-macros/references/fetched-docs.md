# Confluence 宏和存储格式完整参考文档

> 抓取日期: 2025-12-09
> 数据来源: Atlassian 官方文档

---

## 目录

1. [Confluence Storage Format (存储格式)](#1-confluence-storage-format-存储格式)
2. [Confluence Macros 概览](#2-confluence-macros-概览)
3. [什么是宏](#3-什么是宏)
4. [Status 宏](#4-status-宏)
5. [Panel 宏](#5-panel-宏)
6. [Info/Tip/Note/Warning 宏](#6-infotipnotewarning-宏)
7. [Expand 宏](#7-expand-宏)
8. [Table of Contents 宏](#8-table-of-contents-宏)
9. [Code Block 宏](#9-code-block-宏)

---

## 1. Confluence Storage Format (存储格式)

**来源**: https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html

### 概述

Confluence 使用基于 XHTML 的 XML 格式来存储页面内容。用户可以通过 **更多选项 > 查看存储格式** 来查看（需要管理员权限或安装 Confluence Source Editor 插件）。

### 核心格式元素

#### 标题

```xml
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
```

#### 文本样式

- **粗体**: `<strong>text</strong>`
- **斜体**: `<em>text</em>`
- **删除线**: `<span style="text-decoration: line-through;">text</span>`
- **下划线**: `<u>text</u>`
- **等宽字体**: `<code>text</code>`
- **引用块**: `<blockquote><p>quote</p></blockquote>`

#### 列表

```xml
<!-- 无序列表 -->
<ul><li>bullet item</li></ul>

<!-- 有序列表 -->
<ol><li>numbered item</li></ol>

<!-- 任务列表 -->
<ac:task-list>
  <ac:task>
    <ac:task-status>incomplete</ac:task-status>
    <ac:task-body>task item</ac:task-body>
  </ac:task>
</ac:task-list>
```

#### 链接

```xml
<!-- 页面链接 -->
<ac:link><ri:page ri:content-title="Title" /></ac:link>

<!-- 外部链接 -->
<a href="url">text</a>

<!-- 附件链接 -->
<ac:link><ri:attachment ri:filename="file.gif" /></ac:link>
```

#### 图片

```xml
<!-- 附件图片 -->
<ac:image><ri:attachment ri:filename="image.gif" /></ac:image>

<!-- URL 图片 -->
<ac:image><ri:url ri:value="http://example.com/image.png" /></ac:image>
```

#### 表格

使用标准 HTML 表格语法：`<table>`, `<tbody>`, `<tr>`, `<th>`, `<td>` 元素，支持 `rowspan` 和 `colspan` 属性。

#### 页面布局

```xml
<ac:layout>
  <ac:layout-section ac:type="single">
    <ac:layout-cell>{content}</ac:layout-cell>
  </ac:layout-section>
</ac:layout>
```

**布局类型**:
- `single` - 单列
- `two_equal` - 两列等宽
- `two_left_sidebar` - 左侧边栏
- `two_right_sidebar` - 右侧边栏
- `three_equal` - 三列等宽
- `three_with_sidebars` - 三列带侧边栏

#### 表情符号

```xml
<ac:emoticon ac:name="smile" />
<ac:emoticon ac:name="thumbs-up" />
<ac:emoticon ac:name="warning" />
```

#### 资源标识符

```xml
<!-- 页面引用 -->
<ri:page ri:space-key="KEY" ri:content-title="Title"/>

<!-- 用户引用 -->
<ri:user ri:userkey="uuid"/>

<!-- URL 引用 -->
<ri:url ri:value="http://example.com"/>
```

#### 模板变量

```xml
<at:declarations>
  <!-- 字符串变量 -->
  <at:string at:name="VarName" />

  <!-- 文本区域变量 -->
  <at:textarea at:columns="100" at:rows="5" at:name="Multi" />

  <!-- 列表变量 -->
  <at:list at:name="ListVar">
    <at:option at:value="Option1" />
  </at:list>
</at:declarations>

<!-- 使用变量 -->
<at:var at:name="VarName" />
```

#### 指令文本

```xml
<!-- 占位符文本（用户输入时替换） -->
<ac:placeholder>Instruction text replaced when user types</ac:placeholder>

<!-- @提及占位符 -->
<ac:placeholder ac:type="mention">@mention prompt text</ac:placeholder>
```

### 重要注意事项

- 该格式在技术上是 XML（而非真正的 XHTML），因为包含自定义元素如 `<ac:link>` 和宏
- 链接主体支持有限的标记：`<b>`, `<strong>`, `<em>`, `<i>`, `<code>`, `<tt>`, `<sub>`, `<sup>`, `<br>`, `<span>`
- 相对资源引用会省略容器标识符
- 模板变量会在用户开始输入时自动清除指令文本

---

## 2. Confluence Macros 概览

**来源**: https://confluence.atlassian.com/doc/macros-139387.html

### 可用宏类别

该页面列出了 **79 个宏**，按功能组织：

- **内容显示**: Children Display, Include Page, Gallery, Table of Contents
- **格式化**: Code Block, Panel, Expand, Status, Info/Tip/Note/Warning
- **报告**: Content Report Table, Page Properties Report, Task Report, Global Reports
- **集成**: Jira Issues, Jira Chart, RSS Feed, HTML
- **导航**: Navigation Map, Page Tree, Breadcrumbs
- **用户与协作**: User List, Contributors, Profile Picture, IM Presence
- **高级**: Advanced Roadmaps, Roadmap Planner, Team Calendar

### 访问方式

用户必须登录才能查看 Confluence 编辑器或编辑文档。

### 文档结构

每个宏都有自己的专用页面，通常涵盖：
- 参数/配置选项
- 使用场景
- XML 存储格式语法
- 代码示例

---

## 3. 什么是宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/what-are-macros/

### 宏的定义

宏是"扩展 Confluence 页面和实时文档功能的工具，允许您添加额外功能或包含动态内容"。

### 工作原理

宏使用户能够将动态元素添加到页面中。示例包括：
- **附件宏 (Attachments Macro)**: 列出附加到内容的文件
- **小部件连接器宏 (Widget Connector Macro)**: 嵌入外部内容，如 YouTube 视频或社交媒体源

### 添加和编辑宏

**插入方法**:
1. 编辑时从工具栏选择宏选项
2. 按名称搜索所需的宏
3. 根据需要配置参数
4. 或者，输入"/"触发宏菜单

**编辑方法**:
1. 选择宏占位符
2. 点击编辑图标打开配置
3. 调整参数（更改自动保存）
4. 关闭面板继续编辑

用户还可以使用居中、中等宽度和全宽图标调整宏宽度，或通过垃圾桶图标删除宏。

### 宏参数

许多宏支持控制输出行为的可选参数。例如，附件宏允许用户指定要显示的文件格式，并选择是否显示旧版本。

### 宏占位符

编辑器中插入宏的位置会显示占位符，用户可以双击进行编辑，或在页面内剪切/复制/粘贴宏。

### 可用宏

文档列出了 30 多个内置宏，包括 Chart、Page Tree、Jira Issues 和 Table of Contents 宏。通过 Atlassian Marketplace 可以获得更多宏。

---

## 4. Status 宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/insert-the-status-macro/

### 概述

Status 宏创建"一个彩色的胶囊形状（圆角框），用于报告项目状态"。用户可以自定义颜色和附带文本，并在编辑器中实时编辑。

### 使用方法

**宏浏览器方式**:
1. 编辑时从工具栏选择插入菜单
2. 按名称定位并选择宏
3. 根据需要配置参数

**斜杠命令替代方式**:
输入 `/ ` 后跟宏名称以触发自动完成建议。

**编辑现有宏**:
点击宏占位符，选择编辑，并在对话框窗口中修改参数。

### 参数

| 参数 | 默认值 | 详情 |
|------|--------|------|
| **Color** (colour) | Grey | 可用选项：Grey、Red、Yellow、Green、Blue |
| **Title** (title) | 颜色名称 | 显示在胶囊内的文本；如果为空则默认为颜色名称 |
| **Use outline style** (subtle) | False | 实心背景配白色文本（默认）vs. 白色背景配彩色边框和文本 |

### Wiki 标记语法

**宏名称**: `status`

**宏主体**: 无

**示例**:
```
status:colour=Green|title=On track|subtle=true
```

### 重要提示

Atlassian 宣布从 2026 年 1 月开始弃用旧版编辑器。云编辑器有更新版本的 Status 宏。旧版本将在过渡期内保持功能。

---

## 5. Panel 宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/insert-the-panel-macro/

### 概述

Panel 宏在 Confluence Cloud 中显示可自定义的文本容器。自 2025 年 6 月起，Atlassian 宣布从 2026 年 1 月开始弃用旧版编辑器，但该宏在过渡期内仍然有效。

### 插入步骤

**添加 Panel 宏**:
1. 从编辑工具栏选择插入宏按钮
2. 从可用选项中定位并选择 Panel 宏
3. 点击"插入"

**编辑现有 Panel 宏**:
1. 点击宏占位符选择它
2. 选择编辑图标打开配置设置
3. 根据需要调整参数（更改自动保存）
4. 关闭面板继续编辑页面

您还可以使用居中、中等宽度和全宽图标调整宏宽度，或使用删除图标完全移除宏。

### 参数

| 参数 | 默认值 | 描述 |
|------|--------|------|
| **Panel Title** `(title)` | 无 | "面板的标题。如果指定，此标题将显示在自己的标题行中" |
| **Border Style** `(borderStyle)` | solid | 接受 `solid`、`dashed` 和其他有效的 CSS 边框样式 |
| **Border Color** `(borderColor)` | — | 接受 HTML 颜色名称或十六进制代码 |
| **Border Pixel Width** `(borderWidth)` | — | 以像素为单位的宽度测量 |
| **Background Color** `(bgColor)` | — | 接受 HTML 颜色名称或十六进制代码 |
| **Title Background Color** `(titleBGColor)` | — | "标题行的背景颜色" |
| **Title Text Color** `(titleColor)` | — | "标题行中文本的颜色" |

### Wiki 标记示例

**宏名称**: `panel`

**宏主体**: 接受富文本

```
{panel:title=My title|borderStyle=dashed|borderColor=blue|titleBGColor=#00a400|titleColor=white|bgColor=#72bc72}
A formatted panel
{panel}
```

此语法对于在可视化编辑器之外添加宏很有用，例如在空间侧边栏、页眉或页脚中。

---

## 6. Info/Tip/Note/Warning 宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/insert-the-info-tip-note-and-warning-macros/

### 概述

这些宏允许您"在 Confluence 页面上突出显示信息"，通过在文本周围创建彩色框。它们在旧版编辑器中可用；云编辑器使用面板元素代替。

### 宏类型

- **Info**: 蓝色背景
- **Tip**: 绿色背景
- **Note**: 紫色背景
- **Warning**: 黄色背景

### 参数

| 参数 | 默认值 | 描述 |
|------|--------|------|
| **Optional Title** `(title)` | 无 | "框的标题。如果指定，标题文本将以粗体显示在图标旁边。" |
| **Show Icon** `(icon)` | true | "如果为 'false'，将不显示图标。" |

### 插入方法

1. **工具栏**: 编辑时从工具栏选择，按名称查找，根据需要配置
2. **斜杠命令**: 在页面上输入 `/`，继续输入宏名称以过滤
3. **自动完成**: 输入 `{` 后跟宏名称的开头以获得建议

### 编辑现有宏

- 选择宏占位符
- 点击编辑图标打开配置
- 更改自动保存
- 使用居中、中等宽度或全宽图标调整宽度
- 使用垃圾桶图标删除

### Wiki 标记语法

**宏名称**: info/tip/note/warning

**基本示例**:
```
{info:title=This is my title|icon=false}
This is _important_ information.
{info}
```

宏主体接受富文本格式。

### 弃用通知

旧版编辑器正在被弃用，从 2026 年 1 月开始实施。在 Confluence Cloud 的云编辑器中使用面板元素以获得等效功能。

---

## 7. Expand 宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/insert-the-expand-macro/

### 概述

Expand 宏在 Confluence 页面上创建可折叠/可展开的文本部分。根据文档，它"在您的页面上显示可展开/可折叠的文本部分"。

### 主要特征

**导出时的行为**: 将页面导出为 PDF 或 HTML 格式时，宏会自动展开，以便读者可以在这些导出格式中查看完整内容。

### 插入步骤

文档概述了一个四步流程：

1. **访问宏**: 编辑时，从工具栏选择宏插入按钮或使用斜杠 (/) 命令
2. **定位并选择**: 在显示的列表中找到 Expand 宏并选择它
3. **配置标题**: 修改默认标题文本（显示为"点击此处展开..."）为您首选的标签文本，该文本显示在展开/折叠图标旁边
4. **添加内容**: 在可展开部分内插入您想要的内容

### 视觉参考

官方文档包含演示宏插入的动画 GIF，可在 Atlassian 支持资源中找到。

### 附加说明

提供的源材料不包含关于 XML/存储格式语法、特定参数或高级代码示例的详细信息，仅限于上述基本插入工作流程。

---

## 8. Table of Contents 宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/insert-the-table-of-contents-macro/

### 概述

Table of Contents 宏通过扫描当前 Confluence Cloud 页面或实时文档上的标题生成可导航的索引，帮助读者浏览冗长的内容。

### 基本设置

要插入宏，用户可以：
- 选择工具栏并按名称查找宏
- 在页面上输入"/"以访问相同的列表并按宏名称过滤

要配置，选择宏占位符，点击编辑图标打开配置面板，并调整参数。更改自动保存。

### 配置选项

#### 基本参数

| 参数 | 默认值 | 功能 |
|------|--------|------|
| **Display as** | Vertical list | 选择垂直列表格式或水平菜单样式链接 |
| **Bullet style** | Bullet | 选项：None、Mixed、Bullet、Circle、Square 或 Numbered（仅适用于垂直列表） |
| **Heading levels** | 1 到 6 | 选择要包含的最小和最大标题级别 |
| **Section numbers** | 未选中 | 启用大纲编号（例如，1.1、1.2、1.3） |

#### 高级参数

- **Indent headings (indent)**: 为垂直列表设置基于 CSS 的缩进（例如，"10px"）
- **Include headings with (include)**: 使用通配符和管道符（"|"）作为分隔符过滤特定标题；区分大小写
- **Exclude headings with (exclude)**: 使用相同的过滤器语法删除特定标题
- **CSS class name (class)**: 通过为输出 div 指定类属性来应用自定义样式
- **Exclude in PDF export (printable)**: 在 PDF 导出和打印输出中隐藏宏

### 限制

"宏仅在已添加到的页面、实时文档、博客或宏内工作，无法跨多个页面引用或被引用。"

当在摘录宏中使用时，它仅显示该摘录内的标题，导航链接不引用源内容。

### 支持的内容

宏显示来自页面、实时文档和博客文章的标题格式文本、表情符号、提及、状态和日期。

---

## 9. Code Block 宏

**来源**: https://support.atlassian.com/confluence-cloud/docs/insert-the-code-block-macro/

### 概述

Code Block 宏在 Confluence Cloud 页面上显示带有语法高亮的源代码。**注意**: 此旧版宏将于 2026 年 1 月弃用；云编辑器使用代码片段元素代替。

### 添加宏

1. 编辑时从工具栏选择 **+** 图标
2. 按名称搜索并选择 Code Block 宏
3. 根据需要配置

**替代方式**: 在页面上输入 `/` 以访问相同的宏列表并按名称过滤。

### 编辑宏

1. 点击宏占位符
2. 选择**编辑**图标打开配置
3. 调整参数（更改自动保存）
4. 继续编辑以关闭面板

您还可以使用居中、中等或全宽图标调整宽度，或使用垃圾桶图标删除宏。

### 关键参数

| 参数 | 默认值 | 用途 |
|------|--------|------|
| **Syntax highlighting** (language) | Java | 从以下语言中选择：ActionScript、AppleScript、Bash、C#、C++、CSS、ColdFusion、Delphi、Diff、Erlang、Groovy、HTML/XML、Java、JavaFX、JavaScript、Plain Text、PowerShell、Python、Ruby、SQL、Sass、Scala、Visual Basic |
| **Title** | 无 | 添加显示指定标题的标题行 |
| **Collapsible** (collapse) | false | 在页面加载时折叠代码；用户点击以展开 |
| **Show line numbers** (linenumbers) | false | 在左侧显示行号 |
| **First line number** (firstline) | 1 | 启用行号时设置起始编号 |
| **Theme** | Confluence | 选项：Django、Emacs、FadeToGrey、Midnight、RDark、Eclipse、Confluence、Wiki |

### 存储格式（Wiki 标记）

旧版编辑器语法:
```
{code:title=Title|theme=FadeToGrey|linenumbers=true|language=html/xml|firstline=0001|collapse=true}
Code content here
{code}
```

### 重要注意事项

- 占位符中的空白**按原样保留**以提供格式灵活性
- Wiki 标记仅在旧版编辑器中受支持
- 云编辑器用户应过渡到代码片段元素

---

## 附录：Storage Format 宏结构

### 通用宏 XML 结构

```xml
<!-- 无主体宏 -->
<ac:structured-macro ac:name="macro-name">
  <ac:parameter ac:name="param1">value1</ac:parameter>
  <ac:parameter ac:name="param2">value2</ac:parameter>
</ac:structured-macro>

<!-- 有主体宏 -->
<ac:structured-macro ac:name="macro-name">
  <ac:parameter ac:name="param1">value1</ac:parameter>
  <ac:rich-text-body>
    <p>Rich text content here</p>
  </ac:rich-text-body>
</ac:structured-macro>

<!-- 纯文本主体宏 -->
<ac:structured-macro ac:name="macro-name">
  <ac:parameter ac:name="param1">value1</ac:parameter>
  <ac:plain-text-body><![CDATA[Plain text content]]></ac:plain-text-body>
</ac:structured-macro>
```

### 示例：Status 宏 Storage Format

```xml
<ac:structured-macro ac:name="status">
  <ac:parameter ac:name="colour">Green</ac:parameter>
  <ac:parameter ac:name="title">On track</ac:parameter>
  <ac:parameter ac:name="subtle">true</ac:parameter>
</ac:structured-macro>
```

### 示例：Panel 宏 Storage Format

```xml
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="title">My title</ac:parameter>
  <ac:parameter ac:name="borderStyle">dashed</ac:parameter>
  <ac:parameter ac="borderColor">blue</ac:parameter>
  <ac:parameter ac:name="titleBGColor">#00a400</ac:parameter>
  <ac:parameter ac:name="titleColor">white</ac:parameter>
  <ac:parameter ac:name="bgColor">#72bc72</ac:parameter>
  <ac:rich-text-body>
    <p>A formatted panel</p>
  </ac:rich-text-body>
</ac:structured-macro>
```

### 示例：Info 宏 Storage Format

```xml
<ac:structured-macro ac:name="info">
  <ac:parameter ac:name="title">This is my title</ac:parameter>
  <ac:parameter ac:name="icon">false</ac:parameter>
  <ac:rich-text-body>
    <p>This is <em>important</em> information.</p>
  </ac:rich-text-body>
</ac:structured-macro>
```

### 示例：Code Block 宏 Storage Format

```xml
<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">python</ac:parameter>
  <ac:parameter ac:name="title">Example Code</ac:parameter>
  <ac:parameter ac:name="theme">FadeToGrey</ac:parameter>
  <ac:parameter ac:name="linenumbers">true</ac:parameter>
  <ac:parameter ac:name="firstline">1</ac:parameter>
  <ac:parameter ac:name="collapse">false</ac:parameter>
  <ac:plain-text-body><![CDATA[def hello_world():
    print("Hello, World!")]]></ac:plain-text-body>
</ac:structured-macro>
```

---

## 总结

### 核心要点

1. **Storage Format 是 XML**: Confluence 使用 XHTML 风格的 XML，带有自定义命名空间（`ac:`, `ri:`, `at:`）
2. **宏是结构化元素**: 所有宏使用 `<ac:structured-macro>` 元素，带有名称和参数
3. **三种主体类型**: 无主体、富文本主体 (`<ac:rich-text-body>`)、纯文本主体 (`<ac:plain-text-body>`)
4. **参数化配置**: 所有宏行为通过 `<ac:parameter>` 元素控制
5. **向后兼容**: Wiki 标记 (`{macro:param=value}`) 仍在旧版编辑器中支持

### 弃用时间表

- **2026 年 1 月**: 旧版编辑器开始强制弃用
- **云编辑器**: 使用新的元素替代（panel 元素、code snippet 元素等）
- **过渡期**: 旧版宏在过渡期内继续工作

### 最佳实践

1. **使用 Storage Format**: 直接操作 Confluence 内容时使用 XML
2. **参数验证**: 始终验证宏参数的有效值
3. **富文本处理**: 在宏主体中使用有效的 XHTML
4. **CDATA 包装**: 纯文本主体使用 CDATA 避免 XML 解析问题
5. **命名空间**: 正确使用 `ac:`, `ri:`, `at:` 命名空间前缀

---

**文档结束**
