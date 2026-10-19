# Bossborder

## Description {#description}

Traps the the target player within a vanilla world border around the caster.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the border | 32 |

## Examples {#examples}

```yml
  Skills:
  - bossBorder{r=40} @NearestPlayer{r=30}
```

## Aliases {#aliases}

- effect:bossBorder
- e:bossBorder
