---
title: Disengage
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/disengage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Disengage {#disengage}

## 说明 {#description}

使施法者向后跳跃远离目标实体

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v, magnitude | 跳跃的速度。 | 1 |
| velocityy | yvelocity, vy, yv | 跳跃速度的 y 分量。 | 0.01337 |

## 示例 {#examples}

```yaml
ExampleMob:
  Skills:
  - disengage @trigger ~onDamaged
```
