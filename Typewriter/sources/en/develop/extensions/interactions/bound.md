# Interaction Bound

The InteractionBounds allows you to constrain the lifetime of an interactions to specific conditions, such as player location or actions.
For example, a player staying within range of an NPC during a conversation or while they are sitting on a bench.

## States and Behavior {#states-and-behavior}

InteractionBounds operate in three states:

1. **INTERRUPTING**: When the bound condition is broken (e.g., player moves too far), the interaction ends
2. **BLOCKING**: Prevents the bound from being broken (e.g., cancels movement beyond the allowed range)
3. **IGNORING**: Bound conditions are not enforced (e.g., player can move freely)

**warning**

The bound itself doesn't determine the state - it only responds to the current state provided by the system.

## Implementation {#implementation}

Here's how to create a interaction bound:

ExampleInteractionBound.kt

```kotlin
@Entry("example_bound", "An example interaction bound", Colors.MEDIUM_PURPLE, "mdi:square-rounded")
class ExampleBoundEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
    override val interruptTriggers: List<Ref<TriggerableEntry>> = emptyList(),
) : InteractionBoundEntry {
    override fun build(player: Player): InteractionBound =
        ExampleBound(player, priority, interruptTriggers.eventTriggers)
}

class ExampleBound(
    private val player: Player,
    override val priority: Int,
    override val interruptionTriggers: List<EventTrigger>,
) : ListenerInteractionBound {

    override suspend fun initialize() {
        super.initialize()
        // Setup initial state
    }

    override suspend fun transitionTo(bound: InteractionBound): Boolean {
        // Called before this bound is replaced
        // Return false to cancel the transition
        return true
    }

    override suspend fun transitionFrom(bound: InteractionBound) {
        // Called after becoming the new bound
        // Use this to inherit state from the previous bound
    }

    @EventHandler(priority = EventPriority.HIGHEST)
    private fun onPlayerAction(event: SomeCancellablePlayerEvent) {
        if (event.player.uniqueId != player.uniqueId) return

        if (boundConditionBroken()) {
            // For PlayerEvents, we have a handy method to handle the breaking
            handleEvent(event)

            // A manual version of the above
            when (event.player.boundState) {
                InteractionBoundState.BLOCKING -> event.isCancelled = true
                InteractionBoundState.INTERRUPTING -> event.player.interruptInteraction()
                InteractionBoundState.IGNORING -> {}
            }
        }
    }

    private fun boundConditionBroken(): Boolean {
        // Check if the bound condition is broken
        return false
    }

    override suspend fun tick() {
        // Do something every tick
    }

    override suspend fun teardown() {
        // Cleanup any state
        super.teardown()
    }
}
```

## Implementation Tips {#implementation-tips}

1. Always use `handleEvent()` for consistent state handling
2. Check player UUID to ensure you're handling the right player
3. Clean up resources in `teardown()`
4. Consider performance for frequently triggered events

## Example Flow {#example-flow}

Here's how a typical radius bound might work:

```text
1. Player starts interaction
2. Bound initializes with start location
3. Player moves:
   - Within range: No action
   - Beyond range:
     - If BLOCKING: Cancel movement
     - If INTERRUPTING: End interaction
     - If IGNORING: Allow movement
4. Interaction ends, bound tears down
```
