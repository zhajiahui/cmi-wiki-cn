# SpeakerEntry

The `SpeakerEntry` is a specialized interface extending the `EntityEntry`.
It is designed to enhance dialogues in the game by associating non-player characters (NPCs) with specific names and sounds.
This feature is pivotal for creating more immersive and interactive storytelling experiences in Minecraft.

## Usage {#usage}

ExampleSpeakerEntry.kt

```kotlin
@Entry("example_speaker", "An example speaker entry.", Colors.BLUE, "ic:round-spatial-audio-off")
class ExampleSpeakerEntry(
    override val id: String = "",
    override val name: String = "",
    override val displayName: Var<String> = ConstVar(""),
    override val sound: Var<Sound> = ConstVar(Sound.EMPTY),
) : SpeakerEntry
```

This speaker can be used by users in various dialogues and interactions within the game.
You almost never need to access the `SpeakerEntry` directly, as it is automatically handled by the `DialogueSequence`.
