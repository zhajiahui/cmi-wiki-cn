---
title: 插件 API
source: https://docs.phoenixdevt.fr/mmoitems/api/main
source_snapshot: '2026-10-19'
---

# 插件 API {#🔧-plugin-api}

> **警告**
>
> MI7 中可能会有较大改动。

如果你需要有关MMOItemsAPI的更多信息，请加入Discord支持频道。提问请使用`#developers`频道！

## 检查 ItemStack 是否来自 MI {#checking-if-an-itemstack-is-from-mi}

首先，使用`NBTItem.get(ItemStack)`获取 ItemStack 的 NBTItem 。此类可让你轻松地从物品操作 NBTTag（1.14有一个新的API，它允许你使用 ItemMeta 执行此操作，但对于 <1.14支持，MI 使用NMS代码处理 NBT）。使用`nbtItem.hasType()`来查看 NBTItem 是否可以找到与MMOItems类型对应的标签。该方法主要检查插件是否来自 MI。

你可以使用`nbtItem.getType()`获取物品类型。此方法通过所有插件物品类型调用地图检查，因此将其结果保存在字段中以保存计算。

## 检查 MI物品是否为特定物品 {#checking-if-an-mi-item-is-a-specific-item}

再次，使用`NBTItem.get(ItemStack)`获取 ItemStack 的 NBTItem 。然后，你可以轻松运行`nbtItem.hasType()`来检查它是否是 MMOItem，然后运行 ​​`nbtItem.getType()`和`nbtItem.getString("MMOITEMS_ITEM_ID")`来获取所述物品的ID。你可以将类型和ID与你需要的任何内容进行比较，以检查物品是否是特定的。

## 生成物品 {#generating-an-item}

自6.0起，所有物品现在都是 *物品模板*。你可以使用以下方法之一从模板构建`MMOItem`的实例：

```java
itemTemplate.newBuilder(RPGPlayer).build()
itemTemplate.newBuilder(level, tier).build()
```

可以使用`MMOItems.plugin.getTemplates.getTemplate(type, id)`从插件`TemplateManager`检索模板。通过使用`MMOItem#newBuilder()`方法，你可以创建一个`MMOItemBuilder`，它可以从`MMOItem`构建 ItemStack 实例。

```java
MMOItem mmoitem = MMOItems.plugin.getMMOItem(MMOItems.plugin.getTypes().get("SWORD"), "CUTLASS");
ItemStack item = mmoitem.newBuilder().build();
```

确保你不要使用相同的`MMOItemBuilder`两次来使用`build()`方法构建`ItemStack`。该方法对大量物品数据进行打乱，因此不能重复使用。但是，你可以使用相同的`MMOItem`实例来生成任意数量的`MMOItemBuilder`实例。

以下方法直接返回 ItemStack 实例：

```java
MMOItems.plugin.getItem(MMOItems.plugin.getTypes().get("SWORD"), "CUTLASS")
```

但请注意，使用此方法将返回未按玩家等级缩放且没有随机层的物品。如果你想获得经过缩放且具有随机层的物品，请使用：

```java
MMOItems.plugin.getItem(type, id, level, tier) // fixed level and tier
MMOItems.plugin.getItem(type, id, playerdata) // scale on player data
```

## 正在检索物品品质 {#retrieving-item-tiers}

你可以通过从插件中检索`TierManager`类来获取物品品质。

```java
TierManager tiers = MMOItems.plugin.getTiers();
boolean exists = tiers.has("RARE");
ItemTier rare = tiers.get("RARE");
Collection<ItemTier> all = tiers.getAll();
```

## 检索物品类型实例 {#retrieving-item-type-instances}

从4.6开始，类型不再存储在枚举中，因为你可以添加任意数量的类型。类型实例现在存储在`TypeManager`类实例中，可以使用以下方法访问该实例：

```java
TypeManager types = MMOItems.plugin.getTypes();
boolean exists = types.has("SWORD");
Type sword = types.get("SWORD"); // e.g get the type which ID is SWORD
Collection<Type> all = types.getAll(); // get all loaded types
```

## 打开插件 GUI {#opening-plugin-guis}

```java
new AdvancedTypeList(player, 1).open(); // opens the recipe list at type selection
new AdvancedRecipeList(player, MMOItems.plugin.getTypes().get("SWORD")).open(); // opens the recipe list (after selecting item type)
new AdvancedRecipeWorkbench(player).open(); // opens the advanced workbench
new ItemEdition(player, MMOItems.plugin.getTypes().get("STAFF"), "EARTH_STAFF").open(); // opens the edition gui for a specific item
```

## 检查GUI是否来自 MI {#checking-if-a-gui-is-from-mi}

MMOItems中的每个GUI都是使用扩展`PluginInventory`的定制物品栏支架创建的。要检查GUI是否是 MI 的GUI，只需检索物品栏持有者并检查它是否是该类的实例：

```java
boolean isMMOItemsUi = inventory.getHolder() instanceof PluginInventory
```

---

原文：[🔧 Plugin API](https://docs.phoenixdevt.fr/mmoitems/api/main) · 原文归档：2026-10-19
