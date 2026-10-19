---
title: Set Faction
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setFaction
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Set Faction {#set-faction}

## 说明 {#description}

设置或更改目标生物的阵营。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| faction | f | 要为生物设置的阵营名称 |  |

## 示例 {#examples}

生物生成时，将阵营设置为 Hostile。

```yaml
  Skills:
  - setFaction{faction=Hostile} @self ~onSpawn
```
