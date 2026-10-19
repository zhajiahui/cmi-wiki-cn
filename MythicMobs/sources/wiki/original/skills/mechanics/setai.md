# Setai

## Description {#description}

Toggles the target AI

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| ai | state, value | Sets the new mob AI. `true` enables it, `false` disables it | false |

## Examples {#examples}

This example will turn off the ai of the mob for 5 seconds

```yaml
TemporaryAISwitcher:
  Skills:
  - setAI{ai=false} @self
  - delay 100
  - setAI{ai=true} @self
```

## Aliases {#aliases}

- ai
