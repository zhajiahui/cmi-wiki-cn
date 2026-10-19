---
title: Beam
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Beam
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Beam {#beam}

## 说明 {#description}

在施法者与目标之间创建由指定材质组成的光束。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onhitskill | onhit, oh | 光束命中实体时执行的技能，目前不支持。 |  |
| ontickskill | ontick, ot | 每刻执行的技能，原点为起始位置。 |  |
| duration | d | 光束的持续时间，单位为刻。 | 20 |
| tickinterval | interval, i | 光束的更新间隔，单位为刻。 | 1 |
| material | m | 光束的材质。 | END_ROD |
| rotationspeed | rs | 光束的旋转速度，单位为度/刻。 | 0 |
| hitradius | radius, r | 光束的命中半径。 | 1.0 |
| startyoffset | syo | 光束起点相对于施法者位置的 y 轴偏移。 | 0 |
| endyoffset | eyo | 光束终点相对于目标位置的 y 轴偏移。 | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - beam{d=100;rs=2;syo=100} @selflocation
```
