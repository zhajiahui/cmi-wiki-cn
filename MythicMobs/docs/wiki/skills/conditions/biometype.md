---
title: Biometype
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/biometype
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Biometype {#biometype}

## 说明 {#description}

测试目标是否在给定的生物群落类型列表内

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 要检查的生物群系列表。 | ocean |
| exact | e | 是否精确匹配类型。 | true |

## 示例 {#examples}

```yaml
Conditions:
- biometype{t=jungle,ocean,extreme_hills} true
```

## 生物群系类型 {#biome-types}

- none
- taiga
- extreme_hills
- jungle
- mesa
- plains
- savanna
- icy
- the_end
- beach
- forest
- ocean
- desert
- river
- swamp
- mushroom
- nether
- underground
- mountain

## 别名 {#aliases}

- biomecategory
