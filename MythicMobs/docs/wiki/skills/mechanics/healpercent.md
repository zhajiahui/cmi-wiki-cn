---
title: Healpercent
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/healpercent
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Healpercent {#healpercent}

## 说明 {#description}

治疗目标实体最大生命值的一定百分比。与治疗技能一样，也可以按一定比例过度治疗生物。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| multiplier | m, amount, a | 相对于目标最大生命值的治疗比例。0.1 = 10%，1 = 100%，以此类推。 | 0.1 |
| overheal | oh | 是否将过量治疗作为额外 MaxHealth 应用。 | false |
| maxoverheal | maxabsorb, maxshield, mo, ma, ms | 可应用的最大过量治疗量。 | 0 |
| tags | tag | 可使用 `tags=THIS,THAT` 为机制指定任意数量的标签。所有添加的标签都会转换为大写，因此检查标签时应始终使用大写名称。 |  |
| rawtags | rtag | 作用与 tags 相同，此处内容也会被视为标签，但不会像 tags 那样转换为大写。 |  |

### Tags 属性 {#tags-attribute}

```yaml
- healpercent{amount=0.5;tags=BLESSING,PALADIN}
```

这允许你在这种类型的治疗上设置任何你想要的标签，以与 [DamageTag](../conditions/damagetag.md) 条件一起使用。

标签是任意的，因此可以具有任何名称，只要不包含无效字符即可。

## 示例 {#examples}

这将使施法生物在每次攻击时恢复 20% 的生命值。

```yaml
  Skills:
  - healpercent{m=0.2} @self ~onAttack
```

## 别名 {#aliases}

- percentheal
- hp
