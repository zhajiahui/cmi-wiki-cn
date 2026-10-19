---
title: "实体行为目标"
source_url: "https://wiki.itemsadder.com/adding-content/entities/entity-goals"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 实体行为目标

可以通过行为目标自定义实体的 AI。

### **注意**

`clear_all` 用于清除原版实体的全部基础行为目标。\
`replace_vanilla` 用于清除原版实体中所有同类基础行为目标。

### 示例

```yaml
entities:
  happy_creeper:
    model_folder: entity/happy_creeper
    type: ZOMBIE
    can_sun_burn: false
    eyes_height: 0.1
    goals:
      clear_all: true
      move_to_block:
        priority: 7
        blocks:
        - POPPY
      attack_near:
        priority: 8
        entity: CREEPER
      look_at_entity:
        priority: 8
        entity: PLAYER
      melee_attack:
        priority: 10
        enabled: true
      random_teleport_timed:
        min_delay: 60
        max_delay: 100
      random_teleport_on_hit:
        check_visibility: false
        chance: 100
      hurt_by_target:
        enabled: true
```
