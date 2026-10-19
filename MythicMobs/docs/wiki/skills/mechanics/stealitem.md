---
title: Steal Item
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/StealItem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Steal Item {#steal-item}

## 说明 {#description}

从目标身上偷走一件物品并将其放入怪物手中

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要偷取的数量 | 1 |
| dropchance | dc | 设置被偷物品在死亡时掉落的概率 | 0.0 |
| strict | exact, e | 匹配器是否应更严格地匹配目标物品。 | false |
| types | type, t, material, mat, m, item, i | 要匹配的物品，可以是列表 | DIRT |
| vanillaonly | vanilla | 匹配的物品是否只能为原版物品。 | false |
| onStealSkill | onsteal, then | 成功偷取物品后执行的元技能 |  |

## 示例 {#examples}

```yaml
  Skills:
  - stealitem @trigger ~onDamaged 0.1 =100%
```

## 别名 {#aliases}

- steal
- stealitems
- itemsteal
