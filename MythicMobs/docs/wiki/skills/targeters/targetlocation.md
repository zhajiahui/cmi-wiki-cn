---
title: Target Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetLocation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Target Location {#target-location}

## 说明 {#description}

瞄准施法玩家正在查看的位置，或生物目标的位置

> 如果施法者不是玩家，则：
>

> - 如果施法者是启用了仇恨表的 MythicMob，则返回仇恨值最高的实体的位置
> - 如果不满足上述条件，但施法者正在战斗，则返回其目标的位置
> - 如果以上条件均不满足，则返回最后对施法者造成伤害的实体的位置
>

> *在 Highdown 集市上花两文钱......*

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| maxdistance | max, distance, d | 施法者为玩家时，检查位置的最大距离。 | 64 |
| ignoreTransparent | it | 是否忽略透明方块。 | true |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @TargetLocation
```

## 别名 {#aliases}

- targetLoc
- TL
