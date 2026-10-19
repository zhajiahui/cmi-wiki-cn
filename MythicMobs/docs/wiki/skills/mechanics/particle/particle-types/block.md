---
title: Block
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Block
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block {#block}

## Particle {#particle}

![img](../../../../assets/f1ddb4fedbc31f.gif)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m | blockdata 粒子所使用的材质。 | STONE |

> 该粒子具有[Blockdata](../particle-types.md#blockdata)数据类型，并继承其所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particle{p=block_crack;material=STONE}
```

## 别名 {#aliases}

- block_crack
- blockcrack

> 该粒子在1.20.5之前的版本中具有不同的名称
>

> - block_crack
