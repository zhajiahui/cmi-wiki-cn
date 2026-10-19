# Setlevel

## Description {#description}

Causes the casting mob to change its level.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| action | a | The type of the operation to perform | SET |
| level | l | Amount used in the operation | 1 |

## Action Attribute {#action-attribute}

Available actions are

- `SET`
- `ADD`
- `SUBTRACT`
- `MULTIPLY`
- `DIVIDE`

## Examples {#examples}

This will set the mob level to 3 when it spawns

```yaml
    - setlevel{a=set;l=3} @self ~onSpawn
```

##  {#section}

This will increase the mob level by 1 each time it kills a player

```yaml
    - setlevel{a=add;l=1} ~onKillPlayer
```

##  {#section-2}

This will set the level of the mob to a random value between 1 and 5 when it spawns, plus the score of the `__GLOBAL__` fake player from the "testlevel" scoreboard.

```yaml
    - setlevel{a=set;l="<random.1to5> + <global.score.testlevel>"} @self ~onSpawn
```

> The usage of [Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders) and [Math Operations](https://wiki.mythiccraft.io/mythicmobs/Skills/Math) inside of a non-string attribute is [**Premium Only**](https://wiki.mythiccraft.io/mythicmobs/Premium-Features)

## Aliases {#aliases}

- modifylevel
