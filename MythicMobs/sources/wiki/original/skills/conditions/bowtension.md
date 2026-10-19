# Bowtension

## Description {#description}

Checks the bow tension of when an entity shoots from a bow

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| force | f, value, v, val | The value of the force/tension to check for. Accepts ranged float values, but only in a range from 0 to 1 | >0 |

## Examples {#examples}

```yaml
  Conditions:
  - bowtension{value=>0.5} true
```

## Aliases {#aliases}

- bowshoottension
