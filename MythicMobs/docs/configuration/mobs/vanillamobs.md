---
title: mobs/VanillaMobs.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: mobs/VanillaMobs.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# mobs/VanillaMobs.yml

文件：`mobs/VanillaMobs.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包示例配置。

## `CAVE_SPIDER` { #cave_spider }

```yaml title="mobs/VanillaMobs.yml · CAVE_SPIDER"
# 更多信息请查看插件手册，或加入 Discord：
# http://www.mythicmobs.net
#  

CAVE_SPIDER:
  Health: 30
  Damage: 7
```

## `WITHER_SKELETON` { #wither_skeleton }

```yaml title="mobs/VanillaMobs.yml · WITHER_SKELETON"
WITHER_SKELETON:
  Health: 50
  Damage: 10
```

## `GIANT` { #giant }

```yaml title="mobs/VanillaMobs.yml · GIANT"
GIANT:
  Health: 1000
  Damage: 20
  Skills:
  - potion{type=POISON;duration=100;lvl=1} @target ~onAttack
```
