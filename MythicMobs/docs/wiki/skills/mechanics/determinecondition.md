---
title: Determine Condition
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/DetermineCondition
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Determine Condition {#determine-condition}

## 说明 {#description}

通过 [MetaskillCondition](../conditions/metaskillcondition.md) 条件确定用作条件的元技能的结果

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| determination | det | 修改相关条件的返回结果，可以为 `true` 或 `false`。 | true |
| mode |  | 修改判定值的方式，可以为 `SET`、`OR`、`AND`、`NOT`。除 SET 会直接覆盖已有判定值外，其余选项均按相应的[布尔运算](https://en.wikipedia.org/wiki/Boolean_algebra#Boolean_operations)工作。 | SET |

## 示例 {#examples}

```yaml
  Skills:
  - determinecondition{determination=true} @self
```

## 别名 {#aliases}

- detCond
