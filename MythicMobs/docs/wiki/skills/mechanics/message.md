---
title: Message
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/message
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Message {#message}

## 说明 {#description}

如果目标是玩家，则向目标发送聊天消息。 [颜色代码](../placeholders.md#color-codes)和[变量](../variables.md)在此机制中可用。

- 允许格式为 **`<#FFFFFF>`** 的十六进制颜色
- 支持 **`<gradient:#color1:#color2>text</gradient>`** 格式的渐变
- 支持**`<rainbow>text</rainbow>`**
- 支持格式为 **`<hover:show_text:'hover text??'>hover over me!</hover>`** 的悬停文本
- 支持 **`<click:run_command:/say hello>click me!</click>`** 格式的可点击文本

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| message | msg,m | 要发送的消息。 | None |
| audience |  | 消息的[接收对象](../audience.md)。 |  |

## 示例 {#examples}

```yaml
   Skills:
   - message{m="<caster.name>&f<&co> Hahaha! You will all die!"} @PlayersInRadius{r=30}
```

## 别名 {#aliases}

- m
- msg
