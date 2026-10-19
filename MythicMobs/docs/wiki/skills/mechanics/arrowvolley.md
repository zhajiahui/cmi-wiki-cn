---
title: Arrowvolley
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/arrowvolley
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Arrowvolley {#arrowvolley}

## 说明 {#description}

向目标发射一连串箭，具有许多可配置的属性。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | arrows, a | 齐射的箭矢数量。 | 20 |
| spread | s | 箭矢的散布程度。 | 45 |
| velocity | v | 箭矢的速度。 | 20 |
| fireTicks | ft, f | 被命中实体的燃烧持续时间，单位为刻。 | 0 |
| removeDelay | rd, r | 箭矢消失前保留的时间，单位为刻。 | 200 |
| canPickup | pickup | 玩家是否可以捡起箭矢。 | true |

> Spread 的数值必须很高，才能明显看出散布效果！

## 示例 {#examples}

本例发射 20 支箭，散布为 25，速度为 10。箭会点燃命中的目标，持续 50 游戏刻（2.5 秒），并在 200 游戏刻（10 秒）后移除。

```yaml
  Skills:
  - arrowvolley{a=20;s=25;v=10;f=50;rd=200} @Target
```
