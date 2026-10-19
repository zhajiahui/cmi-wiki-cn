# Take Experience Levels

## Description {#description}

Takes experience levels from the targeted players

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of levels to take | 0 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - takeexperiencelevels{a=1} @trigger ~onDamaged
```

## Aliases {#aliases}

- takeexplevels
