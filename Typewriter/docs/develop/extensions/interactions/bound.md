---
title: 交互边界（Interaction Bound）
source: https://docs.typewritermc.com/develop/extensions/interactions/bound
source_version: 0.8.0
---

# 交互边界（Interaction Bound）

InteractionBounds 允许你将交互的生命周期限制为特定条件，例如玩家位置或操作。
例如，玩家在对话期间或坐在长凳上时停留在 NPC 的范围内。

## 状态与行为 {#states-and-behavior}

InteractionBounds 在三种状态下运行：

1. **中断（INTERRUPTING）**：违反边界条件时结束交互，例如玩家走得太远。
2. **阻止（BLOCKING）**：阻止违反边界条件，例如取消超出允许范围的移动。
3. **忽略（IGNORING）**：不执行边界约束，例如允许玩家自由移动。

**警告**

边界本身不决定状态，只响应系统提供的当前状态。

## 实现 {#implementation}

以下是创建交互边界的方法：

ExampleInteractionBound.kt

```kotlin
@Entry("example_bound", "An example interaction bound", Colors.MEDIUM_PURPLE, "mdi:square-rounded")
class ExampleBoundEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    override val modifiers: List<Modifier> = emptyList(),
    override val triggers: List<Ref<TriggerableEntry>> = emptyList(),
    override val interruptTriggers: List<Ref<TriggerableEntry>> = emptyList(),
) : InteractionBoundEntry {
    override fun build(player: Player): InteractionBound =
        ExampleBound(player, priority, interruptTriggers.eventTriggers)
}

class ExampleBound(
    private val player: Player,
    override val priority: Int,
    override val interruptionTriggers: List<EventTrigger>,
) : ListenerInteractionBound {

    override suspend fun initialize() {
        super.initialize()
        // Setup initial state
    }

    override suspend fun transitionTo(bound: InteractionBound): Boolean {
        // Called before this bound is replaced
        // Return false to cancel the transition
        return true
    }

    override suspend fun transitionFrom(bound: InteractionBound) {
        // Called after becoming the new bound
        // Use this to inherit state from the previous bound
    }

    @EventHandler(priority = EventPriority.HIGHEST)
    private fun onPlayerAction(event: SomeCancellablePlayerEvent) {
        if (event.player.uniqueId != player.uniqueId) return

        if (boundConditionBroken()) {
            // For PlayerEvents, we have a handy method to handle the breaking
            handleEvent(event)

            // A manual version of the above
            when (event.player.boundState) {
                InteractionBoundState.BLOCKING -> event.isCancelled = true
                InteractionBoundState.INTERRUPTING -> event.player.interruptInteraction()
                InteractionBoundState.IGNORING -> {}
            }
        }
    }

    private fun boundConditionBroken(): Boolean {
        // Check if the bound condition is broken
        return false
    }

    override suspend fun tick() {
        // Do something every tick
    }

    override suspend fun teardown() {
        // Cleanup any state
        super.teardown()
    }
}
```

## 实现提示 {#implementation-tips}

1. 始终使用`handleEvent()`进行一致的状态处理
2. 检查玩家 UUID 以确保你正在处理正确的玩家
3. 清理`teardown()`中的资源
4. 考虑频繁触发事件的性能

## 流程示例 {#example-flow}

以下是典型半径边界的工作原理：

```text
1. Player starts interaction
2. Bound initializes with start location
3. Player moves:
   - Within range: No action
   - Beyond range:
     - If BLOCKING: Cancel movement
     - If INTERRUPTING: End interaction
     - If IGNORING: Allow movement
4. Interaction ends, bound tears down
```

---

原文：[Interaction Bound](https://docs.typewritermc.com/develop/extensions/interactions/bound) · 文档版本：0.8.0
