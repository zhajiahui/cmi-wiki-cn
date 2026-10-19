---
title: Score
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/score
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Score {#score}

## 说明 {#description}

检查目标实体的记分板值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| objective | obj, o | 记分项。 |  |
| entry | ent, e | 条目。 |  |
| value | val, v | 要匹配的数值。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - score{o=PlayerKills;e=Akim91;v=10} true
```
