---
title: Oxygen
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/oxygen
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Oxygen {#oxygen}

## 说明 {#description}

为目标玩家提供一定量的氧气。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 给予玩家的氧气量。 | 1 |

## 示例 {#examples}

```yaml
  Skills:
  - oxygen{amount=10} @trigger ~onInteract
```
