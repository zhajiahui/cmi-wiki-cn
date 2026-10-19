# Gamemode

## Description {#description}

Matches the target player's gamemode

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| mode | m | The gamemode to match | SURVIVAL |

### Mode Attribute {#mode-attribute}

Possible gamemodes are

- `SURVIVAL`
- `CREATIVE`
- `ADVENTURE`
- `SPECTATOR`

## Examples {#examples}

```yaml
ExampleSkill:
  Conditions:
  - gamemode{m=ADVENTURE} true
```

## Aliases {#aliases}

- gm
