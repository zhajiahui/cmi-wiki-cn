---
title: （步骤 3）创建第一个生物
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/%28Step-3%29-Creating-Your-First-Mob
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# （步骤 3）创建第一个生物

现在你已经了解基础概念、使用方法以及它们应放的位置，接下来创建第一个生物！

我们将创建一个简单的生物：骷髅王，为它配上几个基本技能和物品。

# 生物文件 {#mob-file}

`/plugins/MythicMobs/Mobs/SkeletonKing.yml`

先创建基本生物配置，为它设置内部 ID、Type、Display、Health 和 Damage。

这个生物的内部 ID 为 `SkeletonKing`。每个生物的内部 ID 都必须唯一，不能与其他生物重复。我们将用它生成生物：`/mm m spawn SkeletonKing`。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
```

接下来，为生物添加一些选项。

- `AlwaysShowName: true` 会让生物的显示名称出现在头顶。
- `MovementSpeed: 0.2` 用于修改生物的行走速度。
- `MaxCombatDistance: 25` 用于修改玩家可与生物战斗的距离，单位为格。
- `PreventOtherDrops: true` 会阻止该生物类型掉落原版掉落物。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
```

现在添加一些装备，自定义生物的外观和所用武器。这里使用的物品包括一双原版靴子，以及 2 件 Mythic 物品；我们稍后会在物品文件中创建这两件物品。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
  Equipment:
  - KingsCrown HEAD
  - IRON_BOOTS FEET
  - SkeletonKingSword HAND
```

既然移除了生物的原版掉落物，就添加我们自己的掉落物。我们会通过下文创建的掉落表来处理这些掉落。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
  Equipment:
  - KingsCrown HEAD
  - IRON_BOOTS FEET
  - SkeletonKingSword HAND
  Drops:
  - SkeletonKingDrops
```

最后，给生物添加一些技能，让它拥有有趣的能力！

我们为生物添加了 2 个机制和 2 个元技能。稍后会在技能文件中创建这些元技能。前往[机制](../skills/mechanics.md)、[目标选择器](../skills/targeters.md)和[触发器](../skills/triggers.md)页面，了解这些机制的作用！

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Options:
    AlwaysShowName: true
    MovementSpeed: 0.2
    MaxCombatDistance: 25
    PreventOtherDrops: true
  Equipment:
  - KingsCrown HEAD
  - IRON_BOOTS FEET
  - SkeletonKingSword HAND
  Drops:
  - SkeletonKingDrops
  Skills:
  - speak{m="None may challenge the Skeleton King!";cooldown=20} @PlayersInRadius{r=40} ~onCombat 0.2
  - speak{m="Ahahahahah! Die, <trigger.name>!"} @PlayersInRadius{r=40} ~onPlayerKill
  - skill{s=SummonSkeletons} @self 0.1
  - skill{s=SmashAttack} @target 0.2
```

在部分机制后面添加 0.2 和 0.1，就能设置它们的执行概率，使其不再有 100% 的概率触发。概率以 1 为基准，因此 0.2 表示 20% 的概率。

# 技能文件 {#skills-file}

`/plugins/MythicMobs/Skills/SkeletonKing.yml`

技能文件将包含我们在生物文件中使用的 `SummonSkeletons` 和 `SmashAttack` 元技能。

### SummonSkeletons {#summonskeletons}

这个技能的内部 ID 为 `SummonSkeletons`，调用时会用到它。我们为技能设置了 15 秒的冷却时间，因此技能执行后，这段时间内无法再次执行。

Mechanics:

- [message](../skills/mechanics/message.md)：向生物周围半径 40 格内的所有玩家发送消息，告知即将生成骷髅。这里使用 caster.name 占位符获取生物的 Display 设置，并使用 &co 占位符插入 :，因为直接使用冒号可能影响语法。
- [delay 20](../skills/mechanics/delay.md)：在消息与下一个机制之间添加 20 刻（1 秒）的延迟。
- [summon](../skills/mechanics/summon.md)：召唤 2 个普通骷髅，随机出现在骷髅王周围 5 格内。summon 机制支持原版生物（如此处所用），也支持通过内部 ID 指定其他 MythicMobs 生物。我们重复了延迟和召唤机制，因此会在 3 秒内总共生成 6 个骷髅。

```yaml
SummonSkeletons:
  Cooldown: 15
  Skills:
  - message{m="<caster.name><&co> Arise, my minions!"} @PlayersInRadius{r=40}
  - delay 20
  - summon{mob=SKELETON;amount=2;radius=5} @Self
  - delay 20
  - summon{mob=SKELETON;amount=2;radius=5} @Self
  - delay 20
  - summon{mob=SKELETON;amount=2;radius=5} @Self
```

> 请注意，要多次重复一个机制，也可以使用 `repeat` 和 `repeatInterval` 通用属性。
> 因此，上面的元技能可以改写为：
>

> ```yaml
> SummonSkeletons:
>   Cooldown: 15
>   Skills:
>   - message{m="<caster.name><&co> Arise, my minions!"} @PlayersInRadius{r=40}
>   - delay 20
>   - summon{mob=SKELETON;amount=2;radius=5;repeat=2;repeatInterval=20} @Self
> ```

### SmashAttack {#smashattack}

这个技能会让生物传送到目标处，对目标造成伤害并将其击飞。

我们使用了条件来确保目标处于指定距离内；目标太远时，技能就不会执行。

- [TargetWithin{d=25}](-step-3--creating-your-first-mob.md)：确保目标位于生物周围 25 格内。

Mechanics:

- [message](../skills/mechanics/message.md)：向半径 40 格内的所有玩家发送消息，警告即将发动的攻击。
- [teleport](../skills/mechanics/teleport.md)：将生物直接传送到目标玩家处。
- [sound](../skills/mechanics/sound.md)：在生物所在位置播放末影人传送的声音。
- [delay](../skills/mechanics/delay.md)：让技能延迟 10 刻。
- [damage](../skills/mechanics/damage.md)：无视护甲，直接对生物周围 5 格内的所有玩家造成 5 点伤害。
- [throw](../skills/mechanics/throw.md)：按指定的速度和 Y 轴速度将玩家抛出。
- [fakeexplosion](../skills/mechanics/fakeexplosion.md)：产生爆炸效果，但不会造成伤害或破坏方块。

```yaml
SmashAttack:
  Cooldown: 8
  Conditions:
  - targetwithin{d=25}
  Skills:
  - message{cooldown=30;m="<mob.name><&co> Hahahah! I will crush you, fool!"} @PlayersInRadius{r=40}
  - teleport @target
  - sound{s=mob.endermen.portal;volume=1.0;pitch=0.5}
  - delay 10
  - damage{amount=5;ignorearmor=true} @PlayersInRadius{r=5}
  - throw{velocity=10;velocityY=5} @PlayersInRadius{r=5}
  - fakeexplosion @Self
```

# 物品文件 {#items-file}

`/plugins/MythicMobs/Items/SkeletonKing.yml`

现在创建生物所需的盔甲和武器物品。

先创建剑。我们为它设置 Display 和 Lore，玩家在物品栏中将鼠标悬停在物品上时就会显示这些内容，并为它添加附魔。DAMAGE_ALL 是锋利附魔的名称。我们还为剑添加属性，让持有者获得 +10 生命值和 10% 的额外移动速度。

```yaml
SkeletonKingSword:
  Id: DIAMOND_SWORD
  Display: '&3Greatsword of the Skeleton King'
  Lore:
  - '&6A powerful sword used by'
  - '&6the King of Skeletons.'
  Enchantments:
  - DAMAGE_ALL:5
  - KNOCKBACK:2
  - FIRE_ASPECT:2
  Attributes:
    MainHand:
      Health: 10
      MovementSpeed: 0.1
```

现在创建王冠。与上面的剑类似，我们为它设置 Display、Lore、Enchantments 和 Attributes。同时添加 2 个 Hide 标志，防止属性和附魔显示在物品描述中。

```yaml
KingsCrown:
  Id: GOLDEN_HELMET
  Display: '&dCrown of the King'
  Lore:
  - '&6A kingly crowl that grants'
  - '&6the wearer unwavering power!'
  Enchantments:
  - PROTECTION_ENVIRONMENTAL:2
  - PROTECTION_PROJECTILE:2
  - PROTECTION_FIRE:2
  - PROTECTION_EXPLOSIONS:2
  Hide:
  - ATTRIBUTES
  - ENCHANTS
  Attributes:
    Head:
      Health: 10
      KnockbackResistance: 10
```

# 掉落物文件 {#drops-file}

`/plugins/MythicMobs/DropTables/SkeletonKing.yml`

对于掉落，我们创建 2 个掉落表，并让第一个掉落第二个。我们使用条件，确保生物只有在夜间死亡时，才会掉落第 2 个掉落表中的物品。

掉落格式为 `<Drop Type> <Amount> <Chance>`。因此，第一个掉落表会以 100% 的概率掉落 1 次 SkeletonKingItemDrops 掉落表，并随机掉落 100 到 150 点经验。在 SkeletonKingItemDrops 中，王冠的掉落概率为 1%，剑的掉落概率为 10%。

我们使用 MinItems 和 MaxItems 指定掉落表总共选取多少项掉落，这里会从列表中选出 1 或 2 项。这不是单个物品的总数量：金粒和钻石都设置了数量范围，因此可能掉落 64 个金粒和 12 个钻石，而这仍符合 MaxItems 为 2 的限制。

```yaml
SkeletonKingDrops:
  Drops:
  - SkeletonKingItemDrops 1 1
  - experience 100-150 1
  
SkeletonKingItemDrops:
  Conditions:
  - night
  MinItems: 1
  MaxItems: 2
  Drops:
  - KingsCrown 1 0.01
  - SkeletonKingSword 0.1
  - GOLD_NUGGET 32-64 1
  - DIAMOND 1-12 0.8
```

# 测试 {#testing}

现在，自定义生物所需的全部文件都已创建完毕！接下来进入游戏，使用 `/mm reload` 将生物及其物品加载到服务器，再通过 `/mm m spawn SkeletonKing` 生成生物，检查是否正常！

# 随机生成文件 {#random-spawn-file}

`/plugins/MythicMobs/RandomSpawns/SkeletonKing.yml`

创建生物后，你可能想让它在世界中随机生成。我们可以配置一个简单的 RandomSpawns 文件来实现！

RandomSpawns 的用法相当简单，相关 Wiki 页面介绍了如何创建。

本指南将创建一个基本配置，让骷髅王在夜间的室外生成。我们使用 REPLACE 操作，将原版生物的生成替换为自定义生物，并添加条件，使其只替换骷髅。

我们使用 `0.005` 的概率，因此每次骷髅生成时，都有 0.5% 的概率被替换。

请将 `world` 替换为你希望生物生成的世界名称（也可以填写多个世界，用 , 分隔）。

```yaml
RandomSkeletonKing:
  Type: SkeletonKing
  Worlds: world
  Chance: 0.005
  Priority: 1
  Action: REPLACE
  Conditions:
  - outside true
  - night true
  - entitytype{t=SKELETON}
```

**[>> 第 4 步](-step-4--essential-commands.md)**
