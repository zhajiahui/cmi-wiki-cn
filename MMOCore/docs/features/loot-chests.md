---
title: 战利品箱
source: https://docs.phoenixdevt.fr/mmocore/features/loot-chests
source_snapshot: '2026-10-19'
---

# 战利品箱 {#🎁-loot-chests}

可掠夺的箱子是奖励RPG玩家探索世界的好方法。它们在特定区域的玩家周围生成，并随机生成战利品。战利品箱可以有等级；等级越高，战利品就越好。

以下代码片段可以在`/loot-chests`文件夹下找到。

## 一般选项 {#general-options}

这些选项可以在MMOCore`config.yml`内找到。

```yml
loot-chests:

    # Time in seconds it takes for a loot chest to
    # expire after it was spawned. 600 is 10 minutes.
    chest-expire-time: 600
    
    # Interval in seconds before the same player
    # spawns two loot chests in ANY region.
    player-cooldown: 600
```

## 战利品箱区域 {#loot-chest-regions}

MMOCore允许你设置宝箱可以生成的区域。你需要定义的第一件事是区域边界，就像WorldGuard区域一样：

```yml
loot-chest-region-id:
    
    # Region boundaries
    bounds:
        world: world_name_here
        x1: 32
        x2: -15
        z1: -419
        z2: -375
```

`loot-chest-region-id`仅用作内部标识符。它可以是任何东西，只需确保编辑配置时两个区域不共享相同的ID即可。

然后，你需要定义该区域中宝箱生成的频率（周期以秒为单位，默认设置为120，对应于2分钟）。

```yml
loot-chest-region-id:
    spawn-period: 120
```

每隔 X 分钟，该区域就会在该区域中随机寻找一个玩家并在附近生成一个箱子。请记住，MMOCore将首先过滤仍在冷却时间上的玩家：这意味着当且仅当该区域中没有玩家/所有玩家都在冷却时间上时，特定区域中不会生成任何箱子。

## 战利品宝箱等级 {#loot-chest-tiers}

宝箱等级直接决定战利品宝箱的掉落量。当某个地区产生战利品箱时，每个等级都有一定的选择机会。

```yml
loot-chest-region-id:
    tiers:
    
        # Some tier
        normal:
        
            # Particle effect played around a spawned loot chest
            effect:
                type: OFFSET # Type of particle effect used
                particle: FLAME # Particle used to play the effect
                period: 60 # Plays the effect every 60 ticks
            
            chance: 0.9
            drops:
                items:
                - 'vanilla{type=DIAMOND} 1 1-10 8'
                - 'vanilla{type=GOLD_INGOT} 0.5 1-10 4'
                - 'vanilla{type=EMERALD} 0.5 1-10 4'

        # Some other tier
        rare:
            effect:
                type: HELIX
                particle: FIREWORKS_SPARK
                period: 80
            chance: 0.1
            capacity: 10
            drops: drop-table-id
```

每个层都有自己的粒子效果，每 X 个刻就会显示在战利品箱周围（它对应于`period`选项），直到它被打开/过期。粒子效果由其类型（粒子将绘制的形状或图形）和使用的粒子（火焰、烟花、水等粒子）定义。可用的粒子类型有 HELIX、OFFSET 和 GALAXY。可用的粒子名称可以在 [SpigotJavadocs](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)] 中找到。

`chance`是生成战利品箱时选择等级的概率。所有等级机会加起来应为1（10%机会为0.1）。

`drops`是用于填充战利品箱物品栏的掉落表，以及`capacity`是箱子容量。有关战利品表 *容量* 工作原理的更多信息，请参阅此 [wiki 部分](drop-tables.md#table-capacity-items-weights)。你可以使用`capacity: 10`直接指定数字，也可以使用缩放公式，如下所示：

```yml
capacity:
    base: 10 # Base value of 10 capacity
    scale: 3 # 3 extra capacity for every player level
    spread: 0.1 # +/-10% spread in average
    max-spread: 0.3 # Relative offset due to the 'spread' option cannot be greater than 30%
```

如果你使用战利品容量缩放公式，则`spread`和`max-spread`选项是可选的。

对于`drops`选项，请注意，如果你的掉落表已在掉落表配置文件夹中设置，则可以指定掉落表ID；如果你想专门为宝箱层定义新的掉落表，则可以指定整个配置部分。

## 默认配置 {#default-config}

`chests.yml`处理你所有的RPG随机战利品箱！这个维基页面尚未完成，因为有更多的战利品选项和插件兼容性被添加到可能的掉落表中。

```yml
'world 59 71 131':

    # Create directly your drop table here.
    drop-table:
        items:
        - 'vanilla{type=DIAMOND} 1 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'gold{} .9 1-3'
        - 'note{min=1;max=10} .9 1-3'
    
    # Ticks the chest takes to appear again.
    regen-time: 40
    
    # The particle played every 4sec around the chest.
    # Types available: helix|offset|galaxy
    # Particle names here: https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html
    effect:
        type: helix
        particle: FLAME
```

宝箱的名称决定它放置的位置，例如“world 59 71 131”。格式为 WORLD,X,Y,Z。这里并不是给箱子起显示名称，而是填写希望放置箱子的世界和坐标。

- drop-table

此选项定义了你的胸部可能有什么。目前支持MMOItems、原版、物品、MMOCore货币（黄金和纸币）。格式显示在默认箱子中。

输入后的2组数字分别是掉落几率和掉落数量。在这个例子中。9(90%) 是宝箱包含它的机会，而1-3是随机数量。

- regen-time

这是箱子以随机战利品重生所需的时间（以刻为单位）。当宝箱被打开并清除时，它将被删除。或者，可以敲击箱子，将所有战利品掉落在地上。

- 效果

为了使战利品箱脱颖而出，你可以在它们上添加粒子效果，以便玩家知道它们是特殊的箱子。你还可以使用这些粒子效果来确定宝箱等级。只要给予不同的宝箱和掉落台，就有不同的效果！

---

原文：[🎁 Loot Chests](https://docs.phoenixdevt.fr/mmocore/features/loot-chests) · 原文归档：2026-10-19
