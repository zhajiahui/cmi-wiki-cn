---
title: Variableequals
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/variableequals
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variableequals {#variableequals}

## 说明 {#description}

检查[变量](../variables.md)值的条件。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | 变量名称，可以在前面加上作用域。 |  |
| value | val, v | 变量必须等于此值才返回 true。此值必须适用于对应类型，否则机制会失败。包含空格时应使用双引号括起来。值也可以包含占位符，包括 PlaceholderAPI 占位符。 |  |
| scope | s | 变量的[作用域](../variables.md#variable-scopes)，即变量所在的位置。 |  |

## 示例 {#examples}

在这个例子中，目标玩家每10分钟只会听到附近任意数量的熊的咆哮声。

```yaml
BearMob:
  Skills:
  - skill:BearGrowl @PlayersInRadius{r=40} ~onTimer:60
```

```yaml
BearGrowl:
  TargetConditions:
  - variableEquals{var=target.heardbear;value="yes"} cancel
  Skills:
  - message{m="&7You hear a growling noise..."}
  - setvariable{var=target.heardbear;value="yes";duration=6000}
```

在此示例中，仅当全局变量“poison_storm”设置为  true  时，该技能才会触发。

```yaml
PoisonStormDamage:
  Conditions:
  - varEquals{var=global.poison_storm;value="yes"}
  Skills:
  - potion{type=POISON;duration=100}
  - damage{amount=1;ignorearmor=true}
```

## 别名 {#aliases}

- variableeq
- varequals
- vareq
