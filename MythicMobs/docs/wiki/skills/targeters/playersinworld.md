---
title: Players In World
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInWorld
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Players In World {#players-in-world}

## 说明 {#description}

以施法者世界中的所有玩家为目标

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

```yaml
PlayerCount:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @PlayersInWorld{targetself=true}
  - message{m="There are <skill.var.count> entities loaded in the current world"} @self
```

## 别名 {#aliases}

- World
