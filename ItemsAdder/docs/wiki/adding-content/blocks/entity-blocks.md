---
title: "实体方块"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/entity-blocks"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 实体方块
# 实体方块

服务端和客户端均需要 Minecraft 1.21.4+，并需要 ItemsAdder 4.0.18+。

`ENTITY` 方块类型通过展示实体渲染自定义模型，同时保留普通完整方块的碰撞箱，不占用自定义方块状态槽位。

> 碰撞箱始终占据完整的一格，即使外观模型较小或形状不同也一样。

## 创建内容包

创建以下文件夹和文件：

``` text
contents/my_entity_blocks/
├── configs/
│   └── blocks.yml
└── textures/
    └── block/
        └── ruby_block.png
```

对于普通立方体方块，建议使用正方形 `16x16` 纹理。

## 最小配置

创建 `contents/my_entity_blocks/configs/blocks.yml`：

``` yaml
info:
  namespace: my_entity_blocks

items:
  ruby_block:
    name: Ruby Block

    graphics:
      texture: block/ruby_block

    behaviours:
      block:
        placed_model:
          type: ENTITY
          break_particles: ITEM
```

ItemsAdder 会根据纹理自动生成立方体模型。

## 为每个面使用不同纹理

在 `textures/block/` 中创建六张纹理，然后将 `graphics` 配置节替换为：

``` yaml
graphics:
  textures:
    down: block/ruby_block_down
    up: block/ruby_block_up
    north: block/ruby_block_north
    south: block/ruby_block_south
    west: block/ruby_block_west
    east: block/ruby_block_east
```

`.png` 扩展名可省略。

## 使用自定义模型

将模型及其纹理放入内容包：

``` text
contents/my_entity_blocks/
├── models/
│   └── block/
│       └── ruby_crate.json
└── textures/
    └── block/
        └── ruby_crate.png
```

然后在物品配置中使用该模型：

``` yaml
graphics:
  model: block/ruby_crate
```

模型 JSON 必须使用正确的命名空间引用纹理，例如：

``` json
"my_entity_blocks:block/ruby_crate"
```

如果条件允许，建议使用自动生成的立方体模型，因为 ItemsAdder 可以自动优化成组的相邻兼容方块。

## 方向性方块

如果方块应根据放置的面旋转，请添加 `directional_mode`：

``` yaml
behaviours:
  block:
    placed_model:
      type: ENTITY
      directional_mode: FURNACE
      break_particles: ITEM
```

可用模式：

| 模式 | 旋转方式 |
| --- | --- |
| `FURNACE` | 水平四个方向 |
| `LOG` | 三个轴，类似原木 |
| `DROPPER` | 六个方向 |
| `ALL` | 六个方向，并完整旋转模型 |

只有模型本身或各个面的外观不同时，方向模式才有用。

也可以用 `rotx` 和 `roty` 配置固定旋转角度：

``` yaml
placed_model:
  type: ENTITY
  rotx: 0
  roty: 90
```

## 回退方块

无法显示自定义展示实体时，玩家会看到原版回退方块。默认值为 `GRAY_CONCRETE`。

可为每个方块选择不同的回退方块：

``` yaml
behaviours:
  block:
    fallback_vanilla_block: RED_CONCRETE
    placed_model:
      type: ENTITY
      break_particles: ITEM
```

回退方块必须为无重力、不可交互的实心方块。混凝土和石头可用；箱子、沙子和玻璃不可用。

## 生成与测试

1. 保存配置和纹理文件。
2. 执行平时使用的 ItemsAdder 重载及资源包生成命令，例如 `/iazip`。
3. 确认客户端已接受更新后的资源包。
4. 获取该方块：

``` text
/iaget my_entity_blocks:ruby_block
```

5. 放置并破坏方块，检查模型、旋转、粒子和碰撞箱。

## 服务端限制

实体方块的限制在 ItemsAdder 主配置 `config.yml` 中设置：

``` yaml
blocks:
  custom:
    entity:
      enabled: true
      render-radius: 48
      max-displays-per-player: 512
      max-blocks-per-chunk: 256
      fallback-vanilla-block: GRAY_CONCRETE
```

`max-blocks-per-chunk` 用于避免一个区块内放置过多实体方块。设为 `0` 可禁用此放置数量限制。

除非有明确的调整需求，否则保留默认值。

## 故障排查

### 自定义模型被原版方块替代

请检查：

- 服务端和客户端均使用 Minecraft 1.21.4 或更新版本。
- 已在 `config.yml` 中启用实体方块。
- 方块位于配置的渲染半径内。
- 尚未达到每位玩家的展示实体数量上限。

超出渲染范围后显示回退方块属于正常现象。

### 缺少纹理

请检查：

- PNG 文件存在于该命名空间的 `textures` 文件夹中。
- `graphics` 中的路径相对于该文件夹。
- 命名空间正确。
- 已生成并接受更新后的资源包。

例如：

``` yaml
graphics:
  texture: my_entity_blocks:block/ruby_block
```

对应文件：

``` text
contents/my_entity_blocks/textures/block/ruby_block.png
```

### 无法放置方块

区块可能已经达到 `max-blocks-per-chunk` 上限。请谨慎提高上限，或设为 `0` 以禁用限制。

### 模型方向错误

使用合适的 `directional_mode`，或调整固定的 `rotx` 和 `roty` 数值。

