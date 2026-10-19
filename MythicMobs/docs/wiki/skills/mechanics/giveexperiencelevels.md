---
title: Give Experience Levels
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/GiveExperienceLevels
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Give Experience Levels {#give-experience-levels}

## 说明 {#description}

为目标玩家提供经验级别

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要给予的等级数量。 | 0 |

## 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - giveexperiencelevels{a=1} @trigger ~onDamaged
```

## 别名 {#aliases}

- giveexplevels
