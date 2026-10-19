# Mobsinradius

## Description {#description}

Checks how many mobs are in a given radius

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| types | type, t | The types of mobs to check for |  |
| amount | a | The range of mobs to check for. The caster is not counted | 1 |
| radius | r | The radius to check | 5 |

## Examples {#examples}

### Single type {#single-type}

```yaml
  Conditions:
  - mobsInRadius{types=NewZombie;amount=5to10;radius=15}
```

### Multiple types {#multiple-types}

```yaml
  Conditions:
  - mobsInRadius{types=NewZombie,NewSkeleton,NewSpider;amount=5to10;radius=15}
```
