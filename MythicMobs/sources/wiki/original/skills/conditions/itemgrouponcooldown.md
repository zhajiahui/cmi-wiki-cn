# Item Group On Cooldown

## Description {#description}

Checks whether the target player has the specified item group on cooldown.  
Do also check out the related [SetItemGroupCooldown mechanic](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetItemGroupCooldown)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| group | g | the group to check against |  |

## Examples {#examples}

```yaml
  Conditions:
  - ItemGroupOnCooldown{g=teleportingitems}
```
