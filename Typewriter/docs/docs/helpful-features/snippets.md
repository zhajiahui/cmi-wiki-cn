---
title: 片段（Snippets）（What are Snippets?）
source: https://docs.typewritermc.com/docs/helpful-features/snippets
source_version: 0.8.0
---

# 片段（Snippets）（What are Snippets?）

片段是扩展可以使用的小信息片段。主要与如何向用户显示事物有关。
片段允许你自定义不同适配器的各种部分。例如，你可以自定义消息在`Basic Extension`中的显示方式。

# 如何自定义片段？

可以通过编辑`plugin/Typewriter/snippets.yml`文件来自定义片段。

**重要**

请注意，代码片段仅在第一次使用时写入。所以如果你想自定义一个snippet，你需要先触发使用该snippet的条目。

因此，对于`Basic Extension`，第一个人收到`MessageDialogueEntry`后，`snippets.yml`文件将如下所示：

plugin/Typewriter/snippets.yml

```yaml
dialogue:
  message:
    format: |2

      <gray> | <bold><speaker></bold><reset><gray> |
      <reset><white> <message>
```

然后，你可以编辑此文件来自定义代码片段。例如，如果你想更改说话者姓名的默认颜色，你可以将`<bold><speaker></bold>`更改为`<bold><red><speaker></red></bold>`。

Yaml 使用`|`来指示文本是多行字符串。

plugin/Typewriter/snippets.yml

```yaml
dialogue:
  message:
    format: |2

      <gray> | <bold><speaker></bold><reset><gray> |
      <reset><white> <message>
```

`|2`表示文本是多行字符串，字符串末尾有`2`换行符。如果你不需要换行符，可以删除`2`使其成为`|`。

---

原文：[What are Snippets?](https://docs.typewritermc.com/docs/helpful-features/snippets) · 文档版本：0.8.0
