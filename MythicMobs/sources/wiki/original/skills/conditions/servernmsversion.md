# Servernmsversion

## Description {#description}

Checks is the server is running a specific minecraft NMS version

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| version | sv, v | The version to check for | v1_19_R1_2 |

## Examples {#examples}

```yaml
  Conditions:
  - nmsversion{v="v1_19_R1"}
```

## Aliases {#aliases}

- servernms
- nmsversion
