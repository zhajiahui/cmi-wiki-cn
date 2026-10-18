---
title: 物品套装
source: https://docs.phoenixdevt.fr/mmoitems/features/sets
source_snapshot: '2026-10-19'
---

# 物品套装 {#🛡️-item-sets}

物品套装允许你将多个物品连接在一起，使它们在同时佩戴时更坚固。  如果物品套装佩戴了足够多的物品套装中的物品，则为玩家提供额外的属性。配置文件非常不言自明；这是一个配置片段。

```yml
ARCANE:
  name: '&2Arcane Set'
  bonuses:
    '3':
      magic-damage: 20
    '4':
      max-mana: 30
      potion-speed: 1
  lore-tag:
  - '&7Arcane Set Bonus:'
  - '&8[3] +20% Magic Damage'
  - '&8[4] 30 Max Mana'
  - '&8[4] Permanent Speed I'
```

## 设定奖金 {#set-bonuses}

可以使用 *lore-tag* 选项在物品描述中显示设置的奖金。你确实可以在该列表中添加任何内容，但我喜欢精确给出物品提供的额外属性的数量。奖金部分定义了物品套装提供的奖金。带数字的小节对应于物品套装为玩家佩戴的每个物品授予的属性。

全套可以赋予属性、能力、永久药水效果、权限以及粒子效果给玩家。

## 永久药水效果 {#permanent-potion-effects}

设置奖励可以为玩家授予**永久药水效果**。你需要指定药水效果名称（名称可以在[此处](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)] 找到）和药水等级（必须是整数）。你需要使用以下格式：`potion-<potion-effect-name>: <permanent-level>`。使用`potion-`前缀将向MMOItems表明你想要设置永久药水效果。

```yml
SPEED:
  name: '&2Speed Set'
  bonuses:
    '4':
      potion-speed: 1
      # ......
```

## 能力 {#abilities}

最后但并非最不重要的一点是，你还可以将**能力**设置为全套奖励。设置非常简单，因为它的格式与物品功能相同。在以下示例中，任何持有仇恨套装中至少2物品的玩家将被临时授予生命终结能力，该能力在击中任何实体时会触发。能力有30sec冷却时间。只需确保你使用的是`ability-`前缀，它向MMOItems表明你想要设置永久能力。

```yml
HATRED:
  name: '&cHatred Set'
  bonuses:
    '2':
      ability-1:
        type: LIFE_ENDER
        cooldown: 30
        mode: ON_HIT
      #......
```

## 粒子效果 {#particle-effects}

粒子效果的前缀是`particle-`。你可以在该前缀后添加任何你想要的内容。

```yml
HATRED:
  name: '&cHatred Set'
  bonuses:
    '2':
        particle-whatever_you_want_here:
          type: GALAXY
          particle: FLAME
          # Modifiers which are specific to the particle type (GALAXY in that case)
          height: 1
          speed: 1
        #......
```

你可以找到有关MMOItems粒子效果的更多信息 [此处](stats/stats.md#item-particles)。

## 权限 {#permissions}

你可以提供权限的列表，一旦玩家达到集合中的物品的特定数量，该列表将被授予。

```yml
HATRED:
  name: '&cHatred Set'
  bonuses:
    '2':
      granted-permissions:
        - 'hatred.fullset'
        - 'whatever.permission'
      #......
```

---

原文：[🛡️ Item Sets](https://docs.phoenixdevt.fr/mmoitems/features/sets) · 原文归档：2026-10-19
