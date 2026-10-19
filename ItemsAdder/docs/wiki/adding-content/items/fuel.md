---
title: "燃料"
source_url: "https://wiki.itemsadder.com/adding-content/items/fuel"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 燃料

## 创建物品

必须选择原版 Minecraft 已支持作为燃料燃烧的材质，否则不会生效。\
例如：`STICK`、`COAL`、`CHARCOAL` 等。

例如，以下配置让该物品可在**高炉（BLAST\_FURNACE）**中作为燃料，燃烧 **20 tick（1 秒）**。

```yaml
  magic_fuel:
    display_name: Fuel
    material: COAL
    graphics:
      texture: item/diamond
    behaviours:
      fuel: 
        burn_ticks: 20
        machines:
          - BLAST_FURNACE
```

```yaml
  magic_fuel:
    display_name: Fuel
    resource:
      material: COAL
      generate: true
      textures:
      - item/diamond
    behaviours:
      fuel: 
        burn_ticks: 20
        machines:
          - BLAST_FURNACE
```
