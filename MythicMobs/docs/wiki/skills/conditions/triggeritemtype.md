---
title: Trigger Item Type
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/TriggerItemType
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Trigger Item Type {#trigger-item-type}

## 说明 {#description}

检查触发技能的物品材料类型。仅适用于特定的[触发器](../triggers.md)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, items, item, i | 用于检查的[材质](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)列表。 | DIRT |

## 示例 {#examples}

```yaml
  Conditions:
  - triggeritemtype{mat=STONE,DIRT,STONE_SWORD} true
```

## 别名 {#aliases}

- triggeringItemType
