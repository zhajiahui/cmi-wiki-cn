---
title: 变量
source: https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/variables
source_snapshot: '2026-10-19'
---

# 变量 {#🧮-variables}

> **警告**
>
> 建设中

**请先了解变量** [**此处**](../variables.md)。由于变量具有作用域，因此每次编辑或初始化变量时，都必须使用`scope`选项提供变量作用域。默认情况下，它始终设置为`SKILL`。

## 其他变量 {#other-variables}

始终有一种机制可用于初始化和编辑变量的当前值。

### 初始化/编辑带小数的数字（双精度） {#initialize-edit-a-number-with-decimals-a-double}

```
example_mechanic:
    type: set_double
    variable: variable_name
    scope: SKILL
    value: '<target.attribute.max_health> - <caster.attribute.max_health>'
```

### 初始化/编辑整数 {#initialize-edit-an-integer}

`value`选项中提供的公式可以返回双精度值，但由于它是整数变量，ML 会将返回的数字四舍五入为最接近的较低整数。

```
example_mechanic:
    type: set_integer
    variable: variable_name
    scope: SKILL
    value: '<target.attribute.max_health> - <caster.attribute.max_health>'
```

### 初始化/编辑字符串变量 {#initialize-edit-a-string-variable}

这会将脚本施法者的世界名称保存在变量中。

```
example_mechanic:
    type: set_string
    variable: variable_name
    scope: SKILL
    value: '<caster.location.world.name>'
```

### 初始化/编辑向量 {#initialize-edit-a-vector}

```
example_mechanic:
    type: set_vector
    variable: variable_name
    scope: SKILL
    x: '10 + <caster.location.x>'
    y: '10 + <caster.location.y>'
    z: '10 + <caster.location.z>'
```

## 矢量计算机制 {#vector-calculation-mechanics}

在MythicLib中，位置、位置、向量的处理方式相同。为了使脚本创建更加容易，已经实现了以下机制： ML 提供了一小部分用于矢量计算的基本/更复杂的机制。

### 向量加法 {#vector-addition}

使用它将一个向量（存储在变量中）添加到另一个向量（存储在另一个变量中）。

```
example_mechanic:
    type: add_vector
    variable: variable_name
    scope: SKILL
    added: added_vector_variable_name
```

你还可以使用它将 x、y、z 坐标分别添加到现有向量变量：

```
example_mechanic:
    type: add_vector
    variable: variable_name
    scope: SKILL
    x: '10'
    y: '4'
    z: '-7'
```

### 复制/重复向量 {#copy-duplicate-vector}

将现有向量（名称由`copied`选项指定）复制到另一个变量（名称由`variable`选项指定）。`scope`选项对应于创建的新变量的范围。

```
example_mechanic:
    type: copy_vector
    variable: vector_variable_name
    scope: SKILL
    copied: copied_var_name
```

### 向量点积 {#vector-dot-product}

计算向量`vec1`和`vec2`的点积并将其保存在变量中。结果是一个十进制数（双精度）。

```
example_mechanic:
    type: dot_product
    variable: saved_variable_name
    scope: SKILL
    vec1: first_vector_variable_name
    vec2: second_vector_variable_name
```

这是完全等价的：

```
example_mechanic:
    type: set_double
    variable: variable_name
    scope: SKILL
    value: '<var.vec1.x> * <var.vec2.x> + <var.vec1.y> * <var.vec2.y> + <var.vec1.z> * <var.vec2.z>'
```

### 将向量乘以常数 {#multiply-vector-by-a-constant}

将向量的 X、Y 和 Z 坐标乘以相同的常数。

```
example_mechanic:
    type: multiply_vector
    variable: vector_variable_name
    scope: SKILL
    coef: '3.14159'
```

### 标准化向量 {#normalize-a-vector}

这需要一个向量并使其长度为1（本质上是除以它自己的长度），这在处理描述方向的向量时很有用。

```
example_mechanic:
    type: normalize_vector
    variable: vector_variable_name
    scope: SKILL
```

### 设置向量的 X/Y/Z 坐标 {#set-x-y-z-coordinate-of-a-vector}

机械师名称为`set_x`、`set_y`和`set_z`。以下机制将变量`knockback`中向量的 Y 坐标设置为0。

```
example_mechanic:
    type: set_y
    variable: knockback
    scope: SKILL
    z: 0
```

### 矢量减法 {#vector-subtraction}

从一个向量中减去另一个向量。用它来减去存储在变量中的向量：

```
example_mechanic:
    type: subtract_vector
    variable: edited_var_name
    scope: SKILL
    subtracted: other_var_name
```

你还可以单独减去 X、Y 和 Z 坐标，这与添加相反坐标具有相同的效果。

```
example_mechanic:
    type: subtract_vector
    variable: edited_var_name
    scope: SKILL
    x: -4
    y: 0
    z: 10
```

## 复杂矢量力学 {#complex-vector-mechanics}

### 向量叉积 {#vector-cross-product}

计算向量`vec1`和`vec2`的叉积并将其保存在变量中。结果是另一个向量。

```
example_mechanic:
    type: cross_product
    variable: saved_variable_name
    scope: SKILL
    vec1: first_vector_variable_name
    vec2: second_vector_variable_name
```

### 矢量哈达玛积 {#vector-hadamard-product}

这将两个向量的 X、Y 和 Z 坐标分别相乘，并将结果保存在变量中。结果是另一个向量。

```
example_mechanic:
    type: hadamard_product
    variable: saved_variable_name
    scope: SKILL
    vec1: first_vector_variable_name
    vec2: second_vector_variable_name
```

---

原文：[🧮 Variables](https://docs.phoenixdevt.fr/mythiclib/scripts/mechanics/variables) · 原文归档：2026-10-19
