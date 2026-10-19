# Banner Layers

![image](https://wiki.mythiccraft.io/_media/mythicmobs/uploads/204528492902aa041447fe90880071d8/image.png)

To make complex banner items in MythicMobs, you can use the following syntax.
There is no hard limit placed by MythicMobs on the number of banner layers you can use, and you can go past the vanilla maximum of 6 layers set by Minecraft using this.
However, going past 6 layers may cause unusual behavior and/or lag.

Banner layers are also applicable to shields.

## Syntax {#syntax}

```yml
Banner:
  Id: <banner/shield>
  #For Banners, the base color is set by the item ID
  BannerLayers:
  - <color> <pattern>
  - <color> <pattern>
```

## Patterns {#patterns}

A list of available [patterns](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/banner/PatternType.html) can be found on the spigot javadocs.

## Examples {#examples}

```yml
SkeletonKingBannerShield:
  Id: shield
  Display: <dark_red>Skeleton King's Banner</dark_red>
  BannerLayers:
  - RED BASE
  - WHITE CURLY_BORDER
  - WHITE STRIPE_CENTER
  - BLACK STRIPE_BOTTOM
  - WHITE CREEPER
  - YELLOW STRIPE_TOP
  - BLACK TRIANGLES_TOP
```

```yml
SkeletonKingBanner:
  Id: orange_banner
  Display: <dark_red>Skeleton King's Banner</dark_red>
  BannerLayers:
  - RED BASE
  - WHITE CURLY_BORDER
  - WHITE STRIPE_CENTER
  - BLACK STRIPE_BOTTOM
  - WHITE CREEPER
  - YELLOW STRIPE_TOP
  - BLACK TRIANGLES_TOP
```
