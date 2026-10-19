---
title: Set Item Group Cooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetItemGroupCooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Item Group Cooldown {#set-item-group-cooldown}

## 说明 {#description}

为目标玩家设置物品组的冷却时间

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| key | k, group, g | 要设置冷却的组 | minecraft:item_group |
| ticks | t | 冷却持续的刻数 | 20 |

## 示例 {#examples}

```yaml
  Skills:
  - SetItemGroupCooldown{key=yournamespace.teleportingitems;ticks=200}
```
