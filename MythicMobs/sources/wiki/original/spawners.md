# Spawners

## **WARNING: Once a spawner-configuration file has been loaded onto a running server, it can only be edited by ingame commands. If you want to edit an already loaded spawner-configuration file in a text-editor, you have to stop the server before you edit the file.** {#warning-once-a-spawner-configuration-file-has-been-loaded-onto-a-running-server-it-can-only-be-edited-by-ingame-commands-if-you-want-to-edit-an-already-loaded-spawner-configuration-file-in-a-text-editor-you-have-to-stop-the-server-before-you-edit-the-file}

Spawners allow you to define specific points in your worlds at which your custom mob creations can spawn. They can be used with a variety of useful options such as; conditions, built-in timers, cooldowns, and warmups.

You can create spawners directly ingame by using [Commands](/commands and permissions) or by creating the a configuration file in the folder */MythicMobs/Spawners*.

### Pros of Spawners {#pros-of-spawners}

- Doesn't require natural mob spawning to be enabled to work.
- Allows for much more control over your spawning implementation as you can specify exactly where and how each mob spawn.
- Support timers, leashing and other features.
- Great for populating small arenas or dungeons.

### Cons of Spawners {#cons-of-spawners}

- Setup can be time consuming, especially for larger implementations.
- Can become very difficult to manage if not planned out correctly.
- Mobs need to be configured appropriately.

## Example Config {#example-config}

```yaml
SpawnerName:
  MobName: mobTypeName 
  World: worldname
  SpawnerGroup: GroupName
  X: 0 
  Y: 0 
  Z: 0 
  Radius: 0 
  RadiusY: 0 
  UseTimer: true  
  MaxMobs: 1
  MobLevel: 1
  MobsPerSpawn: 1
  Cooldown: 0
  CooldownTimer: 0
  Warmup: 0
  WarmupTimer: 0
  CheckForPlayers: true
  ActivationRange: 40
  LeashRange: 32
  HealOnLeash: false
  ResetThreatOnLeash: false
  ShowFlames: false
  Breakable: false
  Chance: 1
  RandomRotation: false
  UseWorldScaling: false
  Conditions: []
  ActiveMobs: 1
```

## Options {#options}

**Value expressions:** numeric options (Radius, RadiusY, MaxMobs, MobLevel, MobsPerSpawn, Cooldown, Warmup, ActivationRange, LeashRange, Chance) accept all of the following:

- a fixed value (`10`, `0.5`)
- a random range in the `XtoY` format (`10to20`, `0.1to0.5`), rolled again each time the option is used
- a placeholder or math expression (math/variable placeholders require MythicMobs Premium)

| Option | Description | Usage | Default |
| --- | --- | --- | --- |
| **mobtype: <mobtype>** or **mobname: <mobtype>:** | This is mob type that the spawner will spawn. Can only be set to an internal MythicMobs mob. Allows for an array of mobs with weightings. | /mm s set [name] mobtype 25%Mob1,25%Mob2,50%mMob2 | N/A |
| **world: <worldname>:** | This is the filename of the world where the spawner is located | /mm s set <name> world <world> | Creation World |
| **spawnergroup: <group name>** | This sets the group name for the spawn. For larger configurations, such as if you are populating a dungeon, you can group all spawners and then change the settings for them all at the same time. | /mm s set g:<group> <setting> <value> | N/A |
| **X: / Y: / Z:** | Coordinates of the spawner |  | Creation Location |
| **radius: <number>** | This is the radius around the spawner at which the mob can spawn. | /mm s set <name> radius <radius> | 0 |
| **radiusY: <number>** | This is the vertical radius around the spawner at which the mob can spawn | /mm s set <name> radiusy <radius> | 0 |
| **usetimer: <true/false>** | Whether or not the spawner activates on a timer. | /mm s set <name> usetimer <true/false> | True |
| **maxmobs: <number>** | This is the max number of mobs that can be spawned and existing in the world for this spawner. **Must be equal to or greater than mobsperspawn** | /mm s set <name> maxmobs <amount> | 1 |
| **moblevel: <number>** | This is the level of the mob that should spawn from this spawner. Mob must have level configuration for this to work. | /mm s set <name> moblevel <level> | 1 |
| **mobsperspawn: <number>** | This is the number of mobs spawned each time the spawner spawns a mob. | /mm s set mobsperspawn <amount> | 1 |
| **cooldown: <number>** | This the amount of time in seconds that the spawner waits after a mob has been spawned before another mob is spawned. | /mm s set cooldown | 0 |
| **cooldowntimer: <number>** | This option is set automatically by the spawner. Used to bridge cooldowns over server reboots. | *does not require any user setting* |  |
| **warmup: <number>** | The amount of time in seconds before the spawner starts cooldown. Warmup starts on activation and if maxmobs is reached and a mob dies. | /mm s set warmup | 0 |
| **warmuptimer: <number>** | This option is set automatically by the spawner, used to bridge warmups over server reboots. | *does not require any user setting*. |  |
| **checkforplayers: <true/false>** | Whether or not players must be near the spawner for it to "activate" |  | true (recommended for performance) |
| **activationrange: <number>** | What radius must players be within for the spawner to activate. |  | 40 blocks |
| **leashrange: <number>** | This is the max distance that a mob can move from its spawn location before it is teleported back. | /mm s set <name> leashrange <distance> | -1(none) |
| **healonleash: <true/false>** | Whether the mob should heal to full health when it leashes back to its spawner | /mm s set <name> healonleash <true/false> | false |
| **resetthreatonleash: <true/false>** | Resets ThreatTables (if enabled) when a mob teleports back to its spawner. |  | false |
| **showflames: <true/false>** | Set this to true to show flames around the spawner. | /mm s set <name> showflames <true/false> | false |
| **breakable: <true/false>** | Determines if the spawner is broken with the block it is placed on |  | false |
| **chance: <number>** | The chance (0.0-1.0) for the spawner to spawn when it would otherwise spawn. A failed roll arms no cooldown or warmup and is retried on the next tick. | /mm s set <name> chance <chance> | 1 |
| **randomrotation: <true/false>** | Whether spawned mobs get a random rotation instead of the spawner's configured yaw/pitch. | /mm s set <name> randomrotation <true/false> | false |
| **useworldscaling: <true/false>** | Whether the world scaling level bonus is added to the spawned mob's MobLevel. Only applies when MobLevel is set; mobs spawning at their default level are unaffected. | /mm s set <name> useworldscaling <true/false> | false |
| **conditions:** | the conditions to be met for the spawner to activate. | /mm s addcondition <name> <condition> <action> | None |
| **SpawnConditions** | the conditions to be met by the position a mob is being attempted to be spawned at |  | None |
| **activemobs: <number>** | Used to keep track of mobs connected to (spawned by) the spawner. | *it does not require any user setting*. |  |

**Note on timing of spawns:** `Timing: warmup-> mob spawns-> cooldown-> mob spawns*>`
