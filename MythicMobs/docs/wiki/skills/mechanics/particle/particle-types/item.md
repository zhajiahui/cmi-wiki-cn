---
title: Item
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Item
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Item {#item}

## Particle {#particle}

![img](../../../../assets/c71783896641a7.gif)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | itemstack 粒子所使用的材质。 | STONE |

> 该粒子具有 [Itemstack](../particle-types.md#itemstack) 数据类型，并继承其所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particle{p=item;material=STONE}
```

## 别名 {#aliases}

- item_crack
- icon_crack
- itemcrack

> 该粒子在1.20.5之前的版本中具有不同的名称
>

> - item_crack
