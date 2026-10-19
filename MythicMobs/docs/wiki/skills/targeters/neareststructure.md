---
title: Nearest Structure
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/NearestStructure
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Nearest Structure {#nearest-structure}

## 说明 {#description}

选中施法者所在世界中，指定半径内最近的指定类型结构

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 结构类型。 | STRONGHOLD |
| radius | r | 目标选择器的半径。 | 5000 |
| unexplored | u | 结构是否必须尚未被探索。 | false |

## 示例 {#examples}

```yaml
StrongholdFinder:
  Cooldown: 10
  Skills:
  - projectile{hp=false;se=false;sb=false;v=5;d=100;onTick=[ effect:particles ]} @NearestStructure{r=1000}
```
