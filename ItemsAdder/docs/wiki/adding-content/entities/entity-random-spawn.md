---
title: "实体随机生成"
source_url: "https://wiki.itemsadder.com/adding-content/entities/entity-random-spawn"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 实体随机生成

### 需要 ItemsAdder 4.0.11 或更高版本！

可以让自定义实体像原版生物一样，在世界中随机生成。

以下示例让 `red_zombie` 生成。

原版僵尸生成时，只有 `20%` 的概率生成此实体，并用自定义实体替换原版僵尸。

仅在名称以 `world` 开头的世界中，于高度 `0` 到 `150`、天气为 `RAIN`、亮度为 `0` 到 `10` 时生成。

```yaml
info:
  namespace: test
entities:
  red_zombie:
    model_folder: entity/red_zombie
    can_sun_burn: false
    type: ZOMBIE
entities_populators:
  red_zombie_1:
    entity: test:red_zombie
    spawn_logic:
      method: REPLACE # or SPAWN_NEAR
      types:
      - ZOMBIE
    chance: 20.0
    amount: 1
    worlds:
    - world*
    # you can also use x and z as location_range parameters, for example
    # to make edge of the worlds harder with more dangerous mobs
    location_range:
      y:
        min: 0
        max: 150
    weather:
    - RAIN
    light_level:
      min: 0
      max: 10

```

## 全部属性

```yaml
entities_populators:
  red_zombie:
    entity: test:red_zombie
    # This sets how to actually spawn the entity. 
    # You can replace a vanilla mob when it's spawned or spawn your mob near it.
    # Note: This uses the Minecraft spawn logic, so gemerule `doMobSpawning false` 
    # will make this stop working.
    spawn_logic:
      method: REPLACE # or SPAWN_NEAR
      types:
      - ZOMBIE
    chance: 20.0
    amount: 1
    # Optional
    biomes:
    - FOREST
    - JUNGLE
    worlds:
    - world
    - "!banned_other_world"
    - "test_world_*"
    # you can also use x and z as location_range parameters, for example
    # to make edge of the worlds harder with more dangerous mobs
    # Optional
    location_range:
      y:
        min: 25
        max: 45
    # Optional
    weather:
    - CLEAR
    - RAIN
    - THUNDER
    - SNOW
    # you can create more intervals, this is useful 
    # to introduce dynamicity to your gameplay
    # Optional
    time:
      interval_1:
        min: 12000 # sunset. also supports the 'sunset' word directly
        max: 23000 # sunrise. also supports the 'sunrise' word directly
    # Optional
    light_level:
      min: 0
      max: 5
```

## 示例内容包


