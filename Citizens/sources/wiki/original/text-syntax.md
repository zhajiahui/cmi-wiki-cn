Configuration syntax in Citizens is simple. Nodes within arrow brackets -- `<>` -- will be parsed and replaced if possible. Below are the available nodes that you can use.

## Chat Colors

Use the Chat Color characters the same as any other plugin. For example, `&a` would give you green.

**Color Reference**
  
0 -- BLACK
  
1 -- DARK BLUE
  
2 -- DARK GREEN
  
3 -- CYAN
  
4 -- DARK RED
  
5 -- PURPLE
  
6 -- GOLD
  
7 -- LIGHT GRAY
  
8 -- GRAY
  
9 -- BLUE
  
a -- GREEN
  
b -- AQUA
  
c -- ROSE RED
  
d -- LIGHT PURPLE
  
e -- YELLOW
  
f -- WHITE

**Format Reference**
  
k -- Obfuscated
  
l -- Bold
  
m -- Strikethrough
  
n -- Underline
  
o -- Italic
  
r -- Reset

[Alternate color/format reference page](https://www.digminecraft.com/lists/color_list_pc.php)

You can also use hexadecimal colors in Minecraft 1.16+, using Spigot's syntax - `&x&f&f&0&0&e&e` or Essentials' syntax - `&#ff00ee` (both examples produce the same pink/magenta color).

You can also use [MiniMessage](https://docs.adventure.kyori.net/minimessage/format.html).

## Special

You can use `<br>` to create a newline in the middle of a text line.

## Other

There are also other nodes that you can use in configuration files. Some of these do not apply to certain configuration settings, so use with care. More will be added in the future as the need arises.

### NPC Nodes

`<npc>` -- NPC's name
  
`<id>` -- NPC's ID
  
`<owner>` -- NPC's owner

### Player Nodes

`<player>` -- Player's name
  
`<world>` -- Player's world
  
`<nearest_player>` -- Name of the player closest to the NPC

### Extra Nodes

`<random_player>` -- Random online player name
  
`<random_npc>` -- Random NPC name
  
`<random_npc_id>` -- Random NPC ID

## PlaceholderAPI

If you have [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) installed on your server, you can use PAPI placeholders on NPCs and use specific Citizens PAPI placeholders anywhere that supports PAPI.

### External Placeholders on NPCs

You can use any PAPI Placeholders the same as you would use them elsewhere in NPC text or commands, and non-player placeholders in NPC names/holograms/etc. [See the FAQ for more details on the non-player limit](https://wiki.citizensnpcs.co/Frequently_Asked_Questions#My_PlaceholderAPI_Placeholder_Works_In_Chat.2C_But_Not_On_An_NPC).

### Citizens Placeholders

`%citizens_selected_npc_name%` -- the name of the NPC selected by the player.
  
`%citizens_selected_npc_id%` -- the ID of the NPC selected by the player.

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · Text Syntax  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
