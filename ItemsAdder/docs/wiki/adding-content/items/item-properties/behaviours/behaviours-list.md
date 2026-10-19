---
title: "行为列表"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/behaviours/behaviours-list"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 行为列表

## 行为

### `block_trade_machine`

告诉 ItemsAdder 此物品是交易机。\
玩家可像与村民交易一样，用该机器交换物品。

#### 属性：

* `enabled` （布尔值）
* `title` （字符串）
* `gui_texture`（对象）：用自定义纹理替换交易界面外观；替换后不再显示标题。
* `trades_list`（对象）：该机器接受的交易列表。
  * `change_me`（对象）：交易配方。
    * `ingredients`（对象）：此配方所需原料。
      * `slot1` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
      * `slot2` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
    * `result`（对象）：此配方的产物。
      * `item`（字符串）：原版或 ItemsAdder 自定义物品。
      * `amount` （整数）
  * `change_me_2`（对象）：交易配方。
    * `ingredients`（对象）：此配方所需原料。
      * `slot1` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
      * `slot2` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
    * `result`（对象）：此配方的产物。
      * `item`（字符串）：原版或 ItemsAdder 自定义物品。
      * `amount` （整数）
  * `change_me_xxx`（对象）：交易配方。
    * `ingredients`（对象）：此配方所需原料。
      * `slot1` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
      * `slot2` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
    * `result`（对象）：此配方的产物。
      * `item`（字符串）：原版或 ItemsAdder 自定义物品。
      * `amount` （整数）

### `complex_furniture`

使用自定义实体创建复杂家具，支持动画和更多旋转角度，不限于 22.5 度步进。

#### 属性：

* `enabled` （布尔值）
* `entity`（字符串）：自定义实体 ID。
* `static`（布尔值）：默认 `false`；静态模型不会播放动画。
* `light_level`（整数）：设置家具发出的光照等级。
* `solid`（布尔值）：默认 `false`；实体家具使用 BARRIER 方块模拟碰撞。
* `permission_suffix`（字符串）：控制玩家放置／破坏复杂家具的权限后缀。例如，`example.ceiling_fan` 对应 `ia.user.complex_furniture.break.example.ceiling_fan` 的后缀。
* `sound` （类型未知）
* `drop_when_mined`（布尔值）：默认 `true`；可用此选项禁止玩家破坏家具时掉落物品。
* `max_per_chunk`（整数）：每区块可放置的复杂家具上限，覆盖 `config.yml` 的 `max_per_chunk`。
* `placement_offset`（对象）：复杂家具放置位置的偏移。
  * `ceiling`（数值）：天花板上的放置偏移，可正可负。
  * `floor`（数值）：地板上的放置偏移，可正可负。
  * `wall`（数值）：墙面上的放置偏移，可正可负。

### `entity_summoner`

交互时生成指定的原版或自定义实体，类似原版刷怪蛋。

#### 属性：

* `enabled` （布尔值）
* `entity` （类型未知）
* `max_per_chunk`（整数）：每区块可生成的实体上限。
* `decrement_durability`（布尔值）：生成实体时是否减少物品耐久度。
* `decrement_amount`（整数）：默认 `1`；原文将其描述为生成实体时减少的耐久数量。

### `fuel`

告诉 ItemsAdder 此物品是自定义燃料。
\
此物品可放入熔炉。请务必使用 Minecraft 原本已支持的燃料材质，例如 COAL、COAL\_BLOCK、LAVA\_BUCKET。

#### 属性：

* `enabled` （布尔值）
* `burn_ticks`（整数）：燃烧时长，单位 tick（20 tick = 1 秒）。原版煤炭燃烧 1600 tick。
* `machines`（数组）：接受该燃料的机器列表。
* `machines`（数组）：接受该燃料的机器列表；可选值为 `FURNACE`、`BLAST_FURNACE`、`SMOKER`。

### `furniture`

告诉 ItemsAdder 此物品是家具。
\
右键可放置，攻击已放置的实体可移除。

家具限制：

* 非实体家具不接收交互事件，只能用鼠标左键移除；只有实体家具支持交互事件。
* 出于性能考虑，碰撞箱尺寸最大为 3x3x3。

#### 属性：

* `enabled` （布尔值）
* `entity`（字符串）：创建家具时使用的实体类型。
* `gravity`（布尔值）：家具是否受重力影响。
* `small`（布尔值）：家具使用小尺寸还是大尺寸。请据此在 Blockbench 中调整 3D 模型大小。
* `fixed_rotation`（布尔值）：是否固定旋转角度，用于精确放置，例如壁画。
* `light_level`（整数）：设置家具发出的光照等级。
* `shift_interact_rotate`（布尔值）：默认为 `true`。设为 `true` 时，可以通过潜行交互（右键）旋转自定义 `item_frame` 家具。
* `solid`（布尔值）：家具是否具有实体碰撞。ItemsAdder 使用 BARRIER 方块构建碰撞箱，可通过 hitbox 属性调整尺寸。
* `hitbox`（对象）：玩家点击以移除家具的范围；`solid` 为 `true` 时也可产生实体碰撞。
  * `length` （数值）
  * `width` （数值）
  * `height` （数值）
  * `length_offset` （数值）
  * `width_offset` （数值）
  * `height_offset` （数值）
* `opposite_direction`（布尔值）：放置时自动将模型旋转 180 度。
* `permission_suffix` （类型未知）
* `sound` （类型未知）
* `placeable_on`（对象）：设置家具允许放置的位置。
  * `walls` （布尔值）
  * `ceiling` （布尔值）
  * `floor` （布尔值）
* `drop_when_mined`（布尔值）：可用于禁止玩家破坏家具时掉落物品。
* `display_transformation`（对象）：`item_display` 的变换属性，可自由缩放、平移或旋转模型。
  * `adjust_legacy_model`（字符串）：让原先面向 `item_frame` 或 `armor_stand` 制作的模型适配 `item_display`，无需逐个手动调整。
  * `transform` （字符串）
  * `right_rotation`（对象）：旋转模型，使用 `axis_angle` 或 `quaternion` 其中之一。
  * `left_rotation`（对象）：旋转模型，使用 `axis_angle` 或 `quaternion` 其中之一。
  * `translation` （对象）
    * `x` （数值）
    * `y` （数值）
    * `z` （数值）
  * `scale` （对象）
    * `x` （数值）
    * `y` （数值）
    * `z` （数值）

### `furniture_sit`

告诉 ItemsAdder 此物品是椅子。
\
右键家具碰撞箱即可坐下。

#### 属性：

* `enabled` （布尔值）
* `sit_height`（数值）：乘坐位置的高度。
* `opposite_direction`（布尔值）：默认 true；启用时，玩家坐下后旋转 180 度。
* `sit_all_solid_blocks`（布尔值）：默认 true；允许玩家坐在家具的每个 BARRIER 方块上，适合多座位椅子。仅适用于实体家具。
* `passenger_front_view_on_sit`（布尔值）：默认 true；坐下时让玩家面向家具正面。
* `passenger_rotate_body`（布尔值）：默认 false；乘坐时旋转玩家身体。

### `furniture_trade_machine`

告诉 ItemsAdder 此物品是交易机。
\
玩家可像与村民交易一样，用该机器交换物品。

#### 属性：

* `enabled` （布尔值）
* `title` （字符串）
* `gui_texture`（对象）：用自定义纹理替换交易界面外观；替换后不再显示标题。
* `trades_list`（对象）：该机器接受的交易列表。
  * `change_me`（对象）：交易配方。
    * `ingredients`（对象）：此配方所需原料。
      * `slot1` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
      * `slot2` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
    * `result`（对象）：此配方的产物。
      * `item`（字符串）：原版或 ItemsAdder 自定义物品。
      * `amount` （整数）
  * `change_me_2`（对象）：交易配方。
    * `ingredients`（对象）：此配方所需原料。
      * `slot1` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
      * `slot2` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
    * `result`（对象）：此配方的产物。
      * `item`（字符串）：原版或 ItemsAdder 自定义物品。
      * `amount` （整数）
  * `change_me_xxx`（对象）：交易配方。
    * `ingredients`（对象）：此配方所需原料。
      * `slot1` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
      * `slot2` （对象）
        * `item`（字符串）：原版或 ItemsAdder 自定义物品。
        * `amount` （整数）
    * `result`（对象）：此配方的产物。
      * `item`（字符串）：原版或 ItemsAdder 自定义物品。
      * `amount` （整数）

### `gun`

告诉 ItemsAdder 此物品是枪械。
\
玩家可以射击并装填弹药。

#### 属性：

* `enabled` （布尔值）
* `projectile`（字符串）：原版或 ItemsAdder 自定义物品。

### `liquid_bucket`

告诉 ItemsAdder 此物品是液体桶。
\
可以放置自定义液体，再用桶收回。

#### 属性：

* `enabled` （布尔值）
* `name`（字符串）：液体标识符。

### `music_disc`

（**已弃用**）告诉 ItemsAdder 此物品是音乐唱片。
\
可以放入唱片机播放歌曲。
**注意：**这是旧方法，请改用新的 `jukebox_disc` 属性。

#### 属性：

* `enabled` （布尔值）
* `song`（对象）：歌曲属性。
  * `name`（字符串）：填写 songs.json 中定义的歌曲名称。原文教程链接：https://itemsadder.devs.beer/adding-content/sounds
  * `description`（字符串）：歌曲描述，唱片放入唱片机时显示在快捷栏消息中。

### `vehicle`

告诉 ItemsAdder 此物品是载具。
\
玩家可乘坐并在地面或空中移动，也可以配置燃料。

#### 属性：

* `enabled` （布尔值）
* `sit_height`（数值）：乘坐位置的高度。
* `fixed_rotation`（布尔值）：是否固定载具旋转角度，以便精确放置。
* `small`（布尔值）：载具是大还是小；3D 模型应与此设置对应，使用 Blockbench 相应调整模型大小。
* `step_height`（数值）：自动越过台阶的高度。
* `speed`（对象）：载具在不同动作下的速度。
  * `drive`（数值）：普通行驶速度。
  * `jump`（数值）：跳跃速度。
  * `fly`（数值）：飞行速度。
* `sound` （类型未知）
* `fuel`（对象）：燃料设置。
  * `start`（数值）：合成／获取载具时的初始燃料。
  * `max`（数值）：载具燃料上限。
  * `items`（类型未知）：载具接受的原版／自定义燃料物品。可以设置任意原版材质或自定义物品；编辑器只会补全部分示例。
* `hitbox`（对象）：载具尺寸，用于驾驶时与墙面／方块碰撞。
  * `length` （数值）
  * `width` （数值）
  * `height` （数值）
* `smoke`（对象）：尾气烟雾效果。
  * `amount` （数值）
  * `x` （数值）
  * `y` （数值）
  * `z` （数值）

## ItemsAdderAdditions 行为

### `bed`
文档见[此处](https://itemsadderadditions.com/en/docs/behaviours/bed).

### `connectable`
文档见[此处](https://itemsadderadditions.com/en/docs/behaviours/connectable).

### `contact_effect`
文档见[此处](https://itemsadderadditions.com/en/docs/behaviours/contact-effect).

### `stackable`
文档见[此处](https://itemsadderadditions.com/en/docs/behaviours/stackable).

### `storage`
文档见[此处](https://itemsadderadditions.com/en/docs/behaviours/storage).

### `text_display`
文档见[此处](https://itemsadderadditions.com/en/docs/behaviours/text-display).