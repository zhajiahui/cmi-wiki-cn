---
title: Particle Equation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ParticleEquation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Particle Equation

# DISCLAIMER {#disclaimer}

**此机制尚在开发中，目前无法正常使用，示例也不可用，请勿用于实际配置。**

## 说明 {#description}

根据方程生成粒子效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| equation |  | 要使用的方程，允许使用 `x`、`y`、`z` 变量。 | 0 |
| precision |  | 各个粒子之间的距离。 | 1 |
| tolerance |  | 浮点误差容差。 | 0.1 |
| variables |  | 方程表达式的变量映射，与 x/y/z 类似，以 `;` 分隔，例如 `variables="h=1;t=2"`。 |  |

> 该机制继承了[粒子](particle.md)机制的所有属性

## 别名 {#aliases}

- effect:particleequation
- particleequation
- e:peq
- peq
