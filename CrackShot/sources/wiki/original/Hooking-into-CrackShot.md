## **░ CrackShot Utility Functions**
#### **Getting started**
The CSUtility class offers a few functions that some may find useful. In order to access them:

* Import _CrackShot_ into your libraries.
* Import the CSUtility class: `import com.shampaggon.crackshot.CSUtility;`
* Create an instance of CSUtility and assign it to a field.

You will now be able to use the functions described below.

#### **Spawning weapons**
You can give _CrackShot_ weapons directly to players using the function:

    giveWeapon(Player player, String weaponName, int amount)

* `player` - the player who will receive the item(s).
* `weaponName` - the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon the player will receive.
* `amount` - the amount the player will receive.

No weapon will be given if the provided weapon title does not exist in the configuration, or if the player's inventory is full.

#### **Generating weapons**
You can generate a _CrackShot_ weapon using the function:

    generateWeapon(String weaponName)

* `weaponName` - the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon you wish to generate.

Returns the ItemStack of the given weapon or null if the given weapon does not exist in the configuration.

#### **Generating explosions**
You can generate a _CrackShot_ explosion at a given location using the function:

    generateExplosion(Player player, Location loc, String weaponTitle)

* `player` - the player who will be identified as the causer of the explosion.
* `loc` - the location the explosion will be generated at.
* `weaponTitle` - the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) that the explosion will use.

#### **Spawning mines**
You can spawn a _CrackShot_ mine at a given location using the function:

    spawnMine(Player player, Location loc, String weaponTitle)

* `player` - the player who will be identified as the placer of the mine.
* `loc` - the location the mine will be spawned at.
* `weaponTitle` - the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) that the mine will use.

#### **CrackShot projectiles**
You can convert ordinary projectiles into _CrackShot_ projectiles. Applies only to snowballs, eggs, arrows, fireballs and wither skulls.

    setProjectile(Player player, Projectile proj, String weaponTitle)

* `player` - the player who will be identified as the shooter of the projectile. Cannot be **null**.
* `proj` - the projectile to convert.
* `weaponTitle` - the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the converted projectile.

#### **Getting the weapon title of an item**
You can get the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of an item. Returns the weapon title of the item as a String. Returns **null** if one could not be found.

    getWeaponTitle(ItemStack item)

* `item` - the item you would like to identify. Cannot be **null**.

#### **Getting the weapon title of a projectile**
You can get the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of a projectile. Returns the weapon title of the projectile as a String. Returns **null** if one could not be found.

    getWeaponTitle(Projectile proj)

* `proj` - the projectile you would like to identify. Cannot be **null**.

#### **Getting the weapon title of a TNTPrimed entity**
You can get the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of a TNTPrimed entity. Returns the weapon title of the entity as a String. Returns **null** if one could not be found.

    getWeaponTitle(TNTPrimed tnt)

* `tnt` - the TNTPrimed entity you would like to identify. Cannot be **null**.

## **░ CrackShot Events**
#### **WeaponAttachmentToggleEvent**
This event is called whenever a player toggles an attachment on a _CrackShot_ weapon.

* Methods:
  * getItemStack() - Returns the ItemStack involved in this event.
  * getPlayer() - Returns the Player involved in this event.
  * getToggleDelay() - Returns the [toggle delay](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#attachments) of this event.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * isCancelled() - Gets the cancellation state of this event.
  * setCancelled() - Sets the cancellation state of this event.
  * setToggleDelay() - Sets the [toggle delay](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#attachments) of this event.

#### **WeaponDamageEntityEvent**
This event is called when an entity is damaged by a melee attack, projectile or explosion caused by a _CrackShot_ weapon.

* Methods:
  * getDamager() - Returns the damager as an Entity, or null if the damage was caused by an energy/splash projectile or a melee attack.
      * This entity could be of the type:
          * Projectile, if the damage was caused by a projectile (direct impact).
          * TNTPrimed, if the damage was caused by an explosion.
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getVictim() - Returns the victim as an Entity.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * getDamage() - Returns the amount of damage caused by this event.
  * isBackstab() - Checks if the event was a backstab.
  * isCancelled() - Gets the cancellation state of this event.
  * isCritical() - Checks if the event was a critical hit.
  * isHeadshot() - Checks if the event was a headshot.
  * setCancelled() - Sets the cancellation state of this event.
  * setDamage() - Sets the amount of damage caused by this event.

#### **WeaponExplodeEvent**
This event is called whenever a _CrackShot_ weapon creates an explosion, splits or calls an airstrike.

* Methods:
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getLocation() - Returns the Location of the explosion.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * isSplit() - Checks if the event was a cluster bomb _split_.
  * isAirstrike() - Checks if the event was an airstrike call.

#### **WeaponFireRateEvent**
This event is called when a player fires a _CrackShot_ weapon that is using the [Fully_Automatic](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#spray_and_pray) module.

* Methods:
  * getFireRate() - Returns the [Fire_Rate](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#fire_rate) value being used in this event.
  * getItemStack() - Returns the ItemStack of the weapon involved in this event.
  * getPlayer() - Returns the Player involved in this event.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * setFireRate() - Sets the [Fire_Rate](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#fire_rate) value to be used by this event.

#### **WeaponHitBlockEvent**
This event is called whenever a _CrackShot_ projectile strikes a solid block. Applies only to arrows, eggs and snowballs.

* Methods:
  * getAirBlock() - Returns the Block that the projectile traveled through before impact.
  * getBlock() - Returns the Block that the projectile struck.
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getProjectile() - Returns the fired projectile as an Entity, or null if the projectile is of the _energy_ type.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.

#### **WeaponPlaceMineEvent**
This event is called whenever a _CrackShot_ landmine is placed.

* Methods:
  * getPlayer() - Returns the Player that placed the mine.
  * getMine() - Returns the placed mine as an Entity.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the placed mine.

#### **WeaponPreShootEvent**
This event is called right before a weapon launches any projectiles.

* Methods:
  * getBulletSpread() - Returns the [bullet spread](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#bullet_spread) value to be used in this event.
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getSounds() - Gets the reload [sounds](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#sounds).
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * isCancelled() - Gets the cancellation state of this event.
  * isLeftClick() - Check whether this was a left click.
  * setBulletSpread() - Sets the [bullet spread](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#bullet_spread) value to be used in this event.
  * setCancelled() - Sets the cancellation state of this event.
  * setSounds() - Sets the reload [sounds](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#sounds).

#### **WeaponPrepareShootEvent**
This event is called at the very start of the _shooting_ process. Its intention is to provide finer control over which players are allowed to use particular weapons.

* Methods:
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * isCancelled() - Gets the cancellation state of this event.
  * setCancelled() - Sets the cancellation state of this event.

#### **WeaponReloadEvent**
This event is called whenever a player reloads a weapon. The reload speed can be scaled with a **double** ranging from zero to infinity. For example, **0** is instantaneous, **1** is normal and **2** will double the reload time.

* Methods:
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getReloadSpeed() - Gets the reload speed of this event.
  * getSounds() - Gets the reload [sounds](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#sounds).
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * setReloadSpeed() - Sets the reload speed of this event.
  * setSounds() - Sets the reload [sounds](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#sounds).

#### **WeaponReloadCompleteEvent**
This event is called whenever a player successfully completes a reload.

* Methods:
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.

#### **WeaponScopeEvent**
This event is called whenever a player zooms in or out with a _CrackShot_ weapon.

* Methods:
  * getPlayer() - Returns the Player involved in this event.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * isCancelled() - Gets the cancellation state of this event.
  * isZoomIn() - Checks if the player was zooming in.
  * setCancelled() - Sets the cancellation state of this event.

#### **WeaponShootEvent**
This event is called when a player uses a _CrackShot_ weapon to fire any of the [9 supported projectiles](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#projectile_type), or when an [item bomb](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-devices) is thrown.

* Methods:
  * getPlayer() - Returns the Player involved in this event.
  * getProjectile() - Returns the fired projectile as an Entity, or null if the projectile is of the _energy_ type.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.

#### **WeaponTriggerEvent**
This event is called whenever a landmine is triggered by an entity walking through it.

* Methods:
  * getPlayer() - Returns the Player that caused this event, or null if the player is offline.
  * getVictim() - Returns the victim as a LivingEntity.
  * getWeaponTitle() - Returns the [weapon title](https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot#wiki-title) of the weapon involved in this event.
  * isCancelled() - Gets the cancellation state of this event.
  * setCancelled() - Sets the cancellation state of this event.