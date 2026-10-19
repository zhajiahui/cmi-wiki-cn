---
title: Interaction Last Attacker
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/InteractionLastAttacker
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Interaction Last Attacker {#interaction-last-attacker}

## 说明 {#description}

如果施法者属于 `INTERACTION` [类型](../../mobs/mobs.md#type)，则以攻击施法者的最后一个实体为目标。

## 属性 {#attributes}

> *此条件没有属性*

## 示例 {#examples}

以下示例会每隔 100 个游戏刻，点燃最后攻击施法者的实体

```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - ignite @interactionLastAttacker ~onTimer:100
```

## 别名 {#aliases}

- lastAttacker
