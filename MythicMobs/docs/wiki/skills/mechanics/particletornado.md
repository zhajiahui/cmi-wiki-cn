---
title: Particle Tornado
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleTornado
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Tornado {#particle-tornado}

## 说明 {#description}

创建龙卷风风格的粒子效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| maxradius | mr | 龙卷风最上层“圆盘”的最大半径。 | 3 |
| yoffset | yo | 效果的 yoffset。 | 0.8 |
| height | h | 所需圆盘数量 * 2 + 1 | 4 |
| interval | i | 粒子竖直方向的显示速度，也可配合“rotationspeed”尝试调整。 | 4 |
| duration | d | 效果的持续时间，单位为刻。 | 200 |
| rotationspeed | rs | 粒子水平方向的显示速度，也可配合“interval”尝试调整。 | 0.04 |
| sliceheight | sh | 小于 1 的值会使龙卷风不完整，大于 10 的值则会使不同大小的球体以奇怪的顺序出现。此项尚未完全明确。 | 64 |
| stoponcasterdeath | scd | 施法者死亡时是否停止效果。 | true |
| stoponentitydeath | sed | 被施加此效果的实体死亡时是否停止效果。 | true |
| cloudparticle | cp | 龙卷风底部的粒子类型。通常用于表现龙卷风旋转时的“撞击”效果，因此默认值为 largeexplode。 | largeexplode |
| cloudsize | cs | 云中粒子出现范围的半径。 | 5 |
| cloudamount | ca | 每个随机生成的云位置出现的粒子数量。 | 1 |
| cloudhspread | chs | 云的水平散布。 | 1 |
| cloudvspread | cvs | 云的竖直散布。 | 1.8 |
| cloudpspeed | cps | 云粒子的播放速度。 | 2 |
| cloudyoffset | cyo | 整个龙卷风的 Y 轴偏移，计算为 (1 + 所需高度)。 | 1.8 |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 示例 {#examples}

```yaml
ExplodingTornado:
  Skills:
  - particletornado{p=flame;cp=largeexplode;mr=1;h=3;i=4;d=100;rs=1;sh=1;cs=0;ca=0;chs=0.1;cvs=0.1;cps=1;cyo=2} @self ~onTimer:100
```

## 别名 {#aliases}

- effect:particletornado
- e:pt
