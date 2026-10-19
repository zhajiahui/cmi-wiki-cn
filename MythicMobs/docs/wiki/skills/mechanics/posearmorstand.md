---
title: Posearmorstand
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/posearmorstand
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Posearmorstand {#posearmorstand}

## 说明 {#description}

移动盔甲架的肢体，数值单位为弧度。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| head | h | 头部的旋转角度。 | 0,0,0 |
| body | b | 身体的旋转角度。 | 0,0,0 |
| leftarm | la | 左臂的旋转角度。 | 0,0,0 |
| rightarm | ra | 右臂的旋转角度。 | 0,0,0 |
| leftleg | ll | 左腿的旋转角度。 | 0,0,0 |
| rightleg | rl | 右腿的旋转角度。 | 0,0,0 |

## 示例 {#examples}

```yaml
  Skills:
  - posearmorstand{head=0.78,0,0} @self ~onSpawn
  - ...
```

## 别名 {#aliases}

- armorstandpose
