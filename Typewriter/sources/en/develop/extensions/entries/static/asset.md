# AssetEntry

The AssetEntry is a specialized interface that extends the `StaticEntry`.
It is primarily used for handling static assets within the game.
Assets can include various types of files such as images, sounds, or other external resources that are crucial to enhancing the game environment and player experience.
The key attribute of AssetEntry is the path, which specifies the location of the asset.

## Usage {#usage}

Here's a generic example of creating and using an `AssetEntry`:

### Defining an AssetEntry {#defining-an-assetentry}

ExampleAssetEntry.kt

```kotlin
@Entry("example_asset", "An example asset entry.", Colors.BLUE, "material-symbols:home-storage-rounded")
class ExampleAssetEntry(
    override val id: String = "",
    override val name: String = "",
    override val path: String = "",
) : AssetEntry
```

### Accessing the Artifact's Content {#accessing-the-artifacts-content}

To get the asset from the entry, you can use the following code:

ExampleAssetEntry.kt

```kotlin
suspend fun accessAssetData(ref: Ref<out AssetEntry>) {
    val assetManager = KoinJavaComponent.get<AssetManager>(AssetManager::class.java)
    val entry = ref.get() ?: return
    val stringContent: String? = assetManager.fetchStringAsset(entry)
    // Do something with the string content
}
```
