# SoundSourceEntry

The `SoundSourceEntry` class is used to have a sound play at a specific entity in the world. This can be a moving target like an NPC. The sound source can be used in an entry with a `Sound` parameter.

## Usage {#usage}

ExampleSoundSourceEntry.kt

```kotlin
@Entry("example_sound_source", "An example sound source entry.", Colors.BLUE, "ic:round-spatial-audio-off")
class ExampleSoundSourceEntry(
    override val id: String = "",
    override val name: String = "",
) : SoundSourceEntry, StaticEntry {
    override fun getEmitter(player: Player): SoundEmitter {
        // Return the emitter that should be used for the sound.
        // An entity should be provided.
        return SoundEmitter(player.entityId)
    }
}
```

This can be combined with other entry types like `Speaker`. For example, an NPC that speaks can also be a sound emitter.
