---
title: Has Item
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasItem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Has Item {#has-item}

## 说明 {#description}

测试目标玩家或物品容器是否恰好具有给定数量的给定材料。   使用[物品匹配器](../../items/item-matcher.md)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | i, material, m, type, t, mat, types | 要检查的物品。 | DIRT |
| amount | a | 要检查的数量。 | >0 |
| strict | exact, e | 匹配器是否应更严格地匹配目标物品。 | false |
| vanillaonly | vanilla | 匹配的物品是否只能为原版物品。 | false |

## 示例 {#examples}

```yaml
  Conditions:
  - hasitem{i=stick;amount=>1} true
```

```yaml
  Conditions:
  - hasitem{i=my_custom_item;amount=<10} true
```

```yaml
  Conditions:
  - hasitem{i=mmoitems.SWORD.CUTLASS;amount=1to10} true
```
