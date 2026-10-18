---
title: 交互系统（Interaction System）
source: https://docs.typewritermc.com/develop/extensions/interactions
source_version: 0.8.0
---

# 交互系统（Interaction System）

交互系统提供了一个框架，用于管理需要随时间运行的有状态玩家交互。
示例包括过场动画、对话或自定义游戏模式。
该系统由两个主要组件组成：触发器处理程序和交互。

**说明**

在任何给定时刻，玩家一次只能进行一次交互。
无论交互类型如何。如果你需要多次交互，可以使用[受众条目](entries/manifest/audience.md)来管理它们。

## 核心概念 {#core-concepts}

交互遵循特定的生命周期：

1. 条目引发带有启动触发器的事件
2. TriggerHandler 处理该事件并创建交互
3. 交互初始化，并开始逐 tick 更新。
4. 当交互应该结束时，它会引发停止触发器
5. TriggerHandler处理停止触发器并结束Interaction

## 基本实现 {#basic-implementation}

这是实现交互的基本示例：

ExampleInteraction.kt

```kotlin
class ExampleInteraction(
    val player: Player,
    override val context: InteractionContext,
    override val priority: Int,
    val eventTriggers: List<EventTrigger>
) : Interaction {
    override suspend fun initialize(): Result<Unit> {
        if (Random.nextBoolean()) {
            // Failing during initialization makes it so that the interaction will be stopped.
            return failure("Failed to initialize")
        }

        // Setup your interaction state
        player.sendMessage("Starting interaction!")

        return ok(Unit)
    }

    override suspend fun tick(deltaTime: Duration) {
        // Update your interaction state
        if (shouldEnd()) {
            // Trigger the stop event when done
            ExampleStopTrigger.triggerFor(player, context)
        }
    }

    override suspend fun teardown() {
        // Cleanup your interaction state
        player.sendMessage("Ending interaction!")
    }

    private fun shouldEnd(): Boolean = false // Your end condition
}
```

Interaction 类处理实际的状态和行为。要点：

- `initialize()`设置初始状态
- `tick()`随着时间的推移更新状态
- `teardown()`交互结束时进行清理
- 优先级来自开始交互的条目

## 触发系统 {#trigger-system}

触发系统管理交互的启动和停止。

交互应该通过引发其特定的启动触发器来启动。
也可以发出相应的停止触发器，让交互平稳结束。

ExampleInteraction.kt

```kotlin
// Trigger to start the interaction
data class ExampleStartTrigger(
    val priority: Int,
    val eventTriggers: List<EventTrigger> = emptyList()
) : EventTrigger {
    override val id: String = "example.start"
}

// Trigger to stop the interaction
data object ExampleStopTrigger : EventTrigger {
    override val id: String = "example.stop"
}
```

### 触发处理器 {#trigger-handlers}

处理程序负责：

1. 从开始触发器创建新的交互
2. 收到停止触发器时结束交互

它也可以修改当前交互的状态或行为。
例如，它可以替换对话。

ExampleInteraction.kt

```kotlin
@Singleton // This registers the handler to Typewriter
class ExampleTriggerHandler : TriggerHandler {
    override suspend fun trigger(event: Event, currentInteraction: Interaction?): TriggerContinuation {
        // Handle stopping the interaction
        if (ExampleStopTrigger in event && currentInteraction is ExampleInteraction) {
            return TriggerContinuation.Multi(
                TriggerContinuation.EndInteraction,
                TriggerContinuation.Append(
                    Event(
                        event.player,
                        currentInteraction.context,
                        currentInteraction.eventTriggers
                    )
                ),
            )
        }

        // Handle starting the interaction
        return tryStartExampleInteraction(event)
    }

    private fun tryStartExampleInteraction(
        event: Event
    ): TriggerContinuation {
        // Find all start triggers in the event
        val triggers = event.triggers
            .filterIsInstance<ExampleStartTrigger>()

        if (triggers.isEmpty()) return TriggerContinuation.Nothing

        // Use the highest priority trigger
        val trigger = triggers.maxBy { it.priority }

        // Start the interaction
        return TriggerContinuation.StartInteraction(
            ExampleInteraction(
                event.player,
                event.context,
                trigger.priority,
                trigger.eventTriggers
            )
        )
    }
}
```

## 激活交互 {#activating-the-interaction}

需要一些东西来开始交互。
这可以是任何条目。
对于此示例，我们有一个操作条目，触发时会启动交互。

ExampleInteraction.kt

```kotlin
@Entry("example_interaction", "Start an example interaction", Colors.RED, "mdi:play")
class ExampleInteractionActionEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
) : ActionEntry {
    // Preventing the `triggers` from being used, instead we pass them to the interaction
    // And also start the interaction when the entry is triggered.
    override val eventTriggers: List<EventTrigger>
        get() = listOf(
            ExampleStartTrigger(
                this.priority,
                super.eventTriggers
            )
        )

    override fun ActionTrigger.execute() {}
}
```

## 流程示例 {#flow-example}

以下是一切如何协同工作的：

```text
1. Player triggers ExampleInteractionActionEntry
2. Entry creates ExampleStartTrigger
3. ExampleTriggerHandler receives the trigger
4. Handler creates ExampleInteraction
5. Interaction get initialized (automatically)
6. Interaction runs until end condition met
7. Interaction raises ExampleStopTrigger
8. Handler processes stop trigger
9. Interaction teardown is called (automatically)
```

## 优先级系统 {#priority-system}

有些互动比其他互动更重要。
由于一次只能有 1 个交互处于活动状态，因此优先级系统可确保最重要的交互处于活动状态。
确保一些随机的闲置对话不会打断故事关键的过场动画。

仅当正在运行的交互的优先级低于或等于新交互的优先级时，才能启动交互。

例如，玩家正在观看优先级为 1 的过场动画时，如果触发了优先级为 0 的闲置对话，该对话不会打断过场动画。

---

原文：[Interaction System](https://docs.typewritermc.com/develop/extensions/interactions) · 文档版本：0.8.0
