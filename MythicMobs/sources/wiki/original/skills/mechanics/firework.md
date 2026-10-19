# Firework

## Description {#description}

Creates a firework effect at the target.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| type | t | The Type of firework. See below for a list. | BALL |
| power | p, duration, d | The flight duration of the firework. | 2 |
| flicker | f | Whether to add the flicker effect to the explosion. | false |
| trail | tr | Whether to add the trail effect to the firework rocket. | false |
| colors | color, c | The color of the firework explosion, in RGB or hex | #FFFFFF |
| fadecolors | fcolors, fc | The fade colors of the firework explosion, in RBG or hex | #FFFFFF |

### Type Attribute {#type-attribute}

The type attribute's value can be one of the following

- `BALL`
- `BALL_LARGE`
- `BURST`
- `CREEPER`
- `STAR`

## Examples {#examples}

```yaml
  Skills:
  - effect:firework{t=BALL;d=1;f=true;tr=true} @self ~onInteract
```

## Aliases {#aliases}

- fireworks
- effect:firework
- effect:fireworks
- e:firework
