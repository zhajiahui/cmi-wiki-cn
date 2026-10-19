---
title: Removehelditem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/removehelditem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Removehelditem {#removehelditem}

## 说明 {#description}

从施法玩家持有的物品中移除指定数量。

> **这是一个无目标机制，受影响的玩家将始终是施法者**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要移除的数量 | 1 |

## 示例 {#examples}

作为仅针对施法玩家的技能，生物可能需要使用 [sudoskill](sudoskill.md) 来移除玩家的物品：

```yaml
munchy:
  Type: PIG
  Skills:
  - SudoSkill{s=removeApple} @trigger ~onInteract
```

这将导致玩家在右键单击生物时施放`removeApple`元技能：

```yaml
removeApple:
  Conditions:
  - holding{m=APPLE} true
  Skills:
  - removeHeldItem{amount=1}
```

此示例检查玩家（现在是施法者）是否拿着苹果，如果是，则从手中移除 1。

## 别名 {#aliases}

- consumeHeldItem
- takeHeldItem
