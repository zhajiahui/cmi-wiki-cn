---
title: Item Group On Cooldown
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ItemGroupOnCooldown
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Item Group On Cooldown {#item-group-on-cooldown}

## 说明 {#description}

检查目标玩家是否有指定的处于冷却状态的物品组。   另请查看相关的 [SetItemGroupCooldown 机制](../mechanics/setitemgroupcooldown.md)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| group | g | 用于检查的组。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - ItemGroupOnCooldown{g=teleportingitems}
```
