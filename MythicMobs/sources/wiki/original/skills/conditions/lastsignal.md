# Lastsignal

## Description {#description}

Matches the last signal received by the target mob

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| signal | s | The signal to match | DEFAULT |

## Examples {#examples}

```yaml
  Conditions:
  - lastsignal{s=fireCannonShot} true
```
