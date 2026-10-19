---
title: Distance
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/distance
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Distance {#distance}

## 说明 {#description}

施法者与目标之间的距离是否在给定范围内。   可以是单个数字、范围值 (20 到 40) 或 >10 <5 等。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 要匹配的距离。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - distance{d=<2}
```

---

此示例将生成一个带有调试环的盔甲架以显示距离。根据玩家与盔甲架的距离，生物会发送不同的消息

```yaml
distance_mob:
  Type: ARMOR_STAND
  Skills:
  - particlering{p=redstone;points=20;r=3;a=1} @self ~onTimer:20
  - particlering{p=redstone;points=20;r=7;color=#00ff48;a=1} @self ~onTimer:20
  - particlering{p=redstone;points=20;r=10;color=#0059ff;a=1} @self ~onTimer:20
  - skill{s=distance_check} @PIR{r=10;limit=1;sort=NEAREST} ~onTimer:20
```

```yaml
distance_check:
  TargetConditions:
  - distance{d=0to3} castinstead distance_check_close
  - distance{d=3to7} castinstead distance_check_mid
  - distance{d=>7} castinstead distance_check_far
  Skills:
  - message{m="This message is never sent"}
distance_check_close:
  Skills:
  - message{m="<red><target.name> is close to the caster!"}
distance_check_mid:
  Skills:
  - message{m="<green><target.name> is medium distance from the caster!"}
distance_check_far:
  Skills:
  - message{m="<blue><target.name> is far from the caster!"}
```

> *此示例由 slipperysmurf 友情提供*
