---
title: Effect
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Effect
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Effect {#effect}

## Particle {#particle}

![img](../../../../assets/f0b70d383410fb.gif)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 粒子的颜色。 | #FF0000 |
| power | p | 法术粒子的威力。 | 1 |

> 该粒子具有 [Spell](../particle-types.md#spell) 数据类型，并继承其所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particle{p=effect;color=#FF0000;power=1}
```

## 别名 {#aliases}

- spell

> 该粒子在1.20.5之前的版本中具有不同的名称
>

> - spell
