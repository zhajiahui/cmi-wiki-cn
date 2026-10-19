---
title: StatDamageModifier
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/StatDamageModifier
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# StatDamageModifier {#statdamagemodifier}

## 说明 {#description}

用于属性触发器，检查伤害的增加量，以倍率表示，可用于区分正面和负面效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value | v, amount, a, damage, d, multiplier, m | 要检查的最小倍率，默认为 1。倍率大于此值时返回 true。 | 1 |

## 示例 {#examples}

```yaml
  Conditions:
  - statDamageModifier{m=1.01) castInstead positiveEffectSkill
  - statDamageModifier{m=0.99) orElseCast negativeEffectSkill
```

## 别名 {#aliases}

- statDamage
