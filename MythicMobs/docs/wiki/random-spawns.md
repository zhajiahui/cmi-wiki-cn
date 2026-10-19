---
title: 随机生成
source_url: https://wiki.mythiccraft.io/mythicmobs/Random-Spawns
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 随机生成 {#random-spawns}

RandomSpawns 让你可以完全控制生物在你的世界中的生成方式。你可以完全自定义怪物生成的位置、频率和数量，从而可以精确控制怪物生成。

这是你第一次制作RandomSpawn吗？考虑阅读[初学者RandomSpawns指南](guides/your-first-random-spawn.md)

## 重要区别 {#important-differences}

有一些主要的 randomspawn 选项需要区分：

- **Action: REPLACE**
  - REPLACE 动作用于用你自己的生物替换 Minecraft 自己的随机生成系统生成的生物。
  - 这允许完全控制 Minecraft 的生成系统。
  - 如果服务器关闭了 Minecraft 的随机生成，例如将游戏规则 doMobSpawning 设为   false  ，这个动作就不会执行任何操作。

- **Action: ADD**
  - ADD 使用 MythicMobs 自己的生成算法，以类似 Minecraft 生成系统的方式，在玩家周围创建随机生成点。
  - 然而，与 Minecraft 不同，这些生成点将在没有任何条件的情况下生成，允许你在任何光照水平和任何位置生成生物。
  - 有关如何生成这些生成点的详细配置可以在MythicMobs 的配置文件“config.yml”中找到。
  - **注意：**Action: ADD 只在生存或冒险模式玩家附近生成点，而且必须存在位置。
  - 若使用需要实体的条件，会抛出异常。生物群系条件可改用 Biomes: 选项。
  - 要使用 Action: ADD，必须在 `plugins/MythicMobs/config/config-spawning.yml` 中将 GenerateSpawnPoints 设为   true  ！

- **Action: DENY**
  - 拒绝动作可用于防止怪物生成。
  - 任何符合配置了 DENY 的 RandomSpawn 条件的生物都不会生成。

- **Action: SCALE**
  - *即将推出的功能*

## 选项 {#options}

所有可用 randomspawn 选项的完整列表。

### 全局随机生成选项 {#global-randomspawn-options}

#### 示例 {#example}

```yaml
    my_favorite_randomspawn:
      Action: ADD
      Type: cute_zombie
      Level: 2
      Chance: 0.01
      Priority: 10
      UseWorldScaling: false
      Worlds: my_overworld,my_overworld_nether
      Biomes: JUNGLE,PLAINS
      Conditions:
      - day true
```

- **Action: [action]**
  - 要使用的生成方法，默认为“ADD”
  - Action: ADD
  - Action: REPLACE

- **Type: [mobtypes]**
  - 定义要生成的生物的类型。可以是数组/多种生物类型
  - Type: SuperZombie
  - Type: SkeletalMage,WitchBoss
  - 也可以使用原版生物类型。
  - 也可以使用以下语法，让同一个 randomspawn 按不同权重生成多种生物。

```yaml
Deeps:
  Types:
  - RegularZombie 100
  - BigZombie 50
  - GiantZombie 5
  - HugeZombie 1
  Worlds: world
  Chance: 0.1
  Priority: 1
  Action: ADD
  PositionType: LAND
```

- **Level: [number]**
  - 指定生物应生成的级别。
  - 必须是固定数字，不会解析数字范围
  - 可能会被世界缩放设置覆盖（选项见下文）
  - 默认为1
  - Level: 7

- **Chance: [number]**
  - 生物产生的机会。
  - 默认为 1 [1]
  - **Chance: 0.025**

- **Priority: [number]**
  - 同一生成点有多个可用随机生成配置时，决定优先选择哪一个。
  - 一般来说：*优先级数值越高，同时存在多个候选生物时被选中的概率越高*。
  - 默认为1
  - **Priority: 128**

- **UseWorldScaling: [true/false]**
  - 生成的生物的等级是否应该受到世界缩放设置的影响
  - 默认为  true  

- **Conditions: [list]**
  - 用于进一步塑造随机生成的条件列表。
  - 任一指定条件未满足，随机生成就会失败。
  - 可用条件的完整列表可以在这里找到：[条件手册页](skills/conditions.md#conditions)
  - **Conditions:**
  - **- condition 1**
  - **- condition 2**
  - **...**

- **Worlds: [worldnames]**
  - 应应用随机生成的世界的名称。
  - 可以是数组/多个世界
  - 这些名称与你的 Minecraft 世界在游戏文件中的命名方式相对应
  - **Worlds: world**
  - **Worlds: world,world_the_end,world_nether**
  - **Worlds: jays_overworld**

- **Biomes: [biomes]**
  - 指定生物类型可以在其中生成的生物群系。
  - 可以是一个数组/多个生物群落
  - **Biomes: SNOWY_TUNDRA,ICE_SPIKES,SNOWY_TAIGA,...**

- **Reason: [reason]**
  - minecraft-randomspawn要匹配的原因
  - 可以是数组/多个原因
  - 如果此选项存在，则 randomspawn 仅在符合指定原因之一时才起作用
  - 可以是此列表中的任何内容：[CreatureSpawnEvent.SpawnReason](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/CreatureSpawnEvent.SpawnReason.html)
  - **Reason: NATURAL**

- **PositionType: [LAND/SEA]**
  - 这个RandomSpawn是否应该使用陆地或海洋点来生成
  - 仅适用于 Action: ADD。
  - **PositionType: LAND**

- **Cooldown: [number]**
  - 同一RandomSpawn生成两个生物之间必须经过的时间间隔（以秒为单位）
  - 自 MythicMobs 5.2.0 加入。
  - **Cooldown: 60**

- **Structures: [list]**
  - 生物可以在其中生成的结构列表。如果设置，生物将只能在那里生成。

```yaml
Nether_Fortress:
  Types:
  - blaze_wisp 100
  - blazer 60
  - blaze_soldier 60
  - blaze_skeleton 50
  Worlds: world_nether
  Chance: 0.02
  Priority: 1
  Action: ADD
  PositionType: LAND
  Structures:
  - 'minecraft:fortress'
  - 'incendium:forbidden_castle'
  - 'incendium:infernal_altar'
```

### config.yml 中的额外选项 {#extra-options-in-configyml}

你可以在 `MythicMobs/config/config-spawning.yml` 文件中找到常规 RandomSpawn 选项，以及可以在[此处](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Config/config-spawning)找到的最新副本
