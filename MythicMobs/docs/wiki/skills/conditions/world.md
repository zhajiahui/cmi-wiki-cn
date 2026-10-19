---
title: World
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/world
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# World {#world}

## 说明 {#description}

检查目标世界的名称。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| world | w | 要检查的世界列表。 | tutorial_world |

## 示例 {#examples}

```yaml
  Conditions:
  - world{w=tutorial_world} true
```

```yaml
  Conditions:
  - world{w=world1,world2} true
```
