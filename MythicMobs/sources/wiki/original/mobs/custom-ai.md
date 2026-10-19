1. [AI Goal Selectors](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-goal-selectors)
   1. [All Mobs](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#all-mobs)
   2. [Creatures Only](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#creatures-only)
   3. [Animals Only](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#animals-only)
   4. [Creepers Only](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#creepers-only)
   5. [Ranged Entities Only](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ranged-entities-only)
   6. [Piglins and Pillagers Only](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#piglins-and-pillagers-only)
2. [AI Target Selectors](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-target-selectors)
   1. [All Creatures](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#all-creatures)
   2. [All Creatures (Faction Support)](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#all-creatures-faction-support)
3. [AI Pathfinding Malus](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#ai-pathfinding-malus)
   1. [Examples](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#examples)
   2. [Path Types](https://wiki.mythiccraft.io/mythicmobs/Mobs/Custom-AI#path-types)

# AI Goal Selectors {#ai-goal-selectors}

Goal Selectors are used with the AIGoalSelectors field and determine what mobs want to “do”. Certain custom goals might not work if they're not included in the base AI of the mob you're creating. For example, a zombie won't be able to use the AI goal “EatGrass” because a zombie would never use that goal in the first place. Feel free to experiment to figure out what does and doesn't work!

Note: Certain goals will not work correctly if the world is in peaceful mode.

Example:

```yaml
SuperMob:
  Type: zombie
  Health: 200
  Display: 'Superb Zombie'
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
```

This zombie would attack players, and walk around randomly when not targeting an enemy.

## All Mobs {#all-mobs}

| AI Goal | Aliases | Description |
| --- | --- | --- |
| clear | reset | Removes the AI from the mob |
| [breakdoors](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/BreakDoor) |  | Causes the mob to break down doors it runs into |
| [eatgrass](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/EatGrass) |  | Makes the mob occasionally… eat grass |
| [float](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/Float) | swim | Makes the mob swim in water/not |
| [lookatplayers](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/lookatplayers) |  | The mob will look at nearby players |
| [LookAtTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/LookAtTarget) |  | The mob will look at its target |
| [opendoor](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/OpenDoor) | opendoors | The mob will open doors it runs into and close the door behind it |
| [randomlookaround](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/RandomLookAround) | lookaround | The mob will randomly look around |
| [gotospawnlocation](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/gotospawn) | gotospawn | Mob will pathfind to its spawn location |
| [doNothing](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/doNothing) **[Premium-only]** |  | Causes the mob to do nothing if conditions are met. |

## Creatures Only {#creatures-only}

| AI Goal | Aliases | Description |
| --- | --- | --- |
| [meleeattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/meleeattack) |  | Causes the mob to move to and melee-attack its target |
| [meleeAttackConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/meleeAttackConditional) | meleeAttackCond | Causes the mob to move to and melee-attack its target while the target matches some conditions |
| [movetowardstarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveTowardsTarget) |  | Causes the mob to move towards its target |
| [randomstroll](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/RandomStroll) |  | The mob will randomly walk around |
| [restrictsun](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/RestrictSun) |  | Will prevent the mob from entering sunlight |
| [fleeplayers](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleeplayers) | runfromplayers | Causes the mob to avoid Players |
| [fleegolems](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleegolems) | runfromgolems | Causes the mob to avoid Iron Golems |
| [fleevillagers](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleevillagers) | runfromvillagers | Causes the mob to avoid villagers |
| [fleewolf](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleewolf) | runfromwolves | Causes the mob to avoid wolves |
| [fleefaction](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleefaction) | runfromfaction | Causes the mob to avoid entities in a given faction |
| [fleesun](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleesun) |  | The mob will hide in the shade when the sun it out |
| [fleeConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/fleeconditional) **[Premium-only]** | fleeIf | Causes the mob to flee based on provided conditions. Safe speed is required for distances greater than 5 |
| [spiderattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/SpiderAttack) |  | Uses the attack a spider would |
| [zombieattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/ZombieAttack) |  | Zombie melee attack |
| [leapattarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/leapattarget) |  | Makes the mob leap at its target |
| [movethroughvillage](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movethroughvillage) |  |  |
| [movetoblock](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movetoblock) |  | Makes the mob go towards a specific type of block |
| [movetolava](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movetolava) |  | Makes the mob move towards lava |
| [movetowater](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/movetowater) |  | Makes the mob move towards water |
| [movetowardsrestriction](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveTowardsRestriction) |  | Make a mob move towards its "Restriction Point" for some Entities (for instance, the village of a Villager) |
| [MoveWithinDistanceOfTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveWithinDistanceOfTarget) |  | Moves towards the target to be within a certain range |
| [MoveWithinDistanceOfTargetConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveWithinDistanceOfTargetConditional) | moveWithinConditional, moveWithinCond | Moves towards the target to be within a certain range while the target matches some conditions |
| [MoveTowardsTargetConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/MoveTowardsTargetConditional) |  | Paths to an entity that checks some conditions |
| [FollowRoute](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/FollowRoute) | followpath | Makes the mob follow a specific path, one time only. |
| [patrol](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/Patrol) x1,y1,z1;x2,y2,z2;x3,y3,z3;… | patrolroute | Makes the mob patrol between the specified locations |
| [gotolocation](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/GoToLocation) x,y,z | goto | Makes the mob go to the specified location(Notice Followrange must more than the distance between location and mob) |
| [goToLocationConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/goToLocationConditional) | gotoConditional, goToLocationCond, gotoCond | Makes the mob go to a location while the location and the mob match some conditions |
| [gotoowner](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/GoToOwner) # |  | Makes the mob move towards its [owner](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner) when beyond a certain distance (defaults to 5 blocks) [Followrange](https://wiki.mythiccraft.io/mythicmobs/Mobs/Options#followrange) must be more than the distance between the owner and the mob) |
| [gotoparent](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/GoToParent) |  | Makes the mob move towards its parent mob |
| [Panic](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/Panic) | panicWhenOnFire | Run around panicking when on fire and look for water |
| [randomFly](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/RandomFly) |  | Fly around randomly |
| [randomNod](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/RandomNod) |  | Makes the mob randomly nod its head |
| [horrified](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/Horrified) |  | Run around frantically |

## Animals Only {#animals-only}

| AI Goal | Aliases | Description |
| --- | --- | --- |
| [breed](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/breed) |  | Causes the mob to be able to breed with other mobs |

## Creepers Only {#creepers-only}

| AI Goal | Aliases | Description |
| --- | --- | --- |
| [creeperswell](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/CreeperSwell) | creeperexplode | Make a creeper want to explode on its target |

## Ranged Entities Only {#ranged-entities-only}

| AI Goal | Aliases | Description |
| --- | --- | --- |
| [rangedattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/arrowattack) | arrowattack | A basic ranged/projectile attack |
| [bowattack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/bowattack) | bowshoot, bowmaster | An advanced bow attack. |
| [arrowAttackConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/arrowAttackConditional) | rangedAttackConditional, arrowAttackCond | A basic ranged/projectile attack while the target matches some conditions |
| [bowAttackConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/bowAttackConditional) | bowAttackCond | An advanced bow attack while the target matches some conditions |

## Piglins and Pillagers Only {#piglins-and-pillagers-only}

| AI Goal | Aliases | Description |
| --- | --- | --- |
| [crossbowAttack](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/crossbowattack) |  | attack with a crossbow |
| [crossbowAttackConditional](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/goals/crossbowAttackConditional) | crossbowAttackCond | attack with a crossbow while the target matches some conditions |

# AI Target Selectors {#ai-target-selectors}

Target Selectors are used with the AITargetSelectors field and determine what mobs try to target.

> If the mob has AITargets but not AIGoal that allows them to act based on their target, they will *still* be considered to have valid targets chosen according to the AITargets used (so, for instance, a @target targeter can be used and so on)

Example

```yaml
SuperMob:
  Type: zombie
  Health: 200
  Display: 'Superb Zombie'
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
  AITargetSelectors:
  - clear
  - players
  - golems
```

## All Creatures {#all-creatures}

| AI Target | Aliases | Description |
| --- | --- | --- |
| clear |  | Special Option. Clears all of the mob's AI |
| [hurtbytarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/HurtByTarget) | attacker, damager | Targets whatever attacks the mob |
| [monsters](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/Monsters) | monster | Targets monsters |
| [Players](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/Players) | player | Targets players |
| [Villagers](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/Villagers) | villager | Targets villagers |
| [irongolem](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/Irongolems) | irongolem, iron_golems, iron_golem | Targets Golems |
| [nearestConditionalTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/nearestconditionaltarget) **[Premium-only]** | nearestConditional, nearestIf | Targets the nearest entity that meets the conditions provided |
| [OwnerAttacker](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/OwnerAttacker) | ownerHurtBy, ownerHurtByTarget, ownerDamager | Targets whatever attacks the mob's owner |
| [OwnerTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/OwnerTarget) | ownerAttack, ownerhurt | Targets whatever the mob's owner attacks. |
| [ParentHurtBy](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/ParentHurtBy) | parentHurtByTarget, parentDamager, parentAttacker | Targets the entity that attacks the mob's parent |
| [ParentTarget](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/ParentTarget) | parentHurt, parentAttack | Targets the entity that is being hit by the caster's parent |

## All Creatures ([Faction](https://wiki.mythiccraft.io/mythicmobs/Mobs/Factions) Support) {#all-creatures-faction-support}

| AI Target | Aliases | Description |
| --- | --- | --- |
| [NearestOtherFaction](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/NearestOtherFaction) | OtherFaction | Targets ANY entities that are in a different faction |
| [NearestOtherFactionMonsters](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/NearestOtherFactionMonsters) | OtherFactionMonsters | Targets any monster that is in a different faction |
| [SpecificFaction](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/specificfaction) [faction_name] |  | Targets any entities that are in the given faction |
| [SpecificFactionMonsters](https://wiki.mythiccraft.io/mythicmobs/Mobs/ai/targets/specificfactionmonsters) [faction_name] |  | Targets any monsters that are in the given faction |

# AI Pathfinding Malus {#ai-pathfinding-malus}

The AIPathfindingMalus field overrides how the mob's navigation weighs specific path types when calculating paths. Each entry is a path type name followed by a value, separated by a space. The values are applied when the mob spawns and re-applied when it loads.

- A negative value (e.g. -1) makes the path type impassable
- A value of 0 means no penalty
- A positive value makes the path type more expensive to cross, so paths through it are avoided when alternatives exist

Movement goals that pick their own destination (such as randomstroll or the flee goals) only accept candidate positions whose path type malus is exactly 0. A positive malus is enough to make a spot invalid as a destination, even though the mob would still cross it while following a path.

## Examples {#examples}

Let a ground mob wander across ponds. Land mobs default WATER to 8, so goals like randomstroll can never pick a target on water and a mob floating mid-pond will not move at all:

```yaml
PondWanderer:
  Type: pig
  AIPathfindingMalus:
  - WATER 0
  AIGoalSelectors:
  - clear
  - randomstroll
  - float
```

Keep a mob from ever pathing into water. A negative malus makes water impassable to its navigation (it can still be knocked or pushed in):

```yaml
DuneStalker:
  Type: husk
  AIPathfindingMalus:
  - WATER -1
```

Stop a fire-immune mob from detouring around burning ground. FIRE (fire, magma blocks, lit campfires) defaults to 16, and walkable blocks next to fire or lava default to 8:

```yaml
CinderBrute:
  Type: zombified_piglin
  AIPathfindingMalus:
  - FIRE 0
  - FIRE_IN_NEIGHBOR 0
```

Path straight through cactus fields and berry thickets. DAMAGING blocks are impassable by default, so mobs normally route around them. The mob still takes their damage unless it is immune:

```yaml
BrambleBoar:
  Type: hoglin
  AIPathfindingMalus:
  - DAMAGING 0
  - DAMAGING_IN_NEIGHBOR 0
```

Let a mob cross minecart tracks. Rails a mob is not already standing on count as UNPASSABLE_RAIL (default -1), which is why mobs refuse to walk over them:

```yaml
RailRunner:
  Type: zombie
  AIPathfindingMalus:
  - UNPASSABLE_RAIL 0
```

Treat the tree canopy as walkable ground. Leaf blocks are impassable to pathfinding by default, even though mobs can physically stand on them:

```yaml
CanopyStalker:
  Type: spider
  AIPathfindingMalus:
  - LEAVES 0
```

## Path Types {#path-types}

Valid names come from the server version's PathType enum. On current versions:

| Path type | Default | Applies to |
| --- | --- | --- |
| `BLOCKED` | -1 | Solid blocks that cannot be pathed through |
| `OPEN` | 0 | Air with no floor below |
| `WALKABLE` | 0 | Normal walkable ground |
| `WALKABLE_DOOR` | 0 | Closed wooden doors, for mobs whose AI can open doors |
| `TRAPDOOR` | 0 | Trapdoors, lily pads, big dripleaf |
| `POWDER_SNOW` | -1 | Powder snow |
| `ON_TOP_OF_POWDER_SNOW` | 0 | Standing on powder snow |
| `FENCE` | -1 | Fences, walls, closed fence gates |
| `LAVA` | -1 | Lava |
| `WATER` | 8 | Water |
| `WATER_BORDER` | 8 | Walkable block next to water |
| `RAIL` | 0 | Rails, while the mob is already on rails |
| `UNPASSABLE_RAIL` | -1 | Rails the mob is not already standing on |
| `FIRE_IN_NEIGHBOR` | 8 | Walkable block next to fire or lava |
| `FIRE` | 16 | Fire and soul fire, magma blocks, lit campfires, lava cauldrons |
| `DAMAGING_IN_NEIGHBOR` | 8 | Walkable block next to a damaging block |
| `DAMAGING` | -1 | Cactus, sweet berry bushes |
| `DOOR_OPEN` | 0 | Open doors |
| `DOOR_WOOD_CLOSED` | -1 | Closed doors that can be opened by hand |
| `DOOR_IRON_CLOSED` | -1 | Closed doors that need redstone |
| `BREACH` | 4 | Air directly above water (swim navigation, breaching) |
| `LEAVES` | -1 | Leaf blocks |
| `STICKY_HONEY` | 8 | Honey blocks |
| `COCOA` | 0 | Cocoa pods |
| `DAMAGE_CAUTIOUS` | 0 | Wither roses, pointed dripstone |
| `ON_TOP_OF_TRAPDOOR` | 0 | Standing on a trapdoor |
| `BIG_MOBS_CLOSE_TO_DANGER` | 4 | Mobs wider than one block whose hitbox clips a dangerous block |

Older server versions use different names for some of these (the [SetPathfindingMalus](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetPathfindingMalus) mechanic page has the legacy table). An invalid name logs a config error and the entry is skipped.

The [setpathfindingmalus](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SetPathfindingMalus) mechanic changes the same values at runtime from skills.
