---
title: Sphere
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Sphere
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sphere {#sphere}

## 说明 {#description}

瞄准施法者周围球体中的点

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |
| points | p | 点数。 | 10 |
| yoffset | y | 目标在 y 轴上的偏移。 | 0 |
| exact | e | 目标选择器是否绘制完美球体。 | false |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @Sphere{r=6;points=50}
```
