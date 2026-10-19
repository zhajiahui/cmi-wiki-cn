Targeters are used to determine what a skill targets when it is fired.

While targeters are technically optional (as the default targeter will usually be @trigger), forgetting a targeter is probably one of the most common mistakes people who are new to MythicMobs make.

When a targeter is used on the Skill mechanic, all of the skills inside of the meta-skill inherit the initial targeter. You can still overwrite the parent targeter for individual mechanics inside of the meta-skill by giving them their own targeter to use.

If entity targets are passed to a location-based mechanic, it will use the entity's location.

1. [Additional Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#additional-targeters)
2. [Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#targeters)
   1. [Entity Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#entity-targeters)
      1. [Single-Entity Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#single-entity-targeters)
      2. [Multi-Entity Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#multi-entity-targeters)
      3. [ThreatTable Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#threattable-targeters)
   2. [Location Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#location-targeters)
      1. [Single-Location Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#single-location-targeters)
      2. [Multi-Location Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#multi-location-targeters)
   3. [Meta Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#meta-targeters)
      1. [Meta-Entity Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#meta-entity-targeters)
      2. [Meta-Location Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#meta-location-targeters)
   4. [Special Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#special-targeters)
3. [Common Attributes](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#common-attributes)
   1. [All Targeters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#all-targeters)
      1. [Sudo Attributes](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#sudo-attributes)
   2. [Common Entity Targeters Attributes](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#common-entity-targeters-attributes)
   3. [Common Location Targeters Attributes](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#common-location-targeters-attributes)
4. [Targeter Options](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#targeter-options)
   1. [Target Filters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#target-filters)
      1. [Specific Filters](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#specific-filters)
   2. [Target Limits](https://wiki.mythiccraft.io/mythicmobs/skills/targeters#target-limits)

# Additional Targeters {#additional-targeters}

Links to targeters added by addon plugins. Any targeters from these links will not work without that plugin installed.

- [ModelEngine 4](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Skills/Targeters)
- [Mythic Crucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Targeters)
- [Mythic Enchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Skills/Targeters)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#targeters)

# Targeters {#targeters}

## Entity Targeters {#entity-targeters}

### Single-Entity Targeters {#single-entity-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[Self](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Self) | @Caster @Boss @Mob | Targets the caster of the mechanic |
| @[Target](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Target) | @T | Targets the caster's target |
| @[Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) |  | Targets the entity that triggered the skill |
| @[NearestPlayer](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/NearestPlayer) |  | Targets the nearest player in radius |
| @[WolfOwner](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/WolfOwner) |  | Targets the owner of the wolf |
| @[Owner](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner) |  | Targets the [owner](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setowner) of the mob |
| @[Parent](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Parent) | @summoner | Targets the [parent](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setparent) of the mob |
| @[Mount](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Mount) |  | Targets the caster's original [mount](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#mount) |
| @[Father](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Father) | @dad @daddy | Targets the father of the casting mob. |
| @[Mother](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Mother) | @mom @mommy | Targets the mother of the casting mob. |
| @[Passenger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Passenger) |  | Targets the rider of the casting mob. |
| @[PlayerByName](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayerByName) | @specificplayer | Targets a specific player by name. Supports placeholders. |
| @[UniqueIdentifier](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/UniqueIdentifier) | @UUID | Targets a specific entity by their UUID, supports placeholders |
| @[Vehicle](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Vehicle) |  | Targets the caster's vehicle |
| @[InteractionLastAttacker](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/InteractionLastAttacker) | @lastAttacker | Targets the last entity that attacked the casting `INTERACTION` entity |
| @[InteractionLastInteract](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/InteractionLastInteract) | @lastInteract | Targets the last entity that interacted with the casting `INTERACTION` entity |
| @[OwnerLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Ownerlocation) |  | Targets the position of the owner of the mob |
| @[ParentLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ParentLocation) | @summonerlocation | Targets the position of the parent of the mob |

### Multi-Entity Targeters {#multi-entity-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[LivingInCone](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone) | @entitiesInCone @livingEntitiesInCone @LEIC @EIC | Targets all living entities in cone with a specified angle, length and rotation relative to facing direction |
| @[LivingInWorld](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInWorld) | @EIW | Targets all living entities in the caster's world |
| @[NotLivingNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/NotLivingNearOrigin) | @nonLivingNearOrigin @NLNO | Targets all non living entities in a radius near the origin |
| @[PlayersInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRadius) | @PIR | Targets all players in the given radius |
| @[MobsInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/MobsInRadius) | @MIR | Targets all mythicmobs or vanilla overrides of the given type in a radius |
| @[EntitiesInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRadius) | @livingEntitiesInRadius @livingInRadius @allInRadius @EIR | Targets all entities in the given radius. |
| @[EntitiesInRing](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRing) | @EIRR | Targets all entities in the given ring. |
| @[EntitiesInRingNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRingNearOrigin) | @ERNO | Targets all entities in the given ring around the origin. |
| @[PlayersInWorld](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInWorld) | @World | Targets all players in the current world. |
| @[PlayersOnServer](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersOnServer) | @Server @Everyone | Targets all players in the server. |
| @[PlayersInRing](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRing) |  | Target all players between the specified min and max radius. |
| @[PlayersNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersNearOrigin) | @PNO | Targets players near the [origin](https://wiki.mythiccraft.io/mythicmobs/skills/targeters/origin) of a meta-skill. |
| @[TrackedPlayers](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TrackedPlayers) | @tracked | Targets players that are within the render distance of the caster |
| @[MobsNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/MobsNearOrigin) |  | Targets all MythicMobs or vanilla overrides of the given type(s) in a radius around the origin |
| @[EntitiesNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesNearOrigin) | @ENO | Targets all entities near the [origin](https://wiki.mythiccraft.io/mythicmobs/skills/targeters/origin) of a meta-skill |
| @[Children](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Children) | @child @summons | Targets any child entities summoned by the caster. |
| @[Siblings](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Siblings) | @sibling @brothers @sisters | Targets any mobs that share the same parent as the caster. |
| @[ItemsNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ItemsNearOrigin) |  | Targets item drops near the [origin](https://wiki.mythiccraft.io/mythicmobs/skills/targeters/origin) of a meta-skill. |
| @[ItemsInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ItemsInRadius) | @IIR | Targets all item drops in the given radius |
| @[Bound](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Bound) | @bounds | Targets all living entities inside a cuboid, sphere, or cylinder |

### ThreatTable Targeters {#threattable-targeters}

These targeters only work if the mob has [Threat Tables](https://wiki.mythiccraft.io/mythicmobs/Mobs/ThreatTables) enabled.

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[ThreatTable](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ThreatTable) | @TT | Targets every entity on the casting mob's threat table |
| @[ThreatTablePlayers](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ThreatTablePlayers) |  | Targets all the players on the casting mob's threat table |
| @[RandomThreatTarget](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomThreatTarget) | @RTT | Targets a random entity on the casting mob's threat table |
| @[RandomThreatTargetLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomThreatTargetLocation) | @RTTL | Targets the location of a random entity on the casting mob's threat table |

## Location Targeters {#location-targeters}

### Single-Location Targeters {#single-location-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[SelfLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/SelfLocation) | @casterLocation @bossLocation @mobLocation | Targets the caster's location |
| @[SelfEyeLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/SelfEyeLocation) | @eyeDirection @casterEyeLocation @bossEyeLocation @mobEyeLocation | Targets the caster's eye location |
| @[Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) |  | Targets a location in front of caster's facing direction |
| @[ProjectileForward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ProjectileForward) |  | Targets a location in front of the casting projectile, relative to its direction |
| @[TargetLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetLocation) | @targetloc @TL | Targets the caster's target's location |
| @[TargetPredictedLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetPredictedLocation) | @targetPredictedLoc @TPL @PredictedTargetLocation | Targets the predicted location at which the caster's top target will be after an amount of ticks has elapsed, based on its current movement speed |
| @[TriggerLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TriggerLocation) |  | Targets the location of the entity that triggered the skill |
| @[SpawnLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/SpawnLocation) |  | Targets the world's spawn location. |
| @[CasterSpawnLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/CasterSpawnLocation) |  | Targets the location the caster spawned at. |
| @[Location](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Location) |  | Targets the specified coordinates in the caster's world. |
| @[Origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin) | @source | Targets the location of the "origin" or "source" of a meta-skill. While that is usually the casting mob, there are special cases where this is not true (such as with the Projectile Skill, where the "origin" is the location of the projectile). |
| @[ObstructingBlock](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ObstructingBlock) |  | Tries to target the block in front of the caster that is obstructing it |
| @[TargetBlock](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetBlock) |  | Targets the block the casting player is looking at. |
| @[TrackedLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TrackedLocation) |  | Targets the mob's tracked location |
| @[NearestStructure](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/NearestStructure) |  | Targets the nearest structure of the specified type within a radius in the caster's world |
| @[VariableLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/VariableLocation) | @varLocation | Targets the location stored in the specified variable |
| @[HighestBlock](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/HighestBlock) |  | Targets the highest block at the skill origin |
| @[PlayerLocationByName](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayerLocationByName) |  | Targets a specific player's location by their name |
| @[EscapeLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EscapeLocation) |  | Targets a nearby safe escape location like how an Enderman would choose its teleport destination |

### Multi-Location Targeters {#multi-location-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[ForwardWall](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ForwardWall) |  | Targets a plane in front of the caster |
| @[PlayerLocationsInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayerLocationsInRadius) | @PLIR | Targets all player locations in the given radius |
| @[Pin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Pin) |  | Targets the location(s) of a [pin](https://wiki.mythiccraft.io/mythicmobs/Pins). |
| @[Ring](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Ring) |  | Target points to form a ring of locations |
| @[RandomRingPoint](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomRingPoint) |  | Targets random points in a ring around the caster |
| @[Cone](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Cone) |  | Returns the # of points target locations that comprise a cone (Note: Cone is fixed on the y-axis, and cannot be rotated up or down) |
| @[Sphere](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Sphere) |  | Targets points in a sphere around the caster |
| @[Rectangle](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Rectangle) | @cube @cuboid | Returns the # of points target locations that comprise a rectangle |
| @[RandomLocationsNearCaster](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomLocationsNearCaster) | @randomLocations @RLNC | Targets random locations near the caster. |
| @[RandomLocationsNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomLocationsNearOrigin) | @RLO @randomLocationsOrigin @RLNO | Targets random locations near the origin of a skill. |
| @[BlocksNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksNearOrigin) | @BNO | Targets all blocks in a radius around the origin of the metaskill. |
| @[RingAroundOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RingAroundOrigin) | @ringOrigin @RAO | Targets locations in a specified ring around the origin. |
| @[Spawners](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Spawners) |  | Targets the location of the specified spawners. |
| @[BlocksInPinRegion](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksInPinRegion) |  | Targets the blocks in a region delimited by two pins |
| @[ChunksInWERegion](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ChunksInWERegion) | @chunksInWGRegion | Targets the 0,0 chunk corners of the chunks in a specified WorldGuard region |

## Meta Targeters {#meta-targeters}

Meta Targeters targets relative to an [inherited target](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#inheritance). For example:

```yaml
# Mob file
Laser:
  Type: CREEPER
  Display: 'Laser'
  Health: 12
  AITargetSelectors:
  - 0 clear
  - 1 players
  Skills:
  - skill{s=Laser} @target
```

```yaml
# Skill file
Laser:
  Skills:
  - ignite @EntitiesInLine{r=1}
```

In the example skill above, the "ignite" mechanic will target entities between the caster and the targeter specified in `- skill{s=Laser} @target`, i.e. a line between the caster and the caster's target.

Some meta targeters also allow the mechanic to be casted "fromOrigin". This will change the starting location of the meta-targeter to be @Origin rather than the caster, which can allow for some complex effects, particularly when used with Projectiles.

### Meta-Entity Targeters {#meta-entity-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[LivingInLine](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInLine) | @entitiesInLine @livingEntitiesInLine @LEIL @EIL | Targets any entities in a line between the inherited target and the casting mob. |
| @[LivingNearTargetLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingNearTargetLocation) | @LNTL @ENTL @ENT | Targets all living entities near the inherited target. |
| @[PlayersNearTargetLocations](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersNearTargetLocations) | @playersNearTargetLocation @PNTL | Targets all players near the inherited targets. |
| @[TargetedTarget](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetedTarget) | @Targeted | Targets the inherited targeted entities. |

### Meta-Location Targeters {#meta-location-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[Line](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Line) |  | Targets locations between the mob and the inherited targets. |
| @[RandomLocationsNearTargets](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/RandomLocationsNearTargets) | @randomLocationsNearTarget @randomLocationsNearTargetEntities @randomLocationsNearTargetLocations @RLNT @RLNTE @RLNTL | Targets random locations around the inherited targets. |
| @[FloorOfTargets](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/FloorOfTargets) | @FOT @floorsOfTarget | Targets the blocks underneath the inherited targets. |
| @[LocationsOfTargets](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LocationsOfTargets) | @locationOfTarget @LOT | Targets the location of the inherited target entities. |
| @[TargetedLocation](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetedLocation) | @targetedLocations @targetedLoc | Targets the location of the inherited target locations. |
| @[BlocksInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksInRadius) | @BIR | Targets all blocks in a radius of the inherited targets. |
| @[BlocksInChunk](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlocksInChunk) | @BIC | Targets all blocks in a chunk relative to the inherited target. |
| @[BlockVein](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/BlockVein) | @vein @bv | Target all adjancent blocks that match the blocktype, starting from the origin of the skill. |

## Special Targeters {#special-targeters}

| Targeter | Shorthand | Description |
| --- | --- | --- |
| @[None](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/None) |  | Provides no target. (Useful for mechanics with no target input.) |
| @[Region](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Region) |  | Special targeter to target a region. Only works with specific mechanics |

# Common Attributes {#common-attributes}

There are some common attributes that can be used in most of the Targeters, depending on the targeter's returned value

## All Targeters {#all-targeters}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| targetconditions | conditions, cond, c | [Inline Target Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Inline-Conditions#targetconditions) |  |
| fallback | fb | The fallback targeter to use, if this one returns no target |  |

### Sudo Attributes {#sudo-attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| sudoparent | fromparent, ofparent, asparent, parent, ofparent | If this attribute is set to `true`, the targeter will be parsed as if it was the [Parent](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Parent) of the casting entity executing the mechanic |  |
| sudoowner | fromowner, ofowner, asowner, owner, ofowner | If this attribute is set to `true`, the targeter will be parsed as if it was the [Owner](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner) of the casting entity executing the mechanic |  |
| sudotrigger | fromtrigger, oftrigger, astrigger, trigger, oftrigger | If this attribute is set to `true`, the targeter will be parsed as if it was the [Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) of the skilltree executing the mechanic |  |

In this example, [the mob will keep getting teleported in front of its owner](https://cdn.discordapp.com/attachments/523443579574681600/1101186712174088253/a.gif), since the `Forward` targeter is using the `sudoowner` attribute, and is, as such, getting parsed as if it was the owner of the casting mob executing the mechanic

```yaml
TestOwner:
  Type: Wolf
  Skills:
  - setOwner @NearestPlayer{r=99} ~onSpawn
  - tp @Forward{f=5;y=1;sudoowner=true} ~onTimer:1
```

## Common Entity Targeters Attributes {#common-entity-targeters-attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| useboundingbox | bb | If the targeter is performing a distance check, this option allows it to check against the bounding box of the target instead of the center of its hitbox |  |
| unique | u | The maximum number of times an entity can be targeted. Defaults to 1, disable with 0. This is mostly used for meg models with multiple hitboxes |  |
| nomegbb | nmb | Whether MEG sub hitboxes should be filtered out |  |

## Common Location Targeters Attributes {#common-location-targeters-attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| xoffset | xo, x | Centers the offset on the x axis |  |
| yoffset | yo, y | Centers the offset on the y axis |  |
| zoffset | zo, z | Centers the offset on the z axis |  |
| forwardOffset | foffset, fo | Centers forward and backward offset, based on the caster's viewing angle | 0 |
| sideOffset | soffset, so | Centers left and right offset, based on the caster's viewing angle | 0 |
| upoffset | uoffset, uo | Centers up and down offset, based on the caster's viewing angle | 0 |
| rotatex | rotx | Rotation on the x axis |  |
| rotatey | roty | Rotation on the y axis |  |
| rotatez | rotz | Rotation on the z axis |  |
| coordinatex | cx | Sets the x axis coordinate |  |
| coordinatey | cy | Sets the y axis coordinate |  |
| coordinatez | cz | Sets the z axis coordinate |  |
| length |  | Multiplied the direction vector by the specified value |  |
| blocktypes | blocktype, bt | Only targets selected block types. Multiple blocks can be listed by separating them using a `,` You can add a `#` at the front of the type to indicate that the block only needs to match part of the type, add `@` to indicate that the block only needs to match the start of the type You can add a `*` at the front of the type to indicate that the one specified is not a block type, but a [block tag](https://minecraft.wiki/w/Tag#Block_tags_2) (example: `blocktype=*sculk_replaceable` ) |  |
| blockignores | blockignore, bi | Excludes selected block types from the targeter. Multiple blocks can be listed by separating them using a `,` Can use the special syntaxes specified in `blocktype` |  |
| coordinateyaw | cyaw | Sets the yaw value |  |
| coordinatepitch | cpitch | Sets the pitch value |  |
| blockcentered | centered | Boolean value. If set to true, the center of the block at the target location will be targeted, instead of the target location itself |  |
| faulty |  | Whether the old vector calculation formula should be used | false |
| blockSurface | surface | Whether the plugin should attempt to adjust the location to be on a surface | false |
| blockSurfaceTolerance | surfaceTolerance | The tolerance used when searching for a surface, when `blockSurface` is set to `true` | 5 |

# Targeter Options {#targeter-options}

## Target Filters {#target-filters}

Target Filters allow you to filter out certain targets, and makes targeters a lot more flexible.

They are used with two attributes (available on ANY entity-targeter):

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| target |  | The entity types to target |  |
| ignore |  | The entity types to not target |  |

For example, to make a targeter that will ignore any players or non-hostile mobs, you'd use this:

```yaml
  - damage{a=20} @EntitiesInRadius{r=10;ignore=players,animals}
```

To make a targeter ONLY target players, you'd do something like this:

```yaml
  - skill{s=ASkill} @EntitiesInRadius{r=5;target=players}
```

> You can set the default target filters in MythicMobs/config/config-skills.yml

Possible filters include:

#### Target Attribute {#target-attribute}

| Target Filter | Aliases | Description |
| --- | --- | --- |
| ground |  | Whether to target ground entities. Will ignore flying and water entities if used |
| water |  | Whether to target water entities. Will ignore flying and ground entities if used |
| flying |  | Whether to target flying entities. Will ignore ground and water entities if used |
| self | caster | Whether the caster of the mechanic can be targetd |
| player |  | Whether players can be targeted |
| creative |  | Whether creative mode players can be targeted |
| spectator |  | Whether spectator mode players can be targeted |
| armorstand | armor_stand | Whether armor stands can be targeted |
| marker |  | Whether markers can be targeted |
| textdisplay | text_display | Whether text displays can be targeted |
| itemdisplay | item_display | Whether item displays can be targeted |
| blockdisplay | block_display | Whether block displays can be targeted |
| interaction |  | Whether interaction entities can be targeted |
| npc |  | Whether Citizens NPCs can be targeted |
| animal |  | Whether animals can be targeted |
| creature |  | Whether creatures can be targeted |
| monster |  | Whether monsters can be targeted |
| villager |  | Whether villagers can be targeted |
| vanilla |  | Whether to target only non-Mythic entities. Will ignore Mythic mobs if used |
| mythic |  | Whether to target only Mythic mobs. Will ignore non-Mythic entities if used |

> If neither `ground`, `water` and `flying` are used and the default filters do not include any of them, then `Players`, `ArmorStands`, `Markers`, `TextDisplays`, `ItemDisplays`, `BlockDisplays`, `Interactions`, `Creative`, `Spectator`, `CitizensNPCs`, `Animals`, `Creatures`, `Monsters` and `Villagers` will also be ignored

#### Ignore Attribute {#ignore-attribute}

| Ignore Filter | Aliases | Description |
| --- | --- | --- |
| player |  | Whether players shouldn't be targetd |
| creative |  | Whether creative mode players shouldn't be targeted |
| spectator |  | Whether spectator mode players shouldn't be targeted |
| armorstand | armor_stand | Whether armor stands shouldn't be targeted |
| marker |  | Whether markers shouldn't be targeted |
| textdisplay | text_display | Whether text displays shouldn't be targeted |
| itemdisplay | item_display | Whether item displays shouldn't be targeted |
| blockdisplay | block_display | Whether block displays shouldn't be targeted |
| interaction |  | Whether interaction entities shouldn't be targeted |
| npc |  | Whether Citizens NPCs shouldn't be targeted |
| animal |  | Whether animals shouldn't be targeted |
| creature |  | Whether creatures shouldn't be targeted |
| monster |  | Whether monsters shouldn't be targeted |
| villager |  | Whether villagers shouldn't be targeted |
| faction |  | Whether entities in the same faction shouldn't be targeted |
| owner |  | Whether the caster's owner shouldn't be targeted |
| vanilla | nonmythic | Whether vanilla (non-Mythic) entities shouldn't be targeted |
| mythic |  | Whether Mythic entities shouldn't be targeted |

### Specific Filters {#specific-filters}

You can also specifically set whether to target a specific type of entity or not by using the attributes below. The effects of these attributes override the effects of the more generic target/ignore attributes for the specific entity type the attribute handles

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| targetself |  | Whether to target the caster of the mechanic |  |
| targetplayers |  | Whether to target players |  |
| targetcreative |  | Whether to target players in creative mode |  |
| targetspectator |  | Whether to target players in spectator mode |  |
| targetinvulnerable |  | Whether to target invulnerable entities |  |
| targetarmorstands |  | Whether to target armor stands |  |
| targetmarkers |  | Whether to target markers |  |
| targettextdisplays | targettextdisplay | Whether to target text displays |  |
| targetitemdisplays | targetitemdisplay | Whether to target item displays |  |
| targetblockdisplays | targetblockdisplay | Whether to target block displays |  |
| targetinteractions | targetinteraction | Whether to target interaction entities |  |
| targetnpcs |  | Whether to target Citizens NPCs |  |
| targetanimals |  | Whether to target animals |  |
| targetcreatures |  | Whether to target creatures |  |
| targetsamefaction |  | Whether to target entities of the same faction |  |
| targetowner |  | Whether to target the caster's owner |  |
| targetvanilla | targetnonmythic | Whether to target non-Mythic entities |  |
| targetvillagers |  | Whether to target villagers |  |
| targetall |  | Whether to target everything. If this is true, all filters are ignored | false |

```yaml
  - damage{a=20} @EntitiesInRadius{r=10;targetplayers=true;targetsamefaction=true;targetowner=false}
```

> Use this to explicitly target players and entities in the same faction alongside any other valid target there may be, while also not targeting the owner of the caster

## Target Limits {#target-limits}

All entity and location targeters also support target limits (as of v5.0.4). With this you can limit how many entities/locations are targeted, including the order in which they are selected.

This is done with the attributes:

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| sort | sortby | How to sort the targeted entities/locations. Distance-based sorts are made against the mechanic's origin |  |
| skipTargetsUpToIndex | stuti | skips the first `n` targets of the targeter after the sort is applied, if >0 | 0 |
| limit |  | The limit to the targeted entities/locations after the skip is applied, if >0 | 0 |

Lets say you want your ability to only target the 2 nearest players within 30 blocks. To do this, you'd simply set the limit 2 to and sort by nearest:

```yaml
  - mechanic @PlayersInRadius{r=30;limit=2;sort=NEAREST}
```

Currently, sort can have the following values:

**General sorters:**

- NONE *(usually sorts by how long the entity has existed)*
- RANDOM
- NEAREST *(to the origin of the mechanic)*
- FURTHEST *(from the origin of the mechanic)*

**Entity Only Sorters**

- HIGHEST_HEALTH
- LOWEST_HEALTH
- HIGHEST_THREAT
- LOWEST_THREAT

So the targeter will, in this order:

- Sort the targets based on the provided sort attribute, if any (and if limit and skipTargetsUpToIndex are >0)
- Skip the first n targets based on the skipTargetsUpToIndex attribute's value, if >0
- Return the first n targets based on the value of the limit attribute, if > 0

So, in essence, you can fetch target(s) at specific index(es) by using both limit and skipTargetsUpToIndex

```yaml
GiveRewards:
  Skills:
  - message{m="You are first!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1} #targets the player that has the highest threat
  - message{m="You are second!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1;stuti=1} #targets the player that has the second highest threat
  - message{m="You are third!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;limit=1;stuti=2} #targets the player that has the third highest threat
  - message{m="You aren't on the podium!"} @ThreatTablePlayers{sort=HIGHEST_THREAT;stuti=3} #targets everyone else
```
