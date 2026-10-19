# Disguises

### Mob Disguises {#mob-disguises}

**Mob disguises are dependent on the plugins [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises.81/) . They will not work without both of those plugins. [The most up to date documentation for LibsDisguises can be found here](https://www.spigotmc.org/wiki/lib-s-disguises/)**

Most features do not require the premium version of LibsDisguises because LibraryAddict is a pretty nice dude.

### Now that the technical mumbo-jumbo is over... What is a disguise? {#now-that-the-technical-mumbo-jumbo-is-over-what-is-a-disguise}

Disguises allow you to make your mob look like a different mob, a block, or even an item! Disguises are great for shaking things up with mobs, allowing you to do things that are otherwise not possible… for example, making a spider that looks like a zombie– a zombie that climbs walls!. The possibilities are huge.

Any entity type found in the spigot docs should function correctly.
<https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html>

## How To Set up Disguises {#how-to-set-up-disguises}

With the newer versions of MythicMobs, disguises can now be done completely inline using the same **disguise string** syntax as the in-game `/disguise` command.

For example, let's say we want a skeleton that is glowing, spinning, and on fire. To get this disguise ingame, we would use the command: `/disguise SKELETON setGlowing setSpinning setBurning`.
We can take this command, and use it on a mob next to the disguise option, like in the example below:

```yml
SLSkelF:
  Type: ZOMBIE
  Equipment:
  - IRON_SWORD HAND
  - SHIELD OFFHAND
  - LEATHER_HELMET HEAD
  - LEATHER_CHESTPLATE CHEST
  - LEATHER_LEGGINGS LEGS
  - LEATHER_BOOTS FEET
  Display: '&BSkeletal Fighter\n&ELv.<mob.level>'
  Disguise: SKELETON setGlowing setSpinning setBurning
```

## Disguise Options {#disguise-options}

You can view additional disguise options by using `/dhelp <disguisetype>`. You can also view more information on types by using `/dhelp`.  
Examples:

```yml
#Invisible powered Creeper
Disguise: creeper setPowered true setInvisible true

#Brown horse with white spots and gold armor
Disguise: horse setColor brown setStyle white_dots setHorseArmor 418

#Upside-down player disguise with Notch's skin
Disguise: player Dinnerbone setSkin Notch
```

## Saving Disguises {#saving-disguises}

1. Download the skin.png file you want to use for your disguises and put it inside of the server/plugins/libsdisguises/skins folder.
2. use the command `/savedisguise RumiIsAwesome player <inherit> setSkin RumiExMachina.png setDynamicName` to save your skin to a disguise.
3. Apply it to your MM with `Disguise: RumiIsAwesome`

### Detailed steps {#detailed-steps}

1. `RumiIsAwesome` would be the name of your disguise
2. `player` means it's a player disguise
3. `<inherit>` means it will take its name from `Display:` instead of adding it here
4. `setSkin RumiExMachina.png` is telling it to set the disguise skin to your .png file in the skins folder So if you have a skin named Goblin.png in the skins folder, use setSkin Goblin.png
5. `setDynamicName` is used to allow the disguise name to change often, useful when you want to display the entity's health in its name

Excessive Example:

```yml
SneakyDisguisingMob:
  Type: wither_skeleton
  Display: 'meh'
  CustomKillMessages:
  - '<target.name> was sneaked upon! (to death)'
  Health: 128
  Disguise: player Steve setSkin meeeh.png setBurning true setSneaking true setSprinting true setModifyBoundingBox false setDynamicName true
```

#### Nameplates {#nameplates}

Nameplates allow you to extend the nameplates of Player-disguise mobs, which are normally limited to 16 characters.
To use this, simply have Holograms installed and then leave out the “Player” field in your disguise (skin is still required!).
If you don't specify the player field, it will use the Display field instead using a custom nameplate.
Additionally, mob names can be put on multiple lines with diacritics (\n)

```yml
Monkey:
  Type: skeleton
  Display: "this display name is too \n long for players normally"
  Disguise: player Steve setSkin Kurdie.png
```

This feature requires LibsDisguises and the Holograms plugin: <https://www.spigotmc.org/resources/holograms.4924/>

If you have LibsDisguises premium you can use multi line disguise names using the `setDynamicName` option

![image](https://wiki.mythiccraft.io/_media/mythicmobs/uploads/e9f3926c7a8d74dfb1b8fa6d2cd2d67c/image.png)

#### Examples {#examples}

Examples of Disguises being used:

```yml
ExampleMob:
  Type: skeleton
  Disguise: player libraryaddict setCustomName "&8Not Darkitect" setSkin Darkitect.png
```

```yml
ExampleMob2:
  Type: skeleton
  Health: 20
  Disguise: player Ashijin setSkin Notch.png
```

```yml
ExampleMob3:
  MobType: skeleton
  Health: 20
  Disguise: pig
```

```yml
ExampleMob4:
  MobType: skeleton
  Health: 20
  Disguise: FALLING_BLOCK STONE
```
