---
title: 玩家属性
source: https://docs.phoenixdevt.fr/mythiclib/features/stats
source_snapshot: '2026-10-19'
---

# 玩家属性 {#💪-player-stats}

MMOItems和MMOCore共享相同的属性系统。你通过放置在MMOInventory物品栏内的MMOItems物品、MMOCore职业或物品获得的任何属性都将传播到所有 MMO 插件。

在此页面中，我们查看`MythicLib/stats.yml`配置文件。除非另有指定，否则所有 YML 片段都将在此配置文件内使用。

## 临时属性 {#temporary-stats}

临时属性或 *属性修正器* 是在有限/无限时间内给予玩家的属性增强/减益。无论哪种方式，这些属性都会在服务器重新启动时删除。

### 使用脚本 {#using-a-script}

请注意，你可以使用`add_stat`脚本机制将临时属性赋予玩家。你可以在 [此 wiki 页面](../scripts/mechanics/buffs.md#add-temporary-stats)上找到更多信息。当服务器重新启动时，这些属性将被删除。

### 使用命令 {#using-commands}

向玩家提供临时属性的最简单方法是通过命令。

```cmd
/ml stat add <player> <stat> <amount> (duration) (key) (unique)
/ml stat remove <player> <stat> <key>
/ml stat clear <player> <key>
```

使用`add`子命令，你可以将属性修正器提供给玩家。

- 如果你通过`duration`参数提供持续时间（以刻为单位），则属性将是临时的并在该时间之后删除。
- 如果你提供`key`，则稍后可以使用`remove`子命令删除此属性修正器。如果你不提供任何密钥，它将使用默认密钥`default`。
- 如果将`unique`设置为true，则一次只有一个具有相同键的修改器会处于活动状态；添加新的将取代先前的。这对于你想要定期刷新的增益效果非常有用。

> **示例**
>
> 以下命令使用密钥`my_custom_buff`向玩家`Notch`提供 Flat +10攻击伤害属性持续5秒（100刻）。如果再次执行相同的命令，它不会覆盖前一个命令，因为`unique`设置为false，并且它会与自身堆栈。
>
```cmd
/ml stat add Notch ATTACK_DAMAGE 10 100 my_custom_buff false
```

使用`remove`子命令，你可以使用`key`从玩家中删除特定的属性修正器。

> **示例**
>
> 以下命令取消注册上一示例中给出的属性修正器。
>
```cmd
/ml stat remove Notch ATTACK_DAMAGE my_custom_buff
```

使用`clear`子命令，你可以从玩家中删除所有属性修正器以及关联的`key`。

> **示例**
>
> 以下命令从玩家`Notch`中删除带有密钥`my_custom_buff`的所有属性修正器。
>
```cmd
/ml stat clear Notch my_custom_buff
```

## 最小/最大属性值 {#min-max-stat-values}

属性值的最小值和最大值。这意味着对CRITICAL_STRIKE_CHANCE使用“0=100”意味着你的值不能小于0%且不能大于100%暴击几率。这是服务器平衡的重要工具。你可以平衡属性，如格挡等级、防御、最大生命值、伤害减少等。

- 一般格式为`{min_value} = {max_value}`
- 仅使用`= {max_value}`将禁用下限。
- 仅使用`{min_value} =`将禁用上限。
- 如果未指定任何内容，则没有上限或下限。

> **信息**
>
> 基本属性值和最小值之间存在细微差别。最小/最大值用于限制属性总值。属性总值是基本属性值和所有修饰符的总和。换句话说，基本属性值就像永久的属性buff。

你将在`MythicLib/stats.yml`配置文件中找到以下代码片段。

```yml
min-max-values:

  # Crits
  CRITICAL_STRIKE_CHANCE: '0 = 80'
  CRITICAL_STRIKE_POWER: '0 = 500'
  SKILL_CRITICAL_STRIKE_CHANCE: '0 = 80'
  SKILL_CRITICAL_STRIKE_POWER: '0 = 500'

  # Mitigation
  BLOCK_RATING: '0 = 80'
  DODGE_RATING: '0 = 80'
  PARRY_RATING: '0 = 80'
  BLOCK_POWER: '25 = 75'

  BLOCK_COOLDOWN_REDUCTION: '0 = 80'
  DODGE_COOLDOWN_REDUCTION: '0 = 80'
  PARRY_COOLDOWN_REDUCTION: '0 = 80'

  # Other
  MOVEMENT_SPEED: '0 = .3'
  DEFENSE: '0 = 10000'
  SPEED_MALUS_REDUCTION: '0=80'

  # Add as many as you want.
```

## 属性基本值 {#base-stat-values}

修改`MythicLib/stats.yml`内的属性的基值与对玩家应用永久平坦属性增益效果或减益效果相同。如果你的MMOCore职业具有20基数 *最大生命值* ，并且你将 *最大生命值*属性的基数设置为10，则结果 *最大生命值* 为`10 + 20 = 30`。

当你想要按固定量调整服务器上所有玩家的基本属性值时，此功能最有用。如果你使用的是MMOCore，你可能根本不需要此功能，因为你可能会发现简单地编辑职业的基本属性值会更容易。

请注意，默认的Minecraft属性，如 *最大生命值*、*护甲*、*攻击伤害* 和 *攻击速度* 自然具有由原版Minecraft定义的non-zero基值。例如， *最大生命值* 的基值为20， *移动速度* 为0.1， *攻击速度* 为4， *攻击伤害* 为1等。这些原版基值**合计**此配置文件中指定的基值；它们不会被它们所覆盖。

请注意，`MMOCore/stats.yml`内部指定的基本属性值会覆盖原版基本属性值，而MythicLib基本属性值充当 **属性值调整（偏移）**。最后，[MMOCore职业配置](../../mmocore/features/classes.md#class-stats)中提供的属性公式覆盖`MMOCore/stats.yml`中提供的公式。

```yml
base-stat-value:

  # Crits. By default, crits deal 2x damage
  CRITICAL_STRIKE_POWER: 200
  SKILL_CRITICAL_STRIKE_POWER: 200

  # Mitigation
  BLOCK_POWER: 25

  # Add as many as you want.
```

## 属性代理 {#stat-proxies}

属性代理是一个非常有用的功能，它允许你创建提供其他属性** 的 **属性**。例如，你可以创建一个*强度*属性，对于每个点，*最大生命值* 增加4%点，*攻击力伤害* 增加1点。

如果使用 MMOCore，你可能会发现它与[基础属性](../../mmocore/features/attributes.md)相似。这是因为 MMOCore 的基础属性在内部就是通过属性代理实现的。属性代理可以看作 MMOCore 基础属性的扩展，而基础属性则为玩家提供了更容易使用属性代理的方式。

让我们看一下以下 YML 片段，你可以在`MythicLib/stats.yml`配置文件中找到该片段。

```yml
proxies:
  
  POWER:
    # 1 pt in Power gives +2% max health
    # and +1% atk damage 
    MAX_HEALTH:
      type: RELATIVE
      multiplier: 2
    ATTACK_DAMAGE:
      type: RELATIVE
      multiplier: 1

  MAX_HEALTH_PERCENT:
    # One unit in MAX_HEALTH_PERCENT increases
    # MAX_HEALTH by 1%, linearly
    MAX_HEALTH:
      multiplier: 1
      type: RELATIVE
```

此语法定义两个属性代理。第一个类似于我们之前提到的*强度*属性。此属性代理经过配置，以便`POWER`属性中的每个点自动提供 +2%*最大生命值* 和 +1%*Atk Damage*。

`multiplier`是对于源属性中的每个点，传输到目标属性的属性点的数量。`type`可以设置为`FLAT`以获得固定奖金，`RELATIVE`为基于百分比的奖金或`COMPOUND`为基于几何/复合百分比的奖金。当 type 设置为`RELATIVE`或`COMPOUND`时，`multiplier`应以百分比形式提供（即MythicLib会将给定值乘以`1/100`以将其表示为标量）。

### 基于%的属性 {#based-stats}

上面的代码片段定义的第二个代理提供了属性代理的另一个潜在用例。如果是特定的属性，比如`MAX_HEALTH`，因为MMOItems中没有 %-属性等效项，你可以创建一个中间/代理属性，它将线性增益效果转换为`MAX_HEALTH_PERCENT`属性到基于%的增益效果到`MAX_HEALTH`属性。

---

原文：[💪 Player Stats](https://docs.phoenixdevt.fr/mythiclib/features/stats) · 原文归档：2026-10-19
