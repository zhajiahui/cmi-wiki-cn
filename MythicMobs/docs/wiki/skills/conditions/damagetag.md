---
title: Damagetag
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/damagetag
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Damagetag {#damagetag}

## 说明 {#description}

检查造成当前技能树的伤害是否有特定标签

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| tag | t | 用于检查的标签。 |  |
| value | val, v, b, bool, boolean | 为 true 时检查标签是否存在；为 false 时检查标签是否不存在。 | true |

## 示例 {#examples}

```yaml
Conditions:
- damageTag{tag=WITCHCURSES}
```

用于检查[伤害](../mechanics/damage.md)机制或继承其属性的机制中指定的伤害标签

## 别名 {#aliases}

- damagehastag
