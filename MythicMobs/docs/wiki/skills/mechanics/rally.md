---
title: Rally
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/rally
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Rally {#rally}

## 说明 {#description}

集结附近给定类型的生物来集中攻击给定目标。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t | 要召集的生物类型列表，可同时包含 Mythic 生物类型和普通实体类型 |  |
| radius | r, hradius, hr | 搜索并召集生物的半径，以方块为单位 | 10 |
| vradius | vr | 覆盖半径的垂直分量。 | radius |
| overwritetarget | ot | 是否召集已经有目标的生物 | true |
| rallyconditions | conditions, cond, c | 实体必须通过此条件列表，才会被召集 |  |

## 示例 {#examples}

本例让 30 格内类型为 Guard 或 Knight、且当前没有目标的生物，攻击触发技能的实体。

```yaml
CallForHelp:
  Skills:
  - message{m="<caster.name><&co> Guards! Help me!"} @PlayersInRadius{r=30}
  - rally{types=Guard,Knight;radius=30;ot=false} @Trigger
```

## 别名： {#aliases}

- callforhelp
