# Spin

## Description {#description}

Causes the target entity to spin around for the given duration.  
When a mob casts the spin mechanic repeatedly it will move upwards while spinning.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| velocity | v | The velocity the target spins at | 18 |

> This mechanic inherits every attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Aura) mechanic

### Velocity Attribute {#velocity-attribute}

When you set velocity to 0, this mob's direction will be locked.

## Examples {#examples}

```yaml
SpinningSpider:
  Type: SPIDER
  Skills:
  - spin{duration=100;velocity=20} @self ~onTimer:100
```

## Aliases {#aliases}

- effect:spin
- e:spin
