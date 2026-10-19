# Hasaura

## Description {#description}

Checks if the target entity has the given aura

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| aura | auraname, b, buff, buffname, debuff, debuffname, n, name | The name of the aura to check for |  |

## Examples {#examples}

```yaml
  Conditions:
  - hasaura{aura=firedebuff} true
```

## Aliases {#aliases}

- hasbuff
- hasdebuff
