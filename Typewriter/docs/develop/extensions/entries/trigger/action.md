---
title: 动作条目（ActionEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/trigger/action
source_version: 0.8.0
---

# 动作条目（ActionEntry）

`ActionEntry`定义要采取的操作。当它被触发时，它将运行它的`execute`方法。
之后它将触发链中的所有下一个条目。

**不可变条目**

需要强调的是，该条目必须是不可变的。
**它不能有任何可变状态。**

## 用法 {#usage}

ExampleActionEntry.kt

```kotlin
@Entry("example_action", "An example action entry.", Colors.RED, "material-symbols:touch-app-rounded")
class ExampleActionEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
) : ActionEntry {
    override fun ActionTrigger.execute() {
        // Do something with the player
    }
}
```

在调用`execute`方法后，Typewriter将自动触发链中的下一个条目，并应用所有修改器。

有时你希望对何时触发下一个触发器或触发哪些触发器有更多的控制。

ExampleActionEntry.kt

```kotlin
    override fun ActionTrigger.execute() {
        // This disables Typewriter's automatic triggering of the next entries,
        // and disables the automatic apply of the modifiers.
        disableAutomaticTriggering()

        // Now you can manually trigger the next entries.
        triggerManually()

        // Or if you want to specify which triggers to trigger, you can do so.
        triggers.filterIndexed { index, _ -> index % 2 == 0 }.triggerFor(player)

        // You can also manually apply the modifiers.
        applyModifiers()
    }
```

---

原文：[ActionEntry](https://docs.typewritermc.com/develop/extensions/entries/trigger/action) · 文档版本：0.8.0
