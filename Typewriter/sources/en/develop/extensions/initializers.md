# Initializers

Sometimes your extension needs to do some initialization before it can be used.
For example, you might need to add a hook to a plugin to make it work with your extension.

## Declaring an Initializer {#declaring-an-initializer}

To declare an initializer, you need to create a **object** that implements the `Initializable` interface.
And add the `@Initializer` annotation to the class.

ExampleInitializer.kt

```kotlin
import com.typewritermc.core.extension.Initializable
import com.typewritermc.core.extension.annotations.Singleton

@Singleton
object ExampleInitializer : Initializable {
    override suspend fun initialize() {
        // Do something when the extension is initialized
    }

    override suspend fun shutdown() {
        // Do something when the extension is shutdown
    }
}
```

**Ensure Cleanup**

The `shutdown` method is called when the extension is unloaded.
You should make sure that no resources are leaked when the extension is unloaded.

Typewriter will automatically register and call the control flow methods when the extension is loaded and unloaded.
