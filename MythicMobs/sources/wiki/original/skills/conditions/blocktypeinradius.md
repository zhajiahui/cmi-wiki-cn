# Block Type In Radius

## Description {#description}

Checks against the amount of specified blocks in a radius around the evaluated location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, b, block | A list of [materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) to check against | DIRT |
| radius | r | The radius | 8 |
| amount | a | The amount of blocks to match | >0 |

## Examples {#examples}

```yaml
  TargetConditions:
  - blockTypeInRadius{type=STONE;amount=>10;radius=3} true
```
