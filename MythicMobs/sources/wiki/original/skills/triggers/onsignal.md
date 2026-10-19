# Onsignal

## Description {#description}

This Trigger has a special syntax: `~onSignal:<signal>`

Executes the skill when the mob receives a signal from the [signal](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Signal) mechanic.  
A signal must be alphanumeric.

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the entity that sent the signal

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: CHICKEN
  Skills:
    # sends a signal to all mythicmob entity in a radius of 64 blocks
    # when a player right-clicks the mob
    - signal{s=MOO_FOR_ME} @EIR{r=64} ~onInteract
```

##  {#section}

```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # sends a message to all the players in the world
    # when the mob receives a "MOO_FOR_ME" signal
    - message{m=MOO} @World ~onSignal:MOO_FOR_ME
```

##  {#section-2}

You may also choose to not specify a signal for this trigger, in which case the associated mechanic will be triggered every time the mob receives a generic signal.

```yml
DUMMY_MOB:
  Type: COW
  Skills:
    # sends a message to all the players in the world
    # when the mob receives a signal
    - message{m=MOO...?} @World ~onSignal
```
