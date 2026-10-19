---
title: Heal
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/heal
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Heal {#heal}

## 说明 {#description}

治疗目标实体指定的值。还可以“过度治疗”生物，使其超过其最大生命值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 对目标的治疗量。 | 1 |
| overheal | oh | 是否将过量治疗作为额外 MaxHealth 应用。 | false |
| maxoverheal | maxabsorb, maxshield, mo, ma, ms | 可应用的最大过量治疗量。 | 1 |
| tags | tag | 可使用 `tags=THIS,THAT` 为机制指定任意数量的标签。所有添加的标签都会转换为大写，因此检查标签时应始终使用大写名称。 |  |
| rawtags | rtag | 作用与 tags 相同，此处内容也会被视为标签，但不会像 tags 那样转换为大写。 |  |

### Tags 属性 {#tags-attribute}

```yaml
- heal{amount=5;tags=BLESSING,PALADIN}
```

这允许你在这种类型的治疗上设置任何你想要的标签，以与 [DamageTag](../conditions/damagetag.md) 条件一起使用。

标签是任意的，因此可以具有任何名称，只要不包含无效字符即可。   你可以为每个治疗机制设置无限数量的标签。

## 示例 {#examples}

当施法生物受到伤害时，可以治疗其20生命值（10心）。 （20% 几率）

```yaml
  Skills:
  - heal{amount=20} @self ~onDamaged 0.2
```

##  {#section}

当施法生物受到伤害时，可以治疗其20生命值（10心）。 （20% 几率）

```yaml
  Skills:
  - heal{amount=20;overheal=true} @self ~onDamaged 0.2
```

如果生物接近满生命值或已满生命值，这 20 点生命值会直接加到当前生命值上。例如，原有 20 点生命值的生物使用此技能后会有 40 点生命值：20/20 + 20 = 40/20

具有 17 生命值的同一生物将在其最大生命值之上获得 17 生命值
20. 17/20 + 20 = 37/20

## 别名 {#aliases}

- h
