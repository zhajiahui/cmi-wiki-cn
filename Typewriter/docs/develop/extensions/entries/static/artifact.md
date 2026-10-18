---
title: 文件产物条目（ArtifactEntry）
source: https://docs.typewritermc.com/develop/extensions/entries/static/artifact
source_version: 0.8.0
---

# 文件产物条目（ArtifactEntry）

`ArtifactEntry`是从`AssetEntry`派生的专用接口。
它的主要目的是处理文件产物，即扩展生成的资源。
与标准资源不同，文件产物通常是动态的并在运行时创建。
这使得它们对于存储根据玩家交互或游戏事件而变化的数据特别有用。

`ArtifactEntry`的一个重要特征是其独特的`artifactId`。
该标识符一旦分配就必须保持不变，并用于引用插件内的文件产物。

## 用法 {#usage}

以下是创建和使用`ArtifactEntry`的通用示例：

### 定义 ArtifactEntry {#defining-an-artifactentry}

ExampleArtifactEntry.kt

```kotlin
@Entry("example_artifact", "An example artifact entry.", Colors.BLUE, "material-symbols:home-storage-rounded")
class ExampleArtifactEntry(
    override val id: String = "",
    override val name: String = "",
    override val artifactId: String = "",
) : ArtifactEntry
```

### 读取文件产物内容 {#accessing-the-artifacts-content}

ExampleArtifactEntry.kt

```kotlin
suspend fun accessArtifactData(ref: Ref<out ArtifactEntry>) {
    val assetManager = KoinJavaComponent.get<AssetManager>(AssetManager::class.java)
    val entry = ref.get() ?: return
    val stringContent: String? = assetManager.fetchStringAsset(entry)
    // Do something with the string content
}
```

在此示例中，我们使用`AssetManager`获取给定文件产物引用的内容。
然后，使用`assetManager.fetchAsset`方法基于`entry`检索文件产物的内容。

---

原文：[ArtifactEntry](https://docs.typewritermc.com/develop/extensions/entries/static/artifact) · 文档版本：0.8.0
