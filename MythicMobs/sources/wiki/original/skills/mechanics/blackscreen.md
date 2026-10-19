# Blackscreen

## Description {#description}

Causes the player's screen to black out.

## Attributes {#attributes}

> This mechanic inherits every attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Aura) mechanic
>
> > - The `auraname` attribute is **set** at `#blackScreen`
> > - The `maxStacks` attribute is **set** at `1`
> > - The `refreshDuration` attribute is **set** at `true`
> > - The `interval` attribute is **set** at `10`

## Examples {#examples}

Blinds players when the mob teleports

```yaml
BlackScreen:
  Skills:
  - blackscreen{d=2} @PlayersInRadius{r=100} ~onTeleport
```

## Aliases {#aliases}

- effect:blackScreen
- e:blackScreen
