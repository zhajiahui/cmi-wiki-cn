# Mobs

MythicMobs is based all around customized entities/mobs and there are
plenty of options, attributes that you can utilize. Below you find a
complete list of options/attributes that can be added to your custom
creations.

Most of the options below are optional, meaning you don't have to configure the entire
list every time you are creating a new mob. All that really is required
are the `Internal_Name` and the `Type`.

Table Of Contents:

1. [Breaking Down The Mob Configuration](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#breaking-down-the-mob-configuration)
2. [Examples](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#examples)

## Breaking Down The Mob Configuration {#breaking-down-the-mob-configuration}

#### Internal_Name {#internal-name}

This string will be how your mob will be referenced internally in MythicMobs and can be any name you like.
Must be a unique name and does not clash with other internal mob names, **NO SPACES ALLOWED**.

```yml
example_name:
```

#### Type {#type}

This field determines which entity type your creation will be based upon.
A complete list of available [entity types](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html) can be found on spigot javadocs, while [here](https://wiki.mythiccraft.io/mythicmobs/Mobs/Types) you can find a list of types that are explicitly implemented.

> Several mob options for new entity types that Minecraft adds to the base game will not function until Mythic adds support for said entity types

> Some entity types can have negative, hard-to-discover quirks. It is advised that you refer to the [unstable entity types](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs/Unstable-Entity-Types) page in order to form a better opinion on what entity you should be using for your current endeavor

```yml
example_mob:
  Type: zombie
```

```yml
another_mob:
  Type: ZOMBIE
```

#### Display {#display}

Sets the display name of the mob.
This option supports color codes and [placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders).
**The mob's name will not change or update on its own, you have to use [setname](https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/setname) mechanic to change or update it.**

```yml
example_mob:
  Type: zombie
  Display: Example Mob
```

```yml
example_mob:
  Type: zombie
  Display: Example Mob <caster.hp> <red><&heart></red>
```

#### Health {#health}

Sets the base value of the mob's max health attribute.
Mythic doesn't have any limitations on max health but Spigot, however, caps the max health at `2048`.
This can easily be changed in spigot's configuration file, `server_root\spigot.yml`.
Whenever the mob is holding or wearing an item with attribute modifiers will also affect the total max health.

```yml
example_mob:
  Type: zombie
  Display: Example Mob
  Health: 30
```

#### Damage {#damage}

Sets the base value of the mob's melee attack damage attribute.
1 damage equals to 0.5 hearts, so a mob with 6 damage will deal 3 full hearts of damage.
This attribute will never affect damage done by ranged attacks, like arrows or potions.
Whenever the mob is holding or wearing an item with attribute modifiers will also affect the mob's melee damage.

```yml
example_mob:
  Type: zombie
  Display: Example Mob
  Damage: 20
```

#### Armor {#armor}

Sets the base value of the mob's armor attribute.
Minecraft caps the max armor value to 30.
Whenever the mob is holding or wearing an item with attribute modifiers will also affect the total armor.

```yml
example_mob:
  Type: zombie
  Display: Tanker
  Armor: 25
```

#### HealthBar {#healthbar}

Creates a basic health bar hologram above the mob, once the mob has been damaged.

```yml
example_mob:
  Type: zombie
  Display: HealthyBoi
  Health: 1000
  HealthBar:
    Enabled: true
    Offset: 1.45
```

#### BossBar {#bossbar}

Defines and controls the health bar of the mob.
Looks like the Ender Dragon's or the Wither's health bar, but is configurable in appearance.
See [BossBar](https://wiki.mythiccraft.io/mythicmobs/Mobs/BossBar)

```yml
example_mob:
  Type: zombie
  Armor: 25
  BossBar:
    Enabled: true
    Title: Tanker
    Range: 20
    Color: RED
    Style: NOTCHED_6
    CreateFog: true
    DarkenSky: true
    PlayMusic: true
```

#### Faction {#faction}

Sets the mob's faction, which can be used for advanced [Custom AI](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI) configurations or [targeter filtering](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#targeter-options).
Faction is case-sensitive, so be careful when using faction conditions.

```yml
example_mob:
  Type: zombie
  Armor: 25
  Faction: Tank
```

#### Mount {#mount}

Sets the mount of your mob.
Must be another MythicMob.
The mob will automatically ride on the defined mount when it spawns.

```yml
another_example:
  Type: chicken
  Mount: example_mo
```

#### Display Options {#display-options}

Sets the display entity options.
A list of available display options can be found in the [Display Options](https://wiki.mythiccraft.io/mythicmobs/Mobs/DisplayOptions) page

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```

#### Options {#options}

This is a special field which comes with numerous sub-options, like determining if the mob should despawn,
setting knockback resistance, follow range, movement speed and many more.
A list of available mob options can be found in the [Mob Options](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options) page

```yml
slow_persistent_mob:
  Type: husk
  Options:
    MovementSpeed: 0.025
    Despawn: PERSISTENT
```

#### Modules {#modules}

This field allows you to enable or disable modules, like [Threat Tables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ThreatTables) and/or [Immunity Tables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ImmunityTables)

```yml
example_mob:
  Type: husk
  Modules:
    ThreatTable: false
    ImmunityTable: false
```

#### AIGoalSelectors {#aigoalselectors}

Modifies and customizes the [AI goals](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-goal-selectors) of the mob.

```yml
dummy_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
```

```yml
passive_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
    - randomstroll
    - randomlookaround
```

#### AITargetSelectors {#aitargetselectors}

Modifies and customizes the [AI targets](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-target-selectors) of the mob.

```yml
neutral_mob:
  Type: zombie
  AIGoalSelectors:
    - clear
    - meleeattack
    - randomstroll
    - randomlookaround
  AITargetSelectors:
    - clear
    - attacker
```

#### AIPathfindingMalus {#aipathfindingmalus}

Overrides the mob's pathfinding malus for specific path types, changing how its navigation weighs those blocks when calculating paths. Each entry is a path type name followed by the value.
See [AI Pathfinding Malus](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-pathfinding-malus) for value semantics and the list of valid path types.

```yml
pond_wanderer:
  Type: pig
  AIPathfindingMalus:
    - WATER 0
  AIGoalSelectors:
    - clear
    - randomstroll
    - float
```

#### Drops {#drops}

Add or completely modify the mob loot drops.
Can be vanilla items, mythic items, experience points, cross-plugin items (if supported), or even custom drop tables with their own condition system.
See [Drops & DropTables](https://wiki.mythiccraft.io/mythicmobs/drops/Drops) for more information.

```yml
example_mob:
  Type: zombie
  Options:
    PreventOtherDrops: true
  Drops:
    - diamond 32 1
    - netherite_ingot 12 0.5
```

#### DamageModifiers {#damagemodifiers}

Modify how much damage the mob will take from different damage causes.
For example, DamageModifiers can be used to make the mob immune to melee attacks, but weak to ranged attacks.
See [Damage Modifiers](https://wiki.mythiccraft.io/mythicmobs/Mobs/DamageModifiers) for more information.

```yml
example_mob:
  Type: zombie
  DamageModifiers:
    - ENTITY_ATTACK 0
    - PROJECTILE 1.25
```

#### Equipment {#equipment}

Equips the mob with vanilla items or mythic items when it first spawns.
See [Equipment](https://wiki.mythiccraft.io/mythicmobs/Mobs/Equipment) for more information.

```yml
example_mob:
  Type: zombie
  Options:
    PreventRandomEquipment: true
  Equipment:
    - diamond_sword HAND
    - diamond_helmet{name=<green>COMMON</green> helmet} HEAD
```

#### KillMessages {#killmessages}

Customize the [kill messages](https://wiki.mythiccraft.io/mythicmobs/Mobs/KillMessages) that appears when the mob kills a player.

```yml
example_mob:
  Type: zombie
  Display: Tanker
  KillMessages:
    - <caster.name> yeeted <target.name>!!
    - You're too weak <target.name>!!
```

#### Level {#level}

Sets the mob's default [level](https://wiki.mythiccraft.io/mythicmobs/Mobs/Levels).
Accepts a fixed number or a range like `3to7`, which rolls a random level each time the mob spawns.
This level is used whenever the mob is spawned without a level being specified.

```yml
example_mob:
  Type: zombie
  Level: 5
```

#### LevelModifiers {#levelmodifiers}

MythicMobs can have [levels](https://wiki.mythiccraft.io/mythicmobs/Mobs/Levels) and this field is used to determine which kinds of statistics they should gain on when their levels change.

```yml
example_mob:
  Type: zombie
  Display: Dummy
  LevelModifiers:
    Damage: 2
    Health: 0.25
```

#### Disguise {#disguise}

Changes the appearance of the mob to be like other entity types.
Requires the plugin [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/) to be installed and functioning on your server.
See [Add-on: Disguises](https://wiki.mythiccraft.io/mythicmobs/Mobs/Disguises) for more information.

```yml
#This mob acts like a zombie but looks like a chicken
example_mob:
  Type: zombie
  Disguise: chicken
```

#### Skills {#skills}

Skills are an integral feature of Mythic. All mobs are able to have skills of various types that can be triggered under different circumstances with varying
conditions. The Mythic skill system is quite intuitive once you get used to it, and can be used to create anything from simple mobs to incredibly complex bosses.
See [Skills](https://wiki.mythiccraft.io/mythicmobs/Skills/Skills) to get started on making your own skills.

```yml
#swaps locations with the player that right-clicked the mob
example_mob:
  Type: zombie
  Skills:
    - swap @trigger ~onInteract
```

#### Nameplate {#nameplate}

Forces the usage of Mythic nameplates on the mob, if the `Enabled: true` option is used.  
This makes display names like `Display: "Hello\nWorld!"` be displayed on two separate lines.

```yaml
ExampleMob:
  Type: PIG
  Display: "Hello\nWorld!"
  Nameplate:
    Enabled: true

    # The Offset of the nameplate
    Offset: 1.8 
    
    # The Scale of the nameplate
    Scale: 1,1,1

    # If set, forces the nameplate to work with modeled entities from the ModelEngine plugin
    Mounted: true
```

#### Hearing {#hearing}

Allows the mob to "hear" sounds like a warden would.  
Turning this on enables the new [~onHear](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onHear) trigger.

```yaml
ICanHearYou:
  Type: ZOMBIE
  Hearing:
    Enabled: true
  Skills:
  - message{m="I can hear you <trigger.name>! <skill.var.volume>? Way too loud!"} @trigger ~onHear
```

#### Totem {#totem}

Allows you to configure a custom structure that, once built, will summon a mob

```yaml
ExampleMob:
  Type: ZOMBIE
  Totem:

    # The block that once placed will prompt the plugin to check for a totem
    Head: player_head

    # A list of offset vectors and materials that define what the totem should look like
    Pattern:
    - 1,2,0 player_head
    - 0,2,0 player_head
    - -1,2,0 player_head
    - 1,1,0 NETHERITE_BLOCK
    - -1,1,0 NETHERITE_BLOCK
    - 0,1,0 NETHERITE_BLOCK
    - 0,0,0 NETHERITE_BLOCK

    # Optional list of replacements blocks for the pattern.
    # If a replacement for them is not set, every block in the pattern will be replaced with AIR
    Replacement:
    - 0,0,0 AIR
```

The 'Head''s value is the actual block type that, once placed in the world, will prompt the plugin to check if the totem structure is built. It is, as such, suggested to not use a common block type for this

Block offsets are in a x,y,z syntax, configured from the perspective of facing yaw=0 and 0,0,0 being the very bottom of the totem where the mob spawns.

![Mob Totem](https://i.imgur.com/yOc8Hnm.gif)

#### Variables {#variables}

Instead of using a lot of `setvariable` mechanics `~onSpawn`, you can make a mob spawn with already set [variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables) via the use the of Variables mob field.

```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```

> The above example would set
>
> - a `SomeVariable` variable of type `STRING` and of value `something`
> - a `AnIntVariable` variable of type `INTEGER` and of value `2`
> - a `AFloatVariable` variable of type `FLOAT` and of value `420.69`

Possible prefixes:

- `int/`
- `float/`
- `set/`
- `list/`
- `map/`

#### Trades {#trades}

Customizes the villager trades.
Villagers must have a profession and a profession level of 2 to be able to keep its custom trades.

```yml
MerchantTest:
  Type: VILLAGER
  Display: '&6Merchant Test'
  Options:
    Profession: CLERIC
    Type: DESERT
    Level: 2
  Trades:
    1:
      Item1: 5 EMERALD
      Item2: 5 DIAMOND
      Result: DIAMOND_SWORD
    2:
      Item1: 64 EMERALD
      Result: mmoitems.SWORD.CUTLASS
      MaxUses: 1
    3:
      Item1: 32 EMERALD
      Item2: 1 PAPER
      Result: 1 CUSTOM_ITEM
      MaxUses: 1
```

> If `MaxUses` is not set, it will default to `10000`

## Examples {#examples}

More mob examples can be found in the [Examples](https://wiki.mythiccraft.io/mythicmobs/examples/Common-Examples#mobs) section.
