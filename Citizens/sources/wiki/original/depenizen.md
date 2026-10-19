For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

# Depenizen: Dependencies for Denizen!

Welcome to the Depenizen Project! What is Depenizen all about?

Depenizen is a simple plugin that does exactly what its name implies: adds external plugin dependencies to Denizen.

Head on over to our [FAQ page](https://wiki.citizensnpcs.co/Depenizen/Frequently_Asked_Questions "Depenizen/Frequently Asked Questions") for more information!

[Depenizen Github](https://github.com/DenizenScript/Depenizen)

[Development builds download](http://ci.citizensnpcs.co/view/All/job/Depenizen/)

## Depenizen V0.2

If you used 0.1, you might notice that some tags were broken when updating to the latest builds. This was intentional, and mostly unavoidable in terms of the new Denizen 0.9 system, which is geared toward more object oriented systems. For example, previously in Denizen, using **<player>** would return the player's name. Now, it will return a dPlayer, represented by "**p@**", followed by the player's name. That being said, a tag such as **<player.faction>** will no longer return the faction name. To do that, you must now use **<player.faction.name>**.

Other tags, such as **<player.town.ismayor>**, which would return whether or not the player is the mayor of his/her town, make no sense in this system. Instead, you should use **- if <player.town.mayor> == <player>**

...

[List Of Depenizen Tags](https://wiki.citizensnpcs.co/Depenizen/Tag-List "Depenizen/Tag-List") /// [List of Depenizen Commands](https://wiki.citizensnpcs.co/Depenizen/Command-List "Depenizen/Command-List") /// [List of Depenizen's Supported Plugins](https://wiki.citizensnpcs.co/Depenizen/Supported-Plugins "Depenizen/Supported-Plugins")
