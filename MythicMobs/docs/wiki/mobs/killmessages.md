---
title: 击杀消息
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/KillMessages
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 击杀消息 {#kill-messages}

击杀消息用于自定义玩家被生物击杀时显示的内容。通常只会显示“Player was slain by Zombie”或“Player burned to death”等消息。MythicMobs 可以方便地为生物设置自定义击杀消息，让死亡过程也多一些变化。

## 语法 {#syntax}

添加击杀消息的语法很简单。每个生物可以设置多条消息，实际显示时随机选取一条。

```yaml
Souleater:
  Type: SKELETON
  Display: 'Soul Eater'
  Health: 666
  KillMessages:
  - '<target.name> had their soul completely devoured'
  - '<target.name><&sq>s soul was feasted upon by <caster.name>'
  Skills:
  ...
```

就是这么简单！任何被噬魂者杀死的玩家都会在服务器上显示这两条自定义死亡消息之一。 [占位符](../skills/placeholders.md) 也可以在消息中使用，其中重要的一个是<target.name>，代表死亡玩家的名字。

还可以编辑 `config-mobs.yml`，修改 KillMessagePrefix，为全部击杀消息添加统一前缀。前缀不支持占位符。
