# Holding

## Description {#description}

Checks if the target is holding a given material.  
Uses the [Item Matcher](https://wiki.mythiccraft.io/mythicmobs/Items/Item-Matcher)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | m, type, t, item, i, mat, types | A material or MythicItem to check for |  |
| strict | exact, e | Whether the matcher should more strictly match the target item | false |
| vanillaonly | vanilla | Whether the matched item can only be a vanilla one | false |

## Examples {#examples}

```yaml
# Make sure you use all caps for materials, otherwise the console will say it is not a valid material!
Conditions:
- holding{m=DIAMOND_SWORD} true
```
