# EventEntry

The `EventEntry` is used as a starting point for any sequence. It can have external event listeners listening to events and trigger based on that.

## Usage {#usage}

ExampleEventEntry.kt

```kotlin
@Entry("example_event", "An example event entry.", Colors.YELLOW, "material-symbols:bigtop-updates")
class ExampleEventEntry(
    override val id: String = "",
    override val name: String = "",
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
) : EventEntry
```

To listen to an event, you must create a function that is annotated with `@EntryListener`.
The great thing about kotlin, is that this can be done in the same file as the entry.

ExampleEventEntry.kt

```kotlin
@EntryListener(ExampleEventEntry::class)
fun onEvent(event: SomeBukkitEvent, query: Query<ExampleEventEntry>) {
    // Do something
    val entries = query.find() // Find all the entries of this type, for more information see the Query section
    // Do something with the entries, for example trigger them
    entries.triggerAllFor(event.player, context())
}
```

The function will automatically be registered as a listener for the event by Typewriter and be called when the Bukkit event is trigger.
An optional `Query` parameter can be added to easily fetch all the different event entries.

## Entry Context Variables {#entry-context-variables}

Sometimes you want to pass some information to the context so that subsequent entries can use it.

InteractionContextExamples.kt

```kotlin
@Entry(
    "example_event_with_context_keys",
    "An example event entry with context keys.",
    Colors.YELLOW,
    "material-symbols:bigtop-updates"
)
// This tells Typewriter that this entry exposes some context
@ContextKeys(ExampleEntryContextKeys::class)
class ExampleEventEntryWithContextKeys(
    override val id: String = "",
    override val name: String = "",
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
) : EventEntry

@EntryListener(ExampleEventEntryWithContextKeys::class)
fun onEventAddContext(event: SomeBukkitEvent, query: Query<ExampleEventEntryWithContextKeys>) {
    val entries = query.find()
    entries.triggerAllFor(event.player) {
        // Make sure these values are drawn from the event.
        // You MUST supply all the context keys.
        ExampleEntryContextKeys.TEXT withValue "Hello World"
        ExampleEntryContextKeys.NUMBER withValue 42
        // You can also use += to assign the value to the key
        ExampleEntryContextKeys.POSITION += Position.ORIGIN

        // Or we can assign any global key to it.
        LuckyNumberKey += 69
    }
}
```
