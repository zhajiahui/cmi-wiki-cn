---
title: Block Crumble
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Block_Crumble
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block Crumble {#block-crumble}

## Particle {#particle}

![img](../../../../assets/20d4ce6d3986e6.svg)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | blockdata 粒子所使用的材质。 | STONE |

> 该粒子具有[Blockdata](../particle-types.md#blockdata)数据类型，并继承其所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particle{p=block_crumble;material=STONE}
```
