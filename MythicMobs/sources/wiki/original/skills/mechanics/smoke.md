# Smoke

## Description {#description}

Creates a puff of smoke at the location of the targeter.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| direction | dir, d | The direction the effect should play towards. Can be an integer from 1 to 4 | 4 |

## Examples {#examples}

```yaml
SmokeMonster:
  Type: ZOMBIE
  Skills:
  - smoke @target ~onTimer:10
  - smoke{direction=2} @self ~onAttack
```

## Aliases {#aliases}

- effect:smoke
- e:smoke
