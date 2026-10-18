---
title: 受众过滤器（AudienceFilter）
source: https://docs.typewritermc.com/develop/extensions/entries/manifest/audience_filter
source_version: 0.8.0
---

# 受众过滤器（AudienceFilter）

`AudienceFilterEntry`是`AudienceEntry`的专门版本，旨在根据特定条件过滤受众成员。
它接受可以包含`AudienceEntry`和`AudienceFilterEntry`组件的子级列表。

## 基本用法 {#basic-usage}

### 静态筛选 {#static-filtering}

以下是仅允许姓名以“g”开头的玩家的过滤器示例：

ExampleAudienceFilter.kt

```kotlin
class ExampleAudienceFilter(
    ref: Ref<out AudienceFilterEntry>
) : AudienceFilter(ref) {
    override fun filter(player: Player): Boolean {
        return player.name.startsWith("g")
    }
}
```

该过滤器是静态的，因为玩家名称在服务器上无法更改。
玩家是否通过这个静态过滤器，在一开始就决定。

### 动态筛选 {#dynamic-filtering}

对于更动态的过滤，你可以根据不断变化的玩家属性（例如生命值）进行过滤：

ExampleAudienceFilter.kt

```kotlin
class HealthAudienceFilter(
    ref: Ref<out AudienceFilterEntry>,
    private val healthRange: ClosedFloatingPointRange<Float> = 0f..20f
) : AudienceFilter(ref), TickableDisplay {
    override fun filter(player: Player): Boolean {
        return player.health in healthRange
    }

    // You can refresh the filters on events
    @EventHandler
    fun healthRegent(event: EntityRegainHealthEvent) {
        val player = event.entity as? Player ?: return
        // Reruns the filter
        player.refresh()

        // Or if you know the player should be filtered, you can update the filter directly
        player.updateFilter(isFiltered = event.amount in healthRange)
    }

    // It is also possible to run the filter every tick
    override fun tick() {
        // Refresh the filter for all considered players
        consideredPlayers.forEach { it.refresh() }
    }
}
```

这个示例根据玩家的生命值筛选玩家，生命值条件通过条目参数提供。
与`AudienceDisplay`一样，我们可以使用Bukkit事件和`TickableDisplay`来更新哪些玩家通过过滤器。

### 可反转的过滤器 {#invertible-filters}

有时你可能想要反转过滤器的行为。
当相反的条件难以明确定义时，这特别有用，例如过滤不在特定世界中的所有玩家：

ExampleAudienceFilter.kt

```kotlin
@Entry("inverted_example_audience_filter", "An example audience filter.", Colors.MYRTLE_GREEN, "material-symbols:filter-alt")
class InvertedExampleAudienceFilterEntry(
    override val id: String = "",
    override val name: String = "",
    override val children: List<Ref<out AudienceEntry>> = emptyList(),
    override val inverted: Boolean = true,
) : AudienceFilterEntry, Invertible {
    override suspend fun display(): AudienceFilter = ExampleAudienceFilter(ref())
}
```

只需实现`Invertible`接口即可在Typewriter中实现此功能。

---

原文：[AudienceFilter](https://docs.typewritermc.com/develop/extensions/entries/manifest/audience_filter) · 文档版本：0.8.0
