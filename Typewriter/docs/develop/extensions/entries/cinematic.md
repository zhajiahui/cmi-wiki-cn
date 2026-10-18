---
title: 过场动画条目（CinematicEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/cinematic
source_version: 0.8.0
---

# 过场动画条目（CinematicEntry）

`CinematicEntry` 没有派生类型，但可自定义的部分很多。要在过场动画页面中提供条目，需要实现这个接口。

`CinematicEntry` 至少包含 1 个 `Segment` 列表。片段代表动画中的一部分，可定义子属性；至少要有整数类型的 `startFrame` 和 `endFrame`，表示起止帧。

帧与游戏 tick 对应，每秒有 20 帧。过场动画的总时长取决于所有条目片段中最晚的 `endFrame`。

用 `@Segments` 注解标记条目中的片段字段，字段类型必须是 `Segment` 列表。

**说明**

`CinematicEntry` 可以包含多条不同的片段轨道。
例如，过场动画条目可能具有`TextSegment`和`SoundSegment`。

尽管插件支持此功能，但尚未在过场动画编辑器中实现。
如果你需要这个，请通过[Discord](https://discord.gg/HtbKyuDDBw)与我联系。

由于条目不允许有任何状态，因此每次在玩家的动画中使用条目时，我们都会创建一个`CinematicAction`。

## 用法 {#usage}

ExampleCinematicEntry.kt

```kotlin
@Entry("example_cinematic", "An example cinematic entry", Colors.BLUE, "material-symbols:cinematic-blur")
class ExampleCinematicEntry(
    override val id: String = "",
    override val name: String = "",
    override val criteria: List<Criteria> = emptyList(),
    @Segments(Colors.BLUE, "material-symbols:cinematic-blur")
    val segments: List<ExampleSegment> = emptyList(),
) : CinematicEntry {
    override fun create(player: Player): CinematicAction {
        return ExampleCinematicAction(player, this)
    }
}
```

分段有时需要最小或最大持续时间。这可以使用`@InnerMin`和`@InnerMax`注解来完成。

ExampleCinematicEntry.kt

```kotlin
    @Segments(Colors.BLUE, "material-symbols:cinematic-blur")
    @InnerMin(Min(10))
    @InnerMax(Max(20))
    val segments: List<ExampleSegment> = emptyList(),
```

这将确保该片段的长度至少为 10 帧，最多为 20 帧。

### 示例段 {#examplesegment}

ExampleCinematicEntry.kt

```kotlin
data class ExampleSegment(
    override val startFrame: Int = 0,
    override val endFrame: Int = 0,
) : Segment
```

### 示例过场动画动作 {#examplecinematicaction}

`CinematicAction`是动画开始时创建的动作。它用于跟踪当前帧并执行片段。
可以使用几种不同的生命周期方法。

- `setup()`在创建过场动画时被调用。这是初始化任何变量、生成实体等的地方。
- 每帧调用`tick(frame: Int)`。这是执行段的地方。它甚至在没有段处于活动状态时执行。
- 动画结束时调用`teardown()`。这是删除任何实体等的地方。
- `canFinish(frame: Int)`是唯一需要实现的方法。`CinematicSequence`使用它来确定动画是否完成。

如果你需要所有定制，你可以直接实现`CinematicAction`：

ExampleCinematicEntry.kt

```kotlin
class ExampleCinematicAction(
    val player: Player,
    val entry: ExampleCinematicEntry,
) : CinematicAction {
    override suspend fun setup() {
        // Initialize variables, spawn entities, etc.
    }

    override suspend fun tick(frame: Int) {
        val segment = entry.segments activeSegmentAt frame
        // Can be null if no segment is active

        // The `frame` parameter is not necessarily next frame: `frame != old(frame)+1`

        // Execute tick logic for the segment
    }

    override suspend fun teardown() {
        // Remove entities, etc.
    }

    override fun canFinish(frame: Int): Boolean = entry.segments canFinishAt frame
}
```

### 简单的过场动画动作 {#simplecinematicaction}

有时你不需要所有的定制和灵活性。如果你只关心 1 段轨道，并且只需要在段开始或结束时执行某些操作，则可以使用`SimpleCinematicAction`。

ExampleCinematicEntry.kt

```kotlin
class ExampleSimpleTemporalAction(
    val player: Player,
    entry: ExampleCinematicEntry,
) : SimpleCinematicAction<ExampleSegment>() {
    override val segments: List<ExampleSegment> = entry.segments

    override suspend fun startSegment(segment: ExampleSegment) {
        super.startSegment(segment) // Keep this
        // Called when a segment starts
    }

    override suspend fun tickSegment(segment: ExampleSegment, frame: Int) {
        super.tickSegment(segment, frame) // Keep this
        // Called every tick while the segment is active
        // Will always be called after startSegment and never after stopSegment

        // The `frame` parameter is not necessarily next frame: `frame != old(frame)+1`
    }

    override suspend fun stopSegment(segment: ExampleSegment) {
        super.stopSegment(segment) // Keep this
        // Called when the segment ends
        // Will also be called if the cinematic is stopped early
    }
}
```

## 逐 tick 执行 {#ticking}

一个重要的细节是`tick`方法不一定按顺序调用。
tick 方法应根据给定帧，呈现动作在该帧应有的状态。

确实存在这种情况的一个地方是当玩家在内容模式下观看过场动画时。
由于玩家能够滚动过场动画，因此可能会跳过或倒带多个帧。

## 模拟与录制 {#simulation--recording}

有时，过场动画在录制或模拟时应该有所不同。
就像致盲过场动画一样，你不想在模拟/录制过程中被致盲。
或者你想在模拟/录制过程中显示不同的东西。
例如，镜头动作在模拟时显示世界中的镜头位置，而不是切换玩家视角。

为此，可以在`CinematicEntry`上实现 2 种附加方法，这些方法可以返回不同的`CinematicAction`进行记录和模拟。

ExampleCinematicEntry.kt

```kotlin
    // This will be used when the cinematic is normally displayed to the player.
    override fun create(player: Player): CinematicAction {
        return DefaultCinematicAction(player, this)
    }

    // This is used during content mode to display the cinematic to the player.
    // It may be null to not show it during simulation.
    override fun createSimulating(player: Player): CinematicAction? {
        return SimulatedCinematicAction(player, this)
    }

    // This is used during content mode to record the cinematic.
    // It may be null to not record it during simulation.
    override fun createRecording(player: Player): CinematicAction? {
        return RecordingCinematicAction(player, this)
    }
```

---

原文：[CinematicEntry](https://docs.typewritermc.com/develop/extensions/entries/cinematic) · 文档版本：0.8.0
