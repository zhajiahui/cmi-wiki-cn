# Give Experience Levels

## Description {#description}

Gives experience levels to the targeted players

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of levels to give | 0 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - giveexperiencelevels{a=1} @trigger ~onDamaged
```

## Aliases {#aliases}

- giveexplevels
