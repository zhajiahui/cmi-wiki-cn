---
title: 配置第一个随机生成
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/Your-First-Random-Spawn
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 配置第一个随机生成

**难度：入门**

[随机生成](../random-spawns.md)系统可以让自定义 MythicMobs 生物在世界中随机生成！通过各种选项和条件，可以细调生成规则，让它们按你想要的方式生成！

创建生成规则时，有 2 种可用操作：ADD 和 REPLACE。使用 replace 时，MythicMobs 会覆盖原版生物的生成，因此原版生物会减少，你对生成的控制也更少。add 则会在原版生成点之外创建生成点，因此不会影响原版生成，而且更便于控制。

使用 add 时，必须启用 `/plugins/MythicMobs/config/config-spawning.yml` 中的 `GenerateSpawnPoints` 设置，而且你必须处于生存或冒险模式，生物才会生成。

本指南会使用 ADD 操作，因为一般情况下它是更好的选择。

随机生成配置放在 `/plugins/MythicMobs/RandomSpawns` 文件夹中，也可以放入其子文件夹以便整理。还可以在[包](../packs.md)中创建 `RandomSpawns` 文件夹。

# 基础设置 {#basic-setup}

RandomSpawn 的基本配置包含几个设置。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
```

在这个基本示例中，我们让生物 `SkeletonKing` 有 10% 的概率在 `world` 和 `world_nether` 世界中生成。

- `Action: ADD`：使用 [ADD](../random-spawns.md#important-differences) 操作创建生成点。
- `Type: SkeletonKing`：要生成的 MythicMob 的[内部名称](https://wiki.mythiccraft.io/mythicmobs/Mobs/Mobs#internal_name)。
- `Chance: 0.1`：概率以 1 为基准，因此 0.1 表示 10%。
- `Priority: 10`：如果有多个随机生成规则，其中 2 个选中了同一位置，优先级较高的生物会生成。
- `Worlds: world,world_nether`：生物只会在这些世界中生成。在基本服务器设置中，它们分别是主世界和下界。

### 生物群系 {#biomes}

还可以进一步指定生物生成的生物群系！使用 Biomes 选项即可，可以添加 1 个生物群系，也可以列出多个。

Biomes 使用 [Spigot 生物群系名称](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
```

在这个示例中，生物可以在 `world` 和 `nether` 世界中生成，且仅限 `JUNGLE`、`FOREST` 和 `SOUL_SAND_VALLEY` 生物群系。

### 位置类型 {#position-type}

使用 ADD 操作时，可以设置位置类型，告诉 Mythic 生物应在陆地还是水中生成。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
  PositionType: LAND
```

现在，SkeletonKing 只会在陆地上生成，不会在海洋和河流中生成。

### Level {#level}

如果你使用[等级](../mobs/levels.md)系统，并希望生物以特定等级生成，也可以进行设置。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Level: 4
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
```

这会生成一个等级为 4 的生物。

# 添加条件 {#adding-conditions}

可以为随机生成添加几乎所有[条件](../skills/conditions.md)，进一步决定生物的生成方式。通常只能使用实体和位置类型的条件，Replace 操作会检查实体条件。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
  Conditions:
  - night true
  - raining true
```

在这个示例中，我们添加了条件，让生物只在夜间且下雨时生成。列表中的所有条件都必须满足，生物才会生成。

**进阶说明**

使用[复合条件](../skills/conditions.md#composite-conditions)，可以设置只满足两个条件之一、但不同时满足两者的条件组合。

# 限制 {#limiting}

可以通过条件限制生物生成，让生物数量保持在一定范围内。最常用的 2 种方法是使用 [MobsInRadius](../skills/conditions/mobsinradius.md) 和 [MobsInChunk](../skills/conditions/mobsinchunk.md) 条件。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  Biomes: JUNGLE,FOREST,SOUL_SAND_VALLEY
  Conditions:
  - night true
  - raining true
  - mobsinchunk{a=<10} true
  - mobsinradius{t=SkeletonKing;a=<3;r=64} true
```

在这个示例中，只有当前区块内的*所有*生物少于 10 个，且半径 64 格内的 SkeletonKing 少于 3 个，才允许生成 SkeletonKing。

# 属性成长（Scaling） {#scaling}

本节仅适用于已设置[等级修正](../mobs/levels.md)的生物。

可以使用 [WorldScaling](../mobs/levels.md#world-scaling)，决定是否根据距离提高生物等级。此选项默认启用，因此如果生物设置了等级修正，但你*不希望*它们根据世界缩放规则提高等级，请将此项设为 false。

```yaml
SkeletonKingSpawn:
  Action: ADD
  Type: SkeletonKing
  Chance: 0.1
  Priority: 10
  Worlds: world,world_nether
  UseWorldScaling: false
```
