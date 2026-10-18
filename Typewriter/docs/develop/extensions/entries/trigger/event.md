---
title: 事件条目（EventEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/trigger/event
source_version: 0.8.0
---

# 事件条目（EventEntry）

`EventEntry`用作任何序列的起点。它可以让外部事件监听器监听事件并据此触发。

## 用法 {#usage}

ExampleEventEntry.kt

```kotlin
@Entry("example_event", "An example event entry.", Colors.YELLOW, "material-symbols:bigtop-updates")
class ExampleEventEntry(
    override val id: String = "",
    override val name: String = "",
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
) : EventEntry
```

要监听事件，你必须创建一个用`@EntryListener`注释的函数。
kotlin 的伟大之处在于，这可以在与条目相同的文件中完成。

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

该函数会自动被Typewriter注册为该事件的监听器，并在Bukkit事件触发时被调用。
可以添加可选的`Query`参数以轻松获取所有不同的事件条目。

## 条目上下文变量 {#entry-context-variables}

有时你希望将一些信息传递给上下文，以便后续条目可以使用它。

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

---

原文：[EventEntry](https://docs.typewritermc.com/develop/extensions/entries/trigger/event) · 文档版本：0.8.0
