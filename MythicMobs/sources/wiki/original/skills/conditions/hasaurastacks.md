# Hasaurastacks

## Description {#description}

Tests if the target has the given range of stacks from an aura

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| aura | auraname, b, buff, buffname, debuff, debuffname, n, name | The name of the aura to check for |  |
| stacks | s | The number/range of stacks to check for | 1 |

## Examples {#examples}

```yaml
  Conditions:
  - hasaurastacks{n=firedebuff;s=>3} true
```

## Aliases {#aliases}

- hasbuffstacks
- hasdebuffstacks
- aurastacks
- buffstacks
- debuffstacks
