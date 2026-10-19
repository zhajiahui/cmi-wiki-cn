[![](https://wiki.citizensnpcs.co/images/5/5b/Alchemist.png)](https://wiki.citizensnpcs.co/File:Alchemist.png)  
  
**Alchemist**

|  |  |
| --- | --- |
| **Author** | aPunch |
| **Version** | 1.1 |
| **Citizens build** | 2.0 |
| **Other dependencies** | None |
| **Download** | [Link](http://ci.citizensnpcs.co/view/Add-ons/job/Alchemist/) |
| **Description:** Customizable Potion Recipes | |

Alchemist is a Citizens 2.0 character trait that gives NPCs the ability to:

- Craft potions based on pre-defined recipes.
- Charge a fee for their service.

## How to Use

### General Information

Alchemists provide the ability to create custom recipes for potions. You can customize these recipes in the configuration file. A default recipe is provided as an example.

Keep in mind, there is no way to view an alchemist's current recipe ingredients using this plugin. This is intentional, as you, the server admin, should be allowed total freedom to decide how you display recipes. You could show the ingredients using signs, another plugin, or not at all.

### Interaction

Right-clicking the alchemist with the proper ingredients will remove them from your hand and give them to the alchemist. Once the recipe has been completely fulfilled, the alchemist will drop a potion around it's location. If the user walks too far away, the alchemist will stop brewing the potion and any items that were given to it will be lost.

## Commands

To use alchemist commands, you must have an NPC selected and be the owner of that NPC. There are no permission nodes required for commands.

| **Alchemist Commands** | | | | | |
| --- | --- | --- | --- | --- | --- |
| Command | Description |
| /alchemist help | Show the help menu |
| /alchemist recipe | Show the alchemist's current recipe |
| /alchemist recipe [name] | Set an alchemist's current recipe. |

## Permissions

To use alchemists, you only need one permission node. The permission node *alchemist.interact* allows a player to interact with an alchemist.

## Configuration

The configuration file for Alchemists is found in */plugins/Alchemist/config.yml* and is generated automatically when not present.

### Default Configuration

Mouseover each section to view it's description.

```
# Alchemist Configuration
recipes:
 default:
   result:
     effect: fire-resistance
     duration: 60
     amplifier: 1
     splash: false
   ingredients:
     '0':
       name: sugar
       amount: 1
     '1':
       name: glass-bottle
       amount: 1
     '2':
       name: wool
       amount: 1
       data: 6
messages:
 initialization-message: <e>Hello there, <player>. Give me what I need and I will brew you a potion!
 success-message: <e>I have combined the ingredients to concoct a potion of <a><potion><e>.
 cooldown-not-expired: You've already had your turn. Come back later!
cooldown-in-seconds: 60
```

## Valid Effects

- *speed* - Increases movement speed.
- *slow* - Decreases movement speed.
- *fast-digging* - Increases dig speed.
- *slow-digging* - Decreases dig speed.
- *increase-damage* - Increases damage dealt.
- *heal* - Heals player instantly.
- *harm* - Harms player instantly.
- *jump* - Increases jump height.
- *confusion* - Warps vision on player's client.
- *regeneration* - Regenerates health.
- *damage-resistance* - Decreases damage dealt to the player.
- *fire-resistance* - Adds resistance to the effects of fire.
- *water-breathing* - Allows breathing underwater.
- *blindness* - Blinds the player.
- *hunger* - Increases hunger.
- *weakness* - Decreases damage dealt by player.
- *poision* - Deals damage to player over time.

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
