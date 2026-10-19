# Bloody Screen

## Description {#description}

Shows the near world border effect.  
Players must enable Fancy Graphics to see the effect.

Note: Players with the effect are unable to use the trigger "onUse" in skills.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| duration | d | The time (in ticks) that the effect is active | 20 |
| cancel | c | If true, it stops any existing redscreen | false |

## Examples {#examples}

```yaml
BloodyEffect:
  Skills:
  - effect:bloodyScreen{d=25} @PIR{r=15} ~onTimer:20
```

## Aliases {#aliases}

- effect:bloodyScreen
- e:bloodyScreen
- redScreen
- effect:redScreen
- e:redScreen
