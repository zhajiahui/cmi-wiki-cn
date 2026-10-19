# Atom

## Description {#description}

Creates an orbiting Atom effect at the location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| particleorbital | particleo, po | The [particle](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types) that will be displayed at the orbitals | `particle` |
| particlenucleus | particlen, pn | The [particle](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types) that will be displayed at the nucleus | reddust |
| amountnucleus | amountn, apn, an | The amount of particles for the nucleus | 50 |
| orbitals | o | The amount of orbitals around the nucleus | 2 |
| amountorbital | amounto, apo, ao | The amount of particles for each orbital | 1 |
| radius | r | The radius of the orbitals | 4 |
| radiusnucleus | rn | The radius of the nucleus | 1 |
| rotation | ro | The rotation of the atom | 0 |
| ticks | t | The amount of ticks during which the atom will persist | 1 |
| interval | in | The interval of the updates of the atom | 10 |
| velocity | v | The velocity of the atom | 80 |

> This mechanic inherits every attribute of the [particle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle) mechanic

## Examples {#examples}

```yaml
  Skills:
  - Atom{p=reddust;r=2;d=true;dr=true;dir=1,0,0;ticks=20} @selflocation{y=2} ~onSwing
```

## Aliases {#aliases}

- effect:atom
- e:atom
