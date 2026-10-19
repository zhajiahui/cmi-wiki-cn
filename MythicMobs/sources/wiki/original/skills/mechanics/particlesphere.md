# Particle Sphere

## Description {#description}

Creates a sphere of particles at the targeted entity or location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the sphere to draw | 0 |

> This mechanic inherits every attribute of the [Particle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/particle) mechanic

## Examples {#examples}

```yaml
FlameSphere:
  Skills:
  - particlesphere{particle=flame;amount=200;radius=5} @self
```

## Aliases {#aliases}

- effect:particlesphere
- e:ps
- ps
