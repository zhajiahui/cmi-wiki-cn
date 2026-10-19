---
title: Equip
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/equip
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Equip {#equip}

## 说明 {#description}

为生物装备一件物品。使用与 [Equipment](../../mobs/equipment.md) 配置完全相同的语法。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | items, i, equipment, equip, e | 要应用于生物的物品配置字符串。 |  |

## 示例 {#examples}

此示例为施法生物装备钻石剑。

```yaml
EquipDiamondSword:
  Skills:
  - equip{item=diamond_sword HAND}
```

此示例将骷髅王的王冠装备为头盔。

```yaml
EquipCrown:
  Skills:
  - equip{item=KingsCrown HEAD}
```
