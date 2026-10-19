# Spring

## Description {#description}

Creates a temporary "spring" of liquid at the target entity or location.

> Liquid spread from the spring can and will destroy any blocks that are
> normally destroyed by liquids. Use wisely

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| type | t | The type of spring. Can be `water` or `lava` | water |
| duration | d | The duration (in ticks) the spring will last | 40 |

## Examples {#examples}

Creates a spring of water under the target for 5 seconds.

```yaml
Flood:
  Skills:
  - spring{d=100} @target
```

## Aliases {#aliases}

- water
