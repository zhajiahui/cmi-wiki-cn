---
title: Fleegolems
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleegolems
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fleegolems {#fleegolems}

## 说明 {#description}

让生物逃离铁傀儡。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 目标与该生物自身的距离。 | 16 |
| speed | s | 逃离的速度。 | 1.2 |
| safespeed | ss | 到达安全距离（50 格）后逃离的速度。 | 1 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleegolems{d=10;s=2;ss=1}
```

## 别名 {#aliases}

- runfromgolems
