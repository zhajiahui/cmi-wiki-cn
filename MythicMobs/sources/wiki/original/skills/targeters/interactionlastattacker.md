# Interaction Last Attacker

## Description {#description}

Targets the last entity that attacked the caster, if the caster is of the `INTERACTION` [Type](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#type).

## Attributes {#attributes}

> *This condition has no attributes*

## Examples {#examples}

The following example would ignite the last entity that attacked the caster once every 100 ticks

```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - ignite @interactionLastAttacker ~onTimer:100
```

## Aliases {#aliases}

- lastAttacker
