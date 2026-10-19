All options available when creating a mob. Most of these options go under the `Options` section, like so:

```yml
Dummy:
  Type: skeleton
  Options:
    MovementSpeed: 0.3
    PreventSunburn: true
```

##  {#section}

- [Universal Options](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#universal-options)
- [Group Specific Options](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#group-specific-options)
- [Mob Specific Options](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#mob-specific-options)

##  {#section-2}

# Universal options {#universal-options}

These options are universal and will work regardless of the mob type.

#### AlwaysShowName {#alwaysshowname}

Whether the name-tag is always displayed.
Equivalent to the NBT-tag `CustomNameVisible`.
Defaults to `false`.

```yml
  Options:
    AlwaysShowName: false
```

#### AttackSpeed {#attackspeed}

The attack speed of the mob  
Defaults to vanilla attack speed of the respective mobs

```yaml
  Options:
    AttackSpeed: 1
```

#### VisibleByDefault {#visiblebydefault}

Sets whether the mob is visible by default when the mobs spawns or when the mob gets loaded.
Defaults to `true`.

```yml
  Options:
    VisibleByDefault: true
```

#### Invisible {#invisible}

Sets the permanent invisibility effect on the mob; no need to apply invisibility potion with `~onSpawn` trigger.
Defaults to `false`.

```yml
  Options:
    Invisible: true
```

#### Collidable {#collidable}

Whether the mob has collisions. Collisions in Minecraft are bidirectional, so this would need to be set to `false` on both
the entity colliders to ensure that no collisions takes place but will also stop the player from pushing the mob. Defaults to `true`.

```yml
  Options:
    Collidable: true
```

#### DigOutOfGround {#digoutofground}

Teleports the mob two blocks up if it takes `SUFFOCATION` damage. Defaults to `false`.

```yml
  Options:
    DigOutOfGround: false
```

#### Despawn {#despawn}

Determines how the mob will despawn.
This option should be turned on if you're using a lot of mob spawners or entities will overwhelm your server, or the entity you are making requires some special behavior regarding its despawn policy (Npcs, Bosses etc.)  
Defaults to `true`.

| Mode | Aliases | Description |
| --- | --- | --- |
| NORMAL | TRUE, YES | - Despawns if no players are nearby - Despawns if the server is restarted - Despawns if the chunk is unloaded - Is killed by normal mythicmobs kill commands |
| CHUNK |  | - Despawns if the server is restarted - Despawns if the chunk is unloaded - Is killed by normal mythicmobs kill commands |
| NEVER | FALSE, NO | - Is killed by normal mythicmobs kill commands |
| PERSISTENT |  | - Saves the mob in the world file once a chunk unloads. - Persists across server reboots. - Persistent mobs do not fire skills in unloaded chunks. |
| NPC |  | - Despawns if the server is restarted - Despawns if the chunk is unloaded |

> For the PERSISTENT despawn mode: to remove a persistent mob, you have to either use the kill command (`/mm m kill <type>`) or append the `-p` flag to the killall one (`/mm m killall -p`). More information on the subject can be found [here](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions#mob-commands).

```yml
  Options:
    Despawn: true
```

#### FollowRange {#followrange}

The range in blocks within which a mob will target to attack or track an entity.
Defaults to vanilla follow range - `32`.

```yml
  Options:
    FollowRange: 32
```

#### Glowing {#glowing}

Sets whether the mob is permanently glowing. Defaults to `false`.

```yml
  Options:
    Glowing: false
```

#### HealOnReload {#healonreload}

Allows non-despawning mobs to heal once the chunk they are in gets reloaded. Defaults to `false`.

```yml
  Options:
    HealOnReload: false
```

#### Hidden {#hidden}

If true the mob will be left out of command suggestions and the mob browser menu, useful for template mobs
and internal utility mobs. Defaults to `false`.

The mob stays fully usable by its internal name, and `/mm mobs list` still lists it. `/mm mobs list` is the
one place that shows every loaded mob, hidden or not.

**This is a top-level mob key, not an `Options:` key.** Nesting it under `Options:` does nothing.

```yml
example_mob:
  Type: ZOMBIE
  Hidden: true
```

#### Invincible {#invincible}

Makes the mob completely invincible to all types of damage. This option cannot be changed by command skills.
Defaults to `false`.

```yml
  Options:
    Invincible: false
```

#### Interactable {#interactable}

Sets whether the mob can be interacted with. If the mob is an armor stand, it will deny any interaction with the equipments.
Defaults to `false`.

```yml
  Options:
    Interactable: false
```

#### LockPitch {#lockpitch}

Keeps the mob's head from looking up/down.
Defaults to `false`.

```yml
  Options:
    LockPitch: false
```

#### KnockbackResistance {#knockbackresistance}

A percentage of knockback resisted from attacks. This option can be anywhere between `0` and `1`.
But a mob with 100% knockback resistance can still be knocked back by a bow's enchantment: `ARROW_KNOCKBACK` (punch enchantment).
For true knockback resistance, see the [velocity](https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/velocity) mechanic page. Defaults to `0`.

```yml
  Options:
    KnockbackResistance: 0.5
```

#### MaxCombatDistance {#maxcombatdistance}

Prevents players that are a number of blocks away from damaging the mob.
Setting this option to a number less than the distance of a certain mob skill or attack will ensure that the mob can damage the player and will not be as easy to exploit.
Defaults to `256`.

```yml
  Options:
    MaxCombatDistance: 256 
```

#### MovementSpeed {#movementspeed}

The movement speed of the mob.
Most mobs has a default move speed of `0.2` and any value higher than `1` tends to make a mob difficult or impossible to fight.

```yml
  Options:
    MovementSpeed: 0.2
```

#### NoAI {#noai}

Whether the mob should have AI. This option overrides any AI goals specified in [AIGoalSelectors](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#aigoalselectors).
As opposed to AIGoalSelectors, this will work on entities that have hardcoded AI. And if this is set to `true`, the mob will never cast any skills.
Defaults to `false`.

```yml
  Options:
    NoAI: false
```

#### NoDamageTicks {#nodamageticks}

Defines how long in ticks the mob is invulnerable after taking damage.
If [ImmunityTables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ImmunityTables) is enabled for the mob, then `NoDamageTicks` will be per player instead of global.
Defaults to `10`.

```yml
  Options:
    NoDamageTicks: 20
```

#### NoGravity {#nogravity}

Whether the mob should not have gravity. If set to `true`, the mob **CANNOT** have the [velocity](https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/velocity) mechanic used on it.
Defaults to `false`.

```yml
  Options:
    NoGravity: false
```

#### PassthroughDamage {#passthroughdamage}

Causes all damage taken to be redirected to the mob's parent, if one exists. A mob's parent is the entity that initially summoned the mob.
Defaults to `false`.

```yml
  Options:
    PassthroughDamage: false
```

#### PreventItemPickup {#preventitempickup}

Prevent mobs from picking up items;
Defaults to `true`.

```yml
  Options:
    PreventItemPickup: false
```

#### PreventLeashing {#preventleashing}

Whether to prevent a leash from being placed on the mob.
Defaults to `true`.

```yml
  Options:
    PreventLeashing: false
```

#### PreventMobKillDrops {#preventmobkilldrops}

Prevents a MythicMob's target from dropping loot.
Defaults to `false`.

```yml
  Options:
    PreventMobKillDrops: false
```

#### PreventOtherDrops {#preventotherdrops}

Prevents the mob from dropping its vanilla loot table.
Defaults to `false`.

```yml
  Options:
    PreventOtherDrops: false
```

#### PreventRandomEquipment {#preventrandomequipment}

Prevents the mob from spawning with random equipment.
Defaults to `false`.

```yml
  Options:
    PreventRandomEquipment: false
```

#### PreventRenaming {#preventrenaming}

Prevents the mob from being renamed using a nametag.
Defaults to `true`.

```yml
  Options:
    PreventRenaming: false
```

#### PreventSunburn {#preventsunburn}

Prevents the mob from burning in the sun.
Defaults to `false`.

```yml
  Options:
    PreventSunburn: true
```

#### PreventTransformation {#preventtransformation}

Sets whether the mob should be prevented from being turned into other entities.

```yaml
  Options:
    PreventTransformation: false
```

#### PreventVanillaDamage {#preventvanilladamage}

Cancels every instance of the mob dealing "regular" vanilla damage, canceling it.

```yml
  Options:
    PreventVanillaDamage: true
```

#### RepeatAllSkills {#repeatallskills}

Whether to repeat HP based skills if a mob heals back above the health threshold.
Defaults to `false`.

```yml
  Options:
    RepeatAllSkills: false
```

#### ReviveHealth {#revivehealth}

When the mob's death event gets cancelled (via a [Cancelevent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/cancelevent) mechanic [~onDeath](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDeath)) the one specified is the amount of health the mob's will be set to. If the value is `-1`, the mob will heal to its own max health value.

```yaml
#This mob will always return to 50 health every time the death event is cancelled
ExampleMob:
  Type: COW
  Health: 100
  Options:
    ReviveHealth: 50
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```

```yaml
#This mob will always return to its maximum health (100) every time the death event is cancelled
ExampleMob:
  Type: COW
  Health: 100  
  Options:
    ReviveHealth: -1
  Skills:
  - cancelevent{sync=true} @self ~onDeath
```

#### Scale {#scale}

The scale of the mob.

```yaml
  Options:
    Scale: 2
```

#### ShowHealth {#showhealth}

Displays the health of the mob through messages broadcast within a radius and formatting by `Mobs.ShowHealth.Radius` and `Mobs.ShowHealth.Formatting`, respectively, in `/plugins/MythicMobs/config.yml`
Defaults to `false`.

```yml
  Options:
    ShowHealth: false
```

#### Silent {#silent}

Whether a mob should use vanilla sound effects.
Defaults to `false`.

```yml
  Options:
    Silent: false
```

#### UseThreatTable {#usethreattable}

Whether the mob should have [Threat Tables](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/wikis/Mobs/ThreatTables) enabled

```yaml
  Options:
    UseThreatTable: true
```

#### RandomizeProperties {#randomizeproperties}

RandomizeProperties is the vanilla feature in charge of giving variations to mobs when they spawn, such as equipment, zombie leader status, animal variations, zombie/spider jockey, mob size, chance of spawning as baby, etc

```yaml
  Options:
    RandomizeProperties: false
```

# Group specific options {#group-specific-options}

## Boat & BoatChest {#boat-boatchest}

#### Type {#type}

The [type of the boat entity](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Boat.Type.html).

```yaml
  Options:
    BoatType: MANGROVE
```

## Breedable mobs {#breedable-mobs}

#### Age {#age}

The age of the mob. Use `-1` for Baby and `1` for Adults.  
Usable on any mob that can age. For example: Sheep, Pigs, Cows...  
When above 0, represents the number of ticks before this mob can breed again.  
Equivalent to the `Age` NBT.  
Use very low negative numbers to mess with the mobs model (not supported).  
May not be working properly under some situations.  
Defaults to `1`.

```yml
  Options:
    Age: -1
```

#### AgeLock {#agelock}

Whether the mobs age should be locked in place.
Useful for keeping a baby mob from growing up over time.
This is required if you want Age option to work over time.
Defaults to `false`.

```yml
  Options:
    AgeLock: true
```

#### Adult {#adult}

Sets adult status of mob.
Use if `Age` does not work.

```yml
  Options:
    Adult: true
```

#### Baby {#baby}

Sets baby/adult status of mob.
Use if `Age` does not work.

```yml
  Options:
    Baby: true
```

## Colorable Mobs {#colorable-mobs}

Used for Horses, Llamas, TraderLlamas, Parrots, Sheeps, Shulkers, TropicalFishes and Wolves

### Color {#color}

Sets the color of the mob (wool color of sheep or the collar color of wolves)
The value can be any of this [Colors](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html)
Defaults to `WHITE`.

```yml
  Options:
    Color: RED
```

## Neutral Entities {#neutral-entities}

Used for wolves and zombie pigmen, for instance.

#### Angry {#angry}

Whether the mob will spawn angry or not.

> Note: Due to a Bukkit/Spigot bug wolves can not be spawned angry with this option.
> Use AIGoalSelectors and AITargetSelectors if you want to spawn angry wolves.
> Defaults to `false`.

```yaml
  Options:
    Angry: true
```

## Slimes & Magma Cubes {#slimes-magma-cubes}

#### PreventSlimeSplit {#preventslimesplit}

Prevents slimes and magmacubes from splitting.
Default to `false`.

```yaml
  Options:
    PreventSlimeSplit: true
```

## Entities with variable size {#entities-with-variable-size}

#### Size {#size}

Sets the size of slimes, magma cubes, and phantoms.
Can get VERY big and get exponentially larger with each increase.
Extremely high size will cause server lag and possibly crashes.
Default to `1to8` (Phantoms is `1`)

```yaml
  Options:
    Size: 10
```

## Raiders {#raiders}

#### CanJoinRaid {#canjoinraid}

Whether the entity can join a raid.
Defaults to `true`.

```yaml
  Options:
    CanJoinRaid: false
```

#### PatrolLeader {#patrolleader}

Whether the entity is the leader of a patrol.
Defaults to `false`.

```yaml
  Options:
    PatrolLeader: true
```

#### PatrolSpawnPoint {#patrolspawnpoint}

Defaults to `false`.

```yaml
  Options:
    PatrolSpawnPoint: true
```

## Tameable Mobs {#tameable-mobs}

#### Tameable {#tameable}

Whether players are able to tame the mob. Used for wolves, cats and horses.
Defaults to `false`.

```yaml
  Options:
    Tameable: true
```

## Zombies (all variants) {#zombies-all-variants}

#### PreventJockeyMounts {#preventjockeymounts}

Sets whether the zombie will be prevented from spawning as a jockey.  
Only works for Zombies.  
Defaults to `false`.

```yaml
  Options:
    PreventJockeyMounts: true
```

#### PreventConversion {#preventconversion}

Prevents the Zombie from being converted into other types of zombies.  
Defaults to `false`.

```yaml
  Options:
    PreventConversion: true
```

#### ReinforcementsChance {#reinforcementschance}

Chance for zombies to spawn reinforcements on taking damage.  
Should be a number between 0 and 1 (0% and 100% chance).  
Only works for Zombies.  
Defaults to `0`.

```yaml
  Options:
    ReinforcementsChance: 0.38
```

# Mob specific options {#mob-specific-options}

These are specific mob options and will have no effect when used on a
different mob type.

## Armor Stand {#armor-stand}

#### CanMove {#canmove}

Sets whether an armor stand can move. Defaults to `true` and requires PaperSpigot

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanMove: true
```

#### CanTick {#cantick}

Sets whether an armor stand can tick. Defaults to `true` and requires PaperSpigot

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    CanTick: true
```

#### HasArms {#hasarms}

Sets whether an armor stand has arms. Defaults to `false`.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasArms: true
```

#### HasBasePlate {#hasbaseplate}

Sets whether an armor stand has a baseplate. Defaults to `true`

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasBasePlate: false
```

#### HasGravity {#hasgravity}

Sets whether the armor stand is affected by gravity. Defaults to `true`.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    HasGravity: true
```

#### Invisible {#invisible-2}

Sets whether the armor stand is invisible. Defaults to `false`.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Invisible: true
```

#### ItemBody {#itembody}

Designates the [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/Items/Items) that should go in the body/chest slot of an armor stand.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemBody: AN_EXAMPLE_CHESTPLATE
```

#### ItemFeet {#itemfeet}

Designates the [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/Items/Items) that should go in the feet slot of an armor stand.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemFeet: AN_EXAMPLE_BOOTS
```

#### ItemHand {#itemhand}

Designates the [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/Items/Items) that should go in the main hand slot of an armor stand.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHand: AN_EXAMPLE_SWORD
```

#### ItemOffhand {#itemoffhand}

Designates the [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/Items/Items) that should go in the off hand slot of an armor stand.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemOffhand: AN_EXAMPLE_STICK
```

#### ItemHead {#itemhead}

Designates the [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/Items/Items) that should go in the helmet slot of an armor stand.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemHead: AN_EXAMPLE_HELMET
```

#### ItemLegs {#itemlegs}

Designates the [Mythic Item](https://wiki.mythiccraft.io/mythicmobs/Items/Items) that should go in the leggings slot of an armor stand.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    ItemLegs: AN_EXAMPLE_PANTS
```

#### Marker {#marker}

Sets the armor stand as a marker. This option prevents the armor stand from being destroyed in game,
making it completely non-interactable. Defaults to `false`.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Marker: false
```

#### Small {#small}

Sets the armor stand to small variant. Defaults to `false`.

```yml
Dummy:
  Type: ARMOR_STAND
  Options:
    Small: true
```

#### Pose {#pose}

Sets the body part's current pose.  
Default values are `0,0,0` and accepts ranges like `#to#`.  
These will go under the `Pose` section instead of the `Options` section.

###### Head

```yml
Mob:
  Type: armor_stand
  Pose:
    Head: 0,50,0
```

###### Body

```yml
Mob:
  Type: armor_stand
  Pose:
    Body: 0,10,10
```

###### LeftArm

```yml
Mob:
  Type: armor_stand
  Pose:
    LeftArm: 0to360,0,0
```

###### RightArm

```yml
Mob:
  Type: armor_stand
  Pose:
    RightArm: 0to90,0,0
```

###### LeftLeg

```yml
Mob:
  Type: armor_stand
  Pose:
    LegLeg: 0,0to80,0
```

###### RightLeg

```yml
Mob:
  Type: armor_stand
  Pose:
    RightLeg: 20,25,0
```

## Bee {#bee}

#### Anger {#anger}

Sets the time in ticks until bee anger ends.  
If set to 0 the bee will not be angry.  
Defaults to `0`.

```yaml
  Options:
    Anger: 200
```

#### HasNectar {#hasnectar}

Whether the bee is carrying pollen.  
Defaults to `false`.

```yaml
  Options:
    HasNectar: true
```

#### HasStung {#hasstung}

Whether the bee has stung an entity.  
Defaults to `false`.

```yaml
  Options:
    HasStung: true
```

#### PreventStingerLoss {#preventstingerloss}

Whether to prevent the bee from losing its stinger once it hits an entity.  
Defaults to `false`.

```yaml
  Options:
    PreventStingerLoss: true
```

## Camel {#camel}

#### Saddled {#saddled}

Whether the entity is saddled or not.  
Defaults to `false`.

```yaml
  Options:
    Saddled: true
```

#### Tamed {#tamed}

Whether the entity is tamed or not.  
Defaults to `false`.

```yaml
  Options:
    Tamed: true
```

## Cat {#cat}

#### CatType {#cattype}

Sets the type of cat.  
Types can be ALL_BLACK, BLACK, BRITISH_SHORTHAIR, CALICO, PERSIAN, JELLIE, RAGDOLL, RED, SIAMESE, TABBY or WHITE.

```yaml
  Options:
    CatType: BLACK
```

#### CollarColor {#collarcolor}

Sets the color of the cat's collar.  
Available colors are: BLACK, BLUE, BROWN, CYAN, GRAY, GREEN, LIGHT_BLUE, LIGHT_GRAY, LIME, MAGENTA, ORANGE, PINK, PURPLE, RED, WHITE, or YELLOW.

```yaml
  Options:
    CollarColor: GREEN
```

#### Tamed {#tamed-2}

Whether the entity is tamed or not.  
Defaults to `false`.

```yaml
  Options:
    Tamed: true
```

## Cow {#cow}

#### Variant {#variant}

The variant to use for the cow entity. Accepts a namespace, if there is a datapack adding more variants. Read more on the subject on the Minecraft Wiki [here](https://minecraft.wiki/w/Cow#Variants) and [here](https://minecraft.wiki/w/Mob_variant_definitions#Cow)

```yaml
  Options:
    Variant: WARM
```

## Chicken {#chicken}

#### Jockey {#jockey}

Whether or not the chicken has the `IsChickenJockey` NBT set to 1.  
If true, the chicken can naturally despawn, drops 10 experience upon death instead of 1-3 and cannot lay eggs.  
Defaults to `false`.

```yaml
  Options:
    Jockey: true
```

#### Variant {#variant-2}

The variant to use for the chicken entity. Accepts a namespace, if there is a datapack adding more variants. Read more on the subject on the Minecraft Wiki [here](https://minecraft.wiki/w/Chicken#Variants) and [here](https://minecraft.wiki/w/Mob_variant_definitions#Chicken)

```yaml
  Options:
    Variant: WARM
```

## Creepers {#creepers}

#### ExplosionRadius {#explosionradius}

Sets the radius/power of the creepers explosion.  
Negative values are ignored, and the explosion radius remains the creeper's default one.  
Defaults to `-1`.

```yaml
  Options:
    ExplosionRadius: 5
```

#### FuseTicks {#fuseticks}

Sets the number of ticks it takes for creepers to explode.  
Negative values are ignored, and the time it takes remains the creeper's default one.  
Defaults to `-1`.

```yaml
  Options:
    FuseTicks: 60
```

#### SuperCharged {#supercharged}

Whether the creeper should spawn as a super charged creeper.  
Defaults to `false`.

```yaml
  Options:
    SuperCharged: true
```

#### PreventSuicide {#preventsuicide}

Prevents creepers from dying upon exploding. Set `mobGriefing` gamerule to true for this option to work.  
Defaults to `false`.

```yaml
  Options:
    PreventSuicide: true
```

## Copper_Golem {#copper-golem}

#### WeatheringState {#weatheringstate}

The weathering state of the golem. Can be any of [these values](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/CopperGolem.CopperWeatherState.html)

```yaml
  Options:
    WeatheringState: OXIDIZED
```

#### Waxed {#waxed}

Whether the copper golem is waxed.  
Defaults to `true`.

```yaml
  Options:
    Waxed: false
```

## Enderman {#enderman}

#### PreventTeleport {#preventteleport}

Meant for Endermen but //might// work on other mobs. May break teleport skills!  
Defaults to `false`.

```yaml
  Options:
    PreventTeleport: true
```

#### HeldBlock {#heldblock}

Sets the block that the Enderman is carrying.  
Defaults to `AIR`.

```yaml
  Options:
    HeldBlock: STONE
```

## Experience_orb {#experience-orb}

#### Experience {#experience}

Sets the amount of experience give by the experience orb mob.  
Defaults to `1`.

```yaml
  Options:
    Experience: 10
```

## Falling Blocks {#falling-blocks}

#### Block {#block}

Determines the [type of the block](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html).  
Defaults to `STONE`.

```yaml
  Options:
    Block: BIRCH_WOOD
```

#### BlockData {#blockdata}

Additional field for inputting blockdata.  
Defaults to `0`.

#### DropsItem {#dropsitem}

Should the entity be able to drops the falling block's item.  
Defaults to `true`.

```yaml
  Options:
    DropsItem: false
```

#### HurtsEntities {#hurtsentities}

Damages entities on impact.  
Defaults to `true`.

```yaml
  Options:
    HurtsEntities: false
```

#### ReplaceSpawnLocationBlock {#replacespawnlocationblock}

If the entity should replace the block at its spawn location.  
Defaults to `false`.

```yaml
  Options:
    ReplaceSpawnLocationBlock: true
```

#### UseSpawnLocationType {#usespawnlocationtype}

If the type of the falling block should be the one at the spawn location.  
Defaults to `false`.

```yaml
  Options:
    UseSpawnLocationType: true
```

## Fox {#fox}

#### FoxType {#foxtype}

Determines the type of the fox.  
Can be `RED` or `SNOW`.  
Defaults to `RED`.

```yaml
  Options:
    FoxType: SNOW
```

## Frog {#frog}

#### Type {#type-2}

Determines the type of the Frog.  
Alias is `Variant`.  
Can be `WARM`, `COLD` or `TEMPERATE`.  
Defaults to `WARM`.

```yaml
  Options:
    Type: COLD
```

## Goat {#goat}

#### Screaming {#screaming}

Sets if this is a screaming goat. A screaming goat makes screaming sounds and rams more often.  
Defaults to `false`.

```yaml
  Options:
    Screaming: true
```

## Hoglin {#hoglin}

#### ImmuneToZombification {#immunetozombification}

Whether or not the hoglin is immune to being zombified.  
Defaults to `false`.

```yaml
  Options:
    ImmuneToZombification: true
```

#### Huntable {#huntable}

Whether the hoglin is able to be hunted by piglins.  
Defaults to `true`.

```yaml
  Options:
    Huntable: true
```

## Horses, Donkeys, and Mules {#horses-donkeys-and-mules}

#### HorseArmor {#horsearmor}

Used for horses to set the type of armor they have on.  
Can be `iron`, `gold`, or `diamond`  
[armor_type] must be in lower case

```yaml
  Options:
    HorseArmor: gold
```

#### CarryingChest {#carryingchest}

Used for donkeys to set whether they are carrying a chest or not.  
Defaults to `false`.

```yaml
  Options:
    CarryingChest: true
```

#### HorseColor {#horsecolor}

Sets color of the horse.  
Colors must be uppercase,can be any of the [Spigot Horse colors](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Color.html).

```yaml
  Options:
    HorseColor: CREAMY
```

#### Saddled {#saddled-2}

Used for horses to set whether they are saddled or not.  
Defaults to `true` if [HorseArmor](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#horsearmor) is set, or `false` otherwise

```yaml
  Options:
    Saddled: true
```

#### HorseStyle {#horsestyle}

Sets the style of the horse.  
Styles can be any of the [Spigot Horse Style](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Style.html)

```yaml
  Options:
    HorseStyle: WHITE_DOTS
```

#### Tamed {#tamed-3}

Used for horses to set whether they are tamed or not.  
Defaults to `false`.

```yaml
  Options:
    Tamed: true
```

#### HorseType {#horsetype}

Defines the type of horse
Can be any of the [Spigot Horse variants](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Horse.Variant.html)
Defaults to `HORSE`
**Removed in MC 1.11+, use[Type](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#type) instead.**

## Interaction {#interaction}

#### Height {#height}

The Height of the Interaction entity.  
Defaults to `1`.

```yaml
  Options:
    Height: 2
```

#### Width {#width}

The Width of the Interaction entity.  
Defaults to the value of the `Height` option.

```yaml
  Options:
    Width: 3
```

#### Responsive {#responsive}

If the Interaction entity is responsive.  
Defaults to `true`.

```yaml
  Options:
    Responsive: false
```

## IronGolem {#irongolem}

#### PlayerCreated {#playercreated}

Acts as if the player built the mob.  
Defaults to `false`.

```yaml
  Options:
    PlayerCreated: true
```

## Item {#item}

#### Item {#item-2}

The material of the item entity.  
Defaults to `STONE`.

```yaml
  Options:
    Item: BRICK
```

#### Amount {#amount}

The amount of items in the itemstack.  
Defaults to `1`.

```yaml
  Options:
    Amount: 10
```

#### CanPickup {#canpickup}

If the itemstack can be picked up.  
Defaults to `true`.

```yaml
  Options:
    CanPickup: false
```

## Llama {#llama}

#### CarryingChest {#carryingchest-2}

Set whether the entity is carrying a chest or not.  
Defaults to `false`.

```yaml
  Options:
    CarryingChest: true
```

#### Tamed {#tamed-4}

Set whether the entity is tamed or not.  
Defaults to `false`.

```yaml
  Options:
    Tamed: true
```

#### Color {#color-2}

Sets color of the llama.  
Colors must be uppercase,can be any of the [Spigot Llama colors](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Llama.Color.html).

```yaml
  Options:
    Color: CREAMY
```

## MinecartChest {#minecartchest}

#### ChestContents {#chestcontents}

The [droptable](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop-tables) that will be put inside the chest.

```yaml
  Options:
    ChestContents: example_droptable
```

## Panda {#panda}

#### MainGene {#maingene}

Sets the main [gene](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Panda.Gene.html) that the panda can pass on to its offspring.  
Can be NORMAL, AGGRESSIVE, LAZY, WORRIED, PLAYFUL, WEAK, BROWN.  
Defaults to `NORMAL`.

```yaml
  Options:
    MainGene: LAZY
```

#### HiddenGene {#hiddengene}

Sets the hidden [gene](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Panda.Gene.html) that the panda can pass on to its offspring.  
Can be NORMAL, AGGRESSIVE, LAZY, WORRIED, PLAYFUL, WEAK, BROWN.  
Defaults to `NORMAL`.

```yaml
  Options:
    HiddenGene: WORRIED
```

## Parrot {#parrot}

#### Variant {#variant-3}

The [variant](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Parrot.Variant.html) of the parrot.

```yaml
  Options:
    Variant: GRAY
```

#### FlyingSpeed {#flyingspeed}

The flying speed of the parrot.  
Defaults to `-1` (The option is not applied)

```yml
  Options:
    FlyingSpeed: 0.2
```

## Pig {#pig}

#### Saddled {#saddled-3}

If the pig is saddled.  
Defaults to `false`.

```yaml
  Options:
    Saddled: true
```

#### Variant {#variant-4}

The variant to use for the pig entity. Accepts a namespace, if there is a datapack adding more variants. Read more on the subject on the Minecraft Wiki [here](https://minecraft.wiki/w/Pig#Variants) and [here](https://minecraft.wiki/w/Mob_variant_definitions#Pig)

```yaml
  Options:
    Variant: WARM
```

## Piglin {#piglin}

#### AbleToHunt {#abletohunt}

Whether or not the piglin is able to hunt.  
Defaults to `true`.

```yaml
  Options:
    AbleToHunt: false
```

#### ImmuneToZombification {#immunetozombification-2}

Whether or not the piglin is immune to being zombified.  
Defaults to `true`.

```yaml
  Options:
    ImmuneToZombification: false
```

## Piglin Brute {#piglin-brute}

#### ImmuneToZombification {#immunetozombification-3}

Whether or not the piglin is immune to being zombified.  
Defaults to `true`.

```yaml
  Options:
    ImmuneToZombification: false
```

## Rabbit {#rabbit}

#### IsKillerBunny {#iskillerbunny}

Alias: `Angry`.  
Sets the rabbit as the Killer Bunny.  
Defaults to `false`.

```yaml
  Options:
    IsKillerBunny: true
```

#### RabbitType {#rabbittype}

Sets the [type](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Rabbit.Type.html) of rabbit.  
Types can be BLACK, BLACK_AND_WHITE, BROWN, GOLD, SALT_AND_PEPPER, THE_KILLER_BUNNY or WHITE

```yaml
  Options:
    RabbitType: SALT_AND_PEPPER
```

## Sheep {#sheep}

#### Sheared {#sheared}

Whether the Sheep is already sheared.  
Defaults to `false`.

```yaml
  Options:
    Sheared: true
```

## Silverfish {#silverfish}

#### PreventBlockInfection {#preventblockinfection}

Prevent silverfish from infecting blocks.  
Defaults to `false`.

```yaml
  Options:
    PreventBlockInfection: true
```

## Skeleton {#skeleton}

#### PreventConversion {#preventconversion-2}

Prevents the Skeleton from being converted into other types of skeletons.  
Defaults to `false`.

```yaml
  Options:
    PreventConversion: true
```

## Snow Golem {#snow-golem}

#### Derp {#derp}

Whether the Snow Golem has its pumpkin already sheared.  
Defaults to `false`.

```yaml
  Options:
    Derp: true
```

#### PreventSnowFormation {#preventsnowformation}

Prevent the Snow Golem from creating snow.  
Defaults to `false`.

```yaml
  Options:
    PreventSnowFormation: true
```

## TNT {#tnt}

#### FuseTicks {#fuseticks-2}

How long the TNT takes to explode.  
Defaults to `-1` (instantly).

```yaml
  Options:
    FuseTicks: 100
```

#### ExplosionYield {#explosionyield}

Determines the strength of the explosion.  
Defaults to `-1` (The normal TNT Explosion Yield is used).

```yaml
  Options:
    ExplosionYield: 2
```

#### Incendiary {#incendiary}

Whether the explosion is capable of starting fires.  
Defaults to `false`.

```yaml
  Options:
    Incendiary: true
```

## Tropical Fish {#tropical-fish}

#### Pattern {#pattern}

Sets the [Shape/Pattern](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/TropicalFish.Pattern.html) of the fish.

```yaml
  Options:
    Pattern: GLITTER
```

#### BodyColor {#bodycolor}

Sets the [Primary Color](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html) of the fish.

```yaml
  Options:
    BodyColor: GRAY
```

## PatternColor {#patterncolor}

Sets the [Secondary Color](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html) of the fish

```yaml
  Options:
    BodyColor: LIME
```

## Villagers {#villagers}

#### HasTrades {#hastrades}

Whether the villager can be traded with.  
Defaults to `false`.

> Check out [Trades](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#trades)

```yaml
  Options:
    HasTrades: true
```

#### Profession {#profession}

Specifies the [Profession](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Profession.html) of the villager.  
Villagers without this option will roll a random profession on their initial spawn.

```yaml
  Options:
    Profession: MASON
```

#### Type {#type-3}

Represents [Villager type](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Type.html), usually corresponding to what biome they spawn in.  
Defaults to PLAINS.

```yaml
  Options:
    Type: DESERT
```

#### Level {#level}

Villager profession level, levels 1 - 5.  
Level 1 villagers might switch professions. If you want a villager to hold its profession, give them a level of 2 or higher.  
Required if setting villager professions.

```yaml
  Options:
    Level: 3
```

## Wolfs {#wolfs}

#### Variant {#variant-5}

Sets the [Wolf Variant](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Wolf.Variant.html)

```yaml
  Options:
    Variant: black
```

#### Color {#color-3}

Sets the [Color](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/DyeColor.html) of the Wolf's Collar

```yaml
  Options:
    Color: RED
```

## Zombie Villagers {#zombie-villagers}

#### Profession {#profession-2}

Specifies the [Profession](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/Villager.Profession.html) of the zombie villager.  
This option will also make the zombie turn into the respective villager type when being cured using potions.  
Defaults to `FARMER`.

```yaml
  Options:
    Profession: MASON
```
