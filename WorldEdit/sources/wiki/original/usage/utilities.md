# Utilities { #utilities }

WorldEdit provides a handful of utility commands. These are often conveniences for common tasks which would require multiple commands and selections otherwise. All these commands operate on your placement position. By default, this is your player position, but it can be changed to your first selection position using the `/toggleplace` command.

<a id="contents"></a>

- [Editing nearby blocks](https://worldedit.enginehub.org/en/latest/usage/utilities/#editing-nearby-blocks)

- [Filling pits](https://worldedit.enginehub.org/en/latest/usage/utilities/#filling-pits)



  - [Recursive Fill](https://worldedit.enginehub.org/en/latest/usage/utilities/#recursive-fill)

- [Draining pools](https://worldedit.enginehub.org/en/latest/usage/utilities/#draining-pools)

- [Fixing pools](https://worldedit.enginehub.org/en/latest/usage/utilities/#fixing-pools)

- [Simulating snowfall](https://worldedit.enginehub.org/en/latest/usage/utilities/#simulating-snowfall)

- [Thawing snow](https://worldedit.enginehub.org/en/latest/usage/utilities/#thawing-snow)

- [Simulating grass growth](https://worldedit.enginehub.org/en/latest/usage/utilities/#simulating-grass-growth)

- [Extinguishing fires](https://worldedit.enginehub.org/en/latest/usage/utilities/#extinguishing-fires)

- [Removing mobs](https://worldedit.enginehub.org/en/latest/usage/utilities/#removing-mobs)

## Editing nearby blocks { #editing-nearby-blocks }

Sometimes you want to set or replace blocks in an area, but don’t need a precise selection - you just want to use an area around you.

Removing blocks above and below:

```text
/removeabove <size> [height]
/removebelow <size> [depth]
```

These two commands let you easily remove blocks above or below you. An example usage is to remove those tower blocks people create in order to get to a high point. The size parameter indicates the size of the cuboid to remove. The cuboid’s width and length will be `(size - 1) * 2 + 1`. The center of the cuboid is the block above the one that you are standing on. If you don’t specify a height or depth, the commands will extend to the extents of the world.

Removing nearby blocks:

```text
/removenear <mask> <size>
```

This command removes nearby blocks of a certain type. The size parameter indicates the size of the cuboid to remove. The cuboid’s width and length will be `(size - 1) * 2 + 1`. The center of the cuboid is the block above the one that you are standing on.

Replacing nearby blocks:

```text
/replacenear <size> <mask> <pattern>
```

If you need to quickly replace nearby blocks, this command is a nice shortcut. The size parameter indicates the size of the cuboid to replace. The cuboid’s width and length will be `(size - 1) * 2 + 1`. The center of the cuboid is the block above the one that you are standing on.

## Filling pits { #filling-pits }

```text
//fill <pattern> <radius> [depth]
```

The fill command will start at the your placement position and work outward and downward, filling air with the given pattern. Note that it only works straight downward from the starting layer, so while it will fill a pond, it will not fill a cave (that goes “outward” as it goes down).

The fill command will never go upwards from your starting position.

<a id="id1"></a>

![../../_images/fill_pond.png](https://worldedit.enginehub.org/en/latest/_images/fill_pond.png)

*An irregularly shaped pool filled with `//fill`. You wouldn’t have been able to replace air with water (with `/replace`) in this situation because the area doesn’t fit neatly into a cuboid.*

### Recursive Fill { #recursive-fill }

```text
//fillr <pattern> <radius>
```

Unlike the fill command, the recursive fill command *will* work outwards as it moves down, meaning it can fill caves and other holes that expand into the walls.

Like the fill command, it will not travel upwards beyond the starting y level.

## Draining pools { #draining-pools }

```text
//drain [-w] <radius>
```

The drain command can empty a pool of water or lava. It only removes connected blocks from the starting position, so it will not drain non-connected pools even if they are in the radius.

Adding the `-w` flag will also un-waterlog blocks, leaving them dry.

!!! note "Note"

    Some blocks, like kelp and seagrass, despite looking like they are waterlogged, do not actually have a “dry” state. If you’re trying to drain an ocean or river with these blocks, use `//removenear` (explained above) to remove those blocks first.

## Fixing pools { #fixing-pools }

```text
/fixwater <radius>
/fixlava <radius>
```

This command will replace “flowing” versions of lava and water with “stationary” ones within the radius. This was useful for fixing water features that had been partially removed with buckets or blocks broken. Note that since Mojang changed water mechanics relatively recently, `fixwater` is much less useful than before.

## Simulating snowfall { #simulating-snowfall }

```text
/snow <radius>
```

Cover snow over the general area! This algorithm will only cover blocks with snow if they should be covered (for example, torch blocks will not be covered). If an area has something above it (like an overhang), snow will not reach it. “Snowfall” is completely vertical.

!!! note "Note"

    The snow command does not yet build up layers of snow.

<a id="id2"></a>

![../../_images/snow.jpg](https://worldedit.enginehub.org/en/latest/_images/snow.jpg)

*Snowfall transforming a landscape*

## Thawing snow { #thawing-snow }

```text
/thaw <radius>
```

This command works exactly in the opposite way as the `/snow` command above, removing snow and ice from exposed areas.

## Simulating grass growth { #simulating-grass-growth }

```text
/green [-f] <radius>
```

Cover grass over the general area! This area works horizontally outwards to convert dirt into grass.

Using the `-f` flag will also turn coarse dirt into grass as well as regular dirt.

## Extinguishing fires { #extinguishing-fires }

```text
/ex [radius]
```

This is essentially a shortcut `/removenear fire <radius>`, to allow you to quickly put out fires.

## Removing mobs { #removing-mobs }

```text
/butcher [-pngabtfl] [radius]
```

This command removes nearby mobs. If you don’t specify a radius, all active mobs in the entire loaded world will be removed. The mobs will not drop their loot. Be aware that even if you kill all mobs, they will come back quickly if there isn’t anything else preventing spawning.

Butcher flags

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**Flag**</td>
<td markdown="span">**Description**</td>
</tr>
<tr>
<td markdown="span">`-p`</td>
<td markdown="span">Kills tamed pets</td>
</tr>
<tr>
<td markdown="span">`-n`</td>
<td markdown="span">Kills NPCs</td>
</tr>
<tr>
<td markdown="span">`-g`</td>
<td markdown="span">Kills golems</td>
</tr>
<tr>
<td markdown="span">`-a`</td>
<td markdown="span">Kills animals</td>
</tr>
<tr>
<td markdown="span">`-b`</td>
<td markdown="span">Kills ambient mobs</td>
</tr>
<tr>
<td markdown="span">`-t`</td>
<td markdown="span">Kills mobs with name tags</td>
</tr>
<tr>
<td markdown="span">`-f`</td>
<td markdown="span">Combines all of the above flags</td>
</tr>
<tr>
<td markdown="span">`-r`</td>
<td markdown="span">Kills armor stands</td>
</tr>
</tbody>
</table>
