# Modify Damage

## Description {#description}

Modifies the damage event that triggered the skill.  
This mechanic must be synced, meaning that either the mechanic or the initial skill calling it must be run with the `sync=true` attribute.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of the operation | 1 |
| damagetype | type, dt, t | The type of the damage to evaluate | ALL |
| action | mod, m | The [modifier](https://wiki.mythiccraft.io/mythicmobs/Stats#modifiers) to use | ADD |

## Examples {#examples}

```yaml
  Skills:
  - modifyDamage{a=2;action=ADDITIVE_MULTIPLIER;sync=true} @self ~onAttack 0.2
```

## Aliases {#aliases}

- modDamage
