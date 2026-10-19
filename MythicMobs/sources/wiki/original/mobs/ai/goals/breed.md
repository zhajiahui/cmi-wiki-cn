# Breed

## Description {#description}

Causes the mob to be able to breed with other mobs.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| speedmodifier | speed,s | The speed at which to move towards the partner | 1 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: COW
  AIGoalSelectors:
    - clear
    - breed{s=2}
```
