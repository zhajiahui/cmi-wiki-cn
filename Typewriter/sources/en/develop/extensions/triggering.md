# Triggering Entries

There are easy ways to trigger all the next entries in a `TriggerEntry`.
The most important is that you have a `player` to trigger the entries on.

**info**

Typewriter takes care of only triggering the entries that should be triggered.
If criteria are not met, the entries are not triggered.

If you have a single `TriggerEntry`:

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

Sometimes you don't want to trigger the entries when the player is in a dialogue.
For example, when the player is in a dialogue with a NPC, you don't want to trigger the first entry of the NPC again.
You expect when the player clicks on the NPC again, the next dialogue is triggered.
To facilitate this, you can use the `startDialogueWithOrNextDialogue` function.

TriggerExample.kt

```kotlin
    val triggerEntries: Sequence<MyTriggerableEntry> = Query.find<MyTriggerableEntry>()
    triggerEntries.startDialogueWithOrNextDialogue(player, context())

    // Or trigger something completely different when the player is in dialogue:
    val customTrigger: EventTrigger = InteractionEndTrigger
    triggerEntries.startDialogueWithOrTrigger(player, customTrigger, context())
```

Previously, we triggered entries with a new fresh `context`, but sometimes we already have a context.
Then you need to make sure that you pass on the context to the trigger.

TriggerExample.kt

```kotlin
    // The context that you have, most likely provided by Typewriter in some way.
    val context = player.interactionContext ?: context()
    // Triggers all the next entries in the sequence.
    triggerEntries.triggerAllFor(player, context)
```

## Custom triggers {#custom-triggers}

Typewriter triggers based on the `EventTrigger` interface.
So all the entries that are triggered are wrapped in a `EntryTrigger`.

### System Triggers {#system-triggers}

For some interactions there are custom triggers that are defined in Typewriter.
These triggers allow you to do special things with the interaction.

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

#### Dialogue Interaction {#dialogue-interaction}

TriggerExample.kt

```kotlin
    // Next dialogue should be triggered or the current dialogue should complete its typing animation.
    DialogueTrigger.NEXT_OR_SKIP_ANIMATION.triggerFor(player, context())

    // Forces the next dialogue to be triggered, even if the animation hasn't finished.
    DialogueTrigger.FORCE_NEXT.triggerFor(player, context())
```

#### Temporal Interaction {#temporal-interaction}

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
