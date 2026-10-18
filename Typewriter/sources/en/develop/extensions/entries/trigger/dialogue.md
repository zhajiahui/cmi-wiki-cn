# DialogueEntry

The `DialogueEntry` is used to define a type of dialogue. When a `DialogueEntry` is triggered it's associated `DialogueMessenger` will be used to display the dialogue to the player.
Multiple `DialogueMessenger`'s can be associated with a single `DialogueEntry` and the `DialogueMessenger` that is used is determined by the `DialogueMessenger`'s `MessengerFilter`.

**info**

There can always be at most one `DialogueEntry` active for a player.
This is automatically handled by Typewriter.

## Usage {#usage}

ExampleDialogueEntry.kt

```kotlin
@Entry("example_dialogue", "An example dialogue entry.", Colors.BLUE, "material-symbols:chat-rounded")
class ExampleDialogueEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
    override val speaker: Ref<SpeakerEntry> = emptyRef(),
    @MultiLine
    @Placeholder
    @Colored
    @Help("The text to display to the player.")
    val text: String = "",
) : DialogueEntry {
    // May return null to skip the dialogue
    override fun messenger(player: Player, context: InteractionContext): DialogueMessenger<*>? {
        // You can use if statements to return a different messenger depending on different conditions
        return ExampleDialogueDialogueMessenger(player, context, this)
    }
}
```

To define the messenger that will be used to display the dialogue to the player, you must create a class that implements the `DialogueMessenger` interface.

ExampleDialogueEntry.kt

```kotlin
class ExampleDialogueDialogueMessenger(player: Player, context: InteractionContext, entry: ExampleDialogueEntry) :
    DialogueMessenger<ExampleDialogueEntry>(player, context, entry) {

    // Called every game tick (20 times per second).
    // The cycle is a parameter that is incremented every tick, starting at 0.
    override fun tick(context: TickContext) {
        super.tick(context)
        if (state != MessengerState.RUNNING) return

        player.sendMessage("${entry.speakerDisplayName}: ${entry.text}".parsePlaceholders(player).asMini())

        // When we want the dialogue to end, we can set the state to FINISHED.
        state = MessengerState.FINISHED
    }
}
```

### Lifecycle {#lifecycle}

The `state` of the messenger determines what happens to the messenger.

- `MessengerState.FINISHED` - The dialogue is finished and the next dialogue in the chain will be triggered.
- `MessengerState.CANCELLED` - The dialogue is cancelled and dialogue chain is stopped, even if there are more dialogues in the chain.
- `MessengerState.RUNNING` - The dialogue is still running and will continue to run until the state is changed.

The state object can be changed inside the `tick` method or from outside. It can even be changed from the plugin itself. For example when the user runs a command the dialogue will be cancelled.

There are some additional lifecycle methods that can be overridden.

- `init` - Called when the messenger is initialized. Will be called before the first `tick` call.
- `dispose` - Called when the messenger is disposed. By default this will unregister any listeners that were registered by the messenger.
- `end` - Normally this does not need to be overwritten. Only if you do not want to resend the chat history for some reason.
