# AudienceFilter

The `AudienceFilterEntry` is a specialized version of `AudienceEntry` designed to filter audience members based on specific criteria.
It accepts a list of children that can include both `AudienceEntry` and `AudienceFilterEntry` components.

## Basic Usage {#basic-usage}

### Static Filtering {#static-filtering}

Here's an example of a filter that only allows players whose names start with 'g':

ExampleAudienceFilter.kt

```kotlin
class ExampleAudienceFilter(
    ref: Ref<out AudienceFilterEntry>
) : AudienceFilter(ref) {
    override fun filter(player: Player): Boolean {
        return player.name.startsWith("g")
    }
}
```

This filter is static because player names cannot be changed while on the server.
Players are either filtered at the start or not at all.

### Dynamic Filtering {#dynamic-filtering}

For more dynamic filtering, you can filter based on changing player attributes, such as health:

ExampleAudienceFilter.kt

```kotlin
class HealthAudienceFilter(
    ref: Ref<out AudienceFilterEntry>,
    private val healthRange: ClosedFloatingPointRange<Float> = 0f..20f
) : AudienceFilter(ref), TickableDisplay {
    override fun filter(player: Player): Boolean {
        return player.health in healthRange
    }

    // You can refresh the filters on events
    @EventHandler
    fun healthRegent(event: EntityRegainHealthEvent) {
        val player = event.entity as? Player ?: return
        // Reruns the filter
        player.refresh()

        // Or if you know the player should be filtered, you can update the filter directly
        player.updateFilter(isFiltered = event.amount in healthRange)
    }

    // It is also possible to run the filter every tick
    override fun tick() {
        // Refresh the filter for all considered players
        consideredPlayers.forEach { it.refresh() }
    }
}
```

This example filters players based on their health value, which is provided as a parameter from the entry.
Like `AudienceDisplay`, we can use both Bukkit events and `TickableDisplay` to update which players pass through the filter.

### Invertible Filters {#invertible-filters}

Sometimes you may want to invert a filter's behavior.
This is particularly useful when the opposite condition would be complex to define explicitly, such as filtering all players that are not in a specific world:

ExampleAudienceFilter.kt

```kotlin
@Entry("inverted_example_audience_filter", "An example audience filter.", Colors.MYRTLE_GREEN, "material-symbols:filter-alt")
class InvertedExampleAudienceFilterEntry(
    override val id: String = "",
    override val name: String = "",
    override val children: List<Ref<out AudienceEntry>> = emptyList(),
    override val inverted: Boolean = true,
) : AudienceFilterEntry, Invertible {
    override suspend fun display(): AudienceFilter = ExampleAudienceFilter(ref())
}
```

Simply implementing the `Invertible` interface enables this functionality in Typewriter.
