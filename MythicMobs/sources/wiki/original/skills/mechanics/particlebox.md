# Particle Box

## Description {#description}

Creates a box of particles at the targeted entity or location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the box to draw | 5 |

> This mechanic inherits every attribute of the [Particle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/particle) mechanic

## Examples {#examples}

```yaml
ParticleCube:
  Skills:
  - particlebox{particle=flame;amount=200;radius=5} @self
```

## Aliases {#aliases}

- effect:particlebox
- e:pb
- pb
