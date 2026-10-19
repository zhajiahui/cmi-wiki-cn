---
title: "实体行为目标列表"
source_url: "https://wiki.itemsadder.com/adding-content/entities/entity-goals/entity-goals-list"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 实体行为目标列表

## 实体行为目标

### `attack_near`

让实体寻找最近的可攻击目标

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `entity`（字符串）：自定义实体类型或 Bukkit 实体类型
* `selector` （类型未知）
  * `min_health`（数值，默认 `0.0`）：应用此目标所需的实体最低生命值。实体生命值低于此值时，不应用该目标。
  * `max_health`（数值，默认 `20.0`）：应用此目标所允许的实体最高生命值。实体生命值高于此值时，不应用该目标。
  * `equipment`（对象）：应用此目标所需的实体装备。装备不匹配时，不应用该目标。
    * `match_all`（布尔值，默认 `false`）：为 true 时，实体装备必须匹配指定的全部物品；为 false 时，至少匹配其中一件物品即可。
    * `head`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `chest`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `legs`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `feet`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `main_hand`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `off_hand`（字符串）：原版物品或 ItemsAdder 自定义物品
* `must_be_angry_at`（布尔值，默认 `true`）：为 true 时，仅以实体当前愤怒指向的实体为目标，适合狼等会对特定目标愤怒的实体。
* `interval`（整数，默认 `10`）：两次搜索目标之间的间隔，单位为刻。
* `check_visibility`（布尔值，默认 `true`）：为 true 时，仅选择自身可见的实体作为目标。
* `check_can_navigate`（布尔值，默认 `true`）：为 true 时，仅选择自身能够寻路到达的实体作为目标。

### `avoid_entity`

让实体躲避其他实体

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `entity`（字符串）：自定义实体类型或 Bukkit 实体类型
* `selector` （类型未知）
  * `min_health`（数值，默认 `0.0`）：应用此目标所需的实体最低生命值。实体生命值低于此值时，不应用该目标。
  * `max_health`（数值，默认 `20.0`）：应用此目标所允许的实体最高生命值。实体生命值高于此值时，不应用该目标。
  * `equipment`（对象）：应用此目标所需的实体装备。装备不匹配时，不应用该目标。
    * `match_all`（布尔值，默认 `false`）：为 true 时，实体装备必须匹配指定的全部物品；为 false 时，至少匹配其中一件物品即可。
    * `head`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `chest`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `legs`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `feet`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `main_hand`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `off_hand`（字符串）：原版物品或 ItemsAdder 自定义物品

### `avoid_sun`

让实体躲避阳光

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。

### `break_door`

让实体破坏门

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。

### `eat_block`

让实体吃掉方块

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `blocks`（数组）：实体会吃掉的方块列表。例如 `STONE`、`minecraft:cherry_trapdoor[open=true]`、`test:my_block`。
* `blocks`（数组）：实体会吃掉的方块列表。例如 `STONE`、`minecraft:cherry_trapdoor[open=true]`、`test:my_block`。

### `float`

让实体浮在水面上

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。

### `hurt_by_target`

让实体记住最后一次伤害它的实体

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `ignore_damage_from_entities`（数组）：不会触发复仇的原版实体类型列表。
* `ignore_damage_from_entities`（数组）：不会触发复仇的原版实体类型列表。
* `alert_others_types`（数组）：此实体受伤时会收到警报的实体类型列表。
* `alert_others_types`（数组）：此实体受伤时会收到警报的实体类型列表。

### `look_at_entity`

让实体看向其他实体

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `entity`（字符串）：自定义实体类型或 Bukkit 实体类型
* `selector` （类型未知）
  * `min_health`（数值，默认 `0.0`）：应用此目标所需的实体最低生命值。实体生命值低于此值时，不应用该目标。
  * `max_health`（数值，默认 `20.0`）：应用此目标所允许的实体最高生命值。实体生命值高于此值时，不应用该目标。
  * `equipment`（对象）：应用此目标所需的实体装备。装备不匹配时，不应用该目标。
    * `match_all`（布尔值，默认 `false`）：为 true 时，实体装备必须匹配指定的全部物品；为 false 时，至少匹配其中一件物品即可。
    * `head`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `chest`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `legs`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `feet`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `main_hand`（字符串）：原版物品或 ItemsAdder 自定义物品
    * `off_hand`（字符串）：原版物品或 ItemsAdder 自定义物品
* `chance`（数值，默认 `20`）：执行此行为目标的概率，单位为百分比。
* `range`（整数，默认 `8`）：实体会看向目标的最远距离，单位为格。
* `look_forward`（布尔值，默认 `false`）：为 true 时，看向目标实体面朝的方向，而非目标的位置。

### `melee_attack`

让实体进行近战攻击

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `speed_modifier`（数值，默认 `1.0`）：实体攻击时的速度修正值。
* `pause_when_idle`（布尔值，默认 `true`）：为 true 时，实体不移动时会暂停攻击。

### `move_to_block`

让实体移动到指定方块

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `blocks`（数组）：实体会前往的方块列表。例如 `STONE`、`minecraft:cherry_trapdoor[open=true]`、`test:my_block`。
* `blocks`（数组）：实体会前往的方块列表。例如 `STONE`、`minecraft:cherry_trapdoor[open=true]`、`test:my_block`。
* `speed_modifier`（数值，默认 `1.0`）：实体前往方块时的速度修正值。
* `search_range`（整数，默认 `16`）：实体搜索可前往方块的最远距离，单位为格。

### `open_door`

让实体开门

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `close`（布尔值，默认 `false`）：为 true 时，实体开门后会关门。

### `random_look_around`

让实体随机环顾四周

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。

### `random_wander_around`

让实体随机环顾四周

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `speed_modifier`（数值，默认 `1.0`）：实体闲逛时的速度修正值。
* `interval`（整数，默认 `10`）：两次随机闲逛之间的间隔，单位为刻。
* `check_no_action_time`（布尔值，默认 `true`）：为 true 时，仅当实体过去 10 秒未执行任何动作时才会闲逛（原版硬编码值，无法自定义）。

### `ranged_bow_attack`

让实体用弓攻击。注意：此行为目标仅适用于以下原版基础实体类型：`BOGGED`、`DROWNED`、`ILLUSIONER`、`LLAMA`、`PIGLIN`、`PILLAGER`、`SKELETON`、`SNOW_GOLEM`、`STRAY`、`TRADER_LLAMA`、`WITCH`、`WITHER`、`WITHER_SKELETON`。

#### 属性：

* `enabled` （布尔值）
* `replace_vanilla`（布尔值）：用此行为目标替换原版同类目标（如果存在）。为 false 时，将其添加到已有目标中。
* `priority`（整数）：此行为目标的优先级。优先级越高，越先于低优先级目标执行。
* `speed_modifier`（数值，默认 `1.0`）：实体攻击时的速度修正值。
* `attack_interval_min`（整数，默认 `20`）：两次远程攻击之间的最小间隔，单位为刻。
* `attack_radius`（整数，默认 `16`）：实体会攻击目标的最远距离，单位为格。
