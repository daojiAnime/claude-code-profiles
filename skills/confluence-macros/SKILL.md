---
name: confluence-macros
description: Confluence 宏和 Storage Format 语法参考，用于创建专业文档布局、面板、状态标签、表格等组件 (适用于 Confluence 7.19 Data Center)
---

# Confluence Macros Skill

用于 Confluence 页面编写的宏组件和 Storage Format 语法完整参考。

**目标版本**: Confluence Data Center 7.19.x

## 版本兼容性

| 版本 | 兼容性 | 说明 |
|------|--------|------|
| Confluence 7.19 Data Center | ✅ 完全兼容 | 本文档主要目标版本 |
| Confluence 7.x Data Center | ✅ 兼容 | 宏语法基本一致 |
| Confluence Cloud | ⚠️ 部分兼容 | Cloud 版有新编辑器，部分宏语法不同 |

## 触发场景

当需要以下操作时使用此 Skill：
- 创建/编辑 Confluence 页面内容（使用 Storage Format）
- 使用 Confluence REST API 或 MCP 工具更新页面
- 设计专业的文档布局（多列、面板）
- 添加面板、状态标签、折叠区域、代码块等组件
- 编写 Confluence 模板

## ⚠️ API 使用注意事项

**重要：通过 API 更新页面时的已知限制**

| 问题 | 说明 | 解决方案 |
|------|------|----------|
| **内容长度限制** | MCP 工具对 Storage Format 内容有长度限制 | 精简内容，分批更新 |
| **task-list 宏失败** | `<ac:task-list>` 通过 API 更新时会报错 | 用普通列表 + status 宏替代，或在编辑器中手动添加 |
| **布局宏限制** | 复杂嵌套布局可能失败 | 简化布局结构，避免多层嵌套 |

### 推荐做法

```xml
<!-- ❌ 避免：复杂任务列表 -->
<ac:task-list>
  <ac:task>
    <ac:task-id>1</ac:task-id>
    <ac:task-status>incomplete</ac:task-status>
    <ac:task-body>任务</ac:task-body>
  </ac:task>
</ac:task-list>

<!-- ✅ 推荐：用列表 + status 替代 -->
<ul>
  <li><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">进行中</ac:parameter></ac:structured-macro> 任务描述</li>
</ul>
```

## 快速参考

### 宏基本结构

```xml
<ac:structured-macro ac:name="宏名称">
  <ac:parameter ac:name="参数名">参数值</ac:parameter>
  <ac:rich-text-body>富文本内容</ac:rich-text-body>
</ac:structured-macro>
```

### 常用宏速查

| 宏名称 | 用途 | 主体类型 | API 兼容性 |
|--------|------|----------|------------|
| panel | 带边框/背景的面板 | rich-text-body | ✅ 良好 |
| info/note/warning/tip | 提示框 | rich-text-body | ✅ 良好 |
| status | 彩色状态标签 | 无主体 | ✅ 良好 |
| expand | 可折叠区域 | rich-text-body | ✅ 良好 |
| code | 代码块 | plain-text-body | ✅ 良好 |
| toc | 目录 | 无主体 | ✅ 良好 |
| recently-updated | 最近更新 | 无主体 | ✅ 良好 |
| pagetree | 页面树导航 | 无主体 | ✅ 良好 |
| task-list | 任务列表 | 特殊结构 | ⚠️ API 失败 |

### 状态颜色

```xml
<ac:structured-macro ac:name="status">
  <ac:parameter ac:name="colour">Green</ac:parameter>
  <ac:parameter ac:name="title">完成</ac:parameter>
</ac:structured-macro>
```

| colour | 用途 | 十六进制参考 |
|--------|------|--------------|
| Green | 完成、成功、已上线 | #00875A |
| Blue | 进行中、活跃 | #0052CC |
| Yellow | 待确认、规划中 | #FF991F |
| Red | 阻塞、失败、紧急 | #DE350B |
| Grey | 待启动、观察、暂停 | #6B778C |

### 面板

```xml
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="title">标题</ac:parameter>
  <ac:parameter ac:name="borderStyle">solid</ac:parameter>
  <ac:parameter ac:name="borderColor">#0052CC</ac:parameter>
  <ac:parameter ac:name="bgColor">#DEEBFF</ac:parameter>
  <ac:rich-text-body><p>内容</p></ac:rich-text-body>
</ac:structured-macro>
```

#### 面板配色方案

| 用途 | borderColor | bgColor |
|------|-------------|---------|
| 信息/默认 | #0052CC | #DEEBFF |
| 成功/完成 | #00875A | #E3FCEF |
| 警告/注意 | #FF991F | #FFFAE6 |
| 错误/紧急 | #DE350B | #FFEBE6 |
| 紫色/特殊 | #6554C0 | #EAE6FF |
| 灰色/中性 | #6B778C | #F4F5F7 |

### 提示框

```xml
<!-- 信息 (蓝) -->
<ac:structured-macro ac:name="info">
  <ac:rich-text-body><p>信息内容</p></ac:rich-text-body>
</ac:structured-macro>

<!-- 注意 (黄) -->
<ac:structured-macro ac:name="note">
  <ac:rich-text-body><p>注意内容</p></ac:rich-text-body>
</ac:structured-macro>

<!-- 警告 (红) -->
<ac:structured-macro ac:name="warning">
  <ac:rich-text-body><p>警告内容</p></ac:rich-text-body>
</ac:structured-macro>

<!-- 提示 (绿) -->
<ac:structured-macro ac:name="tip">
  <ac:rich-text-body><p>提示内容</p></ac:rich-text-body>
</ac:structured-macro>
```

### 布局

```xml
<ac:layout>
  <ac:layout-section ac:type="two_equal">
    <ac:layout-cell>左列内容</ac:layout-cell>
    <ac:layout-cell>右列内容</ac:layout-cell>
  </ac:layout-section>
</ac:layout>
```

| 布局类型 | 说明 |
|----------|------|
| single | 单列 100% |
| two_equal | 双列 50%-50% |
| two_left_sidebar | 左侧边栏 30%-70% |
| two_right_sidebar | 右侧边栏 70%-30% |
| three_equal | 三列 33%-33%-33% |
| three_with_sidebars | 三列带侧边栏 |

### 代码块

```xml
<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">python</ac:parameter>
  <ac:parameter ac:name="title">示例</ac:parameter>
  <ac:parameter ac:name="linenumbers">true</ac:parameter>
  <ac:plain-text-body><![CDATA[
def hello():
    print("Hello")
  ]]></ac:plain-text-body>
</ac:structured-macro>
```

**支持的语言**: python, java, javascript, bash, sql, html/xml, css, json, yaml, go, rust, c, cpp, csharp

### 动态宏

```xml
<!-- 最近更新 -->
<ac:structured-macro ac:name="recently-updated">
  <ac:parameter ac:name="max">5</ac:parameter>
  <ac:parameter ac:name="spaces">SPACEKEY</ac:parameter>
</ac:structured-macro>

<!-- 页面树 -->
<ac:structured-macro ac:name="pagetree"/>

<!-- 页面树搜索 -->
<ac:structured-macro ac:name="pagetreesearch"/>

<!-- 目录 -->
<ac:structured-macro ac:name="toc"/>
```

### 表情符号 (Confluence 7.19 Data Center)

```xml
<!-- 官方支持的 emoticon 名称 -->
<ac:emoticon ac:name="tick" />        <!-- ✓ 勾选 -->
<ac:emoticon ac:name="cross" />       <!-- ✗ 叉号 -->
<ac:emoticon ac:name="warning" />     <!-- ⚠ 警告 -->
<ac:emoticon ac:name="information" /> <!-- ℹ 信息（注意：不是 info） -->
<ac:emoticon ac:name="smile" />       <!-- 😊 微笑 -->
<ac:emoticon ac:name="sad" />         <!-- 😢 悲伤 -->
<ac:emoticon ac:name="cheeky" />      <!-- 😜 调皮 -->
<ac:emoticon ac:name="laugh" />       <!-- 😄 大笑 -->
<ac:emoticon ac:name="wink" />        <!-- 😉 眨眼 -->
<ac:emoticon ac:name="thumbs-up" />   <!-- 👍 点赞 -->
<ac:emoticon ac:name="thumbs-down" /> <!-- 👎 踩 -->
```

> ⚠️ **注意**：`info` 在 7.19 中不支持，必须使用 `information`。`light-on`、`blue-star` 等在官方文档中未列出，可能不可用。

## 实战示例

### 个人主页模板

```xml
<!-- 头部横幅 -->
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="borderStyle">solid</ac:parameter>
  <ac:parameter ac:name="borderColor">#0052CC</ac:parameter>
  <ac:parameter ac:name="bgColor">#DEEBFF</ac:parameter>
  <ac:rich-text-body>
    <h1>姓名 | 职位</h1>
    <p>
      <ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">在职</ac:parameter></ac:structured-macro>
      <ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">技能1</ac:parameter></ac:structured-macro>
    </p>
  </ac:rich-text-body>
</ac:structured-macro>

<!-- 信息面板 -->
<h2>关于我</h2>
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="bgColor">#F4F5F7</ac:parameter>
  <ac:rich-text-body>
    <p><strong>姓名</strong>：xxx | <strong>部门</strong>：xxx</p>
  </ac:rich-text-body>
</ac:structured-macro>

<!-- 项目卡片 -->
<h2>项目</h2>
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="title">项目名称</ac:parameter>
  <ac:parameter ac:name="bgColor">#EAE6FF</ac:parameter>
  <ac:rich-text-body>
    <p>项目描述 <ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">进行中</ac:parameter></ac:structured-macro></p>
  </ac:rich-text-body>
</ac:structured-macro>

<!-- 动态内容 -->
<h2>最近更新</h2>
<ac:structured-macro ac:name="recently-updated"><ac:parameter ac:name="max">5</ac:parameter></ac:structured-macro>

<!-- 底部提示 -->
<ac:structured-macro ac:name="tip">
  <ac:rich-text-body><p><strong>欢迎交流！</strong></p></ac:rich-text-body>
</ac:structured-macro>
```

### 技术文档模板

```xml
<!-- 文档头部 -->
<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="bgColor">#DEEBFF</ac:parameter>
  <ac:rich-text-body>
    <p><strong>版本</strong>: 1.0 | <strong>状态</strong>: <ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">已发布</ac:parameter></ac:structured-macro> | <strong>更新</strong>: 2024-01-01</p>
  </ac:rich-text-body>
</ac:structured-macro>

<!-- 目录 -->
<ac:structured-macro ac:name="toc"/>

<!-- 提示框 -->
<ac:structured-macro ac:name="info">
  <ac:rich-text-body><p>前置条件说明...</p></ac:rich-text-body>
</ac:structured-macro>

<!-- 代码示例 -->
<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">bash</ac:parameter>
  <ac:parameter ac:name="title">安装命令</ac:parameter>
  <ac:plain-text-body><![CDATA[pip install package-name]]></ac:plain-text-body>
</ac:structured-macro>

<!-- 警告 -->
<ac:structured-macro ac:name="warning">
  <ac:rich-text-body><p>注意事项...</p></ac:rich-text-body>
</ac:structured-macro>
```

## 参考文件

详细文档位于 `references/` 目录：

- **fetched-docs.md** - 完整官方文档抓取（636行，9个页面）
  - Storage Format 完整语法
  - 9 个常用宏详细参数说明
  - XML 代码示例
- **macros.md** - 宏参数详解
- **storage-format.md** - Storage Format 规范

## 官方文档 (Confluence 7.19)

- [Confluence 7.19 Storage Format](https://confluence.atlassian.com/conf719/confluence-storage-format-1157466554.html)
- [Confluence 7.19 Macros](https://confluence.atlassian.com/conf719/macros-1157466666.html)
- [Storage Format (通用)](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)

## 弃用提醒

⚠️ **2026 年 1 月起**，Atlassian 将弃用旧版编辑器。Cloud 编辑器使用新元素替代部分宏（panel 元素、code snippet 元素等）。过渡期内旧版宏继续工作。
