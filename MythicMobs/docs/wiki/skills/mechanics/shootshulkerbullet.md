---
title: Shootshulkerbullet
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/shootshulkerbullet
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Shootshulkerbullet {#shootshulkerbullet}

## 说明 {#description}

向目标实体发射一颗潜影贝子弹，使目标实体在击中时悬浮起来。

> 需要一个目标实体。不适用于位置目标选择器

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 子弹的类型 | arrow |
| damage | d | 子弹的伤害 | 5 |
| bounce |  | 子弹是否弹跳 | false |
| interval | int, i | 此机制每隔多少刻更新一次 | 4 |
| onTick | oT, m, meta, ontickskill, s, skill | 此机制在每个间隔调用的技能 |  |
| onHit | oH, onhitskill | 此机制命中目标时调用的技能 |  |
| onEnd | oE, onendskill | 此机制结束时调用的技能 |  |
| startyoffset | syo | 子弹起点的 y 偏移量 | 0 |
| forwardoffset | startfoffset, sfo | 子弹的前向偏移量 | 0 |
| fromorigin | fo | 是否从原点发射潜影贝子弹 | false |

## 示例 {#examples}

本例发射潜影贝导弹，在 onTick 和 onEnd 中产生小型白色红石粒子，并在命中时对目标造成 5 点伤害。

```yaml
TestingShootShulkerBullet:
  Skills:
  - ShootShulkerBullet{oT=TSSB_oT;oH=TSSB_oH;oE=TSSB_oE;i=1} @target
  
TSSB_oT:
  Skills:
  - particles{particle=reddust;color=#ffffff;size=0.66;a=2;hs=0;vs=0;s=0;y=0} @origin
TSSB_oH:
  Skills:
  - damage{a=5}
TSSB_oE:
  Skills:
  - particlesphere{particle=reddust;color=#ffffff;size=0.66;a=30;r=1;hs=0;vs=0;s=0;y=0} @origin
```

## 别名 {#aliases}

- shootshulker
