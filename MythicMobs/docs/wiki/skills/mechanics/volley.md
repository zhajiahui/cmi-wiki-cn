---
title: Volley
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/volley
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Volley {#volley}

## 说明 {#description}

向目标实体或位置发射一连串箭或物品弹射物，造成伤害。可以使用射击机制中的任何属性。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 投射物的数量 | 10 |
| source | s | 齐射类型，可为 REGULAR 或 RAIN | REGULAR |
| radius | r | 齐射的散布半径。**仅在 `source=RAIN` 时生效。** | 0 |
| yoffset | y | 降雨式齐射的发射源相对目标的垂直偏移。**仅在 `source=RAIN` 时生效。** | 1 |
| spread | sp | 齐射的散布程度（随机的 yaw/pitch 抖动，以度为单位） | 0 |
| canPickup | pickup | 玩家是否可以捡起箭矢。 | true |

> 该机制继承了[射击](shoot.md)机制的所有*可继承*属性

> **调整REGULAR齐射的原点：** `radius`和`yoffset`仅由`source=RAIN`使用。
> 要改变 `REGULAR` 齐射的产生位置（例如阻止箭头夹入生物下方的地面），
> 使用继承的 Shoot 属性 `startyoffset`（`syo`）、`forwardoffset`（`sfo`）、`startsideoffset`（`sso`）。

## 示例 {#examples}

```yaml
  Skills:
  - volley{type=EGG;velocity=5;damage=10;amount=20}
  # Raise a REGULAR volley so arrows don't spawn in the block below the caster
  - volley{amount=10;spread=5;startyoffset=1.5}
  # A rain of arrows falling in a 4-block radius, 20 blocks above the target
  - volley{source=RAIN;amount=30;radius=4;yoffset=20}
```

## 别名 {#aliases}

- shootvolley
