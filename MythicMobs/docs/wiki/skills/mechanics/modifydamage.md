---
title: Modify Damage
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ModifyDamage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Modify Damage {#modify-damage}

## 说明 {#description}

修改触发技能的伤害事件。   该机制必须同步，这意味着该机制或调用它的初始技能必须使用`sync=true`属性运行。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 运算使用的数值。 | 1 |
| damagetype | type, dt, t | 要评估的伤害类型。 | ALL |
| action | mod, m | 要使用的[修饰符](../../stats.md#modifiers)。 | ADD |

## 示例 {#examples}

```yaml
  Skills:
  - modifyDamage{a=2;action=ADDITIVE_MULTIPLIER;sync=true} @self ~onAttack 0.2
```

## 别名 {#aliases}

- modDamage
