# Barremove

## Description {#description}

Removes a custom boss bar on the casting mob (cannot be player).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| name | n | The name of the bossbar to remove | infobar |

## Examples {#examples}

```yaml
  Skills:
  - barRemove{name="MyBossBar"} @self ~onInteract
```
