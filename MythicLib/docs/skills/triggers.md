---
title: 触发器
source: https://docs.phoenixdevt.fr/mythiclib/skills/triggers
source_snapshot: '2026-10-19'
---

# 触发器 {#💥-triggers}

使用 MMOItems 或 MMOCore 时，需要指定技能何时执行，例如对实体造成伤害、受到伤害或潜行时。这通过触发器设置；MMOItems 过去将它们称为*施法模式*。

## 可用的触发器 {#available-triggers}

你可以在 MMO 插件中使用这些触发器类型来定义某些技能何时应该运行。

### 战斗与伤害 {#combat-damage}

|技能触发器 |描述 |目标实体 |目标块|
| --- | --- | --- | --- |
| KILL_ENTITY | 当玩家杀死实体时激活技能 | 被杀死的实体 | - |
| KILL_PLAYER | 当玩家杀死玩家时激活技能 | 被杀的玩家 | - |
| 攻击 | 当玩家攻击某物时激活技能 | 玩家攻击的实体 | - |
| 损坏 | 当玩家受到伤害时激活技能 | - | - |
| DAMAGED_BY_ENTITY | 当玩家受到实体伤害时激活技能 | 损坏玩家的实体 | - |
| 死亡 | 当玩家死亡时激活技能 | - | - |

### 投射物 {#projectiles}

| 技能触发器 | 描述 | 目标实体 | 目标块 |
| --- | --- | --- | --- |
| SHOOT_TRIDENT | 当玩家射出三叉戟时 | 投射物 | - |
| TRIDENT_TICK | 当三叉戟仍在半空中时激活每个刻 | 投射物 | - |
| TRIDENT_LAND | 当三叉戟落地时 | 投射物 | - |
| TRIDENT_HIT | 当投掷的三叉戟击中实体时 | 命中实体 | - |
| SHOOT_BOW | 当玩家射箭时 | 投射物 | - |
| ARROW_TICK | 当箭头仍在半空中时激活每个刻 | 投射物 | - |
| ARROW_LAND | 当箭落在地上时 | 投射物 | - |
| ARROW_HIT | 当射出的箭击中实体时 | 命中实体 | - |

### 玩家点击次数 {#player-clicks}

| 技能触发器 | 描述 | 目标实体 | 目标块 |
| --- | --- | --- | --- |
| RIGHT_CLICK | 玩家右键点击时 | - | - |
| LEFT_CLICK | 在玩家上左键单击 | - | - |
| SHIFT_RIGHT_CLICK | 在玩家上潜行时右键单击 | - | - |
| SHIFT_LEFT_CLICK | 在玩家上潜行时左键单击 | - | - |

### 积木 {#blocks}

| 技能触发器 | 描述 | 目标实体 | 目标块 |
| --- | --- | --- | --- |
| BREAK_BLOCK | 当玩家破坏方块时 | - | 开采区块的位置 |
| PLACE_BLOCK | 当玩家放置方块时 | - | 放置方块的位置 |

### MMOCore触发器 {#mmocore-triggers}

这些触发器仅在安装MMOCore时可用。如果你在未安装MMOCore的情况下尝试使用它们，将会遇到错误。

| 技能触发器 | 描述 | 目标实体 | 目标块 |
| --- | --- | --- | --- |
| ENTER_COMBAT | 当玩家进入 [战斗](../../mmocore/features/combat.md)] 时激活技能。 | - | - |
| QUIT_COMBAT | 当玩家退出时激活技能[战斗](../../mmocore/features/combat.md)。 | - | - |

### 物品 {#items}

| 技能触发器 | 描述 | 目标实体 | 目标块 |
| --- | --- | --- | --- |
| DROP_ITEM | 当玩家按 Q 时激活技能 | 掉落的物品 | - |
| SHIFT_DROP_ITEM | 当玩家按 Shift + Q 时激活技能 | 掉落的物品 | - |
| SWAP_ITEMS | 当玩家按 F 时激活技能 | - | - |
| SHIFT_SWAP_ITEMS | 当玩家按 Shift + F 时激活技能 | - | - |
| ~~EQUIP_ARMOR~~ | 当玩家装备护甲时激活技能 | 玩家 | - |
| ~~UNEQUIP_ARMOR~~ | 当玩家未装备护甲时激活技能 | 玩家 | - |

### 其他功能 {#miscellaneous}

| 技能触发器 | 描述 | 目标实体 | 目标块 |
| --- | --- | --- | --- |
| 登录 | 当玩家登录时激活技能 | - | - |
| 潜行 | 当玩家潜行时激活技能 | - | - |
| 传送 | 当玩家传送时激活技能 | - | 目标传送位置 |
| 定时器 | 每 X 个周期投射技能 | - | - |

## 当技能/脚本被触发时 {#when-a-skill-script-is-triggered}

某些触发器类型将特殊属性传递给它们触发的脚本/技能。例如;使用`ATTACK`触发类型时：

- `<target>`内部变量可用于访问被损坏的实体，
- `<attack>`内部变量返回有关当前攻击的元数据，
- `<attack.damage>`返回攻击伤害。

具有`ATTACK`、`DAMAGED`、`DAMAGED_BY_ENTITY`、`KILL_ENTITY`、`SHOOT_TRIDENT`、`ARROW_TICK`等实体/投射物的触发器类型允许用户使用`<target>`内部变量来访问射击投射物。这些触发器还解锁了[实体和位置目标选择器](../scripts/targeters/intro.md)的使用，例如`target`和`target_location`。

具有`TRIDENT_LAND`或`ARROW_HIT`等世界位置的触发器类型可解锁`target_location`位置目标选择器以及`<target_location>`内部变量。

某些触发器（例如`TIMER`或`RIGHT_CLICK`）不会解锁任何其他内部变量。

`ATTACK`是唯一解锁`<attack>`内部变量以及特殊机制 (`multiply_damage`) 或条件 (`has_damage_type`) 的触发器类型。

## 自定义触发器 {#custom-triggers}

MythicLib允许用户定义自己的触发器并手动调用它们。这是一个复杂但超级强大的功能，在现有技能的基础上添加了另一层可配置性。

### 定义自定义触发器 {#defining-custom-triggers}

你可以在`MythicLib/triggers.yml`配置文件中定义自定义触发器。请注意，该文件仅包含user-defined触发器，因为上面提供的触发器是hard-coded并且无法编辑。

```yml
# Triggered on weapon crits
# Corresponding on-hit effect: on_hit_effects/weapon_crits
# Call in script:              script/on_hit_effects.yml>weapon_crit_script
CRIT:

  # When set to false, send messages to the player
  # when skills cannot cast due to them being on cooldown,
  # missing mana/stamina....
  silent: true

# Triggered on special mage abilities
MAGE_BURN:
  silent: true
```

### 调用自定义触发器 {#calling-custom-triggers}

在 MMOLib 脚本中，可使用 `call_trigger` 机制调用自定义触发器。“调用触发器”是指施放指定玩家所有匹配该触发器的技能。例如，每次玩家或生物攻击时，MMOLib 都会在内部调用 `ATTACK` 触发器。

我们以built-in武器暴击为例。我们想要创建一个技能触发器，每当玩家在攻击时执行武器暴击时就会调用该触发器。

以下代码片段取自默认的`MythicLib/script/on_hit_effects.yml`文件，该文件定义了武器暴击的行为。

```yml
# Called to check if weapon crits may apply
weapon_crit_script_check:
  conditions:
    - 'has_damage_type{types="weapon,unarmed"}'

# Called when a weapon crit occurs
weapon_crit_script:
  mechanics:
    - 'set_double{var=crit_coef;val="<stat.critical_strike_power> / 100"}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=WEAPON}'
    - 'multiply_damage{scalar="<crit_coef>";dtype=UNARMED}'
    - 'mark_crit{dtype="WEAPON,UNARMED"}'
    - 'call_trigger{trigger=crit}'
    # [...]
```

正如你所看到的，当调用`weapon_crit_script`脚本时（i.e发生武器暴击时），脚本最终使用`call_trigger`机制来调用我们之前定义的`CRIT`user-defined技能触发器。这具有在触发器设置为`CRIT`的情况下施放所有施法者的技能的效果。

> **警告**
>
> 你可以使用`call_trigger`机制来调用任何触发器，而不仅仅是user-defined触发器。这可用于创建更复杂的行为，例如on-hit技能触发器，尽管用户有责任确保在调用built-in技能触发器时提供正确的技能元数据参数。

### 禁用user-defined触发器 {#disabling-user-defined-triggers}

此功能很难理解 - 如果你希望完全禁用此功能，只需注释掉/删除`triggers.yml`文件的内容即可。不要删除配置文件本身，否则它将重新生成其默认内容。

---

原文：[💥 Triggers](https://docs.phoenixdevt.fr/mythiclib/skills/triggers) · 原文归档：2026-10-19
