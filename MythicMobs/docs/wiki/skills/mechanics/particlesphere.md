---
title: Particle Sphere
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleSphere
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Sphere {#particle-sphere}

## 说明 {#description}

在目标实体或位置创建粒子球体。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 要绘制的球体半径。 | 0 |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 示例 {#examples}

```yaml
FlameSphere:
  Skills:
  - particlesphere{particle=flame;amount=200;radius=5} @self
```

## 别名 {#aliases}

- effect:particlesphere
- e:ps
- ps
