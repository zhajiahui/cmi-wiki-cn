---
title: 数学运算
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Math
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 数学运算 {#math}

可用于简单或复杂的计算，支持所有返回数值的占位符。大多数支持占位符的位置也支持数学运算。

1. [运算符](math.md#operators)
   1. [数学运算符](math.md#math-operators)
   2. [布尔运算符](math.md#boolean-operators)
2. [函数](math.md#functions)
3. [用法示例](math.md#example-usage)

## 运算符 {#operators}

这些运算符大多可在此处查到：<https://www.objecthunter.net/exp4j/#Built-in_operators>

### 数学运算符 {#math-operators}

| 运算符 | 说明 | 示例 |
| --- | --- | --- |
| + | 一元加号 | 2 + 2 |
| - | 一元减号 | 2 - 2 |
| * | 乘法 | 2 * 2 |
| / | 除法 | 2 / 2 |
| ^ | 乘方 | 2 ^ 2 |
| % | 余数 | 2 % 2 |

### 布尔运算符 {#boolean-operators}

| 运算符 | 说明 | 示例 |
| --- | --- | --- |
| < | 小于 | 2<5 |
| <= | 小于或等于 | 2<=5 |
| > | 大于 | 5>1 |
| >= | 大于或等于 | 5>=0 |
| == | 等于 | 0==0 |

*表达式为 true 时，布尔运算符返回 `1`；为 false 时返回 `0`。*

## 函数 {#functions}

这些函数大多可在此处查到：<https://www.objecthunter.net/exp4j/#Built-in_functions>

| 函数 | 说明 |
| --- | --- |
| abs(x) | (x) 的绝对值 |
| acos(x) | 反余弦 |
| asin(x) | 反正弦 |
| atan(x) | 反正切 |
| cbrt(x) | 立方根 |
| ceil(x) | 向上取整到最近的整数 |
| cos(x) | 余弦 |
| csch(x) | 双曲余割 |
| exp(x) | 欧拉数的幂 (e^x) |
| floor(x) | 向下取整到最近的整数 |
| log(x) | 自然对数（以 e 为底） |
| log2(x) | 以 2 为底的对数 |
| log10(x) | 以 10 为底的对数 |
| logb(x) | 以 b 为底的对数 |
| sec(x) | 正割 |
| sech(x) | 双曲正割 |
| sin(x) | 正弦 |
| sinh(x) | 双曲正弦 |
| sqrt(x) | 平方根 |
| tan(x) | 正切 |
| tanh(x) | 双曲正切 |
| signum(x) | 数值的符号 |
| toradian(x) | 将角度转换为弧度 |
| todegree(x) | 将弧度转换为角度 |
| min(x, y) | 最小值 |
| max(x, y) | 最大值 |
| atan2(y, x) | y/x 的反正切主值，以弧度表示。 |
| random(min, max) | 在指定上下限内生成随机值。 |
| clamp(value, min, max) | 将数值限制在给定的最小值和最大值之间。小于最小值时返回最小值；大于最大值时返回最大值；位于两者之间时原样返回。 |

注意：如需新增运算符或函数，可以在我们的 [问题页面](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/issues) 提交建议工单。

## 使用示例 {#example-usage}

```yml
MyCoolMob:
  Type: HUSK
  AIGoalSelectors:
    - clear
  AITargetSelectors:
    - clear
  Skills:
    - skill{s=[
      - setvar{var=skill.test;type=FLOAT;val="<caster.hp> <= <caster.mhp>"} #returns 1 or 0 if the mob's health is less than or equal to its max health
      - message{m=<skill.var.test>} #sends the player a message to see the value
      ]} @trigger ~onInteract
```

```yml
MyCoolItem:
  Id: STICK
  Skills:
    - skill{s=[
        - setvar{var=skill.test;type=FLOAT;val="1>=0"} #returns 1 since the expression evaluates to true
        - message{m=<skill.var.test>} #sends the player a message to see the value
      ]} @Self ~onUse
```
