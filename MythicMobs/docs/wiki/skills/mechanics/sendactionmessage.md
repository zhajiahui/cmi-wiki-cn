---
title: Sendactionmessage
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sendactionmessage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sendactionmessage {#sendactionmessage}

## 说明 {#description}

向目标玩家的动作栏发送消息。

动作栏消息支持[颜色代码](../placeholders.md#color-codes)和[变量](../variables.md)。部分目标选择器可能不兼容，若发现不兼容的选择器，请在错误或建议子论坛反馈。

![](../../assets/9eea4bd2766607.jpg)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| message | m, msg | 要发送的消息，必须用引号包裹 |  |

## 示例 {#examples}

```yaml
  Skills:
  - actionmessage{m="<caster.name>&f is casting a spell!"} @PlayersInRadius{r=30}
  - actionmessage{m="&lHello! &cI'm &athe &9&lactionmessage-bar&r! &e:)"} @trigger
  - am{m="<caster.name>&f is using the *skill alias!*"} @PlayersInRadius{r=30}
```

## 别名 {#aliases}

- am
- actionmessage
