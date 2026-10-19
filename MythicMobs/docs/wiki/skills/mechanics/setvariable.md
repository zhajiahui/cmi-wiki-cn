---
title: Setvariable
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setvariable {#setvariable}

## 说明 {#description}

设置一个[变量](../variables.md)。变量可以是永久的或临时的，并且可以与条件或占位符结合使用来存储数据。

> 了解有关设置特殊变量类型的更多信息[此处](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#special-variable-types)

## 属性 {#attributes}

### 可继承的属性 {#inheritable-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | 变量名称，可选择添加 `scope` 前缀 |  |
| scope | s | 变量的[作用域](../variables.md#variable-scopes)，即变量所在的位置 | SKILL |
| save |  | 变量是否在重载、重启和断开连接后保留。不适用于 SKILL 作用域的变量 | false |
| duration | d, e, expire | 变量的持续时间，以刻为单位。不适用于 SKILL 作用域的变量 | 无限 |

### 不可继承的属性 {#non-inheritable-attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value | val, v, amount, a | 要为变量设置的值。必须适用于 `type`，否则机制会执行失败。包含空格或分号时，应使用双引号包裹。值也可包含占位符，包括 PlaceholderAPI 的占位符 |  |
| type | t | 变量的[类型](https://wiki.mythiccraft.io/mythicmobs/skills/variables#variable_types)。使用文本而不是数字时设为 STRING | INTEGER |

## 示例 {#examples}

在这个例子中，目标玩家每10分钟只会听到附近任意数量的熊的咆哮声。

```yaml
# Mob File
BearMob:
  Skills:
  - skill{s=BearGrowl} @PlayersInRadius{r=40} ~onTimer:60
```

```yaml
# Skill File
BearGrowl:
  TargetConditions:
  - variableEquals{var=target.heardbear;value="yes"} cancel
  Skills:
  - message{m="&7You hear a growling noise..."}
  - setvariable{var=target.heardbear;value="yes";type=STRING;duration=6000}
```

##  {#section}

在此示例中，只有在技能树上设置了“do_ignite”变量时，额外的“IgnitionDamage”技能才会触发。

```yaml
Strike:
  Skills:
  - setvariable{var=skill.do_ignite;type=STRING;value="yes"} 0.5
  - damage{amount=20}
  - skill{s=IgnitionDamage}

IgnitionDamage:
  Conditions:
  - varEquals{var=skill.do_ignite;value="yes"}
  Skills:
  - ignite{ticks=20}
  - effects:particles
```

##  {#section-2}

在此示例中，MMOItems 中的占位符存储在 int/float 变量中。

```yaml
PlaceholderDamage:
  Skills:
  - setvariable{var=caster.new_skill_damage;value="%mmoitems_stat_skill_damage%";type=INTEGER} @self
  - damage{a="100 * <caster.var.new_skill_damage>"} @PIR{r=5}
```

##  {#section-3}

其他变量可以存储在 int/float 变量中。

```yaml
VariableSend:
  Skills:
  - setvariable{var=caster.VariableA;value="%mmoitems_stat_skill_damage%";type=INTEGER} @self
  - setvariable{var=caster.VariableB;value="<caster.var.VariableA> * 2";type=INTEGER} @self
  - setvariable{var=caster.VariableC;value="<caster.var.VariableA> + <caster.var.VariableB>";type=INTEGER} @self
```

## 别名 {#aliases}

- setvar
- variableset
