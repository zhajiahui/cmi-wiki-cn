# Damage Amount

## Description {#description}

Checks for a range of damage the entity took, if the skilltree originated from a [onDamaged Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDamaged) or an [onDamaged Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ondamaged).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| damageAmount | amount, a | Range of damage to check for | >0 |

## Examples {#examples}

```yaml
  Conditions:
  - damageamount{amount=>10} true
```
