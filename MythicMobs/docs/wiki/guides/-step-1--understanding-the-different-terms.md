---
title: （步骤 1）理解各个术语
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/%28Step-1%29-Understanding-the-different-terms
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# （步骤 1）理解各个术语 {#step-1-understanding-the-different-terms}

MythicMobs 包含许多不同的功能和术语，了解它们十分重要。本页简要介绍了编写生物时可能遇到的各种内容。

## 生物 {#mobs}

[生物 Wiki](../mobs/mobs.md)

正如插件名称所示，生物是 MythicMobs 最重要的核心组成部分。

### 选项 {#options}

[生物选项 Wiki](../mobs/options.md)

生物选项可以修改生物的各种设置。并非所有生物都支持全部选项，请查看 Wiki 页面，确认不同生物类型可以使用哪些选项。

### 自定义 AI {#custom-ai}

[自定义 AI Wiki](../mobs/custom-ai.md)

自定义 AI 可以改变生物的默认行为，让它选择不同的目标，并以不同方式对待目标。自定义 AI 由 2 类选择器组成：行为目标和攻击目标。

行为目标（Goals）：决定生物做什么，例如逃离玩家、浮在水中或攻击。

攻击目标（Targets）：决定生物以谁或什么为目标，例如玩家或其他生物。

## 技能机制 {#mechanics}

[机制 Wiki](../skills/mechanics.md)

机制是为你创建的生物添加有趣而独特能力的主要方式。最基本的用法是在生物的 Skills 部分加入机制，并配上触发器和目标选择器；也可以将机制写入元技能。大多数机制都有一组可用的属性，可以用来调整其行为。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

## 目标选择器 {#targeters}

[目标选择器 Wiki](../skills/targeters.md)

目标选择器决定机制作用于谁。例如，使用 giveitem 机制时，目标选择器会决定将物品交给谁。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

## 触发器 {#triggers}

[触发器 Wiki](../skills/triggers.md)

触发器决定生物何时激活机制和能力。触发器必须以 `~` 开头，放在目标选择器之后。它们只能直接写在生物配置中，写在元技能中不会生效。在这个示例中，`~onTimer:20` 是触发器，表示每 20 刻（1 秒）运行一次机制。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

## 条件 {#conditions}

[条件 Wiki](../skills/conditions.md)

条件可以限制各项内容的执行方式。使用条件时，可以写成行内条件，也可以写在条件部分。

## 属性 {#attributes}

属性是传递给机制、目标选择器或条件的信息，用于自定义其行为。在这个示例中，`cd=10` 和 `i=DIAMOND` 是属性，分别指定冷却时间为 10 秒，以及要给予的物品。属性之间用 `;` 分隔，所设值之前必须有 `=`。

`- giveitem{i=DIAMOND;cd=10} @NearestPlayer ~onTimer:20`

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| attribute1 | alias1, alias2 | 各参数作用的说明 | 默认值 |
| attribute2 | alias3 | 各参数作用的说明 | 默认值 |
| attribute3 |  | 各参数作用的说明 | 默认值 |

这表示该机制有 3 个不同的属性：`attribute1`、`attribute2` 和 `attribute2`。每个属性都有相应的作用说明，以及未显式指定时采用的“默认值”。有些属性还有“别名”，即可以用来设置同一属性的其他名称。

> 此机制继承 [Damage](../skills/mechanics/damage.md) 机制的所有*可继承*属性。

这意味着，除了当前 Wiki 页面列出的属性，还可以使用所指机制中未标记为“不可继承”的属性。例如，此处作为示例的 Damage 机制只有一个不可继承的属性（`amount`），其他属性都可以使用。

## MetaSkills {#metaskills}

[元技能 Wiki](../skills/metaskills.md)

技能是 MythicMobs 的基础功能。它允许你将多个机制组合在一起，创建具有多种效果和视觉表现的有趣攻击或功能。

## 物品 {#items}

[物品 Wiki](../items/items.md)

MythicMobs 可以创建基本的自定义物品，供生物使用或给予玩家。如果安装了 [MythicCrucible](https://mythiccraft.io/index.php?resources/crucible-custom-items-armor-furniture-blocks-more.2/) 附属插件，还可以进一步扩展这些物品。

## RandomSpawns {#randomspawns}

[随机生成 Wiki](../random-spawns.md)

随机生成可以让生物在世界中自然生成，无需使用命令或刷怪点。可以添加条件来决定它们何时生成。

## 刷怪点 {#spawners}

[刷怪点 Wiki](../spawners.md)

刷怪点可以在固定位置定期生成生物，适用于副本或 RPG 地图。

请注意：服务器运行时无法编辑刷怪点文件，必须先关闭服务器再编辑。你也可以改用游戏内命令。

## 变量 {#variables}

[变量 Wiki](../skills/variables.md)

变量是一套便捷的信息存储系统。存储的信息可以用于其他各种位置，例如机制和条件中的占位符。

## 占位符 {#placeholders}

[占位符 Wiki](../skills/placeholders.md)

占位符用于显示或获取实体、位置或元技能中的信息。例如，`<caster.hp>` 占位符可以获取施法实体的生命值。

**[>> 第 2 步](-step-2--files-and-directories.md)**
