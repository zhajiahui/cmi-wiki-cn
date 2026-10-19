# Patterns { #patterns }

You may have noticed (or if you haven’t yet, you soon will) that many WorldEdit [commands](https://worldedit.enginehub.org/en/latest/commands/) take a “pattern” as a parameter. Patterns range from very simple (such as a single block - `stone`) to very complex. Patterns determine what blocks get set into the world as a command, tool, etc operates.

<a id="contents"></a>

- [Available Patterns](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#available-patterns)



  - [Single Block Pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#single-block-pattern)

  - [Random Pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#random-pattern)

  - [Random State Pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#random-state-pattern)

  - [Clipboard Pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#clipboard-pattern)

  - [Type or State Applying Pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#type-or-state-applying-pattern)

  - [Block Category Pattern](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#block-category-pattern)

- [Special Block Data Syntax](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#special-block-data-syntax)



  - [Sign Text](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#sign-text)

  - [Player Heads](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#player-heads)

  - [Mob Spawners](https://worldedit.enginehub.org/en/latest/usage/general/patterns/#mob-spawners)

## Available Patterns { #available-patterns }

!!! note "Note"

    This list may be incomplete as patterns are added to WorldEdit. In addition, our API allows other plugins to register new patterns, which will not be listed here.

!!! tip "Tip"

    Here’s a video detailing some of these patterns which were added in WorldEdit 7: [https://www.youtube.com/watch?v=S5wCVMf3SvM](https://www.youtube.com/watch?v=S5wCVMf3SvM)

### Single Block Pattern { #single-block-pattern }

The most basic pattern of just a single block. A block is identified by three parts: the [block type](https://minecraft.wiki/w/Java_Edition_data_values#IDs), additional [block states](https://minecraft.wiki/w/Block_states), and [nbt data](https://minecraft.wiki/w/NBT_format). These three links to the Minecraft Wiki, along with WorldEdit’s in-built tab-completion for commands, should guide you in specifying the block you want. Additional states are always appended to the type using the syntax `block_type[state1=value,state2=value,...]`. Note that when states are not specified, or if some are left out, the default values will be used for those states. NBT is written using Minecraft’s SNBT syntax, `block_type{'nbt_key':'value'}`. NBT data always comes after the block states if supplied, `block_type[property=value]{'nbt_key':'value'}`.

Instead of specifying a block type directly, you can use `hand` or `offhand` to use the block held in your main hand or offhand respectively. This is useful when you already have the block you want to use in your hotbar. You can also use `pos1` to use the block at your primary selection point. See [Selection Modes](https://worldedit.enginehub.org/en/latest/usage/regions/selections/#selection-modes) for what that means for the various selection types. Only `pos1` will currently retain any state or NBT (e.g. using `hand` with a shulker box will place an empty one).

The states and NBT can still be set when using these, as if it were a normal block type. A top-level merge occurs for both state and NBT, with the keys specified in the command taking precedence.

Example: Single block patterns

Setting a selection to stone:

```text
//set stone
```

Setting a selection to a note block with a specific instrument and pitch:

```text
//set note_block[instrument=chime,note=18]
```

Setting a selection to an oak stair block facing east with the bigger part on top:

```text
//set oak_stairs[facing=east,half=top]
```

Setting a selection to an oak sign that is waxed:

```text
//set oak_sign{'is_waxed':1}
```

Setting a selection to an oak sign that is waxed and rotated:

```text
//set oak_sign[rotation=12]{'is_waxed':1}
```

Setting a selection to the block in your main hand:

```text
//set hand
```

Setting a selection to the block in your main hand, applying a `facing` state override:

```text
//set hand[facing=east]
```

Setting a selection to the block in your offhand:

```text
//set offhand
```

Setting a selection to the block at pos1:

```text
//set pos1
```

### Random Pattern { #random-pattern }

This pattern allows setting random blocks from any number of other patterns. The basic form is as simple as a comma-separated list of patterns, which will be chosen from evenly. You can also specify weights for each pattern with `<x>%<pattern>`.

Example:: Random Patterns

Setting a selection to different types of stone, equally distributed:

```text
//set stone,diorite,andesite,granite
```

Setting a selection to mostly red wool, with a small amount of glass (5:1 ratio, see note below):

```text
//set 50%red_wool,10%red_stained_glass
```

!!! note "Note"

    Despite the percentage sign, weights need not add up to 100. They are cumulative and will be divided by the total. That is, `5%dirt,15%stone` means 25% of blocks will be dirt, and 75% will be stone. In other words, weights are relative to each other, not to 100. Because of that, the pattern `5%dirt` isn’t valid. If you only want to set 5% of blocks to dirt, you should use the [random noise mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#random-noise-mask).

!!! tip "Tip"

    You can use any other pattern as one of the choices, not just the single block pattern. Keep reading to see more patterns…

### Random State Pattern { #random-state-pattern }

Prefixing any block type with an asterisk (`*`) will randomly choose between all states for that block for each position.

Example: Random State Pattern

Setting oak logs facing in random directions:

```text
//set *oak_log
```

### Clipboard Pattern { #clipboard-pattern }

The `#clipboard` pattern will take blocks from your [clipboard](https://worldedit.enginehub.org/en/latest/usage/clipboard/) in the same arrangement. This makes it easy to build one part of a repeating complicated pattern by hand, and then repeat it over and over. You can also offset the pattern by adding `@[x,y,z]`.

Example: Using the clipboard pattern

Replacing [all existing blocks](https://worldedit.enginehub.org/en/latest/usage/general/masks/#existing-block-mask) to your clipboard:

```text
//replace #existing #clipboard
```

**Using the clipboard in the first image to replace a hill. Note the repeating layers.**

[![clipboard_pattern](https://worldedit.enginehub.org/en/latest/_images/clipboard.png)](https://worldedit.enginehub.org/en/latest/_images/clipboard.png) [![clipboard_replace](https://worldedit.enginehub.org/en/latest/_images/clipboard_replace.png)](https://worldedit.enginehub.org/en/latest/_images/clipboard_replace.png)

Using an offset to align the clipboard:

```text
//set #clipboard@[2,0,1]
```

### Type or State Applying Pattern { #type-or-state-applying-pattern }

This pattern, prefixed by `^`, lets you set the type or states of a block without modifying everything else. This pattern will, for example, allow you to change a spiral staircase from oak to acacia without having to worry about the stairs facing in different directions and so on. You can either specify a block type (to change block type but not states, where applicable), or any number of states (to only change those states, where applicable).

Example: Type/State Applying Patterns

Replacing all oak stairs to acacia stairs, while maintaining orientation, etc:

```text
//replace oak_stairs ^acacia_stairs
```

Removing the water from all waterloggable blocks:

```text
//set ^[waterlogged=false]
```

Doubling up all slabs:

```text
//replace ##slabs ^[type=double]
```

Replacing all stairs with a random selection of stairs, while maintaining orientation, etc:

```text
//replace ##stairs ^##stairs
```

### Block Category Pattern { #block-category-pattern }

This pattern allows setting random blocks within a block category, often referred to as a “[tag](https://minecraft.wiki/w/Tag)”. Tags allow grouping blocks together under a single name. Minecraft comes with many tags inbuilt (see the link) and also allows creating and modifying tags via data packs. You may already have noticed these tags being used as a [mask](https://worldedit.enginehub.org/en/latest/usage/general/masks/#block-category-mask) in the example above (`##slabs`).

The syntax for this pattern is `##<tag name>`, which will randomly choose between the default state of all blocks in the category. You can also mix this with the random state pattern (`##*<tag name>`) to use all states, not just the defaults.

Example: Block Category Pattern Usage

Replacing all existing blocks with rainbow wool:

```text
//replace #existing ##wool
```

Setting the selection to random types of slabs, both top/bottom/double, and waterlogged at random:

```text
//set ##*slabs
```

## Special Block Data Syntax { #special-block-data-syntax }

Some blocks have additional syntax for setting extra information.

### Sign Text { #sign-text }

You can set text on signs by separating it with a pipe symbol (`|`). Note that if the text has spaces, you must wrap the entire pattern in quotes `""`.

Example: Setting sign text

Simple Example:

```text
//set oak_sign|Line1|Line2
```

With spaces and rotation:

```text
//set "oak_wall_sign[facing=north]|Hello world|Second|Third line"
```

### Player Heads { #player-heads }

You can set the skin of a player head by specifying a username after the pipe symbol.

Example: Setting a skin on a head

```text
//set player_head|dinnerbone
```

### Mob Spawners { #mob-spawners }

You can set the type of mob to be spawned (again via the pipe symbol). Note that the name of the mob must be an [entity ID](https://minecraft.wiki/w/Java_Edition_data_values#Entities). Prefixing minecraft: is optional, modded mobs must have a namespace.

Example: Creating a squid spawner

```text
//set spawner|squid
```
