Editors are used to further edit NPCs in easy ways. These are things considered too complex to require just commands to edit. In all editors, you must type the associated command once to enter the editor, and again to exit it. **You can only be in one editor at a time.**

## Text Editor

Command: /npc text
  
  
Editing a NPC's text is simple. Follow the in-game directions to add, edit, and remove text from NPCs. A NPC being a "random-talker" means that it will repeat random phrases from its list of text. If "random" is false, it will loop through the text linearly. Changing its close-talker setting by typing "close" will toggle whether a NPC talks when a player comes within 5 blocks. If close is false, the NPC will only talk when it is clicked with the configurable talk-item. If close is true, it will only talk when a player comes near.

**Note that players need the citizens.npc.talk permission to hear NPCs!**

Important note: Type 'exit' in chat to close the editor!

Also see [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")

## Waypoint Editor

Command: /npc path
  
  
  
See the [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints") page for more information.

## Equipment Editor

Command: /npc equip
  
  
  
Equipment is things like armor, held-items, and other visible features on NPCs. Only some NPC types can have their equipment edited.

### Generic

With the new mob equipment updating in 1.4.5, any mobs not listed here will default to the Human equipping style. Note that the equipment may not display properly on all mobs as some do not support it.

### Humans (regular NPCs)

Human NPCs can have their armor and held item modified. To give armor to a NPC, right-click one with armor in your hand. The armor is placed on the NPC's body. Any item or armor that was previously on a NPC will be removed and dropped to the ground. To place armor in a NPC's hand, *crouch* and right-click. To clear all items, right-click the NPC with no items in your hand.

### Endermen

Enderman NPCs can have their carried material modified. The only valid materials that an enderman can hold are blocks - most items do not appear on the client. Note that certain "utility" blocks such as sign posts, silverfish blocks, etc. *do not* appear on the client either. Click with no items in your hand to remove blocks from the enderman NPC.

### Sheep

Sheep NPCs can have their wool color and sheared status modified. To shear, right-click with shears like your normally would. To un-shear a sheep NPC, click it with the shears again. To change the wool color, click the sheep NPC with dye. Clicking with anything but dye in your hand will turn the sheep NPC white and drop the dye on the ground.

### Pigs

Pig NPCs can have saddles added and removed from them. Simply right-click the pig NPC with a saddle in hand. Clicking with any other item in your hand will remove the saddle from the pig NPC.

### Clientside Issues

There are known clientside issues with some equipment editors. If you are experiencing an issue, it is likely clientside. Try relogging and if necessary restarting your server. If you still think the issue is present, report an issue [here](http://issues.citizensnpcs.net).

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · Editors  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
