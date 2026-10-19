# Hologram

## Description {#description}

Spawns a hologram at a target location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| text | t | The text to show | Hologram Text Missing |
| stay | time, staytime | The duration of the hologram in ticks | 100 |

## Examples {#examples}

Creates a hologram above the mob when the mob gets right clicked, which displays for 100 ticks.

```yaml
  Skills:
  - holo{text="Example Text";time=100} @selflocation{y=1.6} ~onInteract
```

## Aliases {#aliases}

- summonhologram
- holo
