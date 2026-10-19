[[File:{{{PICTURE}}}]]  
  
**CitiTraders**

|  |  |
| --- | --- |
| **Author** | tehbeard, tenowg |
| **Version** | RC-5 |
| **Citizens build** | 2.0 |
| **Other dependencies** | Citizens 2, Vault, a permissions system and an economy system. |
| **Download** | [Link](http://thedemgel.com:8080/jenkins/job/CitiTraders/Recommended/artifact/target/CitiTrader-RC-5.jar) |
| **Description:** Cititraders are NPCs that support interface-based trading.  **Issues**: [JIRA Issues](http://thedemgel.com:8080/jira/browse/CITITRADER) | |

1-21-2013 Cititraders is currently out of date, please see [DtlTraders](https://wiki.citizensnpcs.co/DtlTraders "DtlTraders")

# RELEASE CANDIDATE

CitiTraders is in RC, which means that while I feel that it is close to Release, it not perfect, if you see any issues, please use the issue page to let me know, but otherwise I feel that it is ALMOST bug free.
You can download the dev builds from here: [Jenkins Dev Builds](http://thedemgel.com:8080/jenkins/job/CitiTraders/lastSuccessfulBuild/artifact/target/CitiTrader-RC-5.jar)

# CitiTraders

CitiTraders is a set of Citizens 2.0 traits that gives NPCs the ability to:

- Buy and sell items for pre-set prices.
- Maintain an inventory.
- Work with Economy plugins to use bank accounts, owner accounts, or a per-npc account.

You can visit me on irc.esper.net in channel [#cititrader](irc://cititrader@irc.esper.net) to ask questions, or make suggestions, or just to talk

Load video

YouTube

YouTube might collect personal data. [Privacy Policy](https://www.youtube.com/howyoutubeworks/user-settings/privacy/)

Continue
Dismiss

## Installation

- Ensure you have Citizens 2, Vault, and an Economy plugin installed.
- Download the .jar from the link at the top of the page and place it in your /plugins folder.
- CitiTraders requires no configuration by itself. However it requires that you have Vault, an economy plugin that can be accessed via Vault and

## Commands

For a full list of commands visit by Bukkit page till I can update this Wiki

[[BUKKIT PAGE](http://dev.bukkit.org/server-mods/cititraders/)]

## Permissions

[Permissions](https://wiki.citizensnpcs.co/Cititrader/Permissions "Cititrader/Permissions")

## Creating a new npc as a trader

:   **/trader create [NAME] -type [TYPE]**

[NAME] - Name of the NPC to create
[TYPE] - type of NPC to create, (defaults to PLAYER if omitted)

## Adding trader to an existing NPC

To add trader functionality to existing NPCs use:

:   **`/trait wallet`**

and

:   **`/trait stockroom`**

## Buying and Selling

(If at any time you get stuck and a trader is not responding, close any windows and type /trader cancel)

### Accessing the storeroom of a trader

1. Get a book
2. Hold the book
3. Right click your trader while holding the book
4. Place items into traders inventory

### Setting Buy/Sell prices

:   **`/trader sellprice <amount>`**

and

:   **`/trader buyprice <amount>`**

after either of these command, right click the trader with the item in hand, this will set that items price with **this** trader. Prices are not global.

### Buy from a Trader

To purchase goods from a trader you need to **Right Click** a trader. This will open a trade (inventory) window that lists all the different types of items the trader has on hand.
At this time you need to select the item you wish to purchase, **Left Click** on the item you wish to purchase, this will take you to the purchase window, here stacks of items will be made available, but only up to what the NPC has forsale. At this point you can **Right Click** to see the price of the stack, and **Left Click** to purchase the stack.

At any time you can click the **Arrow** to return to the item select screen.

### Selling to a Trader

To sell to a trader first **Left Click** the trader, an inventory window will open, drag any item you want to sell to the trader to his window. Close the window. The prices will be caluculated and deposited into your account, any items he doesn't take will be dropped to the group on close.
(This is going to be changed, Items the trader takes will be listed, and consumed on drop)

## Wallets

To set a wallet you:

:   **`/trader setwallet <admin|private|bank <player>|owner|town_bank>`**

### Admin

Setting a Wallet to admin will create an **ADMIN** shop, items will not be removed from the shop on sale, and money will be removed from players bank, but not deposited anywhere.

:   **`/trader setwallet admin`**

### Private

The NPC will hold any money that he makes, and you can withdraw the money later.

:   **`/trader setwallet private`**

### Bank

The NPC will use the bank account, this bank must be owned by the player that owns the NPC.

:   **`/trader setwallet bank <accountname>`**

### Owner

The NPC will use the Economy account of the Owner of the NPC

:   **`/trader setwallet owner`**

### Town Bank

The NPC will use the bank account of a town (Using Towny Plugin). The Owner of the NPC that tries to assign this value must be Mayor or Assistant of the town.

:   **`/trader setwallet town_bank`**

# TODO

- Update this wiki

### Discounts

There will be group/player based discounts, they will be percentage based.

### Sales Display

Will be changing the way sales are displayed and handled, NPCs will list what they are buying in the inventory window, and players will drop and drop the item to the inventory, and the item will be sold immediately. (This change will trigger a release phase)

### Manager/Assistants

Add Managers and Assistants to Shops, Managers and Assistants will be able stock stores, and set prices. Managers will have access to private bank, will look at adding additional banks later. They will not be able to link traders, link chests, or remove/fire NPCs, that will remain available for the owner of the Trader. This will allow for Server Admin to setup traders, and assign Manager Permissions to Players to operate a store.

### Rewrite Sell To Player

More efficient and will allow for buystack
