# Hastag

## Description {#description}

Tests if the target has a scoreboard tag

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| tag | t | The tag to check for |  |

## Examples {#examples}

```yaml
  Conditions:
  - hastag{t=KilledBoss1} true
```

```yaml
  TargetConditions:
  - hastag{t=PuzzleRoom1Solved} true
```

## Aliases {#aliases}

- hasScoreboardTag
