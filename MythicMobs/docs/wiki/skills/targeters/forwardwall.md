---
title: Forward Wall
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ForwardWall
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Forward Wall {#forward-wall}

## 说明 {#description}

瞄准施法者前方的方块平面

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| forward | f, amount, a | 目标点应距离多远，接受小数。 | 5.0 |
| yoffset | y | 平面的 y 轴偏移，接受小数。 | 0.0 |
| height | h | 平面的高度，仅限整数。 | 2 |
| width | w | 平面的宽度，仅限整数。 | 3 |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @ForwardWall{f=5;y=1;h=2;w=2}
```
