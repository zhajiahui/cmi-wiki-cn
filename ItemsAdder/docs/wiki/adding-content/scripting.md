---
title: "脚本"
source_url: "https://wiki.itemsadder.com/adding-content/scripting"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 脚本

### 需要 ItemsAdder 4.0.10 或更高版本

此功能仍在开发中，后续改动可能影响已有配置和脚本。虽然会尽量保持兼容，部分变化仍难以避免。

ItemsAdder 的脚本功能允许定义超出内置事件和动作范围的高级物品行为，用于创建动态、复杂的功能。

***

### 🧫 概述

脚本引擎底层使用 Java 或类似 Java 的语言（JSPP）。

> 📝 **注意**：ItemsAdder 脚本会编译为 Java 代码，性能与服务端原生代码相当。与 Skript 等解释型语言不同，它没有运行时解释开销。

#### ↺ 支持的事件

脚本支持以下事件，由物品中的 `events` 属性触发。

* `BlockBreakEvent`
* `CustomBlockBreakEventInternal`
* `PlayerInteractEvent`
* `EntityDamageByEntityEvent`
* `EntityDeathEvent`
* `PlayerInteractEntityEvent`
* `PlayerDropItemEvent`
* `PlayerDropHeldItemEvent`
* `EntityShootBowEvent`
* `EntityShootBowArrowEvent`
* `PlayerItemConsumeEvent`
* `FoodLevelChangeEvent`
* `PlayerEditBookEvent`
* `PlayerFishEvent`
* `InventoryClickEvent`
* `ProjectileLaunchEvent`
* `ProjectileHitEvent`
* `PlayerItemHeldEvent`
* `InventoryDragEvent`
* `PlayerPickupItemEvent`
* `PlayerBucketEmptyEvent`
* `PlayerBucketFillEvent`
* `ArmorEquipEvent`
* `PlayerItemBreakEvent`
* `PlayerSwapHandItemsEvent`
* `PlayerEvent`
