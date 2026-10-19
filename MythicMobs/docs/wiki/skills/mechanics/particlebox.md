---
title: Particle Box
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleBox
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Box {#particle-box}

## 说明 {#description}

在目标实体或位置创建粒子框。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 要绘制的方框半径。 | 5 |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 示例 {#examples}

```yaml
ParticleCube:
  Skills:
  - particlebox{particle=flame;amount=200;radius=5} @self
```

## 别名 {#aliases}

- effect:particlebox
- e:pb
- pb
