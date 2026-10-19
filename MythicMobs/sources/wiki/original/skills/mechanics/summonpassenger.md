# Summonpassenger

## Description {#description}

Summons a mob to mount the caster. Will knock the current rider off if there is one.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| passenger | p, rider, r, type, t | The type of the mob to set as the passenger |  |
| stack | s | Sets whether to mount the summoned entity to the current passenger of the caster | false |

## Examples {#examples}

```yaml
  Skills:
  - summonPassenger{type=MyZombie}
```

Will summon the mob "MyZombie" to ride the caster of the mechanic.

## Aliases {#aliases}

- passenger
- summonRider
- rider
