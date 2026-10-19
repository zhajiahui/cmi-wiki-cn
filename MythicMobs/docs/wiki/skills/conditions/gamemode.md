---
title: Gamemode
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/Gamemode
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Gamemode {#gamemode}

## 说明 {#description}

匹配目标玩家的游戏模式

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mode | m | 要匹配的游戏模式。 | SURVIVAL |

### Mode 属性 {#mode-attribute}

可能的游戏模式有

- `SURVIVAL`
- `CREATIVE`
- `ADVENTURE`
- `SPECTATOR`

## 示例 {#examples}

```yaml
ExampleSkill:
  Conditions:
  - gamemode{m=ADVENTURE} true
```

## 别名 {#aliases}

- gm
