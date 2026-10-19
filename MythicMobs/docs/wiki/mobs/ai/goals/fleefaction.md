---
title: Fleefaction
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleefaction
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fleefaction {#fleefaction}

## 说明 {#description}

让生物逃离特定阵营。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 目标与该生物自身的距离。 | 4 |
| speed | s | 逃离的速度。 | 1.2 |
| safespeed | ss | 到达安全距离（50 格）后逃离的速度。 | 1 |
| faction | f | 要逃离的阵营。 |  |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleefaction{distance=5;speed=2;safespeed=2;faction=somefaction}
```

## 别名 {#aliases}

- runfromfaction
