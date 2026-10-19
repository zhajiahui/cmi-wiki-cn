# Summon Falling Block

## Description {#description}

Summons a falling block of the specified material at the targeted locations

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| type | types, t, material, mat, m | The [material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) of the falling block | DIRT |

## Examples {#examples}

```yaml
  Skills:
  - summonfallingblock{m=ANVIL} @PlayerLocationsInRadius{r=20;y=10}
```
