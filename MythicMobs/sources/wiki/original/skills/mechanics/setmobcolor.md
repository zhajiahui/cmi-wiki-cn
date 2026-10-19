# Setmobcolor

## Description {#description}

Changes the target color, can only be applied to colorable mobs such as
shulkers or sheeps.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| color | c | The color name |  |

## Examples {#examples}

Sets the color of colorable mobs to blue when it spawns.

```yaml
  Skills:
  - setcolor{color=blue} @self ~onSpawn
  - ...
```

## Aliases {#aliases}

- setcolor
