---
title: "方块"
source_url: "https://wiki.itemsadder.com/adding-content/blocks"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 方块

## 方块属性

```yaml
behaviours:
  block:
    placed_model:
      type: REAL_NOTE
      break_particles: BLOCK
      rotx: 0
      roty: 0
    drop_when_mined: true
    light_level: 12 # make block emit light
    # tools you can't use to break block (accepts partial name of material/customitem)
    break_tools_blacklist:
    - WOODEN_PICKAXE
    - STONE_PICKAXE
    - IRON_PICKAXE
    # tools you can use to break block (accepts partial name of material/customitem)
    break_tools_whitelist:
    - DIAMOND_PICKAXE
    - PICKAXE
    - pickaxe
    hardness: 2
    blast_resistance: 1 # explosion resistance (by default is hardness * 3)
    no_explosion: false # totally immune from explosions, ignoring blast_resistance
    sound: # customizable sounds of the block
      break:
        name: BLOCK_WOOD_BREAK
        volume: 1
        pitch: 0.9
      place:
        name: BLOCK_WOOD_PLACE
        volume: 1
        pitch: 0.9
```

## `placed_model`

### `type`

此属性可使用以下值：

* `REAL_NOTE`
  * 使用真实方块（note_block），没有实体，不造成卡顿，100% 为真实方块。
  * 限制：
    * **不支持透明**。
    * 总计**最多 750 个方块**。
* `REAL`
  * 使用真实方块（蘑菇），没有实体，不造成卡顿，100% 为真实方块。（不过建议使用更稳定的 `REAL_NOTE`。）
  * 限制：
    * 总计**最多 191 个方块**
* `REAL_TRANSPARENT`
  * 使用真实方块（紫颂植物），没有实体，不造成卡顿，100% 为真实方块，并支持透明！
  * 限制：
    * 总计**最多 63 个方块**。
* `REAL_WIRE`
  * 使用真实方块（绊线），没有实体，不造成卡顿，100% 为真实方块。
  * 限制：
    * 总计**最多 127 个方块**。
* `TILE`
  * 使用 **tile** 方块（带自定义外观的修改版**刷怪笼**）。它**不是实体**，但存在一些限制。优点是可以创建**无限数量的方块**，没有 **REAL** 方块的数量限制。
  * 限制：
    * 并非 100% 的真实方块，而是更换纹理的刷怪笼。
    * 距离较远时纹理或模型会消失，露出刷怪笼的原版纹理。
    * 玩家视野内有大量方块时，可能造成客户端卡顿，但只影响配置较低的电脑。
* `FIRE`
  * 这是**特殊方块**类型，使用**火**方块。
  * 限制：
    * 自定义**火焰最多只能有 14 种**，因此只创建需要的种类。

- **`REAL`** 和 **`REAL_NOTE`** 用于装饰方块和矿石。
- **`TILE`** 方块用于交易机器、机械/稀有装饰方块。\
  不应将 **`TILE`** 方块用于矿石，因为它_**可能**_在区块生成时造成卡顿。不建议将其用于[地物生成器](world-generation/trees-populators.md)或[装饰器](world-generation/cave-decorators.md)。

### `rotx` 和 `roty`

可为特定模型指定旋转角度，适用于熟悉相关配置的用户。\
这里的旋转是静态的，不会动态变化。它适合用来创建同一方块的多个变体，无需手动单独制作模型。

### `placeable_on_water`

允许部分方块直接放置在**水面**上。

### **`placeable_on_lava`**

允许部分方块直接放置在**熔岩表面**上。

### `placeable_on_other_real_wire`

设置 `REAL_WIRE` 方块是否可以放在其他 `REAL_WIRE` 方块上。

### `shift_up`

允许部分方块向上偏移 1 格。可用 `REAL_WIRE` 方块制作高大植物。

### `custom_variants`

[variants.md](blocks/variants.md)

### `drop_when_mined`

自 ItemsAdder 4.0.9 起可用。

旧版本使用 `cancel_drop`，其中 `true/false` 的含义相反。

控制方块被挖掘后是否掉落。如果方块会产出矿物等战利品，可用此项避免重复获取。

### `drop_on_shears`

自 ItemsAdder 4.0.9 起可用。

控制使用剪刀时是否掉落方块。

### `drop_on_silk_touch`

自 ItemsAdder 4.0.9 起可用。

控制使用带精准采集附魔的工具时是否掉落方块。

使用带精准采集附魔的工具破坏方块时，仍会获得方块本身，但不会获得战利品中的任何物品

## 工具黑名单和白名单

可以设置“_PICKAXE”来匹配所有镐，也可以设置“_AXE”。插件会检查材质名是否包含规则中设置的文字。\
同样适用于自定义物品 ID。例如设置“ruby_”后，所有 ruby 工具都会匹配（ruby_pickaxe、ruby_axe 等）。

### `break_tools_blacklist`

无法破坏此方块的工具黑名单。

### `break_tools_whitelist`

可以破坏此方块的工具白名单。

### `events_tools_blacklist`

无法在此方块上触发事件的工具黑名单[（`placed_block.interact`）](items/item-properties/events/events-list.md)

### `events_tools_whitelist`

可以在此方块上触发事件的工具白名单[（`placed_block.interact`）](items/item-properties/events/events-list.md)

## 其他选项

### `hardness`

方块硬度，数值越高越难挖掘。\
示例可参考现有方块（查看 **itemsadder 命名空间**中的 **blocks.yml** 文件）。

将 `hardness` 设为 `-1` 可让方块立即被破坏。

### `blast_resistance`

爆炸抗性（默认为 `hardness * 3`）。

### `no_explosion`

完全免疫爆炸，忽略 `blast_resistance`。

### `sounds`

可以使用[自定义声音](adding-sounds.md)名称代替原版声音。\
可以指定 [Spigot 声音](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html)或原版 [Minecraft 声音](https://www.digminecraft.com/lists/sound_list_pc.php)名称。

未指定声音时使用**石头**方块的声音。

#### 使用原版声音的示例

```yaml
    behaviours:
      block:
        placed_model:
          type: REAL_NOTE
          break_particles_material: PRISMARINE_BRICKS
        break_tools_whitelist:
          - PICKAXE
          - pickaxe
        sound:
          break:
            name: minecraft:block.amethyst_block.break
          place:
            name: minecraft:block.amethyst_block.place
          hit:
            name: minecraft:block.amethyst_block.hit
          step:
            name: minecraft:block.amethyst_block.step
          fall:
            name: minecraft:block.amethyst_block.fall

```

#### 使用自定义声音的示例

```yaml
    sound:
      break:
        name: my_sounds:sound_1
      place:
        name: my_sounds:sound_2
      hit:
        name: my_sounds:sound_3
      step:
        name: my_sounds:sound_4
      fall:
        name: my_sounds:sound_5
```

向资源包添加自定义声音的方法见[声音教程](adding-sounds.md)。

### `permission_suffix`

该属性允许你为方块放置/破坏事件启用权限。\
默认不设置此项，以便玩家自由破坏和放置方块。\
指定这些属性后，玩家需要明确授予相应权限：

* `ia.user.block.break.iasurvival.ruby_ore`
* `ia.user.block.place.iasurvival.ruby_ore`

```yaml
info:
  namespace: iasurvival
items:
  ruby_ore:
    enabled: true
    display_name: display-name-ruby_ore
    permission: iasurvival.items.ruby_ore
    resource:
      material: PAPER
      generate: true
      textures:
        - block/ores/ruby_ore
    behaviours:
      block:
        permission_suffix:
          break: iasurvival.ruby_ore
          place: iasurvival.ruby_ore
        hardness: 4
        placed_model:
          type: REAL_NOTE
          break_particles_material: REDSTONE_ORE
        cancel_drop: true
        break_tools_blacklist:
          - WOODEN_PICKAXE
          - STONE_PICKAXE
        break_tools_whitelist:
          - PICKAXE
          - pickaxe
          - _hammer
```

### 使用官方文件编辑器查看全部属性

指南

## 方块掉落经验

**有 2 种方法让自定义方块掉落经验。**

### 1. 在创建自定义方块时直接添加经验掉落

这有一个缺点，你只能向自定义方块添加经验掉落，原版方块不行。

```yaml
  ruby_block:
    display_name: display-name-ruby_block
    permission: ruby_block
    resource:
      material: PAPER
      generate: true
      textures:
      - block/ruby_block.png
    behaviours:
      block:
        placed_model:
          type: REAL_NOTE
          break_particles_material: REDSTONE_BLOCK
        break_tools_whitelist:
        - PICKAXE
        - pickaxe
    events:
      placed_block:
        break:
          drop_exp:
            chance: 100
            min_amount: 0
            max_amount: 3
```

### 2. 向战利品添加经验

这是最好的方法，因为您也可以将其应用于原版方块类型，并且可以添加任意数量的经验设置。这允许您为您的掉落物添加更多的随机性和动态性。

```yaml
loots:
  blocks:
    ruby_ore:
      type: iasurvival:ruby_ore
      items:
        ruby:
          item: iasurvival:ruby
          min_amount: 1
          max_amount: 2
          chance: 100
      exp:
        exp_1:
          min_amount: 0
          max_amount: 3
          chance: 100
```
