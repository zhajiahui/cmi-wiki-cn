---
title: 对话条目（DialogueEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/trigger/dialogue
source_version: 0.8.0
---

# 对话条目（DialogueEntry）

`DialogueEntry`用于定义一种对话类型。当`DialogueEntry`被触发时，其关联的`DialogueMessenger`将用于向玩家显示对话。
多个`DialogueMessenger`可以与单个`DialogueEntry`关联，所使用的`DialogueMessenger`由`DialogueMessenger`的`MessengerFilter`确定。

**说明**

一名玩家最多只能有一个`DialogueEntry`处于活动状态。
这是由Typewriter自动处理的。

## 用法 {#usage}

ExampleDialogueEntry.kt

```kotlin
@Entry("example_dialogue", "An example dialogue entry.", Colors.BLUE, "material-symbols:chat-rounded")
class ExampleDialogueEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
    override val speaker: Ref<SpeakerEntry> = emptyRef(),
    @MultiLine
    @Placeholder
    @Colored
    @Help("The text to display to the player.")
    val text: String = "",
) : DialogueEntry {
    // May return null to skip the dialogue
    override fun messenger(player: Player, context: InteractionContext): DialogueMessenger<*>? {
        // You can use if statements to return a different messenger depending on different conditions
        return ExampleDialogueDialogueMessenger(player, context, this)
    }
}
```

要定义用于向玩家显示对话的Messenger，你必须创建一个实现`DialogueMessenger`接口的类。

ExampleDialogueEntry.kt

```kotlin
class ExampleDialogueDialogueMessenger(player: Player, context: InteractionContext, entry: ExampleDialogueEntry) :
    DialogueMessenger<ExampleDialogueEntry>(player, context, entry) {

    // Called every game tick (20 times per second).
    // The cycle is a parameter that is incremented every tick, starting at 0.
    override fun tick(context: TickContext) {
        super.tick(context)
        if (state != MessengerState.RUNNING) return

        player.sendMessage("${entry.speakerDisplayName}: ${entry.text}".parsePlaceholders(player).asMini())

        // When we want the dialogue to end, we can set the state to FINISHED.
        state = MessengerState.FINISHED
    }
}
```

### 生命周期 {#lifecycle}

Messenger的`state`决定了Messenger会发生什么。

- `MessengerState.FINISHED`- 对话结束，将触发链中的下一个对话。
- `MessengerState.CANCELLED`- 对话被取消并且对话链被停止，即使链中还有更多对话。
- `MessengerState.RUNNING`- 对话仍在运行，并将继续运行，直到状态改变。

状态对象可以在`tick`方法内部或从外部更改。它甚至可以从插件本身进行更改。例如，当用户运行命令时，对话将被取消。

还有一些可以重写的附加生命周期方法。

- `init`- 初始化Messenger时调用。将在第一个`tick`调用之前调用。
- `dispose`- 当Messenger被处置时调用。默认情况下，这将取消注册由Messenger注册的任何侦听器。
- `end`- 通常不需要覆盖。仅当你出于某种原因不想重新发送聊天记录时。

---

原文：[DialogueEntry](https://docs.typewritermc.com/develop/extensions/entries/trigger/dialogue) · 文档版本：0.8.0
