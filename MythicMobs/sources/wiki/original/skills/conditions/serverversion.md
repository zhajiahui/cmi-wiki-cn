# Server Version

## Description {#description}

Checks is the server is running a specific minecraft version

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| version | sv, v | The version to check for | 1.19.3 |

## Examples {#examples}

```yaml
  Conditions:
  - serverversion{v="v1.19.4"} true
```

## Aliases {#aliases}

- server
- version
