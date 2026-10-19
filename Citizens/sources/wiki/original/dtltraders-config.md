To be sure that everyone of you will understand the configuration file I have decided to explain each config option here, I will try to give you examples how it will affect the way you can use this plugin, and how helpful it can be if your using more advanced features.

## Default config file

```
debug: critical
#locale settings
locale:
  #the choosen localization to load
  load: en
  #should the locale updated autmaticaly, (not implemented)
  auto-update: false
#logging settings
logging:
  #should transactions be logged? (false/FILE/SQL/WEB) , (not used at this moment)
  log: false
  #the foramt how transactions should be logged to FILE, (not used at this moment)
  log-format: ''
#statistics
statistics: 
  #enable or disable statistics (not implemented)
  enabled: false
  #metrics should be enabled? (not implemented)
  metrics: false
#trader types related settings
trader:
  #sets if left clicking the Trader should damage him, if set to false the trader wont be damaged and the click will be handled as ManagerMode toogling
  #when the player meets the requirements (permissions, and right-click = false)
  #it this setting is set to true, manager modes is toggled only when sneaking 
  allow-damage: false
  #item used to toggle between modes (air counts for anything)
  #transaction related settings
  transaction:
    #sets if buying and selling should be done after clicking on a item twice in a row
    double-click: false
  #manager mode related settings
  managing:
    #the starting stock when opening a trader (buy/sell)
    start-stock: sell
    #right click toggling (instead of left click, which is default from 3.0+) 
    #Attention: When PvP is disabled in the world, and the NPC is Player-Type, left click may not work!
    #if r.click toggling is enabled the item needs to be other than AIR. If not set to an item "stick" item will be used.
    right-click: false
    item: 'air'
    #special blocks used when setting prices and limits, format => 'item_id value'
    special-blocks:
    - dirt 0.01
    - wood 0.1
    - log 10
    - cobblestone 100
    - stone 10000
  #stock related settings
  stock:
    #default starting stock (if this stock is set and not empty!, this does not apply for player traders)
    start-stock: 'sell'
    #default stock size in rows, min 1, max 6 (applied on creation)
    size: 6
    #default stock name format, how should be the traders stock named by default, {npc} tag for npc name
    format: '{npc}^r''s shop'
  #wallet related settings
  wallet:
    #default wallet type for traders (if set to infinite player traders will use "owner" type instead)
    type: 'infinite'
    #initial wallet money on creation (does not apply for player traders)
    money: 0.0
  #pattern related settings
  pattern:
    #default patterns applied to each market and server trader uppon creation (array setting)
    defaults: []
    #the file where patterns are saved
    file: 'patterns.yml'
  #book item related settings
  books:
    #the file where book datas are stored
    file: 'books.yml'
    #how should be books stored? (file)
    store: 'file'
  #player trader related settings
  player:
    #limits of player traders per player
    limit: 1
    #default stock size for player traders, if set overrides the stock.size setting
    size: 2
    #default stock name format, how should be the traders stock named by default, {npc} tag for npc name, and {player} for the traders owner
    #if set overrides the stock.format setting
    format: '{npc}^r''s shop, {player}''s company'
  #ui related settings
  ui:
    #item that will "link" to sell stock
    sell: wool:1
    #item that will "link" to buy stock
    buy: wool:2
    #item that will "link" back to a basic stock
    back: wool:14
    #item that will "link" to price managing
    price: wool:15
    #item that will "link" to limit managing
    limit: wool:3
    #item that will "unlock" the stock for eiding
    lock: wool:4
    #item that will "lock" the stock (saving all changes)
    unlock: wool:5
#denizen support related settings
denizen: []
```

## Debug

Plugins sometimes got a debug logger, this feature allows you and me easier bug tracking, if a bug shows up, changing this node to a lower priority value, will show more information about the plugin actions and behavior. The dtlTraders debugger got **six** logging levels, **critical**, **high**, **normal**, **low**, **info**, **none**.

Setting the level to **none** will totally mute the logger, so no error will be shown when anything goes wrong (unless its really serious).

The **critical** level setting shows only errors that totally break the plugin actions, so they are really rare and should be reported to the plugin dev.

The **high** level setting show errors that disturbed an action the plugin was performing, but did not changed the actions result.

The **normal** level setting shows all things that can cause more serious problems.

The **low** and **info** levels shows almost any information under the hood, these levels should not be used by server admins, nless you need information about the plugin behavior, the amount of data that will be sent by the logger will make the console unreadable.

Additionally there are custom logging levels, but are used only for specific cases.

### Level relations

| Level | Shows |
| --- | --- |
| None, [false, disabled] | Nothing |
| Critical | Critical |
| High | High, Critical |
| Normal | Normal, High, Critical |
| Low | Low, Normal, High, Critical |
| Info | Info, Low, Normal, High, Critical |
| Custom | Custom |

## Locale section

This section allows you to choose what language you want to use for this plugin and if it should auto update it if a new version was found.

```
   load: en
```

This node is used to choose the language you want to use, it first looks for a file with the name **locale.<target>.yml** in the **locales** folder, where the **<target>** part is the value you set in the **load** node, so for this example it would be **locale.en.yml**

It it is not present, it will try to look for that locale file in the plugins resources, if it fails to find it a second time a **critical** error is thrown, and the plugin will not work as it should.

```
   auto-update: false
```

Info: This node is not used!

Setting the **auto-update** to **true** allows to manage locale updates, if a update is found *(the locale version is higher)* for the locale you are using, it will automatically replace all lines to the newest version.

## Trader section

All settings in this section affects the behavior of all traders on the server, so changing any setting here will affect every trader in game, however some settings will only affect new created traders.

---

```
   allow-damage: false
```

Allows you to change the behavior when **left-clicking** *(damaging)* a trader. When set to **false** it will disable any damage done to the trader, moreover it will check the player if he has permissions to toggle **manager mode**, unless the **right-click** setting is set to **true**.

If you set this setting to **true** you can damage a trader *(if other citizen settings allow this too)* and toggling **manager mode** is only possible when **sneaking**.

### Transactions

```
   double-click: false
```

Changes the click behavior when buying or selling, by default if set to **false** you sell and buy items clicking once on them, if set to **true** you will need to **double-click** the item to perform any action.

### More coming soon!

## denizen section
