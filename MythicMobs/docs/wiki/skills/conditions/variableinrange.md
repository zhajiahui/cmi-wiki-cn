---
title: Variableinrange
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/variableinrange
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Variableinrange {#variableinrange}

## 说明 {#description}

检查给定的数值变量是否在特定范围内。

使用`<skill.var.index>`获取目标的当前索引（从0开始）。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | 要匹配的变量，可以在前面加上作用域。 |  |
| value | val, v, range, r | 要匹配的数值范围。 |  |
| scope | s | 变量的[作用域](../variables.md#variable-scopes)，即变量所在的位置。 |  |

## 示例 {#examples}

```yaml
ShootCheck:
  Cooldown: 0
  Conditions:
  - variableInRange{var=caster.shootsLeft;value=>0} castInstead ShootThemUp
  Skills:
  - message{m="&7Reloading..."} @self
  - delay 0
  - setskillcooldown{skill=ShootCheck;seconds=2} @self
  - delay 20
  - setvariable{var=caster.shootsLeft;value=10} @self
  - message{m="&7Reloaded!"} @self
```

## 别名 {#aliases}

- varinrange
- varrange
