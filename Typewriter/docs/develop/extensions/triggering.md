---
title: 触发条目（Triggering Entries）
source: https://docs.typewritermc.com/develop/extensions/triggering
source_version: 0.8.0
---

# 触发条目（Triggering Entries）

有一些简单的方法可以触发`TriggerEntry`中的所有下一个条目。
关键是为条目触发提供 `player`。

**说明**

Typewriter只负责触发应该触发的条目。
如果不满足条件，则不会触发条目。

如果你有一个`TriggerEntry`：

TriggerExample.kt

```kotlin
    // If you only have one entry
    val triggerEntry: TriggerEntry = Query.findById<MyTriggerableEntry>("some_id") ?: return
    // Triggers all the next entries in the sequence.
    triggerEntry.triggerAllFor(player, context())

    // If you have multiple entries
    val triggerEntries: Sequence<TriggerEntry> = Query.find<MyTriggerableEntry>()
    // Triggers all the next entries for all entries.
    triggerEntries.triggerAllFor(player, context())
```

有时你不想在玩家处于对话时触发条目。
例如，当玩家与NPC对话时，你不想再次触发NPC的第一个条目。
你期望当玩家再次点击 NPC 时，会触发下一个对话。
为此，你可以使用`startDialogueWithOrNextDialogue`函数。

TriggerExample.kt

```kotlin
    val triggerEntries: Sequence<MyTriggerableEntry> = Query.find<MyTriggerableEntry>()
    triggerEntries.startDialogueWithOrNextDialogue(player, context())

    // Or trigger something completely different when the player is in dialogue:
    val customTrigger: EventTrigger = InteractionEndTrigger
    triggerEntries.startDialogueWithOrTrigger(player, customTrigger, context())
```

以前，我们使用新的`context`触发条目，但有时我们已经有了上下文。
然后你需要确保将上下文传递给触发器。

TriggerExample.kt

```kotlin
    // The context that you have, most likely provided by Typewriter in some way.
    val context = player.interactionContext ?: context()
    // Triggers all the next entries in the sequence.
    triggerEntries.triggerAllFor(player, context)
```

## 自定义触发器 {#custom-triggers}

Typewriter基于`EventTrigger`接口触发。
因此，所有触发的条目都包含在`EntryTrigger`中。

### 系统触发器 {#system-triggers}

对于某些交互，有在Typewriter中定义的自定义触发器。
这些触发器允许你通过交互执行特殊的操作。

ExampleInteraction.kt

```kotlin
// Trigger to start the interaction
data class ExampleStartTrigger(
    val priority: Int,
    val eventTriggers: List<EventTrigger> = emptyList()
) : EventTrigger {
    override val id: String = "example.start"
}

// Trigger to stop the interaction
data object ExampleStopTrigger : EventTrigger {
    override val id: String = "example.stop"
}
```

#### 对话交互 {#dialogue-interaction}

TriggerExample.kt

```kotlin
    // Next dialogue should be triggered or the current dialogue should complete its typing animation.
    DialogueTrigger.NEXT_OR_SKIP_ANIMATION.triggerFor(player, context())

    // Forces the next dialogue to be triggered, even if the animation hasn't finished.
    DialogueTrigger.FORCE_NEXT.triggerFor(player, context())
```

#### 时间交互 {#temporal-interaction}

TriggerExample.kt

```kotlin
    // To start a temporal sequence
    TemporalStartTrigger(
        pageId = "some_id",
        eventTriggers = listOf<EventTrigger>(),
        settings = TemporalSettings(
            blockChatMessages = true,
            blockActionBarMessages = true
        )
    ).triggerFor(player, context())

    // To stop the temporal sequence and trigger the following entries.
    TemporalStopTrigger.triggerFor(player, player.interactionContext ?: context())
```

---

原文：[Triggering Entries](https://docs.typewritermc.com/develop/extensions/triggering) · 文档版本：0.8.0
