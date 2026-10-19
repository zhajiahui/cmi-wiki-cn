# Mount

## Description {#description}

Causes the casting mob to summon a specified MythicMob and mount it. The caster will be set as both the [owner](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner) and the [parent](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Parent) of the summoned mob.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| type | t, mob, m | The type of MythicMob to summon |  |
| stack | s | If the summoned mob should stack atop existing mounted entities | false |

### Type Attribute {#type-attribute}

The MythicMob defines in type must be a valid MythicMob type (and is
case-sensitive). If an invalid type is specified the skill may throw an
error.

## Examples {#examples}

This example would summon a Mythic Mob of the type "UndeadMount" and
make the caster mount it.

```yaml
CallSkeletalHorse:
  Skills:
  - mount{type=UndeadMount}
```

## Aliases {#aliases}

- vehicle
