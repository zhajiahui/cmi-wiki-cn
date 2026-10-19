---
title: Metaskill Condition
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/MetaskillCondition
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Metaskill Condition {#metaskill-condition}

## 说明 {#description}

施放元技能，以判断此条件是否成立，从而对给定目标应用更复杂的逻辑。被调用的元技能必须使用 [DetermineCondition](../mechanics/determinecondition.md) 机制，设置或修改此条件是否成立。

## 属性 {#attributes}

> 该条件继承[技能](../mechanics/skill.md)机制的所有属性

## 示例 {#examples}

```yaml
YourNormalMetaskill:
  Conditions:
  - metaskillcondition{skill=metaskillcondition_check;hello=ciao;world=mondo}
  Skills:
  - message{m="Condition Passed"} @self
metaskillcondition_check:
  Conditions:
  - holding{types=stick}
  Skills:
  - log{message=metaskill condition passed with parameters of <skill.test> <skill.aaa>} @self
  - determineCondition{det=true} @self
```

## 别名 {#aliases}

- skillcondition
