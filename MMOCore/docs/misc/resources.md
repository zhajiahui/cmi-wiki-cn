---
title: 玩家资源值
source: https://docs.phoenixdevt.fr/mmocore/misc/resources
source_snapshot: '2026-10-19'
---

# 玩家资源值 {#💖-player-resources}

MMOCore中有四个玩家资源，具有不同的目标。这些资源会随着时间的推移而再生。

- **生命值**
- **魔力** 和 **耐力**，用于施放 [技能](../skills/intro.md)并使用物品
- **stellium**，用于[航点](../features/waypoints.md)

## 基础资源再生 {#base-resource-regen}

MMOCore有**两种**类型的资源再生。首先，每个职业都有一个基础 **扁平** 资源再生属性，适用于四种资源中的任何一个。例如，*10耐力Regen* 表示玩家每秒重新生成10耐力点。如果你打开`off-combat-stamina-regen`职业选项，玩家将仅在脱离战斗时重新生成固定金额。

每个职业还具有另一个再生属性，如`Max Health Regeneration`，以每秒 %最大生命值表示。它是你每秒重新生成的最大生命值的百分比。第二个属性与第一个再生叠加。

```yml
# classes/mage/mage.yml

options:
  off-combat-health-regen: true

attributes:
  health-regeneration:
    base: 0.13
    per-level: 0
  max-health-regeneration:
    base: 1
    per-level: 0
```

在默认的MMOCore配置中，法师只有在脱离战斗时才会恢复生命值，*因为他们相当虚弱，必须集中精力才能恢复力量*。法师的基础回复值为0.13生命值 +1%的最大生命值/秒。

## 特殊资源再生 {#special-resource-regen}

MMOCore中的第二种类型的资源再生几乎可以被认为是被动的技能。职业可以设置为具有特殊类型的资源再生，可根据玩家的最大/缺失资源量进行缩放。这种特殊的资源再生也可以在战斗中关闭。

如果你想开发具有特殊类型资源的新职业，这可能特别有用。例如，拥有“怒气”而不是“魔力*”的战士，可以在脱离战斗时以更灵活的速度缓慢降低怒气。

资源再生（或丢失）的速率也可以配置。你还可以通过关闭`off-combat`选项来使再生在战斗中不适用。 **与第一种资源再生不同，这种资源再生完全独立于玩家佩戴的物品。它仅取决于玩家的等级。**

```yml
resource:

  # Health resource
  health:
    type: MAX
    value:
      base: 10
      per-level: 1
      max: 20
    off-combat: true

  # Mana resource
  mana:
    type: MISSING
    #......

  # Other resources....
```

这是一个强度很高的近战职业：脱离战斗后，玩家每秒恢复最大生命值的 10–20%，具体比例取决于当前等级。

`type`选项是`MAX`（根据最大资源进行缩放）或`MISSING`（根据缺失资源进行缩放），具体取决于你希望资源再生进行缩放的内容。`value`条目对应于每秒重新生成的资源的百分比。你可以使用`min`和`max`选项来创建玩家等级的有界线性函数。

---

原文：[💖 Player Resources](https://docs.phoenixdevt.fr/mmocore/misc/resources) · 原文归档：2026-10-19
