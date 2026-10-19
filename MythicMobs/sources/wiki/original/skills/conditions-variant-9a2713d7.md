1. [Additional Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/conditions#additional-conditions)
2. [Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/conditions#conditions-2)
   1. [More Examples](https://wiki.mythiccraft.io/mythicmobs/Skills/conditions#more-examples)

## Introduction

Conditions are used to determine whether or not an action may execute.

Conditions can be used in [1]:

- [Skill Mechanics](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/skill)
- [Drop Tables](https://wiki.mythiccraft.io/mythicmobs/drops/Drops#drop-tables)
- [Spawners](https://wiki.mythiccraft.io/mythicmobs/Spawners)
- [Random Spawners](https://wiki.mythiccraft.io/mythicmobs/Random-Spawns)

When applying multiple conditions, all of them must be met in order for the skill to be executed. Some conditions allow arrays that can be split by commas. Such conditions only require one of the strings in the array to match.

To see how to use in-line conditions, [click here!](https://wiki.mythiccraft.io/mythicmobs/skills/Inline-Conditions)

## Types

Conditions can be broken into four types:

1. Entity Conditions: These check the conditions of an entity.
2. Location Conditions: These check the conditions at a location. If a location condition is used while an entity is targeted, it will check the conditions at the entity's location.
3. Compare conditions: These check for certain conditions between two different "things". For example, "Cuboid" will return true if a target is within a cube where the corners are two coordinates
4. Meta conditions: they will not necessarily check against any inherent property of either the caster or a target. For instance, "StringEquals" will return true or false depending on whether two strings match. Those strings *can* be placeholders that fetch the value from either the caster or a target, but that is just one possible application.

## Usage

Conditions can also be used in three different places within a metaskill:

#### Conditions

Conditions in this section check against the caster or its location.

```yaml
  Conditions:
  - health{h=>10}
```

> Checks if the caster has more than 10 health points

```yaml
  Conditions:
  - globalscore{objective=Test;v=>10}
```

> In the example above, the globalscore condition will check the caster's global score.

---

#### TargetConditions

Conditions in this section check against the [inherited target](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#inheritance) of the metaskill

```yaml
  TargetConditions:
  - health{h=>10}
```

> Checks if the inherited targeted entities have more than 10 health points, and only those that do will be inherited as an inherited target by the metaskill. If none do then the metaskill, by default, will not execute.

```yaml
  TargetConditions:
  - globalscore{objective=Test;v=>10}
```

> The example above the globalscore condition will check the inherited target's global score. Since globalscore is an entity condition, it will only work if an entity is targeted.

---

#### TriggerConditions

Conditions in this section check against the trigger of the metaskill

```yaml
  TriggerConditions:
  - health{h=>10}
```

> Checks if the trigger of the metaskill has more than 10 health points

## Ranged Values

Ranged values use either the format **#to#** or **#-#**. You must use "to" instead of "-" if you want to use negative numbers in the range. For:

```yaml
YourMagnificentSkill:
  Conditions:
    - altitude{a=1-5}
  TargetConditions:
    - distance{d=1to10} true
  TriggerConditions:
    - distance{d=1to10} true
```

## Condition Actions

Condition Actions allow you to do additional things based off of conditions. The default condition action is **true**

| Action | Description |
| --- | --- |
| `true` | The skill will run if this condition is met |
| `false` | The skill will *not* run if this condition is met |
| `power` [multiplier] | Multiplies the skill's power by the value of `multiplier` (e.i. power 2.0 would double the skill's power) |
| `cast` [skill] | Casts an additional skill if the condition is met, without having effect on the execution of original skill |
| `castinstead` [skill] | Casts a different skill instead if the condition is met |
| `orElseCast` [skill] | Casts a different skill instead if the condition is not met |

```yaml
  Conditions:
  - day true
  Skills:
  - message{m="It's day!"} @self
```

> Will run only if it's day in the caster's world

```yaml
  Conditions:
  - day false
  Skills:
  - message{m="It's *not* day!"} @self
```

> Will run only if it's *not* day in the caster's world  
> The opposite behavior of `true`

```yaml
ExampleSkill:
  Conditions:
  - day true
  - sunny orElseCast OtherSkill
  Skills:
  - message{m="It's day and sunny!"} @self

OtherSkill:
  Skills:
  - message{m="It's day and not sunny!"} @self
```

> If a condition line is not met *(the condition is met and the condition action if false or vice versa)* [no more conditions will be checked](https://en.wikipedia.org/wiki/Short-circuit_evaluation)  
> So even if OtherSkill is executed because of the `sunny` condition we can be sure that the `day` condition is also met, or else no skill would have run at all because  
> `day true`  
> is checked before  
> `sunny orElseCast OtherSkill`

```yaml
YourAwesomeSkill:
  Conditions:
  - day true
  TargetConditions:
  - stance{s=defensive} power 0.5
  TriggerConditions:
  - stance{stance=defensive} power 0.5
  - score{objective=test;value=>20} false
  - haspotioneffect{type=POISON;level=>0;duration=0to100} true
```

## Composite Conditions

Conditions can also be grouped by parenthesis and evaluated via the **AND** (`&&`) and **OR** (`||`) boolean operators. Conditions used this way can still have a condition action.

```yaml
  Conditions:
  - ((day false || raining true) && onBlock{material=LIME_CONCRETE}) true
```

> The condition is met when it's either raining or not daytime, and, in addition to that, only when the caster is on a LIME_CONCRETE block

> The day and raining have their condition action declared, while onBlock uses the default one, `true`

## Universal Attributes

Every condition shares and can use the following attributes

# Additional Conditions

Links to conditions added by addon plugins. Any conditions from these links will not work without that plugin installed.

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Conditions)
- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Conditions)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Conditions)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#conditions)

# Conditions

| Condition | Type | Description |
| --- | --- | --- |
| [Altitude](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/altitude) | Entity | Tests how far above the ground the target entity is |
| [Biome](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/biome) | Location | Tests if the target is within the given list of biomes |
| [BiomeType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/biometype) | Location | Tests for the biome category at a location. |
| [BlockType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/blocktype) | Location | Tests the material type present at the target location |
| [BlockTypeInRadius](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/BlockTypeInRadius) | Location | Checks against the amount of specified blocks in a radius around the target location |
| [Blocking](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/blocking) | Entity | Tests if the targeted player is blocking with a shield |
| [BoundingBoxesOverlap](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/BoundingBoxesOverlap) | Compare | Checks if the caster's BoundingBox overlaps with the target's |
| [BowTension](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/bowtension) | Meta | Checks the bow tension of when an entity shoots from a bow |
| [Burning](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/burning) | Entity | Whether or not the target entity is on fire |
| [Chance](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/chance) | Meta | The chance that the metaskill has to be executed |
| [Charged](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/charged) | Entity | Checks if the target creeper is charged |
| [Children](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/children) | Entity | Tests how many children the caster has |
| [Color](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/color) | Entity | Tests the entity's colors |
| [CompareValues](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/CompareValues) | Meta | Compares two values based on a specified operation |
| [Crouching](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/crouching) | Entity | Whether or not the target entity is crouching |
| [Cuboid](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/cuboid) | Compare | Whether the target is within the given cuboid between location1 x location2 |
| [DamageAmount](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DamageAmount) | Meta | Checks for a range of damage taken |
| [DamageCause](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DamageCause) | Meta | Checks the type of the damage cause |
| [DamageTag](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/damagetag) | Meta | Checks the tags of the damage cause |
| [Dawn](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/dawn) | Location | If the time is dawn, from 22000 to 2000 in-game time |
| [Day](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/day) | Location | If the time is day, from 2000 to 10000 in-game time |
| [Dimension](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/dimension) | Location | If the target location is within a certain dimension |
| [DirectionalVelocity](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/directionalvelocity) | Entity | If the target has a velocity matching the given parameters |
| [Distance](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/distance) | Compare | Whether the distance between the caster and target is within the given range |
| [DistanceFromLocation](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DistanceFromLocation) | Entity | Whether the distance between the target and a specified location is within a certain range |
| [DistanceFromPin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/DistanceFromPin) | Location | Checks if the target is within a certain distance of a specified pin |
| [DistanceFromSpawn](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/distancefromspawn) | Location | Whether the distance from the world's spawn point to the target is within the given range |
| [DistanceFromTrackedLocation](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/distancefromtrackedlocation) | Location | Whether the distance from the tracked location to the caster is within the given range |
| [Dusk](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/dusk) | Location | If the time is dusk, from 14000 to 18000 in-game time. |
| [EnchantingExperience](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EnchantingExperience) | Entity | Checks the target player's experience points |
| [EnchantingLevel](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/enchantingLevel) | Entity | Checks the target player's experience level |
| [EnderDragonAlive](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EnderDragonAlive) | Location | Checks if there is at least one EnderDragon alive in the world of the targeted location |
| [EnderDragonPhase](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EnderDragonPhase) | Entity | Checks if the ender dragon is in a phase or phases |
| [EntityItemIsSimilar](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EntityItemIsSimilar) | Entity | Tests if the target item entity is similar to another item |
| [EntityItemType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EntityItemType) | Entity | Tests the type of the target item entity |
| [EntityMaterialType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/EntityMaterialType) | Entity | Tests the material of the target item entity |
| [EntityType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/entitytype) | Entity | Tests the entity type of the target |
| [Faction](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/faction) | Entity | Tests for the targets faction |
| [FallSpeed](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/fallspeed) | Entity | If the fall speed of the target is within the given range |
| [FieldOfView](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/fieldofview) | Compare | Tests if the target is within the given angle from where the caster is looking |
| [FoodLevel](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/FoodLevel) | Entity | Checks if the target has food within the range |
| [FoodSaturation](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/FoodSaturation) | Entity | Checks if the target has food within the range |
| [Gamemode](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/Gamemode) | Entity | Checks if the target player's gamemode is the specified one |
| [Gliding](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/gliding) | Entity | If the target is gliding |
| [GlobalScore](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/globalscore) | Entity | Checks a global scoreboard value |
| [HasAI](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasai) | Entity | Checks if the target entity has its AI enabled |
| [HasAura](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasaura) | Entity | Checks if the target entity has the given aura |
| [HasAuraStacks](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasaurastacks) | Entity | Tests if the target has the given range of stacks from an aura |
| [HasAuraType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasAuraType) | Entity | Checks if the target entity has the given aura type |
| [HasCurrency](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hascurrency) | Entity | If the target has the given amount of vault currency |
| [HasDialogOpen](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasDialogOpen) | Entity | Checks if the target player has a dialog open |
| [HasEnchantment](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasEnchantment) | Entity | Checks if the target entity's equipped item has an enchantment |
| [HasFreeInventorySlot](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasFreeInventorySlot) | Entity | Checks if the evaluated entity has a free inventory slot |
| [HasGravity](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasgravity) | Entity | Tests if the target mob has gravity |
| [HasItem](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasItem) | Entity | Tests if the target player has the given number of given material |
| [HasOffhand](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HasOffhand) | Entity | Checks if the target entity has something in the offhand |
| [HasOwner](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasowner) | Entity | Tests if the target mob has an owner |
| [HasParent](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasparent) | Entity | Tests if the target mob has a parent |
| [HasPassenger](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasPassenger) | Entity | Checks if the target entity has a passenger |
| [HasPermission](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/haspermission) | Entity | Tests if the target player has a permission |
| [HasPotionEffect](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/haspotioneffect) | Entity | Tests if the target entity has a potion effect |
| [HasTag](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hastag) | Entity | Tests if the target has a scoreboard tag |
| [Health](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/health) | Entity | Matches the target's health |
| [HealthPercent](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HealthPercent) | Entity | Matches the target's health percentage or multiplier |
| [Height](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/height) | Location | Checks if the target's Y location is within a range |
| [HeightAbove](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/heightabove) | Location | Checks if the target's Y location is above a value |
| [HeightBelow](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/heightbelow) | Location | Checks if the target's Y location is below a given value |
| [Holding](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/holding) | Entity | Checks if the target is holding a given material(support MythicMobs and Vanilla) |
| [inBounds](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/inBounds) | Compare | Tests whether the target is inside a cuboid, sphere, or cylinder |
| [inClaim](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/inClaim) | Location | Checks if the target location is inside a claim |
| [InCombat](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/incombat) | Entity | Checks if the target mob is considered in combat |
| [InPinRegion](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/InPinRegion) | Location | Checks if the target location is within a region delimited by two pins |
| [IsInvulnerable](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsInvulnerable) | Entity | Checks whether the target entity is invulnerable |
| [IsInSurvivalMode](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsInSurvivalMode) | Entity | Checks if the target player is in survival mode |
| [Inside](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/inside) | Location | Checks if the target has a block over their head |
| [isBaby](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isbaby) | Entity | Checks if the target entity is a baby |
| [isCancelled](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsCancelled) | Meta | Checks if the triggering event is cancelled |
| [isCaster](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/iscaster) | Entity | Checks if the target is the caster |
| [isChild](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ischild) | Entity | Checks if the target is a child of the caster |
| [isClimbing](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isClimbing) | Entity | Checks if the target entity is climbing |
| [IsCreeperPrimed](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsCreeperPrimed) | Entity | Checks if the target creeper is primed to explode |
| [isFlying](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isflying) | Entity | Checks if the target player is flying |
| [isFrozen](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isfrozen) | Entity | Checks if the target entity is frozen |
| [isInCinematic](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsInCinematic) | Entity | Checks if the target player is in an active cinematic |
| [isLeashed](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isleashed) | Entity | Checks if the target has been leashed |
| [isLiving](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isliving) | Entity | Checks if the target is a living entity |
| [isMonster](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ismonster) | Entity | Checks if the target is a monster |
| [isMythicMob](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ismythicmob) | Entity | Checks if the target is a MythicMob |
| [IsParentAlive](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsParentAlive) | Entity | Checks if the parent of the target entity is still alive |
| [IsParent](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsParent) | Compare | Checks if the target entity is the parent of the caster |
| [isPlayer](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isplayer) | Entity | Checks if the target is a player |
| [isRaiderPatrolLeader](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isRaiderPatrolLeader) | Entity | Checks if the target entity is the captain of a pillager group |
| [isSaddled](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/issaddled) | Entity | Checks if the target entity is saddled |
| [IsSibling](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsSibling) | Compare | Whether the target entity is a sibling of the caster |
| [isSkill](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsSkill) | Meta | Checks whether the specified metaskill exists |
| [isTamed](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsTamed) | Entity | Checks if the target entity is tamed |
| [IsUsingSpyglass](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/IsUsingSpyglass) | Entity | Checks if the target player is using a spyglass |
| [ItemGroupOnCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ItemGroupOnCooldown) | Entity | Checks whether the target player has the specified item group on cooldown |
| [ItemIsSimilar](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/itemissimilar) | Entity | Checks that targeted player's inventory slot if it's similar to an item |
| [ItemRecharging](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/itemrecharging) | Entity | Checks if the target's weapon is recharging |
| [ItemType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ItemType) | Meta | Checks against the material of the item that triggered the skill |
| [LastDamageCause](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lastdamagecause) | Entity | Checks the target's last damage cause |
| [LastSignal](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lastsignal) | Entity | Matches the last signal received by the target mob |
| [Level](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/level) | Entity | Checks the target MythicMob's level |
| [LightLevel](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lightlevel) | Location | Tests the light level at the target location |
| [LightLevelFromBlocks](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lightlevelfromblocks) | Location | Tests the light level originating from light-emitting blocks at the target location |
| [SkyLightLevel](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/skylightlevel) | Location | Tests the sky light level at the target location |
| [LineOfSight](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lineofsight) | Compare | Tests if the target is within line of sight of the caster |
| [LineOfSightFromOrigin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lineofsightfromorigin) | Compare | Tests if the target is within line of sight of the caster |
| [LivingInRadius](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/LivingInRadius) | Location | Matches a range to how many living entities are in the given radius |
| [LocalDifficulty](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/localdifficulty) | Location | Tests the difficulty scale at the target location |
| [LookingAt](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/LookingAt) | Entity | Checks if the player is looking at something |
| [LunarPhase](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lunarphase) | Location | Checks the target world's lunar phase |
| [MaterialisOnCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MaterialIsOnCooldown) | Entity | Checks if the target player's specified material is on cooldown |
| [MetaskillCondition](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MetaskillCondition) | Meta | Casts a Metaskill that will determine if the condition should check or not |
| [MobsInChunk](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsinchunk) | Location | Matches a range to how many mobs are in the target location's chunk |
| [MobsInRadius](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsinradius) | Location | Checks how many mobs are in a given radius |
| [MobsInWorld](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsinworld) | Location | Matches a range to how many mobs are in the target world |
| [MobsNearOrigin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MobsNearOrigin) | Meta | Matches a range to how many mobs are in the given radius around the origin |
| [MobSize](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mobsize) | Entity | Checks the size of an entity that can have its size changed |
| [Moist](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/Moist) | Location | Checks if the target block of farmland is hydrated |
| [MoistureLevel](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/moisturelevel) | Location | Checks if the target block of farmland has the specified level of hydratation |
| [MotionX](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/motionx) | Entity | Checks the X motion of the target entity against a range. |
| [MotionY](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/motiony) | Entity | Checks the Y motion of the target entity against a range. |
| [MotionZ](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/motionz) | Entity | Checks the Z motion of the target entity against a range. |
| [Mounted](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mounted) | Entity | If the target entity is riding a mount/vehicle |
| [Moving](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/moving) | Entity | If the target has a velocity greater than zero |
| [MythicMobType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mythicmobtype) | Entity | Checks the MythicMob type of the target mob |
| [MythicPack](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/mythicpack) | Meta | Checks for the presence of Pack |
| [MythicPackVersion](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MythicPackVersion) | Meta | Checks if a pack has a specified version |
| [MythicPackVersionGreater](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/MythicPackVersionGreater) | Meta | Checks if a pack has a version greater or equal the specified one |
| [Name](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/name) | Entity | Checks against the entity's name |
| [NearClaim](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/nearclaim) | Location | If the target location is near any GriefPrevention claims |
| [Night](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/night) | Location | If the time is night, from 14000 to 22000 in-game time |
| [NotInRegion](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/notinregion) | Location | If the target location is not within the given WorldGuard region |
| [OffGCD](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/offgcd) | Entity | Checks if the target mob has an active Global Cooldown |
| [OnBlock](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/onblock) | Location | Matches the block the target entity is standing on |
| [OnGround](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/onground) | Entity | If the target entity is standing on solid ground |
| [OriginDistanceFromPin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/OriginDistanceFromPin) | Location | Checks if the origin is within a certain distance of a specified pin |
| [OriginLocation](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/OriginLocation) | Meta | Checks if the origin is at a given location |
| [Outside](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/outside) | Location | If the target has open sky above them |
| [Owner](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/owner) | Compare | Checks if the target entity is the owner of the caster |
| [OwnerIsOnline](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ownerisonline) | Entity | Checks if the owner of the target mob is online, if the owner is a player |
| [Pitch](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/pitch) | Entity | Checks if the pitch of the target entity is within a range |
| [PlayerKills](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playerkills) | Entity | Matches how many players the target mob has killed |
| [PlayerNotWithin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playernotwithin) | Location | Checks if any players are within a radius of the target |
| [PlayerWithin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playerwithin) | Location | Checks if any players are within a radius of the target |
| [PlayersInRadius](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playersinradius) | Entity | Checks how many players are in a radius |
| [PlayersInWorld](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playersinworld) | Meta | Matches the number of players in the caster's world |
| [PlayersOnline](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/playersonline) | Meta | Matches the number of players online |
| [Plugin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/plugin) | Meta | Checks if the specified plugin is running on the server |
| [Premium](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/premium) | Meta | Checks if MythicMobs Premium is running on the server |
| [ProjectileHasEnded](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ProjectileHasEnded) | Meta | Checks if the calling projectile has ended |
| [Raining](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/raining) | Location | If it's raining in the target world |
| [Region](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/region) | Location | If the target is within the given WorldGuard region |
| [SameFaction](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/samefaction) | Entity | Tests if the caster and target are in the same faction |
| [Score](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/score) | Entity | Checks a scoreboard value of the target entity |
| [ServerIsPaper](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ServerIsPaper) | Meta | Checks whether the server is running a fork of paper. |
| [ServerNmsVersion](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/servernmsversion) | Meta | Checks if the server is running the specified minecraft NMS version. |
| [ServerVersion](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/serverversion) | Meta | Checks if the server is running the specified minecraft version. |
| [ServerVersionAfterOrEqual](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ServerVersionAfterOrEqual) | Meta | Checks whether the server is after or equal to a specific version |
| [ServerVersionBefore](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ServerVersionBefore) | Meta | Checks whether the server is before a specific version |
| [Size](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/Size) | Entity | Checks the size of the target entity |
| [SkillOnCooldown](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/skilloncooldown) | Entity | Checks if the given skill is in cooldown for the target |
| [SpawnReason](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/SpawnReason) | Entity | Checks against the spawn reason of the target |
| [Sprinting](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/Sprinting) | Entity | Checks if the target **Player** is sprinting |
| [Stance](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/stance) | Entity | Checks the stance of the target mob |
| [StatDamageModifier](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/StatDamageModifier) | Meta | Used in stat triggers to check the increased damage (as a multiplier). |
| [StringEmpty](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/StringEmpty) | Meta | Checks if the provided string is empty |
| [StringNotEmpty](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/StringNotEmpty) | Meta | Checks if the provided string is not empty |
| [StringEquals](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/stringequals) | Meta | Checks if value1 equals value2. Both values can use variables and placeholders. |
| [Structure](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/structure) | Location | Matches if the target location is inside of a structure |
| [Sunny](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/sunny) | Location | If the weather is sunny in the target world. |
| [TargetInLineOfSight](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targetinlineofsight) | Entity | Tests if the target has line of sight to their target |
| [TargetNotInLineOfSight](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targetnotinlineofsight) | Entity | Tests if the target doesn't have line of sight to their target |
| [TargetWithin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targetwithin) | Entity | Tests if the target's target is within a certain distance |
| [TargetNotWithin](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targetnotwithin) | Entity | Tests if the target's target is not within a certain distance |
| [Targets](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targets) | Meta | Tests if the number of inherited targets from the parent skilltree matches the given range. |
| [TemplateType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/TemplateType) | Entity | Checks if the target mob extends the specified Template |
| [Thundering](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/thundering) | Location | If it's thundering in the target world |
| [TriggerBlockType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/TriggerBlockType) | Meta | Checks against the material type that triggered the skill |
| [TriggerItemType](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/TriggerItemType) | Meta | Checks against the item material type that triggered the skill |
| [VariableContains](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/VariableContains) | Meta | Checks if the given variable contains a certain value |
| [VariableEquals](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/variableequals) | Meta | Checks if the given variable has a particular value. |
| [VariableInRange](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/variableinrange) | Meta | Checks if the given numeric variable is within a certain range. |
| [VariableIsSet](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/variableisset) | Meta | Checks if the given variable is set. |
| [VehicleIsDead](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/vehicleisdead) | Entity | Checks if the casters mounted vehicle is dead. |
| [Velocity](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/Velocity) | Entity | Checks the velocity of the target entity against a range. |
| [Wearing](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/wearing) | Entity | Tests what the target entity has equipped. |
| [World](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/world) | Location | Checks the name of the target world. |
| [WorldTime](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/worldtime) | Location | Matches a range against the target location's world's time. |
| [Yaw](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/yaw) | Entity | Checks the yaw of the target entity against a range. |
| [xDiff](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/xdiff) | Entity | Checks the difference in X between the targeted entity and the caster. |
| [yDiff](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/ydiff) | Entity | Checks the difference in Y between the targeted entity and the caster. |
| [zDiff](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/zdiff) | Entity | Checks the difference in Z between the targeted entity and the caster. |

## More Examples

```yaml
FlameShock:
  Cooldown: 1
  Conditions:
  - targetwithin 15
  - targetinlineofsight true
  - incombat
  - stance aggressive
  - onblock GRASS
  - offgcd
  Skills:
  - gcd{t=60}
  - message{m="<mob.name> begins casting a spell"}
  - potion{t=SLOW;d=60;l=7}
  - delay 60
  - message{m="<target.name> &ecombusts"}
  - effect:particles{p=flame;a=20;hS=3;vS=1;s=0;y=2}
  - potion{t=HARM;d=1;l=1}
```

[1] Not all conditions may be applicable everywhere.
