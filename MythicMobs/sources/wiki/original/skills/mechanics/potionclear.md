# Potionclear

## Description {#description}

Clears all potion effects from the target entity

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| types | type, t | The type or list of types of potion effects to clear. Not providing a type will clear all effects. |  |

## Examples {#examples}

```yaml
  Skills:
  - potionclear{type=FIRE_RESISTANCE} @target
  - potionclear{type=FIRE_RESISTANCE,SPEED} @self
  - potionclear @self
```

## Aliases {#aliases}

- clearpotion
- clearpotions
