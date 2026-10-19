# Geyser

## Description {#description}

Causes a geyser of liquid to shoot out of the ground at the targeted entity or location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| type | t | The type of liquid. Can be “WATER” or “LAVA” | WATER |
| height | h | How high the geyser will go. Will be set to *at least* 1 even if specified otherwise. | 3 |
| interval | i, speed, s | The interval (in ticks) between each iteration of the geyser animation | 10 |
| audience |  | The [audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) of the effect | nearby |

## Examples {#examples}

```yaml
GeyserSkill:
  Skills:
  - geyser{type=LAVA;height=3;speed=10} @selflocation
```

## Aliases {#aliases}

- effect:geyser
- e:geyser
