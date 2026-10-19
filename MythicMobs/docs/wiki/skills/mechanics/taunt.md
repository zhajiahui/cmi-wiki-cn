---
title: Taunt
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Taunt
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Taunt {#taunt}

## 说明 {#description}

修改施法者对目标实体的仇恨值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mode | m | 仇恨值的分配方式 | taunt |

> 此机制继承 [threat](threat.md) 机制的全部属性

## 示例 {#examples}

```yaml
  Skills:
  - taunt @EIR{r=20}
```
