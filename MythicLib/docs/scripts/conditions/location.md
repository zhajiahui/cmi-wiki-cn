---
title: 位置条件
source: https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/location
source_snapshot: '2026-10-19'
---

# 位置条件 {#location}

> **警告**
>
> 建设中

## 检查目标脚本位置生物群系 {#check-for-the-target-script-location-biome}

检查脚本目标位置（或当`source`设置为true时的源位置）生物群落是否是特定生物群落。生物群系列表[此处为](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)。你可以使用多个生物群系名称，并使用`,`将它们分开。警告，生物群落名称高度区分大小写。

```
example_condition:
    type: biome
    name: 'BIRCH_FOREST,DEEP_COLD_OCEAN,END_HIGHLANDS'
    source: false
```

## 检查某个位置是否在块边界内 {#checking-if-some-location-is-within-block-boundaries}

检查脚本的目标位置（或源位置，如果`source`设置为true）是否位于由其他两个位置`loc1`和`loc2`定义的边界内。这些位置必须使用位置目标选择器提供。

```
example_condition:
    type: cuboid
    loc1: # Location targeter needed here
        type: custom
        x: 10
        y: 67
        z: -250
    loc2: # Location targeter needed here
        type: custom
        x: 15
        y: 72
        z: -246
    source: false
```

## 检查脚本目标位置是否靠近另一个位置 {#check-if-script-target-location-is-close-to-another-location}

检查脚本目标位置（或源位置，如果`source`设置为true）距中心位置是否小于 X 个街区。

```
example_condition:
    type: distance
    location: # Location targeter needed here
        type: target_location
    max: '10' # 10 blocks away max
    source: false
```

## 检查脚本世界 {#check-for-the-script-world}

检查脚本是否在特定世界中运行。你可以使用多个世界名称，并使用`,`将它们分开。警告，世界名称高度区分大小写。

```
example_condition:
    type: world
    name: 'world_the_end'
```

---

原文：[Location](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/location) · 原文归档：2026-10-19
