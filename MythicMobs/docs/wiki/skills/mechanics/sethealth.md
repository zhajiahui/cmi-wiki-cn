---
title: Sethealth
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sethealth
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sethealth {#sethealth}

## 说明 {#description}

设置目标实体的生命值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要设置的生命值 | 1.0 |

## 示例 {#examples}

当玩家右键单击生物时，此示例会将玩家的生命值设置为6（3心）。

```yaml
  Skills:
  - sethealth{a=6} @trigger ~onInteract
  - ...
```

## 别名 {#aliases}

- sethp
