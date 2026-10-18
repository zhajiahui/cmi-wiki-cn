---
title: 内置兼容
source: https://docs.phoenixdevt.fr/mmoitems/compatibility/plugins
source_snapshot: '2026-10-19'
---

# 内置兼容 {#🦾-built-in-compatibility}

本节列出了MMOItems中实现的所有built-in兼容性。

## WorldGuard标志 {#worldguard-flags}

MythicLib实现了适用于MMOCore和MMOItems的新标志。请参阅[此处的完整列表](../../mythiclib/features/compatibility.md#flag-plugins)。

与任何其他插件一样，[WorldGuard](http://www.enginehub.org/worldguard)应在服务器启动时由MMOItems自动检测到。你可以在加载插件时检查控制台，以确保检测到它。

## 自定义附魔插件 {#custom-enchantments-plugins}

MMOItems与 EcoEnchants、MythicEnchants 和 AdvancedEnchants 兼容（不推荐）。它很可能与其他附魔插件本身不兼容，尽管设计良好的附魔插件应该没有问题（例如，EcoEnchants）。更多信息请参见[此 wiki 页面](enchant-plugins.md)。

## RPG 插件 {#rpg-plugins}

> **提示**
>
> 我们建议使用 [MMOCore](https://www.spigotmc.org/resources/70575/)以获得完整的本机插件兼容性。

MMOItems支持来自[以下插件](../../mythiclib/features/compatibility.md#rpg-plugins)的等级、职业和魔力/耐力。  这些插件中的等级和职业被转发到MMOItems，以便将职业和等级要求应用于物品。

虽然大多数RPG核心插件具有魔力功能，但 *Max魔力*属性仅适用于MMOCore、Heroes和built-inMythicLib魔力/耐力模块。其他插件不允许向玩家提供临时属性，因此MythicLib不可能向玩家提供最大魔力/耐力。

## Aurelium技能 {#aureliumskills}

MMOItems引入了新的属性，为玩家提供更多技能以及物品限制，阻止玩家使用特定的物品，除非它们在技能中至少具有 X 等级。为了让这些属性显示在物品描述中，请将其添加到你的`stats.yml`配置文件中：

```yml
additional-wisdom: '&3 &7■ Extra Wisdom: &f{value}'
additional-health: '&3 &7■ Extra Health: &f{value}'
additional-regeneration: '&3 &7■ Extra Regeneration: &f{value}'
additional-luck: '&3 &7■ Extra Luck: &f{value}'
additional-toughness: '&3 &7■ Extra Toughness: &f{value}'
additional-strength: '&3 &7■ Extra Strength: &f{value}'
additional-crit-damage: '&3 &7■ Extra Crit Damage: &f{value}'
additional-crit-chance: '&3 &7■ Extra Crit Chance: &f{value}'
required-farming: '&eRequires {value} in Farming'
required-foraging: '&eRequires {value} in Foraging'
required-mining: '&eRequires {value} in Mining'
required-fishing: '&eRequires {value} in Fishing'
required-excavation: '&eRequires {value} in Excavation'
required-archery: '&eRequires {value} in Archery'
required-defense: '&eRequires {value} in Defense'
required-fighting: '&eRequires {value} in Fighting'
required-endurance: '&eRequires {value} in Endurance'
required-agility: '&eRequires {value} in Agility'
required-alchemy: '&eRequires {value} in Alchemy'
required-enchanting: '&eRequires {value} in Enchanting'
required-sorcery: '&eRequires {value} in Sorcery'
required-healing: '&eRequires {value} in Healing'
required-forging: '&eRequires {value} in Forging'
```

然后将其发送给你的`lore-format.yml`：

```yml
  ...
  - '#additional-wisdom#'
  - '#additional-health#'
  - '#additional-regeneration#'
  - '#additional-luck#'
  - '#additional-toughness#'
  - '#additional-strength#'
  - '#additional-crit-chance#'
  - '#additional-crit-damage#'
  - '#required-farming#'
  - '#required-foraging#'
  - '#required-mining#'
  - '#required-fishing#'
  - '#required-excavation#'
  - '#required-archery#'
  - '#required-defense#'
  - '#required-fighting#'
  - '#required-endurance#'
  - '#required-agility#'
  - '#required-alchemy#'
  - '#required-enchanting#'
  - '#required-sorcery#'
  - '#required-healing#'
  - '#required-forging#'
  - '#required-forging#'
```

## MythicMobs {#mythicmobs}

MMOItems让你的神话小怪从 MI 掉落物品。请参考[此wiki页面](../items/drop-tables.md)。

## PlaceholderAPI {#placeholderapi}

请参阅 [此 wiki 页面](../general/placeholders.md)上的占位符的完整列表。

## 角色扮演游戏物品栏 {#rpginventory}

MMOItems支持 [RPGInventory](https://www.spigotmc.org/resources/12498/)：玩家可以在其自定义物品栏中装备MMOItems中的物品，并从其属性中受益。然而，由于 RPGInventory 不支持物品基础属性修饰符，因此基于原版基础属性修饰符（如攻击速度、最大生命值和移动速度）的属性不适用于non-armor/手物品插槽（i.e额外插槽，如配件插槽）。任何其他物品效果都可以正常工作。

然而，MMOInventory可以与MMOItems完美配合。

## 老板商城专业版 {#bossshoppro}

MMOItems为BossShopPro添加了一种特殊类型的奖励。当用户点击物品时，此奖励类型可用于为玩家提供物品。以下是设置 MMOItem 奖励类型时需要使用的格式：

```yml
RewardType: MMOITEM
Reward:
- <ITEM_TYPE>.<ITEM_ID>
- <ITEM_TYPE>.<ITEM_ID>
- etc.
```

## MythicMobs {#mythicmobs-1}

你可以将物品从 MI 添加到MythicMobs删除表：有关 [此页面](../items/drop-tables.md#adding-mmoitems-to-mythicmobs-drop-tables)的更多信息]。

---

原文：[🦾 Built-in Compatibility](https://docs.phoenixdevt.fr/mmoitems/compatibility/plugins) · 原文归档：2026-10-19
