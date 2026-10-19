---
title: Cancel Skill
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/CancelSkill
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cancel Skill {#cancel-skill}

## 说明 {#description}

触发时取消[Metaskill](../metaskills.md)的执行

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

```yml
SomeSkill:
  Skills:
  - message{m="Hello"} @server
  - cancelSkill ?isMonster #cancels the rest of the skill from executing if the condition is met
  - message{m="It appears i am not a monster! Yay!"} @server
```

## 别名 {#aliases}

- cancel
- return
