---
title: 烟花
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/firework
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 烟花

# Firework {#firework}

## 说明 {#description}

在目标处产生烟花效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 烟花类型，列表见下文。 | BALL |
| power | p, duration, d | 烟花的飞行时间。 | 2 |
| flicker | f | 是否为爆炸添加闪烁效果。 | false |
| trail | tr | 是否为烟花火箭添加拖尾效果。 | false |
| colors | color, c | 烟花爆炸的颜色，以 RGB 或十六进制表示。 | #FFFFFF |
| fadecolors | fcolors, fc | 烟花爆炸的渐变颜色，以 RBG 或十六进制表示。 | #FFFFFF |

### Type 属性 {#type-attribute}

type 属性的值可以是以下之一

- `BALL`
- `BALL_LARGE`
- `BURST`
- `CREEPER`
- `STAR`

## 示例 {#examples}

```yaml
  Skills:
  - effect:firework{t=BALL;d=1;f=true;tr=true} @self ~onInteract
```

## 别名 {#aliases}

- fireworks
- effect:firework
- effect:fireworks
- e:firework
