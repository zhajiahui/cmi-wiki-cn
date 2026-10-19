# Tools { #tools }

Sometimes, running commands over and over is too tedious for some tasks. WorldEdit comes with a wide variety of tools which can be bound to an item and will activate upon clicking on a block. Most tools activate on right-click, while some also have actions for left-clicks. Some tools, including all “brush”-style tools, can be used at a distance, and will act as if you clicked the block you are looking at, even from far away.

To use a tool, hold an item in your hand, then bind the desired tool by name using `/tool [name]` . You will get a message that the tool was bound to that item. Now, every time you activate the tool (by clicking with the item in your hand), that tool will perform its action. **To unbind a tool, hold the item and use the** `/tool none` **command.**

!!! tip "Tip"

    The selection wand (default: wooden axe, bound with `/tool selwand`) and navigation wand (default: compass, bound with `/tool navwand`) are technically tools. They are described on the [selections](https://worldedit.enginehub.org/en/latest/usage/regions/selections/) and [navigation](https://worldedit.enginehub.org/en/latest/usage/navigation/) pages respectively. You can bind and unbind them just as any other tool.

<a id="contents"></a>

- [Tool Listing](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#tool-listing)



  - [Tree generation tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#tree-generation-tool)

  - [Floating tree remover](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#floating-tree-remover)

  - [Block replacer tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#block-replacer-tool)

  - [Long range building tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#long-range-building-tool)

  - [Long range wand](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#long-range-wand)

  - [Cycler Tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#cycler-tool)

  - [Query Tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#query-tool)

  - [Flood fill tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#flood-fill-tool)

- [Super-pickaxes](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#super-pickaxes)



  - [Single Superpick](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#single-superpick)

  - [Area Superpick](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#area-superpick)

  - [Recursive Superpick](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#recursive-superpick)

- [Brushes](https://worldedit.enginehub.org/en/latest/usage/tools/tools/#brushes)

## Tool Listing { #tool-listing }

### Tree generation tool { #tree-generation-tool }

```text
/tool tree [type]
```

This tool will generate a tree of the chosen type when you right click a block. Note that it uses Minecraft’s tree generator, and has the same limitations - it will not generate trees on unplantable blocks, or through solid blocks above (unless the tree would normally be able to grow there).

### Floating tree remover { #floating-tree-remover }

```text
/tool deltree
```

Have players who chop down trees half-way and leave floating tree tops everywhere? This tool, upon right-clicking a floating leaf or log block (or mushroom block), will remove all connected floating tree blocks. This tool will not operate on trees that are still connected to something (such as the ground).

### Block replacer tool { #block-replacer-tool }

```text
/tool repl <pattern>
```

This tool will replace the right-clicked block with a block from your pattern. You can also left-click a block to replace your current pattern with the left-clicked block.

### Long range building tool { #long-range-building-tool }

```text
/tool lrbuild <leftclick pattern> <rightclick pattern>
```

This tool allows you to place and destroy blocks at a distance. Just aim and click. Blocks are placed as if you right clicked the block. If you set one of the blocks to air, it will instead delete the block you are targeting.

### Long range wand { #long-range-wand }

```text
/tool farwand
```

This tool works just like the normal selection wand - but at any distance. Instead of being `//pos1` and `//pos2`, it’s `//hpos1` and `//hpos2`.

### Cycler Tool { #cycler-tool }

```text
/tool cycler
```

This tool can be used to cycle a block’s states. Left-clicking will choose which property to cycle, and right-clicking will cycle the available values of that property. This is useful for example, to rotate individual blocks in place.

### Query Tool { #query-tool }

```text
/tool info
```

The query tool will show information about the right-clicked block. It will show the coordinates, the block type, states, light level (emitted/above), and the internal id (if available).

### Flood fill tool { #flood-fill-tool }

```text
/tool floodfill <pattern> <range>
```

The flood fill tool will, starting at the right-clicked block, change it and all connected blocks of the same type (within the given range) to the specified pattern.

## Super-pickaxes { #super-pickaxes }

Super-pickaxes are slightly different than other tools. Instead of being bound to a single item, they are just toggled on or off with their commands. When on, left-clicking with *any* pickaxe in your hand will trigger the superpick. Unlike normal tools, they are toggled off with `//`.

### Single Superpick { #single-superpick }

```text
//
/sp single
```

This super-pickaxe allows you to instantly break blocks. That may seem redundant, but it predates creative mode (creative mode was removed before alpha and wasn’t re-added until Beta 1.8). It also will drop the blocks you break as items ([configurably](https://worldedit.enginehub.org/en/latest/config/)), which creative mode does not do.

### Area Superpick { #area-superpick }

```text
/sp area <radius>
```

This super-pickaxe will break all blocks matching the same type as the initially clicked block within the radius. Like the single mode superpick, it can be configured to drop items.

### Recursive Superpick { #recursive-superpick }

```text
/sp recur <radius>
```

This super-pickaxe also breaks all blocks matching the same type as the initially clicked block within the radius, but only those that are connected (via matching blocks) to the original. Think of this as a “vein miner” mode.

## Brushes { #brushes }

Unlike the above tools, which are mostly for utility, another group of tools, known as brushes, are mainly designed for painting and building quickly from afar.

They can be found on the [brush page](https://worldedit.enginehub.org/en/latest/usage/tools/brushes/).
