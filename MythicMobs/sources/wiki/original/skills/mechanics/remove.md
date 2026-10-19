# Remove

## Description {#description}

Removes the targeted entity from existence. Does not work on players.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| onRemoveSkill | onRemove, then | The Metaskill to execute once an entity is removed |  |

## Examples {#examples}

This mob would despawn 10 seconds after spawning:

```yaml
  Skills:
  - remove{delay=200} @self ~onSpawn
```

This skill despawns the mob immediately when it is right clicked.

```yaml
  Skills:
  - remove @self ~onInteract
```

## Aliases {#aliases}

- delete
