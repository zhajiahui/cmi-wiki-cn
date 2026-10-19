[![](https://wiki.citizensnpcs.co/images/b/be/Blacksmith.png)](https://wiki.citizensnpcs.co/File:Blacksmith.png)  
  
**Blacksmith**

|  |  |
| --- | --- |
| **Author** | aPunch |
| **Version** | ??? |
| **Citizens build** | 2.0.x |
| **Other dependencies** | Vault, and an economy system |
| **Download** | [Link](http://ci.citizensnpcs.co/view/Add-ons/job/Blacksmith/) |
| **Description:** Heavily Customizable Tool and Armor Reforging | |

Blacksmith is a Citizens 2.0 character trait that gives Citizens NPCs the ability to:

- Repair weapons, tools, and armor for a fee.

Most up-to-date source code available here: <https://github.com/mcmonkey4eva/Blacksmith>

## Updates

v1.13 10/12/2018

- HurricanKai is missing, so mcmonkey has performed minimalist updates, now available here <https://github.com/mcmonkey4eva/Blacksmith>

??? ?/?/2017

- Now maintained by HurricanKai, compat with minecraft 1.12 as of this message. See github for commit logs. <https://github.com/HurricanKai/Blacksmith>

??? 2/17/2015

- update to latest everything.

v1.3 8/5/2013

- Fix blacksmith not returning items.

v1.2 8/15/2012

- Added price-per-durability-point option on a per-item basis.
- dded session timeout if player asks for price and does not reforge item.
- Fixed Random-enchant algorithm.

v1.1 8/8/2012

- Compatible with 1.3.1 builds of C2

## How to Use

## Installation

- Install Citizens 2
- Place Blacksmith.jar file in /plugins directory.
- Start Server
- Create NPC and give the Blacksmith trait.

```
/npc create Smithy --trait blacksmith 
```

or

```
/npc create Smithy
/trait blacksmith 
```

### General Information

Blacksmiths have a variety of settings that can be per-NPC or global. The settings under "defaults" in the configuration file are the default settings that a blacksmith will be given when it is created. You can override these settings by using the commands from the Commands section below. You can even configure which items a blacksmith is able to reforge in-game using commands. By default, a blacksmith is able to reforge all items.

### Interaction

Interacting with a blacksmith is simple:

- Right click the NPC with a tool or armor in your hand. It will tell you the price that it costs to reforge it.
- Right click again within 10 seconds and the blacksmith will begin reforging the item.
  - Depending on the configuration, the reforging has a chance to enchant or damage an item.

## Prices

Prices are determined by the damage of an item, the number and type of enchantments, and the prices defined in the configuration file. Basically, the formula for determining the price of a reforge is *basePrice + durabilityRemaining + enchantments*.

### Base Price

The default base price for a reforge is the *base-prices.default* value in the configuration file. To add new base prices for each individual item, add the item to the config file under *base-prices*

### Durability

Durability is the amount of damage that an item has taken. Generally, the more damaged an item is, the cheaper it will be to reforge. Trying to reforge an item with no damage will be significantly more expensive. The price per durability point is *price-per-durability-point.default* in the configuration. Per-item values may be set by adding to this section.

These are the items names to use with custom base and per-durability-point prices.

**Valid Items**

wood-pickaxe
  
wood-spade
  
wood-hoe
  
wood-sword
  
wood-axe
  
stone-pickaxe
  
stone-spade
  
stone-hoe
  
stone-sword
  
stone-axe
  
gold-pickaxe
  
gold-spade
  
gold-hoe
  
gold-sword
  
gold-axe
  
iron-pickaxe
  
iron-spade
  
iron-hoe
  
iron-sword
  
iron-axe
  
diamond-pickaxe
  
diamond-spade
  
diamond-hoe
  
diamond-axe
  
bow
  
flint-and-steel
  
fishing-rod
  
shears
  
leather-helmet
  
leather-chestplate
  
leather-leggings
  
leather-boots
  
chainmail-helmet
  
chainmail-chestplate
  
chainmail-leggings
  
chainmail-boots
  
gold-helmet
  
gold-chestplate
  
gold-leggings
  
gold-boots
  
iron-helmet
  
iron-chestplate
  
iron-leggings
  
iron-boots
  
diamond-helmet
  
diamond-chestplate
  
diamond-leggings

diamond-boots

Example:

```
base-prices:
  default: 10
  diamond-sword: 45
price-per-durability-point:
  default: 1
  diamond-sword: 3
```

### Enchantments

The price of reforging an item with enchantments is more expensive than one without any. For each enchantment, an amount is added to the total price based on the "enchantment-modifier" and the level of the enchantment. Enchantment modifiers can be configured in the configuration file by adding the enchantment name and a value within the *enchantment-modifiers* section. The default modifier, *enchantment-modifiers.default*, is used if the enchantment name is not found. Here are valid, case-sensitive names for enchantment modifiers:

- *arrow-damage* - Provides extra damage when shooting arrows from bows
- *arrow-fire* - Sets entities on fire when hit by arrows shot from a bow
- *arrow-infinite* - Provides infinite arrows when shooting a bow
- *arrow-knockback* - Provides a knockback when an entity is hit by an arrow from a bow
- *damage-all* - Increases damage against all targets
- *damage-arthropods* - Increases damage against arthropod targets
- *damage-undead* - Increases damage against undead targets
- *dig-speed* - Increases the rate at which you mine/dig
- *durability* - Decreases the rate at which a tool looses durability
- *fire-aspect* - When attacking a target, has a chance to set them on fire
- *knockback* - All damage to other targets will knock them back when hit
- *loot-bonus-blocks* - Provides a chance of gaining extra loot when destroying blocks
- *loot-bonus-mobs* - Provides a chance of gaining extra loot when killing monsters
- *oxygen* - Decreases the rate of air loss whilst underwater
- *protection-environmental* - Provides protection against environmental damage
- *protection-explosions* - Provides protection against explosive damage
- *protection-fall* - Provides protection against fall damage
- *protection-fire* - Provides protection against fire damage
- *protection-projectile* - Provides protection against projectile damage
- *silk-touch* - Allows blocks to drop themselves instead of fragments (for example, stone instead of cobblestone)
- *water-worker* - Increases the speed at which a player may mine underwater

## Permissions

If you want a player to be able to use a blacksmith, give them the

- *blacksmith.reforge* permission node.

## Configuration

The configuration file for Blacksmiths is found in */plugins/Blacksmith/config.yml* and is generated automatically when not present.

### Default Configuration

The blacksmith config.yml contains the default settings for **new** blacksmiths. All of these options can be changed on existing blacksmiths in the Citizens/saves.yml.
Mouseover each section to view it's description. All settings under *defaults* can be overriden by individual blacksmiths in the Citizens 2 saves.yml.

```
# Blacksmith Configuration
base-prices:
 default: 10
price-per-durability-point:
 default: 1
defaults:
 messages:
   busy-with-player: <c>I'm busy at the moment. Come back later!
   busy-with-reforge: <c>I'm working on it. Be patient!
   cooldown-not-expired: <c>You've already had your chance! Give me a break!
   cost: <e>It will cost <a><price> <e>to reforge that <a><item><e>! Click again to reforge!
   fail-reforge: <c>Whoops! Didn't mean to do that! Maybe next time?
   insufficient-funds: <c>You don't have enough money to reforge that item!
   invalid-item: <c>I'm sorry, but I don't know how to reforge that!
   start-reforge: <e>Ok, let's see what I can do...
   successful-reforge: <a>There you go! All better!
 drop-item: true
 percent-chance-to-fail-reforge: 10
 percent-chance-for-extra-enchantments: 5
 maximum-enchantments: 3
 delays-in-seconds:
   maximum: 30
   minimum: 5
   reforge-cooldown: 60
enchantment-modifiers:
 default: 5
```

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
