---
title: Entity Effect
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Entity_Effect
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entity Effect {#entity-effect}

## Particle {#particle}

![img](../../../../assets/0b03aae31f0f65.gif)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 粒子的颜色。 | #FF0000 |

> 该粒子具有 [Color](../particle-types.md#color) 数据类型，并继承其所有属性

## 示例 {#examples}

```yaml
  Skills:
  - particle{p=entity_effect;color=#FF0000}
```

## 别名 {#aliases}

- spell_mob
- mob_spell

> 该粒子在1.20.5之前的版本中具有不同的名称
>

> - spell_mob
