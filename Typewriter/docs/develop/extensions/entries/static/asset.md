---
title: 资源条目（AssetEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/static/asset
source_version: 0.8.0
---

# 资源条目（AssetEntry）

AssetEntry 是扩展`StaticEntry`的专用接口。
它主要用于处理游戏中的静态资源。
资源可以包括各种类型的文件，例如图像、声音或其他对于增强游戏环境和玩家体验至关重要的外部资源。
AssetEntry的关键属性是路径，它指定了资源的位置。

## 用法 {#usage}

以下是创建和使用`AssetEntry`的通用示例：

### 定义 AssetEntry {#defining-an-assetentry}

ExampleAssetEntry.kt

```kotlin
@Entry("example_asset", "An example asset entry.", Colors.BLUE, "material-symbols:home-storage-rounded")
class ExampleAssetEntry(
    override val id: String = "",
    override val name: String = "",
    override val path: String = "",
) : AssetEntry
```

### 读取文件产物内容 {#accessing-the-artifacts-content}

要从条目中获取资源，可以使用以下代码：

ExampleAssetEntry.kt

```kotlin
suspend fun accessAssetData(ref: Ref<out AssetEntry>) {
    val assetManager = KoinJavaComponent.get<AssetManager>(AssetManager::class.java)
    val entry = ref.get() ?: return
    val stringContent: String? = assetManager.fetchStringAsset(entry)
    // Do something with the string content
}
```

---

原文：[AssetEntry](https://docs.typewritermc.com/develop/extensions/entries/static/asset) · 文档版本：0.8.0
