---
title: Barremove
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/barremove
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Barremove {#barremove}

## 说明 {#description}

移除施法生物的自定义 Boss 血条，不能用于玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n | 要移除的 Boss 血条名称。 | infobar |

## 示例 {#examples}

```yaml
  Skills:
  - barRemove{name="MyBossBar"} @self ~onInteract
```
