# Wearing

## Description {#description}

This condition checks if the target entity is wearing the selected item.  
Uses the [Item Matcher](https://wiki.mythiccraft.io/mythicmobs/Items/Item-Matcher)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| armorslot | slot, s | The [item slot](https://wiki.mythiccraft.io/mythicmobs/Skills/EquipSlot) to check. | HEAD |
| material | mat, m, item, i, t, type, types | A material or MythicItem name to check for. Also supports MMOItems in the format mmoitems.TYPE.ID | DIRT |
| strict | exact, e | Whether the matcher should more strictly match the target item | false |
| vanillaonly | vanilla | Whether the matched item can only be a vanilla one | false |

## Examples {#examples}

```yaml
Conditions:
  - wearing{slot=HAND;m=IRON_SWORD} true
  - wearing{slot=CHEST;m=mmoitems.TYPE.ID} true
```

## Aliases {#aliases}

- iswearing
- wielding
- iswielding
