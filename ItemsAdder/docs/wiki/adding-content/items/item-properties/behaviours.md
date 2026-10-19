---
title: "行为"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/behaviours"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 行为

## 什么是行为？

可通过[官方编辑器](../../../plugin-usage/beginners/files-editor.md)查看可用行为列表。

行为是一组插件**预先实现**的动作，用于提供**非原版**功能。\
这些**行为**已内置于插件，可以直接为物品添加对应功能。

## 示例

```yaml
# This behaviour allows you to open a trade GUI with the following items
# For example black_fishing_rod and red_fishing_rod
block_trade_machine:
  title: "Your title"
  permission: "mypermission.trade.example" # <--- this is optional
  gui_texture: ###THIS IS OPTIONAL, use it only to retexture the GUI
    left: customization_table_left
    right: customization_table_right
  trades_list:
    black_fishing_rod:
      ingredients:
        slot1:
          item: FISHING_ROD
          amount: 1
        slot2:
          item: BLACK_DYE
          amount: 1
      result:
        item: black_fishing_rod
        amount: 1
    red_fishing_rod:
      ingredients:
        slot1:
          item: FISHING_ROD
          amount: 1
        slot2:
          item: RED_DYE
          amount: 1
      result:
        item: red_fishing_rod
        amount: 1
        
furniture_trade_machine:
# ....... it's the same as block_trade_machine

   
# When you rightclick with that item it will be placed on the ground with an
# armorstand. The armorstand will have the item as helmet and will be invisible.
furniture:
  entity: armor_stand # you can also use item_frame (works better on 1.16+)
  small: true
  gravity: true
  fixed_rotation: false
  light_level: 7  
  solid: false
  opposite_direction: false #makes the model rotate 180 when placed
  hitbox:
    length: 2
    width: 2.3
    height: 1
    length_offset: 0.5
    width_offset: 0.5
    height_offset: 0.5
  placeable_on:
    walls: false
    ceiling: false
    floor: true

# If you add this behaviour and "furniture" behaviour you will be able to sit
# on the furniture at the defined height.
furniture_sit:
  sit_height: 0.9
  opposite_direction: true #default is true
  # Sit on every BARRIER block of the furniture (for multi-seats chairs)
  sit_all_solid_blocks: false
  

# Allows you to use this item as a gun. You can decide which projectile must
# be hold on left hand in order to shot.
gun:
  projectile: itemsadder:clip
  

# Allows you to use the current item as hat (same vanilla helmet behaviour)
hat: true

# Allows you to make the item stay in player inventory on death
keep_on_death: true

# Allows you to use the current item as a vanilla music disc.
# Remember that you will have to create a custom sound to be able
# to play something.
music_disc:
  song:
    name: "itemsadder:music_disc.cdk_sunday"
    description: "Cdk - Sunday"
    

# Allows you to use the current item as a ridable vehicle
vehicle:
  fixed_rotation: false
  small: true
  sit_height: 0
  step_height: 0.1
  hitbox:
    length: 2
    width: 1.7
    height: 1
  speed:
    drive: 1
    jump: 0.3
    fly: 0
  fuel:
    start: 150
    max: 300
    items:
      COAL: 1
      CHARCOAL: 1
      COAL_BLOCK: 9
      "itemsadder:banana": 1
  smoke:
    amount: 2
    offset:
      x: 0
      y: 0
      z: -0.8
```
