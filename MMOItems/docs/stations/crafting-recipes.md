---
title: 合成配方
source: https://docs.phoenixdevt.fr/mmoitems/stations/crafting-recipes
source_snapshot: '2026-10-19'
---

# 合成配方 {#🥘-crafting-recipes}

合成站可以拥有无限数量的合成配方。每个配方在`recipes`配置部分下都有自己的配置小部分。你将用于小节名称的字符串键仅由MMOItems在内部使用，因此你可以使用任何内容，只要它是唯一的即可。它应该类似于`<item_type>_<item_id>_recipe`。

在本指南中，我们将为*钢剑*物品创建配方，满足以下要求

- 玩家至少为5等级
- 玩家需要特定的权限才能使用配方
- 配方需要1棍子和一些钢锭

## 配方输出 {#recipe-output}

你可以在此处定义使用配方时将给出的物品和玩家。配方输出位于输出`subsection`下。像往常一样，你需要提供物品类型和ID。使用以下语法将配方输出设置为MMOItems物品。

```yml
# crafting-stations/cs_example.yml

recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD,amount=1;display="Very Long Steel Sword!!"} # Recipe output
```

`amount`字段是可选的，如果你不提供任何字段，MMOItems将使用1。`display`也是可选的 - 如果提供，它将替换物品显示名称。

下表显示了你可以使用的所有可能的配方输出。

|输出类型 |格式|评论 |
| --- | --- | --- |
| 原版物品 | `vanilla{type=DIAMOND_HELMET}` | 原版物品 |
| MMO 项目 | `mmoitem{type=SWORD,id=KATANA,level=7-9}` | 你可以为所需的物品等级定义一个范围 |
| MythicMobs/坩埚 | `mythic{id=KingsCrown}` |  |
| Oraxen | `oraxen{id=SomeItemId}` |  |
| Nexo | `nexo{id=SomeItemId}` |  |
| ItemsAdder | `itemsadder{id=SomeItemId;display="Item Name"}` | 由于 IA 使用组件来显示名称，而MMOItems目前不支持它们，因此一些通过 IA 生成的物品显示没有名称。使用`display`选项覆盖物品显示名称。 |

## 制作时间 {#crafting-time}

配方有一个制作时间，即玩家制作物品所花费的时间（以秒为单位）。如果设置为零（默认值），则玩家将立即获得精心制作的物品。如果是non-zero，食材仍然会从玩家的物品栏中取走，而物品会被发送到*制作队列*，也就是车站 UI 底部的物品的那一行。从那里，玩家可以看到配方的进展。

单击制作队列中尚未完成的配方/物品将*取消*该配方：原料将返回到玩家。单击完整的配方/物品将为玩家提供配方输出。

```yml
recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD,amount=1}'
        crafting-time: 10 # time in seconds
```

## 使用/领取/取消配方时执行特定操作 {#perform-specific-actions-when-using-claiming-canceling-the-recipe}

请先阅读[此 wiki 页面](triggers.md)，了解如何制作触发器。使用触发器，你可以在与配方交互时执行特定操作。

设置这些触发器时，你可以收听三种类型的交互，以便修改配方的行为。如果你的配方不是即时的，则必须与其交互两次：首先单击配方时（其效果是消耗所有成分并将配方放入制作队列中一段时间 - 此交互称为`use`），然后在领取制作队列中的配方输出一次时（具有将配方输出提供给玩家的效果 - 称为`claim`） ）。`cancel`是指当点击制作队列中尚未完成的配方时（原料返回到玩家）。

```yml
recipes:
    steel-sword:
        output: 'mmoitems{type=SWORD,id=STEEL_SWORD,amount=1}
        crafting-time: 10 # time in seconds
        on-use: # Optional - called when USING the recipe
        - 'message{format="You are crafting a steel sword"}'
        - ...
        triggers: # Optional - called when obtaining the item
        - 'message{format="You just claimed a steel sword"}'
        - ...
        on-cancel: # Optional - called when CANCELING any craft from that recipe
        - 'message{format="You are no longer crafting a steel sword"}'
        - ...
```

请小心，不要将`triggers`选项误认为是`on-use`选项。有些配方有延迟，因此你在使用配方后不会立即获得物品，而是在 X 秒后获得。不过，即时配方会同时触发两个列表。

触发器可以与[配方条件](conditions.md)一起使用来处理虚构成分，例如货币。你可以有一些占位符条件，例如`%yourplugin_coins% >= 50`，它检查玩家是否至少具有50某种货币，并有一个触发器，当玩家使用配方时会调用该触发器，该配方将具有从玩家中取出50货币的效果。在这种情况下，如果玩家想要取消该飞船，你还必须退还他的钱。

这些触发器是完全可选的。如果你不想使用它们，请不要将任何内容添加到配方配置部分。你还可以使用`output-item: false`选项来阻止配方提供其输出物品（见下文）

## 额外选项 {#extra-options}

配方选项是你可以为每个配方设置的独特设置。

```yml
recipes:
    steel-sword:
        options:
            output-item: false
            hide-when-locked: false
            hide-when-no-ingredients: false
            silent-craft: true
```

| 选项 | 配置键 | 描述 |
| --- | --- | --- |
| 输出物品 | `output-item` | 如果输出物品将被赋予玩家。 |
| 锁定时隐藏 | `hide-when-locked` | 如果玩家不满足条件，则不会显示配方。 |
| 没有配料时隐藏 | `hide-when-no-ingredients` | 如果玩家没有配方的所有资源，则不会显示。 |
| 无声工艺 | `silent-craft` | 物品制作时不会发出任何噪音。 |

---

原文：[🥘 Crafting Recipes](https://docs.phoenixdevt.fr/mmoitems/stations/crafting-recipes) · 原文归档：2026-10-19
