---
title: "触发数值变化"
source_url: "https://wiki.itemsadder.com/adding-content/font-images/huds/trigger-value-change"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 触发数值变化

## 使 HUD 值动态化

使用 ItemsAdder，您可以轻松地使 HUD 值在游戏过程中自动变化，例如，您可以使 HUD 值逐渐减少。

在这个例子中，我将解释**口渴** HUD 是如何工作的。

## 口渴 HUD 是如何工作的？

口渴 HUD 会根据一些因素自动减少：生物群系、您在家中或在外面，以及在没有任何特定因素的情况下在游戏过程中一般会减少。

我知道这个 HUD 系统缺乏一些功能，可能有点令人困惑，未来我会对其进行改进，增加更多功能并使其更好。

如果需要更精细地控制 HUD，应使用 [Java API](https://wiki.itemsadder.com/developers/java-api)。

这是 HUD 配置文件：

```yaml
info:
  namespace: realcraft
huds:
  thirst_bar:
    enabled: true
    show:
      auto: true
      creative: false
      underwater: false
      riding: false
    type: STATUS
    x_position_pixels: 10
    direction: LEFT
    value:
      player_stat_name: thirst
      start: 10
      min: 0
      max: 10
      triggers:
        decrement:
          generic_over_time_60_minutes_inside:
            min_sky_light: 0
            max_sky_light: 13
            every_ticks: 30000
            amount: 0.5
          generic_over_time_45_minutes_outside:
            min_sky_light: 14
            max_sky_light: 15
            every_ticks: 30000
            amount: 0.5
          biome_over_time_desert_30_minutes_outside:
            min_sky_light: 14
            max_sky_light: 15
            biome: DESERT
            every_ticks: 30000
            amount: 0.5
          food_level_change:
            amount: 0.1
        increment:
          food_level_change:
            amount: 0.1
          player_respawn:
            amount: 10
        on_min_value:
          damage_player:
            every_ticks: 100
            damage: 0.5
          potion_effect:
            every_ticks: 100
            type: SLOW
            amplifier: 1
            duration: 100
    images:
      positive: realcraft:thirst_bar_positive
      half: realcraft:thirst_bar_half
      negative: realcraft:thirst_bar_negative

```

## 触发器

在 ItemsAdder 中，您可以使用触发器来决定如何使 HUD 值变化，有两种触发器：`decrement`、`increment` 和 `on_min_value`。

`decrement` 触发器使 HUD 值减少，`increment` 触发器使其增加。

`on_min_value` 是一个特殊的触发器，当 HUD 值达到最小值时，它会运行其规则。

每个触发器都有一个可能的规则列表，告诉 ItemsAdder 是否可以更改 HUD 值。

## 规则

`triggers` 有一些特定的规则，并不是每个触发器都可用，请参考此列表：

### `decrement` 触发器

```yaml
      triggers:
        decrement:
          generic_over_time:
            min_sky_light: 0
            max_sky_light: 13
            every_ticks: 30000
            amount: 0.5
          biome_over_time:
            min_sky_light: 14
            max_sky_light: 15
            biome: DESERT
            every_ticks: 30000
            amount: 0.5
          food_level_change:
            amount: 0.1
```

* `generic_over_time`：天空光照等级介于 0 和 13 之间时（表示玩家位于建筑内部），每隔 30000 刻让 HUD 值减少 0.5。
* `biome_over_time`：天空光照等级介于 14 和 15 之间时（表示玩家位于户外），且生物群系为 `DESERT` 时，每隔 30000 刻让 HUD 值减少 0.5。
* `food_level_change` 使 HUD 值在饱食度下降时减少 0.1（原版）。

### `increment` 触发器

```yaml
  triggers:
    increment:
      generic_over_time:
        min_sky_light: 0
        max_sky_light: 13
        every_ticks: 30000
        amount: 0.5
      biome_over_time:
        min_sky_light: 14
        max_sky_light: 15
        biome: DESERT
        every_ticks: 30000
        amount: 0.5
      food_level_change:
        amount: 0.1
      player_respawn:
        amount: 10
```

* `generic_over_time`：天空光照等级介于 0 和 13 之间时（表示玩家位于建筑内部），每隔 30000 刻让 HUD 值增加 0.5。
* `biome_over_time`：天空光照等级介于 14 和 15 之间时（表示玩家位于户外），且生物群系为 `DESERT` 时，每隔 30000 刻让 HUD 值增加 0.5。
* `food_level_change` 使 HUD 值在饱食度增加时减少 0.1（原版，即玩家进食时）。
* `player_respawn`使 HUD 值在玩家死亡后重生时增加 10，在这种情况下，这有助于使玩家的口渴值在重生时增加到最大值。

### `on_min_value`触发器

这是一个特殊的触发器，它不会改变 HUD 值，但用于在 HUD 值达到最小值时使某些事情发生。

```yaml
  triggers:
    on_min_value:
      damage_player:
        every_ticks: 100
        damage: 0.5
      potion_effect:
        every_ticks: 100
        type: SLOW
        amplifier: 1
        duration: 100
```

* `damage_player`：每隔 100 刻对玩家造成 0.5 点伤害。
* `potion_effect`：每隔 100 刻给予玩家 SLOW 效果，强度为 1、持续时间为 100。本例意味着玩家会持续受到缓慢效果，直到 HUD 值以某种方式增加。
