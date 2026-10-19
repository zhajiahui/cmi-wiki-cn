---
title: Leap
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/leap
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Leap {#leap}

## 说明 {#description}

使生物从空中跃向目标。Leap 会计算类似抛物线的轨迹：速度足够大时，生物直接落到目标上方；否则尽可能向目标跳远。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v | 跳跃的最大速度。 | 100 |
| noise | n | 生物落点额外增加的随机变化量。 | 0 |

### Velocity 属性 {#velocity-attribute}

由于此技能的工作方式，建议使用非常高的速度值（通常超过100的值效果最佳）。此技能的速度计算方式与大多数其他技能不同。

## 示例 {#examples}

该技能会让生物以高速跃向目标，然后猛烈撞击地面并引发爆炸。

```yaml
CrushingLeap:
  Cooldown: 10
  Skills:
  - leap{velocity=200} @target
  - delay 20
  - jump{velocity=-100}
  - effect:explosion @self
  - damage{amount=20} @EntitiesInRadius{r=5}
```
