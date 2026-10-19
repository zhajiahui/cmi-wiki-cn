---
title: Damage
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Damage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Damage {#damage}

## 说明 {#description}

对目标实体造成伤害。

## 属性 {#attributes}

### 不可继承的属性 {#non-inheritable-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 要造成的伤害量。 | 1 |

### 可继承的属性 {#inheritable-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ignoreArmor | ia, i | 是否忽略护甲；计算总伤害时仍会使用附魔修饰符。 | false |
| preventknockback | pkb, pk | 是否防止击退。 | false |
| preventimmunity | pi | 是否在造成伤害后将目标的[伤害无敌刻数](setnodamageticks.md)设为 0，从而禁用该无敌时间。 | false |
| damagecause | dc, cause | 为此伤害机制设置伤害来源，此选项仅适用于 1.17+。 | entity_attack |
| ignoreenchantments | ignoreenchants, ie | 计算总伤害时是否忽略附魔，此选项仅适用于 1.19+。 | false |
| noanger | na | 对实体造成伤害时是否产生愤怒值。 | false |
| ignoreinvulnerability | ignoreinvulnerable, ii | 是否在造成伤害前将目标的[伤害无敌刻数](setnodamageticks.md)设为 0，从而忽略该无敌时间。 | false |
| ignoreshield | is | 是否忽略目标的盾牌格挡。 | false |
| damageshelmet | dh | 是否损耗头盔耐久。 | false |
| ignoreeffects | ieff | 是否忽略效果。 | false |
| ignoreresistance | ir | 是否忽略抗性。 | false |
| poweraffectsdamage | pad | 技能威力是否影响造成的伤害。 | true |
| tags | tag | 可使用 `tags=THIS,THAT` 为机制指定任意数量的标签。所有添加的标签都会转换为大写，因此检查标签时应始终使用大写名称。 |  |
| rawtags | rtag | 作用与 tags 相同，此处内容也会被视为标签，但不会像 tags 那样转换为大写。 |  |
| damagetype | element, e | *成为其中一个标签* |  |
| triggerSkills | ts | 伤害机制是否也可以触发与 `onAttack` 相关的触发器。 | false |
| bonusdamage |  | 要造成的额外伤害，格式为 `FIRE 5,LIGHTNING 5`。 |  |
| bonusdamagemodifiers | bonusdamagemods | 将对应的额外伤害乘以指定数值。例如，要将前述伤害翻倍，可使用 `FIRE 2,LIGHTNING 2`。 |  |

### DamageCause 属性 {#damagecause-attribute}

此属性仅在较新的 MM 5.0 构建中可用。全部可用伤害原因见 [Spigot Javadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。

注意：只有 `entity_attack`、`entity_sweep_attack`、`thorns`、`sonic_boom`、`entity_explosion` 和 `projectile` 会返回造成伤害的实体，也就是说，这些情况下 `<trigger.name>` 不会返回 "Unknown"。

### Element 属性 {#element-attribute}

如上所示，伤害机制提供了为伤害设置“元素”的能力，如下所示：

```yaml
- damage{amount=10;element=FIRE} @target ~onUse
- damage{amount=10;element=ICE} @target ~onUse
```

该元素可以命名为任何名称，并且可以在生物的DamageModifiers中使用，以根据需要改变对伤害类型的抵抗力：

```yaml
DamageModTest: 
  Type: COW 
  DamageModifiers:
  - LIGHTNING 0.1
  - FIRE 2.0
  - AIR 1.0
  - ICE 0.5 
  Skills:
  - message{m="Damaged by <skill.var.damage-type> for <skill.var.damage-amount>"} @PIR{r=50} ~onDamaged
```

这些选项也可以在“onDamaged”光环中使用，使用`damageMods="FIRE 0.5"`属性。

### Tags 属性 {#tags-attribute}

```yaml
- damage{amount=5;tags=WITCHCURSE,FIRE}
```

可为此类伤害添加任意所需标签，与 [DamageTag](../conditions/damagetag.md) 条件配合使用。

标签是任意的，因此可以具有任何名称，只要不包含无效字符即可。

## 示例 {#examples}

```yaml
  Skills:
  - damage{amount=20;ignoreArmor=true} @target ~onTimer:20
```

```yaml
FreezeBlast:
  Skills:
  - effect:sound{s=block.fire.extinguish;v=1;p=0.5} @PIR{r=6}
  - effect:particles{p=explode;a=8;vs=0.5;hs=0.5;s=0;y=1;repeat=5;repeatInterval=20} @PIR{r=6}
  - effect:particles{p=drip_water;a=10;vs=0.5;hs=0.5;s=0;y=1;repeat=5;repeatInterval=20} @PIR{r=6}
  - potion{t=SLOW;d=120;l=6} @PIR{r=6}
  - damage{a=120;pkb=true} @PIR{r=6}
```

更复杂地使用 **damage** 机制可以制造冰系攻击效果。如上例，通过粒子和重复间隔产生持续冰霜，再施加等级 7 的缓慢（移动速度 -105%），让目标看似冻结。此外，该机制会对 6 格内的玩家造成 120 点伤害（60 颗心）。

##  {#section}

**高级示例**

```yaml
  Skills:
  - damage{amount=<caster.var.somevariable> * 0.5 + 1} @target ~onTimer:20
```

上述技能造成“<caster.var.somevariable> * 0.5 + 1”伤害，如果变量：<caster.var.somevariable>的值为5，则该机械链将造成3.5伤害

## 别名 {#aliases}

- d
