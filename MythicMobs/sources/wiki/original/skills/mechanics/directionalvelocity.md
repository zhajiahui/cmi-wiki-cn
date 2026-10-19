# Directional Velocity

## Description {#description}

Changes the velocity on the target entity on a specific vector

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| yaw |  | The yaw of the vector for the velocity change |  |
| pitch |  | The pitch of the vector for the velocity change |  |
| velocity | v | The magnitude of the velocity change |  |
| mode | m | The mode to use | SET |

### Mode Attribute {#mode-attribute}

Accepted values are

- `SET`
- `ADD`
- `MULTIPLY`
- `REMOVE`
- `DIVIDE`
- `MINIMUM`

## Examples {#examples}

```yaml
  Skills:
  - directionalvelocity{yaw=180;v=1;mode=MINIMUM} @self
```

## Aliases {#aliases}

- dvelocity
