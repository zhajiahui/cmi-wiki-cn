Known Compatibility issues with Citizens 2.0.4

- Citizens requires CraftBukkit 1.4.5+
- Setting pvp=false may break left clicking on NPCs as this is treated as attacking the NPC and the event will not fire.
- The spawning of hostile-mob-type NPCs may be prevented under the following circumstances:
  - There is a plugin preventing spawns with a HIGHEST priority, Plugin List:
    - Essentials WILL prevent npc spawn
    - WorldGuard WILL NOT prevent npc spawn
    - MultiVerse WILL NOT prevent npc spawn

- Authme may throw console errors trying to hook into citizens2.
- PvPToggle may throw console errors trying to hook into citizens2.
- TeleportSuite may throw console errors looking for NPCs.
- HomeSpawnPlus may prevent right-click selection with a stick.
- APIPlus may prevent all right-clicking
- PopulationDensity/GriefPrevention may interfere with the spawning of NPCs on server start and may duplicate them on /reload.
- [Heroes](http://dev.bukkit.org/server-mods/heroes/) has known issues with player-type NPCs. Please do not send them tickets, we are trying to work with Kainzo to fix this.
- CityScape uses the /npc command. Use /npc2 to run citizens2 commands if both plugins are installed.

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
