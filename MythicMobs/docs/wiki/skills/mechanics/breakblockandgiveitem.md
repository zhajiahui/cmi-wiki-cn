---
title: Break Block And Give Item
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/breakBlockAndGiveItem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Break Block And Give Item {#break-block-and-give-item}

## 说明 {#description}

破坏目标位置的方块并提供物品，也会掉落方块物品，基岩除外。必须设置 `forcesync=true`。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| dodrops | drops, d | 是否掉落方块。 | true |
| doeffect | effect, e | 是否播放方块破坏粒子 (?) | true |
| usetool | tool, t | 是否使用玩家手中的工具 (?) | true |
| doFakeLooting | fakeLooting, fl | 从原点播放拾取物品动画。 | false |
| items | item, i | 物品材质或掉落表数组。 |  |

## 示例 {#examples}

使用 Crucible 物品：

它不会掉落泥土，而是会给玩家钻石。

```yaml
#Items Document
CustomItem:
  Id: GOLDEN_SHOVEL
  Display: 'Lucky Shovel'
  Skills:
  - skill{s=dirtToDiamonds;sync=true} @origin ~onBreakBlock

#Skills Document
dirtToDiamonds:
  TargetConditions:
  - blocktype{t=DIRT,GRASS_BLOCK} true
  Skills:
  - breakBlockAndGiveItem{dodrops=false;items=diamond}
```

## 别名 {#aliases}

- blockBreakAndGiveItem
