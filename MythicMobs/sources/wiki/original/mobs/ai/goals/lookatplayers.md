# Lookatplayers

## Description {#description}

Causes the mob to look at nearby players

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| range | radius,r | The range to look for players | 5 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - lookatplayers{r=12}
```

## Aliases {#aliases}

- lookatplayer
