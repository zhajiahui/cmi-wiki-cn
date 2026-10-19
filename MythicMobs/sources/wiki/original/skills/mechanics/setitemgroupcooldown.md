# Set Item Group Cooldown

## Description {#description}

Sets the cooldown on an item group for the target player

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| key | k, group, g | The group to set the cooldown to | minecraft:item_group |
| ticks | t | The amount of ticks the cooldown will last | 20 |

## Examples {#examples}

```yaml
  Skills:
  - SetItemGroupCooldown{key=yournamespace.teleportingitems;ticks=200}
```
