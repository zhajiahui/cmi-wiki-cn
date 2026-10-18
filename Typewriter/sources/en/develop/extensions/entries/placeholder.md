# Placeholder

Entries can expose a placeholder.
The placeholders can be used by users or other plugins with the PlaceholderAPI.

**danger**

Placeholder is an additional interface for an existing entry. It cannot be used on its own.

## Basic Usage {#basic-usage}

To just expose a single placeholder, extend your entry with `PlaceholderEntry`:

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

This placeholder can be used with `%typewriter_<entry id>%` and will return `Hello <player name>!`

## Sub Placeholders {#sub-placeholders}

Besides just having a primary placeholder, entries can also have sub placeholders.
These can be literal strings which needs to be matched:

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

Where the placeholder can be used in the following ways:

| Placeholder | Result |
| --- | --- |
| `%typewriter_<entry id>%` | `Standard text` |
| `%typewriter_<entry id>:greet%` | `Hello, <player name>!` |
| `%typewriter_<entry id>:greet:enthusiastic%` | `HEY HOW IS YOUR DAY, <player name>!` |

But is can also have variables:

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

Where the placeholder can be used in the following ways:

| Placeholder | Result |
| --- | --- |
| `%typewriter_<entry id>%` | `%typewriter_<entry id>%` |
| `%typewriter_<entry id>:bob%` | `Hello, bob!` |
| `%typewriter_<entry id>:alice%` | `Hello, alice!` |

Notice how the default placeholder no longer works, because we don't have a supplier for it anymore.
