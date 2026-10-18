---
title: 事件
source: https://docs.phoenixdevt.fr/mmoinventory/api/events
source_snapshot: '2026-10-19'
---

# 事件 {#📮-events}

本页介绍了MMOInventory触发的Bukkit事件。

## `InventoryUpdateEvent` {#inventoryupdateevent}

每次物品栏内容更改时都会调用此事件。`#getPreviousItem`返回前一个物品，如果没有，则返回`null`。`#getNewItem`返回正在“装备”的物品，如果正在移除，则返回`null`。`#getInventoryData`返回玩家的物品栏数据。`#getSlot`返回单击的插槽。

此活动无法取消。它特别用于将物品栏更新广播到MMOItems。

## `ItemEquipEvent` {#itemequipevent}

这是`InventoryUpdateEvent`的可取消对应项。仅当玩家从箱子物品栏内部点击时才会调用。请注意，当玩家与其原版物品栏内的自定义插槽交互时也会调用此事件。

请注意，在单击时编辑物品并非易事，因为它可能会导致与MMOItems物品栏更新不一致的行为。以下是一些解决方案：

- 要么侦听之前的事件之一，然后安排一个任务以使用`InventoryData#setItem`在下一个刻上编辑它，
- 或者通过设置物品类型和物品元来*就地*编辑装备的物品。请注意，MMOItems有时会针对“就地”耐久度损失和物品降级等功能执行此操作。之后你需要再次从物品栏解析MMOItems修饰符。

---

原文：[📮 Events](https://docs.phoenixdevt.fr/mmoinventory/api/events) · 原文归档：2026-10-19
