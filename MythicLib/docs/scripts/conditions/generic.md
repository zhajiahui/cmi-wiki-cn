---
title: 通用条件
source: https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/generic
source_snapshot: '2026-10-19'
---

# 通用条件 {#generic}

## 表达检查 {#expression-check}

使用此条件执行算术和布尔计算。你可以使用 PAPI 中的占位符返回`true`或`false`以及逻辑运算符（否定`!`或`||`和`&&`），并且MythicLib将解析和计算布尔公式的结果。

这可用于同时比较多个数字，例如使用`(a < b) && (c >= d)`。括号不是强制性的，但有助于提高可读性。你可以在公式的不同部分之间添加任意多个空格，以提高清晰度。

|参数|别名 |描述 |默认 |
| --- | --- | --- | --- |
| formula | form, f, expression, expr, e | 要评估的布尔公式。 | - |

```yml
condition_generic_1:
  conditions:
  - 'boolean{formula=" (%mmocore_in_combat% || %mmocore_in_combat%) && true"}'
  mechanics:
  - 'message{format="You are in combat!"}'

condition_generic_2:
  conditions:
  - 'boolean{formula="(<caster.health> <= 10 && <caster.health> > 5) || (!%mmocore_in_combat%)"}'
  mechanics:
  - 'message{format="Condition met!"}'
```

## 有变量 {#has-variable}

检查变量是否存在。这也可以用于保留变量，如`target`或`target_location`。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| variable | var, v, name, n | 要检查的变量的名称。 | - |

```yml
condition_has_variable:
  conditions:
  - 'has_variable{var=target_location}'
  mechanics:
  - 'message{format="The variable target_location exists!"}'
```

## 字符串包含 {#string-contain}

使用此条件检查某个字符串是否包含另一个字符串。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| within | in | 在此字符串中搜索。 | - |
| search | lookfor, look, lf | 要搜索的字符串。 | - |
| ignore_case | ic | 比较字符串时是否忽略大小写。 | false |

此示例脚本检查目标实体是僵尸还是骷髅。

```yml
condition_string_contain:
  conditions:
  - 'string_contains{in="ZOMBIE,SKELETON";look="<target.type>"}'
  mechanics:
  - 'message{format="Target is either a Zombie or a Skeleton!"}'
```

## 字符串匹配 {#string-match}

使用此条件检查两个字符串是否完全匹配。

| Parameter | Alias | 描述 | Default |
| --- | --- | --- | --- |
| first | one, left, lhs | 第一个字符串。 | - |
| second | two, right, rhs | 第二根弦。 | - |
| ignore_case | ic | 比较字符串时是否忽略大小写。 | false |

这会检查玩家是否在某个世界中：

```yml
condition_string_eq:
  conditions:
  - 'string_equals{first="<target.location.world.name>";second="spawn"}'
  mechanics:
  - 'message{format="You are in the spawn world!"}'
```

---

原文：[Generic](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/generic) · 原文归档：2026-10-19
