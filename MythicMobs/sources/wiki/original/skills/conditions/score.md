# Score

## Description {#description}

Checks a scoreboard value of the target entity.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| objective | obj, o | The objective |  |
| entry | ent, e | The entry |  |
| value | val, v | The value to match |  |

## Examples {#examples}

```yaml
  Conditions:
  - score{o=PlayerKills;e=Akim91;v=10} true
```
