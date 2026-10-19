---
title: Doppleganger
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/doppleganger
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Doppleganger {#doppleganger}

## 说明 {#description}

复制目标玩家的外观。如果目标不是玩家，则不执行任何操作。此技能需要安装 Libs' Disguises 才能启用伪装功能。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| hasnameplate | nameplate | 伪装是否显示名称标签。 | true |
| usePlayerName | upn | 使用玩家名称作为名称标签。 |  |

## 示例 {#examples}

```yaml
TotallyNotDitto:
  Type: SKELETON
  Skills:
  - doppleganger @NearestPlayer ~onSpawn
```

## 别名 {#aliases}

- copyplayer
