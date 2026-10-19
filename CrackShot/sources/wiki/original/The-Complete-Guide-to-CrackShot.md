## **░ Table of contents** <A NAME="table_contents">

### Other pages
* <a href="https://github.com/Shampaggon/CrackShot/wiki/Installation" target="_blank">Installing CrackShot</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions" target="_blank">Commands and permissions</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/List-of-Modules" target="_blank">Complete list of modules</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/Default-weapons" target="_blank">Default weapons</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/List-of-Accepted-Sounds" target="_blank">Sound types</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/List-of-Accepted-Mobs" target="_blank">Mob types</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/Hooking-into-CrackShot" target="_blank">Hooking into CrackShot</a>
* <a href="https://github.com/Shampaggon/CrackShot/wiki/Frequently-Asked-Questions" target="_blank">Frequently asked questions</a>

### Getting started
* <A HREF="#getting">Getting started</A>
* <A HREF="#modules">Modules and nodes</A>
* <A HREF="#modules">Weapons folder</A>
* <A HREF="#itemID">Item IDs</A>
* <A HREF="#intsplz">Integers for values</A>
* <A HREF="#delay">Delays for dummies</A>
* <A HREF="#damage">Damage for dummies</A>
* <A HREF="#sounds">Customizable sounds</A>
* <A HREF="#variables">Special variables</A>
* <A HREF="#colors">Color codes</A>
* <A HREF="#stacks">Stackable values</A>

### Modules
* <A HREF="#title">Weapon title</A>
* <A HREF="#item_info">Item information</A>
* <A HREF="#shooting">Shooting</A>
* <A HREF="#sneak">Sneak</A>
* <A HREF="#spray_and_pray">Fully automatic</A>
* <A HREF="#burst">Burst fire</A>
* <A HREF="#ammo">Ammunition</A>
* <A HREF="#reload">Reloads</A>
* <A HREF="#firearm">Firearm actions</A>
* <A HREF="#scope">Scopes and iron sights</A>
* <A HREF="#shield">Riot shields</A>
* <A HREF="#stores">Sign shops</A>
* <A HREF="#crafting">Crafting recipes</A>
* <A HREF="#regions">Region checks</A>
* <A HREF="#death_messages">Custom death messages</A>
* <A HREF="#headshot">Headshots</A>
* <A HREF="#backstabs">Backstabs</A>
* <A HREF="#Cr1TiKaL">Critical hits</A>
* <A HREF="#entity">Summon entities</A>
* <A HREF="#flight_time">Base damage on flight time</A>
* <A HREF="#airstrikes">Airstrikes</A>
* <A HREF="#devices">Explosive devices</A>
* <A HREF="#cluster">Cluster bombs</A>
* <A HREF="#shrapnel">Shrapnel</A>
* <A HREF="#kaboom">Explosions</A>
* <A HREF="#lightning">Lightning</A>
* <A HREF="#potions">Potion effects</A>
* <A HREF="#particles">Particle effects</A>
* <A HREF="#fireworks">Fireworks</A>
* <A HREF="#abilities">Abilities</A>
* <A HREF="#hit_events">Hit events</A>
* <A HREF="#extras">Extras</A>

## **░ Getting started** <A NAME="getting">
This page should only be used as a reference! Attempting to read through all the modules from top to bottom won't be any different to reading a dictionary. I'd advise playing around with the <a href="https://github.com/Shampaggon/CrackShot/wiki/Default-weapons" target="_blank">_weapons that are provided by default_</a>, as well as having a look at the <a href="https://github.com/Shampaggon/CrackShot/wiki/List-of-Modules" target="_blank">_complete list of modules_</a> and then using the <A HREF="#table_contents">_table of contents_</A> to navigate to the module you have interest in using.

#### **Modules and nodes** <A NAME="modules">
To keep your configuration looking clean, remove any particular module or node that you are not using.  
Removed modules and nodes will not be taken into account. It's as simple as that.

It might also be good to remember that:

* All nodes that require a _number_ for a value will default to `0` if no value is provided.
* All nodes that require _true or false_ for a value will default to `false` if no value is provided.

So if you ever come across `Right_Click_To_Shoot: false` or `Explosion_Delay: 0`, you can simply remove them.

#### **Weapons folder** <A NAME="folder">
_CrackShot_ will load any configuration file that it can find in the 'weapons' folder - the names of the files don't matter. As shown by the default configuration files _defaultWeapons.yml_ and _defaultExplosives.yml_, you can have multiple weapons in one file. You can even fit _all_ your weapons into one file, if you want. Some people prefer to have an individual file for each weapon, some don't. It's up to you how you want to organize your creations.

Note: If the weapons folder is empty, _CrackShot_ will automatically regenerate the three default configuration files: _defaultWeapons.yml_, _defaultExplosives.yml_ and _defaultAttachments.yml_.

#### **Item IDs** <A NAME="itemID">
Unsure of what the ID of a particular item is? I like to refer this <a href="http://www.minecraftinfo.com/IDList.htm" target="_blank">_fantastic website_</a>. It updates whenever new content is introduced, so it is essentially _always_ up to date.

Note: Some nodes support _secondary data values_. For example, `98~2` will represent the item ID of _Cracked Stone Bricks_.

> For **Minecraft 1.13 or higher**, use _names_ instead of _numbers_, because newer blocks/items may not have a numeric ID. Refer to [_this website_](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) for item names.  For example, the item ID of _Cracked Stone Bricks_ (as a name) would be `CRACKED_STONE_BRICKS`.

#### **Integers for values** <A NAME="intsplz">
Whenever a node requires a number for a value, the number must be an _integer_ or a _whole number_. In other words: `5` or `32` is supported, but `0.024` or `1.243` is not. Only **some** nodes support decimal values, such as bullet spread.

Trivia: So what happens if you add decimals to values that do not support it? No, your computer _won't_ explode; the value will simply be considered as _zero_ and will not be taken into account.

#### **Delays for dummies** <A NAME="delay">
_All delays_ in the configuration are in _ticks_. 20 ticks equate to 1 second.

Quiz: How many seconds would 120 ticks equate to? If you answered with anything other than 6 seconds, there might be a problem...

#### **Damage for dummies** <A NAME="damage">
Whenever a node asks about _damage_, you must remember that 2 units of damage equates to _one heart_. If your mathematics is sub-par, that means healthy players can take 20 units of damage before dying.

#### **Customizable sounds** <A NAME="sounds">
_All sounds_ follow the format: `SOUND-VOLUME-PITCH-DELAY`.
* `SOUND` is the type of sound.
* `VOLUME` is a value from 0-1 that determines how loud the sound is. Any value greater than 1 increases the **range** of the sound.
* `PITCH` is a value from 0-2 that determines the pitch of the sound.
* `DELAY` is the delay in ticks before the sound is played.

By default, sounds have a `PITCH` and `VOLUME` of 1.  
View the <a href="https://github.com/Shampaggon/CrackShot/wiki/List-of-Accepted-Sounds" target="_blank">_complete list of sounds_</a> to determine which sound is right for you.

#### **Strings | Special variables** <A NAME="variables">
_All strings_, unless otherwise specified, can use four special variables which are automatically converted into their corresponding values upon interaction.

    <shooter> - Will be converted into the shooter's name.
    <victim> - Will be converted into the victim's name.
    <damage> - Will be converted into the total damage dealt.
    <flight> - Will be converted into the total flight time of the projectile.

Example: A weapon has `Message_Shooter: "You shot <victim> for <damage> damage! Your name is <shooter>!"` in the `Hit_Events:` module. Using this weapon, a player named _MrDerp_ shoots another player named _Bieber_ for 20 damage. The message _MrDerp_ receives will be: "You shot Bieber for 20 damage! Your name is MrDerp!".

#### **Strings | Color codes** <A NAME="colors">
_All strings_ in the configuration support _color codes_ `&<?>`. Be sure to make good use of it!

Note: If a color-code is used in a particular string, that entire string _must_ be surrounded by quotes! For example, this will work - `Message_Victim: "&eWhy, hello there."`, but this will _not_ - `Message_Victim: &eWhy, hello there.`

    Code    Result

    &0 	    Black
	&1 	    Dark Blue
	&2 	    Dark Green
	&3 	    Dark Aqua
	&4 	    Dark Red
	&5 	    Purple
	&6 	    Gold
	&7 	    Gray
	&8 	    Dark Gray
	&9 	    Blue
	&a 	    Green
	&b 	    Aqua
	&c 	    Red
	&d 	    Light Purple
	&e 	    Yellow
	&f 	    White
    &k 	    Obfuscated
    &l 	    Bold
    &m 	    Strikethrough
    &n 	    Underline
    &o 	    Italic
    &r 	    Reset

#### **Stackable values** <A NAME="stacks">
In the examples below, you may come across `(...)` in things like:
* `Sounds_Acquired: <sound>,(...)`
* `Firework_Player_Shoot: <firework>,(...)`
* `Make_Victim_Run_Commmand: <command>|(...)`

While at first glance it may appear a little bizarre, `(...)` simply means that the values are _stackable_. That is, _multiple values_ are supported.

Examples:
* `Sounds_Acquired: <sound1>,<sound2>,<sound3>`
* `Firework_Player_Shoot: <firework1>,<firework2>`
* `Make_Victim_Run_Commmand: <command1>|<command2>|<command3>`

These are all acceptable. Be sure to pay extra care to the _separator_ that is required for these values; it will usually be either `,` or `|` unless otherwise specified.

## **░ Weapon title** <A NAME="title">
    My_Little_Friend:
This will be the name used to spawn the item using `/shot get <weapon>`, will be the name used for permissions `crackshot.<action>.<weapon>`, and will be the same name that appears in the list called by `/shot list`. It must be _unique_, must _not_ contain any spaces and must always be the very first node of _any_ weapon.

Example: To spawn the weapon above, one would type `/shot get my_little_friend`. Similarly, the permission node to use the weapon would be `crackshot.use.my_little_friend`.

## **░ Item information** <A NAME="item_info">
    Item_Information:
        Item_Name: <name>
        Item_Type: <itemID> OR <itemID~data>
        Item_Lore: <line1>|<line2>|<line3>|<line4> ... |<line9001>
        Inventory_Control: <group>,(...)
        Melee_Mode: <true/false>
        Melee_Attachment: <weapon title>
        Attachments:
            Type: <main> OR <accessory>
            Info: <weapon title>
            Toggle_Delay: <ticks>
            Sounds_Toggle: <sound>,(...)
        Enchantment_To_Check: <ENCHANTMENT-LEVEL>
        Skip_Name_Check: <true/false>
        Sounds_Acquired: <sound>,(...)
        Remove_Unused_Tag: <true/false>
        Hidden_From_List: <true/false>

#### Item_Name:
The item's _display name_ - the name that the players will see when selecting this item.

Example: By using the <A HREF="#colors">color-code</A> for _yellow_ `&e`, you can color an item's name: `"&eA yellow display name"`

#### Item_Type:
The <A HREF="#itemID">_ID_</A> of the item's type. For example, if you would like the item to be a _Bone_, you would put `Item_Type: 352`. 

Note: Secondary data values are supported. Simply separate the primary and secondary value with the tilde symbol (~). For example, if you would like the item to be a _Pink Dye_, you would put `Item_Type: 351~9`.

> Important note - If you are using a _block item_, the secondary data value you provide must be valid, or _Bukkit_ will set it to zero. _Block items_ are items with an ID from 1-255. Here are some examples:

> * `Item_Type: 98~2` - 98:2 are _Cracked Stone Bricks_, so this is valid.
> * `Item_Type: 98~66` - 98:66 does not exist, so this is invalid and _Bukkit_ will change the item into 98:0.
> * `Item_Type: 104~23` - 104:23 does not exist, so this is invalid and _Bukkit_ will change the item into 104:0.
> * `Item_Type: 294~23` - This is valid. 294 is _not_ a block item, so you can have whatever secondary data value you want!

> If you provide an invalid secondary data value for a _block item_, the weapon will not function when used.

#### Item_Lore:
The item's description. This is what players will see when hovering their mouse over the item. To indicate a new line, use a vertical bar `|`.

Example: `Item_Name: "&eThis is line one.|&eThis is line two.|&eThis is line three."`

#### Inventory_Control:
The _Inventory Control_ feature is used to limit the amount of specific weapons that can be in the hot bar in order for a weapon to be used, preventing players from having a whole arsenal of weapons that they can switch to and from.

This node represents the group(s) that the weapon belongs to, if any. Use this node with the *Inventory_Control* section in the _general.yml_ configuration file.

Example: A weapon named _Peacekeeper_ has `Inventory_Control: primary_weapons`. In the *Inventory_Control* section of the _general.yml_ file:

        primary_weapons:
            Limit: 2
            Message_Exceeded: "&eYou cannot have more than two primary weapons in the hot bar!"
            Sounds_Exceeded: LAVA_POP-1-1-0

This means that the _Peacekeeper_ can only be used if there are no more than two weapons in the hot bar that belong to the *primary_weapons* group. The sounds and messages are optional.

#### Melee_Mode:
If set to true, **hitting an entity with this weapon would be the same as hitting the entity with a projectile fired from this weapon**. Remember the bolded text very carefully; you should be able to filter out the irrelevant nodes on your own.

If melee-mode is enabled:
* The weapon will no longer fire any projectiles.
* The weapon can be used as a melee attachment by other weapons.
* The weapon will still support the Ammo and Reload modules, but not the Firearm_Action module. Ammo will be taken _per hit_.
* The *Delay_Between_Shots* node will represent the delay between each time the weapon can hit someone.
* Headshots are ignored, as they cannot be detected via a melee attack.
* The *Damage_Based_On_Flight_Time* module will be ignored, as there _is_ no projectile.

For more advanced melee weapons - delays between each _swing_ of the weapon, chainsaws and so forth - consider using the _energy_ projectile type instead.

Trivia: Did you know that weapons using *Melee_Mode* or *Melee_Attachment* can be used as ordinary attachments (`Type: accessory`)?

#### Melee_Attachment:
Represents the <A HREF="#title">weapon-title</A> of a melee weapon. Use this node to make the weapon inherit the melee properties of _another_ weapon. The weapon that you provide must be a valid melee weapon - i.e. have `Melee_Mode: true`.

Slightly confused? You are encouraged to look at the default weapons [Python](https://github.com/Shampaggon/CrackShot/wiki/Default-weapons#python-revolver-w-tactical-knife) and [Tactical Knife (melee attachment)](https://github.com/Shampaggon/CrackShot/wiki/Default-weapons#tactical-knife-melee-attachment).

#### Attachments:
Mains (weapons with `Type: main`) will use the attachment specified in the `Info:` node. These weapons can switch to their attachments with right click (or left click, if `Right_Click_To_Shoot: true`). For obvious reasons, such weapons will not have proper access to _scoping_ or _dual wield_.

Attachments (weapons with `Type: accessory`) do not require any other nodes in the *Item_Information* module except for the ones in the _Attachments_ section. They are inaccessible using the list and get commands, and do not support the *Explosive_Devices* and *Firearm_Action* modules. They _can_, however, be used alongside weapons that use the *Firearm_Action* module.

Slightly confused? You are encouraged to look at the default weapons [Carbine (main)](https://github.com/Shampaggon/CrackShot/wiki/Default-weapons#carbine-assault-rifle-w-grenade-launcher) and [M320 (attachment)](https://github.com/Shampaggon/CrackShot/wiki/Default-weapons#m320-attachment---grenade-launcher).

* **Type:**
    * If the weapon is using an attachment, set this to `main` and provide the attachment's <A HREF="#title">weapon-title</A> to the _Info_ node. If the weapon _is_ an attachment, set this to `accessory`.
* **Info:**
    * This node is only used if the weapon has `Type: main`. Represents the <A HREF="#title">weapon-title</A> of the attachment that the weapon will use.
* **Toggle_Delay:**
    * The <A HREF="#delay">delay</A> in ticks that the player must wait before the freshly toggled weapon can be fired or toggled again.
* **Sounds_Toggle:**
    * The <A HREF="#sounds">sound(s)</A> played whenever the weapon is toggled.

#### Enchantment_To_Check:
All items with this particular enchantment will be converted into this weapon, given that its <A HREF="#itemID">item-ID</A> matches as well.

Example: The configuration for a particular weapon named _Chuck Norris_ has `Enchantment_To_Check: DAMAGE_ALL-2` and `Item_Type: 352`. Any item that has an item-ID of 352 _as well_ as a level 2 Sharpness (DAMAGE_ALL) enchantment will be automatically converted into _Chuck Norris_ upon interaction.

    List of enchantments:
    
    ARROW_DAMAGE
    ARROW_FIRE
    ARROW_INFINITE
    ARROW_KNOCKBACK
    DAMAGE_ALL
    DAMAGE_ARTHROPODS
    DAMAGE_UNDEAD
    DIG_SPEED
    DURABILITY
    FIRE_ASPECT
    KNOCKBACK
    LOOT_BONUS_BLOCKS
    LOOT_BONUS_MOBS
    OXYGEN
    PROTECTION_ENVIRONMENTAL
    PROTECTION_EXPLOSIONS
    PROTECTION_FALL
    PROTECTION_FIRE
    PROTECTION_PROJECTILE
    SILK_TOUCH
    THORNS
    WATER_WORKER

#### Skip_Name_Check:
If set to `true`, all items matching the <A HREF="#itemID">item-ID</A> specified in `Item_Type` will be converted into this weapon.

Example: A weapon named _Fishy_ has `Item_Type: 349~7` and `Skip_Name_Check: true`. Any item that has an <A HREF="#itemID">ID</A> of 349:7 will be automatically converted into _Fishy_.

Note: Try to use _unused_ secondary data values to avoid converting ordinary items. For instance, having `Item_Type: 264` and `Skip_Name_Check: true` is generally a bad idea, as all _Diamonds_ (ID: 264) would be converted into that particular weapon.

> Important note - if you are using this node, you are advised against providing _block items_ or _durability items_ for the Item_Type node. _Block items_ are items with an ID from 1-255. _Durability items_ are any items with durability levels, such as tools and armor.

#### Sounds_Acquired:
The <A HREF="#sounds">sound(s)</A> heard whenever a player either _spawns_ this item using `/shot get`, or purchases it through a sign shop.

#### Remove_Unused_Tag:
If true, any unused tags `«×»` will be removed from the weapon's item name.

Note: The tag cannot be removed from weapons that use the <A HREF="#firearm">Firearm_Action</A> module.

#### Hidden_From_List:
If true, the weapon will be hidden from the list that appears whenever `/shot list` is called.

## **░ Shooting** <A NAME="shooting">
    Shooting:
        Disable: <true/false>
        Dual_Wield: <true/false>
        Right_Click_To_Shoot: <true/false>
        Cancel_Left_Click_Block_Damage: <true/false>
        Cancel_Right_Click_Interactions: <true/false>
        Delay_Between_Shots: <ticks>
        Recoil_Amount: <amount>
        Projectile_Amount: <amount>
        Projectile_Type: <snowball/arrow/egg/grenade/flare/fireball/witherskull/energy/splash>
        Projectile_Subtype: <itemID> OR <itemID~data> OR <energy info> OR <true/false>
        Remove_Arrows_On_Impact: <true/false>
        Remove_Bullet_Drop: <true/false>
        Removal_Or_Drag_Delay: <delay-removal>
        Projectile_Speed: <amount>
        Projectile_Damage: <amount>
        Projectile_Flames: <true/false>
        Projectile_Incendiary:
            Enable: <true/false>
            Duration: <ticks>
        Bullet_Spread: <amount>
        Reset_Fall_Distance: <true/false>
        Sounds_Projectile: <sound>,(...)
        Sounds_Shoot: <sound>,(...)

#### Disable:
If true, shooting will be disabled entirely. Generally, you would only disable shooting if you decide to turn the weapon into a <A HREF="#shield">riot shield</A> or some <A HREF="#devices">explosive device</A>.

#### Dual_Wield:
If true, the weapon will be _dual wielded_ (one weapon held in each hand). Left-clicking the weapon will fire the weapon on the left, while right-clicking the weapon will fire the weapon on the right. Both weapons can be fired simultaneously.

Note: When this node is set to true, the `Right_Click_To_Shoot:` node will obviously be ignored. The `Scope` and `Firearm_Action:` modules will also be ignored.

#### Right_Click_To_Shoot:
By default, left-click is used to shoot, while right-click is used for the iron sights (zooming in). Enabling this will switch things around. 

Note: In most cases, you would only use right-click to shoot if the weapon is fully-automatic, as holding right-click will cause the player to shoot repeatedly, while holding left-click does not.

#### Cancel_Left_Click_Block_Damage:
Players clicking frantically while shooting a weapon may accidentally break blocks. Setting this node to `true` will cancel all block-damage for that particular weapon.

#### Cancel_Right_Click_Interactions:
Players shooting or zooming with right-click may accidentally interact with buttons, doors and so forth. If the weapon is a block or a minecart, they may also accidentally _place_ it. Setting this node to `true` will cancel all right-click interactions for that particular weapon.

#### Delay_Between_Shots:
The <A HREF="#delay">delay</A> in ticks that the player must wait before the next shot can be fired.

#### Recoil_Amount:
The force by which the shooter will be pushed back for each shot. A negative value will pull the player _forwards_; I'm sure one could use that to their imagination.

Note: Shooting a weapon straight down with `Recoil_Amount: 40` is enough to send the player airborne for quite a lengthy period of time. A value between 1-10 is recommended, but feel free to experiment.

#### Projectile_Amount:
The number of projectiles that are launched per shot. For shotguns, this would generally be a value greater than one.

#### Projectile_Type:
There are nine values that you can input: `snowball`, `egg`, `arrow`, `grenade`, `flare`, `fireball`, `witherskull`, `energy`, `splash`.

* _Snowballs_ are highly recommended for ordinary projectiles.
* _Eggs_ are just as recommended as snowballs. Eggs fired from CrackShot weapons do not spawn chickens.
* _Arrows_ are just as recommended as snowballs. When using arrows, you may want to enable the *Remove_Arrows_On_Impact* node.
* _Grenades_ will launch a grenade in the form of a dropped item, which will explode after a specified amount of time. They do _not_ explode on impact. When a grenade _explodes_, it will use the settings defined in the `Explosions:` and `Lightning:` modules.
* _Flares_ are similar to grenades. Instead of exploding, however, they will <A HREF="#airstrikes">_call in an airstrike_</A> after a certain period of time.
* _Fireballs_ travel in a relatively straight line and explode upon impact. The explosion created is determined by the settings defined in the `Explosions:` module. You can prevent this projectile from being deflected by setting the *Projectile_Subtype* node to true.
* _Wither skulls_ are exactly the same as fireballs. The only difference is that they do not explode when hit by other projectiles. Due to a _Bukkit_ bug, wither skulls that score direct-hits on enemies may trigger a "Reach" violation in anti-cheat plugins. Aside from being a nuisance, this has no other effect.
* _Splash potions_ are thrown potions that hit all enemies in a splash radius. These projectiles do not support the `Headshot` or `Damage_Based_On_Flight_Time` modules. You can change the color of the splash, and only the splash, by providing a valid splash potion in the *Projectile_Subtype* node.

Note that `fireball` and `witherskull` can never be truly accurate, and do not take the `Bullet_Spread:` nodes very effectively.

**Energy**  
_Energy_ is an advanced projectile type that hits all enemies in a specified _cuboid region_ in front the player. Think of it as a **giant laser-beam**.  

In the *Projectile_Subtype* node, you will need to define its size (`RADIUS`), how far it travels _in blocks_ (`RANGE`), how many blocks it can pass through before stopping (`WALLS`) and how many victims it can pass through before stopping (`VICTIMS`).

If you are using the `energy` projectile type, the *Projectile_Subtype* node will follow this format:
* `Projectile_Subtype: RANGE-RADIUS-WALLS-VICTIMS`

Note that:
* For `WALLS`, you can input `NONE` if you want to turn off wall penetration completely, or you can input `ALL` if you want the projectile to pass through all blocks in its path. Otherwise, specify a number.
* For `VICTIMS`, you can simply input `0` if you want the projectile to pass through all victims. Otherwise, specify a number.

This projectile type can be used to mimic melee weapons such as chainsaws, area-of-effect weapons such as flamethrowers and highly-penetrative weapons that can pierce through multiple enemies and/or walls.

#### Projectile_Subtype:
A value is only necessary if `Projectile_Type:` is set to `grenade`, `flare`, `fireball`, `energy` or `splash`.

* For `grenade` and `flare` - This node represents the <A HREF="#itemID">item-ID</A> of the thrown item-drop.
* For `splash` - (Optional) This node represents the <A HREF="#itemID">item-ID</A> of the thrown splash potion. This will only change the _color_ of the splash and must be a valid splash potion.
* For `fireball` - (Optional) If this node is set to **true**, then the fireball cannot be deflected.
* For `energy` - This node will represent the information required for the weapon to fire an _energy-type_ projectile.

Note: Secondary data values are supported. Simply separate the primary and secondary value with the tilde symbol (~). For example, if you would like an item to be a _Red Wool_, you would put `Item_Type: 35~14`.

#### Remove_Arrows_On_Impact:
If `Projectile_Type:` is set to `arrow`, arrows will be removed _immediately_ upon impact. After all, nobody likes swimming in arrows, especially if a machine-gun has been customized to fire them.

#### Remove_Bullet_Drop:
If true, the fired projectile will travel in a _straight line_ and will not be affected by gravity. Affects only `snowball`, `egg` and `arrow`.

Note: Due to a Minecraft visual bug, slow projectiles using this node may appear to _bounce_ in mid-air, while fast projectiles may appear to curve away from the direction they are being fired at.

#### Removal_Or_Drag_Delay:
The <A HREF="#delay">delay</A> in ticks before the projectile is either _removed_ (`true`) or _dragged_ (`false`).  
When a projectile is _dragged_, its speed is significantly reduced.

Examples:
* `Removal_Or_Drag_Delay: 4-true` will _remove_ the projectile after 4 ticks.
* `Removal_Or_Drag_Delay: 3-false` will drastically _slow_ the projectile after 3 ticks.

#### Projectile_Speed:
The speed of the fired projectile(s). A value from 0-40 is recommended. Projectiles with a speed exceeding 40 will begin to show signs of _path warping_ due to a visual bug on Minecraft's side. Anything traveling at a speed above 100 would probably enter another dimension.

#### Projectile_Damage:
The amount of <A HREF="#damage">damage</A> each bullet will deal.

#### Projectile_Flames:
If true, the projectile will appear to be set on fire. Affects only `snowball`, `egg`, `arrow` and `splash`.

#### Projectile_Incendiary:
Incendiary projectiles will light victims on fire. Provide a <A HREF="#delay">duration</A> that determines how long the victims should stay alight for, given that `Enable:` is set to `true`.

#### Bullet_Spread:
Remember, this is not _accuracy_, this is _spread_. The closer this value is to 0, the more accurate the fired projectiles will be. _A value from 0-10 is recommended._ Input anything above 10 and the bullet would probably fly out the back of the barrel and hit you in the face.

Note: This node supports **decimal values**, such as _2.354_, _0.22556_ or _3.5_.

#### Reset_Fall_Distance:
Sometimes a firearm's recoil is so great that you can break falls with it. That's what this node is for. If set to `true`, each time this weapon is fired, the shooter's fall-damage will be cleared.

Clarification: Yes. You can now jump off a cliff, fire your gun at the feet _just_ before you hit the ground, and survive the fall.

#### Sounds_Projectile:
The <A HREF="#sounds">sound(s)</A> played by the projectile. Use this node for beeping grenades and so forth.

#### Sounds_Shoot:
The <A HREF="#sounds">sound(s)</A> played whenever the weapon is fired.

## **░ Sneak** <A NAME="sneak">
    Sneak:
        Enable: <true/false>
        No_Recoil: <true/false>
        Bullet_Spread: <amount>
        Sneak_Before_Shooting: <true/false>

#### Enable:
Whether or not sneaking should be taken into account.

#### No_Recoil:
If set to `true`, the player will experience no recoil while sneaking, that is, the player will not be pushed backwards (or forwards) by the recoil.

#### Bullet_Spread:
The spread of the projectiles fired while sneaking.

Note: This node supports **decimal values**, such as _2.354_, _0.22556_ or _3.5_.

Trivia: In games like _Left 4 Dead 2_, you cannot aim down the sights of most weapons. In order to improve accuracy, players will need to crouch while shooting. This is exactly what this node is provided for.

#### Sneak_Before_Shooting:
If set to `true`, the player must _crouch_ by sneaking before being able to shoot. Sneaking while airborne does not count.

## **░ Fully automatic** <A NAME="spray_and_pray">
    Fully_Automatic:
        Enable: <true/false>
        Fire_Rate: <fire-rate>

#### Enable:
If enabled, restricts the weapon to a specific rate of fire. It is highly recommended that you use this module with [Right_Click_To_Shoot](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#right_click_to_shoot) enabled. This is because in _Minecraft_, holding down right-click allows the player to shoot repeatedly, but holding down left-click does not.

In order to use this module:
* The <A HREF="#burst">Burstfire</A> module must be disabled.
* The [Delay_Between_Shots](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#delay_between_shots) node must be removed or set to `1` or `0`.
* The value for [Fire_Rate](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#fire_rate) must range from 1-16.

Example: See the [default AK-47](https://github.com/Shampaggon/CrackShot/wiki/Default-weapons#ak-47-assault-rifle).

#### Fire_Rate:
This is a value ranging from `1-16` that determines how quickly the weapon can shoot, measured in rounds (or shots) per minute.

        Fire rate    Rounds per minute (RPM)
        
        1            300
        2            360
        3            420
        4            480
        5            540
        6            600
        7            660
        8            720
        9            780
        10           840
        11           900
        12           960
        13           1020
        14           1080
        15           1140
        16           1200

Note: With `Fire_Rate: 16`, the weapon will shoot once every <A HREF="#delay">tick</A>. This is twenty shots per second, and is the _highest possible_ rate of fire in Minecraft.

## **░ Burst fire** <A NAME="burst">
    Burstfire:
        Enable: <true/false>
        Shots_Per_Burst: <amount>
        Delay_Between_Shots_In_Burst: <ticks>

#### Enable:
If enabled, allows multiple shots to be fired with a _single_ pull of the trigger.

Note: This module and the <A HREF="#spray_and_pray">Fully_Automatic</A> module cannot be used together.

#### Shots_Per_Burst:
The amount of shots fired per burst.

#### Delay_Between_Shots_In_Burst:
The <A HREF="#delay">delay</A> between each shot in the burst.

## **░ Ammunition** <A NAME="ammo">
    Ammo:
        Enable: <true/false>
        Ammo_Item_ID: <itemID> OR <itemID~data>
        Ammo_Name_Check: <name>
        Take_Ammo_Per_Shot: <true/false>
        Sounds_Out_Of_Ammo: <sound>,(...)
        Sounds_Shoot_With_No_Ammo: <sound>,(...)

#### Enable:
Whether or not ammunition should be taken into account.

#### Ammo_Item_ID:
The <A HREF="#itemID">ID</A> of the type of item being used as ammunition.

Note: Secondary data values are supported. For example, if you would like the item to be a _Pink Dye_, you would put `Ammo_Item_ID: 351~9`.

#### Ammo_Name_Check:
(Optional) The name of the item being used as ammunition.

Example: A weapon has `Ammo_Item_ID: 264`, `Ammo_Name_Check: "&eGun Ammo"` and `Take_Ammo_Per_Shot: true`. On each shot, 1 _Diamond_ with the name _&eGun Ammo_ (where "&e" is the [color-code](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot/_edit#colors) for yellow) will be taken from the shooter's inventory.

Note: Any item that contains the given name will also be accepted. Continuing with the previous example, each shot could also take 1 _Diamond_ with the name _Chocolate **&eGun Ammo** With Cream_.

#### Take_Ammo_Per_Shot:
Whether or not ammunition should be taken from the shooter's inventory after each shot.

Example: A weapon has `Ammo_Item_ID: 264` and `Take_Ammo_Per_Shot: true`. `264` is the <A HREF="#itemID">ID</A> for _Diamond_. On each shot, 1 _Diamond_ will be taken from the shooter's inventory. If the shooter has no diamonds, the weapon will not be able to be fired.

#### Sounds_Out_Of_Ammo:
The <A HREF="#sounds">sound(s)</A> played as soon as the final piece of ammunition is fired. In other words, as soon as the player's _inventory_ runs out of the specified ammunition, the sound(s) will be played.

#### Sounds_Shoot_With_No_Ammo:
The <A HREF="#sounds">sound(s)</A> played when a player attempts to shoot a weapon while having no ammunition.

Example: A player trying to shoot a weapon while having no ammunition in his inventory will hear this sound.

## **░ Reloading** <A NAME="reload">
    Reload:
        Enable: <true/false>
        Reload_With_Mouse: <true/false>
        Starting_Amount: <amount>
        Reload_Amount: <amount>
        Reload_Bullets_Individually: <true/false>
        Take_Ammo_On_Reload: <true/false>
        Take_Ammo_As_Magazine: <true/false>
        Reload_Duration: <ticks>
        Reload_Shoot_Delay: <ticks>
        Destroy_When_Empty: <true/false>
        Sounds_Out_Of_Ammo: <sound>,(...)
        Sounds_Reloading: <sound>,(...)
        Dual_Wield:
            Single_Reload_Duration:
            Sounds_Single_Reload:
            Sounds_Shoot_With_No_Ammo:

#### Enable:
Whether or not reloading should be enabled for this weapon. When this node is enabled:

* `Q` - or the button you use to drop your weapon - will be used to reload. (Unless `Reload_With_Mouse: true`)
* You can drop weapons normally by dragging them out of your inventory.
* The `/shot reload` command can be used to reload the weapon.

#### Reload_With_Mouse:
If set to true, the weapon will be reloaded with the left or right click, depending on whichever mouse button you are using to fire the weapon. `Q`, or the button you use to drop your weapon, will not longer be used to reload the weapon and you will be able to drop it normally.

#### Starting_Amount:
The amount of ammo the weapon starts with when it is first spawned. For example, if *Reload_Amount* is set to 30, and *Starting_Amount* is set to 15, then the weapon will start off with 15 out of 30 ammo.

This node is optional. If no value is provided, the weapon will spawn with full ammo.

#### Reload_Amount:
This value essentially determines the _magazine capacity_ of the weapon. In other words, how many bullets can this weapon hold and fire before a reload is required? And how many bullets will be restored to the weapon upon a reload?

Example: Consider the AK-47 from _Call of Duty 4._ It has a magazine size of 30 bullets. If one were to replicate that weapon, the value of `Reload_Amount:` would be `30`.

#### Reload_Bullets_Individually:
If set to `true`, will reload bullets one by one. This would generally be used for reloading shotguns, bolt-action rifles, revolvers etc.

#### Take_Ammo_On_Reload:
Similar to the `Take_Ammo_Per_Shot` node of the `Ammo` module. Setting this to `true` will take ammunition from the shooter's inventory upon reload.

Note: This node depends on the information provided in the `Ammo` module.

#### Take_Ammo_As_Magazine:
Similar to the `Take_Ammo_Per_Shot` node of the `Ammo` module. Setting this to `true` will cause a single item ("magazine") to be taken from the player's inventory upon each reload. If the weapon is being _dual wielded_, two magazines will be taken for a complete reload, as there are two firearms.

Note: This node depends on the information provided in the `Ammo` module.

#### Reload_Duration:
The amount of time in <A HREF="#delay">ticks</A> it will take to completely reload the weapon.

#### Reload_Shoot_Delay:
The amount of time in <A HREF="#delay">ticks</A> before the player can fire the weapon _after_ the reload has been successfully completed.

#### Destroy_When_Empty:
If set to true, reloading the weapon will not be possible and the weapon will destroy itself as soon as its ammo-reading hits 0.

#### Sounds_Out_Of_Ammo:
The <A HREF="#sounds">sound(s)</A> played as soon as the ammo-reading on the weapon hits 0. 

Note: _Not_ to be confused with `Sounds_Out_Of_Ammo:` of the `Ammo:` module, which refers to the sound that is played when the player's _inventory_ runs out of physical ammunition.

#### Sounds_Reloading:
The <A HREF="#sounds">sound(s)</A> played when the weapon is being reloaded.

#### Dual_Wield:
There is a special case for reloading _dual wielded_ weapons. For example: if both weapons are empty, then you would obviously reload both. But what if only one weapon is empty? You would only reload one of the weapons, which would take significantly less time than reloading both weapons at once.

* **Single_Reload_Duration:**
    * The amount of time in <A HREF="#delay">ticks</A> it will take to reload one of the weapons.
* **Sounds_Single_Reload:**
    * The <A HREF="#sounds">sound(s)</A> played when a single weapon is being reloaded.
* **Sounds_Shoot_With_No_Ammo:**
    * The <A HREF="#sounds">sound(s)</A> played when the player attempts to fire one of the weapons that is out of ammo.

## **░ Firearm actions** <A NAME="firearm">
    Firearm_Action:
        Type: <slide/bolt/lever/pump/break/revolver>
        Open_Duration: <ticks>
        Close_Duration: <ticks>
        Close_Shoot_Delay: <ticks>
        Reload_Open_Delay: <ticks>
        Reload_Close_Delay: <ticks>
        Sound_Open: <sound>,(...)
        Sound_Close: <sound>,(...)

#### Type:
Input one of the six acceptable values below. Specifying a firearm-action is not compulsory.

* `slide`
    * Introduces the _slide mechanism_ or _charging handle_. The weapon will have two states: unlocked `■` and locked `□`. If the weapon runs out of ammo, the bolt will be locked to the rear `■ ➙ □`. In order to shoot again, not only will the weapon need to be reloaded, it will need to have the bolt moved back into its original position `□ ➙ ■`.

* `bolt` or `lever`
    * Bolt-action or lever-action. Introduces three states to the weapon: bullet in firing chamber `■`, cartridge-case in firing chamber `□`, and empty firing chamber `_`. Every time a bullet is fired, the bolt/lever is opened and closed to re-chamber a new round. Furthermore, the weapon can only be reloaded when the bolt/lever is in the _open_ position `_`.

* `pump`
    * Pump-action. Exactly the same as `bolt` and `lever` except the weapon does not have to be opened `_` for a reload to occur. Suitable for shotguns, as you basically insert shells directly into the weapon.

* `break` or `revolver`
    * Upon reload, the weapon must be opened `□` and then closed `■` after the reload is complete. Suitable for, as you would have guessed, break-action shotguns, "noob-tubes" and revolvers.

Note: Selecting _pump_, _bolt_, or _lever_ will use the <A HREF="#delay">delays</A> provided in `Open_Duration`, `Close_Duration` and `Close_Shoot_Delay` to determine the weapon's rate of fire _instead_ of the value provided in `Delay_Between_Shots:`.

#### Open_Duration:
The <A HREF="#delay">duration</A> of the (bolt/lever/pump/...) opening.

Note: For the _HK slap_ method of reloading, this node _can_ used by `slide` weapons.

#### Close_Duration:
The <A HREF="#delay">duration</A> of the (bolt/lever/pump/slide/...) closing.

#### Close_Shoot_Delay:
The <A HREF="#delay">delay</A> until the weapon can be fired again _after_ the bolt, lever, pump or slide closes.

#### Reload_Open_Delay:
(Optional) This node represents the <A HREF="#delay">delay</A> before the [reloading](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#reload) of the weapon begins _after_ the weapon is readied `■ ➙ □`.

#### Reload_Close_Delay:
(Optional) This node represents the <A HREF="#delay">delay</A> before the closing `□ ➙ ■` of the weapon begins _after_ the completion of a successful [reload](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#reload).

#### Sound_Open:
The <A HREF="#sounds">sound(s)</A> of the (...) opening.

#### Sound_Close:
The <A HREF="#sounds">sound(s)</A> of the (...) closing.

## **░ Scope** <A NAME="scope">
    Scope:
        Enable: <true/false>
        Night_Vision: <true/false>
        Zoom_Amount: <amount>
        Zoom_Bullet_Spread: <amount>
        Zoom_Before_Shooting: <true/false>
        Sounds_Toggle_Zoom: <sound>,(...)

#### Enable:
Whether or not scopes or iron sights should be enabled on the weapon.

#### Night_Vision:
Whether or not the scope is a night-vision scope.

#### Zoom_Amount:
The amount of zoom the scope offers. A value between 1-5 is recommended.

#### Zoom_Bullet_Spread:
The amount of spread the fired projectile should have upon being fired.

Note: This node supports **decimal values**, such as _2.354_, _0.22556_ or _3.5_.

#### Zoom_Before_Shooting:
If `true`, the player can _only_ shoot if zoomed in.

#### Sounds_Toggle_Zoom:
The <A HREF="#sounds">sound(s)</A> played when the player zooms in.

## **░ Riot shields** <A NAME="shield">
    Riot_Shield:
        Enable: <true/false>
        Do_Not_Block_Projectiles: <true/false>
        Do_Not_Block_Melee_Attacks: <true/false>
        Durability_Based_On_Damage: <true/false>
        Durability_Loss_Per_Hit: <amount>
        Forcefield_Mode: <true/false>
        Only_Works_While_Blocking: <true/false>
        Sounds_Blocked: <sound>,(...)
        Sounds_Break: <sound>,(...)

#### Enable:
If `true`, allows riot shields to be used. Riot shields are shields that can completely block certain attacks under certain conditions.

#### Do_Not_Block_Projectiles:
If `true`, the shield will not block ranged attacks when raised.

#### Do_Not_Block_Melee_Attacks:
If `true`, the shield will not block melee attacks when raised.

#### Durability_Based_On_Damage:
If `true`, `Durability_Loss_Per_Hit:` will take into account the amount of <A HREF="#damage">damage</A> the player has blocked.

Example: A player is holding a certain shield that has `Durability_Loss_Per_Hit: 10` and `Durability_Based_On_Damage: true`. This player successfully uses the shield to block 4 units of damage. The shield will have `4X10` units of durability deducted from it.

#### Durability_Loss_Per_Hit:
The amount of durability that will be deducted from the shield per _hit_ or _unit of damage_ (depending on whether `Durability_Based_On_Damage` is `true`.

#### Forcefield_Mode:
If `true`, the riot shield will block attacks from every direction when raised, including attacks directed towards the back of the player. The player will no longer need to face the threat.

#### Only_Works_While_Blocking:
If `true`, the riot shield will only block attacks when the player is _blocking_. In Minecraft 1.8, blocking is performed by right-clicking with a sword. In Minecraft 1.9 and above, blocking is performed by right-clicking with a shield.

#### Sounds_Blocked:
The <A HREF="#sounds">sound(s)</A> played whenever the shield successfully blocks an attack.

#### Sounds_Break:
The <A HREF="#sounds">sound(s)</A> played when the shield runs out of durability and breaks.

## **░ Weapon stores** <A NAME="stores">
    SignShops:
        Enable: <true/false>
        Price: <itemID-amount> OR <itemID~data-amount>
        Sign_Gun_ID: <unique number>

#### Enable:
Whether or not a store for this weapon is able to be created and purchased from.

#### Price:
Specify the <A HREF="#itemID">item-type</A> and amount required for a successful transaction. Supports secondary data values - `351~9-5` would equal 5 _Pink Dyes_.

Example: A weapon named `Volleyball` has `Price: 266-12`. `266` is the <A HREF="#itemID">ID</A> for _Gold Ingot_, thus, purchasing a `Volleyball` from a store will cost 12 _Gold Ingots_.

#### Sign_Gun_ID:
This must be a _unique_ number from 1-999. There should not be more than one weapon in the configuration that shares the same `Sign_Gun_ID:` value.

#### Setting up a store:
Simply place a sign. In the first line, type `[CS]<number>`, where `<number>` is the weapon's `Sign_Gun_ID:` value (a value between 1 and 999). As long as this first line is correct, and the player has permission to create a store, the player will be receive a `Shop successfully created` message when the sign has been finalized. You may type _anything_ in the 2nd, 3rd and 4th line.

Note: Players in creative-mode cannot purchase from stores. In order to remove a shop sign, you must be in creative-mode, and you must have the permission to do so - `crackshot.store.<weapon>/all`.

![alt text](http://i.imgur.com/1Zz1dJG.png "Before")

This sign will use the shop configured in the <a href="https://github.com/Shampaggon/CrackShot/wiki/Default-weapons" target="_blank">default weapon</a> _Type 95_. Note that "&e" is the <A HREF="#colors">color code</A> for _yellow_. You can only color your lines if you have a plugin that handles colored-signs.

![alt text](http://i.imgur.com/vN7zFQi.png "After")

Given that the creation was successful, this will be the final result.

## **░ Custom crafting recipes** <A NAME="crafting">
    Crafting:
        Enable: <true/false>
        Quantity: <amount>
        Shaped: <true/false>
        Ingredients: <ingredients>

#### Enable:
If `true`, allows the weapon to be crafted using the custom recipe provided by the user. Remember, players will still need permission `crackshot.craft.<weapon>` to craft the weapon.

#### Quantity:
The number of items that this crafting recipe will _output_. Defaults to 1.

#### Shaped:
Do the items need to be placed in certain slots for this to work (shaped)? Or can they be placed anywhere (not shaped)? If `Shaped: true`, you _must_ provide all 9 values.

#### Ingredients:
The ingredients, with each slot (from 1-9) containing a certain amount of an <A HREF="#itemID">item</A>.

![alt text](http://i.imgur.com/Lwz1O73.png "Custom crafting recipe")

Example 1: Assume that `Shaped:` is `true` for this recipe. Keep in mind that **30** is the <A HREF="#itemID">_item ID_</A> for _Web_, and **98~2** is the <A HREF="#itemID">_item ID_</A> for _Cracked Stone Bricks_. The recipe for the image above would be: `Ingredients: 30,0,98~2,0,30,0,98~2,98~2,30`. All 9 values must be provided, as it is a _shaped_ recipe. The value of an empty slot is `0`.

![alt text](http://i.imgur.com/oRISnnD.png "Custom crafting recipe")

Example 2: Assume that `Shaped:` is `false` for this recipe. The recipe for the image above would be: `Ingredients: 30,30,1`. You do not need to provide all 9 values, and the order of the items placed on the crafting grid _does not_ matter, as it is an _unshaped_ recipe. Furthermore, `Ingredients: 1,30,30` is the same as `Ingredients: 30,30,1` is the same as `Ingredients: 30,1,30` and so on.

#### Advanced usage:
If you are interested in using _CrackShot_ weapons as viable ingredients, you will have to use _secondary data values_. For instance:

    Hunting_Rifle:
        Item_Information:
            Item_Type: 280~1
    
    Hunting_Rifle_Part:
        Item_Information:
            Item_Type: 280~2
    
    Uber_Hunting_Rifle:
        Item_Information:
            Item_Type: 280~3
        Crafting:
            Enable: true
            Shaped: false
            Ingredients: 280~1,280~2

From the simplified example above, you will be able to craft an *Uber_Hunting_Rifle* using *Hunting_Rifle_Part* and *Hunting_Rifle*.

⚠ Note: When using secondary data values to individualize weapons, avoid _block items_ (unless you know what you are doing) and _durability items_. You will find information about those types of items in the <A HREF="#item_info">_Item Information_</A> section of the guide.

## **░ Region checks** <A NAME="regions">
    Region_Check:
        Enable: <true/false>
        World_And_Coordinates: <worldname,X1,Y1,Z1,X2,Y2,Z2,blacklist>|(...)
        Message_Of_Denial: <message>

#### Enable:
If true, the **weapon and its projectiles** will only be functional if the player or projectile is within/outside the region(s) specified. Useful if you want to restrict the usage of weapons to certain arenas.

Clarification: Weapons will not function if it does not pass the region check. Its _projectiles_ will also fail to function. For example, if you fired a _Bazooka_ or threw a _Grenade_ from outside of a restricted region, the projectile will not explode if it lands inside the restricted region.

Note: Projectiles using the *Break_Blocks* node will fail to destroy blocks inside a restricted region.

#### World_And_Coordinates:
Specify the world name. This is generally the name of the world's folder (e.g. The End is usually world_the_end). Follow this by the X,Y,Z coordinates of point 1 and point 2. Finally, specify whether or not the region is a blacklist with _true_ or _false_. You may specify _multiple regions_ by separating each region with a vertical bar `|`.

Note: Supports _decimal values_ such as `-356.217`, but their use is discouraged. Blacklisted regions will also override whitelisted regions should the two regions overlap.

Examples:
* `World_And_Coordinates: world,0,0,0,200,200,200,true` - A region blacklist. The weapon cannot be used inside the defined region, but can be used outside of it.
* `World_And_Coordinates: world,0,0,0,200,200,200,false` - A region whitelist. The weapon can only be used inside the define region, and cannot be used outside of it.
* `World_And_Coordinates: world,0,0,0,200,200,200` - Same as the example above. If true or false is not provided for the `blacklist` variable, it will default to _false_ and become a region whitelist.

#### Message_Of_Denial:
The message the player will receive upon being rejected. Does _not_ support any <A HREF="#variables">variables</A>.

## **░ Custom death messages** <A NAME="death_messages">
    Custom_Death_Message:
        Normal: <message>
        H̶e̶a̶d̶s̶h̶o̶t̶:̶

#### Normal:
The message that will be broadcasted to the entire server when a victim is killed by this weapon. These messages _do not_ support the variables `<flight>` and `<damage>`.

#### Headshot:
This feature has not yet been added, but will aim to broadcast a different message if the victim was killed by a headshot.

## **░ Headshots** <A NAME="headshot">
    Headshot:
        Enable: <true/false>
        Bonus_Damage: <amount>
        Message_Shooter: <message>
        Message_Victim: <message>
        Sounds_Shooter: <sound>,(...)
        Sounds_Victim: <sound>,(...)

#### Enable:
Whether or not headshots should be taken into consideration. Applies only to _projectiles_.

#### Bonus_Damage:
How much extra <A HREF="#damage">damage</A> a headshot will deal.

#### Message_Shooter:
The <A HREF="#variables">message</A> the shooter will receive upon delivering a headshot.

#### Message_Victim:
The <A HREF="#variables">message</A> the victim will receive upon receiving a headshot.

#### Sounds_Shooter:
The <A HREF="#sounds">sound(s)</A> played at the shooter upon delivering a headshot.

#### Sounds_Victim:
The <A HREF="#sounds">sound(s)</A> played at the victim upon receiving a headshot.

## **░ Backstabs** <A NAME="backstabs">
    Backstab:
        Enable: <true/false>
        Bonus_Damage: <amount>
        Message_Shooter: <message>
        Message_Victim: <message>
        Sounds_Shooter: <sound>,(...)
        Sounds_Victim: <sound>,(...)

#### Enable:
Whether or not backstabs should be taken into consideration. Applies to _projectiles_ and weapons with _melee mode_.

#### Bonus_Damage:
How much extra <A HREF="#damage">damage</A> shooting an entity in the back will deal.

#### Message_Shooter:
The <A HREF="#variables">message</A> the shooter will receive upon delivering a backstab.

#### Message_Victim:
The <A HREF="#variables">message</A> the victim will receive upon receiving a backstab.

#### Sounds_Shooter:
The <A HREF="#sounds">sound(s)</A> played at the shooter upon delivering a backstab.

#### Sounds_Victim:
The <A HREF="#sounds">sound(s)</A> played at the victim upon receiving a backstab.

## **░ Critical hits** <A NAME="Cr1TiKaL">
    Critical_Hits:
        Enable: <true/false>
        Bonus_Damage: <amount>
        Chance: <percentage>
        Message_Shooter: <message>
        Message_Victim: <message>
        Sounds_Shooter: <sound>,(...)
        Sounds_Victim: <sound>,(...)

#### Enable:
Whether or not critical hits should be taken into consideration. Applies to _projectiles_ and weapons with _melee mode_.

#### Bonus_Damage:
How much extra <A HREF="#damage">damage</A> a critical hit will deal.

#### Chance:
The percentage chance that the shooter will score a critical hit. Must be a value from 1-100, where 100 means a 100% chance of success.

Example: `Chance: 25` will mean that the weapon will have a 25% chance of scoring a critical hit.

#### Message_Shooter:
The <A HREF="#variables">message</A> the shooter will receive upon delivering a critical hit.

#### Message_Victim:
The <A HREF="#variables">message</A> the victim will receive upon receiving a critical hit.

#### Sounds_Shooter:
The <A HREF="#sounds">sound(s)</A> played at the shooter upon delivering a critical hit.

#### Sounds_Victim:
The <A HREF="#sounds">sound(s)</A> played at the victim upon receiving a critical hit.

## **░ Summon entities** <A NAME="entity">
    Spawn_Entity_On_Hit:
        Enable: <true/false>
        Chance: <percentage>
        Mob_Name: <name>
        EntityType_Baby_Explode_Amount: <entity-baby-explode-amount>,(...)
        Make_Entities_Target_Victim: <true/false>
        Timed_Death: <ticks>
        Entity_Disable_Drops: <true/false>
        Message_Shooter: <message>
        Message_Victim: <message>

#### Enable:
Whether or not entities will be spawned when:
* a projectile fired by the weapon strikes an enemy
* an explosion caused by the weapon damages an enemy

#### Chance:
The percentage chance that entities will be spawned when the enemy is hit. Must be a value from 1-100, where 100 means a 100% chance of success.

#### Mob_Name:
The name of the spawned mobs. This node is optional.

#### EntityType_Baby_Explode_Amount:
Specify the <a href="https://github.com/Shampaggon/CrackShot/wiki/List-of-Accepted-Mobs" target="_blank">entity type</a>, whether or not it is a baby, whether or not it will explode upon death, and the amount. You can spawn more than one type of entity by separating them with a comma `,`.

Example: `EntityType_Baby_Explode_Amount: PIG-TRUE-TRUE-4` will spawn 4 baby pigs that explode upon death.

Note: An entity that explodes upon death will create an explosion with a radius of 2 (half that of TNT). Furthermore, setting _baby_ to _true_ on a _Creeper_ would turn that Creeper into a _Powered Creeper_.

Trivia: Did you know that _zombies_ and _zombie pigmen_ have baby forms?

#### Make_Entities_Target_Victim:
This node is _deprecated_ and may cause mobs to sink into the ground. If `true`, will attempt make the spawned entities target the victim.

#### Timed_Death:
The time in ticks that the spawned entities will live for before dying.

#### Entity_Disable_Drops:
If `true`, the spawned entities will not drop any items or experience orbs upon death.

#### Message_Shooter:
The <A HREF="#variables">message</A> the shooter will receive upon successfully spawning entities at the victim's position.

#### Message_Victim:
The <A HREF="#variables">message</A> the victim will receive if entities were successfully spawned.

## **░ Flight time** <A NAME="flight_time">
    Damage_Based_On_Flight_Time:
        Enable: <true/false>
        Bonus_Damage_Per_Tick: <amount>
        Minimum_Damage: <amount>
        Maximum_Damage: <amount>

#### Enable:
Whether or not the flight-time of the projectile should be taken into consideration upon calculating the total damage dealt to a victim.

Uses: Projectiles can be made to deal much more damage the longer it stays in the air, discouraging players from attempting to shoot enemies point-blank. By setting `Bonus_Damage_Per_Tick:` to a negative value, and not providing a value for `Minimum_Damage`, the range of a weapon can be severely limited; _perfect_ for short-ranged shotguns.

#### Bonus_Damage_Per_Tick:
The extra <A HREF="#damage">damage</A> the projectile will deal upon striking a target after each tick. Can be set to a negative value to reduce damage the longer the projectile stays airborne.

#### Minimum_Damage:
The minimum bonus <A HREF="#damage">damage</A> the projectile must exceed to deal any bonus damage at all.

Example: A weapon has `Minimum_Damage: 10` and `Bonus_Damage_Per_Tick: 2`. The weapon fires a projectile that travels for 4 ticks before striking an enemy. During this time, it had gathered a total damage of 8 units. Since 8 falls below the minimum damage of 10, no bonus damage is added to the total damage dealt.

#### Maximum_Damage:
The maximum bonus <A HREF="#damage">damage</A> the projectile can gain or lose.

Example: A weapon has `Maximum_Damage: 5` and `Bonus_Damage_Per_Tick: 2`. The weapon fires a projectile that travels for 4 ticks before striking an enemy. During this time, it had gathered a total damage of 8 units. Since 8 exceeds the maximum damage of 5, only 5 units of bonus damage is added to the total damage dealt.

Note: If the value provided in `Bonus_Damage_Per_Tick` is negative, this node can be used to limit the amount of damage to be _deducted_! For example, having `Maximum_Damage: -4` and `Bonus_Damage_Per_Tick: -1` will cause the projectile to deal 1 less unit of damage for every tick it is airborne until 4 ticks have elapsed.

## **░ Airstrikes** <A NAME="airstrikes">
    Airstrikes:
        Enable: <true/false>
        Flare_Activation_Delay: <ticks>
        Particle_Call_Airstrike: <particle-effect>,(...)
        Message_Call_Airstrike: <message>
        Block_Type: <itemID> OR <itemID~data>
        Area: <amount>
        Distance_Between_Bombs: <amount>
        Height_Dropped: <amount>
        Vertical_Variation: <amount>
        Horizontal_Variation: <amount>
        Multiple_Strikes:
            Enable: <true/false>
            Number_Of_Strikes: <amount>
            Delay_Between_Strikes: <ticks>
        Sounds_Airstrike: <sound>,(...)

#### Enable:
If `true`, an airstrike will be called whenever a player is struck by an ordinary projectile (snowball, egg, arrow) or when a `flare` is thrown and activated.

#### Flare_Activation_Delay:
If `Projectile_Type:` is set to `flare`, this node will represent the <A HREF="#delay">delay</A> in ticks before the thrown flare will call in an airstrike.

#### Particle_Call_Airstrike:
The <A HREF="#particles">particle effect(s)</A> created when a thrown flare or projectile calls in an airstrike. Visit the <A HREF="#particles">Particles</A> module for more information on how particle-effects are formatted.

#### Message_Call_Airstrike:
The message the _caller of the airstrike_ will receive when an airstrike is called. The only <A HREF="#variables">special variable</A> this node supports is `<shooter>`, which represents the caller of the airstrike.

#### Block_Type:
The <A HREF="#itemID">_item ID_</A> of the dropped bombs. These item IDs must be _blocks_. Secondary data values are supported.

Example: Setting `Block_Type:` to `35~4` will cause the airstrike to drop _Yellow Wool_ as bombs.

#### Area:
Airstrikes drop a _square grid of bombs_ with a certain dimension. This node represents the area of that grid.

Setting `Area:` to `5` will cause the airstrike to drop `5 X 5 = 25` bombs per strike. Setting `Area:` to `2` will cause the airstrike to drop `2 X 2 = 4` bombs per strike, and so on.

#### Distance_Between_Bombs:
The distance in blocks between each bomb.

Examples: Setting this node to `0` will pack all the bombs into a single solid unit. Setting this node to `4` will space every individual bomb four blocks apart.

#### Height_Dropped:
The height in blocks _relative_ to the point of calling from which the bombs will be dropped.

Example: Setting this node to `100 ` will spawn the bombs 100 blocks above the position of the flare or projectile's point of activation.

#### Vertical_Variation:
The degree of vertical variation, in blocks, between the bombs. This node serves to randomize the nature of the strike.

#### Horizontal_Variation:
The degree of horizontal variation, in blocks, between the bombs. This node serves to randomize the nature of the strike.

#### Multiple_Strikes:
* _Enable:_ - Whether or not there will be _multiple_ strikes.
* *Number_Of_Strikes:* - The number of strikes.
* *Delay_Between_Strikes:* - The <A HREF="#delay">delay</A> in ticks between each strike.

#### Sounds_Airstrike:
The <A HREF="#sounds">sound(s)</A> played whenever an airstrike is called.

## **░ Explosive devices** <A NAME="devices">
    Explosive_Devices:
        Enable: <true/false>
        Device_Type: <landmine> OR <remote> OR <trap> OR <itembomb>
        Device_Info: <information>
        Sounds_Deploy: <sound>,(...)
        Remote_Bypass_Regions: <true/false>
        Message_Disarm: <message>
        Message_Trigger_Placer: <message>
        Message_Trigger_Victim: <message>
        Sounds_Alert_Placer: <sound>,(...)
        Sounds_Trigger: <sound>,(...)

#### Enable:
If `true`, the weapon will become an explosive device. For:

* _landmines_ - the act of shooting will involve planting a mine.

* _remote-detonated explosives_ - the act of shooting will involve placing an explosive mob-head.

* _trap_ - traps are items with the following qualities:
    * Place this in a dispenser; triggering the dispenser will result in an explosion.
    * Place this in a chest; opening the chest will result in an explosion.
    * Drop this item onto the ground; picking it up will result in an explosion.
    * Place this in an item frame; pressure-plates within 4 blocks that are stepped on will result in an explosion.
    * **Owners cannot trigger their own traps**.

* _item bombs_ - the act of shooting will involve throwing an item-bomb.

Note: This module takes information from the _Explosions_ module to determine the nature of the explosion.

#### Device_Type:
There are currently 4 supported values:

* _landmine_ - Deploys a minecart that will explode upon contact with enemies. These mines are _permanent_ - they will be active even after server restarts - and will also explode if shot by projectiles. Given that the placer is _online_ at the time, friendly-fire checking is implemented, allowing the mine to distinguish between enemies and teammates in environments managed by other plugins, such as _Factions_ or _PVPArena_. These mines can be used to guard personal property, and can be non-lethal or deadly depending on how you configure it.

* _remote_ - Places an explosive mob-head (Steve) that can be remotely detonated from _any_ world, from _any_ position on the map. Friendly-fire checking is implemented - enemies attempting to break the device will set it off, while allies will not be able to break the device at all. These devices will be disarmed when broken by the person who placed it. Inherits the building properties of the item specified in the *Item_Type* node of the *Item_Information* module, so make sure it's a placeable block! **Compatible with the Ammo module and the One_Time_Use node.**

* _trap_ - An item which will explode when a chest containing the item is opened, when shot out of a dispenser or when picked up by enemies. A trap will not work until a player has given it an owner by _activating_ it. Owners will not be able to trigger their own traps. As usual, friendly-fire checking is implemented as long as the owner is online at the time - allies who attempt to pick up the item or open a chest containing the item will not trigger the device. Note that traps will never run out when fired from dispensers.
    * Pressure-plate mines - _traps_ have one unique property: when placed in an item frame, all pressure-plates within 4 blocks will generate an explosion whenever they are stepped on.

* _itembomb_ - Throws an item that can be remotely detonated from _any_ world, from _any_ position on the map. The thrown item-bombs despawn when the player responsible for throwing them _leaves the server_. All item-bombs are removed upon server restarts. **Compatible with the Ammo module and the One_Time_Use node.**

#### Device_Info:
The value for this node differs depending on the device type. For:

* _landmine_ - Assumes the following format: `<itemID-minecartType>`.
    * `itemID` represents the <A HREF="#itemID">_item ID_</A> of the _fuse_ (the passenger of the minecart). All mines must carry a valid fuse, so a value is required. Supports secondary data values - a value of _35_ would represent _Wool_, while a value of _35~6_ would represent _Pink Wool_.
    * `minecartType` represents the minecart type. The following types are currently supported: MINECART, MINECART_CHEST, MINECART_FURNACE, MINECART_HOPPER, MINECART_MOB_SPAWNER and MINECART_TNT. This setting should be used by plugin developers only; the inherent properties of other minecart types are not blocked.

* _remote_ - This node assumes the following format: `Amount-UniqueID-Headname`.
    * `Amount` determines the maximum number of remote-detonated explosives the weapon can handle.
    * `UniqueID` must be two characters long, and must contain a value _unique_ to the weapon - no other `remote`-type weapon should share the same value. `UniqueID` can contain numbers as well as letters of the alphabet. Not that letters are case insensitive; `1A` is the same as `1a`.
    * `Headname` is the player-name that the mob-head will use upon being triggered. It is not possible to specify the player-name of the mob-head _before_ it is triggered; it will always be a _Steve_ head.

* _trap_ - This node assumes the following format: `Chest-Pickup-DispenserAndPressurePlate-Reusable-NoItemDespawn`. Each value requires a simple _true_ or _false_.
    * `Chest` - whether or not the trap will be triggered when a chest containing the item is _opened_.
    * `Pickup` - whether or not the trap will be triggered when the dropped item is picked up.
    * `DispenserAndPressurePlate` - whether or not the trap will be triggered when the item is fired from a dispenser or triggered by a pressure plate within four blocks of a trap mounted on an item frame.
    * `Reusable` - if set to _true_ will make traps _never_ run out (dropped items can be triggered more than once, and so forth). 
    * `NoItemDespawn` - if set to _true_ will cause the dropped item to _never_ despawn - useful for minefields that are composed of dropped item-traps.

* _itembomb_ - This node assumes the following format: `Amount,Speed,Before,After`.
    * `Amount` determines the maximum number of item bombs the player can throw. This limit will be impossible to exceed, even if a player has multiple instances of the same `itembomb` weapon!
    * `Speed` determines the speed at which the item bomb is thrown.
    * `Before` represents the <A HREF="#itemID">_item ID_</A> of the item bomb when inert. Secondary data values are supported.
    * `After` represents the <A HREF="#itemID">_item ID_</A> of the item bomb when triggered. Secondary data values are supported.

Examples: 
* If *Device_Type* is set to `remote`, inputting `4-T7-Notch` will create a device that can place and store up to 4 explosives that will turn into Notch-heads upon activation.
* If *Device_Type* is set to `itembomb`, inputting `2,10,159,159~14` will create a device that can throw up to 2 item bombs with a speed of 10. These item bombs will look like _White Stained Clay_ (159), but when triggered, will look like _Red Stained Clay_ (159:14).

#### Sounds_Deploy:
The <A HREF="#sounds">sound(s)</A> played when the device is deployed. For:

* _landmine_ - This sound will be played when the mine is placed.

* _remote_ - This sound will be played when an explosive mob-head is placed.

* _trap_ - This sound will be played when the device is first activated by a player.

* _itembomb_ - This sound will be played when an item bomb is thrown.

#### Remote_Bypass_Regions:
Used only for `remote`-type devices. Setting this node to `true` will bypass all region-protection plugins and allow the placement and removal of remote-detonated explosives _anywhere_.

#### Message_Disarm:
Used only for `remote`-type devices. This will represent the message the _placer_ of the device will receive when breaking and disarming devices that he himself has placed. Supports no <A HREF="#variables">special variables</A>.

#### Message_Trigger_Placer:
The message the _placer_ of the device will receive when the device is triggered. Supports all <A HREF="#variables">special variables</A> except for `<flight>` and `<damage>`.

#### Message_Trigger_Victim:
The message the victim will receive upon triggering an explosive device, such as bumping into a landmine, breaking someone's remote-detonated explosive, or opening a chest containing a booby trap. Supports all <A HREF="#variables">special variables</A> except for `<flight>` and `<damage>`.

#### Sounds_Alert_Placer:
The <A HREF="#sounds">sound(s)</A> the _owner of the device_ hears when the device is triggered. For:

* _landmine_ - This sound will be played when the mine is triggered by an enemy, alerting the mine-placer to possible victims.

* _remote_ - This sound will be played when a remote-detonated explosive is manually activated by the placer, or when the explosive is set off by someone trying to break it.

* _trap_ - This sound will be played when a booby trap is triggered by either a player opening a chest containing a booby trap, a victim stepping on a pressure-plate within four blocks of an item-frame booby trap, or a player picking up a booby trap item.

* _itembomb_ - This sound will be played when the item bomb is activated by the thrower.

#### Sounds_Trigger:
The <A HREF="#sounds">sound(s)</A> the device makes when triggered. For:

* _landmine_ - This sound will be emitted by the mine when an enemy triggers it.

* _remote_ - This sound will be emitted by the explosive when manually activated by the placer, or when an enemy tries to break it.

* _trap_ - This sound will be emitted by the trap when an enemy opens a chest containing the trap, an enemy picks up a booby trap item, an enemy steps on a pressure-plate within four blocks of an item-frame booby trap, or when the trap is shot out of a dispenser.

* _remote_ - This sound will be emitted by the item bomb when activated by the thrower.

## **░ Cluster bombs** <A NAME="cluster">
    Cluster_Bombs:
        Enable: <true/false>
        Bomblet_Type: <itemID> OR <itemID~data>
        Delay_Before_Split: <ticks>
        Number_Of_Splits: <amount>
        Number_Of_Bomblets: <amount>
        Speed_Of_Bomblets: <amount>
        Delay_Before_Detonation: <ticks>
        Detonation_Delay_Variation: <ticks>
        Particle_Release: <particle-effect>,(...)
        Sounds_Release: <sound>,(...)

#### Enable:
If set to `true`, _all_ explosions caused by the weapon will release cluster bombs (with the exception of the explosions caused by <A HREF="#airstrikes">_airstrikes_</A>). Uses the _Explosions_ module to determine the nature of the bomblet-explosions.

Clarification: Yes, this module can be used for landmines, remote-detonated devices, grenades, booby traps - everything that explodes except for airstrikes. "Oh, but why no airstrike?!" - because frankly, if every bomb of an airstrike were to split and release bomblets, one's computer would probably implode.

#### Bomblet_Type:
The <A HREF="#itemID">_item ID_</A> of the released bomblets. Secondary data values are supported.

#### Delay_Before_Split:
This node represents the <A HREF="#delay">delay</A> in ticks before a cluster bomb _splits_ and releases its bomblets.

#### Number_Of_Splits:
This node represents the number of times the cluster bomb will split.

Note: The amount of bomblets released is calculated by *Number_Of_Bomblets* to the power of *Number_Of_Splits*. This means having a value of 6 for `Number_Of_Splits` and a value of 5 for `Number_Of_Bomblets` will equate to a total of 15,625 (5⁶) bomblets and consequent explosions!

For your own safety, CrackShot will reject cluster bombs that release over 1000 bomblets in total.

#### Number_Of_Bomblets:
The number of bomblets a single cluster bomb will release.

#### Speed_Of_Bomblets:
The speed of the released bomblets. The higher the value, the further these bomblets will travel away from the point of release.

#### Delay_Before_Detonation:
The delay before the released bomblets _explode_.

Clarification: Cluster bombs _do not_ use the `Explosion_Delay:` node from the `Explosions` module.

#### Detonation_Delay_Variation:
If you do not want all of the bomblets to explode all at once, you can use this node to vary the delay by a specified amount. This node serves to randomize the nature of the explosions.

Example: `Delay_Before_Detonation:` is set to 40 (2 seconds). `Detonation_Delay_Variation:` is set to 20 (1 second). This means the bomblets will have a delay of 2±1 seconds before exploding.

#### Particle_Release:
The <A HREF="#particles">particle effect(s)</A> created when a cluster bomb _splits_ and releases its bomblets. Visit the <A HREF="#particles">Particles</A> module for more information on how particle-effects are formatted.

#### Sounds_Release:
The <A HREF="#sounds">sound(s)</A> played when a cluster bomb _splits_ and releases its bomblets.

## **░ Shrapnel** <A NAME="shrapnel">
    Shrapnel:
        Enable: <true/false>
        Block_Type: <itemID> OR <itemID~data>
        Amount: <amount>
        Speed: <amount>
        Place_Blocks: <true/false>

#### Enable:
If set to `true`, _all_ explosions caused by the weapon will release blocks of "shrapnel".

#### Block_Type:
The <A HREF="#itemID">_item ID_</A> of the dropped bombs. These item IDs must be _blocks_. Secondary data values are supported.

Example: Setting `Block_Type:` to `35~4` will use _Yellow Wool_ as the shrapnel.

#### Amount:
The number of shrapnel released. As always, try to provide an _appropriate_ value.

#### Speed:
The speed of the released shrapnel. The larger the value, the further away from the explosion the shrapnel will travel.

#### Place_Blocks:
If set to `true`, the shrapnel-blocks will place themselves upon landing. If you had ever wanted an explosion that dispersed water, lava, fire and so forth, then this node is right for you.

## **░ Explosions** <A NAME="kaboom">
    Explosions:
        Enable: <true/false>
        Knockback: <amount>
        Ignite_Victims: <ticks>
        Damage_Multiplier: <percentage>
        Enable_Friendly_Fire: <true/false>
        Enable_Owner_Immunity: <true/false>
        Explosion_No_Damage: <true/false>
        Explosion_Potion_Effect: <potioneffect>,(...)
        Explosion_No_Grief: <true/false>
        Explosion_Radius: <amount>
        Explosion_Incendiary: <true/false>
        Explosion_Delay: <ticks>
        On_Impact_With_Anything: <true/false>
        Projectile_Activation_Time: <ticks>
        Message_Shooter: <message>
        Message_Victim: <message>
        Sounds_Shooter: <sound>,(...)
        Sounds_Victim: <sound>,(...)
        Sounds_Explode: <sound>,(...)

#### Enable:
If `true`, enables explosions for the weapon. This module applies to _all_ projectile-types, airstrikes, cluster bombs and <A HREF="#devices">explosive devices</A>.

Note: These explosions are compatible with all region-protection plugins such as WorldGuard, Factions, and Towny. If a projectile lands in a region where explosions are disabled, it _will_ be cancelled.

★ _CrackShot_ explosions have advanced friendly-fire checking. Teammates will not be damaged by your explosions.

#### Knockback:
Provide a value that determines the amount of knockback the explosion will deliver. Negative values are supported.

Example: Giving this node a value of `-10` will cause an _implosion_ that pulls everything towards the center.

#### Ignite_Victims:
If the given value is greater than zero, the explosion will set victims on fire. Provide a <A HREF="#delay">duration</A> that determines how long the victims should stay alight for.

Note: This node is _not_ to be confused with `Explosion_Incendiary:`, which sets _destroyed_ blocks on fire.

#### Damage_Multiplier:
The percentage to multiply the explosion's damage by.

Example: A value of `50` would cause the explosion to deal half damage (50%). A value of `200` would cause the explosion to deal double damage (200%). Please note that you cannot _completely_ nullify the damage of the explosion by giving this node a value of `0` (0%).

#### Enable_Friendly_Fire:
If `true`, explosions will damage your teammates. In team-based arenas managed by plugins such as _MobArena_ and _PVP Arena_, it is generally a good idea to leave this node `false` to prevent team-killing.

Note: Setting this node to `true` is _heavily discouraged_, and may cause the explosions to ignore most of the settings in the `Explosions:` module.

#### Enable_Owner_Immunity:
If `true`, the shooter (the person who _caused_ the explosion) will not be damaged by the explosion, and will not receive any potion-effects (if provided) from the explosion.

#### Explosion_No_Damage:
If `true`, the explosion will not deal any damage. This is useful for tactical grenades such as _flashbangs_ or _gas grenades_, which do not deal any damage but apply potion-effects.

#### Explosion_Potion_Effect:
The potion-effect(s) given to victims who are fully exposed to the explosion - enemies taking shelter behind obstacles will be safe. Please refer to the <A HREF="#potions">Potion effects</A> section for setting up potion-effects, or have a look at the _Flashbang_ <a href="https://github.com/Shampaggon/CrackShot/wiki/Default-weapons" target="_blank">default weapon</a>.

#### Explosion_No_Grief:
If `true`, the explosion will _not_ destroy any blocks, paintings, item-frames, or dropped items.

#### Explosion_Radius:
The radius of the explosion. For your own protection, the radius is capped at 20.

Note: The radius of a TNT block is 4. Recommended values are between 1 and 10.

#### Explosion_Incendiary:
If `Explosion_No_Grief:` is set to `false`, setting this node to `true` will set some of the destroyed blocks on fire. If you would like to light blocks on fire _without_ destroying them, consider using the <A HREF="#shrapnel">Shrapnel</A> module.

Note: This node is _not_ to be confused with `Ignite_Victims:`, which sets victims on fire.

#### Explosion_Delay:
The <A HREF="#delay">delay</A> in ticks before the actual explosion occurs. For ordinary projectiles, this can be used for sticky grenades, which explode in a certain amount of time after hitting a victim. For `grenade` however, this delay determines _when_ the grenade will explode after being thrown.

#### On_Impact_With_Anything:
By default, the projectile will only trigger an explosion when it strikes a living entity. If this node is set to `true`, the projectile will explode upon impact with _anything_, which includes blocks and entities. This node _does not_ apply to grenades.

#### Projectile_Activation_Time:
This node represents the <A HREF="#delay">time</A> in ticks that the projectile has to be airborne before it is primed to explode upon impact.

Trivia: Grenade launchers from FPS games such as _Call of Duty_ fire grenades that explode upon impact after traveling in the air for a certain amount of time. Firing one straight down at your feet _will not_ cause an explosion.

#### Message_Shooter:
The <A HREF="#variables">message</A> the shooter will receive when the explosion damages an entity. This node supports `<shooter>` and `<victim>` as <A HREF="#variables">special variables</A>.

#### Message_Victim:
The <A HREF="#variables">message</A> the victim will receive upon being damaged by the explosion. This node supports `<shooter>` and `<victim>` as <A HREF="#variables">special variables</A>.

#### Sounds_Shooter:
The <A HREF="#sounds">sound(s)</A> the shooter will hear whenever the explosion damages an entity. Great for _hit marker_ noises.

#### Sounds_Victim:
The <A HREF="#sounds">sound(s)</A> victims hear when they are hurt by the explosion.

Trivia: This node is used in the <a href="https://github.com/Shampaggon/CrackShot/wiki/Default-weapons" target="_blank">default weapon</a> _Flashbang_ to mimic the ringing of the ears that occurs after a loud explosion.

#### Sounds_Explode:
The <A HREF="#sounds">sound(s)</A> played when the explosion occurs.

Note: This does _not_ replace the TNT-explosion sound. It is merely an addition.

## **░ Lightning** <A NAME="lightning">
    Lightning:
        Enable: <true/false>
        No_Damage: <true/false>
        On_Impact_With_Anything: <true/false>

#### Enable:
Whether or not lightning should strike at the projectile's position upon impact.

Note: This module is compatible with the `grenade` projectile-type! If this module is enabled, the grenade will use it upon detonation.

#### No_Damage:
If the lightning should deal no damage.

#### On_Impact_With_Anything:
By default, the projectile will only trigger a lightning-strike when it collides with a living entity. If this node is set to `true`, the projectile will call a lightning-strike upon impact with _anything_, which includes blocks and entities.

Note: Setting this node to `true` is not recommended unless the use of the weapon is restricted to a controlled environment, as most region-protection plugins do not block lightning in certain regions. You may risk players killing each other with lightning, even in safe-zones.

## **░ Potion effects** <A NAME="potions">
    Potion_Effects:
        Activation: <head,back,crit,hit,shoot,reload>
        Potion_Effect_Shooter: <POTIONTYPE-DURATION-LEVEL>,(...)
        Potion_Effect_Victim: <POTIONTYPE-DURATION-LEVEL>,(...)

#### List of accepted values for potion-type:
    ABSORPTION
    BLINDNESS
    CONFUSION
    DAMAGE_RESISTANCE
    FAST_DIGGING
    FIRE_RESISTANCE
    HARM
    HEAL
    HEALTH_BOOST
    HUNGER
    INCREASE_DAMAGE
    INVISIBILITY
    JUMP
    NIGHT_VISION
    POISON
    REGENERATION
    SATURATION
    SLOW
    SLOW_DIGGING
    SPEED
    WATER_BREATHING
    WEAKNESS
    WITHER

#### Activation:
Specify the event(s) upon which potion effects will be given. `head` for headshots, `back` for backstabs, `crit` for critical hits, `hit` for normal hits, `shoot` for every time the player shoots and `reload` for every time the player reloads.

Example: A weapon has `Activation: back,crit`. Potion-effects will only be given out if the shooter scores either a backstab or a critical hit.

#### Potion_Effect_Shooter:
The potion effect that will be given to the _shooter_ upon activation. Specify a potion type, followed by the duration of the effect in <A HREF="#delay">ticks</A>, followed by the level.

Example: `Potion_Effect_Victim: SLOW-1200-3,BLINDNESS-60-1` would mean the victim will receive a _Slow III_ potion effect for 60 seconds, and a _Blindness I_ potion effect for 3 seconds.

#### Potion_Effect_Victim:
The potion effect that will be given to the _victim_ upon activation. Works in the same way as `Potion_Effect_Shooter:`.

## **░ Particle effects** <A NAME="particles">
    Particles:
        Enable: <true/false>
        Particle_Player_Shoot: <particle-effect>,(...)
        Particle_Terrain: <true/false>
        Particle_Impact_Anything: <particle-effect>,(...)
        Particle_Hit: <particle-effect>,(...)
        Particle_Headshot: <particle-effect>,(...)
        Particle_Critical: <particle-effect>,(...)
        Particle_Backstab: <particle-effect>,(...)

#### Formatting your desired particle effect:
There are 6 types of particle effects to choose from. Their format will be outlined below.

`smoke` - Sends out a puff of smoke.

`lightning` - Strikes lightning at your position. This is just an _effect_, and will deal _no_ damage.

`explosion` - Creates a small "explosion" at your position. This is just an _effect_, and will deal _no_ damage.

`potion_splash-<number>` - Creates a splash-potion breaking effect at the player's position. The number that you specify will determine the color of the splash.

`block_break-<blockID>` Creates a block-break particle effect at the player's position, with the block-type being the ID that you specify.

`flames-<amount>` - Spawns _mob-spawner_ flames at the player's position. You may specify any number for the amount; it does not cause any visible changes.

Example: A weapon with `Particle_Player_Shoot: flames-10,smoke,block_break-55` will create flame, smoke and the block-break particles of _redstone wire_ whenever the player shoots.

#### Enable:
Whether or not particle effects are enabled.

#### Particle_Player_Shoot:
The particle effect(s) spawned at the player upon shooting.

#### Particle_Terrain:
If set to `true`, whenever a projectile (arrow, snowball or egg) strikes a block, it will cause the said block to emit a _block break_ particle effect depending on its _block type_. A unique effect that makes projectiles appear as though they are damaging the terrain.

#### Particle_Hit:
The particle effect(s) spawned at the victim upon impact.

#### Particle_Impact_Anything:
The particle effect(s) spawned at the point of impact. Not to be confused with `Particle_Hit:`, which only activates when a projectile strikes an entity.

#### Particle_Headshot:
The particle effect(s) spawned at the victim when a headshot is delivered.

#### Particle_Critical:
The particle effect(s) spawned at the victim when a critical hit is delivered.

#### Particle_Backstab:
The particle effect(s) spawned at the victim when a backstab is delivered.

## **░ Fireworks** <A NAME="fireworks">
    Fireworks:
        Enable: <true/false>
        Firework_Player_Shoot: <firework>,(...)
        Firework_Explode: <firework>,(...)
        Firework_Hit: <firework>,(...)
        Firework_Headshot: <firework>,(...)
        Firework_Critical: <firework>,(...)
        Firework_Backstab: <firework>,(...)

#### Formatting firework effects:
All fireworks follow the following format: `TYPE-TRAIL-FLICKER-R-G-B`

Specify the _firework type_, which will either be `BALL`, `BALL_LARGE`, `BURST`, `CREEPER` or `STAR`. State whether _trail_ and _flicker_ are enabled using `true` or `false`. Finally, provide a value from 0-255 for R, G and B. These values will determine the color of the firework effect.

Example: `Firework_Headshot: CREEPER-TRUE-TRUE-255-128-64` would create an orange, creeper-type firework that has a trail and flickers.

#### Enable:
Whether or not fireworks are enabled. Fireworks can be emitted whenever the projectile strikes a victim, or whenever a player fires a weapon.

#### Firework_Player_Shoot:
The firework effect(s) spawned at the player upon shooting.

#### Firework_Explode:
The firework effect(s) spawned during explosions.

#### Firework_Hit:
The firework effect(s) spawned at the victim upon impact.

#### Firework_Headshot:
The firework effect(s) spawned at the victim when a headshot is delivered.

#### Firework_Critical:
The firework effect(s) spawned at the victim when a critical hit is delivered.

#### Firework_Backstab:
The firework effect(s) spawned at the victim when a backstab is delivered.

## **░ Abilities** <A NAME="abilities">
    Abilities:
        Super_Effective: <entity-multiplier>,(...)
        Death_No_Drop: <true/false>
        Bonus_Drops: <itemID>,(...)
        Reset_Hit_Cooldown: <true/false>
        Knockback: <amount>
        No_Fall_Damage: <true/false>
        No_Vertical_Recoil: <true/false>
        Hurt_Effect: <true/false>
        Jetpack_Mode: <true/false>
        Break_Blocks: <whitelist-block1,block2,block3,(...)>

#### Super_Effective:
Use this node to increase or decrease the damage dealt to players and certain mobs. This applies to the entire weapon, even explosions caused by it. The multiplier value supports _decimal places_.

List of accepted values for entity type (differs from [this list](https://github.com/Shampaggon/CrackShot/wiki/List-of-Accepted-Mobs), which is only used for the *Spawn_Entity_On_Hit* module):

    Bat
    Blaze
    Cave_Spider
    Chicken
    Cow
    Creeper
    Ender_Dragon
    Enderman
    Ghast
    Giant
    Horse
    Iron_Golem
    Magma_Cube
    Mushroom_Cow
    Ocelot
    Pig
    Pig_Zombie
    Player
    Sheep
    Silverfish
    Skeleton
    Slime
    Snowman
    Spider
    Squid
    Villager
    Witch
    Wither
    Wolf
    Zombie

Example usage: `Super_Effective: PLAYER-0,WITHER-4,ZOMBIE-0.75` will cause the weapon to deal no damage to players, quadruple damage to _Wither_ bosses and 75% damage to _Zombies_.

#### Death_No_Drop:
If set to `true`, the weapon will _not_ drop when the player dies. When the player respawns, the weapon will still be in the inventory. Perfect for hard-to-earn weapons, as it makes it much more difficult for players lose them.

Clarification: This only prevents the weapon from dropping upon player death. You can drop it normally, place it in chests and so forth.

#### Bonus_Drops:
Killing mobs with this weapon will cause them to drop the <A HREF="#itemID">item(s)</A> specified. Bonus drops only apply to mobs, not players.

Uses: This ability can be used in conjunction with arena plugins such as MobArena for _Nazi Zombies_ styled arenas, where zombies are killed for their gold ingots, which are then used to purchase better weapons through weapon stores.

Example: A weapon with `Bonus_Drops: 264,98,352` will cause the victim to drop a diamond, a stone brick, and a bone upon death.

#### Reset_Hit_Cooldown:
This is a particularly useful ability. You may have realized by now that hitting an entity will grant them invulnerability for a split second. This prevents them from getting hit too many times in one second. Setting this to `true` will reset the temporary invulnerability. If this node is `false`, weapons with a high rate of fire, or weapons like shotguns that fire more than one projectile, would not be as effective.

In a nutshell: This ability is a must-have for most firearms, especially for shotguns, which rely on having more than one projectile hit the enemy at the same time.

#### Knockback:
The amount of knockback the victim will experience upon being shot by the weapon. A value between 0-10 is recommended, where a value of 10 means... you shoot at an enemy, you blink, and the enemy is not longer visible. Negative values are accepted, and this will simply _pull_ the victim towards you.

#### No_Fall_Damage:
If `true`, a player holding this weapon upon landing will receive _no_ fall damage.

#### No_Vertical_Recoil:
If `true`, all vertical components of the weapon's recoil will be nullified. This will mean players will only ever be pushed backwards or forwards by the recoil, and never upwards or downwards.

#### Hurt_Effect:
If `true`, the player will receive the _hurt effect_ whenever the weapon is used. A great effect for high-damage, single-shot weapons. However, using this node for fully automatic weapons with a high rate-of-fire may induce headaches.

#### Jetpack_Mode:
If `true`, the recoil from the weapon will only launch the player upwards or downwards. Ideal for reaching great heights, but not so much for traveling, as your movement speed while airborne is incredibly slow.

Tip: For actual _jets_, do not use this node. Instead, simply give weapons a negative recoil.

#### Break_Blocks:
This node causes projectiles to destroy the blocks they hit, except for blocks protected by _CrackShot's_ built-in <A HREF="#regions">Region_Check</A> module. Applies only to arrows, snowballs and eggs.

Format: `<whitelist-blockID,(...)>`

Provide `true` or `false` for `whitelist`. If whitelist is set to true, the projectile will destroy all blocks that you do not list. If whitelist is set to false, the projectile will only destroy the blocks that you list. You can specify as many <A HREF="#itemID">block IDs</A> that you want.

Examples:
* `Break_Blocks: false-18,20,102` will cause the projectile to destroy all _Leaves_ `18`, _Glass_ `20` and _Glass Pane_ `102`.
* `Break_Blocks: true-1,12` will cause the projectile to destroy _all blocks_ except for _Stone_ `1` and _Sand_ `12`.

Secondary data values are supported - `160~4` would represent _Stained Glass Pane (Yellow)_.

Flexibility: Blocks broken by this feature can be recorded and rolled back by external plugins (i.e. [LogBlock](http://dev.bukkit.org/bukkit-plugins/logblock/), [MobArena](http://dev.bukkit.org/bukkit-plugins/mobarena/), [Minigames](http://dev.bukkit.org/bukkit-plugins/minigames/)).

## **░ Hit events** <A NAME="hit_events">
    Hit_Events:
        Enable: <true/false>
        Message_Shooter: <message>
        Message_Victim: <message>
        Sounds_Impact: <sound>,(...)
        Sounds_Shooter: <sound>,(...)
        Sounds_Victim: <sound>,(...)

#### Enable:
Whether or not normal hits should display messages and/or sounds to the shooter and/or victim. Applies only to _projectiles_.

Note: Use this module _appropriately_, or it will result in the shooter/victim being spammed by messages or unsuitable noises. An example of an appropriate use of this node is for _Semtex_ (sticky) grenades. When successfully hitting and "sticking" to an enemy, the shooter will be informed that an enemy has been successfully "stuck". I also like to play a soft "thoonk" noise to replicate _hit markers_, which indicate that an entity was hit.

#### Message_Shooter:
The <A HREF="#variables">message</A> the shooter will receive upon hitting an enemy.

#### Message_Victim:
The <A HREF="#variables">message</A> the victim will receive upon being hit.

#### Sounds_Impact:
The <A HREF="#sounds">sound(s)</A> played at the projectile's position upon striking any surface, whether it be block or entity.

#### Sounds_Shooter:
The <A HREF="#sounds">sound(s)</A> played at the shooter's position upon hitting an enemy.

#### Sounds_Victim:
The <A HREF="#sounds">sound(s)</A> played at the victim's position upon being hit.

## **░ Extras** <A NAME="extras">
    Extras:
        One_Time_Use: <true/false>
        Disable_Underwater: <true/false>
        Make_Victim_Run_Commmand: <command>|(...)
        Make_Victim_Speak: <message>
        Run_Console_Command: <command>|(...)
        Run_Command:
            - <command>
            - (...)

#### One_Time_Use:
Highly recommended for grenades and the like. If `true`, each time the weapon is used, one will be taken out of the player's hand. For ordinary firearms, setting this node to `true` will destroy the weapon after a single shot.

For **remote-type** and **itembomb-type** explosive devices, setting this node to `true` will:
* prevent the device from recharging its ammo after each detonation and
* destroy the device after its ammo reaches zero

Example: _MrDerp_ is holding onto 6 _Frag Grenades_ that have `One_Time_Use:` set to `true`. He right-clicks and throws one of the grenades. He now has 5 _Frag Grenades_ left.

#### Disable_Underwater:
If `true`, and the player is submerged in water, the weapon will be disabled. However, if the player is _not_ in water, the weapon will be functional. Please note that this does not _break_ the weapon as soon as the player is underwater.

#### Make_Victim_Run_Commmand:
Makes the victim run a command upon getting hit. Do _not_ provide the slash `/`, and surround your command(s) with quotes `"`. Reminder: <A HREF="#variables">special variables</A> are supported.

Example: `Make_Victim_Run_Commmand: "clear|me I'm getting out of here|quit"` will make the victim execute `/clear`, `/me I'm getting out of here` and `/quit` upon being hit.

#### Make_Victim_Speak:
Makes the victim say something upon getting hit. Reminder: <A HREF="#variables">special variables</A> are supported.

Example: `Make_Victim_Speak: "Ow. <shooter> just shot me!"` will make the victim say "Ow. (shooter's name) just shot me!" upon being hit.

#### Run_Console_Command:
Runs a console command when the weapon successfully damages a victim. Works in the same way as `Make_Victim_Run_Commmand:`, except this time the commands are run by the console. Reminder: <A HREF="#variables">special variables</A> are supported.

Example: A weapon with `Run_Console_Command: "ban <victim> You've been slapped with the Ban Hammer!"` will ban anyone that gets shot by this weapon.

#### Run_Command:
Runs a command when the weapon is shot. Do _not_ provide the slash `/`, and _always_ surround each command with quotes `"`. Commands that start with `@` will be a _console command_. Only the `<shooter>` <A HREF="#variables">special variable</A> is supported.

**Example 1: Single Command**

        Run_Command:
            - "me is running a command"

Whenever this weapon is shot, the shooter will execute `/me is running a command`.

**Example 2: Single Console Command**

        Run_Command:
            - "@kick <shooter>"

A player named _Doge_ shoots this weapon. The console will execute `kick Doge`.

**Example 3: Multiple Commands**

        Run_Command:
            - "command_1"
            - "command_2"
            - "@console_command_1"
            - "@console_command_2"

Whenever this weapon is shot, the shooter will execute `/command_1` and `/command_2`, and the console will execute `console_command_1` and `console_command_2`. You can list as many commands as you want.