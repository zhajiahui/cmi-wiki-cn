---
title: Raytrace
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/raytrace
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Raytrace {#raytrace}

## 说明 {#description}

追踪一条射线到达目标。

> **这是[仅限高级版](../../premium-features.md) 机制！**

| [已实现的占位符](../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.hit-block-type>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| entityskill | eskill, es | 射线命中实体时使用的元技能 |  |
| locationskill | lskill, ls | 射线命中位置时使用的元技能 |  |
| headshotskill | hsskill, hs | 爆头时使用的元技能 |  |
| maxdistance | distance, md, d | 射线追踪的最大距离 | 50 |
| raywidth | rw, w | 追踪射线的宽度 | 0.2 |
| ignoreentities | ignoreentity, ie | 是否忽略实体，使射线追踪不会被实体阻挡 | false |
| ignorepassableblocks | ignorepassable, ip | 忽略可穿过方块的碰撞 | true |
| fluidcollisionmode | fcm | [决定射线追踪命中流体时的碰撞行为](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/FluidCollisionMode.html) | NEVER |
| accuracy | ac, a | 追踪射线的散布范围 | 1 |
| verticalnoise | vn | 射线的垂直散布范围 | 0 |
| horizontalnoise | hn | 射线的水平散布范围 | 0 |
| raytraceConditions | rc, rcond, rconditions | 对射线追踪目标应用的条件 |  |
| headshotmultiplier | hsmultipler, hsm | 爆头强度倍率 | 1 |

## 示例 {#examples}

```yaml
MyRaytraceSkill:
  Skills:
  - raytrace{
      entitySkill=[
        - damage{amount=20}
      ];
      headshotSkill=[
        - effect:particles{particle=reddust;color=#ff0000}
      ];
      locationSkill=[
        - particles{p=flame;a=20;s=0.2;hS=0.1;vS=0.1}
      ];
      raytraceConditions=[
        - samefaction false
      ]} @targetlocation ~onUse
```
