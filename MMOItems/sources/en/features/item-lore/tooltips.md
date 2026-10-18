# 🖼️ Item Tooltips {#🖼️-item-tooltips}

Tooltips are what players see when hovering an item inside any inventory. While vanilla Minecraft does feature an option to modify the tooltip texture of any item, this functionality is very limited (color only). Although it is also possible to manually setup custom tooltips without using the dedicated MMOItems feature, MMOItems makes it more systematic and very much easier.

Specific tooltips can be bound to items, tiers, item types or even item modifiers. Specific tooltips bound directly to items and modifiers have precedence over tooltips granted by item tiers, and item tiers also have tooltip precedence over item type tooltips.

## General Principle & Examples {#general-principle-examples}

Tooltips are entirely based on custom fonts as well as the [negative space font pack](https://github.com/AmberWat/NegativeSpaceFont). MMOItems injects custom fonts inside the item display name and lore to give the impression of a tooltip background texture.

![image.png](https://docs.phoenixdevt.fr/assets/tt_ex_1.nBTXNtJu.png)![image.png](https://docs.phoenixdevt.fr/assets/tt_ex_2.DGpmT2QG.png)![image.png](https://docs.phoenixdevt.fr/assets/tt_ex_3.vtnaJwDX.png)

MMOItems provides three example tooltip configs (see above). These tooltips utilize textures from the [MMOItems Default Resource Pack](https://gitlab.com/phoenix-dvpmt/mmoitems-default-resource-pack), so make sure you download it and install it on your server beforehand. After installing this resource pack, give yourself the following items (these are all swords): `TOOLTIP_COPPER_SWORD`, `TOOLTIP_SILVER_SWORD` and `TOOLTIP_GOLD_SWORD`.

## How to create custom tooltips {#how-to-create-custom-tooltips}

Head to the `/tooltips` folder in your main MMOItems folder. All tooltip configs should be placed inside this folder. One YAML file may contain multiple tooltip configs, and you can group configs inside subfolders to have an organized folder hierarchy.

There are three steps when creating custom tooltips for MMOItems:

- drawing the actual tooltip textures following the few constraints associated with using custom fonts,
- binding these textures to random unicode characters
- setting up the MMOItems config files.

For our tutorial, we will be using the following item (located inside the `item/sword.yml` config file).

```yml
GOLD_SWORD:
  base:
    material: GOLDEN_SWORD
    name: Gold Shortsword
    attack-damage: 10.0
    attack-speed: 1.6
    tooltip: GOLD # This is where you give your item a tooltip
    element:
      fire:
        damage: 3.0
    required-class:
    - Warrior
```

## 1/ Textures {#_1-textures}

The first step to creating custom tooltips is drawing the tooltip textures. Tooltip textures are split into three different textures:

- The `top` texture, which generally includes the item display name and optionally item type and tier,
- The `middle` texture, a very simple pattern that gets copy-n-pasted once for every extra line in the item lore,
- The `bottom` texture, which is the bottom of the tooltip texture.

You can find below the tooltip textures of the default `gold` tooltip. **Make sure that your textures are at most 255 pixels wide!** This is the only major constraint when working with custom fonts.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAP8AAAAUCAYAAAE1jNsdAAAACXBIWXMAAAsSAAALEgHS3X78AAAC6UlEQVR42u2b2W7TUBCGS67Y24JKs7pp0iQNCUmzNyGhG1URqgAJVQgJoQoQqKIEXoEH4RV4D96Ba56Bux+P6USnVhRKvMTLXHxyemyPT2fm9/EZH88BmJslYxuXLy/DbvzVgcCF4Ne3r7MNwXD3vvUQLF5aAEEGtXntv6Hzfv/8MfII8f340Gij31bsct8medqyA5wQht183us754CgcqGDKLWsSEC9GVDKU+qzDFga06S/WQKOOsAPEnDMAaStUDuAhpFQOyAI0H2G5czDJbfJIGATXrtX0iBBA47adtKuGkw6Rh24ZsU0z3QzTwC/jBVBfaadeQL4Zaz0A5Omr55NgNPtrgTPJj7t9PyXAH56GBRCOAOghz1JApuDT87kUozKtKWdaeASlVpuUquu4yqx3KbOXNzsM/fbjBvJaZshL4yVavB5mmee1pmnp7RfnQr6vZgT2uAHDQm+BF+CL8GX4EvwJfgSfE8F3wsvR4IE+VOKPILl+gvXPMQfgog/AIIeJ2YWurqOhZdeqL+ZMxu4iG1BxO8KZ8k6WgvN2y/7g9DCfohEIucWyZqhfaqvVF+qtv5lg64jfh+cyz/VlyJ+h+A3LzL3E7wG56WIX8QviPhF/HaLX1aIC15dbS/id1j88nWA4NUvLUT8DoufvmaQZBNE/CEUv3wWJngRzksRv0PQ6iY/ij92NYrktRi0G3GkbyaQXUgidyuFwm0NxaUVlO+kUYmuYiOWQSORRSu1ho6WQ3+1gN18CVvZ9dF2f72Eg2IZj0v3cFiu4EmlimfVKp7XNnBUr+FFs46XrQZedZp43W3huNfG234H7x908WGri5PtHk71UWr4sG+8shrqc9WP+t/UTvvfDTbxRj+ezqPzyQ7ZI7tHDaKBp5W/16XrUz8e6f2hfu3l72InVzT6OcgU0EvnsbmSQ1v/f5rJLOrxDGo6vC0tacjrPlhbTCEznzR8k7oeR0L3VexK1Hff17qx+s4N/gBCU9hkp6/ClAAAAABJRU5ErkJggg==)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAP8AAAAKCAYAAAEMULj2AAAACXBIWXMAAAsSAAALEgHS3X78AAAAj0lEQVR42u3XMRJAMBRF0ZQ6pc4aFFZk/3v4aI3CRISMU9yW793/MpIiIh0ZuiFKc/aenfSLAZZ5amyAWlpqfuitAPYHtxDA2I9JAAJ4IICrtBJUK+dZjlALYAHeWYBtWOLKHudBPvnkk08++eST/7k//pKL5PaAD9/EqtzGlB9QfuUHlF/5AeVXfkD5c1gB2UD0vgDaxeEAAAAASUVORK5CYII=)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAP8AAAASCAYAAAHj1TgAAAAACXBIWXMAAAsSAAALEgHS3X78AAABgUlEQVR42u2bTUoDQRCFWyQoiASyyS6bbDQadeUpXLryD7c5hucQr+A9vINrbxDIbpwHtmTCiArV6eqZ78EHyYRAT7163TPpSQgtGu+PK2vCf5R9AH/RwWDvG3NZn/3DxTyvBbcnx/YWvD5eVcks2FZjZre6awVQVyQ5+evptCqhAMni0PsCaBbrdQGUrV4XIMXVg0g2aeVSKXNFKUu6+47e1P3ZKeYZoVoW1wClrBWlXNMW1wBVLQ1caDnIjcbx8fLUYKceptg87mnMQiqqASbDCck1RPXEfMzHfMzHfMzHfMzHfMzHfMzPrPX7Zg/3zCKOR8WMr1fvb437fq9jFgHZbKxEVNT198vnw7DVZwfQ70sIm0bgdQNO/clkQfiB8CPr8KvINBsQ/h6G/24+o9nAHepLwp84/DezI5oN3KG+JPyJwx9/ogfwhPqS8BN+IPzIWnEj3vsTGJ5YXJ631kzHpJ8+0/fazm20O+pUfayID4p0Ivx1X0DH+fp3ELWABp8g52NuMWWjuQAAAABJRU5ErkJggg==)

When an item is being generated, MMOItems injects the `top` texture at the beginning of the item display name. It then injects the `middle` texture at the beginning of every lore line (except the last one). The last lore line instead receives the `bottom` texture. Negative space fonts are crucial here, as MMOItems use them to align text and textures.

As you might have realized, the width of these textures is static. Unlike vanilla tooltips which expand to the longest lore line of the item, custom tooltip textures do not expand. You need to hard-pick a width for your tooltips and make sure your lore lines do not clip out. This is a known limitation of the current tooltip system (which might be expanded later on to support multiple tooltip widths).

## 2/ Resource Pack Configs {#_2-resource-pack-configs}

Install your tooltip textures inside your resource pack. For this tutorial, let's pretend they are located inside the folder `assets/tooltip_tutorial/textures/gold/`.

First make sure your server resource pack includes the [negative space font pack](https://github.com/AmberWat/NegativeSpaceFont). Then, head to your `assets/minecraft/font/default.json` config and add the following entries to your font map.

```json
{
    "providers": [
        {
            "type": "bitmap",
            "file": "tooltip_tutorial:gold/top.png",
            "ascent": 17,
            "height": 21,
            "chars": ["\u4070"]
        },
        {
            "type": "bitmap",
            "file": "tooltip_tutorial:gold/middle.png",
            "ascent": 8,
            "height": 10,
            "chars": ["\u4071"]
        },
        {
            "type": "bitmap",
            "file": "tooltip_tutorial:gold/bottom.png",
            "ascent": 8,
            "height": 17,
            "chars": ["\u4072"]
        },
    ]
}
```

As usual with custom fonts, there is one entry per texture.

- The `file` parameter corresponds to the path of your texture. Here, the namespace we chose for our textures/assets is `tooltip_tutorial`, but it can be anything you want.
- Make sure the `height` parameter exactly matches the height (in pixels) of your texture file, otherwise your in-game tooltip texture will look very weird.
- The `ascent` parameter must be fine-tuned in-game to make sure there are no gaps in your tooltip. First set it to something like half the height, reload your resource pack in-game and correct it.
- The `chars` field is where you select the unicode char. Take some unicode char that you are not using yet and store it somewhere, as we will need it later when setting up MMOItems configs.

## 3/ MMOItems Configs {#_3-mmoitems-configs}

You will find below one of the three tooltip config included in the default MMOItems config files. These can be found in the `tooltips/example_tooltips.yml` config file.

```yml
gold:
  top:  "{-41sp}\u4070{-166sp}"
  middle: "{-41sp}\u4071{-166sp}"
  bottom: "{-41sp}\u4072"
  align_texture: 0 # Optional
  align_text: 0 # Optional
  center_top:
    display_name: true
    span: 161
    default_char_size: 5
    lore_lines: 1
    char_size: [f4, i1, k4, l2, t3, I3, "'1", ' 3', ',1', '(3', ')3']
    regex: "[a-zA-Z0-9 ',()+]"
```

### Textures {#textures}

`top`, `middle` and `bottom` is where you specify the unicode char used for your three textures. These options are the actual strings that will be injected into your item. These strings support custom colors, non-player based PAPI placeholders and built-in `{<value>sp}` positive/negative space placeholders, that you can use to align your three textures.

### Align Texture and Text {#align-texture-and-text}

<details markdown="1">

<summary>Step-by-step tutorial for aligning tooltip textures</summary>

First, fill in your texture unicode characters. Add `debug: true` to your tooltip config, which will help visualizing where text would naturally align in the item lore (see screenshot below).

```yml
gold:
  debug: true
  top: "\u4070"
  middle: "\u4071"
  bottom: "\u4072"
```

![](https://docs.phoenixdevt.fr/assets/tt_align_1.C9I6lAkh.png)

The first step is to align the leftsides of your tooltip to the left of the vanilla tooltip. I measured that there are 41px in between the two tooltip leftsides. This can be corrected by adding negative space fonts of value -41 **BEFORE** the tooltip texture unicode. In my case, the three textures happen to naturally align, but you might need to use different alignment values for your three textures.

```yml
gold:
  debug: true
  top: "{-41sp}\u4070"
  middle: "{-41sp}\u4071"
  bottom: "{-41sp}\u4072"
```

![](https://docs.phoenixdevt.fr/assets/tt_align_2.CXSL4J8O.png)

Now the vanilla and custom tooltip leftsides are perfectly aligned. We now need to align the lore text with the leftmost pixel of the debug bar `| <= Vanilla Text Aligns Here`. You can do that by measuring the number of pixels in between the debug bar and the leftmost pixel of the lore text. Again, alignment values might differ for the 3 tooltip textures, but mine happen to coincide. I measured 166 pixels. Again, this can be corrected by adding negative fonts **AFTER** the tooltip texture unicode.

```yml
gold:
  top:  "{-41sp}\u4070{-166sp}"
  middle: "{-41sp}\u4071{-166sp}"
  bottom: "{-41sp}\u4072"
```

Boom! Here's how your item looks in-game, after toggling off the `debug` option.

![image.png](https://docs.phoenixdevt.fr/assets/tt_align_3.BQbHCz3N.png)

</details>

`align_texture` is an integer; it can be used to horizontal-shift all tooltip textures at once. Usually, you want to leave it to 0 first, align all three textures using negative space, and only then shift them all at once to the left (negative value) or the right (positive value).

`align_text` is an integer; it can be used to horizontal-shift all lore lines and item name at once. This is usually used to account for tooltip textures which are "thicker" than others. Just like the option above, you usually want to leave it to 0, align all lore lines using negative space, and only then shift them all at once using this option. In our case, our tooltip textures are as "thick" as the vanilla tooltip so there's no need to use a non-zero value.

### Displaying item type and tier {#displaying-item-type-and-tier}

Let's now say you want to display the item type and tier right under the item name. Copy and paste the following syntax block to your tooltip config:

```yml
gold:
  # ...
  lore_header:
  - '&6{tier} {type}'
```

This has the effect of inserting a set amount of lines at the very beginning of the item lore, during item generation. `{tier}` returns the item tier, and `{type}` returns the item type. `{tier}` will always return a non-empty value: if the item has no tier, this placeholder will return the value specified in the `default-tier-name` option, in the main MMOItems config file. By default, this value is set to `Common`, which explains what you see on the following screenshot.

![image.png](https://docs.phoenixdevt.fr/assets/tt_display_tier_type.BJ3tjGVj.png)

### Centering the tooltip header {#centering-the-tooltip-header}

The item name, tier and type look really nice, but let's say you want the item name and first lore line to be centered horizontally. This can be achieved using a few strings and proper configuration.

```yml
gold:
  # ...
  center_top:
    display_name: true
    lore_lines: 1
    span: 161
    default_char_size: 5
    char_size: [f4, i1, k4, l2, t3, I3, "'1", ' 3', ',1', '(3', ')3']
    regex: "[a-zA-Z0-9 ',()+]"
```

Set `display_name` to true if you want to center the item display name. Otherwise, MMOItems will only format the N first lore lines.

`lore_lines` corresponds to the amount of lines that you want centered. Here, we want to set this value to 1, because we need our lore header (that we added in the previous section) centered. By default, it is set to 0, in which case MMOItems will only center the item name (if `display_name` is toggled on).

#### The technical part... {#the-technical-part}

Before moving to the other options, you need to understand how MMOItems manages to have centered texts. This is not possible in vanilla Minecraft, however it can be achieved by offseting any text by the right amount of pixels, using positive-space fonts. Let's say your tooltip is `tooltip_width` pixels wide, and that you want to center a text of length `text_length`. You can do that by offseting your text to the right by the following amount:

```
offset_to_center = (tooltip_width - text_length) / 2
```

This is exactly the computation that MMOItems does. In order to do that, it needs two values: the **length of text**, and **width of tooltip**. You have to provide the tooltip width, in pixels. You can measure it in Photoshop or any other image edition software. It is the number of pixels between the leftmost pixel of the leftmost character in your in-game string, and the rightmost pixel where you want text displayed.

The length of text is harder to compute. One could wish it is as easy as multiplying the number of characters per the number of pixels per character. Unfortunately, not all characters are born equal - some are wider and some use less pixels. Actually, the width of a character is a client-side property, and depends also on the font (resource pack used). Therefore, if you plan on using centered tooltip headers, **make sure the font used in your item names are included in your server resource pack**, to make sure all players use the same font pack.

MMOItems need to evaluate the length, in pixels, of any string. For that, it needs to know the font size, which is the width of any character. It turns out that, using the default resource pack, the width of most characters is 5, which is why `default_char_size` is set to 5. However, there are a few exceptions, which are indicated in the `char_size` array. Here are a few examples:

- lowercase `f` is only 4px wide
- lowercase `i` is 1px wide, whereas uppercase `I` is 3px
- space character ``happens to be 3px

If you plan on using the default Minecraft font, you don't need to bother about these as we have already measured most of them for you. If you plan on using a different font for your server resource pack, you will have to open an image editing software, and count the pixels of any character that you plan on using inside your item names.

Finally, the `regex` is the regex expression for characters that should be taken into account when counting the width of a given line. If a character is found inside a lore line and does not match this regex, it will simply be ignored. **This is typically used to avoid counting unicode characters used in custom fonts and color codes.** Doing a regex tutorial here would be very much out-of-scope, so please look it up online if you don't know about it. The default value is set to include *lowercase and uppercase roman litterals, commas, +'s and brackets (used when upgrading items) and spaces*.

> **INFO**
>
> This option is subject to change in the future if we find a better way/less confusing way to implement this

Here's what our item looks like so far! We have successfully centered our display name and first lore line.

![image.png](https://docs.phoenixdevt.fr/assets/tt_center_top.FIUUbkbL.png)

### Making the tooltip top larger {#making-the-tooltip-top-larger}

Our tooltip looks pretty good so far, but there might one thing you still want to do. As of right now, you might want to increase the size of the tooltip header. The first thing that you want to do is draw a new texture for your tooltip. Here's the new texture, that will occupy the item name level, as well as the first lore line. Our new texture is now 42px high.

![top.large.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAP8AAAAqCAYAAAEL/L3AAAAACXBIWXMAAAsSAAALEgHS3X78AAAD4UlEQVR42u1da0sUURj2YyRhRLWX2Z3LVmhWpmZhSVJeKEw0r1laiyKa9CEJuktp90AqgsJ+Rt/7Cf2Ngv5D8TTv6onBlqVkZ2fOnmfgYXZ2z+y88z7vs+ecd86eUwOgJkoUfTOxLYFygwbQgP8yoOpU8HmlO1oKVi650RqwmveiNeDBsBOtAa+vetGr4Of3xa+B1yUDM3IVVuq3qZKxboQD7l50zHbAs8uu2Q54Mx2iBKoVkV1YaoFfP5YRqBnaYusAMVYHCYTmAKlejHaANGaNdoDUr5SAyQ54OWm4BKQ7Z7QDpIVltAOkP220A6oJkosQmN4FCCsACokewaeFXMWhrv3tywwStYnCXkHZpI5V+WAZdU4c7mFj0ysAdOky6YBKZUzL+mW6NBd1gPhSuwBYGmUAlAviS+0CQJeciQ4o9TCVVQCrgHgGwONxBkC5IL7ULgB0yRpX6xPuyANAl5RhtT7gZibwHzOBzAAaSn5chqOR/AopXF5Latff1wT3m0ajgORvEcE8ehR5c5XbVzn9zbl9lc+XrVjuf/N5Ud6Dgjbk23U2G2tlhPiT5JN8kk/yST7JJ/kkn+STfJJP8kk+ySf5JJ/kk3yST/JJPskn+SSf5JN8kk/yST7JJ/kkn6hCVGJUEMExnEQMRqCrz9XYVdk2xq4W3g+OXeUId4o/dsEtwSpNH9OhRKuOi/lGTUwTHP+ryqjzg8dBqHOLXVM1QcnH376h+EOCcjL7fqWxdqPlz4Q/pcqIL2Vfaq4YQakyxDrUjyDFT/ETFD/FX27x8+//RFynUqD4Qxa/LrPlEmZB4pLiD1n8nPuNiOsySRR/yOLnvH9EXOdQpPhDFr8uy6QQZkHikuIPWfyc85uI6/zpFD+z/QSz/RQ/s/0Es/0UP7P9BLP9FD/7/AT7/BT/FsTPVR6JuK6YSfGHLH7dlndL+rBqE7B3JOHtTGL/riQa9iRxKJFCcyqFViuFtmwa7W4aHfvS6DyQRleDhd5GC+ePWOg/amGwJYPhtgzGTmQwcTKLqY4s8p1ZzJzJYq7bxnx3Bjf7PB82bvU7uDPo4P6Qg6URF8vjLp5OuHjhd5ekX7qa9/BuxsPH+RzWFnL4MJfD+1kPb6fXP3s15eH5FRdP/HMejbl4OOLgnu/z2wNO4bsXL3hY6M3geo+N2S4b074N105nMenbNNGewahv49CxDAZ8m/uaLJw7bKHnoIWz9Vbh3k7l0jjupNHq33Ozf+9Nvg8a96ZQv3vdN25dElnfV+nt+i2VR/Gz2U+w2U/xU/wExU/xl0380jRlsBFxg8Qlxc9HfYSBkLisFvH/Br8M91HCSN6rAAAAAElFTkSuQmCC)

Make sure you update the resource pack config to account for the height of your new tooltip `top` texture. I had to increase `height` from 21 to 42, and `ascent` from 17 to 18 for a very minor 1px adjustment.

```json
{
    "providers": [
        {
            "type": "bitmap",
            "file": "tooltip_tutorial:gold/top.png",
            "ascent": 18,
            "height": 42,
            "chars": ["\u4070"]
        },
        ...
    ]
}
```

Now use the following syntax for your tooltip config. The `ignore_first` option tells MMOItems to skip the rendering of the `middle` texture for the two first lore lines, which are now *covered* by your larger tooltip `top` texture!

```yml
gold:
  # ...
  ignore_first: 2
```

Here's the final look of our item. Pretty nice!

![](https://docs.phoenixdevt.fr/assets/tt_use_big_top.B-iPN54U.png)

## Binding tooltips to items, modifiers, tiers, types {#binding-tooltips-to-items-modifiers-tiers-types}

Binding a specific tooltip to a specific item is super easy. Either directly input the tooltip ID after clicking the *Tooltip* option in the item edition UI, or use the following syntax. This option has precedence over type- and tier-level tooltips.

```yml
SOME_ITEM:
  # ...
  tooltip: GOLD # Forces the tooltip to GOLD
```

Similarly, you can have modifiers that apply a tooltip (just like they would give any other stat/item option) using the following syntax. This option has the highest precedence, since modifiers are taken into account after the base item data on item generation. Here's an example of a modifier that adds the prefix *Golden* to items while applying tooltip with ID `GOLD`.

```yml
GOLDEN:
  chance: 0.1
  prefix:
    format: '&6Golden'
    priority: 1
  stats:
    # ...
    tooltip: GOLD # Forces the tooltip to GOLD
```

Binding tooltips to item tiers is super easy as well. Here is the default config of the `Rare` item tier. This option has precedence over type-speficic tooltips, but not over item- or modifier-level tooltips.

```yml
RARE:
  name: '&6Rare'
  # ...
  tooltip: GOLD # Sets default tooltips of Rare items to GOLD
```

Binding tooltips to item types is also super easy using the following syntax. Here's the default config file of the `Sword` item type. This option has the lowest precedence.

```yml
SWORD:
  name: Sword
  # ...
  tooltip: GOLD # Sets default tooltip of swords to GOLD
```
