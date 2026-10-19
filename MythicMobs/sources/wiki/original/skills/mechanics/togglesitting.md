# Togglesitting

## Description {#description}

Toggles the sitting state for cats, dogs, foxes, and parrots.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| setSitting | state | Sets the sitting state | false |

## Examples {#examples}

Makes the wolf sit when right clicked.

```yaml
ExampleDog:
  Type: Wolf
  Skills:
  - sit{state=true} @Self ~onInteract
```

## Aliases: {#aliases}

- sit
