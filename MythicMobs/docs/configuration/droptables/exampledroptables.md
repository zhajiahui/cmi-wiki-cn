---
title: droptables/ExampleDropTables.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: droptables/ExampleDropTables.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# droptables/ExampleDropTables.yml

文件：`droptables/ExampleDropTables.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包示例配置。

## `SkeletonKingDrops` { #skeletonkingdrops }

```yaml title="droptables/ExampleDropTables.yml · SkeletonKingDrops"
# 更多信息请查看插件手册，或加入 Discord：
# http://www.mythicmobs.net
#  

SkeletonKingDrops:
  Conditions:
  - playerwithin{d=40}
  Drops:
  - SkeletonKingItemDrops 1
  - experience 100
  - heroesexp 200
```

## `SkeletonKingItemDrops` { #skeletonkingitemdrops }

```yaml title="droptables/ExampleDropTables.yml · SkeletonKingItemDrops"
SkeletonKingItemDrops:
  MinItems: 1
  MaxItems: 2
  Drops:
  - KingsCrown 1 0.01
  - SkeletonKingSword 0.1
  - GOLD_NUGGET 32-64 1
  - DIAMOND 1-12 0.8
```
