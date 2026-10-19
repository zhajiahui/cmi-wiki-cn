---
title: Players On Server
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersOnServer
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Players On Server {#players-on-server}

## 说明 {#description}

针对服务器中的所有玩家

## 属性 {#attributes}

> *此目标选择器没有属性*

## 示例 {#examples}

```yaml
PlayerCount_ServerWide:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @PlayersOnServer{targetself=true}
  - message{m="There are <skill.var.count> entities loaded in the current world"} @self
```

## 别名 {#aliases}

- server
- everyone
