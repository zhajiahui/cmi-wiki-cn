---
title: 受众条目（AudienceEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/manifest/audience
source_version: 0.8.0
---

# 受众条目（AudienceEntry）

`AudienceEntry`是Typewriter中的重要组件，它允许扩展开发人员向一组玩家显示内容。
Typewriter管理受众中的玩家，提供开发者可以用来展示信息或与受众中的玩家互动的钩子。

`AudienceEntry`是Typewriter中使用最多的`ManifestEntry`。

## 关键概念 {#key-concepts}

1. **有状态显示**：在Typewriter中，条目不允许有任何状态。`AudienceEntry`通过提供一种具有状态显示的方法来弥补这一差距。
2. **受众管理**：Typewriter负责管理受众中的玩家。开发人员可以专注于定义如何显示内容并与受众互动。
3. `AudienceDisplay` 管理受众显示的生命周期，包括初始化、玩家加入与移除，以及销毁。

## 实现 {#implementation}

### 基本 AudienceEntry {#basic-audienceentry}

以下是基本`AudienceEntry`实现的示例：

ExampleAudienceEntry.kt

```kotlin
@Entry("example_audience", "An example audience entry.", Colors.GREEN, "material-symbols:chat-rounded")
class ExampleAudienceEntry(
    override val id: String = "",
    override val name: String = "",
) : AudienceEntry {
    override suspend fun display(): AudienceDisplay {
        return ExampleAudienceDisplay()
    }
}
```

在此示例中，我们定义了一个实现`AudienceEntry`接口的`ExampleAudienceEntry`类。
`display()`函数返回一个`AudienceDisplay`对象，该对象定义如何向受众呈现内容。

### 受众显示 {#audiencedisplay}

`AudienceDisplay`类负责向受众显示内容。
它有生命周期挂钩来完成此任务。
这是一个示例实现：

ExampleAudienceEntry.kt

```kotlin
class ExampleAudienceDisplay : AudienceDisplay() {
    override fun initialize() {
        // This is called when the first player is added to the audience.
        super.initialize()
        // Do something when the audience is initialized
    }

    override fun onPlayerAdd(player: Player) {
        // Do something when a player gets added to the audience
    }

    override fun onPlayerRemove(player: Player) {
        // Do something when a player gets removed from the audience
    }

    override fun dispose() {
        super.dispose()
        // Do something when the audience is disposed
        // It will always call onPlayerRemove for all players.
        // So no player cleanup is needed here.
    }
}
```

`AudienceDisplay`中的关键方法：

1. `initialize()`：当第一个玩家添加到受众中时调用。使用此方法执行任何设置任务。
2. `onPlayerAdd(player: Player)`：当玩家加入受众时调用。使用它来设置特定于玩家的内容或效果。
3. `onPlayerRemove(player: Player)`：当玩家离开受众时调用。使用它来清理特定于玩家的资源。
4. `dispose()`：受众被销毁时调用，用于通用的清理工作。系统会对所有玩家调用 `onPlayerRemove`，因此这里无需再做针对单个玩家的清理。

### 可逐 tick 更新的受众显示 {#tickable-audience-display}

对于需要定期更新的受众，可以实现`TickableDisplay`接口：

ExampleAudienceEntry.kt

```kotlin
class TickableAudienceDisplay : AudienceDisplay(), TickableDisplay {
    override fun onPlayerAdd(player: Player) {}
    override fun onPlayerRemove(player: Player) {}

    override fun tick() {
        // Do something when the audience is ticked
        players.forEach { player ->
            // Do something with the player
        }

        // This is running asynchronously
        // If you need to do something on the main thread
        Dispatchers.Sync.launch {
            // Though this will run a tick later, to sync with the bukkit scheduler.
        }
    }
}
```

`tick()` 在异步线程中每个 Minecraft tick 调用一次，即每秒 20 次，或每 50 毫秒一次。
这允许你更新显示或为受众中的所有玩家执行常规操作。

### 事件处理 {#event-handling}

每个`AudienceDisplay`也是一个Bukkit监听器。
受众中至少有一位玩家时，事件监听器才会启用。
以下是如何处理事件的示例：

ExampleAudienceEntry.kt

```kotlin
class AudienceDisplayWithEvents : AudienceDisplay() {
    override fun onPlayerAdd(player: Player) {}
    override fun onPlayerRemove(player: Player) {}

    @EventHandler
    fun onSomeEvent(event: SomeBukkitEvent) {
        // Do something when the event is triggered
        // This will trigger for all players, not just the ones in the audience.
        // So we need to check if the player is in the audience.
        if (event.player in this) {
            // Do something with the player
        }
    }
}
```

**适合所有玩家的事件**

***所有***玩家都会触发事件，而不仅仅是受众中的玩家。

**在执行针对受众的特定操作之前，请务必检查玩家是否在受众中。**

### 判断玩家是否属于条目的受众 {#check-if-a-player-is-in-the-audience-of-an-entry}

假设你有`Ref<out AudienceEntry>`。
要检查玩家是否在条目的受众中，
可以使用 `player.inAudience` 方法；玩家属于条目受众时，它返回 `true`。
这非常方便，特别是因为它还会自动为你处理条目的所有父项。
这是一个例子：

ExampleAudienceEntry.kt

```kotlin
    if (player.inAudience(ref)) {
        // Do something with the player
    }
```

## 实践建议 {#best-practices}

1. **状态管理**：`AudienceDisplay` 中允许保存状态，但这些状态应局限于该显示对象内部，避免泄漏到外部。
2. **资源管理**：确保适当的资源管理以避免内存泄漏，特别是当玩家离开受众时。
3. **事件处理**：处理Bukkit事件时，在执行特定于受众的操作之前，请务必检查玩家是否在受众中。
4. **异步操作**：请注意，`tick()`方法在异步线程上运行。确保与BukkitAPI或共享资源交互时的线程安全。

---

原文：[AudienceEntry](https://docs.typewritermc.com/develop/extensions/entries/manifest/audience) · 文档版本：0.8.0
