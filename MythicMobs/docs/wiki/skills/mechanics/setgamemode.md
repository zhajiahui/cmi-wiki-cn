---
title: Setgamemode
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setgamemode
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setgamemode {#setgamemode}

## 说明 {#description}

设置目标玩家的游戏模式。如果目标不是玩家，则不执行任何操作。需要 `sync=true` 属性。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mode | m | 要为目标设置的游戏模式。 | SURVIVAL |

## 示例 {#examples}

```yaml
  Skills:
  - setgamemode{m=CREATIVE;sync=true} @PlayersInRadius{r=10} ~onSpawn
  - ...
```
