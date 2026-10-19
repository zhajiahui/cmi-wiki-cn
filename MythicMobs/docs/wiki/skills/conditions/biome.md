---
title: Biome
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/biome
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Biome {#biome}

## 说明 {#description}

此条件测试目标是否在给定的生物群落列表内。   如果没有提供命名空间，则默认为`minecraft:`

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| biome | b | 要检查的生物群系列表。 | minecraft:plains |
| exact | e | 是否精确匹配生物群系。 | true |

## 示例 {#examples}

```yaml
Conditions:
- biome{b=minecraft:plains,river} true
```

如果使用自定义生物群落（例如来自数据包），你可以使用命名空间键来定义它，如下所示：

```yaml
Conditions:
- biome{b=far_end:void,far_end:warped_marsh} true
```
