# Item Type

## Description {#description}

Checks against the material of the item that triggered the skill.  
Uses the [Item Matcher](https://wiki.mythiccraft.io/mythicmobs/Items/Item-Matcher)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, i, item | A list of [materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) to check against | DIRT |
| strict | exact, e | Whether the matcher should more strictly match the target item | false |
| vanillaonly | vanilla | Whether the matched item can only be a vanilla one | false |

## Examples {#examples}

```yaml
  Conditions:
  - itemType{types=STONE,STONE_SWORD} true
```
