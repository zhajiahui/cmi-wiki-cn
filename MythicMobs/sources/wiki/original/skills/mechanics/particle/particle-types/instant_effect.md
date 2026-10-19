# Instant Effect

## Particle {#particle}

![img](https://wiki.mythiccraft.io/_media/mythicmobs/Skills/Mechanics/Particle/Particle-Types/images/INSTANT_EFFECT.gif)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| color | c | The color of the particle | #FF0000 |
| power | p | The power of the spell particle | 1 |

> This particle has a [Spell](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types#spell) Datatype, and inherits all of its attributes

## Examples {#examples}

```yaml
  Skills:
  - particle{p=instant_effect;color=#FF0000;power=1}
```

## Aliases {#aliases}

- spell_instant
- instant_spell

> This particle has a different name in versions before 1.20.5
>
> - spell_instant
