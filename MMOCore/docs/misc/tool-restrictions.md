---
title: 工具限制
source: https://docs.phoenixdevt.fr/mmocore/misc/tool-restrictions
source_snapshot: '2026-10-19'
---

# 工具限制 {#⚒️-tool-restrictions}

此功能允许你定义每种类型的工具可以挖掘哪些块。当与MMOCore[挖矿和区块再生](../features/mining.md)功能一起使用时，它对于进一步自定义和平衡你的工具非常有用。此功能的配置文件是`restrictions.yml`。

## 配置 {#configuration}

默认情况下，该配置仅设置用于采矿，并且包含所有镐。你**可以**将轴、铲子甚至其他材料（不仅仅是工具）添加到此列表中，并给予它们自己的限制。

<details markdown="1">

<summary>默认配置</summary>

```yml
# The corresponding tool. It's CASE_SENSITIVE!
WOODEN_PICKAXE:
    parent: AIR

    # What the tool can mine.
    can-mine:
    - vanilla{type=COAL_ORE}

# You can also use MMOItems specifically TYPE?ID
TOOL?STONE_PICKAXE:

    # What the tool can mine.
    can-mine:
    - vanilla{type=COAL_ORE}

STONE_PICKAXE:
    can-mine:
    - vanilla{type=IRON_ORE}
    # MMOItems custom blocks with ID 1
    - mmoitems{id=1}
    
    # The block break permissions the tool inherits.
    # e.g a stone pickaxe can mine iron ores PLUS
    # any block that the wooden pickaxe can mine.
    # Used to make the config much clearer.
    parent: WOODEN_PICKAXE

IRON_PICKAXE:
    parent: STONE_PICKAXE
    can-mine:
    - vanilla{type=GOLD_ORE}
    # Custom skull with diamond ore texture
    - skull{value="eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2EzYmI4NWRlYzEzMjlmZTgyOWNjNmNkY2QzNGUxYmQ2MGVlODMyZjU3MjYyOTY1MWYxNGI1ZTE0NTU1ZGJiMSJ9fX0="}

GOLDEN_PICKAXE:
    parent: IRON_PICKAXE
    can-mine:
    - vanilla{type=LAPIS_ORE}

DIAMOND_PICKAXE:
    parent: GOLDEN_PICKAXE
    can-mine:
    - vanilla{type=DIAMOND_ORE}
    - vanilla{type=EMERALD_ORE}
    - vanilla{type=REDSTONE_ORE}

# Default permission set
AIR:
    default: true
    can-mine:
    - vanilla{type=OAK_LOG}
    - vanilla{type=SPRUCE_LOG}
```

</details>

选项也非常简单。首先选择工具，然后指定该工具可以破坏的所有块类型](../features/mining.md#target-block)的列表。此功能的工作原理类似于白名单：任何不在列表中的块都不能被给定的工具破坏。为了获得额外的兼容性，我们将块分解为块类型，例如原版块、MMOItems块，甚至定制头骨！

```yml
IRON_AXE:
    default: true
    can-mine:
    - vanilla{type=OAK_LOG}
    - vanilla{type=SPRUCE_LOG}
```

## 默认设置权限 {#default-permission-set}

`default`选项可用于设置默认中断权限。如果玩家碰巧拥有一个在此配置文件中没有设置的物品，则默认情况下将使用此权限设置。仅使用`AIR`作为默认值是有意义的，因为这是任何玩家在不持有特殊工具时都可以挖掘的内容。

## MMOItems {#mmoitems}

要将区块挖掘权限提供给MMOItems工具，请使用`ITEM_TYPE?ITEM_ID`语法。以下是物品的示例，类型为`TOOL`和ID`STEEL_PICKAXE`。

```yml
'TOOL?STEEL_PICKAXE':
    parent: IRON_PICKAXE
    can-mine:
    - 'vanilla{type=EMERALD_ORE}'
```

## 继承 {#inheritance}

当你的工具分层并且你希望更强大的工具自动继承其下工具的所有块时，请使用`parent`选项。这是一个非常方便的组织功能。如果将其留空，它将自动将`default`权限设置为父级。

```yml
TOOL?DIAMOND_PICKAXE:
    parent: DIAMOND_PICKAXE
    can-mine:
    - ...
```

---

原文：[⚒️ Tool Restrictions](https://docs.phoenixdevt.fr/mmocore/misc/tool-restrictions) · 原文归档：2026-10-19
