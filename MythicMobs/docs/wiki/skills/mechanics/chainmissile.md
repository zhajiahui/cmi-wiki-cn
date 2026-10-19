---
title: Chainmissile
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/chainmissile
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Chainmissile {#chainmissile}

## 说明 {#description}

向目标发射连锁寻的导弹

> **这是[仅限高级版](../../premium-features.md) 机制！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| bounces | b | 连锁跳转的次数。 | 2 |
| bounceradius | bouncerange, radius, range, r | 技能跳转到新目标的最大距离。 | 5 |
| returnToCaster | return, rtc | 追踪弹是否返回施法者。 | false |
| bounceConditions | conditions, cond, c | 技能跳转的条件，类似于 [chain](chain.md) 机制。 |  |

> 该机制继承了[导弹](missile.md)机制的所有属性

## 示例** {#examples}

```yaml
## Mob.yml ##
Skills:
- skill{s=ChainMissile} @target ~onTimer:200
```

```yaml
## Skills.yml ##
ChainMissile:
  Skills:
  - ChainMissile{bounces=10;r=10;in=1.25;oT=CM_oT;oH=CM_oH;i=1;md=200;mr=30;v=5;hnp=true;hp=true;hR=1;vR=1;sB=False;sE=false;tyo=1;hs=true;hfs=1}
CM_oT:
  Skills:
  - effect:particles{particle=flame;a=1;hs=0;vs=0;s=0;y=0} @origin
CM_oH:
  Skills:
  - damage{a=1;pkb=true}
```

## 别名 {#aliases}

- cmi
