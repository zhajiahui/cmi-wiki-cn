---
title: Basedamage
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/basedamage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Basedamage {#basedamage}

## 说明 {#description}

按生物伤害的一定百分比对目标实体造成伤害。继承 [damage](damage.md) 机制的全部属性。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| multiplier | m | 要造成的伤害百分比。 | 1 |
| useAttribute | attribute, attr | 伤害是否使用实体实际的攻击属性，而不是原始基础伤害。 | false |

> 该机制继承了[伤害](damage.md)机制的所有属性
>

> > `amout` 属性被忽略

## 示例 {#examples}

此示例将使生物在受到攻击时对其目标造成 150% 的原始伤害。在这种情况下，它将造成15伤害，因为该生物的基础伤害是10。

```yaml
AMob:
  Type: HUSK
  Damage: 10
  Skills:
  - basedamage{m=1.5} @target ~onDamaged
```

## 别名 {#aliases}

- bd
- weaponDamage
- wd
