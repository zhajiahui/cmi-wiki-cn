---
title: 方块类型
source: https://docs.phoenixdevt.fr/mmocore/misc/block-types
source_snapshot: '2026-10-19'
---

# 方块类型 {#📦-block-types}

方块类型有助于确定当你[破坏方块](../features/mining.md)时会发生什么（物品掉落、方块再生..）。

通过区分这些块类型，MMOCore可以对它们应用不同的行为。使用具有自定义纹理的玩家头骨，你可以设置小矿石块，这对建筑来说是一个很好的补充。使用 MI 自定义块，你可以拥有具有新纹理、破坏速度和完全可配置的掉落表的块。

## 可用的块类型 {#available-block-types}

下表提供了MMOCore自定义挖矿系统支持的所有区块类型。

|块型 |描述 |示例|
| --- | --- | --- |
| MMOItems定制块 | 当挖掘MMOItems自定义块时。 | `mmoitems{id=6}` |
| 玩家头 | 当挖掘具有自定义纹理的玩家头时。 | `skull{value="aZd9fE8...48dfQX="}` |
| 笔记块 | 挖掘音符块时。 | `note{note=1;instrument=PIANO}` |
| 蘑菇块 | 开采蘑菇块时。 | `mushroom{type=MUSHROOM_STEM,faces="NORTH,EAST"}` |
| 原版块 | 开采任何其他区块时。倒退。 | `vanilla{type=DIAMOND_ORE}` |

注意事项：

- 对于带有纹理的玩家头/头骨，你需要提供头骨的 Base64 纹理值，而不是纹理 URL。
- 对于音符块，音符是从1到24。仪器列表可以在 [Spigotjavadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Instrument.html)中找到。
- 对于蘑菇块，可能的类型为`MUSHROOM_STEM`、`RED_MUSHROOM_BLOCK`和`BROWN_MUSHROOM_BLOCK`。可用面为`UP`、`DOWN`、`NORTH`、`SOUTH`、`EAST`、`WEST`。

## 配置示例 {#example-config}

这是挖矿副职业默认配置的一小部分。

```
on-mine:
    emerald:
        material: vanilla{type=EMERALD_ORE}
        drop-table:
            items:
            - 'vanilla{type=EMERALD} 1 1-9'
        vanilla-drops: false
        regen:
            time: 2000
            temp-block: skull{value="long_texture_value_here"}
```

此配置使原版祖母绿矿石块掉落1为9祖母绿（并取消原版掉落），并用自定义纹理头骨暂时替换它（100秒 =2.000刻）。这意味着你还可以使用这些块类型来选择在破坏特定块后应放置哪些临时块。

## 额外选项 {#extra-options}

你可以使用`age`原版块类型选项来使用块再生生成完全/部分生长的农作物。以下示例将在小麦块被破坏后重新生成完全生长的小麦作物。`vanilla{type=WHEAT,age=7}`

---

原文：[📦 Block Types](https://docs.phoenixdevt.fr/mmocore/misc/block-types) · 原文归档：2026-10-19
