# Enchanting Experience

## Description {#description}

Checks the experience points that the target player has.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| level | l, amount, a | Checks against the experience points missing to reach the next level, in a range from 0 to 1. 0 is "no progress" and 1 is "next level". Accepts ranges. | 0 |

## Examples {#examples}

```yaml
  TargetConditions:
  - enchantingExperience{l=>0.2} true
```

## Aliases {#aliases}

- enchantingExp
- enchantExperience
- enchantExp
