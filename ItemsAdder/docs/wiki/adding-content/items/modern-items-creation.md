---
title: "1.21.4+：现代物品创建"
source_url: "https://wiki.itemsadder.com/adding-content/items/modern-items-creation"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 1.21.4+：现代物品创建

需要 ItemsAdder 4.0.13，且 Minecraft 客户端和服务端均为 1.21.4+。

## 什么是现代物品方法？

这是创建物品外观的新方式。新的 `graphics` 属性替代旧版 `resource`，更易使用，也提供更多功能。

目前仍保留 `resource`，旧方法依然可用。

如果服务器允许 1.21.3 或更早版本客户端加入，仍需继续使用旧方法，否则这些客户端看不到自定义外观。

## 自动生成物品

`material` 不再必填，默认使用 `paper`。

### 从纹理生成

从纹理自动生成现代物品及模型。

```yaml
  modern_texture:
    name: Modern Texture
    graphics:
      texture: item/modern_texture
```

### 从模型生成

自动生成现代物品，并使用指定的模型文件。

```yaml
  modern_model:
    name: Modern Model
    graphics:
      model: item/modern_model
```

### 从多张纹理创建方块

ItemsAdder 检测到方块 `behaviour` 后，会自动采用 `block/cube` 作为父模型。

如果没有指定方块行为，则使用 `paper` 对应的父模型 `minecraft:item/generated`。

```yaml
  modern_textures_block:
    name: Modern Model Block Textures
    graphics:
      textures:
        north: block/modern_textures_block_north
        south: block/modern_textures_block_south
        east: block/modern_textures_block_east
        west: block/modern_textures_block_west
        up: block/modern_textures_block_up
        down: block/modern_textures_block_down
    behaviours:
      block:
        placed_model:
          type: REAL_NOTE
```

### 从单张纹理创建方块

自动生成现代物品并使用指定模型文件；本例会生成多面方块。

```yaml
  modern_textures_block_2:
    name: Modern Model Block Textures 2
    graphics:
      texture: block/modern_textures_block_all
    behaviours:
      block:
        placed_model:
          type: REAL_NOTE
```

### 从指定父模型创建方块（例如 `cross`）

根据纹理自动生成现代物品和模型；本例会生成多面方块。

本例为待生成的模型设置自定义父模型，并指定连接到 cross 模板的纹理。

```yaml
  modern_textures_block_cross:
    name: Modern Model Block Textures Cross
    graphics:
      icon: block/modern_textures_block_all
      parent: block/cross
      textures:
        cross: block/modern_textures_block_all
    behaviours:
      block:
        placed_model:
          type: REAL_WIRE
```

也可只设置 `texture`。原版 `block/cross` 只有一个纹理层（`cross`），ItemsAdder 会自动分配纹理。

```yaml
  modern_textures_block_cross:
    name: Modern Model Block Textures Cross
    graphics:
      icon: block/modern_textures_block_all
      parent: block/cross
      texture: block/modern_textures_block_all
    behaviours:
      block:
        placed_model:
          type: REAL_WIRE
```

### 从纹理创建弓

```yaml
  modern_bow:
    name: Modern Bow
    material: bow
    graphics:
      textures:
        normal: item/modern_bow
        pulling_0: item/modern_bow_0
        pulling_1: item/modern_bow_1
        pulling_2: item/modern_bow_2
```

### 从模型创建弓

```yaml
  modern_bow_models:
    name: Modern Bow Models
    material: bow
    graphics:
      models:
        normal: item/modern_bow
        pulling_0: item/modern_bow_0
        pulling_1: item/modern_bow_1
        pulling_2: item/modern_bow_2
```

### 从纹理创建钓鱼竿

```yaml
  modern_fishing_rod:
    name: Modern Fishing Rod
    material: fishing_rod
    graphics:
      textures:
        normal: item/modern_fishing_rod
        cast: item/modern_fishing_rod_2
```

### 从模型创建钓鱼竿

```yaml
  modern_fishing_rod_models:
    name: Modern Fishing Rod Models
    material: fishing_rod
    graphics:
      models:
        normal: item/modern_fishing_rod
        cast: item/modern_fishing_rod_2
```

### 从纹理创建弩

可按需创建任意数量的 `pulling_` 状态。

```yaml
  modern_crossbow:
    name: Modern Crossbow
    material: crossbow
    graphics:
      textures:
        normal: item/modern_crossbow
        pulling_0: item/modern_crossbow_0
        pulling_1: item/modern_crossbow_1
        pulling_2: item/modern_crossbow_2
        rocket: minecraft:item/diamond
        arrow: minecraft:item/emerald
```

### 从模型创建弩

可按需创建任意数量的 `pulling_` 状态。

```yaml
  modern_crossbow_model:
    name: Modern Crossbow Model
    material: crossbow
    graphics:
      models:
        normal: item/modern_bow
        pulling_0: item/modern_crossbow_0
        pulling_1: item/modern_crossbow_1
        pulling_2: item/modern_crossbow_2
        rocket: minecraft:item/diamond
        arrow: minecraft:item/emerald
```

### 从模型创建三叉戟

```yaml
  modern_trident_model:
    name: Modern Trident Model
    material: trident
    graphics:
      icon: minecraft:item/diamond
      models:
        normal: item/modern_trident
        throwing: item/modern_trident_2
```

### 从模型创建盾牌

```yaml
  modern_shield_model:
    name: Modern Shield Model
    material: shield
    graphics:
      models:
        normal: item/modern_shield
        blocking: item/modern_shield_2
```

## 其他可选属性

### 材质

```yaml
  modern_texture:
    name: Modern Texture
    material: paper
    graphics:
      texture: item/modern_texture
```

### 图标 <a id="icon"></a>

为背包槽位设置不同于游戏中外观的独立纹理。

```yaml
  modern_texture:
    name: Modern Texture
    graphics:
      texture: item/modern_texture
      icon: item/modern_texture_icon
```

### 禁用切换物品时的手部动画

```yaml
  modern_texture:
    name: Modern Texture
    graphics:
      texture: item/modern_texture
      hand_animation_on_swap: false
```

### 在界面中超出槽位显示

让物品在背包和 GUI 中渲染得比普通槽位更大。

```yaml
  modern_texture:
    name: Modern Model
    graphics:
      model: item/modern_model
      oversized_in_gui: true
```

## 高级配置

### `item_model`

使用新的 1.21.4 格式自行管理物品模型。


```yaml
  modern_item:
    name: Modern Texture
    material: paper
    item_model: test:modern_item
```

## 模板与变体

可以方便地创建物品变体。\
变体会继承模板物品的全部属性；模板本身不会出现在游戏中。

```yaml
info:
  namespace: test_template_furniture
items:
  chair_template:
    template: true # Here
    name: ""
    graphics:
      model: furniture/chair
    behaviours:
      furniture:
        entity: item_display
        solid: true
        fixed_rotation: true
        hitbox:
          length: 1
          width: 1
          height: 1
        placeable_on:
          walls: false
          ceiling: false
          floor: true
      furniture_sit:
        sit_height: 0.75
  black_acacia_chair:
    variant_of: chair_template
    name: "Black Acacia Chair"
    graphics:
      parent: furniture/chair
      textures:
        wood: minecraft:block/acacia_planks
        wool: minecraft:block/black_wool
  red_chair:
    variant_of: chair_template # Here
    name: "Black Acacia Chair"
    graphics:
      parent: furniture/chair
      textures:
        wood: minecraft:block/red_wool
        wool: minecraft:block/red_wool

```

```jsonc
{
  "textures": {
    "wool": "block/white_wool",
    "particle": "block/oak_planks",
    "wood": "block/oak_planks"
  },
  "elements": [
    // ... model elements ...
  ]
}
```
