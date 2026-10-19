# Mobs Near Origin

## Description {#description}

Matches a range to how many mobs are in the given radius around the [origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount of mobs to match. Can be a range | 1 |
| radius | r | The radius in which to match mobs | 5 |
| types | type, t | The mob types to match. Can be a list |  |

## Examples {#examples}

```yaml
  Conditions:
  - mobsnearorigin{type=ExampleMob,SuperDuperStrongMob;r=10;amount=>5}
```
