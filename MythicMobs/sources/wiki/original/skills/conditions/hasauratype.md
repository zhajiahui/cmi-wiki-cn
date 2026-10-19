# Has Aura Type

## Description {#description}

Checks if the target entity has the given aura type

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| auragroup | auratype, group, type, t, g | The aura type to check for |  |

## Examples {#examples}

This example would apply an aura of a `Example` Type. The second example will then check for its presence

```yaml
  Skills:
  - aura{auraName=NotMeThisTime;auratype=Example;d=100} @self
```

```yaml
  Conditions:
  - hasAuraType{type=Example} true
```

## Aliases {#aliases}

- hasbufftype
- hasdebufftype
