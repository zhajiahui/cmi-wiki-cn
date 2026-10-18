---
title: 变量条目（VariableEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/static/variable
source_version: 0.8.0
---

# 变量条目（VariableEntry）

`VariableEntry`旨在通过允许在运行时计算字段来使你的条目更加动态。你可以使用根据当前游戏状态、玩家上下文或其他条件进行调整的变量，而不是在条目中硬编码值。

## 理解变量 {#understanding-variables}

在Typewriter中创建条目时，你通常需要不应该是静态的字段。例如，你可能需要一个根据玩家进度而变化的文本，或者一个取决于游戏中某些事件发生位置的位置。这就是`VariableEntry`的用武之地 - 它充当动态值提供者，可以根据当前上下文返回不同的值。

### 基本实现 {#basic-implementation}

让我们从一个简单的变量条目开始：

ExampleVariableEntry.kt

```kotlin
@Entry("example_variable", "An example variable entry.", Colors.GREEN, "mdi:code-tags")
class ExampleVariableEntry(
    override val id: String = "",
    override val name: String = "",
) : VariableEntry {
    override fun <T : Any> get(context: VarContext<T>): T {
        val player = context.player
        val klass = context.klass

        TODO("Do something with the player and the klass")
    }
}
```

每个变量条目在需要提供其值时都会收到`VarContext`。该上下文包含：

- 当前玩家（`context.player`）
- 预期返回类型（`context.klass`）
- 此特定用途的任何相关数据 (`context.data`)

### 添加变量数据 {#adding-variable-data}

变量可以在不同使用处分别配置，这是通过变量数据实现的：

ExampleVariableEntry.kt

```kotlin
@Entry("example_variable_with_data", "An example variable entry with data.", Colors.GREEN, "mdi:code-tags")
// Register the variable data associated with this variable.
@VariableData(ExampleVariableWithData::class)
class ExampleVariableWithDataEntry(
    override val id: String = "",
    override val name: String = "",
    // This data will be the same for all uses of this variable.
    val someString: String = "",
) : VariableEntry {
    override fun <T : Any> get(context: VarContext<T>): T {
        val player = context.player
        val klass = context.klass
        this.someString
        val data = context.getData<ExampleVariableWithData>() ?: throw IllegalStateException("Could not find data for ${context.klass}, data: ${context.data}")

        TODO("Do something with the player, the klass, and the data")
    }
}

class ExampleVariableWithData(
    // This data can change at the place where the variable is used.
    val otherInfo: Int = 0,
)
```

理解输入字段和变量数据之间的关系很重要：

1. 输入字段（如`someString`）：

   - 创建变量条目时定义
   - 此变量条目实例的所有用途均保持不变
   - 用于需要保持一致的配置
2. 可变数据字段（如`otherInfo`）：

   - 每次使用变量时都可能不同
   - 提供上下文特定的配置
   - 允许相同的变量条目在不同情况下表现不同

![带数据的变量输入](../../../../assets/7b73edf06ce3-example_variable_with_data.6ed163c.422.avif)

变量输入

![数据的变量用法](../../../../assets/18ce148b6a8d-example_var_with_data_used.3958591.419.avif)

可变用法

### 使用泛型 {#working-with-generic-types}

有时变量需要处理不同类型的值，`VariableEntry` 的泛型机制支持这种用法：

ExampleVariableEntry.kt

```kotlin
@Entry("example_generic_variable", "An example generic variable entry.", Colors.GREEN, "mdi:code-tags")
class ExampleGenericVariableEntry(
    override val id: String = "",
    override val name: String = "",
    // We determine how to parse this during runtime.
    val generic: Generic = Generic.Empty,
) : VariableEntry {
    override fun <T : Any> get(context: VarContext<T>): T {
        val player = context.player
        val klass = context.klass

        // Parse the generic data to the correct type.
        val data = generic.get(klass)

        TODO("Do something with the player, the klass, and the generic")
    }
}

class ExampleGenericVariableData(
    // Generic data will always be the same as the generic type in the variable.
    val otherGeneric: Generic,
)
```

使用泛型时，请记住：

- 变量条目的单个实例将始终返回相同的类型
- 同一变量条目的不同实例可以使用不同的类型
- 当变量数据使用泛型类型时，变量条目必须至少有一个使用相同泛型类型的字段
- 这样，泛型的类型信息就能从使用处经变量数据正确传递给条目。

![字符串通用变量](../../../../assets/8351cbec2dea-generic_string.2691b33.424.avif)

字符串通用变量

![持续时间通用变量](../../../../assets/2c63a5a78aa5-generic_duration.ba7762c.421.avif)

持续时间通用变量

![通用变量用法](../../../../assets/a78ef30b27b3-generic_used.f73c1ea.399.avif)

通用变量的用法

### 类型约束 {#type-constraints}

你可以限制变量可以与哪些输入字段一起使用：

ExampleVariableEntry.kt

```kotlin
@Entry("example_constraint_variable", "An example constraint variable entry.", Colors.GREEN, "mdi:code-tags")
@GenericConstraint(String::class)
@GenericConstraint(Int::class)
class ExampleConstraintVariableEntry(
    override val id: String = "",
    override val name: String = "",
    // We determine how to parse this during runtime.
    val generic: Generic = Generic.Empty,
) : VariableEntry {
    override fun <T : Any> get(context: VarContext<T>): T {
        val player = context.player
        // This can only be a String or an Int.
        val klass = context.klass

        // Parse the generic data to the correct type.
        val data = generic.get(klass)

        TODO("Do something with the player, the klass, and the generic")
    }
}
```

`@GenericConstraint`注解指定该变量可以替换哪些类型的字段。在上例中，该变量只能用于其他条目中的`String`或`Int`字段。这可确保变量仅在内容中的适当上下文中使用。

## 变量条目的用法 {#variable-entry-usage}

现在你已经了解了`VariableEntry`的基础知识，让我们看看如何标记字段以允许动态值。

ExampleVariableEntry.kt

```kotlin
@Entry("example_action_using_variable", "An example action that uses a variable.", Colors.RED, "material-symbols:touch-app-rounded")
class ExampleActionUsingVariableEntry(
    override val id: String = "",
    override val name: String = "",
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    val someString: Var<String> = ConstVar(""),
    val someInt: Var<Int> = ConstVar(0),
) : ActionEntry {
    override fun ActionTrigger.execute() {
        val someString = someString.get(player)
        val someInt = someInt.get(player)

        // Do something with the variables
    }
}
```

在此示例中，我们有一个具有两个字段的变量条目：`someString`和`someInt`。
`Var`类型用于表示可以在不同上下文中使用的变量。

**注意**

**并非所有字段都应标记为变量。**仅应将具有动态值的字段标记为变量。

---

原文：[VariableEntry](https://docs.typewritermc.com/develop/extensions/entries/static/variable) · 文档版本：0.8.0
