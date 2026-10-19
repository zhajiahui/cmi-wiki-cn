# Cinematic Cancel

## Description {#description}

Interrupts an active [cinematicCamera](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/CinematicCamera) for the target player, immediately returning their camera and control. The mechanic must target a player.

Cancelling fires the [onCinematicEnd](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onCinematicEnd) trigger (and the original mechanic's `onEnd` skill) with an end reason of `CANCELLED`. If the target player is not currently in a cinematic, the mechanic does nothing.

## Attributes {#attributes}

*This mechanic has no attributes*

## Examples {#examples}

Cancels the cinematic playing for the triggering player.

```yaml
  Skills:
  - cinematicCancel @trigger
```

##  {#section}

Ends the cinematic of every player within 30 blocks when the mob takes damage.

```yaml
  Skills:
  - cinematicCancel @PlayersInRadius{r=30} ~onDamaged
```

## Aliases {#aliases}

- cinecancel
- stopcinematic
