# ActionEntry

The `ActionEntry` defines an action to take. When it is triggered, it will run it's `execute` method.
After which it will trigger all the next entries in the chain.

**Immutable Entry**

It is important to stress that the entry must be immutable.
**It cannot have any mutable state.**

## Usage {#usage}

ExampleActionEntry.kt

```kotlin
@Entry("example_action", "An example action entry.", Colors.RED, "material-symbols:touch-app-rounded")
class ExampleActionEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
) : ActionEntry {
    override fun ActionTrigger.execute() {
        // Do something with the player
    }
}
```

Typewriter will automatically trigger the next entries in the chain after the `execute` method is called, and apply all the modifiers.

Sometimes you want to have a little more control over when the next triggers are triggered, or what triggers are triggered.

ExampleActionEntry.kt

```kotlin
    override fun ActionTrigger.execute() {
        // This disables Typewriter's automatic triggering of the next entries,
        // and disables the automatic apply of the modifiers.
        disableAutomaticTriggering()

        // Now you can manually trigger the next entries.
        triggerManually()

        // Or if you want to specify which triggers to trigger, you can do so.
        triggers.filterIndexed { index, _ -> index % 2 == 0 }.triggerFor(player)

        // You can also manually apply the modifiers.
        applyModifiers()
    }
```
