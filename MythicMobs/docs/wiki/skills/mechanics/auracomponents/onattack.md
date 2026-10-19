---
title: On Attack
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnAttack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Attack {#on-attack}

## 说明 {#description}

为目标施加光环组件，在目标造成伤害时触发技能，也可以修改伤害事件本身。

| [已实现的占位符](../../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onattackskill | onattack, oa, onmelee, onhitskill, onhit, oh | 目标击中其他对象时执行的[元技能](../../metaskills.md)。 |  |
| cancelEvent | cE, canceldamage, cd | 是否取消触发光环的事件。 | false |
| damageAdd | add, a | 对原始命中伤害增加的固定值，可选。 | 0 |
| damageMultiplier | multiplier, m | 对原始命中伤害应用的倍率，可选。 | 1 |
| modDamageType | damagetype | 造成伤害的[类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。 |  |

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 8h.01"></path></svg>Note

只有 **`onAttackSkill` 成功执行时**，此光环才消耗一次次数，并应用 `cancelEvent`、`damageAdd` 或 `damageMultiplier`。成功表示概率判定通过、未在冷却且全部条件满足。技能失败则不修改伤害事件，也不消耗次数。未配置 `onAttackSkill` 时始终视为成功。

此外，`cancelEvent`优先于修改伤害属性：如果`cancelEvent`是`true`，则命中被取消，`damageAdd`和`damageMultiplier`被忽略。

## 别名 {#aliases}

- onhit
