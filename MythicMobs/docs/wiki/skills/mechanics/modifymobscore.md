---
title: Modifymobscore
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifymobscore
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Modifymobscore {#modifymobscore}

## 说明 {#description}

修改施法生物的记分板计分项值，不支持目标选择器。

## 属性 {#attributes}

> 该机制继承了[ModifyGlobalScore](modifyglobalscore.md)机制的所有属性

## 示例 {#examples}

```yaml
  Skills:
  - modifymobscore
      {
      objective=someobjective;
      action=multiply;
      v=2
      } ~onAttack
```

## 别名 {#aliases}

- mms
