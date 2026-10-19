# Particle Ring

## Description {#description}

Creates a ring of particles around the targeted entity or location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| points | pts | The number of points to draw representing the ring | 8 |
| radius | r | The radius of the ring around the target | 10 |

> This mechanic inherits every attribute of the [Particle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/particle) mechanic
>
> > The particles are generated “per point” in this mechanic, so keeping `amount` low is recommended.

## Examples {#examples}

```yaml
FlameRing:
  Skills:
  - particlering{particle=flame;radius=20;points=32;amount=1;hS=1;vS=0} @target
```

## Aliases {#aliases}

- effect:particlering
- e:pr
- pr
