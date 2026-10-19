---
title: Onblock
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/onblock
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Onblock {#onblock}

## 说明 {#description}

匹配目标实体所站立的方块。   可用材料列表可以在 [Spigot Javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) 上找到

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | types, type, t, mat, m, block, b | 材质列表。找到其中任意一种材质时，条件即成立。也支持通配符和方块标签。 | STONE |

## 示例 {#examples}

```yaml
  TargetConditions:
  - onblock{m=BEDROCK,OAK_LEAVES,ACACIA_FENCE} false
```

```yaml
  TargetConditions:
  - onblock{m=DIRT,STONE,GRAVEL} true
```
