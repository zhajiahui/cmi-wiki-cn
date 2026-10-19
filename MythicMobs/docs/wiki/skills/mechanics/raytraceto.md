---
title: Raytraceto
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/raytraceto
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Raytraceto {#raytraceto}

## 说明 {#description}

将光线追踪到目标，类似于 [光线追踪](raytrace.md) 机制，但具有有关光线开始和结束位置的附加属性。

> **这是[仅限高级版](../../premium-features.md) 机制！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| startyoffset | syo, ystartoffset, ys | 射线起点在 y 轴上的偏移量 | 0 |
| targetyoffset | tyo, ytargetoffset, yt | 射线终点在 y 轴上的偏移量 | 0 |
| fromorigin | fo | 射线是否从机制原点出发 | false |
| useeyelocation | uel | 射线是否从施法者眼睛的位置出发 | false |
| forwardoffset | startfoffset, sfo | 射线起点的前向偏移量 | 0 |
| sideoffset | soffset, sso | 射线起点的侧向偏移量 | 0 |
| entityskill | eskill, es | 射线命中实体时使用的元技能 |  |
| locationskill | lskill, ls | 射线命中位置时使用的元技能 |  |
| headshotskill | hsskill, hs | 爆头时使用的元技能 |  |
| maxdistance | distance, md, d | 射线追踪的最大距离 | 50 |
| raywidth | rw, w | 追踪射线的宽度 | 0.2 |
| ignorepassableblocks | ignorepassable, ip | 忽略可穿过方块的碰撞 | true |
| ignoreentities | ignoreentity, ie | 忽略所有实体 | false |
| fluidcollisionmode | fcm | [决定射线追踪命中流体时的碰撞行为](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/FluidCollisionMode.html) | NEVER |
| accuracy | ac, a | 追踪射线的散布范围 | 1 |
| verticalnoise | vn | 射线的垂直散布范围 | 0 |
| horizontalnoise | hn | 射线的水平散布范围 | 0 |
| raytraceConditions | rc, rcond, rconditions | 对射线追踪目标应用的条件 |  |
| headshotmultiplier | hsmultipler, hsm | 爆头强度倍率 | 1 |

## 示例 {#examples}

```yaml
MyRaytraceToSkill:
  Skills:
  - raytraceto{
      entitySkill=[
        - damage{amount=20}
      ];
      locationSkill=[
        - particles{p=flame;a=20;s=0.2;hS=0.1;vS=0.1}
      ];
      startyoffset=1;
      targetyoffset=1;
      useeyelocation=true
      } @targetlocation ~onUse
```
