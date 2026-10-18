---
title: 数值属性
source: https://docs.phoenixdevt.fr/mmoitems/features/stats/numerical-stats
source_snapshot: '2026-10-19'
---

# 数值属性 {#numerical-stats}

通过 *数字属性* 我们指的是物品属性的80%：

## 概览 {#overview}

大多数数值属性（攻击伤害/暴击几率/PvE伤害/...）或更具体的物品选项（能力调节器、药水效果持续时间/等级、附魔等级）都具有数字输入的公式。这些公式经过调整，可以在RPG服务器场景中轻松提供实际的属性值，不过你也可以选择使数字输入更容易配置。

数字输入（数字属性、能力修饰符...）可以随物品等级缩放。物品等级是生成物品时“随机”选取的常数。一般来说，物品等级越高，属性越好。

使用的公式如下：

```yml
attack-damage: # Could be any stat
    base: 10
    scale: 2
```

`base`是属性值，对应于等级0物品。`scale`是属性每增加一个额外等级所获得的额外值。使用上面给出的公式，如果物品等级为6，则属性值将为`10 + (2 * 6) = 22`。因此，一般公式为`stat_value = base + item_level * scale`*.*

如果你不希望属性在物品等级上缩放，请将缩放参数设置为0，或使用以下格式：

```yml
attack-damage: 10
```

## 为数值属性添加随机性和真实感 {#adding-randomness-realism-to-numerical-stats}

在RPG游戏中，你掉落的物品永远不会有仅取决于等级的平坦属性：它们有一个额外的随机因素，这使得一些物品好，因为它们总体略高属性，而另一些则不好，因为它们总体较低属性。MMOItems与数字物品属性具有类似的功能。

### 指定数值范围属性 {#specify-a-range-for-numerical-stats}

通过使用以下格式，将在给定的下限和上限内随机选取属性值。

```yml
attack-damage:
    min: 10
    max: 20
```

这是获取随机属性值的简单方法。如果你不想对属性值造成太多混乱，那就这么做吧。如果你想为服务器添加更深层次的RPG触摸，你可以选择更现实的选项（与RPG游戏中使用的公式相同），但设置起来有点困难。

### 使用正态分布 {#use-a-normal-distribution}

正态分布是一种变量分布，在数学、物理、自然等领域中随处可见……这就是我们将用于属性值的分布。让我们先检查一下格式，然后再将其完全分解。

```yml
attack-damage:   # Unchanged
    base: 10     # Unchanged
    scale: 2     # Unchanged
    spread: .1
    max-spread: .3
```

首先，请记住，我们希望属性值是`base + item_level * scale`的平均值，因为如果没有随机性，这将是属性值。当对属性值“应用”正态分布时，`spread`参数是随机生成的属性值与平均值之间的平均差。价差越高，属性值的分布就越大。较低的价差将导致属性值更加集中在平均值周围。

你应该使用大约0.1的价差，导致70%值的范围从-10%到 +10%，而95%值的范围从-20%到 +20%。

`max-spread`是与平均值的最大差异。你应该将此参数设置为30%到50%左右，这样正态分布就不会生成属性值over-powered。通过这种分布，生成属性值（即10x平均值）的风险仍然很小，为了游戏公平性，我们不希望发生这种情况。

你还可以使用以下格式向此gaussian-distribution-based数值公式添加常数下/上界（尽管与属性缩放配合使用时实用性有限）：

```yml
attack-damage:     # Unchanged
    base: 10       # Unchanged
    scale: 2       # Unchanged
    spread: .1     # Unchanged
    max-spread: .3 # Unchanged
    min: 10
    max: 20
```

---

原文：[Numerical Stats](https://docs.phoenixdevt.fr/mmoitems/features/stats/numerical-stats) · 原文归档：2026-10-19
