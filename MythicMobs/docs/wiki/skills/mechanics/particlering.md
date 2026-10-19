---
title: Particle Ring
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleRing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Ring {#particle-ring}

## 说明 {#description}

在目标实体或位置周围创建一圈粒子。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| points | pts | 用于绘制圆环的点数。 | 8 |
| radius | r | 目标周围圆环的半径。 | 10 |

> 该机制继承了[粒子](particle.md)机制的所有属性
>

> > 在此机制中，粒子是“每点”生成的，因此建议保持 `amount` 较低。

## 示例 {#examples}

```yaml
FlameRing:
  Skills:
  - particlering{particle=flame;radius=20;points=32;amount=1;hS=1;vS=0} @target
```

## 别名 {#aliases}

- effect:particlering
- e:pr
- pr
