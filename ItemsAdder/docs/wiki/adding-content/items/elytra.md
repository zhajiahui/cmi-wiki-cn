---
title: "鞘翅"
source_url: "https://wiki.itemsadder.com/adding-content/items/elytra"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 鞘翅

自定义鞘翅需要 **Minecraft 1.21.2+** 和 **ItemsAdder 4.0.18+**。

自定义鞘翅有三个外观部分：

1. 背包和手持时的普通纹理。
2. 可选的损坏状态背包／手持纹理。
3. 渲染在玩家身体上的翅膀纹理。

ItemsAdder 会自动创建所需的胸部装备、启用原版滑翔组件，并生成 `layers.wings` 装备模型。
无需手动创建装备 JSON 或物品模型 JSON 文件。

## 创建内容包

创建新的内容文件夹：

``` text
plugins/ItemsAdder/contents/my_elytras/
├── configs/
│   └── items.yml
└── textures/
    ├── item/
    │   ├── sky_elytra.png
    │   └── sky_elytra_broken.png
    └── entity/
        └── equipment/
            └── wings/
                └── sky_elytra.png
```

## 创建纹理

### 背包纹理

创建普通物品纹理：

``` text
contents/my_elytras/textures/item/sky_elytra.png
```

建议使用标准的 `16x16` 物品纹理。

### 损坏状态背包纹理（可选）

创建损坏纹理：

``` text
contents/my_elytras/textures/item/sky_elytra_broken.png
```

未指定 `broken_item_texture` 时，ItemsAdder 会自动查找以下命名的纹理：

``` text
<normal_item_texture>_broken.png
```

例如：

``` text
item/sky_elytra.png
item/sky_elytra_broken.png
```

损坏纹理只影响背包和手持模型，不会改变玩家身上的翅膀。

### 翅膀纹理

创建穿戴鞘翅时使用的纹理：

``` text
contents/my_elytras/textures/entity/equipment/wings/sky_elytra.png
```

建议使用原版 `64x32` 分辨率；更高分辨率也应保持 `2:1` 比例，例如 `128x64` 或 `256x128`。

ItemsAdder 会将纹理复制到对应版本的资源包覆盖目录，不会修改图片像素。

## 最小配置

创建 `contents/my_elytras/configs/items.yml`：

``` yaml
info:
  namespace: my_elytras

items:
  sky_elytra:
    name: Sky Elytra
    material: ELYTRA
    graphics:
      texture: item/sky_elytra
    elytra:
      wings_texture: entity/equipment/wings/sky_elytra
```

## 配置损坏纹理

### 自动选择

如果文件命名如下：

``` text
sky_elytra.png
sky_elytra_broken.png
```

则可以省略 `broken_item_texture`：

``` yaml
graphics:
  texture: item/sky_elytra
elytra:
  wings_texture: entity/equipment/wings/sky_elytra
```

### 显式指定

也可以明确指定另一张纹理：

``` yaml
elytra:
  wings_texture: entity/equipment/wings/sky_elytra
  broken_item_texture: item/damaged_sky_elytra
```

资源路径可以包含命名空间：

``` yaml
broken_item_texture: my_elytras:item/damaged_sky_elytra
```

`.png` 扩展名可省略，建议不写。

ItemsAdder 会为各个支持的 Minecraft 版本自动生成正确的损坏物品模型状态。

## 鞘翅属性

``` yaml
elytra:
  wings_texture: entity/equipment/wings/sky_elytra
  broken_item_texture: item/sky_elytra_broken
  max_flight_ticks: 0
  firework:
    enabled: true
    consume: true
    cooldown_ticks: 0
  durability_damage_multiplier: 1.0
  collision_damage_multiplier: 1.0
```

| 属性 | 默认值 | 说明 |
| --- | --- | --- |
| `wings_texture` | 必填 | 穿戴鞘翅时显示在玩家身体上的纹理。 |
| `broken_item_texture` | 自动 | 物品损坏时使用的背包和手持纹理。 |
| `max_flight_ticks` | `0` | 最长连续滑翔时间；`0` 表示不限制。 |
| `firework.enabled` | `true` | 使用该鞘翅时是否允许烟花推进。 |
| `firework.consume` | `true` | 成功推进时是否消耗烟花火箭。 |
| `firework.cooldown_ticks` | `0` | 两次成功推进之间的最短间隔。 |
| `durability_damage_multiplier` | `1.0` | 耐久损耗倍率。 |
| `collision_damage_multiplier` | `1.0` | `FLY_INTO_WALL` 碰撞伤害倍率。 |

每秒有 20 tick。例如，以下配置将连续飞行限制为 30 秒：

``` yaml
max_flight_ticks: 600
```

所有 tick 数值必须为非负整数；伤害倍率必须为非负有限数。

## 烟花示例

### 禁用烟花推进

``` yaml
firework:
  enabled: false
```

此限制只在玩家穿戴这件特定自定义鞘翅滑翔时生效。

原版鞘翅和其他自定义鞘翅不受影响。

### 推进时不消耗烟花

``` yaml
firework:
  enabled: true
  consume: false
  cooldown_ticks: 0
```

### 添加两秒冷却

``` yaml
firework:
  enabled: true
  consume: true
  cooldown_ticks: 40
```

本次滑翔结束时，冷却也会清除。

## 伤害倍率

### 耐久损耗减半

``` yaml
durability_damage_multiplier: 0.5
```

### 禁用耐久损耗

``` yaml
durability_damage_multiplier: 0
```

### 撞墙伤害加倍

``` yaml
collision_damage_multiplier: 2.0
```

### 禁用撞墙伤害

``` yaml
collision_damage_multiplier: 0
```

这些倍率只作用于当前穿戴的这件自定义鞘翅。原版及其他自定义鞘翅维持各自行为。

ItemsAdder 不会替代原版附魔系统；耐久、经验修补等适用附魔仍正常生效。

## 事件与动作

自定义鞘翅提供四个额外物品事件：

| 事件 | 触发时机 |
| --- | --- |
| `glide_start` | 玩家使用此自定义鞘翅开始滑翔。 |
| `glide_stop` | 本次滑翔结束、超时或鞘翅被卸下。 |
| `elytra_boost` | 使用了一次获准的烟花推进。 |
| `elytra_collision` | 玩家受到 `FLY_INTO_WALL` 碰撞伤害。 |

它们使用标准的 ItemsAdder 动作系统：

``` yaml
events:
  glide_start:
    play_sound:
      name: entity.ender_dragon.flap
      volume: 1
      pitch: 1.2

  glide_stop:
    play_sound:
      name: block.note_block.bass
      volume: 1
      pitch: 0.8

  elytra_boost:
    play_sound:
      name: entity.firework_rocket.launch
      volume: 1
      pitch: 1.3

  elytra_collision:
    play_sound:
      name: entity.player.hurt
      volume: 1
      pitch: 0.7
```

这些事件中可使用已有的任何物品动作。

## 完整示例

``` yaml
info:
  namespace: my_elytras

items:
  sky_elytra:
    name: Sky Elytra
    material: ELYTRA

    graphics:
      texture: item/sky_elytra

    elytra:
      wings_texture: entity/equipment/wings/sky_elytra
      # Optional. If omitted, item/sky_elytra_broken.png is detected automatically.
      broken_item_texture: item/sky_elytra_broken

      # 0 means unlimited flight.
      max_flight_ticks: 0

      firework:
        enabled: true
        consume: true
        cooldown_ticks: 0

      durability_damage_multiplier: 1.0
      collision_damage_multiplier: 1.0

    events:
      glide_start:
        play_sound:
          name: entity.ender_dragon.flap
          volume: 1
          pitch: 1.2

      glide_stop:
        play_sound:
          name: block.note_block.bass
          volume: 1
          pitch: 0.8

      elytra_boost:
        play_sound:
          name: entity.firework_rocket.launch
          volume: 1
          pitch: 1.3

      elytra_collision:
        play_sound:
          name: entity.player.hurt
          volume: 1
          pitch: 0.7
```

## 显式设置装备属性

`elytra` 配置段会自动创建必需的装备配置；有需要时仍可添加兼容的装备属性：

``` yaml
equipment:
  sound: item.armor.equip_elytra
  dispensable: true
  swappable: true
  damage_on_hurt: true
```

若明确配置以下属性，必须确保它们与鞘翅兼容：

``` yaml
equipment:
  id: my_elytras:sky_elytra
  slot: CHEST
  glider: true
  allowed_entities:
    - PLAYER
```

ItemsAdder 会拒绝不兼容的属性值，避免生成无效物品。

装备 ID 必须与物品 ID 相同，槽位必须为 `CHEST`，`glider` 必须为 `true`，`allowed_entities` 必须包含 `PLAYER`。

## 生成并测试资源包

1. 保存配置和 PNG 文件。
2. 执行通常的 ItemsAdder 重载与资源包生成流程，例如 `/iazip`。
3. 确认客户端已应用更新后的资源包。
4. 给自己物品：

``` text
/iaget my_elytras:sky_elytra
```

5. 将它装备到胸部槽位。
6. 开始滑翔，检查翅膀纹理。
7. 用烟花测试推进规则。
8. 降低耐久度，验证背包中的损坏纹理。

## 故障排查

### 翅膀纹理缺失

请检查：

- 客户端版本为 Minecraft 1.21.2 或更新。
- `wings_texture` 指向现有 PNG 文件。
- 命名空间正确。
- 已生成并接受更新后的资源包。
- 资源路径相对于 `textures` 文件夹。

例如：

``` yaml
wings_texture: my_elytras:entity/equipment/wings/sky_elytra
```

对应文件：

``` text
contents/my_elytras/textures/entity/equipment/wings/sky_elytra.png
```

### 背包纹理变化了，但穿戴的翅膀没有变化

`graphics.texture` 和 `broken_item_texture` 仅控制背包及手中的物品外观。

穿戴外观始终使用 `wings_texture`。

### 没有显示损坏纹理

使用自动选择时，确认文件名以 `_broken.png` 结尾：

``` text
sky_elytra.png
sky_elytra_broken.png
```

也可以改为显式配置：

``` yaml
broken_item_texture: item/sky_elytra_broken
```

### 装备设置被拒绝

先移除多余的显式装备属性。`elytra` 段已自动配置胸部槽位、装备 ID、玩家兼容性和滑翔组件。

## 可直接使用的测试示例

以下物品可用于验证主要鞘翅属性。请在命名空间的 `textures/item` 文件夹中创建引用的纹理。

``` yaml
info:
  namespace: my_elytras

items:
  baseline_elytra:
    name: Baseline Elytra
    material: ELYTRA
    graphics:
      texture: item/baseline_elytra
    durability:
      max_durability: 12
    elytra:
      wings_texture: item/baseline_elytra_wings
      max_flight_ticks: 0
      firework:
        enabled: true
        consume: true
        cooldown_ticks: 0
      durability_damage_multiplier: 1.0
      collision_damage_multiplier: 1.0

  timed_safe_elytra:
    name: Timed Safe Elytra
    material: ELYTRA
    graphics:
      texture: item/timed_safe_elytra
    durability:
      max_durability: 12
    elytra:
      wings_texture: item/timed_safe_elytra_wings
      max_flight_ticks: 100
      firework:
        enabled: false
        consume: true
        cooldown_ticks: 0
      durability_damage_multiplier: 0.5
      collision_damage_multiplier: 0.0

  boost_heavy_elytra:
    name: Boost Heavy Elytra
    material: ELYTRA
    graphics:
      texture: item/boost_heavy_elytra
    durability:
      max_durability: 12
    elytra:
      wings_texture: item/boost_heavy_elytra_wings
      broken_item_texture: item/boost_heavy_explicit_broken
      max_flight_ticks: 0
      firework:
        enabled: true
        consume: false
        cooldown_ticks: 60
      durability_damage_multiplier: 2.0
      collision_damage_multiplier: 2.0
```

- **基础鞘翅：**保留类似原版的飞行、烟花消耗和伤害行为。
- **限时安全鞘翅：**滑翔 5 秒后停止，禁用烟花推进，耐久损耗减半，并免除撞墙伤害。
- **强力推进鞘翅：**烟花推进不消耗火箭，冷却 3 秒，耐久损耗和碰撞伤害加倍。

前两个物品可添加 `<normal_texture>_broken.png` 测试自动识别损坏纹理；第三个示例演示显式 `broken_item_texture`。

## 示例鞘翅包

[示例内容包](https://www.spigotmc.org/resources/simplyelytras-8-custom-elytras.138297/)
