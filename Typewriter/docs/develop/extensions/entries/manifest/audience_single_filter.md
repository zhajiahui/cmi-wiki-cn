---
title: 单一受众过滤器（SingleFilter）
source: https://docs.typewritermc.com/develop/extensions/entries/manifest/audience_single_filter
source_version: 0.8.0
---

# 单一受众过滤器（SingleFilter）

`SingleFilter`是`AudienceFilter`的一种特殊变体，可确保在任何给定时间只有一个过滤器实例可以为玩家激活。这对于管理专用显示（例如玩家列表页眉/页脚或记分板侧边栏）特别有用。

## 基本用法 {#basic-usage}

这是实现单个过滤器的基本示例：

ExampleAudienceSingleFilter.kt

```kotlin
@Entry("example_single_filter", "An example single filter entry", Colors.MYRTLE_GREEN, "material-symbols:filter-alt")
class ExampleSingleFilterEntry(
    override val id: String = "",
    override val name: String = "",
    override val priorityOverride: Optional<Int> = Optional.empty(),
) : AudienceFilterEntry, PriorityEntry {
    override val children: List<Ref<out AudienceEntry>> get() = emptyList()

    override suspend fun display(): AudienceFilter = ExampleSingleFilter(ref()) { player ->
        PlayerExampleDisplay(player, ExampleSingleFilter::class, ref())
    }
}

private class ExampleSingleFilter(
    ref: Ref<ExampleSingleFilterEntry>,
    createDisplay: (Player) -> PlayerExampleDisplay,
) : SingleFilter<ExampleSingleFilterEntry, PlayerExampleDisplay>(ref, createDisplay) {
    // This must be a references to a shared map.
    // It CANNOT cache the map itself.
    override val displays: MutableMap<UUID, PlayerExampleDisplay>
        get() = map

    companion object {
        // This map is shared between all instances of the filter.
        private val map = ConcurrentHashMap<UUID, PlayerExampleDisplay>()
    }
}

private class PlayerExampleDisplay(
    player: Player,
    displayKClass: KClass<out SingleFilter<ExampleSingleFilterEntry, *>>,
    current: Ref<ExampleSingleFilterEntry>
) : PlayerSingleDisplay<ExampleSingleFilterEntry>(player, displayKClass, current) {
    override fun setup() {
        super.setup()
        player.sendMessage("Display activated!")
    }

    override fun tearDown() {
        super.tearDown()
        player.sendMessage("Display deactivated!")
    }
}
```

`SingleFilter`由三个主要组件组成：

1. 条目类：定义配置，并创建过滤器。
2. 管理实例之间共享状态的过滤器类
3. 处理特定于玩家的显示逻辑的显示类

## 显示生命周期 {#display-lifecycle}

显示生命周期是 SingleFilter 中的一个重要概念，因为它管理显示的创建、更新和删除方式。让我们看一个实际的例子：

ExampleAudienceSingleFilter.kt

```kotlin
private class ComplexPlayerDisplay(
    player: Player,
    displayKClass: KClass<out SingleFilter<ExampleSingleFilterEntry, *>>,
    current: Ref<ExampleSingleFilterEntry>
) : PlayerSingleDisplay<ExampleSingleFilterEntry>(player, displayKClass, current) {
    override fun initialize() {
        super.initialize()
        // Called once when the display is first created
        player.sendMessage("Display initialized!")
    }

    override fun setup() {
        super.setup()
        // Called every time this display becomes active
        player.sendMessage("Display setup!")
    }

    override fun tick() {
        // Called every tick while the display is active
        // Update display content here
    }

    override fun tearDown() {
        super.tearDown()
        // Called when this display becomes inactive
        player.sendMessage("Display torn down!")
    }

    override fun dispose() {
        super.dispose()
        // Called when the display is being completely removed
        player.sendMessage("Display disposed!")
    }
}
```

让我们来看看不同场景下会发生什么：

### 场景 1：玩家加入服务器 {#scenario-1-player-joins-server}

```text
1. Player joins
2. initialize() called once - Creates the display instance
3. setup() called - Activates the display with initial entry
4. tick() starts running periodically
```

### 场景 2：更高优先级的条目生效 {#scenario-2-higher-priority-entry-becomes-active}

```text
1. New entry with higher priority includes player in its audience
2. tearDown() called on current display
3. setup() called with new entry
4. Same display instance continues, but with new entry reference
5. tick() continues running with new entry data
```

### 场景 3：玩家离开条目的受众 {#scenario-3-player-leaves-entrys-audience}

```text
1. Player is filtered out of current entry's audience
2. System looks for next highest priority entry where player is in audience
3. If found:
   - tearDown() called with old entry
   - setup() called with new entry
   - Display continues with new entry
4. If not found:
   - tearDown() called
   - dispose() called
   - Display is completely removed
```

显示生命周期在不同条目间切换时，保持单一显示状态并平稳过渡，适合需要避免闪烁或中断的独占显示。

### 优先级行为 {#priority-behavior}

条目的优先级决定了当多个条目的受众中包含一名玩家时哪个显示变为活动状态。例如：

```kotlin
Entry A (priority: 50) - Basic display
Entry B (priority: 100) - Special display

Scenario:
1. Player joins -> Entry B becomes active (higher priority)
2. Player leaves Entry B's audience -> Entry A becomes active (next highest)
3. Player returns to Entry B's audience -> Switches back to Entry B
```

优先级较高的显示可以暂时覆盖较低的显示；玩家不再属于高优先级条目的受众后，会恢复其他符合条件的显示。

---

原文：[SingleFilter](https://docs.typewritermc.com/develop/extensions/entries/manifest/audience_single_filter) · 文档版本：0.8.0
