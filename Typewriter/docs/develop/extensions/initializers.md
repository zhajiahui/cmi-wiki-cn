---
title: 初始化器（Initializers）
source: https://docs.typewritermc.com/develop/extensions/initializers
source_version: 0.8.0
---

# 初始化器（Initializers）

有时你的扩展需要在使用之前进行一些初始化。
例如，你可能需要向插件添加一个钩子以使其与你的扩展一起使用。

## 声明初始化器 {#declaring-an-initializer}

声明初始化器时，需要创建一个实现 `Initializable` 接口的 **object 对象**。
并将`@Initializer`注解添加到类中。

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

**确保清理**

卸载扩展时调用`shutdown`方法。
你应该确保卸载扩展时不会泄漏资源。

Typewriter在扩展加载和卸载时会自动注册并调用控制流方法。

---

原文：[Initializers](https://docs.typewritermc.com/develop/extensions/initializers) · 文档版本：0.8.0
