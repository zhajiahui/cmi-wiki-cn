---
title: Particle Line Helix
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleLineHelix
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Line Helix {#particle-line-helix}

## 说明 {#description}

在目标实体或位置创建粒子线螺旋效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distanceBetween | db | 各点之间的距离。 | 1 |
| startYOffset | syo, ystartoffset, ys | 起点的 Y 坐标偏移。 | 0 |
| targetYOffset | tyo, ytargetoffset, yt | 目标点的 Y 坐标偏移。 | 0 |
| fromOrigin | fo | 是否改为从 [@origin](../targeters/origin.md) 绘制线条。 | false |
| helixlength | hl | 螺旋效果的长度。 | 2 |
| helixradius | hr | 螺旋效果的半径。 | 1 |
| helixrotation | rot | 螺旋效果的旋转角度。 | 0 |
| maxdistance | md | 线条可达到的最大距离。 | 256 |

> 该机制继承了[粒子](particle.md)机制的所有属性
>

> > 在此机制中，粒子是“每点”生成的，因此建议保持 `amount` 较低。

## 示例 {#examples}

```yaml
  Skills:
  - particlelinehelix{Fo=true;db=0.4;hl=4;syo=1.8;p=scrape;hr=0.5;md=40} @targetlocation
```

## 别名 {#aliases}

- effect:particlelinehelix
- particlehelixline
