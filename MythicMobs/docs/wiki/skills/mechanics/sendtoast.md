---
title: Sendtoast
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sendtoast
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sendtoast {#sendtoast}

## 说明 {#description}

向目标玩家显示类似进度提示的 toast 消息，不影响非玩家实体。

Toast 的标题由帧类型设置，例如 `challenge` 的标题为 `Challenge Complete!`。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| icon | i | 要发送的图标，可使用任何有效的 MATERIAL 或 Mythic 物品 | diamond_sword |
| iconnbt | nbt | 图标的 NBT。 | NONE |
| message | msg,m | 要发送的消息，必须用双引号包裹。 | NONE |
| frame | f | 要发送的进度提示类型，必须使用小写。可选值为 `challenge`、`task` 或 `goal`。 | challenge |

## 示例 {#examples}

```yaml
  Skills:
  - sendtoast{icon=MyCustomDiamond;message="This is a Toast!";frame=challenge} @PlayersInRadius{r=10}
  - ...
```

## 别名 {#aliases}

- toastmessage
- toastmsg
- advmessage
- advancementmessage
