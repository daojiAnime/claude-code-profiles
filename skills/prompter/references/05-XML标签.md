# 使用 XML 标签构建提示词

## 为什么使用 XML 标签？

XML 标签为提示词提供清晰的结构，帮助 Claude 更好地理解不同部分的内容和层级关系。这特别适用于复杂、多层次的提示词。

## 核心优势

### 1. 清晰的边界
XML 标签明确标识内容的开始和结束，避免歧义。

**❌ 无标签（模糊）:**
```
用户信息:
姓名: 张三
任务: 请分析这个用户的购买历史
```

**✅ 使用标签（清晰）:**
```xml
<user_info>
姓名: 张三
</user_info>

<task>
请分析这个用户的购买历史
</task>
```

### 2. 层次结构
支持嵌套和层级组织。

```xml
<project>
  <metadata>
    <name>电商系统</name>
    <version>2.0</version>
  </metadata>

  <requirements>
    <功能需求>
      <item>用户注册登录</item>
      <item>商品浏览购买</item>
    </功能需求>

    <性能需求>
      <item>支持 1000 并发</item>
      <item>响应时间 < 200ms</item>
    </性能需求>
  </requirements>
</project>
```

### 3. 内容隔离
防止不同部分相互干扰。

```xml
<instructions>
请将以下文本翻译成英文，保持专业语气
</instructions>

<text_to_translate>
如何使用 XML 标签
</text_to_translate>

<glossary>
XML = Extensible Markup Language（不要翻译）
</glossary>
```

## 常用标签模式

### 模式 1: 任务结构

```xml
<task>
  <description>创建一个 Python 函数</description>

  <requirements>
    - 函数名: process_data
    - 参数: data (list), threshold (float)
    - 返回: 过滤后的数据
  </requirements>

  <constraints>
    - 使用列表推导式
    - 添加类型提示
    - 包含 docstring
  </constraints>
</task>
```

### 模式 2: 示例组织

```xml
<examples>
  <example id="1">
    <input>Hello, world!</input>
    <output>HELLO, WORLD!</output>
  </example>

  <example id="2">
    <input>Python 3.12</input>
    <output>PYTHON 3.12</output>
  </example>
</examples>

<instruction>
将以下文本转换为大写: "claude ai"
</instruction>
```

### 模式 3: 多文档处理

```xml
<documents>
  <document id="contract">
    <title>服务协议</title>
    <content>
      [合同内容...]
    </content>
  </document>

  <document id="invoice">
    <title>发票</title>
    <content>
      [发票内容...]
    </content>
  </document>
</documents>

<task>
对比这两份文档，找出金额差异
</task>
```

### 模式 4: 角色和上下文

```xml
<role>
你是一位资深的 Python 导师，擅长用简单的语言解释复杂概念。
</role>

<audience>
学习者是编程初学者，刚学完基础语法。
</audience>

<topic>
请解释什么是装饰器，并给出实用例子。
</topic>
```

## 实用标签列表

### 内容组织标签

```xml
<instructions>指令说明</instructions>
<context>背景上下文</context>
<input>输入数据</input>
<output>期望输出</output>
<examples>示例集合</examples>
<requirements>要求列表</requirements>
<constraints>约束条件</constraints>
```

### 数据标签

```xml
<document>文档内容</document>
<code>代码块</code>
<data>数据集</data>
<query>查询语句</query>
<response>响应内容</response>
```

### 元数据标签

```xml
<metadata>元信息</metadata>
<id>标识符</id>
<title>标题</title>
<author>作者</author>
<timestamp>时间戳</timestamp>
```

### 逻辑标签

```xml
<if>条件分支</if>
<case>情况判断</case>
<step>步骤序列</step>
<note>注意事项</note>
<warning>警告信息</warning>
```

## 高级用法

### 技巧 1: 属性使用

```xml
<example type="positive" difficulty="easy">
  <input>优秀的产品</input>
  <sentiment>正面</sentiment>
</example>

<example type="negative" difficulty="hard">
  <input>产品不错，但价格有点贵</input>
  <sentiment>混合</sentiment>
</example>
```

### 技巧 2: 引用机制

```xml
<definitions>
  <term id="api">应用程序接口</term>
  <term id="rest">表述性状态传递</term>
</definitions>

<question>
请解释 RESTful API 的设计原则
(参考上面的定义 #api 和 #rest)
</question>
```

### 技巧 3: 分步指令

```xml
<workflow>
  <step number="1">
    <action>读取输入文件</action>
    <validation>确保文件存在且可读</validation>
  </step>

  <step number="2">
    <action>解析 JSON 数据</action>
    <validation>验证 JSON 格式正确</validation>
  </step>

  <step number="3">
    <action>处理数据</action>
    <details>过滤掉无效记录</details>
  </step>

  <step number="4">
    <action>输出结果</action>
    <format>CSV 格式，UTF-8 编码</format>
  </step>
</workflow>
```

### 技巧 4: 模板变量

```xml
<template>
  <subject>{{product_name}}</subject>
  <greeting>尊敬的 {{customer_name}}</greeting>
  <body>
    感谢您购买 {{product_name}}。
    您的订单号是 {{order_id}}。
  </body>
</template>

<variables>
  <product_name>无线耳机</product_name>
  <customer_name>张三</customer_name>
  <order_id>20240101001</order_id>
</variables>

<instruction>
请用变量填充模板
</instruction>
```

## 实战示例

### 示例 1: 代码审查

```xml
<code_review>
  <file path="src/utils.py">
    <code>
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item.price * item.quantity
    return total
    </code>
  </file>

  <review_aspects>
    <aspect>代码可读性</aspect>
    <aspect>性能优化</aspect>
    <aspect>错误处理</aspect>
    <aspect>最佳实践</aspect>
  </review_aspects>

  <output_format>
    为每个方面提供评分(1-5)和具体建议
  </output_format>
</code_review>
```

### 示例 2: 数据转换

```xml
<transformation>
  <source_format>CSV</source_format>
  <target_format>JSON</target_format>

  <source_data>
name,age,city
张三,25,北京
李四,30,上海
  </source_data>

  <mapping>
    <field source="name" target="fullName"/>
    <field source="age" target="age" type="int"/>
    <field source="city" target="location.city"/>
  </mapping>

  <additional_rules>
    - 添加 id 字段（自动递增）
    - 添加 timestamp 字段（当前时间）
    - 对 city 进行标准化（北京 -> Beijing）
  </additional_rules>
</transformation>
```

### 示例 3: 多语言处理

```xml
<translation_task>
  <source_language>中文</source_language>
  <target_languages>
    <language code="en">英语</language>
    <language code="ja">日语</language>
  </target_languages>

  <content>
    <title>产品介绍</title>
    <text>
      这是一款创新的智能设备，改变你的生活方式。
    </text>
  </content>

  <style_guide>
    <tone>专业、友好</tone>
    <formality>适中</formality>
    <target_audience>年轻消费者</target_audience>
  </style_guide>

  <output_format>
    为每种目标语言生成独立的 <translation> 块
  </output_format>
</translation_task>
```

## 最佳实践

### ✅ 推荐做法

1. **使用有意义的标签名**
   ```xml
   ✅ <user_profile>...</user_profile>
   ❌ <data1>...</data1>
   ```

2. **保持层次清晰**
   ```xml
   ✅ 合理嵌套（2-3 层）
   ❌ 过度嵌套（5+ 层）
   ```

3. **一致的命名风格**
   ```xml
   ✅ <user_name> / <user_email> (snake_case)
   ✅ <UserName> / <UserEmail> (PascalCase)
   ❌ <user_name> / <UserEmail> (混合)
   ```

4. **关闭所有标签**
   ```xml
   ✅ <item>内容</item>
   ❌ <item>内容
   ```

### ❌ 避免的陷阱

1. **标签过于复杂**
   ```xml
   ❌ <super_important_user_critical_data_section_v2>
   ```

2. **不必要的标签**
   ```xml
   ❌ <wrapper><content><text>简单文本</text></content></wrapper>
   ✅ <text>简单文本</text>
   ```

3. **标签与内容冲突**
   ```xml
   ❌ <code>请解释这段代码</code>  // 这不是代码
   ✅ <instruction>请解释这段代码</instruction>
   ```

## 快速参考模板

### 基础任务模板

```xml
<task>
  <objective>[任务目标]</objective>
  <input>[输入数据]</input>
  <requirements>[具体要求]</requirements>
  <output_format>[输出格式]</output_format>
</task>
```

### 分析模板

```xml
<analysis>
  <subject>[分析对象]</subject>
  <dimensions>
    <dimension>[维度1]</dimension>
    <dimension>[维度2]</dimension>
  </dimensions>
  <criteria>[评判标准]</criteria>
  <output>[输出要求]</output>
</analysis>
```

### 对话模板

```xml
<conversation>
  <role>[角色定义]</role>
  <context>[对话背景]</context>
  <history>
    <message role="user">[用户消息]</message>
    <message role="assistant">[助手回复]</message>
  </history>
  <current_query>[当前问题]</current_query>
</conversation>
```

## 总结

XML 标签是组织复杂提示词的强大工具：

- 🎯 提供清晰的内容边界
- 📊 支持层次化结构
- 🔒 隔离不同类型的内容
- 📝 提高可读性和可维护性
- ⚡ 帮助 Claude 准确理解意图
