---
title: Damage Amount
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DamageAmount
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Damage Amount {#damage-amount}

## 说明 {#description}

若技能树源自 [onDamaged 触发器](../triggers/ondamaged.md)或 [onDamaged 光环](../mechanics/ondamaged.md)，检查实体受到的伤害量是否在范围内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| damageAmount | amount, a | 要检查的伤害范围。 | >0 |

## 示例 {#examples}

```yaml
  Conditions:
  - damageamount{amount=>10} true
```
