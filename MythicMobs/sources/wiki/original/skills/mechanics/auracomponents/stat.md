# Stat

## Description {#description}

Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) component to the target that applies a specific [stat](https://wiki.mythiccraft.io/mythicmobs/Stats) to them.  
The buff received is multiplied by the amount of stacks the aura has

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| stat | s | The [stat](https://wiki.mythiccraft.io/mythicmobs/Stats) to apply |  |
| type | t, modifier, mod, m | The [stat modifier](https://wiki.mythiccraft.io/mythicmobs/Stats#modifiers) to use | ADDITIVE |
| value | val, v | The value to use for the stat | 0.0 |

## Examples {#examples}

The following aura will double the critical strike chance of the caster for 5 seconds

```yaml
  Skills:
  - aura{auraName=exampleaura;d=100;components=[
    - stat{stat=CRITICAL_STRIKE_CHANCE;type=COMPOUND_MULTIPLIER;val=2}
    ]} @self
```

## Aliases {#aliases}

- stataura
- stats
