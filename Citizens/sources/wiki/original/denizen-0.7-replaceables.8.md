For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

Replaceable data tags can be used to dynamically put flags and values inside texts and commands.

### Flag Replaceables

| <PLAYER.NAME> | Gets the bukkit Player Name |
| --- | --- |
| <PLAYER.NAME.DISPLAY> | Gets the Player Name with Prefixes and colors, if specified |
| <PLAYER.NAME.PLIST> | Gets the Player Name that is listed in the Player List |

| <PLAYER.LOCATION> | Gets the Player's current location, formatted for dscript. |
| --- | --- |
| <PLAYER.LOCATION.FORMATTED> | Gets a text-friendly formatted version of the Player's current location |
| <PLAYER.LOCATION.STANDING_ON> | Gets the name of the block that the Player is currently standing on |
| <PLAYER.LOCATION.WORLD> | Gets the name of the world the Player is currently in. |
| <PLAYER.LOCATION.WORLD_SPAWN> | Gets the Player's current world's spawn location, formatted for dscript |
| <PLAYER.LOCATION.BED_SPAWN> | Gets the Player's current bed spawn location, formatted for dscript. |

| <PLAYER.HEALTH> | Gets the Player's current health. |
| --- | --- |
| <PLAYER.HEALTH.FORMATTED> | Gets a text-friendly representation of the Player's health, by dividing max-health by current-health. |
| <PLAYER.HEALTH.FORMATTED.#> | Same, except specifies max-health instead of relying on bukkit's p.getMaxHealth(). |
| <PLAYER.HEALTH.PERCENTAGE> | Gets the percentage of the Player's health. |
| <PLAYER.HEALTH.PERCENTAGE.#> | Same, except specifies max-health instead of relying on bukkit's p.getMaxHealth(). |

| <PLAYER.FOOD_LEVEL> | Gets the Player's current food level. |
| --- | --- |
| <PLAYER.FOOD_LEVEL.FORMATTED> | Gets a text-friendly representation of the Player's food level. |
| <PLAYER.FOOD_LEVEL.FORMATTED.#> | Same, except specifies max-food level. |
| <PLAYER.FOOD_LEVEL.PERCENTAGE> | Gets the percentage of the Player's food level. |
| <PLAYER.FOOD_LEVEL.PERCENTAGE.#> | Same, except specifies max-food level. |

| <PLAYER.XP> | Gets the percentage of progress towards the next level. |
| --- | --- |
| <PLAYER.XP.TO_LEVEL> | Gets the number of XP until the next level for a Player. |
| <PLAYER.XP.TOTAL> | Gets the total amount of XP that the Player currently has. |
| <PLAYER.XP.LEVEL> | Gets the Player's current XP Level. |
