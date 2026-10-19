---
title: Targets
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targets
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Targets {#targets}

## 说明 {#description}

检查从父技能树继承的目标数量是否符合给定范围。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要检查的目标数量范围。 | >0 |
| targeter |  | 设置后，此条件改为检查给定目标选择器所选的目标。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - targets{a=>0} true
```

```yaml
  Conditions:
  - targets{a=0to5} true
```

```yaml
  Conditions:
  - targets{a=>10;targeter=@MIR{r=10;type=SomeMythicMob}} true
```
