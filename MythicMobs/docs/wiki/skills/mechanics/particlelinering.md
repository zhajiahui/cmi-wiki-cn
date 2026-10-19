---
title: Particle Line Ring
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleLineRing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Line Ring {#particle-line-ring}

## 说明 {#description}

创建粒子线环。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distanceBetween | db | 各点之间的距离。 | 1 |
| startYOffset | syo, ystartoffset, ys | 起点的 Y 坐标偏移。 | 0 |
| targetYOffset | tyo, ytargetoffset, yt | 目标点的 Y 坐标偏移。 | 0 |
| fromOrigin | fo | 是否改为从 [@origin](../targeters/origin.md) 绘制线条。 | false |
| ringpoints | rp | 线环上的点数。 | 16 |
| ringradius | rr | 线环的半径。 | 0.5 |
| maxdistance | md | 线条可达到的最大距离。 | 256 |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particlelinering{p=flame;r=3;rr=1} @PIR{r=20;limit=1;sort=RANDOM}
```

## 别名 {#aliases}

- effect:particlelinering
- particleringline
