# VariableEntry

The `VariableEntry` is designed to make your entries more dynamic by allowing fields to be computed at runtime. Instead of hardcoding values in your entries, you can use variables that adapt based on the current game state, player context, or other conditions.

## Understanding Variables {#understanding-variables}

When creating entries in Typewriter, you often need fields that shouldn't be static. For example, you might want a text that changes based on a player's progress, or a location that depends on where certain events happened in the game. This is where `VariableEntry` comes in - it acts as a dynamic value provider that can return different values based on the current context.

### Basic Implementation {#basic-implementation}

Let's start with a simple variable entry:

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

Every variable entry receives a `VarContext` when it needs to provide its value. This context contains:

- The current player (`context.player`)
- The expected return type (`context.klass`)
- Any associated data for this specific usage (`context.data`)

### Adding Variable Data {#adding-variable-data}

Variables become more powerful when they can be configured differently at each usage site. This is achieved through variable data:

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

The relationship between entry fields and variable data is important to understand:

1. Entry Fields (like `someString`):

   - Defined when creating the variable entry
   - Remain the same for all uses of this variable entry instance
   - Used for configuration that should be consistent
2. Variable Data Fields (like `otherInfo`):

   - Can be different every time the variable is used
   - Provide context-specific configuration
   - Allow the same variable entry to behave differently in different situations

![Variable Entry with Data](https://docs.typewritermc.com/assets/optimized-img/example_variable_with_data.6ed163c.422.avif)

Variable Entry

![Variable Usage with Data](https://docs.typewritermc.com/assets/optimized-img/example_var_with_data_used.3958591.419.avif)

Variable Usage

### Working with Generic Types {#working-with-generic-types}

Sometimes you need variables that can work with different types of values. The generic system in `VariableEntry` makes this possible:

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

When working with generics, remember:

- A single instance of a variable entry will always return the same type
- Different instances of the same variable entry can work with different types
- When your variable data uses a generic type, the variable entry must have at least one field using that same generic type
- This ensures that the generic type information flows correctly from the usage site through the data to the entry

![String Generic Variable](https://docs.typewritermc.com/assets/optimized-img/generic_string.2691b33.424.avif)

String Generic Variable

![Duration Generic Variable](https://docs.typewritermc.com/assets/optimized-img/generic_duration.ba7762c.421.avif)

Duration Generic Variable

![Generic Variable Usage](https://docs.typewritermc.com/assets/optimized-img/generic_used.f73c1ea.399.avif)

Generic Variable Usage

### Type Constraints {#type-constraints}

You can restrict which entry fields your variable can be used with:

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

The `@GenericConstraint` annotation specifies which types of fields this variable can replace. In the example above, this variable can only be used for `String` or `Int` fields in other entries. This ensures that variables are only used in appropriate contexts within your content.

## Variable Entry Usage {#variable-entry-usage}

Now that you understand the basics of `VariableEntry`, let's see how we can mark fields to allow for dynamic values.

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

In this example, we have a variable entry that has two fields: `someString` and `someInt`.
The `Var` type is used to represent a variable that can be used in different contexts.

**caution**

**Not all fields should be marked as variables.** Only fields where it would make sense to have a dynamic value should be marked as a variable.
