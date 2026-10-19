---
title: Playersinworld
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playersinworld
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Playersinworld {#playersinworld}

## 说明 {#description}

匹配施法者世界中的玩家数量

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要检查的玩家数量，可以是范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - playersInWorld{amount=>5}
```
