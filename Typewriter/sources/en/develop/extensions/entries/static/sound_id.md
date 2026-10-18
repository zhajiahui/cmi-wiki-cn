# SoundIdEntry

The `SoundIdEntry` is an interface derived from `StaticEntry`, specifically designed for managing custom sounds within the Typewriter Spigot plugin.
If a server is using a custom resource pack, the `SoundIdEntry` can be used to add a reference to a custom sound within the resource pack.

## Usage {#usage}

ExampleSoundIdEntry.kt

```kotlin
@Entry("example_sound", "An example sound entry.", Colors.BLUE, "icon-park-solid:volume-up")
class ExampleSoundIdEntry(
    override val id: String = "",
    override val name: String = "",
    override val soundId: String = "",
) : SoundIdEntry
```

A `SoundIdEntry` handled by the interface when an entry needs a sound.
