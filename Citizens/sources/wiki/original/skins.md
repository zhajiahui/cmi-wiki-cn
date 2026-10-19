## NPC Skins

Custom NPC skins are something that many server admins have asked for ever since Citizens was first released. In recent Minecraft versions it has become possible to control an NPC's skin via the new player packet system. By default an NPC will have the default Steve or Alex skin. You can set an NPC's skin by using the `/npc skin [NAME]` command. For example, `/npc skin mcmonkey4eva`

## What's the best way to set a custom skin?

If you want to set a custom skin (one that isn't already on a player), use `/npc skin --url [image]`. The "[image]" part must be filled with a valid public image direct link. "public" means it's on a web host (you can just use Discord or [imgur](https://imgur.com) or whatever else) and "direct" means it's a link that ends with ".png" containing the raw image (not a link to an album or similar. Imgur by default gives you an album link, and you have to right click -> copy image URL).

For example: `/npc skin --url https://gamepedia.cursecdn.com/minecraft_gamepedia/3/37/Steve_skin.png`

Note that the `--url` feature is internally backed by [Mineskin](https://mineskin.org/), and in some cases it may be helpful to use their website directly.

If you want a **slim model** (aka "Alex model") (3-pixel wide arms instead of 4) from a URL, it might be helpful to directly upload the skin image to [Mineskin](https://mineskin.org/) and use the model choice option on the page.

## Other Options

You can use `/npc skin [NAME] -l` (a lowercase L) to always use the latest skin for the player (updating if the player changes their skin). If this is not set, the current skin (at time of using the command) will be retained.

You can use `/npc skin -t [uuid] [data] [signature]` from the console (or any large-input command sender) to set a very specific full skin blob from Mojang. If you don't know exactly what that is, just don't use it. It's a developer tool.

Note that some sites like <https://mineskin.org/> let you generate values for the `-t` option.

## Mirroring A Player's Current Skin

If you want every player to see their own current skin applied to the NPC, install [Denizen](https://denizenscript.com/) and then use the command `/npc mirrorskin`. You can also have the name mirrored via `/npc mirrorname`, or mirror equipped items with `/npc mirrorequip`.

## For API Users

If you use the Java Citizens API, you can control skins on NPCs via `npc.getOrAddTrait(SkinTrait.class)` and calling a method like `setSkinName`. Refer to the [SkinTrait JavaDoc](https://jd.citizensnpcs.co/net/citizensnpcs/trait/SkinTrait.html) for more information.

**Note:** you can't (and shouldn't) set from image or URL directly via Java API. Instead, upload your image to [Mineskin](https://mineskin.org/) and save the texture+signature data (store them in a string or a config file), and set that with `setSkinPersistent(uniqueId, signature, texture)`.

**Also note:** if you're creating a new NPC and giving it a skin, it's best to give it a skin before you call `spawn()`, as the first spawn will trigger a default skin load, which can be slow or even overwrite your custom skin. If you have set a skin prior to the spawn call, it will not try to load a default one.

## Common Issues

Many issues can cause the skin system to fail. If you are experiencing issues, please ensure the following:

- You are running a fully up to date Spigot server acquired from <https://www.spigotmc.org/wiki/buildtools/> running a supported recent version of Minecraft. (Paper also generally works). You can use `/version` to check the version of your server.
- You are running the latest dev version of Citizens2 from <http://ci.citizensnpcs.co/job/Citizens2/> Please verify the specific build number (NOT the file version name) You can use `/version citizens` to check this build number.
- You have a dedicated server (not a shared hosting service!)
- You own your server's IP entirely (no other ports on the server are used by other minecraft servers! (Unless they're your own servers as well.))
- You are running your server in ONLINE MODE (offline mode servers won't work!) (note that if you're on a Bungee network, you must enable "bungeecord: true" to make sure the game knows it can still connect to Mojang's servers to download skins).
- There are no errors ANYWHERE in your current log file (`logs/latest.log`). Any errors, even if seemingly unrelated, must be fixed!
- You are not being rate limited by Mojang. This can occur if you've loaded too many skins recently (from player head skull items, or from the npc skin command). This can be cured by waiting a while without loading more skins in, to allow Mojang to drop the rate limit.
- Mojang's servers are online. Check that the [Mojang Status Page](https://status.mojang.com/check) is showing greens. If skins usually work but suddenly don't for a while, it might just be the official servers are down.

If you have confirmed you meet all of these requirements, but are still having trouble, feel free to post an issue to [GitHub](https://github.com/CitizensDev/Citizens2/issues) or ask on [Discord](https://discord.gg/Q6pZGSR) with as much information as possible (At the very least, pastebin your current log file and Citizens saves.yml file)

Please **DO NOT** lie about any of these when requesting help. They are not to "catch you" or anything like that: these are listed because these requirements **WILL** cause issues if not met, and if you say you meet them but don't actually, you'll just be wasting everyone's time (including your own!).

## Technical Info

If you're interested in how the skin system works internally (texture/signature system), you can view an explanation of the skin-blob system [here on the Denizen documentation site](https://one.denizenscript.com/denizen/lngs/player%20entity%20skins).

## Additional Resources

- Here's a Denizen script to save/load skins on NPCs for if you reuse skins frequently: [NPC Skin Save/Load](https://forum.denizenscript.com/resources/npc-skin-save-load.8/)
- Mineskin has a gallery of skins you can look through: [Mineskin Gallery](https://mineskin.org/gallery)
- Here are some more skin list sites: [MinecraftSkins.com](https://www.minecraftskins.com/), [MinecraftSkins.net](https://www.minecraftskins.net/), [PlanetMinecraft Skins](https://www.planetminecraft.com/skins/)
- Minecraft Wiki page about skins: [Minecraft Wiki: Skins](https://minecraft.fandom.com/wiki/Skin)
- Here's a Denizen script to edit player skins as easily as you can edit NPC skins: [Player Skin Command](https://forum.denizenscript.com/resources/player-skin-command.54/)

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
