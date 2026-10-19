---
title: Look
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/look
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Look {#look}

## 说明 {#description}

使实体注视其目标。可以用来制作很酷的效果或令人毛骨悚然的效果，具体取决于你的创意程度。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| headOnly | ho | 仅让生物的头部朝向目标。 | false |
| force | f | 强制生物看向目标，即使没有 AI 也有效。 | false |
| forcepaper | fp | 是否使用 Paper 的方法强制生物看向目标。 | false |
| immediately | immediate, i | 立即让生物转向目标，不播放转向动画。 | true |
| speed | s, duration, ticks | 实体完全转向新方向所需的刻数。 | 10 |

## 示例 {#examples}

下面的技能使生物立即迫使其头部立即面向目标。给人一种令人毛骨悚然的效果，因为只有头部会凝视一小会儿，然后身体也会跟上并转身。

```yaml
CreepyStare:
  Skills:
  - look{headOnly=true;immediately=true} @Target
```
