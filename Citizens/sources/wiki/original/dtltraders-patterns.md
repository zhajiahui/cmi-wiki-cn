## **NOTICE**

Patterns have not been implemented into vr. 3.0 yet!

## Overview

Every pattern is saved in the *patterns.yml* file located in the plugin's main folder. (plugins/DtlCitizensTrader)  
 You can change the directory in the configuration file.

There are 2 types of patterns:

- *Pricing patterns*  
Sets item prices and pricing tiers.

- *Item patterns*  
Will add certain items to the trader's stock, also has item tiers.

Incoming a third pattern type with 2.6 (long way to it):

- *random patterns*
Those will allow to set maximum items a trader can have showd in stock (like 10 of 20), also set timeouts, "spawn chance", amount and price chances that will be used on each item when it's timeout passed.

All patterns are based on one syntax that is used to build item scripts. Those scripts are used by each pattern type, just each pattern type uses it in another way.

## Item syntax

This sound horrible, I know, but it's best way to explain it in two words :D

Every item within a pattern is build up by some keywords and flags you may use, many options you can't achieve with a basic trader setup are here allowed, but you need to be careful.

### Keywords

**Item setting**

**Keyword**

**Price pattern**

**Item pattern**

**Example**

`ID and data`

`id[:data]`

`Looks for items with the given id and/or data, priority: 130`

`Sets the item id, and when set also the data default: required!`

`wool:14`

`Name`

`n`

`matches the item by the given name, priority: 300`

`Sets the item name, default: nothing`

`n:A Item`

`Item amount`

`a`

`Looks for items with the given amount, priority: 5`

`Sets one or more amounts for an item, default: 1`

`a:1,2,4`

`Durability`

`d`

`Looks for items with the given or higher durability, priority: 45`

`Sets the items durability, default: 0`

`d:22`

`Tier`

`t`

`Matches items only in the given item tier, priority: 25`

`not used`

`t:vip_tier`

`Color`

`c`

`matches by the given color, priority: 5, leather armor only`

`Sets the color for a leather armor item. Uses RGB values separated by ^, leather armor only`

`c:255^210^24`

`Enchants`

`e`

`Checks if the item has the same enchants, priority: 5`

`Sets enchantments for an item, default: none`

`e:smite/3`

`Stored enchants`

`se`

`Checks if the item has the same stored enchants, priority: 5`

`Sets enchantments for a enchanted book item, default: none, enchanted book only`

`se:smite/7`

`Price`

`p`

`Sets the price for each matching item, overriding lower priority matches`

`Sets the price for the given item, default: pattern price`

`p:12.22`

`Multiplier`

`m`

`Sets the multiplier for each matching item, overriding lower priority matches`

`Sets the multiplier for the given item, default: pattern multiplier`

`m:0.9`

`Firework`

`f`

`not used`

`Sets firework data for a firework item, firework only`

`---`

`Global limit`

`gl`

`not used`

`Sets a limit for this item, default: none`

`gl:limit/timeout`

`Player limit`

`pl`

`not used`

`Sets a limit for each player for this item, default: none`

`pl:limit/timeout`

`Slot`

`s`

`Not used`

`Sets the slot for the item, default: first empty`

`s:22`

---

### Flags

**Item flag**

**flag**

**Item pattern**

`Item Lore`

`lore`

`This flag allows you to add lores to your item. It needs always to be set on the end of a item definition and needs to end with :. If used always supply a lore. How it should look like will be shown later.`

`Stack price`

`sp`

`The price calculated for this item, is always applied to the whole stack, not to each item. example:  price = 3$ | amount = 2 | without sp: 2*3$ = 6$ | with sp: 3$, so 1.5$ for each`

`Pattern multiplier`

`pm or !pm`

`Forces to use or to ignore pattern multiplier matches`

---

### Basic syntax

---

#### All patterns

Each patterns starts with a name, that you will use in-game to assign them to your traders. That name may be as long as you wish, just you should only use letters, numbers and use this character `**_**` instead of a whitespace.

Also each pattern from up now needs to have a type specified, so the pattern loader knows how to read it.
So far there are only 2 types, **price**, and **item**. I think it's obvious.

Beside the type node all patterns got 3 additional nodes: "all", "sell", "buy". These nodes applies entries either to both sell and buy stocks, or just to one of them.

Empty pattern example:

```` ```
 pattern_name:
   type: pattern_type
   all:
   - ...
   sell:
   - ...
   buy:
   - ...
``` ````

---

Each entry in a pattern has the same syntax that looks like this and it should be always done like this:

`id[:data] [keywords...] [flags...] [n:...] [lore:]`

As in the example best way is to set after the ID all keywords then flags.

There are two exceptions in this rule.

The **name** keyword is best used on the end because you don't need to worry about that it will interpret any other keyword or flag as a item name part. But if you want you don't need to set it on the end just **remember to always add two spaces** after the item name. *(the example shows that with the **lore** flag)*

The **lore** flag needs always to be on the end, it's a **YAML** syntax requirement, that will allow us to add lores easily to the item.

It's really simple to add items to a pattern, just need type their name or ID, and data if needed, all other values got their default values or behavior, so you don't need to be afraid that you may forget to set something for an item and it will break the pattern.

**Examples:**

`wool:14` - will add to the traders stock a red wool block.

`wool s:3 n:My white wool` - will add to the traders stock a wool block, at slot 3 named **My white wool**.

`276 d:80% e:smite/2 p:1000` - will add to the traders stock a diamond sword, with smite level 2, price 1000 and durability 80%.

#### Price patterns

Generally a price pattern allows you to set prices and multipliers for items a trader has in stock. Each item entry in a price pattern is considered as a matching pattern, this is going to be used to match items the trader has in stock and set their prices and multipliers.

Each match may have another priority, with the rule: the greater priority wins.

Easies and most common used are these patterns as a global price file. So you setup all prices for each item in-game, and just add this pattern to each Trader. Now the only thing you need to do is to add items to his stock and thats it. No more price setting :P Prices are going to be set automatically for each player.

Because there is also the possibility to create **tiers** in these patterns, you may create vip groups that have lower prices (easily done by setting just the multiplier for a tier). To apply prices from a tier, the player needs to have a permission to **"use"** that tier.

Lets say we go a price pattern for all items in-game (going to name this "global-prices" from up now), and we want to set the multiplier to **0.9** for all of them except logs:

```` ```
 - ...
 // because we just set the multiplier, it will be set for all items in this pattern, priority match is equal to 0
 - m:0.9
 // here we add additional information to match items with id 17 (logs), and because this match is higher (equals 130), it will override the 0.9 global multiplier for logs
 - 17 m:1.0
``` ````

Another price pattern example:

```` ```
 price_pattern:
   type: price
   all:
   - m:1.0
   - dirt p:0.55
   - wool p:4.42 
   sell:
   - m:1.0
   - log p:3.33
   - wool m:1.1
   buy:
   - wool m:0.9
``` ````

This pattern will set buy and sell prices for dirt and wool blocks, and just sell price for logs. We also told the pattern to use for all items a multiplier of **1.0**, except for wool, that got a multiplier while selling (to a player) **1.1**, and selling to a trader is like **0.9** of the base price.

Only this allows you for much more possibilities than the old system :P

##### Tiers

##### Tier tags (whats the difference?)

##### Advanced matching

##### Matching informations

What tags and item information can be matched can be found in the table on the beginning, there is also information provided, how does the priority grows when a specific keyword is used.

As because this is not the release version there are going to be many changes to the matching system. Any ideas are always welcome :)

#### Item patterns

Soon.

##### Lores

Soon :)

## Navigation

| **DtlTraders** | |
| --- | --- |
| Configuration | [Commands](http://wiki.citizensnpcs.com/DtlTraders/Commands) | [Permissions](http://wiki.citizensnpcs.com/DtlTraders/permissions) |
| Usage | [Patterns](http://wiki.citizensnpcs.com/DtlTraders/patterns) |
| Types |  |
