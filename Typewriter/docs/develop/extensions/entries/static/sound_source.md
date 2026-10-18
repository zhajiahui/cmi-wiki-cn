---
title: 声音来源条目（SoundSourceEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/static/sound_source
source_version: 0.8.0
---

# 声音来源条目（SoundSourceEntry）

`SoundSourceEntry`类用于在世界上的特定实体上播放声音。这可以是像 NPC 这样的移动目标。该声源可以在带有`Sound`参数的条目中使用。

## 用法 {#usage}

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

这可以与其他条目类型（例如`Speaker`）结合使用。例如，会说话的 NPC 也可以是发声器。

---

原文：[SoundSourceEntry](https://docs.typewritermc.com/develop/extensions/entries/static/sound_source) · 文档版本：0.8.0
