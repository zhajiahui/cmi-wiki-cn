---
title: Dimension
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/dimension
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Dimension {#dimension}

## 说明 {#description}

检查目标是否在特定维度内。   有效维度的列表可以在 [Spigot Enviroment javadoc](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/World.Environment.html) 中找到。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| dimension | d, environment, env | 要检查的维度列表。 | THE_END |

## 示例 {#examples}

```yaml
  Conditions:
  - dimension{d=NORMAL} true
```

## 别名 {#aliases}

- environment
