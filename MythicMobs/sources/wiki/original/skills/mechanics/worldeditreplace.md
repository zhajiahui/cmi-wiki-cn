# World Edit Replace

## Description {#description}

Replaces blocks in a region using WorldEdit. Needs a [@region](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Region) or similar targeter

> **This is a [Premium-Only](https://wiki.mythiccraft.io/mythicmobs/Premium-Features) mechanic!**

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| from | f | The material to replace | AIR |
| to | t | The material to set in place of the replaced one | AIR |

## Examples {#examples}

```yaml
  Skills:
  - worldEditReplace{from=STONE;to=AIR} @Region{min=0,0,0;max=100,100,100;world=resources}
```

## Aliases {#aliases}

- weReplace
