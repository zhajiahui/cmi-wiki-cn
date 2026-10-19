---
title: Blocktype
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/blocktype
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Blocktype {#blocktype}

## 说明 {#description}

检查目标位置的材质是否属于指定类型。支持任意 [Bukkit 材质类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html)、通配符和方块标签。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, block, b | 要检查的材质或 MMOItem 方块名称列表。也支持通配符和方块标签。 | DIRT |

## 示例 {#examples}

```yaml
  Conditions:
  - blocktype{type=dirt} true
```

```yaml
  Conditions:
  - blockType{type=#leaves,*_log,redstone_torch[lit=true]}
```

## 别名 {#aliases}

- inblock
- insideblock
