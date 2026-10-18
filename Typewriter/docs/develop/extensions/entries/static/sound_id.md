---
title: 声音 ID 条目（SoundIdEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/static/sound_id
source_version: 0.8.0
---

# 声音 ID 条目（SoundIdEntry）

`SoundIdEntry`是一个源自`StaticEntry`的接口，专门设计用于管理TypewriterSpigot插件中的自定义声音。
如果服务器使用自定义资源包，则可以使用`SoundIdEntry`在资源包中添加对自定义声音的引用。

## 用法 {#usage}

ExampleSoundIdEntry.kt

```kotlin
@Entry("example_sound", "An example sound entry.", Colors.BLUE, "icon-park-solid:volume-up")
class ExampleSoundIdEntry(
    override val id: String = "",
    override val name: String = "",
    override val soundId: String = "",
) : SoundIdEntry
```

需要声音的条目会通过该接口处理 `SoundIdEntry`。

---

原文：[SoundIdEntry](https://docs.typewritermc.com/develop/extensions/entries/static/sound_id) · 文档版本：0.8.0
