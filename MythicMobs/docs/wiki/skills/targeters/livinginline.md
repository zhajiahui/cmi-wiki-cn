---
title: Living In Line
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInLine
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Living In Line {#living-in-line}

## 说明 {#description}

瞄准继承目标和施法生物之间的一条线上的任何实体

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 线上各点之间的距离，以及每个点周围用于选择实体的半径。 | 1 |
| fromorigin | fo | 是否从元技能原点开始绘制线条。 | false |

## 示例 {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @Forward{f=10}

ExampleSkill2:
  Skills:
  - ignite @LivingInLine{r=0.5}
```

## 别名 {#aliases}

- entitiesInLine
- livingEntitiesInLine
- LEIL
- EIL
