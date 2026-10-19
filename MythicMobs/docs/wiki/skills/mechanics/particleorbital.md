---
title: Particle Orbital
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleOrbital
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Orbital {#particle-orbital}

## 说明 {#description}

创建粒子轨道效果，粒子将围绕目标实体或位置运行。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 粒子环绕运行的半径。 | 4 |
| points | p | 组成圆形的点数。 | 20 |
| ticks | t | 此效果持续的刻数。 | 100 |
| interval | in, i | 粒子移动的刻速率，刻速率越快，移动越慢。 | 10 |
| rotationX | rotX, rX | 绕 X 轴旋转轨道。 | 0 |
| rotationY | rotY, rY | 绕 Y 轴旋转轨道。 | 0 |
| rotationZ | rotZ, rZ | 绕 Z 轴旋转轨道。 | 0 |
| offsetX | offx, ox | 轨道中心的 X 轴偏移。 | 0 |
| offsetY | offy, oy | 轨道中心的 Y 轴偏移。 | 0 |
| offsetZ | offz, oz | 轨道中心的 Z 轴偏移。 | 0 |
| angularVelocityX | avx, vx | 修改绕 X 轴的角速度。 | 0 |
| angularVelocityY | avy, vy | 修改绕 Y 轴的角速度。 | 0 |
| angularVelocityZ | avz, vz | 修改绕 Z 轴的角速度。 | 0 |
| rotate |  | 粒子是否旋转。任意 angularvelocity 属性大于 0 时，默认为 true。 |  |
| reversed | reverse | 粒子是否沿相反方向环绕运行。 | false |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 示例 {#examples}

```yaml
OrbitalParticleSkill:
  Skills:
  - particleorbital{r=2;points=16;t=100;i=1;vy=20;particle=flame} @self ~onSpawn
```

## 别名 {#aliases}

- effect:particleorbital
- e:particleorbital
- effect:particlecircle
- particlecircle
- e:particlecricle
