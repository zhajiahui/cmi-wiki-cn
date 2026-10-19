---
title: Chance
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/chance
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Chance {#chance}

## 说明 {#description}

设置执行元技能的概率。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| chance | c | 表示概率的浮点数。取值范围为 0 到 1，其中 0 表示 0% 的概率，1 表示 100% 的概率。 | 0.5 |

## 示例 {#examples}

在此示例中，平均来说，metaskill 只会执行其触发次数的 30%。

```yaml
Conditions:
  - chance{chance=0.3} true
```

另一个示例中，元技能会在约 70% 的触发次数中执行。

```yaml
Conditions:
  - chance{chance=0.3} false
```
