# Undopaste

## Description {#description}

Undoes a previous paste done via the [fawePaste](https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/fawepaste) mechanic, based on its id or on the schematic used

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| pasteID | pid, id | The id of the paste that needs to be undone |  |

> This mechanic inherits every *inheritable* attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Aura) mechanic

## Examples {#examples}

```yaml
ExampleMob:
  Skills:

  # With ID
  - fawePaste{s=cgym.schem;id=abc} @self ~onSpawn
  - undoPaste{id=abc} @self ~onDamaged

  # Without ID
  - fawePaste{s=lab.schem} @self ~onSpawn
  - undoPaste{id=lab.schem} @self ~onDamaged
```

## Aliases {#aliases}

- undoschem
- undoschematic
