---
title: randomspawns/ExampleRandomSpawns.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: randomspawns/ExampleRandomSpawns.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# randomspawns/ExampleRandomSpawns.yml

文件：`randomspawns/ExampleRandomSpawns.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包示例配置。

## `RandomSkeletonKing` { #randomskeletonking }

```yaml title="randomspawns/ExampleRandomSpawns.yml · RandomSkeletonKing"
# 更多信息请查看插件手册，或加入 Discord：
# http://www.mythicmobs.net
#  

#
# 每只在室外生成的生物都有 0.1% 的概率
# 被替换为骷髅王
# 
RandomSkeletonKing:
  Type: SkeletonKing
  Worlds: world
  Chance: 0.001
  Priority: 1
  Action: REPLACE
  Conditions:
  - outside true
```

## `RandomSkeletalKnight` { #randomskeletalknight }

```yaml title="randomspawns/ExampleRandomSpawns.yml · RandomSkeletalKnight"
#
# 每只生成的生物都有 0.8% 的概率
# 额外生成一名骷髅骑士
# 
RandomSkeletalKnight:
  Type: SkeletalKnight
  Worlds: world
  Chance: 0.008
  Priority: 1
  Action: REPLACE
```
