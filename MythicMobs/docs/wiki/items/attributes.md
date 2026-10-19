---
title: 物品属性
source_url: https://wiki.mythiccraft.io/mythicmobs/Items/Attributes
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 物品属性

# 属性 {#attributes}

MythicMobs 物品的 attributes 部分用于处理 Minecraft 属性系统。它可以根据物品所在槽位，为穿戴或使用物品的实体应用不同属性。

1. [格式](attributes.md#format)
2. [槽位](attributes.md#slots)
3. [数值](attributes.md#value)
4. [运算方式](attributes.md#operations)
5. [属性](attributes.md#attributes)
   1. [ATTACK_DAMAGE](attributes.md#attack-damage)
   2. [ATTACK_SPEED](attributes.md#attack-speed)
   3. [MAX_HEALTH](attributes.md#max-health)
   4. [MOVEMENT_SPEED](attributes.md#movement-speed)
   5. [FLYING_SPEED](attributes.md#flying-speed)
   6. [ATTACK_KNOCKBACK](attributes.md#attack-knockback)
   7. [KNOCKBACK_RESISTANCE](attributes.md#knockback-resistance)
   8. [ARMOR](attributes.md#armor)
   9. [ARMOR_TOUGHNESS](attributes.md#armor-toughness)
   10. [LUCK](attributes.md#luck)
   11. [SCALE](attributes.md#scale)
   12. [FOLLOW_RANGE](attributes.md#follow-range)
   13. [FALL_DAMAGE_MULTIPLIER](attributes.md#fall-damage-multiplier)
   14. [SAFE_FALL_DISTANCE](attributes.md#safe-fall-distance)
   15. [GRAVITY](attributes.md#gravity)
   16. [BLOCK_BREAK_SPEED](attributes.md#block-break-speed)
   17. [ENTITY_INTERACTION_RANGE](attributes.md#entity-interaction-range)
   18. [BLOCK_INTERACTION_RANGE](attributes.md#block-interaction-range)
   19. [JUMP_HEIGHT](attributes.md#jump-height)
   20. [STEP_HEIGHT](attributes.md#step-height)
   21. [MAX_ABSORPTION](attributes.md#max-absorption)
   22. [BURNING_TIME](attributes.md#burning-time)
   23. [EXPLOSION_KNOCKBACK_RESISTANCE](attributes.md#explosion-knockback-resistance)
   24. [MOVEMENT_EFFICIENCY](attributes.md#movement-efficiency)
   25. [OXYGEN](attributes.md#oxygen)
   26. [SNEAKING_SPEED](attributes.md#sneaking-speed)
   27. [WATER_MOVEMENT_EFFICIENCY](attributes.md#water-movement-efficiency)
   28. [SUBMERGED_MINING_SPEED](attributes.md#submerged-mining-speed)
   29. [MINING_EFFICIENCY](attributes.md#mining-efficiency)
   30. [TEMPT_RANGE](attributes.md#tempt-range)
   31. [SWEEPING_DAMAGE_RATIO](attributes.md#sweeping-damage-ratio)
   32. [SPAWN_REINFORCEMENTS](attributes.md#spawn-reinforcements)
6. [示例](attributes.md#examples)

## 格式 {#format}

```yml
Item:
  Id: item_id
  Attributes:
    [Slot]:
      [Attribute]: [value] <operation> 
```

## 槽位 {#slots}

| 槽位 | 说明 |
| --- | --- |
| All | 将给定属性应用于所有槽位。 |
| MainHand | 仅在物品持于主手时应用属性。 |
| OffHand | 仅在物品持于副手时应用属性。 |
| Head | 仅在物品装备于头部槽位时应用属性。 |
| Chest | 仅在物品装备于胸部/躯干槽位时应用属性。 |
| Legs | 仅在物品装备于腿部槽位时应用属性。 |
| Feet | 仅在物品装备于脚部槽位时应用属性。 |

## 值 {#value}

可以输入绝对值或相对值：

- 输入绝对值时，直接填写数值即可。

```yaml
      Damage: 10 ADD
```

- 输入相对值时，在数值后添加 % 符号。

```yaml
      Damage: 10% ADD
```

## 运算 {#operations}

| 运算 | 别名 | 说明 |
| --- | --- | --- |
| ADD | 0, ADD_NUMBER | 将指定数值加到基础值上，或从基础值中减去。 |
| MULTIPLY_BASE | 1, ADD_SCALAR | 将基础值乘以所有修饰符数值之和。 |
| MULTIPLY | 2, MULTIPLY_SCALAR | 类似于 `MULTIPLY_BASE`，但将所有修饰符数值相乘，而不是相加。 |

[*游戏如何计算所有修正值，参见 MC Wiki*](https://minecraft.wiki/w/Attribute#Modifiers)

## 属性 {#attributes}

以下列出了物品上可用的全部属性。可以使用 `<random.#to#>` 或 `<random.float.#to#>` 等通用占位符。本页大部分说明摘自 [Minecraft Wiki](https://minecraft.wiki)，更多信息见其[属性页面](https://minecraft.wiki/w/Attribute#Attributes)。

### ATTACK_DAMAGE {#attack-damage}

设置近战攻击造成的伤害。不考虑护甲时，1 点伤害相当于 0.5 颗心。

```yml
custom_item:
  Id: stick
  Attributes:
    All:
      ATTACK_DAMAGE: 0.2 ADD_SCALAR
```

### ATTACK_SPEED {#attack-speed}

决定攻击强度的恢复速度。数值表示每秒可以进行多少次满强度攻击。

```yml
custom_item:
  Id: stick
  Attributes:
    MainHand:
      ATTACK_SPEED: 0.1 MULTIPLY
```

### MAX_HEALTH {#max-health}

使用者手持或穿戴此物品时获得的最大生命值修正。1 点生命值相当于 0.5 颗心。

```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    MainHand:
      MAX_HEALTH: 2 ADD
```

### MOVEMENT_SPEED {#movement-speed}

移动速度表示实体移动的快慢，但这个数值并不是以格/秒表示的实际速度。实体每秒实际移动的格数略大于此值的 20 倍。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MOVEMENT_SPEED: -0.2 MULTIPLY_BASE
```

### FLYING_SPEED {#flying-speed}

此属性是飞行速度修正，具体计量方式未知。

```yaml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      FLYING_SPEED: 1 ADD
```

### ATTACK_KNOCKBACK {#attack-knockback}

决定攻击产生的击退。

```yaml
custom_item:
  Id: stick
  Attributes:
    MainHand:
      ATTACK_KNOCKBACK: 1 ADD
```

### KNOCKBACK_RESISTANCE {#knockback-resistance}

决定对攻击和投射物造成的水平击退的抵抗比例。不会影响垂直击退，也不会影响爆炸。抗性按百分比计算，范围从 0.0（0% 抗性）到 1.0（100% 抗性）。例如，0.4 表示 40% 抗性，即实体只会受到通常击退的 60%。

```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      KNOCKBACK_RESISTANCE: 2 MULTIPLY_BASE
```

### ARMOR {#armor}

此属性定义[护甲防御点数](https://minecraft.wiki/w/Armor#Armor_points)。1 点护甲相当于 0.5 个护甲图标。超过 20 点的护甲值不会显示，实际最大值为 30。

```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      ARMOR: 2
```

### ARMOR_TOUGHNESS {#armor-toughness}

改变护甲属性的减伤百分比。参见 [MC Wiki](https://minecraft.wiki/Armor#Armor_toughness)。

```yml
custom_item:
  Id: diamond_chestplate
  Attributes:
    Chest:
      ARMOR_TOUGHNESS: 0.5
```

### LUCK {#luck}

设置物品的幸运修正值。此修正会影响[战利品表的结果](https://minecraft.wiki/w/Attribute#Luck)以及[生物掉落](../drops/drops.md)。

```yml
custom_item:
  Id: stick
  Attributes:
    OffHand:
      LUCK: -10 ADD
```

### SCALE {#scale}

实体大小的倍率。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SCALE: 2 ADD
```

### FOLLOW_RANGE {#follow-range}

此属性决定生物搜索并追踪玩家或其他生物的范围，单位为格。目标离开此范围后，生物会停止跟随该玩家或生物。

```yaml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      FOLLOW_RANGE: 1 ADD
```

### FALL_DAMAGE_MULTIPLIER {#fall-damage-multiplier}

实体受到的摔落伤害倍率。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      FALL_DAMAGE_MULTIPLIER: 2 ADD
```

### SAFE_FALL_DISTANCE {#safe-fall-distance}

实体下落多少格后开始累计摔落伤害，也是实体产生落地粒子和声音所需的最小下落格数。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SAFE_FALL_DISTANCE: 2 ADD
```

### GRAVITY {#gravity}

作用于实体的重力，单位为格/刻²。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      GRAVITY: 2 ADD
```

### BLOCK_BREAK_SPEED {#block-break-speed}

玩家破坏方块的速度倍率。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BLOCK_BREAK_SPEED: 2 ADD
```

### ENTITY_INTERACTION_RANGE {#entity-interaction-range}

玩家与实体的交互距离，单位为格。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      ENTITY_INTERACTION_RANGE: 2 ADD
```

### BLOCK_INTERACTION_RANGE {#block-interaction-range}

玩家与方块的交互距离，单位为格。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BLOCK_INTERACTION_RANGE: 2 ADD
```

### JUMP_HEIGHT {#jump-height}

此属性决定实体跳跃时的初始垂直速度，单位为格/刻。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      JUMP_HEIGHT: 2 ADD
```

### STEP_HEIGHT {#step-height}

实体无需跳跃即可跨上的最大方块高度。潜行只会阻止从高于此属性值的高度跌落；只有玩家位于方块上方的高度小于或等于此属性值时，才会出现这种情况。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      STEP_HEIGHT: 2 ADD
```

### MAX_ABSORPTION {#max-absorption}

此实体的最大伤害吸收量，决定其通过伤害吸收效果能获得的最高额外生命值。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MAX_ABSORPTION: 1 ADD
```

### BURNING_TIME {#burning-time}

此属性是实体被点燃后持续燃烧时间的倍率。设为 0 会消除燃烧时间，但不会影响实体停留在火中时增加的燃烧时间。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      BURNING_TIME: 1 ADD
```

### EXPLOSION_KNOCKBACK_RESISTANCE {#explosion-knockback-resistance}

此属性定义实体抵抗爆炸击退的百分比。设为 1 会完全消除击退。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      EXPLOSION_KNOCKBACK_RESISTANCE: 1 ADD
```

### MOVEMENT_EFFICIENCY {#movement-efficiency}

此属性用于改善实体在减速地形上的行走速度。设为 1 会移除减速。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MOVEMENT_EFFICIENCY: 1 ADD
```

### OXYGEN {#oxygen}

此属性决定实体在水下时，每个游戏刻减少 Air 数据标签数值的概率。概率为 $`\frac{1}{(OXYGEN + 1)}`$。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      OXYGEN: 1 ADD
```

### SNEAKING_SPEED {#sneaking-speed}

此属性决定潜行或爬行时的移动速度倍率。倍率为 1 表示潜行或爬行速度与行走相同，倍率为 0 表示潜行或爬行时无法移动。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SNEAKING_SPEED: 1 ADD
```

### WATER_MOVEMENT_EFFICIENCY {#water-movement-efficiency}

此属性是浸没时的移动速度倍率。数值越高，实体移动越快。它只表示浸没本身的影响，其他因素（如疾跑）仍会生效。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      WATER_MOVEMENT_EFFICIENCY: 1 ADD
```

### SUBMERGED_MINING_SPEED {#submerged-mining-speed}

此属性决定水下挖掘速度的倍率。倍率为 1 表示挖掘速度与陆地相同，倍率为 0 表示浸没时无法挖掘。它只表示浸没本身的影响，其他因素（如未接触地面）仍会生效。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SUBMERGED_MINING_SPEED: 1 ADD
```

### MINING_EFFICIENCY {#mining-efficiency}

此属性用于加快使用正确工具时的方块挖掘速度。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      MINING_EFFICIENCY: 1 ADD
```

### TEMPT_RANGE {#tempt-range}

此属性决定生物被引诱的范围，单位为格。被引诱时，生物会跟随手持特定物品的玩家。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      TEMPT_RANGE: 1 ADD
```

### SWEEPING_DAMAGE_RATIO {#sweeping-damage-ratio}

此属性决定横扫攻击将基础攻击伤害的多少比例传递给次要目标。这部分伤害会加在横扫本身的基础伤害之上。设为 1 表示传递全部基础攻击伤害（横扫伤害为 attack_damage + 1）。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SWEEPING_DAMAGE_RATIO: 0.5 ADD
```

### SPAWN_REINFORCEMENTS {#spawn-reinforcements}

此属性决定僵尸受攻击时生成另一只僵尸的概率。

```yml
custom_item:
  Id: wooden_sword
  Attributes:
    All:
      SPAWN_REINFORCEMENTS: 0 MULTIPLY
```

## 示例 {#examples}

这个物品示例在主手持有时提供 +10 幸运值，但在副手持有时会提供 +7 幸运值和 +2 额外伤害：

```yml
lucky_charms:
  Id: potato_item
  Display: 'Rotten Lucky Charm'
  Attributes:
    MainHand:
      Luck: 10
    OffHand:
      Luck: 7
      Damage: 2
```

这个物品示例无论放在哪个槽位，都提供 +2 额外生命值；如果穿在脚部槽位，还会提供 +4% 移动速度：

```yml
happy_feet:
  Id: leather_boots
  Display: 'Penguin Hide'
  Attributes:
    All:
      Health: 2
    Feet:
      MovementSpeed: 0.04
```

每次生成这个物品时，都会随机产生 3 到 5 的伤害值，以及在主手持有时生效的 1% 到 5% 随机速度加成：

```yml
lucky_sword:
  Id: wood_sword
  Display: '<yellow>Lucky Sword</yellow>'
  Attributes:
    MainHand:
      Damage: 3-5
      MovementSpeed: 0.01-0.05 MULTIPLY_BASE
```
