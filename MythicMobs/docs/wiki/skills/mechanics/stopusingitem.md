---
title: Stopusingitem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/stopusingitem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Stopusingitem {#stopusingitem}

## 说明 {#description}

让目标活体实体停止使用物品，例如停止用盾牌格挡。

> 如果你想进行某种冷却，请尝试在光环中使用此机制

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

```yaml
Skills:
  # basic example
  - stopusingitem @NearestPlayer
  
  # with an aura to prevent the player from using a shield
  - aura{onTick=[ - stopusingitem ?isBlocking ];duration=500} @NearestPlayer
```

## 别名 {#aliases}

- releaseitem
