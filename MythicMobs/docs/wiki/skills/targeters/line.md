---
title: Line
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Line
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Line {#line}

## 说明 {#description}

目标位于生物和继承目标之间的位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 线条上各点之间的距离。 | 1 |
| fromorigin | fo | 是否从元技能原点开始绘制线条。 | false |

## 示例 {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @Forward{f=10}

ExampleSkill2:
  Skills:
  - effect:particles @Line{r=0.5}
```
