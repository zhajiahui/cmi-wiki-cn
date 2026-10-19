# Distancefromspawn

## Description {#description}

Whether the distance from the world's spawn point to the target is within the given range

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| distance | d | The distance to match |  |

## Examples {#examples}

```yaml
  Conditions:
  - distancefromspawn{d=<100} true
```

```yaml
  Conditions:
  - distancefromspawn{d=>50} true
```
