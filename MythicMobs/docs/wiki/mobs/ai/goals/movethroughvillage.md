---
title: Movethroughvillage
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movethroughvillage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Movethroughvillage {#movethroughvillage}

## 说明 {#description}

让生物寻找穿过村庄的路径。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动时的速度。 | 0.6 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - movethroughvillage{s=2}
```
