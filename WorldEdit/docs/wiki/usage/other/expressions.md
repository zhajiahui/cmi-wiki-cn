---
title: 表达式语法
source_url: https://worldedit.enginehub.org/en/latest/usage/other/expressions/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 表达式语法 { #expression-syntax }

WorldEdit 表达式解析器的行为与 Java 及相关语言类似，但有一些细微区别：

- 大多数情况下可以省略末尾的分号。

- 即使没有 return 语句，也始终返回序列中的最后一个值。

- 二元中缀运算符 `^` 表示乘方，而不是异或，优先级也作了相应调整。

- 提供后缀阶乘运算符（`!`）。

- 提供二元中缀近似相等运算符（`~=`）。

- 没有对象 :)

<a id="contents"></a>

- [运算符](#operators)



  - [二元中缀](#binary-infix)

  - [前缀](#prefix)

  - [后缀](#postfix)

  - [三元中缀](#ternary-infix)

- [函数](#functions)

- [常量](#constants)

- [语句块](#block-statements)

- [控制结构](#control-structures)



  - [循环](#loops)

## 运算符 { #operators }

表达式解析器使用 [Java 的优先级规则](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html)，但有以下例外和补充：

> - 二元乘方运算符（`^`）的优先级在 2 与 3 之间。
>
> - 后缀阶乘运算符（`!`）的优先级为 2。
>
> - 近似相等运算符（`~=`）的优先级为 7。

### 二元中缀 { #binary-infix }

这些运算符放在两个操作数之间。

算术

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`+`</td>
<td markdown="span">加法</td>
</tr>
<tr>
<td markdown="span">`-`</td>
<td markdown="span">减法</td>
</tr>
<tr>
<td markdown="span">`*`</td>
<td markdown="span">乘法</td>
</tr>
<tr>
<td markdown="span">`/`</td>
<td markdown="span">除法</td>
</tr>
<tr>
<td markdown="span">`%`</td>
<td markdown="span">取余</td>
</tr>
<tr>
<td markdown="span">`^`</td>
<td markdown="span">乘方</td>
</tr>
</tbody>
</table>

按位运算

这些运算符将操作数解释为 32 位整数，并对其中的位进行操作。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`<<`</td>
<td markdown="span">左移</td>
</tr>
<tr>
<td markdown="span">`>>`</td>
<td markdown="span">右移</td>
</tr>
</tbody>
</table>

逻辑

这些运算符将大于零的值视为真，其他值视为假。结果为真时返回 1，为假时返回 0。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`&&`</td>
<td markdown="span">逻辑与</td>
</tr>
<tr>
<td markdown="span">`||`</td>
<td markdown="span">逻辑或</td>
</tr>
</tbody>
</table>

比较

这些运算符比较操作数，结果为真时返回 1，为假时返回 0。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`<`</td>
<td markdown="span">小于</td>
</tr>
<tr>
<td markdown="span">`>`</td>
<td markdown="span">大于</td>
</tr>
<tr>
<td markdown="span">`<=`</td>
<td markdown="span">小于或等于</td>
</tr>
<tr>
<td markdown="span">`>=`</td>
<td markdown="span">大于或等于</td>
</tr>
<tr>
<td markdown="span">`==`</td>
<td markdown="span">equal</td>
</tr>
<tr>
<td markdown="span">`!=`</td>
<td markdown="span">不等于</td>
</tr>
<tr>
<td markdown="span">`~=`</td>
<td markdown="span">near</td>
</tr>
</tbody>
</table>

赋值

这些运算符左侧必须是变量。使用简单赋值运算符（`=`）向不存在的变量赋值时，会创建临时变量。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`=`</td>
<td markdown="span">简单赋值</td>
</tr>
<tr>
<td markdown="span">`+=`</td>
<td markdown="span">加法并赋值</td>
</tr>
<tr>
<td markdown="span">`-=`</td>
<td markdown="span">减法并赋值</td>
</tr>
<tr>
<td markdown="span">`*=`</td>
<td markdown="span">乘法并赋值</td>
</tr>
<tr>
<td markdown="span">`/=`</td>
<td markdown="span">除法并赋值</td>
</tr>
<tr>
<td markdown="span">`%=`</td>
<td markdown="span">取余并赋值</td>
</tr>
<tr>
<td markdown="span">`^=`</td>
<td markdown="span">乘方并赋值</td>
</tr>
</tbody>
</table>

### 前缀 { #prefix }

这些运算符放在所作用表达式的前面。

前缀运算符

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`-x`</td>
<td markdown="span">（取负）</td>
</tr>
<tr>
<td markdown="span">`~x`</td>
<td markdown="span">按位取反（见按位二元运算符）</td>
</tr>
<tr>
<td markdown="span">`!x`</td>
<td markdown="span">逻辑取反（见逻辑二元运算符）</td>
</tr>
<tr>
<td markdown="span">`++x`</td>
<td markdown="span">前置自增</td>
</tr>
<tr>
<td markdown="span">`--x`</td>
<td markdown="span">前置自减</td>
</tr>
</tbody>
</table>

### 后缀 { #postfix }

这些运算符放在所作用表达式的后面。

后缀运算符

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`x!`</td>
<td markdown="span">阶乘</td>
</tr>
<tr>
<td markdown="span">`x++`</td>
<td markdown="span">后置自增</td>
</tr>
<tr>
<td markdown="span">`x--`</td>
<td markdown="span">后置自减</td>
</tr>
</tbody>
</table>

### 三元中缀 { #ternary-infix }

三元运算符可以简洁地表示条件表达式：

```text
<condition> ? <true-branch> : <false-branch>
```

它与 if/else 语句的作用完全相同，只是每个分支只能是单个表达式。

## 函数 { #functions }

数学函数

表达式解析器提供了 Java Math 库中的以下函数：

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`abs`</td>
<td markdown="span">返回一个数的绝对值。</td>
</tr>
<tr>
<td markdown="span">`acos`</td>
<td markdown="span">返回一个值的反余弦，返回角度范围为 0.0 到 pi。</td>
</tr>
<tr>
<td markdown="span">`asin`</td>
<td markdown="span">返回一个值的反正弦，返回角度范围为 -pi/2 到 pi/2。</td>
</tr>
<tr>
<td markdown="span">`atan2`</td>
<td markdown="span">将直角坐标 (x, y) 转换为极坐标 (r, theta)，返回其中的角度 theta。</td>
</tr>
<tr>
<td markdown="span">`atan`</td>
<td markdown="span">返回一个值的反正切，返回角度范围为 -pi/2 到 pi/2。</td>
</tr>
<tr>
<td markdown="span">`cbrt`</td>
<td markdown="span">返回一个值的立方根。</td>
</tr>
<tr>
<td markdown="span">`ceil`</td>
<td markdown="span">返回大于或等于参数的最小（最接近负无穷）整数值。</td>
</tr>
<tr>
<td markdown="span">`cos`</td>
<td markdown="span">返回角度的三角余弦值。</td>
</tr>
<tr>
<td markdown="span">`cosh`</td>
<td markdown="span">返回一个值的双曲余弦。</td>
</tr>
<tr>
<td markdown="span">`exp`</td>
<td markdown="span">返回欧拉数 e 的指定次幂。</td>
</tr>
<tr>
<td markdown="span">`floor`</td>
<td markdown="span">返回小于或等于参数的最大（最接近正无穷）整数值。</td>
</tr>
<tr>
<td markdown="span">`ln`</td>
<td markdown="span">返回一个值的自然对数（以 e 为底）。</td>
</tr>
<tr>
<td markdown="span">`log`</td>
<td markdown="span">返回一个值的自然对数（以 e 为底）。</td>
</tr>
<tr>
<td markdown="span">`log10`</td>
<td markdown="span">返回一个值的以 10 为底的对数（以 e 为底）。</td>
</tr>
<tr>
<td markdown="span">`max`</td>
<td markdown="span">返回这些值中的最大值。（支持 2 个和 3 个参数）</td>
</tr>
<tr>
<td markdown="span">`min`</td>
<td markdown="span">返回这些值中的最小值。（支持 2 个和 3 个参数）</td>
</tr>
<tr>
<td markdown="span">`rint`</td>
<td markdown="span">返回数值上最接近参数的整数值。</td>
</tr>
<tr>
<td markdown="span">`round`</td>
<td markdown="span">返回最接近参数的数。</td>
</tr>
<tr>
<td markdown="span">`sin`</td>
<td markdown="span">返回角度的三角正弦值。</td>
</tr>
<tr>
<td markdown="span">`sinh`</td>
<td markdown="span">返回一个值的双曲正弦。</td>
</tr>
<tr>
<td markdown="span">`sqrt`</td>
<td markdown="span">返回一个值经过正确舍入的正平方根。</td>
</tr>
<tr>
<td markdown="span">`tan`</td>
<td markdown="span">返回角度的三角正切值。</td>
</tr>
<tr>
<td markdown="span">`tanh`</td>
<td markdown="span">返回一个值的双曲正切。</td>
</tr>
</tbody>
</table>

附加函数

此外，还提供以下函数：

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`rotate(x, y, angle)`</td>
<td markdown="span">将给定坐标对旋转指定角度，角度单位为弧度。</td>
</tr>
<tr>
<td markdown="span">`swap(x, y)`</td>
<td markdown="span">交换给定的 2 个变量的内容。</td>
</tr>
<tr>
<td markdown="span">`random()`</td>
<td markdown="span">返回小于 1.0 的随机正数。</td>
</tr>
<tr>
<td markdown="span">`randint(max)`</td>
<td markdown="span">返回小于 max 的随机正整数。</td>
</tr>
<tr>
<td markdown="span">`perlin(seed, x, y, z, frequency, octaves, persisence)`</td>
<td markdown="span">使用给定参数生成柏林噪声。</td>
</tr>
<tr>
<td markdown="span">`voronoi(seed, x, y, z, frequency)`</td>
<td markdown="span">使用给定参数生成 Voronoi 噪声。</td>
</tr>
<tr>
<td markdown="span">`ridgedmulti(seed, x, y, z, frequency, octaves)`</td>
<td markdown="span">使用给定参数生成脊状多重分形噪声。</td>
</tr>
</tbody>
</table>

方块查询函数

以下函数可以在编辑上下文中查询世界里的方块。注意，它们仍使用旧版 ID 和数据值，因此对新方块（1.13+）的行为可能未定义。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`query(x, y, z, type, data)`</td>
<td markdown="span">如果给定坐标处的方块具有指定的旧版 ID 和数据值，返回真。如果 type 或 data 是变量，则会将该方块的 ID 和数据值赋给对应变量。</td>
</tr>
<tr>
<td markdown="span">`queryRel(dx, dy, dz, type, data)`</td>
<td markdown="span">与 query 类似，但使用相对于当前计算方块坐标的偏移量。</td>
</tr>
<tr>
<td markdown="span">`queryAbs(xp, yp, zp, type, data)`</td>
<td markdown="span">与 query 类似，但使用世界绝对坐标。</td>
</tr>
</tbody>
</table>

缓冲区函数

这些函数用于访问数据缓冲区（本质上是数组）。系统提供两个缓冲区，一个为全局共享，另一个为表达式本地使用。函数名前带 g 时访问全局缓冲区，不带 g 时访问本地缓冲区。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`(g)megabuf(index)`</td>
<td markdown="span">返回缓冲区中给定索引处的值。</td>
</tr>
<tr>
<td markdown="span">`(g)megabuf(index, value)`</td>
<td markdown="span">设置缓冲区中给定索引处的值。</td>
</tr>
<tr>
<td markdown="span">`(g)closest(x, y, z, index, count, stride)`</td>
<td markdown="span">从给定索引开始，以 *stride* 为每次迭代的间隔，进行 *count* 次迭代，找到最接近给定 x,y,z 的一组 x,y,z 值（即缓冲区中连续的三个值），并返回其索引。</td>
</tr>
</tbody>
</table>

## 常量 { #constants }

常量

以下常量始终可用，且无法赋值。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`e`</td>
<td markdown="span">2.7182818284590452354</td>
<td markdown="span">自然对数的底数</td>
</tr>
<tr>
<td markdown="span">`pi`</td>
<td markdown="span">3.14159265358979323846</td>
<td markdown="span">圆的周长与直径之比</td>
</tr>
<tr>
<td markdown="span">`true`</td>
<td markdown="span">1</td>
<td markdown="span">用于布尔运算</td>
</tr>
<tr>
<td markdown="span">`false`</td>
<td markdown="span">0</td>
<td markdown="span">用于布尔运算</td>
</tr>
</tbody>
</table>

## 语句块 { #block-statements }

语句块是用花括号包围的一组语句：

```text
{ x=5; y=6; }
```

它们主要与控制结构配合使用。

## 控制结构 { #control-structures }

if/else

```text
if (<condition>) <true-branch>
if (<condition>) <true-branch> else <false-branch>
```

- 通过计算 `<condition>` 来决定执行哪个分支。

- 大于零的值都视为真，其他值都视为假。

- `<true-code>` 和 `<false-code>` 可以是以分号结束的单条语句，也可以是语句块。

**注意：**else 关键字始终与最近的 if 关联。因此可以编写如下 elseif 结构：

```text
if (<condition 1>) <true-code 1> else if (<condition 2>) <true-code 2> else <false-code>
```

### 循环 { #loops }

循环最多执行 256 次。

while

```text
while (<condition>) <body>
do <body> while (<condition>);
```

- 通过计算 `<condition>` 来决定是否继续循环。

- `<body>` 可以是以分号结束的单条语句，也可以是语句块。

- do-while 会在执行循环体之后检查条件。

Java/C 风格的 for

```text
for (<init>; <condition>; <increment>) <body>
```

- `<init>`、`<condition>` 和 `<increment>` 都是单个表达式。

- `<body>` 可以是以分号结束的单条语句，也可以是语句块。

**执行步骤**

首先计算一次 `<init>`，之后每次迭代都按以下步骤执行：

1. 如果 `<condition>` 的结果小于或等于零（即假），结束循环。

2. 执行 `<body>`。

3. 执行 `<increment>`。

简单 for

```text
for (<counter> = <first>, <last>) <body>
```

- `<counter>` 是用于记录迭代次数的变量。

- `<first>` 和 `<last>` 都是单个表达式。

- `<body>` 可以是以分号结束的单条语句，也可以是语句块。

**执行步骤**

首先将内部计数器设为 `<first>`，之后每次迭代都按以下步骤执行：

1. 如果内部计数器超过 `<last>`，结束循环。

2. 将 `<counter>` 设为内部计数器的值。

3. 执行 &lt;body&gt;。

4. 将 &lt;counter&gt; 增加 1.0。

`<first>` 和 `<last>` 都只计算一次。
