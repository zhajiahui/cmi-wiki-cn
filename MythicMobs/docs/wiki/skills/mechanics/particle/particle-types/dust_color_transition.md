---
title: Dust Color Transition
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Dust_Color_Transition
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Dust Color Transition {#dust-color-transition}

## Particle {#particle}

![img](../../../../assets/4dccfb345bf27a.gif)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c, color1, c1, fromcolor, fc | 粒子的起始颜色。 | #FF0000 |
| color2 | c2, tocolor, tc | 粒子渐变到的颜色。 | #0000FF |
| size |  | 粒子的大小。 | 1 |

> 该粒子具有 [Dusttransition](../particle-types.md#dusttransition) 数据类型，并继承其所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particle{p=dust_color_transition;color=#FF0000;color2=#0000FF;size=1}
```

## 别名 {#aliases}

- dustcolortransition
- dustcolor
