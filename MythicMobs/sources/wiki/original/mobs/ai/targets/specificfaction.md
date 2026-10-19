# Specificfaction

## Description {#description}

Causes the mob to target a specific faction.

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
    - specificfaction{f=somefaction}
```

## Aliases {#aliases}

- nearestspecificfaction
