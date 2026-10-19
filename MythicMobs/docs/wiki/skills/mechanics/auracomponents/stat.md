---
title: Stat
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/Stat
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Stat {#stat}

## 说明 {#description}

将 [aura](../aura.md) 组件应用于目标，并对其应用特定的 [stat](../../../stats.md)。   收到的增益效果乘以光环的层数

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| stat | s | 要应用的[属性](../../../stats.md)。 |  |
| type | t, modifier, mod, m | 要使用的[属性修饰符](../../../stats.md#modifiers)。 | ADDITIVE |
| value | val, v | 用于此属性的数值。 | 0.0 |

## 示例 {#examples}

下面的光环让施法者的暴击率翻倍，持续 5 秒。

```yaml
  Skills:
  - aura{auraName=exampleaura;d=100;components=[
    - stat{stat=CRITICAL_STRIKE_CHANCE;type=COMPOUND_MULTIPLIER;val=2}
    ]} @self
```

## 别名 {#aliases}

- stataura
- stats
