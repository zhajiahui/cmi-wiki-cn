---
title: 攻击
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/offense
source_snapshot: '2026-10-19'
---

# 攻击 {#⚔️-offense}

## 对实体造成伤害 {#deal-damage-to-an-entity}

对所提供的实体造成伤害。这适用于on-hit效果、暴击、伤害减免...（与MMOItems和MMOCore完全兼容）。

|参数|别名 |描述 |默认 |
| --- | --- | --- | --- |
| amount | amt, a, damage, dmg, d, value, val, v | 造成的伤害量。 | - |
| knockback | kb, knock | 如果true，则将击退应用于目标。 | true |
| ignore_immunity | ii | 如果是true，则忽略目标的无敌帧。 | false |
| damage_type | dtype, dt | 要造成的伤害类型。用逗号分隔损坏类型且不包含空格。查看可用的损坏类型[此处](../../features/damage.md)。 | magic,skill |
| element | - | 处理伤害的元素名称。查看可用元素[此处](../../features/elements.md) | none |
| target | - | 要造成伤害的一个或多个目标实体。 | target or caster |

```yml
example_script:
  mechanics:
  - 'damage{amount="100 * (1 + <modifier.extra> / 100)";dtype="PHYSICAL,WEAPON";kb=true;ii=false;element=FIRE;target={type=nearby_entities;radius=3}}'
```

## 乘以当前的攻击伤害 {#multiply-the-current-attack-damage}

将当前攻击伤害乘以给定量。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| value | val, v, amount, amt, a, scalar, s, coef, c | 伤害乘以的金额。可以是一个表达式。 | - |
| damage_type | dtype, dt | 要修改的损坏类型。查看可用的损坏类型[此处](../../features/damage.md) | none |
| additive | - | 如果true，该伤害增益将与其他增益增益叠加。 | false |
| element | - | 要修改的元素名称。查看可用元素[此处](../../features/elements.md) | none |

如果未提供损坏类型，则修改整个攻击伤害。否则，只有给定伤害类型造成的攻击的特定部分受到影响。如果提供了元素名称，则只有该特定元素造成的损害才会受到影响。

你不能同时提供元素和损坏类型。提供元素名称时，损坏类型参数将被忽略。

如果`additive`设置为`true`，则该伤害增益将与属性叠加，如PvE伤害、不死伤害（叠加i.e`10% + 10% <=> +20%`）。否则，增益会以几何方式叠加i.e`110% * 110% = 121% <=> +21%`。

```yml
example_script:
  mechanics:
  - 'multiply_damage{amount="1 + <modifier.extra> / 100";damage_type=PHYSICAL;element=FIRE;additive=false}
```

## 应用药水效果 {#apply-potion-effect}

在给定的持续时间和给定的等级下，为目标实体提供药水效果。药水效果名称可在 [Spigotjavadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)上找到。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| effect | eff, e, pe | 起效药水名称 | - |
| duration | dur, d, ticks, t, time | 药水效果的持续时间，单位为刻（tick）。 | - |
| level | lvl, l | 药水效果等级（0= 等级1、1= 等级2等） | 0 |
| ambient | amb | 如果true，药水效果将为环境效果。 | false |
| particles | part | 如果为false，药水效果将没有粒子。 | true |
| icon | ic | 如果是false，药水效果将没有图标。 | true |
| target | - | 要着火的目标实体。 | target or caster |

```yml
example_script:
  mechanics:
  - 'potion{type=INCREASE_DAMAGE;level=5;duration=80;ambient=true;particles=false;icon=true;target=caster}'
```

## 去除药水效果 {#remove-potion-effect}

取消目标实体的药水效果。药水效果名称可在 [Spigotjavadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)上找到。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| effect | eff, e, pe | 起效药水名称 | - |
| target | - | 要着火的目标实体。 | target or caster |

```yml
example_script:
  mechanics:
  - 'remove_potion{effect=slowness;target=caster}'
```

## 放火烧 {#set-on-fire}

让目标实体着火一段时间（以刻为单位）。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| ticks | t, duration, dur, d, time | 使实体着火的时间量（以刻为单位）。 | - |
| stack | add | 如果是true，则将提供的刻添加到实体的当前火刻中，而不是设置它。 | false |
| max | - | 如果true，则取当前触发刻和提供的刻之间的最大值。 | false |
| min | - | 如果true，则取当前触发刻和提供的刻之间的最小值。 | false |
| target | - | 要着火的目标实体。 | target or caster |

`stack`优先于`max`和`min`，`max`优先于`min`。

```yml
example_script:
  mechanics:
  - 'set_on_fire{ticks=20;stack=false;max=false;min=false;target=target}'
```

## 设置无伤害刻 {#set-no-damage-ticks}

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| ticks | t, duration, dur, d, time | 刻的无敌持续时间 | 10 |
| stack | add | 如果是true，则将提供的刻添加到实体的无损坏刻中，而不是设置它。 | false |
| max | - | 如果true，则取当前无损坏刻和提供的刻之间的最大值。 | false |
| min | - | 如果true，则取当前无损坏刻和提供的刻之间的最小值。 | false |
| target | - | 目标实体 | target or caster |

使目标实体在指定的时间内（以刻为单位）无敌。

```yml
example_script:
  mechanics:
  - 'set_no_damage_ticks{target=caster;ticks="40 + 20 * <modifier.extra>"}'
```

---

原文：[⚔️ Offense](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/offense) · 原文归档：2026-10-19
