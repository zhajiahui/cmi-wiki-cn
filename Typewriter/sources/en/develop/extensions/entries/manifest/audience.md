# AudienceEntry

`AudienceEntry` is a crucial component in Typewriter that allows extension developers to display content to a group of players.
Typewriter manages the players in the audience, providing hooks that developers can use to show information or interact with the players in the audience.

The `AudienceEntry` is the most used `ManifestEntry` in Typewriter.

## Key Concepts {#key-concepts}

1. **Stateful Displays**: In Typewriter, entries are not allowed to have any state. `AudienceEntry` bridges this gap by providing a way to have stateful displays.
2. **Audience Management**: Typewriter takes care of managing the players in the audience. Developers can focus on defining how to display content and interact with the audience.
3. **Display Lifecycle**: The `AudienceDisplay` class manages the lifecycle of the audience, including initialization, player addition/removal, and disposal.

## Implementation {#implementation}

### Basic AudienceEntry {#basic-audienceentry}

Here's an example of a basic `AudienceEntry` implementation:

ExampleAudienceEntry.kt

```kotlin
@Entry("example_audience", "An example audience entry.", Colors.GREEN, "material-symbols:chat-rounded")
class ExampleAudienceEntry(
    override val id: String = "",
    override val name: String = "",
) : AudienceEntry {
    override suspend fun display(): AudienceDisplay {
        return ExampleAudienceDisplay()
    }
}
```

In this example, we define an `ExampleAudienceEntry` class that implements the `AudienceEntry` interface.
The `display()` function returns an `AudienceDisplay` object, which defines how the content is presented to the audience.

### AudienceDisplay {#audiencedisplay}

The `AudienceDisplay` class is responsible for displaying content to the audience.
It has lifecycle hooks to accomplish this.
Here's an example implementation:

ExampleAudienceEntry.kt

```kotlin
class ExampleAudienceDisplay : AudienceDisplay() {
    override fun initialize() {
        // This is called when the first player is added to the audience.
        super.initialize()
        // Do something when the audience is initialized
    }

    override fun onPlayerAdd(player: Player) {
        // Do something when a player gets added to the audience
    }

    override fun onPlayerRemove(player: Player) {
        // Do something when a player gets removed from the audience
    }

    override fun dispose() {
        super.dispose()
        // Do something when the audience is disposed
        // It will always call onPlayerRemove for all players.
        // So no player cleanup is needed here.
    }
}
```

Key methods in `AudienceDisplay`:

1. `initialize()`: Called when the first player is added to the audience. Use this method for any setup tasks.
2. `onPlayerAdd(player: Player)`: Invoked when a player joins the audience. Use this to set up player-specific content or effects.
3. `onPlayerRemove(player: Player)`: Called when a player leaves the audience. Use this for cleanup of player-specific resources.
4. `dispose()`: Invoked when the audience is being disposed of. Use this for general cleanup tasks. Note that `onPlayerRemove` will be called for all players, so player-specific cleanup is not needed here.

### Tickable Audience Display {#tickable-audience-display}

For audiences that need to update regularly, you can implement the `TickableDisplay` interface:

ExampleAudienceEntry.kt

```kotlin
class TickableAudienceDisplay : AudienceDisplay(), TickableDisplay {
    override fun onPlayerAdd(player: Player) {}
    override fun onPlayerRemove(player: Player) {}

    override fun tick() {
        // Do something when the audience is ticked
        players.forEach { player ->
            // Do something with the player
        }

        // This is running asynchronously
        // If you need to do something on the main thread
        Dispatchers.Sync.launch {
            // Though this will run a tick later, to sync with the bukkit scheduler.
        }
    }
}
```

The `tick()` method will be called every Minecraft tick (20 times per second, or every 50ms) on an asynchronous thread.
This allows you to update the display or perform regular actions for all players in the audience.

### Event Handling {#event-handling}

Every `AudienceDisplay` is also a Bukkit listener.
Event listeners will only be active when at least one player is in the audience.
Here's an example of how to handle events:

ExampleAudienceEntry.kt

```kotlin
class AudienceDisplayWithEvents : AudienceDisplay() {
    override fun onPlayerAdd(player: Player) {}
    override fun onPlayerRemove(player: Player) {}

    @EventHandler
    fun onSomeEvent(event: SomeBukkitEvent) {
        // Do something when the event is triggered
        // This will trigger for all players, not just the ones in the audience.
        // So we need to check if the player is in the audience.
        if (event.player in this) {
            // Do something with the player
        }
    }
}
```

**Events for All Players**

Events will trigger for ***all*** players, not just those in the audience.

**Always check if the player is in the audience before performing audience-specific actions.**

### Check if a player is in the audience of an entry {#check-if-a-player-is-in-the-audience-of-an-entry}

Suppose you have a `Ref<out AudienceEntry>`.
To check if a player is in the audience of an entry,
you can use the `player.inAudience` method that returns `true` if the player is in the audience of the entry.
This is incredibly convenient, especially because it automatically handles all parents of the entry for you as well.
Here's an example:

ExampleAudienceEntry.kt

```kotlin
    if (player.inAudience(ref)) {
        // Do something with the player
    }
```

## Best Practices {#best-practices}

1. **State Management**: While state is allowed within the `AudienceDisplay`, ensure that all used state is contained within the display and does not leak outside.
2. **Resource Management**: Ensure proper resource management to avoid memory leaks, especially when players leave the audience.
3. **Event Handling**: When handling Bukkit events, always check if the player is in the audience before performing audience-specific actions.
4. **Asynchronous Operations**: Be mindful that the `tick()` method runs on an asynchronous thread. Ensure thread safety when interacting with Bukkit API or shared resources.
