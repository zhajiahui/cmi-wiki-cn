---
title: 经验来源
source: https://docs.phoenixdevt.fr/mmocore/level/sources
source_snapshot: '2026-10-19'
---

# 经验来源 {#🪴-experience-sources}

当某些事件发生时，经验源为你提供针对某些副职业的经验。每个经验源都有其自己的特定参数，你可以在配置中使用`exp_source_name{param1=P1;param2=p2..}`指定这些参数。你必须指定与边界相对应的参数`amount=min-max`，每次都会在该边界之间随机选择经验的数量。

你还可以将经验源用于主职业。

## 示例 {#examples}

以下是*伐木（Woodcutting）*副职业的默认经验来源。玩家每砍掉一个原木，就会获得 1 到 3 点经验。

```yml
exp-sources:
- 'mineblock{type=OAK_LOG;amount=1-3}'
- 'mineblock{type=SPRUCE_LOG;amount=1-3}'
- 'mineblock{type=BIRCH_LOG;amount=1-3}'
- 'mineblock{type=JUNGLE_LOG;amount=1-3}'
- 'mineblock{type=ACACIA_LOG;amount=1-3}'
- 'mineblock{type=BIRCH_LOG;amount=1-3}'
- 'mineblock{type=DARK_OAK_LOG;amount=1-3}'
```

这些是农业副职业的默认经验来源，每当玩家收获任何类型的农作物时，都会授予一些经验积分。

```yml
exp-sources:
- 'mineblock{type=CARROTS;amount=1-3;crop=true;player-placed=true}'
- 'mineblock{type=POTATOES;amount=1-3;crop=true;player-placed=true}'
- 'mineblock{type=WHEAT;amount=1-3;crop=true;player-placed=true}'
```

`crop=true`表示只有在完全成长阶段才会给予经验值。`player-placed=true`意味着即使玩家放置了方块，它也会授予 EXP

## 经验来源表 {#experience-sources-tables}

你可以在`exp-sources.yml`中创建experiences-sources表。该文件允许你创建可以在插件中的其他任何位置使用的 exp 源列表。这是一个例子：

```yml
exp-sources-1: 
  - 'damagedealt{type=physical;amount=250}'
  - 'move{type=WALK;amount=300}'
  # anything from 'exp-sources-2'
  - 'from{source=exp-sources-2}'

exp-sources-2:
  - 'eat{type=CARROT;amount="50"}'
```

## 每一个经验来源 {#every-experience-source}

### 从 {#from}

加载`exp-sources.yml`中与`exp-source-id`匹配的所有经验源。

```yml
from{source=exp-source-id}
```

### 矿区 {#mine-block}

从挖掘特定块中获取经验。更多信息请参见[挖矿](../features/mining.md)wiki 页面。

```yml
mineblock{type=BLOCK_MATERIAL}
```

### 杀死暴民 {#kill-mob}

杀死一个小怪可以获得经验值。这适用于任何原版生物。

```yml
killmob{type=MOB_ENTITY_TYPE;amount=1-3}
```

### 杀死神话暴民 {#kill-mythic-mob}

杀死 MythicMob 可获得经验值。你需要使用`type`参数提供生物的ID。

```yml
killmythicmob{type=MobInternalName;amount=1-3}
```

### 鱼物品 {#fish-item}

钓鱼指定类型的物品可获得经验值。

```yml
fishitem{type=ITEM_MATERIAL;amount=1-3}
```

### 冶炼物品 {#smelt-item}

当物品被熔炼（熔炉）时。

```yml
smeltitem{type=ITEM_MATERIAL;amount=1-3}
```

### 工艺物品 {#craft-item}

当制作物品时。

```yml
craftitem{type=ITEM_MATERIAL;amount=1-3}
```

### 酿造药水 {#brew-potion}

[有关炼金术](../profession/alchemy.md)的更多信息。你可以在此处指定多个药水效果，以逗号分隔。

```yml
brewpotion{effect="SPEED,REGEN,...";amount=1-3}
```

### 放置块 {#place-block}

放置指定类型的方块可获得 xp。

```yml
placeblock{type=BLOCK_MATERIAL;amount=1-3}
```

### 修复物品 {#repair-item}

你可以在`smithing.yml`中定义每种材料的 xp 数量。更多信息请参见 [Smithing](../profession/smithing.md)wiki 页面。

```yml
repairitem{type=ITEM_MATERIAL}
```

### 附魔物品 {#enchant-item}

附魔物品时获得经验。 [有关迷人](../profession/enchanting.md)的更多信息。

```yml
enchantitem{type=...}
```

### 攀登 {#climb}

当你爬上一个街区时。型号可以是`ladder`、`vines`、`weeping-vines`、`twisting-vines`。如果你不指定任何类型，它将触发所有类型。

```yml
climb{type=BLOCK_TYPE;amount=1-3}
```

### 吃 {#eat}

提供食用某些特定食物时的经验。如果你没有指定该类型的材料，无论你吃什么，它都会给出exp。

```yml
eat{type=ITEM_MATERIAL;amount=1-3}
```

### 移动 {#move}

为每个行驶过的街区提供经验，类型可以是`sneak`、`fly`、`swim`、`sprint`或`walk`。如果不指定就会一直触发。

```yml
move{type=MOVING_TYPE;amount=1-3}
```

### 资源 {#resource}

给出消耗的每个“RESOURCE_TYPE”类型资源的exp。资源类型可以是`health`、`mana`、`stamina`或`stellium`。

```yml
resource{type=RESOURCE_TYPE;amount=1-3}
```

### 骑行 {#ride}

当你骑着某个实体移动时。检查 [EntityType](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)枚举以指定类型。

```yml
ride{type=ENTITY_TYPE}
```

### 驯服 {#tame}

驯服小怪（如狼）时给出的经验值。每次点击触发一次。`type`是可选的，如果没有提供，它适用于所有生物类型。

```yml
tame{amount=1-3}
```

### 驯服实体伤害 {#tamed-entity-damage}

当你的驯服小怪造成伤害时会给出经验值。提供的经验值乘以最终的伤害输出。`type`是可选的，如果没有提供，它适用于所有生物类型。

```yml
tame{type=WOLF;amount=1-3}
```

### 受到的伤害 {#damage-taken}

玩家因某种原因受到伤害时给出的每次伤害的经验值。类型可以是`DROWNING`、`FALL`、`FIRE`等...你可以在 [此处](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)] 找到可能的损坏原因列表。

```yml
damagetaken{type=DAMAGE_CAUSE}
# or all damage causes
damagetaken{amount=1}
```

### 造成的伤害 {#damage-dealt}

特定 MMO 伤害类型所造成的伤害所给出的经验值。损坏类型可以是`magic`、`physical`、`weapon`、`skill`、`projectile`、`unarmed`、`on-hit`、`minion`或`dot`。

```yml
damagedealt{type=DAMAGE_TYPE}
# or all damage types
damagedealt{amount=1}
```

---

原文：[🪴 Experience Sources](https://docs.phoenixdevt.fr/mmocore/level/sources) · 原文归档：2026-10-19
