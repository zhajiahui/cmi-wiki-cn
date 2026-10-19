---
title: Movetolava
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movetolava
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Movetolava {#movetolava}

## 说明 {#description}

让生物向熔岩移动。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动时的速度。 | 0.9 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - movetolava{s=2}
```

## 别名 {#aliases}

- gotolava
