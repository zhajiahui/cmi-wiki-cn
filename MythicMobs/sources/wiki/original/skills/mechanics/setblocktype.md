# Setblocktype

## Description {#description}

Change blocktype at target location.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| material | m, mat, t, type, types, block, b | The material for the block to be set to | [DIRT](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html "CLICK ME to view valid block materials") |
| physics | p | Whether to apply physics to the affected area | true |

## Examples {#examples}

Sets a block at the location of the caster

```yaml
SetBlockExample:
  Skills:
  - setblock{m=STONE} @selflocation
```

##  {#section}

Sets a mmoitems block at the location of the target

```yaml
SetMMOItemsBlock:
  Skills:
  - setblock{m=mmoitems:50} @targetlocation
```

##  {#section-2}

Sets a block with specified blockstates at the location of the target

```yaml
SetButton:
 Skills:
 - setblock{m=JUNGLE_BUTTON[facing=east,face=floor]} @targetlocation
```

## Aliases {#aliases}

- setblock
