---
title: Animatearmorstand
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/animatearmorstand
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Animatearmorstand {#animatearmorstand}

## 说明 {#description}

使盔甲架在指定时间内呈现一个姿势

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d | 动画持续时间，单位为刻。 | 1 |
| smart |  | 是否应用智能角度转换。 | true |
| ignoreempty | ie | 是否忽略空的姿势值。 | true |
| usedegrees | ud | 设为 true 时，将输入值解释为角度（0-360）；设为 false 时，解释为弧度（0-6.28）。 | true |
| head | h | 盔甲架头部的姿势。 |  |
| body | b | 盔甲架身体的姿势。 |  |
| leftarm | la | 盔甲架左臂的姿势。 |  |
| rightarm | ra | 盔甲架右臂的姿势。 |  |
| leftleg | ll | 盔甲架左腿的姿势。 |  |
| rightleg | rl | 盔甲架右腿的姿势。 |  |

## 示例 {#examples}

```yaml
  Skills:
  - animatearmorstand{d=10;leftarm=90,0,0;rightarm=270,0,0;ignoreempty=false}
```

## 别名 {#aliases}

- animateas
- animas
