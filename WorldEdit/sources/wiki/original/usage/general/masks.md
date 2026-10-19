# Masks { #masks }

Masks, alongside [patterns](https://worldedit.enginehub.org/en/latest/usage/general/patterns/), are commonly used in WorldEdit commands. Unlike patterns, masks determine *which* blocks will be affected by commands, brushes, and so on.

Aside from commands that take a mask as a parameter (such as `//replace [mask] <pattern>`), you can also apply masks to individual [brushes](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/) by using the `/mask` command while holding the brush, or you can apply a mask to all your WorldEdit actions globally with `//gmask`.

!!! note "Note"

    Masks applied through different means will stack with each other. If you set your global mask with `//gmask dirt`, and then set a brush mask with `/mask stone`, that brush will not be able to modify any blocks at all! This is because the combined mask will only match blocks which are both stone *and* dirt!

!!! tip "Tip"

    You can clear your global mask by using `//gmask` again without arguments.

<a id="contents"></a>

- [Combining Masks](https://worldedit.enginehub.org/en/latest/usage/general/masks/#combining-masks)

- [Available Masks](https://worldedit.enginehub.org/en/latest/usage/general/masks/#available-masks)



  - [Block Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#block-mask)

  - [Mask Negation](https://worldedit.enginehub.org/en/latest/usage/general/masks/#mask-negation)

  - [Existing Block Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#existing-block-mask)

  - [Solid Block Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#solid-block-mask)

  - [Full Cube Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#full-cube-mask)

  - [Offset Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#offset-mask)

  - [Adjacency Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#adjacency-mask)

  - [Region Masks](https://worldedit.enginehub.org/en/latest/usage/general/masks/#region-masks)

  - [Clipboard Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#clipboard-mask)

  - [Block Category Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#block-category-mask)

  - [Random Noise Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#random-noise-mask)

  - [Block State Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#block-state-mask)

  - [Expression Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#expression-mask)

  - [Biome Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#biome-mask)

  - [Surface Mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#surface-mask)

## Combining Masks { #combining-masks }

To get a mask which matches the *intersection* of multiple masks, use a space to separate them. The intersection will match when *all* of the given masks match.

Example: Combining Masks

Replacing surface stone with dirt using a mask intersection:

```text
//replace "stone <air" dirt
```

Setting a mask which restricts the current brush to modifying air blocks in your selection:

```text
/mask "air #sel"
```

## Available Masks { #available-masks }

### Block Mask { #block-mask }

The simplest of masks, the block mask matches one or more blocks or block states. Just like the [single block pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/), you can specify either a block type alone, or a block type with any number of states specified. Unlike the pattern, masks will *not* use default values for unspecified block states - they will “fuzzy” match any value of the unspecified state(s).

To match more than one block, separate each with a comma.

Example: Using the block mask

Removing all oak fences from your selection:

```text
//replace oak_fence air
```

Removing all oak fences that are attached on the east side, and oak fence gates:

```text
//replace oak_fence[east=true],oak_fence_gate air
```

### Mask Negation { #mask-negation }

The `!` symbol can be used to negate everything that comes after it. That is, it matches anything *not* matched by a different mask. Any other mask can follow this.

Example: Negating a mask

Replace any block that isn’t dirt, stone, or grass with stone:

```text
//replace !dirt,stone,grass_block stone
```

### Existing Block Mask { #existing-block-mask }

The mask `#existing` will match any blocks that aren’t air. Note that this isn’t the same as !air, since the game actually has multiple types or air that it uses in some cases.

### Solid Block Mask { #solid-block-mask }

The mask `#solid` will match any blocks that are considered “solid”. That is - blocks that restrict entities (such as players) from moving through them.

### Full Cube Mask { #full-cube-mask }

The mask `#fullcube` will match any blocks that take up the entire block cube.

### Offset Mask { #offset-mask }

Using `>` (overlay) or `<` (underlay) preceding another mask will match blocks that are above or below the other mask, respectively.

Example: Offset masks

Creating a layer of slabs above planks in your selection:

```text
//replace >##planks smooth_stone_slab
```

### Adjacency Mask { #adjacency-mask }

Using ~ preceding another mask will match blocks that are adjacent to the other mask.

!!! note "Note"

    Adjacency for the case of this mask is defined as being directly next to or above/below. Diagonal blocks do not match.

Example: Adjacency masks

Surrounding all mob spawners with glowstone:

```text
//replace ~spawner glowstone
```

### Region Masks { #region-masks }

While it doesn’t make sense for commands like replace, setting a region mask can be very useful for using brushes inside a limited area. For example, if you want to brush some dirt around the base of your wall, you can select the wall, and then negate a region mask so that the dirt doesn’t affect the wall (but still affects the ground around it).

The first type of region mask is `#region` (aliases: `#sel`, `#selection`), which will make a copy of your region at the time you run the command and use that as the mask.

The second type of region mask is `#dregion` (d for dynamic, also `#dsel`, `#dselection`) which will always stay updated with your current selection.

### Clipboard Mask { #clipboard-mask }

The mask `#clipboard` will match any blocks that match the current clipboard. This can be paired with commands such as //regen -c` to match all blocks that are the same as natural generation.

### Block Category Mask { #block-category-mask }

Block categories, or [tags](https://minecraft.wiki/w/Tag) can also be used as masks. A category mask will match any block that is in that category. Just like the pattern, the syntax is ##&lt;tag&gt;.

Example: Block Category Masks

Replacing all carpets with a layer of snow:

```text
//replace ##carpets snow
```

### Random Noise Mask { #random-noise-mask }

The noise mask can create random noise. Specifying `%<percent>` will match the given percentage of blocks. Unlike the weighted patterns, `%50` is actually 50% of blocks.

!!! note "Note"

    Make note of the syntax difference here; Unlike patterns, the % sign preceeds the desired percentage for this mask

Example: Using the random noise mask

Randomly replacing 50% of your selection with stone:

```text
//replace %50 stone
```

### Block State Mask { #block-state-mask }

Like the block mask, this mask matches block states. Unlike the block mask, you don’t need to specify a block type. This means you can match any block that has a property in a given value.

The state mask has two modes, lenient and strict. In lenient mode (`^[state=value,...]`, it will match any block that has the given block states equal the given value, *or* any block that does not even have those properties. In strict mode (`^=[state=value,...]`), it will *only* match blocks that have the block states equal to that value.

Example: Using the block state mask

Removing all closed door, gates, and trapdoors:

```text
//replace ^=[open=false] air
```

### Expression Mask { #expression-mask }

This mask can evaluate a mathematical expression upon each block. The mask starts with `=` and then must have an [expression](https://worldedit.enginehub.org/en/latest/usage/other/expressions/) which can use the variables `x`, `y`, and `z`. The mask will match if the expression returns a positive value.

Example: Expression masks

Only edit blocks below a certain y-level:

```text
//gmask =y<64
```

Only edit blocks with air two blocks below:

```text
//gmask =queryRel(0,-2,0,0,0)
```

### Biome Mask { #biome-mask }

The biome mask matches blocks with the given biome. Its syntax is `$<biome id>`. The biome ID must be the [namespaced id](https://minecraft.wiki/w/Java_Edition_data_values#Biomes), with minecraft: being optional for vanilla biomes, and mod ids being required for mod-added biomes.

### Surface Mask { #surface-mask }

The surface mask matches blocks that are exposed to air on at least one face. This means it’ll match only the surface of an object, nothing fully occluded by other blocks.

The mask is `#surface` (alias `#exposed`).
