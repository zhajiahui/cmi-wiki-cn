---
title: Particle Line
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleLine
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Line {#particle-line}

## 说明 {#description}

创建从施法者到目标实体或位置的粒子线。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distanceBetween | db | 线条上各点之间的距离。 | 0.25 |
| startYOffset | syo, ystartoffset, ys | 线条起点的 Y 坐标偏移。 | 0 |
| targetYOffset | tyo, ytargetoffset, yt | 线条目标点的 Y 坐标偏移。 | 0 |
| fromOrigin | fo | 是否改为从 [@origin](../targeters/origin.md) 绘制线条。 | false |
| zigzag | zz | 是否将通向目标的线条绘制为锯齿形。 | false |
| zigzags | zzs | 使用锯齿选项时的锯齿数量。 | 10 |
| zigzagOffset | zzo | 每个锯齿的偏移。 | 0.2 |
| maxdistance | md | 线条可达到的最大距离。 | 256 |

> 该机制继承了[粒子](particle.md)机制的所有属性
>

> > 在此机制中，粒子是“每点”生成的，因此建议保持 `amount` 较低。

## 示例 {#examples}

```yaml
FlameParticleLine:
  Skills:
  - particleline{particle=flame;amount=1;fromOrigin=true} @target
```

## 别名 {#aliases}

- effect:particleline
- e:pl
- pl
