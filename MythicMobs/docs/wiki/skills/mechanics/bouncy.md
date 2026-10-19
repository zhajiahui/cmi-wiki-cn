---
title: Bouncy
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Bouncy
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bouncy {#bouncy}

## 说明 {#description}

对目标施加光环，使其有弹性

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onBounceSkill | onbounce, ob | 弹跳时执行的元技能。 |  |
| cancelevent | ce, canceldamage, cd | 光环持续期间是否取消摔落伤害。 | false |

> 该机制继承了[光环](aura.md)机制的所有属性

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - bouncy{auraName=bounce;onBounceSkill=ExampleSkill2;ce=true} @target

ExampleSkill2:
  Skills:
  - ignite
```
