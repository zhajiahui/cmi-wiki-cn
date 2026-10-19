---
title: Itemspray
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/itemspray
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Itemspray {#itemspray}

## 说明 {#description}

在目标位置产生临时物品喷发效果。除非通过 `allowpickup` 另行设置，这些物品只以数据包形式存在于玩家客户端，服务器上没有对应物品实体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| items | item, i | 要掉落的物品列表，此属性的用法与 [DropItem](dropitem.md) 中的对应属性相同。 | iron_sword |
| amount | a | 喷散效果中显示的物品数量。 | 10 |
| duration | d | 物品存在的时间，单位为刻。 | 20 |
| radius | r | 物品初始位置的半径或散布范围。 | 0 |
| velocity | v, force, f | 物品的速度。 | 1 |
| yVelocity | yv, yforce, yf | 物品的 Y 轴速度。 | `velocity` |
| yOffset | yo, y | 物品初始位置的 y 轴偏移。 | 1 |
| allowpickup | ap | itemspray 中的物品是否为真实物品，以便玩家捡起。 | false |
| gravity | g | 物品是否受重力影响。 | true |
| audience |  | 效果的[可见对象](../audience.md)。 | world |

## 示例 {#examples}

```yaml
  Skills:
  - itemspray{item=iron_sword;amount=20;velocity=5;d=100} @self
```

## 别名 {#aliases}

- effect:itemspray
- e:itemspray
