---
title: Entity Material Type
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EntityMaterialType
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entity Material Type {#entity-material-type}

## 说明 {#description}

检查目标物品实体的材质。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | mat, m, type, types, t | 要匹配的材质列表。 |  |

## 示例 {#examples}

```yaml
  TargetConditions:
  - entityMaterialType{mat=STONE,DIRT} true
```
