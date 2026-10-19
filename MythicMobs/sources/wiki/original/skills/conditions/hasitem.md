# Has Item

## Description {#description}

Tests if the target player or an item container has exactly the given number of the given material.  
Uses the [Item Matcher](https://wiki.mythiccraft.io/mythicmobs/Items/Item-Matcher)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| item | i, material, m, type, t, mat, types | The item to check for | DIRT |
| amount | a | The amount to check for | >0 |
| strict | exact, e | Whether the matcher should more strictly match the target item | false |
| vanillaonly | vanilla | Whether the matched item can only be a vanilla one | false |

## Examples {#examples}

```yaml
  Conditions:
  - hasitem{i=stick;amount=>1} true
```

```yaml
  Conditions:
  - hasitem{i=my_custom_item;amount=<10} true
```

```yaml
  Conditions:
  - hasitem{i=mmoitems.SWORD.CUTLASS;amount=1to10} true
```
