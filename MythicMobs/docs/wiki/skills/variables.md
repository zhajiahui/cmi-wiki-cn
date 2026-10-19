---
title: 变量
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/variables
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 变量

变量用于存储信息。通过变量系统，可以保存和修改数值或其他值，供之后在占位符或条件中使用。这些值既可以长期保留，也可以临时保存。

1. [变量类型](variables.md#variable-types)
2. [变量作用域](variables.md#variable-scopes)
3. [使用方法](variables.md#usage)
   1. [变量类型行为](variables.md#variable-types-behavior)
      1. [数值](variables.md#number)
      2. [字符串](variables.md#string)
      3. [布尔](variables.md#boolean)
      4. [集合](variables.md#set)
      5. [列表](variables.md#list)
      6. [映射](variables.md#map)
      7. [位置](variables.md#location)
      8. [向量](variables.md#vector)
      9. [时间](variables.md#time)
      10. [元技能](variables.md#metaskill)
      11. [物品](variables.md#item)
   2. [变量技能机制](variables.md#variable-mechanics)
   3. [变量条件](variables.md#variable-conditions)
   4. [变量目标选择器](variables.md#variable-targeters)
4. [变量占位符](variables.md#variable-placeholders)
5. [变量回退](variables.md#variable-fallback)
6. [嵌套变量](variables.md#nested-variable)
7. [生物变量](variables.md#mob-variables)

# 变量类型 {#variable-types}

变量支持多种类型，使用 [setVariable](mechanics/setvariable.md) 机制初始化变量时指定。通常可以在类型之间转换，MythicMobs 会尽量将变量用于所需的场景；但如果某个类型无法用于当前操作，就会报错。

| **类型** | **说明** |
| --- | --- |
| INTEGER | 不带小数位的数值。 |
| FLOAT | 带小数位的数值。 |
| LONG | 不带小数位的数值，可表示比 INT 大得多的数值。 |
| DOUBLE | 带小数位的数值，可表示比 FLOAT 大得多的数值。 |
| STRING | 一个词或句子。 |
| BOOLEAN | 只能为 true 或 false 的值。 |
| SET | 一组无序且不重复的值。 |
| LIST | 有序的条目列表。 |
| MAP | 键值对列表。 |
| LOCATION | 服务器中的某个位置。 |
| VECTOR | 由 3 个 DOUBLE 值组成的列表。 |
| TIME | 某一时刻，以自纪元起经过的毫秒数表示。 |
| METASKILL | 内联元技能，在变量创建时解析。 |
| ITEM | 一个 itemstack，可用于存储和修改物品数据。 |

# 变量作用域 {#variable-scopes}

变量的“作用域”决定它**存储在哪里**。并非所有作用域都适用于所有情况，例如条件可能没有施法者，此时 caster 指向的是条件检查的目标。

| **作用域** | **变量所在位置** |
| --- | --- |
| SKILL | 位于当前技能树中，始终是临时变量，会在当前技能队列结束时消失。 |
| CASTER | 位于施法生物上。 |
| TARGET | 位于机制或条件的目标上。 |
| WORLD | 当前世界。 |
| GLOBAL | 服务器。 |

# 用法 {#usage}

所有变量技能机制和条件都支持 `var=` 与 `scope=` 属性，用于指定要操作的变量及其作用域。也可以简写为 `var=scope.variable_name`。以下示例效果相同：

```yaml
    - setvariable{var=target.somevariable; ...}
    - setvariable{var=somevariable;scope=target; ...}
```

> 变量名称中绝对不要包含点号 (`.`)！点号用作分隔符，将其写入变量名会产生意外行为！

## 各变量类型的行为 {#variable-types-behavior}

### 数字 {#number}

包括 INTEGER、FLOAT、LONG 和 DOUBLE，因为它们的行为在功能上相同

```yaml
  # Create your number variable
  - setvariable{var=skill.example;type=DOUBLE;val=1.5}

  # Add a value to a number
  - variableadd{var=skill.example;amount=2}

  # Remove a value from a number
  - variablesubtract{var=skill.example;amount=1}

  # Print a number
  - message{m=<skill.var.example>} # 2.5
```

### 字符串（String） {#string}

```yaml
  # Create your string variable
  - setvariable{var=skill.example;type=STRING;val="oh oh hello"}

  # append a value to a string
  - variableadd{var=skill.example;amount=" world"}

  # Remove every substring from a string
  - variablesubtract{var=skill.example;amount="oh "}

  # Print a string
  - message{m=<skill.var.example>} # hello world
```

### 布尔值（Boolean） {#boolean}

```yaml
  # Create your boolean variable
  - setvariable{var=skill.example;type=BOOLEAN;val=true} # can also be "1" or "yes" for "true". Every other value is "false"

  # Performs an OR logical operation on the boolean
  - variableadd{var=skill.example;amount=1} # Sets the boolean to true if either current or added value is truthy (OR logic)

  # Performs an AND logical operation on the boolean
  - variablesubtract{var=skill.example;amount=1} # Sets the boolean to true only if both current and added value are truthy (AND logic)

  # Print a boolean
  - message{m=<skill.var.example>} # true
```

### 集合（Set） {#set}

```yaml
  # Create a set
  - setvariable{var=skill.example;type=SET;val=1,2,hello}

  # Add a value to a set
  - variableadd{var=skill.example;amount=world}
  - variableadd{var=skill.example;amount=1} # If you add a value that is already present, the set will not change

  # Remove a value from a set
  - variablesubtract{var=skill.example;amount=hello}

  # Print a set
  - message{m=<skill.var.example>} # 1,2,world
```

### 列表 {#list}

```yaml
  # Create a list
  - setvariable{var=skill.example;type=LIST;val=1,2,hello}

  # Add a value to a list
  - variableadd{var=skill.example;amount=world}

  # Remove a value from a list (using its index)
  - variablesubtract{var=skill.example;amount=0}

  # Print a list
  - message{m=<skill.var.example>} # 2,hello,world
  - message{m=<skill.var.example.0>} # 2
```

### 映射（Map） {#map}

```yaml
  # Create a map
  - setvariable{var=skill.example;type=MAP;val="hello=world;mamma=mia"}

  # Add a value to a map
  - variableadd{var=skill.example;amount="pizza=pasta;please=help"}

  # Remove a value from a map(using its key)
  - variablesubtract{var=skill.example;amount=hello}

  # Print a map
  - message{m=<skill.var.example>} # mamma=mia;pizza=pasta;please=help
  - message{m=<skill.var.example.please>} # help
```

### Location {#location}

```yaml
  # Create your location variable
  - setvariable{var=skill.example;type=LOCATION;val=world,1,2,3}
  - setvarloc{var=skill.specialexample;val=@selflocation} # You can also set a location variable via this special mechanic

  # Increase the coordinates values
  - variableadd{var=skill.example;amount=1,2,3}

  # Decrease the coordinates values
  - variablesubtract{var=skill.example;amount=1,1,1}

  # Print a location
  - message{m=<skill.var.example>} # world,1.0,3.0,5.0
```

### 向量（Vector） {#vector}

```yaml
  # Create your vector variable
  - setvariable{var=skill.example;type=VECTOR;val=1,2,3}

  # Increase the component values
  - variableadd{var=skill.example;amount=1,2,3}

  # Decrease the component values
  - variablesubtract{var=skill.example;amount=1,1,1}

  # Print a location
  - message{m=<skill.var.example>} # 1.0,3.0,5.0
```

### Time {#time}

```yaml
  # Create your time variable
  - setvariable{var=skill.simpleexample;type=TIME;val=1234}

  # While a random int works too, most of the time you will want to use this variable type to store and epoch
  # This can be smoothly done by using the <utils.epoch.*> family of placeholders
  - setvariable{var=skill.example;type=TIME;val=<utils.epoch.timestamp>}

  # Increase the time value
  - variableadd{var=skill.example;amount=2}

  # Decrease the time value
  - variablesubtract{var=skill.example;amount=1}

  # Print the time
  - message{m=<skill.var.example>} # Prints out whatever the current epoch is, after adding 2 and subtracting 1 milliseconds from it

  # Please note that, for output purposes, it might be worthwhile to look at some funny meta-keywords
  - message{m=<skill.var.example.formatted.Z>}
  - message{m=<skill.var.example.duration>} # If you want to display the time as a duration. As in, how many seconds/minutes/hours etc. make up the stored value. For instace, a value of "61000" corresponds to "1 minute and 1 second"
```

### MetaSkill {#metaskill}

```yaml
  # Create your MetaSkill variable
  - setvariable{var=skill.example;type=METASKILL;val=[
    - message{m=hello world} @self
    ]}

  # Print the MetaSkill's original text
  - message{m=<skill.var.example>}

  # Execute the MetaSkill
  - vskill{variable=skill.example}
```

> 如果 MetaSkill 包含 skill、projectile 等元机制，执行前必须等待 15~21 个游戏刻，以免报错

### Item {#item}

```yaml
  # Create your Item variable
  - setvariable{var=skill.example;type=ITEM;val=<target.item.itemstack.HAND>}

  # Some prefixes can be used to induce some specific behavior. Eligible prefixes are `mythic:`, `slot:`, `drop` and `material:`
  - setvariable{var=skill.example;type=ITEM;val=mythic:BanditTunic}
  - setvariable{var=skill.example;type=ITEM;val=material:STONE}
  - setvariable{var=skill.example;type=ITEM;val=drop:itemvariable{var=caster.otheritem}} # Works for both single and multi drops. Droptables will return one item rolled from them
  - setvariable{var=skill.example;type=ITEM;val=slot:HAND}
  - setvariable{var=skill.example;type=ITEM;val=slot:10}


  # Update your Item variable
  - setvariable{var=skill.example;type=ITEM;val=<skill.var.example.withname.test.withlore.hello,world>}

  # Print the Item's ItemStack
  - message{m=<skill.var.example>}

  # Give and Take the Item
  - giveitem{variable=skill.example}
  - takeitem{variable=skill.example}

  # For every mechanic that accepts a drop/droptable as a possible value, it is also possible to use the itemvariable drop type
  # to drop the item stored in the specified item variable
  - equip{item=itemvariable{variable=skill.item} head} @self
  - giveitem{item=itemvariable{variable=skill.item}} @self
```

> 在某些早于 1.21.7 的版本中存在以下问题
>

> - 在持久化生物或玩家身上长期保存物品变量
> - 使用<target.item.itemstack.HAND>设置变量
>

> 简而言之，在受影响的版本中，将 ItemStack 序列化为字符串后，再从该字符串反序列化，会丢失部分数据。如果使用的是受影响版本，仍然可以使用这种变量，但必须：
>

> - 仅用它存储临时数据，*不要*依赖它在服务器重启后保留数据
> - 不要使用 <target.item.itemstack.HAND> 占位符设置变量，应使用上文所示的 slot: 前缀

## 变量技能机制 {#variable-mechanics}

变量技能机制是用于操作变量的特殊机制，可以以实体、位置为目标，也可以不指定目标。所用作用域不同，目标也可能影响结果。例如，未选中实体时，就无法获取 target 作用域的变量。

| 技能机制 | 说明 |
| --- | --- |
| [SetVariable](mechanics/setvariable.md) | 初始化并设置变量。 |
| [SetVariableLocation](mechanics/setvariablelocation.md) | 设置变量，其值取决于目标位置。 |
| [VariableUnset](mechanics/variableunset.md) | 取消设置变量。 |
| [VariableAdd](mechanics/variableadd.md) | 为变量增加数值。 |
| [VariableSubtract](mechanics/variablesubtract.md) | 从变量中减去数值。 |
| [VariableMath](mechanics/variablemath.md) | 使用数值变量进行计算。 |

## 变量条件 {#variable-conditions}

| 条件 | 说明 |
| --- | --- |
| [VariableEquals](conditions/variableequals.md) | 检查变量是否等于给定值。 |
| [VariableIsSet](conditions/variableisset.md) | 检查变量是否已设置。 |
| [VariableInRange](conditions/variableinrange.md) | 检查数值变量是否位于指定范围内。 |
| [VariableContains](conditions/variablecontains.md) | 检查变量是否包含给定值。 |

## 变量目标选择器 {#variable-targeters}

| 目标选择器 | 说明 |
| --- | --- |
| @[VariableLocation](targeters/variablelocation.md) | 以指定 Location 变量中保存的位置为目标。 |

# 变量占位符 {#variable-placeholders}

变量可以在任何允许占位符的 MythicMobs 机制或值中引用。这通常使用格式 `<scope.var.variable>` 完成。

变量占位符还可以使用元占位符来更改占位符的输出，甚至可以将元占位符链接在一起以获得“复合”效果。

了解更多[元占位符说明](placeholders/meta-placeholders.md)

# 变量回退值 {#variable-fallback}

使用占位符变量时，你还可以使用语法 `<scope.var.variable{default=[defaultvalue]}>` 指定变量未定义时将使用的“默认”值。

```yaml
    - message{m="Hello there, <target.var.title{default=wanderer}>"} @trigger ~onInteract
```

在此示例中，如果右键点击 NPC 的玩家没有设置 "title" 变量，NPC 会回复 "Hello there, wanderer"。但如果这样做：

```yaml
    - setVariable{var=target.title;value="Sir"} @trigger ~onInteract
```

……在某处执行过这段操作，即使是由另一个生物执行，第一个生物也会回复 "Hello there, Sir"。

# 嵌套变量 {#nested-variable}

变量也可以无限嵌套：如果这样做，最里面的变量将首先被解析，然后从那里开始，每个变量都会从最里面到最外面解析

```yaml
  Skills:
    - setvariable{var=caster.hello;type=STRING;val=example_name} @self
    - setvariable{var=caster.example_name;type=STRING;val=Hello There!} @self
    - message{m="<caster.var.<caster.var.hello>>"} @PIR{r=10}
```

> 在此示例中，消息内容为 "Hello there!"

> 由于 Mythic 占位符解析器的限制，同时将同一占位符*单独使用*和作为另一个占位符的嵌套值使用非常危险，很可能导致嵌套占位符无法正确解析！例如，下面的写法
>

> ```yaml
>  - message{m=<skill.var.test> <skill.var.<skill.var.test>>} # Don't do this!  
> ```
>

> 结果无法确定！要解决此问题，需更改变量名，或提前解析变量
>

> ```yaml
>  - setvariable{var=skill.segment;type=STRING;val=<skill.var.<skill.var.test>>}
>  - message{m=<skill.var.test> <skill.var.segment>} # Do this instead!
> ```

# [生物变量](../mobs/mobs.md#variables) {#mob-variables}

通过 [Mob Variables](../mobs/mobs.md#variables) 字段，可以让生物在生成时就带有预设变量。

```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```
