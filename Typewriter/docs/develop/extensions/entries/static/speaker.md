---
title: 说话者条目（SpeakerEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/static/speaker
source_version: 0.8.0
---

# 说话者条目（SpeakerEntry）

`SpeakerEntry`是扩展`EntityEntry`的专用接口。
它旨在通过将非玩家角色 (NPC) 与特定名称和声音相关联来增强游戏中的对话。
此功能对于在Minecraft中创建更具沉浸感和互动性的叙事体验至关重要。

## 用法 {#usage}

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

用户可以在游戏内的各种对话和交互中使用该说话者。
你几乎不需要直接访问`SpeakerEntry`，因为它是由`DialogueSequence`自动处理的。

---

原文：[SpeakerEntry](https://docs.typewritermc.com/develop/extensions/entries/static/speaker) · 文档版本：0.8.0
