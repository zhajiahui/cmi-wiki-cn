# Weather

## Description {#description}

Changes the weather in the casting mob's world.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| type | t | The type of weather. Can be "sunny", "rainy", or "stormy" | sunny |
| duration | d | How long (in ticks) the weather will be forced to last | 500 |

#### Weather Types {#weather-types}

| Type | Aliases |
| --- | --- |
| **Sunny** | sun, clear |
| **Rainy** | rain |
| **Stormy** | storm, thunder |

## Examples: {#examples}

Causes a storm for 10 minutes when the mob spawns.

```yaml
Skills:
  - weather{type=storm;duration=6000} ~onSpawn
```
