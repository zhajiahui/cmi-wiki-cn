# Dropitem

## Description {#description}

Drops a set of items or optionally a
[DropTable](https://wiki.mythiccraft.io/mythicmobs/drops/DropTables).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| items | item, i | Items to drop. Can be a comma-separated list of items, or a DropTable. You can specify an amount by putting a space and a number after the item name. | NONE |
| naturally | natural, n | Whether the items should be dropped naturally | true |
| onDropSkill | onDrop, then | [Metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) to be execute when the item drops. Inherits the dropped item entity as the target(s) |  |
| dynamic | fd | Forces the drop to be parsed as a dynamic item each time | false |

## Examples {#examples}

Example of dropping specific items.

```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond} @self ~onDeath
  - ...
```

The below example will drop a Diamond Sword and 5 Diamonds

```yaml
  Skills:
  - dropitem{i=diamond_sword,diamond 5} @self ~onDeath
  - ...
```

##  {#section}

Example of dropping items from a DropTable.

```yaml
  Skills:
  - dropitem{i=SkeletonKingDrops} @self ~onSpawn
  - ...
```

## Aliases {#aliases}

- drop
- dropitems
- itemdrop
