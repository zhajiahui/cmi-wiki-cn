---
title: 概览
source: https://docs.phoenixdevt.fr/mmoinventory/api/overview
source_snapshot: '2026-10-19'
---

# 概览 {#🔌-overview}

确保安装了插件后，使用Bukkit的插件管理器访问`MMOInventory`插件单例实例。

```java
MMOInventory plugin = (MMOInventory) Bukkit.getPluginManager().getPlugin("MMOInventory");
```

## 物品栏 {#inventories}

每个物品栏都有一个`Inventory`实例存储在内存中。该抽象接口有两个实现，用于自定义物品栏的`CustomInventory`和用于原版物品栏的`VanillaInventory`。回想一下，最多可以注册一个原版物品栏。

`Inventory`实例包含有关物品栏的配置信息：物品及其内部的插槽、绑定到它们的命令、打开或关闭物品栏时的脚本...

首先，使用以下语法访问MMOInventory的物品栏管理器：

```java
MMOInventory plugin = /* see above */
InventoryManager inventories = plugin.getInventoryManager();
```

然后使用以下方法访问`Inventory`的实例：

```java
CustomInventory someCustomInv = inventories.getCustom("custom_inventory_id");
VanillaInventory theVanillaInv = inventories.getVanilla();

Collection<Inventory> all = inventories.getAll();
Collection<Inventory> customInvs = inventories.getAllCustom();
```

## 老虎机 {#slots}

`Inventory#getSlots`方法返回类`CustomSlot`实例的集合。自定义插槽对应于箱子 UI 中的插槽，其中玩家可以放置物品。

这些自定义插槽的主要功能是它们的限制列表（每个限制使用一个`SlotRestriction`对象）。`SlotRestriction`抽象接口有多种实现，例如安装MMOItems时的`LevelRestriction`或`TypeRestriction`。

## 注册新的限制类型 {#registering-new-restriction-types}

假设你有一个包含玩家数据的自定义插件，并且你希望将某些插槽限制为玩家，这些插槽在其玩家数据对象`SomePlayerData`中打开了特定的布尔标志。

首先，提供`SlotRestriction`的实现：

```java
public class MyRestriction extends SlotRestriction {
  public MyRestriction(MMOLineConfig config) {
    // No config options needed?
  }

  @Override
  public boolean isVerified(InventoryData player, CustomSlot ignore2, ItemStack ignore1) {
    // does not depend on the custom slot in which item is placed.
    // does not depend on the item placed either.

    SomePlayerData yourPlayerData = SomePlayerData.get(player.getPlayer());
    return yourPlayerData.canUseThisSlot();
  }
}
```

然后向MMOInventory的槽管理器注册此槽限制类型。我们将此限制称为`my_restriction`。

```java
MMOInventory plugin = /* see above */
InventoryManager inventories = plugin.getInventoryManager();
```

> **警告**
>
> 确保在MMOInventory加载之后、启用之前调用此代码。如果你将MMOInventory设为*（软）依赖*，则可以将其放入`#onLoad`中；如果将MMOInventory设为*loadbefore*，则可以将其放入`#onEnable`中。

然后，你可以在物品栏配置中使用此限制来创建仅在满足特定条件时才可用的插槽。这可以与其他现有限制相结合，为玩家创造有趣的福利。

```yml
slots:
  ...
  SPECIAL_RING_SLOT:
    type: accessory
    material: GOLD_NUGGET
    custom_model_data_string: "ring1"
    name: "&6Special Ring Slot"
    slot: 34
    restrictions:
      - "mmoitemstype{type=RING}"
      - "my_restriction{}" # <<==== HERE!
    lore:
      - 'Drag & drop an item to equip it.'
      - ''
      - 'This slot is only available after'
      - 'completing the quest XXXXX.'
```

## 玩家数据 {#player-data}

首先，使用以下语法访问玩家数据对象：

```java
Player yourPlayer = /* see above */
MMOInventory plugin = /* see above */
PlayerDataManager manager = plugin.getDataManager();

PlayerData playerData = manager.get(yourPlayer);
```

每个玩家都有一个存储在内存中的`PlayerData`对象，并且每个注册的物品栏都有一个`InventoryData`对象。`InventoryData`抽象接口针对自定义物品栏(`CustomInventoryData`) 和原版物品栏(`VanillaInventoryData`) 实现。

你可以通过以下方式获取`InventoryData`的实例：

```java
PlayerData playerData = /* see above */
CustomInventory customInv = /* see above */
Inventory someInv = /* see above */

VanillaInventoryData vanillaInvData = playerData.getVanilla();
CustomInventoryData customInvData = playerData.getCustom(customInv);
InventoryData invData = playerData.get(someInv); // either custom or vanilla
```

你可以通过以下方法获取玩家当前的物品装备列表。使用查找模式`NORMAL`将忽略已放置在无效物品栏插槽中的物品。使用查找模式`IGNORE_RESTRICTIONS`将返回所有物品，包括玩家的原版物品栏中存在的物品。

```java
List<InventoryItem> items = playerData.getItems(InventoryLookupMode.NORMAL);
```

`InventoryData`抽象接口主要公开了两个用于获取和更新物品栏内容的重要方法。请注意，对`#setItem`的调用会触发`InventoryUpdateEvent`。

```java
InventoryData invData = /* see above */
CustomSlot someSlot = /* ... */

invData.setItem(someSlot, new ItemStack(Material.DIAMOND_SWORD));
invData.setItem(someSlot, null); // remove item

Collection<InventoryItem> content = invData.retrieveItems();
```

类`InventoryItem`存储有关物品及其在物品栏中的位置的信息。

---

原文：[🔌 Overview](https://docs.phoenixdevt.fr/mmoinventory/api/overview) · 原文归档：2026-10-19
