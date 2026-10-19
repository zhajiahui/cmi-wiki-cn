---
title: Leapattarget
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/leapattarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Leapattarget {#leapattarget}

## 说明 {#description}

让生物跃向目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 向目标跳跃的速度。 | 1.2 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - leapattarget{s=4}
```

## 别名 {#aliases}

- leaptowardstarget
