---
title: Lunge
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/lunge
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lunge {#lunge}

## 说明 {#description}

对目标应用前向速度。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| velocity | v, magnitude | 实体向前移动的水平速度。 | 1 |
| velocityY | vy, yv, yvelocity | 实体向前移动的竖直速度。 | 1 |
| oldmath | old, o | lunge 机制是否使用旧版数学公式。 | false |

## 示例 {#examples}

```yaml
  Skills:    
  - lunge{velocity=15;velocityY=5} @Self
```
