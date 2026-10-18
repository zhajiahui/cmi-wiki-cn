# CinematicEntry

The `CinematicEntry` does not have any decentends, but is very customizable. When a entry is needed in a cinematic page, it needs to inherit this.

`CinematicEntry` works by having at least 1 list of `Segment`'s. Segments are the parts of the cinematic and may have sub-properties defined. A segment needs to have at least a `startFrame` and `endFrame` which are the integers of the frames.

Frames are the ticks in a second. So there are 20 frames in a second. A cinematic takes as long as the latest `endFrame` of a segment from all it's entries.

Segments are defined in the entry using the `@Segments` annotation. And it needs to be a list of `Segment`'s.

**info**

A `CinematicEntry` can have multiple different segment tracks.
For example, a cinematic entry may have a `TextSegment` and a `SoundSegment`.

Though this is supported in the plugin, it is not yet implemented in the cinematic editor.
If you need this, reach out to me on [Discord](https://discord.gg/HtbKyuDDBw).

As entries are not allowed to have any state, we create a `CinematicAction` everytime a entry is used in a cinematic for a player.

## Usage {#usage}

ExampleCinematicEntry.kt

```kotlin
@Entry("example_cinematic", "An example cinematic entry", Colors.BLUE, "material-symbols:cinematic-blur")
class ExampleCinematicEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    @Segments(Colors.BLUE, "material-symbols:cinematic-blur")
    val segments: List<ExampleSegment> = emptyList(),
) : CinematicEntry {
    override fun create(player: Player): CinematicAction {
        return ExampleCinematicAction(player, this)
    }
}
```

Segments sometimes need a minimum or maximum duration. This can be done using the `@InnerMin` and `@InnerMax` annotations.

ExampleCinematicEntry.kt

```kotlin
    @Segments(Colors.BLUE, "material-symbols:cinematic-blur")
    @InnerMin(Min(10))
    @InnerMax(Max(20))
    val segments: List<ExampleSegment> = emptyList(),
```

This will make sure that the segment will be at least 10 frames long and at most 20 frames long.

### ExampleSegment {#examplesegment}

ExampleCinematicEntry.kt

```kotlin
data class ExampleSegment(
    override val startFrame: Int = 0,
    override val endFrame: Int = 0,
) : Segment
```

### ExampleCinematicAction {#examplecinematicaction}

The `CinematicAction` is the action that is created when a cinematic is started. It is used to keep track of the current frame and to execute the segments.
There are a few different lifecycle methods that can be used.

- `setup()` is called when the cinematic is created. This is the place to initialize any variables, spawn entities, etc.
- `tick(frame: Int)` is called every frame. This is the place to execute the segments. It is even executed when no segments are active.
- `teardown()` is called when the cinematic is finished. This is the place to remove any entities, etc.
- `canFinish(frame: Int)` the only method that needs to be implemented. It is used by the `CinematicSequence` to determine if the cinematic is finished.

If you need all the customization, you can can implement the `CinematicAction` directly:

ExampleCinematicEntry.kt

```kotlin
class ExampleCinematicAction(
    val player: Player,
    val entry: ExampleCinematicEntry,
) : CinematicAction {
    override suspend fun setup() {
        // Initialize variables, spawn entities, etc.
    }

    override suspend fun tick(frame: Int) {
        val segment = entry.segments activeSegmentAt frame
        // Can be null if no segment is active

        // The `frame` parameter is not necessarily next frame: `frame != old(frame)+1`

        // Execute tick logic for the segment
    }

    override suspend fun teardown() {
        // Remove entities, etc.
    }

    override fun canFinish(frame: Int): Boolean = entry.segments canFinishAt frame
}
```

### SimpleCinematicAction {#simplecinematicaction}

Sometimes you don't need all the customization and flexiblity. If you only care about 1 segment track, and only need to do something when a segment starts or ends, you can use the `SimpleCinematicAction`.

ExampleCinematicEntry.kt

```kotlin
class ExampleSimpleTemporalAction(
    val player: Player,
    entry: ExampleCinematicEntry,
) : SimpleCinematicAction<ExampleSegment>() {
    override val segments: List<ExampleSegment> = entry.segments

    override suspend fun startSegment(segment: ExampleSegment) {
        super.startSegment(segment) // Keep this
        // Called when a segment starts
    }

    override suspend fun tickSegment(segment: ExampleSegment, frame: Int) {
        super.tickSegment(segment, frame) // Keep this
        // Called every tick while the segment is active
        // Will always be called after startSegment and never after stopSegment

        // The `frame` parameter is not necessarily next frame: `frame != old(frame)+1`
    }

    override suspend fun stopSegment(segment: ExampleSegment) {
        super.stopSegment(segment) // Keep this
        // Called when the segment ends
        // Will also be called if the cinematic is stopped early
    }
}
```

## Ticking {#ticking}

One important detail is that the `tick` methods are not necessarily called in order.
It is important that the tick method should show the state of the action at the given frame.

One place where this is definitely the case is when the player is viewing the cinematic in content mode.
As the player is able to scroll through the cinematic, it might be the case that multiple frames are skipped, or rewinded.

## Simulation & Recording {#simulation--recording}

Sometimes the cinematic should be different when it is being recorded or simulated.
Like the blinding cinematic, where you don't want to be blinded during simulation/recording.
Or you want to show a different thing during simulation/recording.
Like the camera which displays the camera in the world, instead of setting the player's camera.

To do this, there are 2 additional methods that can be implemented on the `CinematicEntry` that can return a different `CinematicAction` for recording and simulation.

ExampleCinematicEntry.kt

```kotlin
    // This will be used when the cinematic is normally displayed to the player.
    override fun create(player: Player): CinematicAction {
        return DefaultCinematicAction(player, this)
    }

    // This is used during content mode to display the cinematic to the player.
    // It may be null to not show it during simulation.
    override fun createSimulating(player: Player): CinematicAction? {
        return SimulatedCinematicAction(player, this)
    }

    // This is used during content mode to record the cinematic.
    // It may be null to not record it during simulation.
    override fun createRecording(player: Player): CinematicAction? {
        return RecordingCinematicAction(player, this)
    }
```
