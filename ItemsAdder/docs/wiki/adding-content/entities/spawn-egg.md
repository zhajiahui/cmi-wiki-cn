---
title: "刷怪蛋"
source_url: "https://wiki.itemsadder.com/adding-content/entities/spawn-egg"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 刷怪蛋

使用 `entity_summoner` 行为，可以为自定义实体创建刷怪蛋。

### 示例

```yaml
items:
  happy_creeper_spawn_egg:
    name: Happy Creeper Spawn Egg
    graphics:
      texture: item/happy_creeper_spawn_egg
    behaviours:
      entity_summoner:
        entity: happy_creeper
```

```yaml
items:
  happy_creeper_spawn_egg:
    name: Happy Creeper Spawn Egg
    resource:
      generate: true
      texture: item/happy_creeper_spawn_egg
      material: PAPER
    behaviours:
      entity_summoner:
        entity: happy_creeper
```
