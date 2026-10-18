---
title: 插件兼容性
source: https://docs.phoenixdevt.fr/mythiclib/features/compatibility
source_snapshot: '2026-10-19'
---

# 插件兼容性 {#🦾-plugin-compatibility}

本节列出了MythicLib实现的所有插件挂钩。

## RPG 插件 {#rpg-plugins}

> **信息**
>
> 虽然我们建议使用 [MMOCore](https://www.spigotmc.org/resources/70575/)来实现完全的原生插件兼容性，但 MMO 插件套件在使用其他RPG核心插件时也可以工作。

MMO 插件支持以下RPG插件。玩家等级和职业适用于MMOItems物品要求和MMOInventory插槽限制。魔力和耐力适用于MMOItems和MMOCore物品和技能资源成本。

|插件 |等级|职业|魔力|耐力|注意|
| --- | --- | --- | --- | --- | --- |
| [MMOCore](https://www.spigotmc.org/resources/70575/) | ✔ | ✔ | ✔ | ✔ |  |
| [Heroes](https://www.spigotmc.org/resources/24734/) | ✔ | ✔ | ✔ | ✔ |  |
| [Fabled](https://www.spigotmc.org/resources/91913/) | ✔ | ✔ | ✔ | ❌ |  |
| [技能](https://www.spigotmc.org/resources/8981/)/ [SkillsPro](https://www.spigotmc.org/resources/skills-pro.8981/) | ✔ | ✔ | ✔ | ❌ |  |
| [种族和类别](https://www.spigotmc.org/resources/28029/) | ✔ | ✔ | ✔ | ❌ |  |
| [RPGPlayer练级](https://www.spigotmc.org/resources/11096/) | ✔ | ❌ | ✔ | ✔ | 耐力是*功率* |
| [AureliumSkills](https://www.spigotmc.org/resources/81069/)/ [AuraSkills](https://www.spigotmc.org/resources/81069/) | ✔ | ❌ | ✔ | ❌ | 等级为*功率等级* |
| [战斗等级](https://www.spigotmc.org/resources/battlelevels.2218/) | ✔ | ❌ | ❌ | ❌ |  |
| [mcMMO](https://www.spigotmc.org/resources/official-mcmmo.64348/) | ✔ | ❌ | ❌ | ❌ | 等级为*功率等级* |
| [McRPG](https://www.spigotmc.org/resources/mcrpg.63020/) | ✔ | ❌ | ❌ | ❌ | 等级为*功率等级* |
| MythicLib | ❌ | ❌ | ✔ | ✔ | 阅读更多内容 [此处](../misc/mana-stamina.md) |
| 占位符 | ✔ | ✔ | ❌ | ❌ | 阅读更多[下面](compatibility.md#using-placeholders) |

### 注释 {#notes}

MythicLib有一个用于魔力和耐力的built-in模块。运行 MMO 插件套件时，魔力通常由MMOCore提供。对于想要在没有MMOCore的情况下使用MMOItems的用户，我们提供了这个准系统魔力/耐力解决方案。该built-in模块取代了旧的 [魔力和耐力插件](https://github.com/mmopluginteam/mmoitems-mana)（不再维护）。

一些插件，如 [mcMMO](https://www.spigotmc.org/resources/official-mcmmo.64348/)或 [McRPG](https://www.spigotmc.org/resources/mcrpg.63020/)] 具有*功率等级*，通常是各个玩家的技能等级的总和。MythicLib将此功率等级解释为玩家的等级。

一些插件只有一种类型的玩家资源，通常是魔力。在这种情况下，耐力将替换为食品等级。第二个玩家资源几乎总是耐力。

### 使用占位符 {#using-placeholders}

你还可以使用PlaceholderAPI占位符向 MMO 插件提供玩家职业和等级。MythicLib将使用PlaceholderAPI解析占位符并将结果转发给MMO插件。

例如，如果你的RPG插件`SomeRpgCore`本身不受MMOCore支持，但为职业名称提供了`%somerpgcore_class%`占位符，请将`class-plugin`设置为`%somerpgcore_class%`。  然后，MythicLib将使用占位符输出作为玩家的当前职业名称。同样，如果你的RPG插件提供了`%somerpgcore_level%`占位符，你可以将其用于`level-plugin`。

> **警告**
>
> 请注意，用于提供玩家等级的占位符必须返回格式正确的整数，因为MythicLib会将其解析为整数。

### 配置 {#configuration}

MythicLib允许单独选择职业、等级和魔力插件。例如，你可以同时使用MMOCore中的职业、mcMMO 中的等级和Fabled中的魔力/耐力。你可以对等级、职业和/或魔力/耐力使用相同的插件。

要选择职业插件，请转到MythicLib`config.yml`并设置`class-plugin`选项。

```yml
# Plugin providing classes. This will propagate to MMOItems for
# item requirements and MMOInventory for class slot requirements.
#
# Supported Plugins:
# ...
class-plugin: MMOCORE
```

要选择关卡插件，请转到MythicLib`config.yml`并设置`level-plugin`选项。

```yml
# Plugin providing player levels. This will propagate to MMOItems
# for items requirements and MMOInventory for level slot requirements.
#
# Supported Plugins:
# ...
level-plugin: MMOCORE
```

## 标记插件 {#flag-plugins}

支持的标志插件：

- WorldGuard
- 居住地

以下是MMOCore和MMOItems的所有可用标志的完整列表。

|旗帜|描述 |默认 |
| --- | --- | --- |
| `MI_WEAPONS` | 禁用MMOItems武器 | Enabled |
| `MI_COMMANDS` | 禁用MMOItems命令 | Enabled |
| `MI_CONSUMABLES` | 禁用MI消耗品 | Enabled |
| `MI_TOOLS` | 禁用 MI 工具 | Enabled |
| `MMO_ABILITIES` | 禁用MMOCore/MI技能 | Enabled |
| `PVP_MODE` | 禁用PvP | Disabled |

## ~~双持插件~~ {#dual-wield-plugins}

~~MythicLib（因此MMOItems和MMOCore）具有与以下双持插件完全兼容（伤害计算和副手攻击效果应用程序）：~~

- ~~[双持](https://www.spigotmc.org/resources/dualwield.82349/)~~
- ~~[RealDualWield](https://www.spigotmc.org/resources/%E2%9C%85-real-dualwield-attack-with-both-hands-with-real-animation-without-mods.30816/)~~

## 全息图插件 {#hologram-plugins}

以下插件与MythicLib兼容，用于显示损坏和再生指示器等。请注意，通过在1.20.6中添加文本显示，MythicLib现在提供稳定的全息图lag-free基本实现。

- [全息显示器](https://dev.bukkit.org/projects/holographic-displays)
- [体面全息图](https://modrinth.com/plugin/decentholograms)
- [CMI](https://www.spigotmc.org/resources/3742/)
- [全息图](https://www.spigotmc.org/resources/trhologram-outdated.75503/)
- [全息图](https://www.spigotmc.org/resources/holograms.4924/)

---

原文：[🦾 Plugin Compatibility](https://docs.phoenixdevt.fr/mythiclib/features/compatibility) · 原文归档：2026-10-19
