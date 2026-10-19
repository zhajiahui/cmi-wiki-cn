Citizens has built-in support for basic GUI shops.

## Getting Started

Type `/npc shop edit` to open the NPC's shop.
You can also create a named shop by typing `/npc shop edit NAMEHERE`. Named shops can be shared by any NPC.

You will see basic configuration settings including editing the type of shop from buy to sell to command shops, setting the permission required to view the shop, and whether to open the shop on right click.

Here you can see the settings screen from left to right:

[![](https://wiki.citizensnpcs.co/images/2/2a/Shop_Settings.png)](https://wiki.citizensnpcs.co/File:Shop_Settings.png)

You can edit the permission required to view the shop, the shop items, the shop title, whether to open this shop on right click and the type of shop (explained later).

After clicking on the edit shop button for example you can see the following screen. Edit the shop title in the anvil menu and click on the paper to change the title!

[![](https://wiki.citizensnpcs.co/images/9/99/Edit_Shop_Screen.png)](https://wiki.citizensnpcs.co/File:Edit_Shop_Screen.png)

## Editing pages

You probably want to create a shop page. Click on the feather icon to start editing individual pages.

In this screen, you can drop an item onto the page slots to put it into the shop.

[![](https://wiki.citizensnpcs.co/images/e/e9/Edit_Shop_Items.png)](https://wiki.citizensnpcs.co/File:Edit_Shop_Items.png)

This will be the item that's displayed in your shop. You can also edit the next page slots by using shift-click.

## Editing items

Once in the editing item screen, you can set a **cost** (on the top left) and a **result** (on the top right). Note that a result item must be set or else the item will just sit in the shop looking pretty.

[![](https://wiki.citizensnpcs.co/images/6/6f/Edit_Item_Screen.png)](https://wiki.citizensnpcs.co/File:Edit_Item_Screen.png)

There's some buttons at the bottom to edit various things like purchase message, click to confirm, max purchases etc.
Please note: the green emerald block must be clicked to save the item when you're done.

Next, let's add a cost and a result. I have some sand and I want to set up a trade from one sand to three sticks.

First, I click on the item cost chest button at the top left.

[![](https://wiki.citizensnpcs.co/images/6/60/Item_Cost_.png)](https://wiki.citizensnpcs.co/File:Item_Cost_.png)

Just drag and drop an item anywhere in the top screen to set it as a cost. I do the same thing for the item result (3 sticks). You can see the preview of the cost and result by hovering over the icons.

[![](https://wiki.citizensnpcs.co/images/4/40/Item_Result_preview.png)](https://wiki.citizensnpcs.co/File:Item_Result_preview.png)
[![](https://wiki.citizensnpcs.co/images/d/d8/Item_Display_Preview.png)](https://wiki.citizensnpcs.co/File:Item_Display_Preview.png)

I also set the shop to show on right click using the following setting.

[![](https://wiki.citizensnpcs.co/images/a/ac/Shop_Show_on_right_click.png)](https://wiki.citizensnpcs.co/File:Shop_Show_on_right_click.png)

Here's the final resulting shop and I can easily trade for some sticks.

[![](https://wiki.citizensnpcs.co/images/9/9c/Shop_Result_1.png)](https://wiki.citizensnpcs.co/File:Shop_Result_1.png)
[![](https://wiki.citizensnpcs.co/images/f/f4/Shop_Result_2.png)](https://wiki.citizensnpcs.co/File:Shop_Result_2.png)

## Changing the shop type

You can change the shop type in the shop settings. Currently, this lets you change the number of chest rows your shop will show and also make it into a trader shop i.e. display as a villager trader GUI.

Using the above demo, let's see what the trader shop looks like. First, I set the shop to a trader shop.

[![](https://wiki.citizensnpcs.co/images/b/b4/Shop_type_set.png)](https://wiki.citizensnpcs.co/File:Shop_type_set.png)

Now we can see the final result.

[![](https://wiki.citizensnpcs.co/images/4/49/Trader_shop.png)](https://wiki.citizensnpcs.co/File:Trader_shop.png)

Note that the result of the trade is shown as the display item, not the stick result.

## Advanced topics

Citizens has a <cost> and <result> placeholder that you can put into the display item description to automatically show the cost and result.

### Component Comparison Filter

By default, Citizens checks that item costs are **exactly** the same including NBT/component tags, except for amount. You can change this by adding a component comparison filter. For example, the filter 'enchantments' would only check that two item enchantments are the same, even if they had other components that were different. You can see a printout of an item's components by using /npc debug -i with the item held in hand.

### Condition cost / result

This enables dynamic costs using placeholders and more. Some documentation about this is here (subject to change): [Behaviors](https://wiki.citizensnpcs.co/Behaviors "Behaviors")

For example, you might use `papi('player_leaderboard_placeholder') < 5`

### Requests

If you would like more info here on a particular shop feature, please ask on Discord.
