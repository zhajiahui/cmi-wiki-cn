---
title: Closeinventory
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/closeinventory
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Closeinventory {#closeinventory}

## 说明 {#description}

关闭目标的物品栏，目标必须是玩家。

必须设置 `forcesync=true`。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

```yaml
  Skills:
  - closeinventory{forcesync=true} @target ~onTimer:100
```
