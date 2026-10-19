---
title: "模板与变体"
source_url: "https://wiki.itemsadder.com/adding-content/items/item-properties/templates-and-variants"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 模板与变体

可参考[这个免费附加包](https://www.spigotmc.org/resources/furniture-more-furniture-for-itemsadder.93193/)中的示例。

## 什么是模板？

模板是不会出现在游戏中的特殊物品，用于保存其他物品需要继承的属性。\
将公共属性写在一个模板物品里，就能自动应用给其他物品，避免反复复制粘贴。

创建模板时，在物品中设置 `template: true`。

## 什么是变体？

变体会出现在游戏中，并继承模板物品的属性。

创建变体时，在物品中设置 `variant_of: template name`。

## 示例

例如，创建多件外观模型不同、其他属性相同的家具。

```yaml
  template_wood_park_bench:
    template: true  # <---- HERE you can see I set this item as "template"
    display_name: ""
    lore:
    - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: false
      model_path: item/oak_wood_park_bench
    behaviours:
      furniture:
        entity: armor_stand
        small: true
        solid: true
        fixed_rotation: true
        hitbox:
          length: 1
          width: 2
          height: 1
          width_offset: 0.5
        placeable_on:
          walls: false
          ceiling: false
          floor: true
      furniture_sit:
        sit_height: 0.5
        sit_all_solid_blocks: true
        
        
  oak_wood_park_bench:
    variant_of: template_wood_park_bench # <-- HERE I specify the template to inherit
    display_name: "Oak wood Park Bench"
    permission: oak_wood_park_bench
    lore:
    - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: false
      model_path: item/oak_wood_park_bench
      
      
  spruce_wood_park_bench:
    variant_of: template_wood_park_bench # <-- HERE I specify the template to inherit
    display_name: "Spruce wood Park Bench"
    permission: spruce_wood_park_bench
    lore:
    - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: false
      model_path: item/spruce_wood_park_bench
      
      
  birch_wood_park_bench:
    variant_of: template_wood_park_bench # <-- HERE I specify the template to inherit
    display_name: "Birch wood Park Bench"
    permission: birch_wood_park_bench
    lore:
    - 'lore-decorative-item'
    resource:
      material: PAPER
      generate: false
      model_path: item/birch_wood_park_bench
```
