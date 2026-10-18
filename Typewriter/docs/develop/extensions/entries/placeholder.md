---
title: 占位符（Placeholder）
source: https://docs.typewritermc.com/develop/extensions/entries/placeholder
source_version: 0.8.0
---

# 占位符（Placeholder）

条目可以公开占位符。
用户或其他带有PlaceholderAPI的插件可以使用占位符。

**危险**

占位符是现有条目的附加接口。它不能单独使用。

## 基本用法 {#basic-usage}

要仅公开单个占位符，请使用`PlaceholderEntry`扩展你的条目：

ExamplePlaceholderEntry.kt

```kotlin
class SimpleExamplePlaceholderEntry(
    override val id: String,
    override val name: String,
) : PlaceholderEntry {
    override fun parser(): PlaceholderParser = placeholderParser {
        supply { player ->
            "Hello, ${player?.name ?: "World"}!"
        }
    }
}
```

该占位符可与`%typewriter_<entry id>%`一起使用，并将返回`Hello <player name>!`

## 子占位符 {#sub-placeholders}

除了仅具有主占位符之外，条目还可以具有子占位符。
这些可以是需要匹配的文字字符串：

ExamplePlaceholderEntry.kt

```kotlin
    override fun parser(): PlaceholderParser = placeholderParser {
        literal("greet") {
            literal("enthusiastic") {
                supply { player ->
                    "HEY HOW IS YOUR DAY, ${player?.name ?: "World"}!"
                }
            }
            supply { player ->
                "Hello, ${player?.name ?: "World"}"
            }
        }
        supply {
            "Standard text"
        }
    }
```

其中占位符可以通过以下方式使用：

|占位符 |结果 |
| --- | --- |
|`%typewriter_<entry id>%`|`Standard text`|
|`%typewriter_<entry id>:greet%`|`Hello, <player name>!`|
|`%typewriter_<entry id>:greet:enthusiastic%`|`HEY HOW IS YOUR DAY, <player name>!`|

但也可以有变量：

ExamplePlaceholderEntry.kt

```kotlin
    override fun parser(): PlaceholderParser = placeholderParser {
        string("name") { name ->
            supply {
                "Hello, ${name()}!"
            }
        }
    }
```

其中占位符可以通过以下方式使用：

|占位符 |结果 |
| --- | --- |
|`%typewriter_<entry id>%`|`%typewriter_<entry id>%`|
|`%typewriter_<entry id>:bob%`|`Hello, bob!`|
|`%typewriter_<entry id>:alice%`|`Hello, alice!`|

注意，默认占位符已不再生效，因为没有为它提供对应的提供器。

---

原文：[Placeholder](https://docs.typewritermc.com/develop/extensions/entries/placeholder) · 文档版本：0.8.0
