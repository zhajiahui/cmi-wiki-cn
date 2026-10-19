# On Death

## Description {#description}

Executes the skill when the mob dies.  
If the server is a Paper one, it is possible to cancel the death event as long as the cancelevent mechanic is synched. The health that the mob has after this is based on what is specified in the `ReviveHealth` Option.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that killed the caster

## Implementations {#implementations}

- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Triggers/onDeath)
- [MythicRPG](https://wiki.mythiccraft.io/mythicrpg/Skills/Triggers/onDeath)

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a message to all the players in the world
    # when the mob dies
    - message{m=DEATH} @World ~onDeath
```

```yaml
ImmortalCow:
  Type: COW
  Display: '&eImmortal Cow'
  Health: 20
  Options:
    ReviveHealth: -1
  Skills:
  - skill{s=[
    - cancelevent
    - particle{p=HEART;hs=0.5;vs=0.5;y=1.5}
    - speak{m=Call an ambulance, but not for me!}
    ];sync=true} @self ~onDeath
```
