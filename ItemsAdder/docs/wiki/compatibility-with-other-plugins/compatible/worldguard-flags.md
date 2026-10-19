---
title: "WorldGuard"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/worldguard-flags"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# WorldGuard

## 标记列表

### ia-furniture-sit

此标志控制玩家是否可以坐在家具上（具有 `furniture_sit` [行为](../../adding-content/items/item-properties/behaviours.md)的家具）

### ia-campfire-item-add

允许玩家将物品移至营火

### ia-campfire-item-remove

允许玩家将物品从营火移除

### ia-vehicle-place

允许玩家在该区域放置车辆

### ia-vehicle-remove

允许玩家在区域中移除任意载具

### ia-vehicle-personal-remove

仅允许玩家在区域中移除自己的载具

### ia-vehicle-sit

允许玩家在区域中乘坐任意载具

### ia-vehicle-personal-sit

仅允许玩家在区域中乘坐自己的载具

### ia-trade-machine-use

允许玩家使用交易机器

### ia-placed-block-interact

允许玩家触发 placed\_block.interact 事件

### ia-placed-armorstand-interact

允许玩家触发 placed\_armorstand.interact 事件

将 **ia-vehicle-sit** 设为 Deny，并将 **ia-vehicle-personal-sit** 设为 Allow，使玩家只能乘坐自己的载具

## 常见问题

如果你设置了正确的标记，玩家仍 **无法坐到家具上**：

* 检查是否将 `__global__ region` 用作主区域（即设置家具标志的区域）。如果是，请创建新区域。全局区域与部分插件的标志存在已知兼容问题。
* 检查你是否设置了 `build` 或 `passthrough` 标记。\
  这些标记不能进行改动，你需要保持为默认值（未选择状态，灰色文本）
