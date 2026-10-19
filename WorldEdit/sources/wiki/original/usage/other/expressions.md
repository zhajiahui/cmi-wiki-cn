# Expression Syntax { #expression-syntax }

The WorldEdit expression parser is supposed to work like Java and related languages, with a few subtle differences:

- Final semicolons can be omitted in most cases.

- The last value in a sequence is always returned, even without a return statement.

- The binary infix `^` operator is a power operator instead of an xor operator and has an according priority as well.

- There is a postfix factorial operator (`!`).

- There is a binary infix near operator (`~=`).

- No objects :)

<a id="contents"></a>

- [Operators](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#operators)



  - [Binary infix](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#binary-infix)

  - [Prefix](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#prefix)

  - [Postfix](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#postfix)

  - [Ternary infix](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#ternary-infix)

- [Functions](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#functions)

- [Constants](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#constants)

- [Block Statements](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#block-statements)

- [Control Structures](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#control-structures)



  - [Loops](https://worldedit.enginehub.org/en/latest/usage/other/expressions/#loops)

## Operators { #operators }

The expression parser uses [Java’s precedence rules](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html), with the following exceptions and additions:

> - The binary power operator (`^`) is between priority 2 and 3
>
> - The postfix factorial operator (`!`) has a priority of 2
>
> - The near operator (`~=`) has a priority of 7

### Binary infix { #binary-infix }

These operators are put between their two operands.

Arithmetic

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`+`</td>
<td markdown="span">Addition</td>
</tr>
<tr>
<td markdown="span">`-`</td>
<td markdown="span">Subtraction</td>
</tr>
<tr>
<td markdown="span">`*`</td>
<td markdown="span">Multiplication</td>
</tr>
<tr>
<td markdown="span">`/`</td>
<td markdown="span">Division</td>
</tr>
<tr>
<td markdown="span">`%`</td>
<td markdown="span">Remainder</td>
</tr>
<tr>
<td markdown="span">`^`</td>
<td markdown="span">Power</td>
</tr>
</tbody>
</table>

Bitwise

These operators interpret their operands as 32 bit integers and operate on their bits.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`<<`</td>
<td markdown="span">Left-shift</td>
</tr>
<tr>
<td markdown="span">`>>`</td>
<td markdown="span">Right-shift</td>
</tr>
</tbody>
</table>

Logical

These operators interpret everything greater than zero as true and everything else as false. They return 1 for true and 0 for false.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`&&`</td>
<td markdown="span">Logical and</td>
</tr>
<tr>
<td markdown="span">`||`</td>
<td markdown="span">Logical or</td>
</tr>
</tbody>
</table>

Comparison

These operators compare their operands and return 1 for true and 0 for false.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`<`</td>
<td markdown="span">less than</td>
</tr>
<tr>
<td markdown="span">`>`</td>
<td markdown="span">greater than</td>
</tr>
<tr>
<td markdown="span">`<=`</td>
<td markdown="span">less or equal</td>
</tr>
<tr>
<td markdown="span">`>=`</td>
<td markdown="span">greater or equal</td>
</tr>
<tr>
<td markdown="span">`==`</td>
<td markdown="span">equal</td>
</tr>
<tr>
<td markdown="span">`!=`</td>
<td markdown="span">not equal</td>
</tr>
<tr>
<td markdown="span">`~=`</td>
<td markdown="span">near</td>
</tr>
</tbody>
</table>

Assignment

These operators require a variable on the left side. Using the simple assignment operator (`=`) to assign to a non-existant variable creates a temporary variable.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`=`</td>
<td markdown="span">simple assignment</td>
</tr>
<tr>
<td markdown="span">`+=`</td>
<td markdown="span">addition+assignment</td>
</tr>
<tr>
<td markdown="span">`-=`</td>
<td markdown="span">subtraction+assignment</td>
</tr>
<tr>
<td markdown="span">`*=`</td>
<td markdown="span">multiplication+assignment</td>
</tr>
<tr>
<td markdown="span">`/=`</td>
<td markdown="span">division+assignment</td>
</tr>
<tr>
<td markdown="span">`%=`</td>
<td markdown="span">remainder+assignment</td>
</tr>
<tr>
<td markdown="span">`^=`</td>
<td markdown="span">power+assignment</td>
</tr>
</tbody>
</table>

### Prefix { #prefix }

These operators precede the expression they apply to.

Prefix Operators

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`-x`</td>
<td markdown="span">(negation)</td>
</tr>
<tr>
<td markdown="span">`~x`</td>
<td markdown="span">Bitwise complement (see bitwise binary operators)</td>
</tr>
<tr>
<td markdown="span">`!x`</td>
<td markdown="span">Logical complement (see logical binary operators)</td>
</tr>
<tr>
<td markdown="span">`++x`</td>
<td markdown="span">Pre-increment</td>
</tr>
<tr>
<td markdown="span">`--x`</td>
<td markdown="span">Pre-decrement</td>
</tr>
</tbody>
</table>

### Postfix { #postfix }

These operators succeed the expression they apply to.

Postfix Operators

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`x!`</td>
<td markdown="span">Factorial</td>
</tr>
<tr>
<td markdown="span">`x++`</td>
<td markdown="span">Post-increment</td>
</tr>
<tr>
<td markdown="span">`x--`</td>
<td markdown="span">Post-decrement</td>
</tr>
</tbody>
</table>

### Ternary infix { #ternary-infix }

The ternary operator is used to represent a conditional expression in a compact way:

```text
<condition> ? <true-branch> : <false-branch>
```

It works exactly like the if/else statement, except that the branches can only be single expressions.

## Functions { #functions }

Math Functions

The expression parser provides the following functions from the Java Math library:

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`abs`</td>
<td markdown="span">Returns the absolute value of a number.</td>
</tr>
<tr>
<td markdown="span">`acos`</td>
<td markdown="span">Returns the arc cosine of a value; the returned angle is in the range 0.0 through pi.</td>
</tr>
<tr>
<td markdown="span">`asin`</td>
<td markdown="span">Returns the arc sine of a value; the returned angle is in the range -pi/2 through pi/2.</td>
</tr>
<tr>
<td markdown="span">`atan2`</td>
<td markdown="span">Returns the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta).</td>
</tr>
<tr>
<td markdown="span">`atan`</td>
<td markdown="span">Returns the arc tangent of a value; the returned angle is in the range -pi/2 through pi/2.</td>
</tr>
<tr>
<td markdown="span">`cbrt`</td>
<td markdown="span">Returns the cube root of a value.</td>
</tr>
<tr>
<td markdown="span">`ceil`</td>
<td markdown="span">Returns the smallest (closest to negative infinity) value that is greater than or equal to the argument and is equal to a mathematical integer.</td>
</tr>
<tr>
<td markdown="span">`cos`</td>
<td markdown="span">Returns the trigonometric cosine of an angle.</td>
</tr>
<tr>
<td markdown="span">`cosh`</td>
<td markdown="span">Returns the hyperbolic cosine of a value.</td>
</tr>
<tr>
<td markdown="span">`exp`</td>
<td markdown="span">Returns Euler’s number e raised to the power of a value.</td>
</tr>
<tr>
<td markdown="span">`floor`</td>
<td markdown="span">Returns the largest (closest to positive infinity) value that is less than or equal to the argument and is equal to a mathematical integer.</td>
</tr>
<tr>
<td markdown="span">`ln`</td>
<td markdown="span">Returns the natural logarithm (base e) of a value.</td>
</tr>
<tr>
<td markdown="span">`log`</td>
<td markdown="span">Returns the natural logarithm (base e) of a value.</td>
</tr>
<tr>
<td markdown="span">`log10`</td>
<td markdown="span">Returns the base 10 logarithm (base e) of a value.</td>
</tr>
<tr>
<td markdown="span">`max`</td>
<td markdown="span">Returns the greatest of the values. (supports 2 and 3 arguments)</td>
</tr>
<tr>
<td markdown="span">`min`</td>
<td markdown="span">Returns the smallest of the values. (supports 2 and 3 arguments)</td>
</tr>
<tr>
<td markdown="span">`rint`</td>
<td markdown="span">Returns the number that is closest in value to the argument and is equal to a mathematical integer.</td>
</tr>
<tr>
<td markdown="span">`round`</td>
<td markdown="span">Returns the closest number to the argument</td>
</tr>
<tr>
<td markdown="span">`sin`</td>
<td markdown="span">Returns the trigonometric sine of an angle.</td>
</tr>
<tr>
<td markdown="span">`sinh`</td>
<td markdown="span">Returns the hyperbolic sine of a value.</td>
</tr>
<tr>
<td markdown="span">`sqrt`</td>
<td markdown="span">Returns the correctly rounded positive square root of a value.</td>
</tr>
<tr>
<td markdown="span">`tan`</td>
<td markdown="span">Returns the trigonometric tangent of an angle.</td>
</tr>
<tr>
<td markdown="span">`tanh`</td>
<td markdown="span">Returns the hyperbolic tangent of a value.</td>
</tr>
</tbody>
</table>

Additional Functions

Additionally, it provides the following functions:

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`rotate(x, y, angle)`</td>
<td markdown="span">Rotates the given coordinate pair by the given angle, in radians.</td>
</tr>
<tr>
<td markdown="span">`swap(x, y)`</td>
<td markdown="span">Swaps the contents of the 2 given variables.</td>
</tr>
<tr>
<td markdown="span">`random()`</td>
<td markdown="span">Returns a random positive number less than 1.0.</td>
</tr>
<tr>
<td markdown="span">`randint(max)`</td>
<td markdown="span">Returns a random positive integer less than max.</td>
</tr>
<tr>
<td markdown="span">`perlin(seed, x, y, z, frequency, octaves, persisence)`</td>
<td markdown="span">Generates perlin noise with the given parameters.</td>
</tr>
<tr>
<td markdown="span">`voronoi(seed, x, y, z, frequency)`</td>
<td markdown="span">Generates voronoi noise with the given parameters.</td>
</tr>
<tr>
<td markdown="span">`ridgedmulti(seed, x, y, z, frequency, octaves)`</td>
<td markdown="span">Generated ridged multi fractal noise with the given parameters.</td>
</tr>
</tbody>
</table>

Block Query Functions

The following functions can be used to query blocks in a world in an editing context. Note that they still use legacy ID and data, so they may have undefined behaviors for new (1.13+) blocks.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`query(x, y, z, type, data)`</td>
<td markdown="span">Returns true if the block at the given coordinates has the given legacy id and data value. If type or data are variables, the id and data of the block will be assigned to that variable.</td>
</tr>
<tr>
<td markdown="span">`queryRel(dx, dy, dz, type, data)`</td>
<td markdown="span">Like query, except with an offset from the currently evaluated block coordinates</td>
</tr>
<tr>
<td markdown="span">`queryAbs(xp, yp, zp, type, data)`</td>
<td markdown="span">Like query, except with absolute world coordinates</td>
</tr>
</tbody>
</table>

Buffer Functions

These functions provide access to data buffers (essentially, arrays). Two buffers are provided, one is a global shared buffer, and one is local to the expression. The function with g prepended accesses the global buffer, without the g accesses the local buffer.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`(g)megabuf(index)`</td>
<td markdown="span">Returns the value of the buffer at the given index.</td>
</tr>
<tr>
<td markdown="span">`(g)megabuf(index, value)`</td>
<td markdown="span">Sets the value of the buffer at the given index.</td>
</tr>
<tr>
<td markdown="span">`(g)closest(x, y, z, index, count, stride)`</td>
<td markdown="span">Finds the index of the closest set of x,y,z values (as in, three consecutive buffer values) to the given x,y,z values within *count* iterations and *stride* space between each iteration, starting at the given index value.</td>
</tr>
</tbody>
</table>

## Constants { #constants }

Constants

The following constants are always available, and cannot be assigned.

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">`e`</td>
<td markdown="span">2.7182818284590452354</td>
<td markdown="span">The base of the natural logarithm</td>
</tr>
<tr>
<td markdown="span">`pi`</td>
<td markdown="span">3.14159265358979323846</td>
<td markdown="span">The ratio between circumference and diameter of a circle</td>
</tr>
<tr>
<td markdown="span">`true`</td>
<td markdown="span">1</td>
<td markdown="span">for boolean operations</td>
</tr>
<tr>
<td markdown="span">`false`</td>
<td markdown="span">0</td>
<td markdown="span">for boolean operations</td>
</tr>
</tbody>
</table>

## Block Statements { #block-statements }

Block statements are groups of statements enclosed in braces:

```text
{ x=5; y=6; }
```

They are mostly used in conjunction with control structures.

## Control Structures { #control-structures }

if/else

```text
if (<condition>) <true-branch>
if (<condition>) <true-branch> else <false-branch>
```

- `<condition>` is evaluated to decide which branch to execute.

- Everything greater than zero is interpreted as true and everything else as false.

- `<true-code>` and `<false-code>` can either be single statements delimited with a semicolon or block statements.

**Note:** An else keyword is always associated with the last if. This allows elseif constructs like these:

```text
if (<condition 1>) <true-code 1> else if (<condition 2>) <true-code 2> else <false-code>
```

### Loops { #loops }

Loops can at most loop 256 times.

while

```text
while (<condition>) <body>
do <body> while (<condition>);
```

- `<condition>` is evaluated to decide whether to continue looping.

- `<body>` can either be a single statement delimited with a semicolon or a block statement.

- do-while checks the condition after executing the body.

Java/C-style for

```text
for (<init>; <condition>; <increment>) <body>
```

- `<init>`, `<condition>` and `<increment>` are single expressions.

- `<body>` can either be a single statement delimited with a semicolon or a block statement.

**Execution steps**

First, `<init>` is evaluated once, then, each iteration follows these steps:

1. If `<condition>` evaluates as less than or equal to zero (i.e. false), the loop is aborted.

2. `<body>` is executed.

3. `<increment>` is executed.

Simple for

```text
for (<counter> = <first>, <last>) <body>
```

- `<counter>` is a variable used to count the iterations.

- `<first>` and `<last>` are single expressions.

- `<body>` can either be a single statement delimited with a semicolon or a block statement.

**Execution steps**

First, an internal counter is set to `<first>`. Then, each iteration follows these steps:

1. If the internal counter exceeds `<last>`, the loop is aborted.

2. `<counter>` is set to the internal counter.

3. &lt;body&gt; is executed.

4. &lt;counter&gt; is incremented by 1.0.

`<first>` and `<last>` are only evaluated once.
