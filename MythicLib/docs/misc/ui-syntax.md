---
title: 界面语法
source: https://docs.phoenixdevt.fr/mythiclib/misc/ui-syntax
source_snapshot: '2026-10-19'
---

# 界面语法 {#🎨-gui-syntax}

MythicLib为宝箱 UI物品栏提供统一语法。这包括MMOItems合成站、MMOProfiles档案选择 UI 以及所有MMOCoreUI，包括玩家属性、航点、队伍和朋友、职业选择等。

GUI插件配置位于`gui`或`language/gui`文件夹内。

在本教程中，我们将重点关注MMOCore基础属性菜单。

<details markdown="1">

<summary>原始配置</summary>

```yml

# GUI display name
name: Player Attributes

# Number of slots in your inventory. Must be
# between 9 and 54 and must be a multiple of 9.
slots: 27

items:
  reallocate:
    slots: [26]
    function: reallocation
    item: CAULDRON
    name: '&aReallocate Skill Points'
    lore:
    - ''
    - 'You have spent a total of &6{total}&7 skill points.'
    - '&7Right click to reallocate them.'
    - ''
    - '&eCosts 1 attribute reallocation point.'
    - '&e◆ Attribute Reallocation Points: &6{points}'
  str:
    slots: [11]
    function: attribute_strength
    name: '&a{name}'
    item: GOLDEN_APPLE
    lore: # {buffs} returns amount of buffs
    - ''
    - '&7Points Spent: &6{spent}&7/&6{max}'
    - '&7Current {name}: &6&l{current}'
    - ''
    - '&8When Leveled Up:'
    - '&7  +{buff_weapon_damage}% Weapon Damage (&a+{total_weapon_damage}%&7)'
    - '&7  +{buff_max_health} Max Health (&a+{total_max_health}&7)'
    - ''
    - '&eClick to level up for 1 attribute point.'
    - '&e◆ Current Attribute Points: {attribute_points}'
  dex:
    slots: [13]
    function: attribute_dexterity
    name: '&a{name}'
    item: LEATHER_BOOTS
    hide-flags: true
    lore:
    - ''
    - '&7Points Spent: &6{spent}&7/&6{max}'
    - '&7Current {name}: &6&l{current}'
    - ''
    - '&8When Leveled Up:'
    - '&7  +{buff_physical_damage}% Physical Damage (&a+{total_physical_damage}%&7)'
    - '&7  +{buff_projectile_damage}% Projectile Damage (&a+{total_projectile_damage}%&7)'
    - '&7  +{buff_attack_speed} Attack Speed (&a+{total_attack_speed}&7)'
    - ''
    - '&eClick to level up for 1 attribute point.'
    - '&e◆ Current Attribute Points: {attribute_points}'
  int:
    slots: [15]
    function: attribute_intelligence
    name: '&a{name}'
    item: BOOK
    lore:
    - ''
    - '&7Points Spent: &6{spent}&7/&6{max}'
    - '&7Current {name}: &6&l{current}'
    - ''
    - '&8When Leveled Up:'
    - '&7  +{buff_magic_damage}% Magic Damage (&a+{total_magic_damage}%&7)'
    - '&7  +{buff_cooldown_reduction}% Cooldown Reduction (&a+{total_cooldown_reduction}%&7)'
    - ''
    - '&eClick to level up for 1 attribute point.'
    - '&e◆ Current Attribute Points: {attribute_points}'
```

</details>

## 一般选项 {#general-options}

你可以编辑常规GUI设置，例如其名称和插槽。

```yml
name: 'Player Attributes'
slots: 27
```

请注意`items`部分下的配置部分如何共享非常相似的属性：`name`（物品显示名称）、`lore`（物品描述/描述）、`item`（物品材料）、`slots`（其中物品放置在物品栏中，它可以是一个列表）和`function`（物品的作用）。这些都可以（并且应该）根据你的需要进行编辑。

### 编辑物品插槽 {#editing-item-slots}

如果你想让物品显示在多个插槽上，请使用以下语法：

```yml
slots: [1, 2, 3, 4]
#slots: 1 # This won't work
#slot: 1  # This won't work
```

## 物品功能 {#item-functions}

`function`告诉MythicLib单击时物品会做什么，以及占位符在物品描述中应用什么。在MMOCore基础属性菜单中工作的功能在MMOProfiles档案选择菜单中不起作用。每个GUI都有自己的一套内置物品功能。

一般来说，你并不真的想更改它，除非你要添加通用物品功能，例如“返回”或“关闭”按钮。你可以根据需要编辑物品视觉效果，但更改功能将更改物品行为以及应用于它的占位符，因此在编辑之前请确保你知道自己在做什么。

在以下示例中，物品使用内置`attribute_<attribute_name>`函数，该函数应用与MMOCore玩家基础属性相关的占位符和点击处理程序。

```yml
# [...]
items:
# [...]
  item_strength:
    slots: [15]
    function: attribute_strength
    name: '&a{name}'
    item: BOOK
    lore:
      #.....
      - '&8When Leveled Up:'
      - '&7  +{buff_weapon_damage}% Weapon Damage (&a+{total_weapon_damage}%&7)'
      - '&7  +{buff_max_health} Max Health (&a+{total_max_health}&7)'
      #.....
```

## 描述占位符 {#lore-placeholders}

选择物品函数会解锁特定的占位符，你可以在物品名称和描述中使用它。例如，MMOCore基础属性菜单中的`attribute_<attribute_name>`函数解锁以下占位符：

|占位符|描述 |
| --- | --- |
| `{spent}` | 玩家在该基础属性中花费的基础属性点金额 |
| `{max}` | 你可以在该基础属性中花费的最大金额基础属性点 |
| `{name}` | 基础属性名称 |
| `{current}` | 目前的基础属性为玩家。考虑到MMOItems和其他插件的修饰符。 |
| `{buff_<stat>}` | 增益效果授予在该基础属性中花费的每一点。 |
| `{total_<stat>}` | 基础属性中花费的所有积分所授予的总计增益效果（`{spent}`和`{buff_xxx}`的乘积）。 |

## 可点击物品 {#clickable-items}

如果你没有为物品指定任何函数，则可以使用以下语法提供要在单击物品时执行的 [MythicLib脚本](../scripts/intro.md)：

```yml
items:
  log_out:
    slots: [ 44 ]
    item: BELL
    name: "&cLog Out"
    script:
      - command{format="kick %player_name% You successfully logged out"}
```

你还可以提供MythicLib脚本的名称，而不是机制列表。

```yml
items:
  log_out:
    # [...]
    script: my_custom_kick_mythiclib_script
```

---

原文：[🎨 GUI Syntax](https://docs.phoenixdevt.fr/mythiclib/misc/ui-syntax) · 原文归档：2026-10-19
