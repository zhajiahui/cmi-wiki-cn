---
title: Onskilldamage
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onskilldamage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onskilldamage {#onskilldamage}

## 说明 {#description}

生物通过技能机制造成伤害时执行技能。

> 关联的 [@trigger](../targeters/trigger.md) 是受到伤害的实体

## 示例 {#examples}

```yaml
ExampleMob:
  Type: 
  Skills:
  - damage @PIR{r=10} ~onTimer:20
  - message{m="Get damaged! MUHAHAHA"} @trigger ~onSkillDamage
```

## 别名 {#aliases}

- onSkillHit
- onSkill_Damage
