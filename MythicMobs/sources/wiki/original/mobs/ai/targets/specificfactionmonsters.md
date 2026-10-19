# Specificfactionmonsters

## Description {#description}

Causes the mob to target monsters of a specific faction.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| faction | f | The faction to target |  |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AITargetSelectors:
    - clear
    - specificfactionmonsters{f=somefaction}
```

## Aliases {#aliases}

- nearestspecificfactionmonsters
