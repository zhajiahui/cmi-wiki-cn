# Haspermission

## Description {#description}

This condition checks if the target player has a permission.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| permission | p | The permission to check for. |  |

## Examples {#examples}

```yaml
  Conditions:
  - haspermission{p=permission.node.here} true
```

```yaml
  TargetConditions:
  - haspermission{p=permission.node.here} true
```

```yaml
  TriggerConditions:
  - haspermission{p=permission.node.here} true
```

## Aliases {#aliases}

- permission
