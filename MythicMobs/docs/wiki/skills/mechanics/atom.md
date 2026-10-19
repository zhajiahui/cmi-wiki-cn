---
title: Atom
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Atom
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Atom {#atom}

## 说明 {#description}

在目标位置创建原子环绕效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| particleorbital | particleo, po | 轨道上显示的[粒子](particle/particle-types.md)。 | `particle` |
| particlenucleus | particlen, pn | 原子核处显示的[粒子](particle/particle-types.md)。 | reddust |
| amountnucleus | amountn, apn, an | 原子核的粒子数量。 | 50 |
| orbitals | o | 原子核周围的轨道数量。 | 2 |
| amountorbital | amounto, apo, ao | 每条轨道的粒子数量。 | 1 |
| radius | r | 轨道半径。 | 4 |
| radiusnucleus | rn | 原子核半径。 | 1 |
| rotation | ro | 原子的旋转角度。 | 0 |
| ticks | t | 原子持续存在的刻数。 | 1 |
| interval | in | 原子的更新间隔。 | 10 |
| velocity | v | 原子的速度。 | 80 |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 示例 {#examples}

```yaml
  Skills:
  - Atom{p=reddust;r=2;d=true;dr=true;dir=1,0,0;ticks=20} @selflocation{y=2} ~onSwing
```

## 别名 {#aliases}

- effect:atom
- e:atom
