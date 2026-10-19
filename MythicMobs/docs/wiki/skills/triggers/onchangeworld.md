---
title: Onchangeworld
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onchangeworld
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onchangeworld {#onchangeworld}

## 说明 {#description}

当施法者改变世界时执行技能。

## 示例 {#examples}

```yaml
WorldJumper:
  Type: WITHER_SKELETON
  Skills:
  - command{c=say The End!} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_the_end}
  - command{c=say The Nether!} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_nether}
```

## 别名 {#aliases}

- onChange_World
- onWorld_Change
- onWorldChange
