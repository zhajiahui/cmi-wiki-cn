# Open Trades

## Description {#description}

Opens the trades of the casting villager to the target player

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| realTrade | real | Whether the opened trades should be the ones of the actual villager instead of a copy of them, so that they do not impact the casting villager | true |

## Examples {#examples}

```yaml
  Skills:
  - opentrades @PIR{r=10;limit=1;sort=NEAREST}
```

## Aliases {#aliases}

- opentrade
- trade
