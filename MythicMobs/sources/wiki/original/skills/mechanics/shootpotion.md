# Shootpotion

## Description {#description}

Throws a potion at the targeted entity or location, causing the splash
potion effect of the given type to all entities hit.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| velocity | v | The velocity of the thrown potion | 1 |

> This mechanic inherits every *inheritable* attribute of the [Potion](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Potion) mechanic

## Examples {#examples}

Throws a potion at the target that slows them down.

```yaml
ThrownCripplingPotion:
  Skills:
  - shootpotion{type=SLOW;duration=200;level=4;velocity=5} @target
```
