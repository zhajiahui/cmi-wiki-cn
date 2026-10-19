---
title: "TNT"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/tnt"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# TNT

需要 ItemsAdder 4.0.15+

## 自定义 TNT

使用自定义方块的 `primeable` 设置创建自定义 TNT。

### `radius`

爆炸半径。默认 `4`。

### `damage_multiplier`

应用于原版 TNT 爆炸的倍率。默认 `1`。

### `waterproof`

爆炸是否在水下生效。默认 `true`。

### `incendiary`

爆炸是否会使周围起火。默认 `false`。

### `fuse_ticks`

爆炸前的等待时长。默认 `80`。

### `triggers`

使方块爆炸的条件。

#### `tools`

交互时可以触发爆炸的工具列表。\
支持通配符 `*`；使用 `hand` 可允许空手触发方块。

默认没有任何物品可以触发爆炸。

#### `flaming_projectile`

燃烧的投射物是否可以触发方块（例如着火的箭）。默认 `false`。

#### `redstone`

红石信号是否会触发方块。默认 `false`。

#### `fire`

火是否会触发方块。默认 `false`。

#### `explosion`

其他爆炸是否会触发方块。默认 `false`。

## TNT 方块示例

```yaml
info:
  namespace: test_tnt
items:
  dark_tnt:
    name: Dark Tnt
    graphics:
      textures:
        down: block/tnt_bottom
        up: block/tnt_top
        south: block/tnt_side
        north: block/tnt_side
        east: block/tnt_side
        west: block/tnt_side
    behaviours:
      block:
        placed_model:
          type: REAL_NOTE
        drop_when_mined: true
        primeable:
          radius: 4
          damage_multiplier: 1
          waterproof: false
          incendiary: false
          fuse_ticks: 30
          triggers:
            tools:
            - diamond_*
            flaming_projectile: true # Default false
            redstone: true # Default false
            fire: true # Default false
            explosion: true # Default false

```
