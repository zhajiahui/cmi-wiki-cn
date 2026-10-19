## **░ Table of contents** <A NAME="table_contents">
#### FAQ
* <A HREF="#flexibility">How do I use CrackShot weapons with other plugins? (kits, arenas, shops, classes etc.)</A>
* <A HREF="#permissions">I configured my permissions file. How come players can still use all weapons?</A>
* <A HREF="#config">I modified the configuration. Why don't the weapons show up anymore?</A>
* <A HREF="#pls">Can you please add 〈insert weapon name here〉?</A>

## **░ Using CrackShot weapons with other plugins** <A NAME="flexibility">
#### Method 1 - The Skip_Name_Check node
You can use the <a href="https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#skip_name_check" target="_blank">Skip_Name_Check</a> node to convert items with particular item IDs into _CrackShot_ weapons.

Example usage:

    Item_Type: 264~10
    Skip_Name_Check: true

All items on the server with an item ID of `264:10` will be automatically converted into that particular _CrackShot_ weapon. Hence, you can now simply give your players `264:10` via other plugins.

#### Method 2 - The Enchantment_To_Check node
You can use the <a href="https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#enchantment_to_check" target="_blank">Enchantment_To_Check</a> node to convert items with particular enchantments into _CrackShot_ weapons.

Example usage:

    Item_Type: 264
    Enchantment_To_Check: SILK_TOUCH-2

All items on the server with an item ID of `264` as well as a _Silk Touch II_ enchantment will be automatically converted into that particular _CrackShot_ weapon. Hence, you can now simply give your players a _Diamond_ (ID: 264) with _Silk Touch II_.

#### Method 3 - The CrackShot API
If you are a plugin developer who wishes to add direct support for _CrackShot_ weapons, you can [hook into _CrackShot_](https://github.com/Shampaggon/CrackShot/wiki/Hooking-into-CrackShot) and give weapons directly to players using the _giveWeapon_ function.

#### Method 4 - The CrackShot commands
If the plugin you are using to spawn _CrackShot_ weapons supports commands, such as _BuyCraft_ or _CommandSigns_, then you can simply utilize the [give and get commands of _CrackShot_](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions) to grant weapons to players.

## **░ Setting up your permissions** <A NAME="permissions">
As stated in the [commands and permissions](https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions) page, the following permission nodes are granted to _all_ users by default:

* crackshot.use.all
* crackshot.craft.all
* crackshot.buy.all

This means that you must first _negate_ these nodes if you want to specify which weapons you want your players to use, craft, or buy. You can negate nodes on most permissions plugins using a dash `-`.

Example permissions configuration:

    permissions:
    - -crackshot.use.all
    - crackshot.use.deagle
    - crackshot.use.python

The above configuration will only allow users to use the default weapons _Desert Eagle_ and _Python_. If you did not negate the `crackshot.use.all` permission that all players have by default, then they will still have permission to use all _CrackShot_ weapons.

## **░ The configuration fails to load** <A NAME="config">
If you find that only some or no weapons show up in CrackShot's _list_ command after modifying the configuration, then you have clearly failed to configure the weapons correctly.

[YAML](http://yaml.org/) follows a very strict format. Make sure that:
* you have not used any tabs.
* each node or module is indented correctly.
* all strings are surrounded by quotes.

If you are really struggling to get your weapons working, here are a list of things you can try:
* **Check the console for errors** - Errors printed out in the console will almost _always_ pinpoint the error. For example, if you've accidentally used a tab somewhere, the error message will tell you exactly which line it is located in.
* **Paste your configuration into a YAML parser** - An [online YAML parser](http://yaml-online-parser.appspot.com/) can always be used to help locate the problem.
* **Post your configuration on the forums** - Along with myself, there will be a large number of users on the forums who will be happy to help you, given that you post your configuration _in its correct format_ (i.e. with [Pastebin](http://pastebin.com/) or proper formatting codes).

## **░ Requesting generic default weapons** <A NAME="pls">
> Example 1: Can you please add Gold Desert Eagle and MP5?  
Example 2: Please add G36C!  
Example 3: Can you please add a mini-gun in?  

These are all silly questions that get asked by people who are very clearly missing the point of the plugin. The default weapons are only there to demonstrate certain features of _CrackShot_ - dual wield, attachments, firearm actions and so forth. Generic weapons that can already be achieved by the plugin will not be thrown in due to personal incompetence. [Read the guide](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot) and learn to create or modify weapons.

Such requests are almost guaranteed to be dismissed. However, if you are feeling lucky, you can always give the [forums](http://dev.bukkit.org/bukkit-plugins/crackshot/forum/) a try.