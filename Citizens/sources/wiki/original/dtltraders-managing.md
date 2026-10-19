## Introduction

Managing a trader is in essence changing its variables. Several aspects of npc traders can be controlled in this way. Managing differs between each trader type, because each has its own function and they don't work in the same way.

So far only basic commands have been adeed, but far more will be included in a future update. At this time it is not possible to fully manage a trader using only commands.

## Server trader

#### Features

1. buy and sell tabs (max 51 slots each)
2. global limits
3. player limits (currently not working, will be fixed in a future update)
4. prices can be set per item or per item stack
5. items can be sold in several customizable stack sizes
6. six different wallets types

#### Stock managing

**Adding an item**
  
To add an item into a *server trader's* stock just drag and drop the item from your inventory. That's it.  
The buy/sell tab layout is saved after every change so items will always appear in the slots they were added to. This allows you to arrange the offered goods in any way you want.  
  
**Editing an item**
  
If you want to relocate an item that is already in the trader's stock just drag it to a new location. Item iformation is retained, the only thing that will change is it's position.  
  
**Removing an item**
  
To remove an item so it can no longer be sold/bought simply drag and drop it to your inventory.  
  
**Switching between the sell and buy tabs**  
In the lower right corner of the trader's inventory are several differently colored wool blocks (this can be changed to anything you want in the config file). The rightmost one switches between selling and buying items. A message will appear when you successfully switch tabs.

#### Price managing

**Enabling the price managment**  
Added items don't have a price assigned to them. To be able to set it you have to click the black wool (the middle one if changed to something else). To exit the price edit mode simply click it again.  
  
**Checking the current price**  
To see an item's current price just click it with an **empty** cursor.  
  
**Changing the price**  
Change in the price value is dependent on:

1. **type of interaction**
   1. right click decreases the price
   2. left click increases the price
2. **item used**
   1. wood counts as * 0.01
   2. log counts as * 0.1
   3. dirt counts as * 10
   4. cobblestone counts as * 100
   5. items not listed above count as * 1

Examples:

```
   A single click with a block of drit increases the price by 10
   Ten clicks with a block of soul sand increase the price by 10
   One right click with 10 blocks of dirt deacreases the price by 100 
```

**Price patterns (will be added in ver 2.0)**

Price patterns let you create several pricing profiles and quickly switch between them. Additionally with a pricing pattern active adding any item included in the profile will automatically set it's price. You can still change the price manually.

#### Stack price

To easily set the desired price when selling multiple items at once you can turn on the stack price setting. Usually you just set the price of a single item and it gets multiplied by the number of items in the stack. The above option gives you direct control over the final price so you don't have to use fractions when you want to set the price to a specific number.

To apply the price to the whole stack instead of a single item just **right click** the item.

***Warning***: Stack price and amount selection menu cannot be used together. This will be changed in the near future.

#### Global limits

Limits are used to control how many items can be bought in a given time frame. Buying an item decreases the limit counter and when it reaches zero the item is no longer offered. When a set amount of time has passed the limit counter resets back to its original value and the item can be bought again.

To place limits on the number of offered items click the blue wool

1. right click lowers the limit
2. left click raises the limit
3. shift right click decreases the time it takes for the limit to reset
4. shift left click increases the time it takes for the limit to reset

#### Player Limits

Player limits work the same as above. The only difference is that the limit is applied individualy per player instead of a global effect.

Player limits are not implemented at this time.

## Navigation

| **DtlTraders** | |
| --- | --- |
| Usage | [Managing](http://wiki.citizensnpcs.com/DtlTraders/managing) | [Trading](http://wiki.citizensnpcs.com/DtlTraders/trading) | [Banking](http://wiki.citizensnpcs.com/DtlTraders/banking) |
| Configuration | [Configuration](http://wiki.citizensnpcs.com/DtlTraders/config) | [Commands](http://wiki.citizensnpcs.com/DtlTraders/Commands) | [Permissions](http://wiki.citizensnpcs.com/DtlTraders/permissions) | [Locale](http://wiki.citizensnpcs.com/DtlTraders/locale) |
| Types | [Traders](http://wiki.citizensnpcs.com/DtlTraders/traders) | [Bankers](http://wiki.citizensnpcs.com/DtlTraders/bankers) |
