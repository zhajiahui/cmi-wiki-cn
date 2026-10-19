---
title: Takeitem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/takeitem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Takeitem {#takeitem}

## 说明 {#description}

从目标玩家的物品栏中移除指定数量的物品。   使用[物品匹配器](../../items/item-matcher.md)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| item | material, m, i, mat, t, type, types | 要移除的物品或材质 | DIRT |
| amount | a | 要移除的数量 | 1 |
| exact | e, strict | 物品名称是否必须与指定名称完全一致 | true |
| vanillaonly | vanilla | 匹配的物品是否只能为原版物品。 | false |
| variable | var | 从物品栏中移除指定物品变量的值所对应的物品。设置后忽略 `item` |  |

## 示例 {#examples}

会从最近的玩家的物品栏中清除一堆泥土

```yaml
  Skills:
  - takeitem{i=DIRT;a=64} @NearestPlayer{r=10}
```

## 别名 {#aliases}

- take
- itemtake
- takeitems
