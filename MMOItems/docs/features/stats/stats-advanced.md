---
title: 高级属性
source: https://docs.phoenixdevt.fr/mmoitems/features/stats/stats-advanced
source_snapshot: '2026-10-19'
---

# 高级属性 {#advanced-stats}

随机生成的物品可以具有 **数字属性**，如攻击伤害、攻击速度、暴击几率，但你也可以添加更多 **复杂的属性** ，如能力或永久药水效果，其威力也随着物品等级而缩放。这些属性更复杂，因此设置起来有点困难。

请记住，在该页面中找到的任何代码片段都将位于物品gen 模板的`base`配置部分（对应于模板基础物品数据），或者位于物品gen 修改器的`stats`配置部分：

```yml
ITEM_TEMPLATE_EXAMPLE:
  base:
    material: IRON_SWORD
    # <======== either here
  modifiers:
    first-modifier:
      prefix: 'Modifier Prefix'
      stats:
        attack-damage: 3
        # <======= or here
```

## 能力 {#abilities}

使用物品生成器，你可以创建具有特殊能力的物品，物品等级越高，其能力就越强。准确地说，能力具有可以在物品等级上缩放的修饰符（造成多少伤害，药水效果持续多长时间......）。使用此格式向物品gen 模板/物品gen 修改器添加能力：

```yml
ability:
  first-ability-id:
    type: burn
    mode: on_hit

    # First ability modifier
    cooldown:
      base: 6
      spread: .1
      max-spread: .3

    # Second ability modifier
    duration:
      base: 3
      scale: .2
  second-ability:
    type: life-ender
    mode: right-click
    damage:
      base: 10
      scale: 3
  third-ability:
    type: blizzard
    mode: left-click
    damage:
      base: 5
    cooldown:
      base: 7
      scale: 2
```

你可能会注意到，该格式与你想要向普通（不是随机生成的）mmoiite 添加能力的格式完全相同。唯一改变的是如何定义能力修饰符，因为它们是唯一可以在物品等级上真正缩放的值。用于定义能力修饰符的公式与 [numeric属性](numerical-stats.md)所使用的公式相同。

在此示例中，on-hit刻录能力具有6s冷却时间，但该值平均波动 +/-10%，最大相对偏移为10%。燃烧持续6秒，但每物品等级持续时间就会增加0.2秒。

请注意，如果你想指定能力修饰符但不希望其缩放，则仍必须指定基础，并将缩放和/或max-spread设置为0或完全删除它们。请参阅上面标题为`third-ability`的示例。在此示例中，使用暴风雪能力生成的每个物品的伤害将为5。但是，冷却时间仍将按指定进行缩放。

## 食用消耗品时获得的药水效果 {#potion-effects-obtained-when-eating-a-consumable}

请记住，药水效果由三个参数定义：药水效果类型、持续时间和药水等级。

```yml
effects:
  speed:
    level:
      base: 1
      scale: 1
    duration:
      base: 10
      scale: 3
```

请注意，你如何开始看到基于`base/scale/spread/maxspread`的配置部分的重复模式，在处理随机生成的物品时，这些配置部分似乎无处不在。与任何其他数值一样，药水持续时间和等级可以按物品等级缩放。

由于这些是数字属性，如果你希望每次等级都相同，你也可以使用此格式：

```yml
effects:
  speed:
    level: 1
    duration: ...
```

这与下面的完全相同

```yml
effects:
  speed:
    level:
      base: 1
      scale: 0
      spread: 0
      max-spread: 0
    duration: ...
```

你可以在 [Spigotjavadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html)] 中查看Minecraft效果列表。

## 永久药水效果 {#permanent-potion-effects}

它实际上与消耗品药水效果相同（见上文），但由于当持有特定物品时，这些药水效果应该永久赋予玩家，因此你**不必指定效果持续时间**。`level`配置部分也消失了，因为没有它它会更干净。

```yml
perm-effect:
  speed:
    base: 1
    scale: 1
  # That format works too
  haste: 3
```

## 结界 {#enchantments}

结界由结界类型和等级定义。使用这种格式：

```yml
enchants:
  efficiency:
    base: 1
    # There is no Efficiency 1.3, but that means that every
    # 10 levels, the item will have an extra efficiency
    # enchant level! This can also be used with potion effect levels.
    scale: .1
  # That format still works because an enchant level is a numeric value
  sharpness: 10
```

## 物品元素属性 {#item-elemental-stats}

```yml
element:
  fire:
    defense: 
      base: 10
      scale: 3
    # That format still works!
    damage: 10
  water:
    defense: 50
```

## 消耗品恢复电源 {#consumable-restore-power}

恢复能力定义了消耗品在使用时恢复的生命值、食物和饱和度。

```yml
restore:
  health:
    base: 3
    scale: 2
    spread: .3
    max-spread: .5
  # You could use a complex formula for food, or just use this format
  food: 5
  saturation: 3
```

---

原文：[Advanced Stats](https://docs.phoenixdevt.fr/mmoitems/features/stats/stats-advanced) · 原文归档：2026-10-19
