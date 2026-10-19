---
title: 刷怪点
source_url: https://wiki.mythiccraft.io/mythicmobs/Spawners
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 刷怪点 {#spawners}

## **警告：刷怪点配置文件一旦加载到运行中的服务器，就只能通过游戏内命令编辑。如果要使用文本编辑器修改已经加载的刷怪点配置文件，必须先关闭服务器，再编辑该文件。** {#warning-once-a-spawner-configuration-file-has-been-loaded-onto-a-running-server-it-can-only-be-edited-by-ingame-commands-if-you-want-to-edit-an-already-loaded-spawner-configuration-file-in-a-text-editor-you-have-to-stop-the-server-before-you-edit-the-file}

刷怪点用于在世界中指定生成自定义生物的位置，支持条件、内置计时器、冷却和预热等多种选项。

可以使用[命令](https://wiki.mythiccraft.io/commands%20and%20permissions)直接在游戏内创建刷怪点，也可以在 */MythicMobs/Spawners* 文件夹中创建配置文件。

### 刷怪点的优点 {#pros-of-spawners}

- 无需开启自然生物生成也能工作。
- 可以精确指定各个生物的生成位置和方式，更细致地控制生成行为。
- 支持计时器、牵引及其他功能。
- 适合在小型竞技场或地牢中布置生物。

### 刷怪点的缺点 {#cons-of-spawners}

- 设置可能较为耗时，尤其是需要布置大量刷怪点时。
- 如果缺少合理规划，管理可能会变得十分困难。
- 生物需要适当配置。

## 配置示例 {#example-config}

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

## 选项 {#options}

**值表达式：**数值选项（Radius、RadiusY、MaxMobs、MobLevel、MobsPerSpawn、Cooldown、Warmup、ActivationRange、LeashRange、Chance）均支持以下写法：

- 固定值 (`10`, `0.5`)
- 使用 `XtoY` 格式的随机范围（`10to20`、`0.1to0.5`），每次使用该选项时重新随机取值
- 占位符或数学表达式（数学/变量占位符需要 MythicMobs Premium）

| 选项 | 说明 | 用法 | 默认值 |
| --- | --- | --- | --- |
| **mobtype: <mobtype>** or **mobname: <mobtype>:** | 刷怪器生成的生物类型，只能设为 MythicMobs 内部生物。允许使用带权重的生物数组。 | /mm s set [name] mobtype 25%Mob1,25%Mob2,50%mMob2 | N/A |
| **world: <worldname>:** | 刷怪器所在世界的文件名。 | /mm s set <name> world <world> | 创建刷怪点时所在的世界 |
| **spawnergroup: <group name>** | 设置刷怪器的分组名称。对于规模较大的配置，例如填充地牢时，可以将所有刷怪器归入同一组，再同时更改它们的设置。 | /mm s set g:<group> <setting> <value> | N/A |
| **X: / Y: / Z:** | 刷怪器的坐标。 |  | 创建刷怪点时的位置 |
| **radius: <number>** | 生物可生成的刷怪器周围半径。 | /mm s set <name> radius <radius> | 0 |
| **radiusY: <number>** | 生物可生成的刷怪器周围竖直半径。 | /mm s set <name> radiusy <radius> | 0 |
| **usetimer: <true/false>** | 刷怪器是否按计时器激活。 | /mm s set <name> usetimer <true/false> | True |
| **maxmobs: <number>** | 此刷怪器生成且同时存在于世界中的生物数量上限。**必须大于或等于 mobsperspawn**。 | /mm s set <name> maxmobs <amount> | 1 |
| **moblevel: <number>** | 此刷怪器生成的生物等级。生物必须具有等级配置，此项才会生效。 | /mm s set <name> moblevel <level> | 1 |
| **mobsperspawn: <number>** | 刷怪器每次生成的生物数量。 | /mm s set mobsperspawn <amount> | 1 |
| **cooldown: <number>** | 生成一个生物后，刷怪器在生成下一个生物前等待的时间，单位为秒。 | /mm s set cooldown | 0 |
| **cooldowntimer: <number>** | 此选项由刷怪器自动设置，用于在服务器重启后延续冷却。 | *无需用户设置* |  |
| **warmup: <number>** | 刷怪器开始冷却前的等待时间，单位为秒。激活时会开始预热；达到 maxmobs 后有生物死亡时，也会开始预热。 | /mm s set warmup | 0 |
| **warmuptimer: <number>** | 此选项由刷怪器自动设置，用于在服务器重启后延续预热。 | *无需用户设置*。 |  |
| **checkforplayers: <true/false>** | 刷怪器“激活”时，是否必须有玩家在附近。 |  | true（为改善性能，建议使用） |
| **activationrange: <number>** | 玩家必须位于刷怪器多大半径内，才能激活刷怪器。 |  | 40 blocks |
| **leashrange: <number>** | 生物离开出生位置后可移动的最大距离，超过后会被传送回去。 | /mm s set <name> leashrange <distance> | -1(none) |
| **healonleash: <true/false>** | 生物被拉回刷怪器时，是否恢复全部生命值。 | /mm s set <name> healonleash <true/false> | false |
| **resetthreatonleash: <true/false>** | 生物传送回刷怪器时，重置 ThreatTables（如果已启用）。 |  | false |
| **showflames: <true/false>** | 设为 true 时，在刷怪器周围显示火焰。 | /mm s set <name> showflames <true/false> | false |
| **breakable: <true/false>** | 决定刷怪器是否随其所在方块一起被破坏。 |  | false |
| **chance: <number>** | 刷怪器原本应生成生物时，实际进行生成的概率，范围为 0.0-1.0。随机判定失败不会启动冷却或预热，并会在下一刻重试。 | /mm s set <name> chance <chance> | 1 |
| **randomrotation: <true/false>** | 生成的生物是否采用随机旋转角度，而不是刷怪器配置的 yaw/pitch。 | /mm s set <name> randomrotation <true/false> | false |
| **useworldscaling: <true/false>** | 是否将世界等级缩放加成计入所生成生物的 MobLevel。仅在设置了 MobLevel 时适用；以默认等级生成的生物不受影响。 | /mm s set <name> useworldscaling <true/false> | false |
| **conditions:** | 激活刷怪器所必须满足的条件。 | /mm s addcondition <name> <condition> <action> | None |
| **SpawnConditions** | 尝试生成生物的位置所必须满足的条件。 |  | None |
| **activemobs: <number>** | 用于追踪与刷怪器关联，即由其生成的生物。 | *无需用户设置*。 |  |

**关于生成时间的注意事项：** `Timing: warmup-> mob spawns-> cooldown-> mob spawns*>`
