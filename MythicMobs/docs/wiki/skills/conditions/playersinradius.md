---
title: Playersinradius
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playersinradius
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Playersinradius {#playersinradius}

## 说明 {#description}

检查半径内有多少玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要检查的给定范围值。 | >0 |
| radius | r, distance, d | 要检查的给定半径。 | 32 |
| ignorespectator | is | 是否忽略旁观模式的玩家。 | true |

## 示例 {#examples}

```yaml
  Conditions:
  - playersinradius{a=>3;r=16}
```

## 别名 {#aliases}

- pir
- playerInRadius
