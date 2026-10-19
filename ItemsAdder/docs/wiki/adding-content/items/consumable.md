---
title: "消耗品"
source_url: "https://wiki.itemsadder.com/adding-content/items/consumable"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 消耗品

**食物**

```yaml
info:
  namespace: my_items
items:
  my_food:
    name: My Food
    graphics:
      texture: item/my_food
    consumable:
      nutrition: 7
      saturation: 4
```

**饮品**

```yaml
info:
  namespace: my_items
items:
  my_drink:
    name: My Drink
    graphics:
      texture: item/my_drink
    consumable:
      nutrition: 1
      animation: drink
```

**食物**

```yaml
info:
  namespace: my_items
items:
  my_food:
    enabled: true
    display_name: My Food
    resource:
      material: COOKED_PORKCHOP
      generate: true
      textures:
        - item/my_food
    events:
      eat:
        feed:
          amount: 7
          saturation: 4
```

**饮品**

```yaml
info:
  namespace: my_items
items:
  my_drink:
    enabled: true
    display_name: My Drink
    resource:
      material: POTION
      generate: true
      textures:
        - item/my_drink
    specific_properties:
      potion:
        type: WATER
        color: WHITE
    item_flags:
      - HIDE_POTION_EFFECTS
    events:
      drink:
        feed:
          amount: 1
          saturation: 0
```
