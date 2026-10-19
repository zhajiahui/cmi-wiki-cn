---
title: "动作列表"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/actions/actions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 动作列表

## 动作

### `cancel`

取消触发此动作的事件。

### `play_sound`

播放原版声音或自定义声音。

```yaml
play_sound:
  name: entity.villager.ambient # or a custom sound
  volume: 1.0 # Optional (Default value: 1.0)
  pitch: 1.0 # Optional (Default value: 1.0)
  category: MASTER # Optional (Default value: MASTER)
  stop_previous: false # Optional (Default value: true) - Whether to stop this sound if it was playing before playing it again
```

* `name`：原版值见[此列表](https://minecraft.wiki/w/Sounds.json/Java_Edition_values)；自定义声音使用 `namespace:value`。
* `category`：可用值见[此列表](https://jd.papermc.io/paper/org/bukkit/SoundCategory.html#enum-constant-summary)。

### `stop_sound`

停止原版声音或自定义声音。

```yaml
stop_sound:
  name: entity.villager.ambient # or a custom sound
```

* `name`：原版值见[此列表](https://minecraft.wiki/w/Sounds.json/Java_Edition_values)；自定义声音使用 `namespace:value`。

### `execute_commands`

执行配置的命令。

```yaml
execute_commands:
  tellraw_action: # Use any name you want
    command: 'tellraw {player} {"text":"Action 1","color":"gold"}'
    as_console: true # Optional (Default value: false)
  # Execute another command
  give_gold:
    command: 'give {player} gold_ingot 16'
    as_console: true
```

### `play_particle`

播放指定粒子。

```yaml
play_particle:
  name: heart
```

* `name`：可用值见[此列表](https://minecraft.wiki/w/Particles_(Java_Edition)#Types_of_particles)。

### `shoot_particle`

发射指定粒子。

```yaml
shoot_particle:
  name: spit
  distance: 5 # Optional (Default value: 7)
```

* `name`：可用值见[此列表](https://minecraft.wiki/w/Particles_(Java_Edition)#Types_of_particles)。

### `play_effect`

播放指定效果。

```yaml
play_effect:
  name: SPAWN_COBWEB
```

* `name`：可用值见[此列表](https://jd.papermc.io/paper/1.21.11/org/bukkit/Effect.html#enum-constant-summary)。

### `increment_durability`

减少／增加该物品的耐久度。

```yaml
increment_durability:
  amount: 5
```

### `decrement_durability`

减少／增加该物品的耐久度。

```yaml
decrement_durability:
  amount: 5
```

### `decrement_usages`

减少该物品的使用次数。

```yaml
decrement_usages:
  amount: 1
```

### `increment_amount`

增加该物品的数量。

```yaml
increment_amount:
  amount: 3
```

### `decrement_amount`

减少该物品的数量。

```yaml
decrement_amount:
  amount: 1
```

### `drop_exp`

掉落经验。

```yaml
drop_exp:
  chance: 1.0 # Optional (Default value: 0.0) - Chance 1.0 = 100%
  min_amount: 4
  max_amount: 8
```

### `feed`

恢复玩家饥饿值。

```yaml
feed:
  amount: 6
  saturation: 8 # Optional (Default value: 0)
```

* `amount`：含义见[此说明](https://minecraft.wiki/w/Food#Hunger)。
* `saturation`：含义见[此说明](https://minecraft.wiki/w/Food#Hunger)。

### `give_item`

给予此玩家一个物品。

```yaml
give_item:
  item: 'minecraft:gold_ingot'
  amount: 6 # Optional (Default value: 1)
```

* `item`：原版值见[此列表](https://jd.papermc.io/paper/org/bukkit/inventory/ItemType.html#field-summary)；自定义物品使用 `namespace:value`。

### `replace_near_blocks`

替换交互位置附近的原版／自定义方块；若事件不是交互事件，则以玩家附近为范围。

#### 属性：

* `from` （类型未知）：原文未说明。
* `from_multiple`（数组）：要替换的原版／自定义方块列表。
* `to` （类型未知）：原文未说明。
* `radius`（对象）：原文未说明。
* `decrement_durability`（整数）：减少的耐久度。
* `decrement_amount`（整数）：减少的物品数量。
* `no_physics`（布尔值）：原文未说明。
* `delay`（整数）：动作执行前等待的 tick 数。
* `flow`（对象）：调整当前事件配置段中动作执行流程的高级选项。
* `permission`（字符串）：执行动作所需权限；前置 `!` 可取反。例如，`!example.permission` 表示拥有 `example.permission` 的玩家不会执行该动作。

### `glow_near_blocks`

使交互位置附近的方块发光；若事件不是交互事件，则以玩家附近为范围。

#### 属性：

* `material`（字符串）：原版方块材质。
* `radius`（对象）：原文未说明。
* `delay`（整数）：动作执行前等待的 tick 数。
* `flow`（对象）：调整当前事件配置段中动作执行流程的高级选项。
* `permission`（字符串）：执行动作所需权限；前置 `!` 可取反。例如，`!example.permission` 表示拥有 `example.permission` 的玩家不会执行该动作。

### `replace_block`

替换交互位置的原版／自定义方块；若事件不是交互事件，则使用玩家所在位置。

#### 属性：

* `from` （类型未知）：原文未说明。
* `to` （类型未知）：原文未说明。
* `decrement_durability`（整数）：减少的耐久度。
* `decrement_amount`（整数）：减少的物品数量。
* `no_physics`（布尔值）：原文未说明。
* `delay`（整数）：动作执行前等待的 tick 数。
* `flow`（对象）：调整当前事件配置段中动作执行流程的高级选项。
* `permission`（字符串）：执行动作所需权限；前置 `!` 可取反。例如，`!example.permission` 表示拥有 `example.permission` 的玩家不会执行该动作。

### `multiple_break`

以破坏的方块为中心，破坏周围多个方块。

```yaml
multiple_break:
  size: 3
  depth: 3 # Optional (Default value: 1)
  vertical: true # Optional (Default value: false)
  keep_ores: true # Whether to break ores
  drop_all_blocks: # Optional
    enabled: true
    need_silk_touch: true
```

### `potion_effect`

给玩家施加药水效果。

```yaml
potion_effect:
  type: REGENERATION
  amplifier: 0 # Optional (Default value: 1) - Amplifier 0 = Level 1
  duration: 200 # Optional (Default value: 40) - Value in ticks (20 ticks = 1 second)
  ambient: true # Optional (Default value: false) - Whether to make the particles more translucent
  particles: false # Optional (Default value: true) - Whether to show the particles
  icon: false # Optional (Default value: true) - Whether to show the icon on screen
# Add another effect
potion_effect_1:
  type: FIRE_RESISTANCE
  amplifier: 0
  duration: 1200
  particles: false
```

* `type`：可用值见[此列表](https://jd.papermc.io/paper/org/bukkit/potion/PotionEffectType.html#field-summary)。

### `remove_potion_effect`

移除药水效果。

```yaml
remove_potion_effect:
  type: RESISTANCE
```

* `type`：可用值见[此列表](https://jd.papermc.io/paper/org/bukkit/potion/PotionEffectType.html#field-summary)。

### `explosion`

产生爆炸。

```yaml
explosion:
  power: 1
  fire: true # Optional (Default value: false) - Whether the TNT spreads fire when exploding
  break_blocks: false # Optional (Default value: true)
```

### `damage_near_entities`

对附近实体造成伤害。

#### 属性：

* `damage`（数值）：原文未说明。
* `radius`（整数）：原文未说明。
* `entity_groups`（数组）：原文未说明。
* `delay`（整数）：动作执行前等待的 tick 数。
* `flow`（对象）：调整当前事件配置段中动作执行流程的高级选项。
* `permission`（字符串）：执行动作所需权限；前置 `!` 可取反。例如，`!example.permission` 表示拥有 `example.permission` 的玩家不会执行该动作。

### `damage_entity_in_sight`

对视线指向的实体造成伤害。

```yaml
damage_entity_in_sight:
  damage: 5.0
  distance: 4 # Optional (Default value: 3)
```

### `damage_entity`

对当前事件关联的实体造成伤害，例如交互、攻击或 item\_hit\_entity 事件的目标。

```yaml
damage_entity:
  damage: 5.0
```

### `target_potion_effect`

给目标实体施加药水效果。

```yaml
target_potion_effect:
  type: REGENERATION
  amplifier: 0 # Optional (Default value: 1) - Amplifier 0 = Level 1
  duration: 200 # Optional (Default value: 40) - Value in ticks (20 ticks = 1 second)
  ambient: true # Optional (Default value: false) - Whether to make the particles more translucent
  particles: false # Optional (Default value: true) - Whether to show the particles
  icon: false # Optional (Default value: true) - Whether to show the icon on screen
# Add another effect
target_potion_effect_1:
  type: FIRE_RESISTANCE
  amplifier: 0
  duration: 1200
  particles: false
```

* `type`：可用值见[此列表](https://jd.papermc.io/paper/org/bukkit/potion/PotionEffectType.html#field-summary)。

### `target_remove_potion_effect`

移除目标实体的药水效果。

```yaml
target_remove_potion_effect:
  type: RESISTANCE
```

* `type`：可用值见[此列表](https://jd.papermc.io/paper/org/bukkit/potion/PotionEffectType.html#field-summary)。

### `increment_player_stat`

增加玩家属性值（ItemsAdder 属性，用于 HUD）。

```yaml
increment_player_stat:
  name: 'my_hud:power'
  amount: 10.0
```

* `name`：使用 `namespace:value` 指定自定义属性。

### `decrement_player_stat`

减少玩家属性值（ItemsAdder 属性，用于 HUD）。

```yaml
decrement_player_stat:
  name: 'my_hud:power'
  amount: 5.0
```

* `name`：使用 `namespace:value` 指定自定义属性。

### `play_totem_animation`

使用指定物品纹理播放图腾动画。

### `script`

在指定事件中执行自定义脚本。

```yaml
script:
  name: 'some_script'
```

* `name`：使用 `value` 指定自定义脚本。

### `drop_item`

掉落原版／自定义物品。

```yaml
drop_item:
  item: 'minecraft:apple'
  chance: 50.0 # Optional (Default value: 100.0) - Chance 100.0 = 100%
  min_amount: 2 # Optional (Default value: 1)
  max_amount: 5 # Optional (Default value: 1)
```

* `item`：原版值见[此列表](https://jd.papermc.io/paper/org/bukkit/inventory/ItemType.html#field-summary)；自定义物品使用 `namespace:value`。

### `set_block`

放置方块，适合在交互事件中放置自定义或原版方块。

#### 属性：

* `block` （类型未知）：原文未说明。
* `target`（字符串）：原文未说明。
* `decrement_amount`（布尔值）：原文未说明。
* `delay`（整数）：动作执行前等待的 tick 数。
* `flow`（对象）：调整当前事件配置段中动作执行流程的高级选项。
* `permission`（字符串）：执行动作所需权限；前置 `!` 可取反。例如，`!example.permission` 表示拥有 `example.permission` 的玩家不会执行该动作。

### `place_furniture`

放置家具，适合在交互事件中放置自定义家具。

```yaml
place_furniture:
  furniture: 'my_furniture:chair'
  decrement_amount: true # Optional (Default value: false)
```

* `furniture`：使用 `namespace:value` 指定自定义家具。

### `remove_furniture`

需要 ItemsAdder 4.0.16+。

移除家具，适合在交互事件中移除自定义家具。

### `replace_furniture`

需要 ItemsAdder 4.0.16+。

替换家具，适合在交互事件中把家具换成另一种家具。

```yaml
replace_furniture:
  furniture: 'my_furniture:table'
```

* `furniture`：使用 `namespace:value` 指定自定义家具。

### `replace_properties`

替换此物品的属性。

#### 属性：

* `custom_model_data`（对象）：原文未说明。

## ItemsAdderAdditions 动作

### `actionbar`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/actionbar).

### `clear_item`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/clear-item).

### `ignite`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/ignite).

### `message`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/message).

### `mythic_mobs_skill`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/mythic-mobs-skill).

### `open_inventory`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/open-inventory).

### `open_trade_machine`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/open-trade-machine).

### `play_animation`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/play-animation).

### `play_emote`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/play-emote).

### `replace_biome`
文档见[此处](https://itemsadderadditions.com/docs/actions/replace-biome).

### `replace_item`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/replace-item).

### `shoot_fireball`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/shoot-fireball).

### `swing_hand`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/swing-hand).

### `teleport`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/teleport).

### `title`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/title).

### `toast`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/toast).

### `replace_biome`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/replace-biome).

### `veinminer`
文档见[此处](https://itemsadderadditions.com/en/docs/actions/veinminer).