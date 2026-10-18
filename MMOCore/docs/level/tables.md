---
title: 经验表
source: https://docs.phoenixdevt.fr/mmocore/level/tables
source_snapshot: '2026-10-19'
---

# 经验表 {#📋-experience-tables}

此功能在MMOCore1.8.3中引入，旨在让玩家在升级提升其副职业时获得更复杂的奖励。其主要功能是给每 N 个副职业等级奖励玩家升级。你还可以为每个“经验drop”配置领取机会，以获得额外的随机性。这是默认的`exp-tables.yml`配置文件

```yml
example_exp_table:
  first_table_item:

    # This item will drop every 3 levels
    period: 3

    # This item has a 80% chance in fact to drop
    chance: 80

    # The level at which the item will be claimed for the first time
    first-trigger: 5

    # Every successive fail in claiming the item will reduce
    # the risk of failing future claims by X%. With a 80%
    # fail reduction rate, chances become:
    # - 80%
    # - 96%
    # - 99.2%
    # - 99.84%
    # so on forever..
    #
    # This is better than just increasing the claim chance by a
    # certain amount each time because otherwise the claim chance
    # just becomes/surpasses 100% at some point.
    fail-reduction: 80

    # What happens when that item is claimed
    triggers:
      - 'exp{amount=20}'
      - 'command{format="broadcast That''s three levels"}'

  # Will be used at level 7,9,11,13
  second_table_item:
    period: 2
    first-trigger: 7
    last-trigger: 13
    triggers:
      - 'exp{amount=80}'
      - 'command{format="broadcast Boy, %player_name% level up twice in one of his(her) professions!"}'

second_exp_table:

  # Base exp every level up, sweet.
  some_item:
    period: 1
    triggers:
      - 'exp{amount=100}'

  # Extra exp every 3 levels
  some_other_item:
    period: 3
    triggers:
      - 'exp{amount=100}'

last_example:

  # Only triggers when getting lvl2
  # Perfect for meticulous exp tables
  level_two:
    level: 2
    triggers:
      - 'exp{amount=100}'

  # Only triggers at lvl 3
  # Perfect for meticulous exp tables
  level_three:
    level: 3
    triggers:
      - 'exp{amount=120}'
  
  # Etc.
  # Add as many items as you want
```

## 基本设置 {#general}

一张经验表被分解为多个 *物品* （经验表中的每个物品有一个配置部分）。 *物品* 是一组奖励，每 Y副职业等级有 X% 的机会被领取。`period`选项（在升级中）指示应将物品提供给玩家的频率。`chance`选项确定玩家被赋予物品的机会。

你可以通过向`triggers`标识的列表添加或删除触发器来编辑物品的奖励。你可以在[此处](../misc/triggers.md)找到可在 exp 表内使用的所有可用触发器的列表。

## 第一个和最后一个触发器 {#first-last-trigger}

使用`first-trigger`选项，你可以选择玩家在领取物品之前必须达到的等级。如果第一个触发电平设置为5且周期设置为10，则物品将按等级5、10、15等声明。如果你没有为该设置指定任何内容，则将其设置为物品周期默认。

`last-trigger`选项允许你限制物品可以下降的等级。如果last-trigger设置为8，周期为2，则物品将在等级2、4、6和8被声明。如果未指定任何内容，则last-trigger将设置为无穷大 (no-limitation)。

如果你希望物品只能领取一次，请将期间设置为0。

## 固定水平 {#fixed-level}

通过使用选项`level: <some_integer>`，你可以创建仅在一个特定等级触发的物品。这可以用于更细致的经验表，或者仅仅用于独特的奖励，例如解锁技能、航路点等。

## 减少失败 {#fail-reduction}

如果玩家不走运并且没有认领物品之一，那么最后一个选项（`fail-reduction`）会派上用场，因为它降低了进一步坏运气的风险。让我们通过一个示例来看看它是如何工作的：假设物品索赔机会设置为60%，失败减少百分比设置为50%。将其设置为50%意味着每次未能领取物品的升级都会将剩余的未再次领取的机会减半。连续的领取机会是60%、80%、90%、95%、97.5%（每次到100%的距离减半）。

*对于那些熟悉数学的人来说，连续失败的机会描述了一个几何序列*

`triggers`选项是你定义声明物品时发生的情况的位置。为了获得最大的可配置性，这是一个[触发器](../misc/triggers.md)...你最常使用的触发器是`experience`和`command`触发器，经验将经验给你的主职业，以及从其他插件提供奖励的命令（如果需要）。

---

原文：[📋 Experience Tables](https://docs.phoenixdevt.fr/mmocore/level/tables) · 原文归档：2026-10-19
