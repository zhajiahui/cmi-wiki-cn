# SingleFilter

The `SingleFilter` is a specialized variant of `AudienceFilter` that ensures only one filter instance can be active for a player at any given time. This is particularly useful for managing exclusive displays like tab list headers/footers or scoreboard sidebars.

## Basic Usage {#basic-usage}

Here's a basic example of implementing a single filter:

ExampleAudienceSingleFilter.kt

```kotlin
@Entry("example_single_filter", "An example single filter entry", Colors.MYRTLE_GREEN, "material-symbols:filter-alt")
class ExampleSingleFilterEntry(
    override val id: String = "",
    override val name: String = "",
    override val priorityOverride: Optional<Int> = Optional.empty(),
) : AudienceFilterEntry, PriorityEntry {
    override val children: List<Ref<out AudienceEntry>> get() = emptyList()

    override suspend fun display(): AudienceFilter = ExampleSingleFilter(ref()) { player ->
        PlayerExampleDisplay(player, ExampleSingleFilter::class, ref())
    }
}

private class ExampleSingleFilter(
    ref: Ref<ExampleSingleFilterEntry>,
    createDisplay: (Player) -> PlayerExampleDisplay,
) : SingleFilter<ExampleSingleFilterEntry, PlayerExampleDisplay>(ref, createDisplay) {
    // This must be a references to a shared map.
    // It CANNOT cache the map itself.
    override val displays: MutableMap<UUID, PlayerExampleDisplay>
        get() = map

    companion object {
        // This map is shared between all instances of the filter.
        private val map = ConcurrentHashMap<UUID, PlayerExampleDisplay>()
    }
}

private class PlayerExampleDisplay(
    player: Player,
    displayKClass: KClass<out SingleFilter<ExampleSingleFilterEntry, *>>,
    current: Ref<ExampleSingleFilterEntry>
) : PlayerSingleDisplay<ExampleSingleFilterEntry>(player, displayKClass, current) {
    override fun setup() {
        super.setup()
        player.sendMessage("Display activated!")
    }

    override fun tearDown() {
        super.tearDown()
        player.sendMessage("Display deactivated!")
    }
}
```

The `SingleFilter` consists of three main components:

1. An entry class that defines the configuration and creates the filter
2. A filter class that manages the shared state between instances
3. A display class that handles the player-specific display logic

## Display Lifecycle {#display-lifecycle}

The display lifecycle is a crucial concept in SingleFilter as it manages how displays are created, updated, and removed. Let's look at a practical example:

ExampleAudienceSingleFilter.kt

```kotlin
private class ComplexPlayerDisplay(
    player: Player,
    displayKClass: KClass<out SingleFilter<ExampleSingleFilterEntry, *>>,
    current: Ref<ExampleSingleFilterEntry>
) : PlayerSingleDisplay<ExampleSingleFilterEntry>(player, displayKClass, current) {
    override fun initialize() {
        super.initialize()
        // Called once when the display is first created
        player.sendMessage("Display initialized!")
    }

    override fun setup() {
        super.setup()
        // Called every time this display becomes active
        player.sendMessage("Display setup!")
    }

    override fun tick() {
        // Called every tick while the display is active
        // Update display content here
    }

    override fun tearDown() {
        super.tearDown()
        // Called when this display becomes inactive
        player.sendMessage("Display torn down!")
    }

    override fun dispose() {
        super.dispose()
        // Called when the display is being completely removed
        player.sendMessage("Display disposed!")
    }
}
```

Let's walk through what happens in different scenarios:

### Scenario 1: Player Joins Server {#scenario-1-player-joins-server}

```text
1. Player joins
2. initialize() called once - Creates the display instance
3. setup() called - Activates the display with initial entry
4. tick() starts running periodically
```

### Scenario 2: Higher Priority Entry Becomes Active {#scenario-2-higher-priority-entry-becomes-active}

```text
1. New entry with higher priority includes player in its audience
2. tearDown() called on current display
3. setup() called with new entry
4. Same display instance continues, but with new entry reference
5. tick() continues running with new entry data
```

### Scenario 3: Player Leaves Entry's Audience {#scenario-3-player-leaves-entrys-audience}

```text
1. Player is filtered out of current entry's audience
2. System looks for next highest priority entry where player is in audience
3. If found:
   - tearDown() called with old entry
   - setup() called with new entry
   - Display continues with new entry
4. If not found:
   - tearDown() called
   - dispose() called
   - Display is completely removed
```

The display lifecycle ensures smooth transitions between different entries while maintaining the single display state. This is particularly important for exclusive displays where you want to avoid flickering or interruptions when switching between different configurations.

### Priority Behavior {#priority-behavior}

The priority of entries determines which display becomes active when multiple entries include a player in their audience. For example:

```kotlin
Entry A (priority: 50) - Basic display
Entry B (priority: 100) - Special display

Scenario:
1. Player joins -> Entry B becomes active (higher priority)
2. Player leaves Entry B's audience -> Entry A becomes active (next highest)
3. Player returns to Entry B's audience -> Switches back to Entry B
```

This priority system ensures that more important displays can temporarily override less important ones, while maintaining a fallback when a player is no longer in the audience of higher priority entries.
