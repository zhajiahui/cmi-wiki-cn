# Percentdamage

## Description {#description}

Deals damage equal to a percent of the player's max health, where 1 is
100%. Inherits every attribute of the [Damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage) mechanic.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| percent | p | The percentage to damage the target | 0.1 |
| currentHealth | current, c, ch | Whether it calculates the percent from your original or current health | false |

> This mechanic inherits every attribute of the [damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage) mechanic
>
> > The `amount` attribute is ignored

## Examples {#examples}

Hurts the target for half (50%) of its max health.

```yaml
  Skills:
  - damagepercent{percent=0.5}
```

## Aliases {#aliases}

- damagepercent
- percentdamage
