---
title: Set Parent
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/SetParent
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Parent {#set-parent}

## 说明 {#description}

将目标实体设为施法 MythicMob 的父实体，可为玩家或其他 MythicMob。与 [@Parent 目标选择器](../targeters/parent.md)和 [IsParent 条件](../conditions/isparent.md)配合使用。

如果父级是`Player`，则此信息不会在玩家重新登录时持续存在，因此只能“暂时”使用，从设置父级到玩家退出服务器。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

如果该生物还没有父级，它将尝试将其当前父级设置为 20 方块半径内最近的 ZombieBoss 生物

```yaml
ZombieFollower:
  Type: DROWNED
  Skills:
  - setparent @MIR{r=20;t=ZombieBoss;limit=1;sort=NEAREST} ~onTimer:20 ?!hasparent
```
