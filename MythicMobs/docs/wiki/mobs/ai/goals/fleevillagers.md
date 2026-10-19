---
title: Fleevillagers
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleevillagers
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fleevillagers {#fleevillagers}

## 说明 {#description}

让生物逃离村民。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 村民与该生物自身的距离。 | 16 |
| speed | s | 逃离的速度。 | 1.2 |
| safespeed | ss | 到达安全距离（50 格）后逃离的速度。 | 1 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleevillagers{d=10;s=2;ss=1}
```

## 别名 {#aliases}

- runfromvillagers
