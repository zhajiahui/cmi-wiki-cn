# Brushes { #brushes }

Brush tools are general more designed for building, sculpting, and painting than the general utility [tools](https://worldedit.enginehub.org/en/latest/usage/tools/tools/). Like the rest of the tools, they are bound to an item by using the command, and are activated by right-clicking (or left clicking, for those with two actions). They are unbound with the `/brush none` command.

Brushes have a few unique settings available to them. Brushes allow you to choose a mask, size, pattern, and range. These allow fine-tuning how you build and paint.

<a id="contents"></a>

- [Brush Listing](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#brush-listing)



  - [Sphere brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#sphere-brush)

  - [Cylinder brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#cylinder-brush)

  - [Set brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#set-brush)

  - [Clipboard brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#clipboard-brush)

  - [Smooth brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#smooth-brush)

  - [Gravity brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#gravity-brush)

  - [Forest brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#forest-brush)

  - [Extinguish brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#extinguish-brush)

  - [Butcher brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#butcher-brush)

  - [Deform brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#deform-brush)

  - [Biome brush](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#biome-brush)

- [Brush Settings](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#brush-settings)



  - [Mask](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#mask)

  - [Size](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#size)

  - [Material](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#material)

  - [Range](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#range)

  - [Trace Mask](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/#trace-mask)

## Brush Listing { #brush-listing }

### Sphere brush { #sphere-brush }

```text
/brush sphere [-h] <pattern> [radius]
/br s [-h] <pattern> [radius]
```

The sphere brush, as its name suggests, creates sphere at the target point. The `-h` flag will make a hollow sphere.

### Cylinder brush { #cylinder-brush }

```text
/brush cylinder [-h] <pattern> [radius] [height]
/br cyl [-h] <pattern> [radius] [height]
```

The cylinder brush creates cylinders of the given radius and height. `-h` is hollow as usual.

### Set brush { #set-brush }

```text
/brush set <shape> [size] <pattern>
```

The set brush can set spheres, cylinders, or cuboids of the given size and pattern. It is mostly redundant to the previous two brushes, unless you need a cube.

### Clipboard brush { #clipboard-brush }

```text
/brush clipboard [-aoeb] [-m <mask>]
```

The clipboard brush uses your clipboard as a shape and places it at the target location each brush activation. The `aebm` flags all work just like the [paste command](https://worldedit.enginehub.org/en/latest/usage/clipboard/). The `-o` flag is a bit different - it makes the clipboard paste at the brush’s location as the origin. Otherwise, the clipboard is centered to that location. Choose your relative position carefully when copying a clipboard for use with this brush.

### Smooth brush { #smooth-brush }

```text
/brush smooth [radius] [iterations] [mask]
```

Smoothes the area, just like the `//smooth` command explained in [region ops](https://worldedit.enginehub.org/en/latest/usage/regions/regionops/). You can specify the mask of blocks to consider while building a heightmap (this is separate from the mask of blocks that will be affected).

### Gravity brush { #gravity-brush }

```text
/brush gravity [radius] [-h]
```

The gravity brush will move blocks downwards within the affected brush area. Using the `-h` flag will start from the max y, instead of from the top of the brush area.

### Forest brush { #forest-brush }

```text
/brush forest <shape> [radius] [density] <tree type>
```

Like the `//forest` and `//forestgen` commands, this brush plants trees, using the shape, radius, density, and tree type provided.

### Extinguish brush { #extinguish-brush }

```text
/brush extinguish [radius]
/br ex [radius]
```

A handy shortcut for a sphere brush of air masked to fire blocks, in case something is burning and you don’t have time to type in 3 commands to put it out.

### Butcher brush { #butcher-brush }

```text
/brush butcher [radius] [-pngabtfr]
/br kill [radius] [-pngabtfr]
```

Just like the `//butcher` [utility command](https://worldedit.enginehub.org/en/latest/usage/utilities/), the butcher brush kills entities in its area. Note that the radius is strictly cylindrical, but goes from minimum to maximum world height. It is not a sphere. By default, it only kills hostile mobs. The flags can be specified to determine what other mobs will be butchered.

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

### Deform brush { #deform-brush }

```text
/brush deform <shape> [size] [expression] [-ro]
```

Just like the `//deform` command described in [region operations](https://worldedit.enginehub.org/en/latest/usage/regions/regionops/), this brush will apply an expression to blocks within the area given by the shape and radius. Also just like the command, `-r` uses raw coordinates, and `-o` offsets from your placement position. The default is the brush target point.

#### Raise Brush { #raise-brush }

```text
/brush raise <shape> [size]
```

A special case of the deform brush which uses the expression `y-=1`.

#### Lower Brush { #lower-brush }

```text
/brush lower <shape> [size]
```

A special case of the deform brush which uses the expression `y+=1`.

### Biome brush { #biome-brush }

```text
/brush biome <shape> [radius] <biomeType>
```

Sets the biome within the area given by the shape and radius. Keep in mind that since 1.15 the biomes are 3D and the smallest area you can change is a 4x4x4 cuboid. Effects can’t be seen until you rejoin the world.

## Brush Settings { #brush-settings }

These commands modify the settings on your *currently selected* brush only. Each brush you have bound has its own settings.

Not all settings are used by all brushes - the clipboard brush doesn’t have a size setting (it uses your clipboard’s size), the butcher brush doesn’t have a mask or material (it affects entities, not blocks), and so on.

### Mask { #mask }

```text
/mask [mask]
/mask
```

Sets a [mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/) on your current brush, which restricts what blocks will be affected by it. Not specifying a mask will disable it for your brush, allowing it to affect everything again. Note that if you already have a global mask set with `//gmask`, it will be combined with this one.

### Size { #size }

```text
/size [size]
```

Sets the size of the brush. Generally, this means the radius or affected area. Note that the maximum size is [configurable](https://worldedit.enginehub.org/en/latest/config/).

### Material { #material }

```text
/material <pattern>
```

Sets the pattern used by the brush.

### Range { #range }

```text
/range <range>
```

Sets the maximum range that the brush will try to build at. Note that with a short enough range, brushes *will build in mid-air* if they can’t find a block in your ray trace.

### Trace Mask { #trace-mask }

```text
/tracemask [mask]
/tracemask
```

Sets the mask used for the ray tracer. By default, brushes will perform their action on the first non-air block (or when the trace hits the range, whichever comes first). By setting the tracemask, you can make brushes trace through any block you choose. For example, `/tracemask #solid` will go through non-solid blocks, such as water. This is useful for building underwater, through walls, and whatever else.
