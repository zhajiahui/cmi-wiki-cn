---
title: 原版物品栏
source: https://docs.phoenixdevt.fr/mmoinventory/features/vanilla-inventory
source_snapshot: '2026-10-19'
---

# 原版物品栏 {#🎒-vanilla-inventory}

玩家的原版物品栏可以直接用来放置配件槽和按钮。此功能完全兼容使用零个、一个或多个[定制物品栏](custom-inventory.md)。

![](../assets/c0665289a26e-vanilla_inventory.COYiXQnH.png)

## 配置 {#configuration}

关闭`enabled`选项，或完全删除`vanilla_inventory.yml`配置文件以禁用玩家的原版物品栏。默认情况下它是禁用的，因此如果你不打算使用它，实际上不需要执行任何操作。

```yml
# For the vanilla inventory, this option is not very important,
# it only has to be different from other inventories
id: vanilla_inventory

# Will place items in the player's vanilla 3x9 inventory grid
# Either 'vanilla' or 'custom'
type: vanilla

# Toggle on/off for temporary disabling this inventory.
# Vanilla inventory is disabled by default.
enabled: false
```

> **警告**
>
> 确保将`type`选项设置为`vanilla`。另请确保你只有一个物品栏配置，并将`type`选项设置为`vanilla`。

## 物品插槽 {#item-slots}

你在`slots`配置节文件中配置的任何插槽都将出现在原版玩家的物品栏中。它的工作原理与物品栏GUI相同：玩家可以将物品拖放到自定义插槽上以装备物品。插槽物品出现在玩家登录时，因此请确保在编辑插槽配置后重新启动服务器。

> **信息**
>
> 请注意，你不能在原版物品栏中使用原版插槽类型，例如`helmet`或`off_hand`，因为它们已经存在。

如果玩家连接并且它们已经碰巧将物品放置在原版物品栏中，并且MMOInventory尝试将插槽物品放在那里，它会首先尝试将物品移动到其他地方。玩家的物品不会丢失。

---

原文：[🎒 Vanilla Inventory](https://docs.phoenixdevt.fr/mmoinventory/features/vanilla-inventory) · 原文归档：2026-10-19
