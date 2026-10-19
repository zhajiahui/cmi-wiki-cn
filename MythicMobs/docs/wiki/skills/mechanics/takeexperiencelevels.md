---
title: Take Experience Levels
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/TakeExperienceLevels
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Take Experience Levels {#take-experience-levels}

## 说明 {#description}

从目标玩家那里获取经验水平

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要扣除的等级数 | 0 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - takeexperiencelevels{a=1} @trigger ~onDamaged
```

## 别名 {#aliases}

- takeexplevels
