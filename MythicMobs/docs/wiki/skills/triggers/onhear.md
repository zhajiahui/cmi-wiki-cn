---
title: On Hear
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onHear
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Hear {#on-hear}

## 说明 {#description}

[启用此功能](../../mobs/mobs.md#hearing)后，生物听到声音时执行技能。可在触发的技能中使用 `<skill.var.volume>` [占位符](../placeholders.md#variable-placeholders)，获取一个介于 1 和 15 之间、表示距声源距离的浮点数

> 关联的 [@trigger](../targeters/trigger.md) 是生成声音的实体

> 关联的[@origin](../targeters/origin.md)是声音产生的位置

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.volume>` |
| `<skill.var.sound-type>` |

## 示例 {#examples}

```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="I can hear you <trigger.name>! <skill.var.volume>? Way too loud!"} @trigger ~onHear
```

## 别名 {#aliases}

- onVibration
