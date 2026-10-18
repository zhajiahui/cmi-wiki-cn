---
title: MythicMobs
source: https://docs.phoenixdevt.fr/mmoitems/compatibility/mythic
source_snapshot: '2026-10-19'
---

# MythicMobs {#🧟-mythicmobs}

## 定制能力 {#custom-abilities}

你可以创建自定义技能/能力并将其添加到你的物品中。有关 [MythicLib维基](../../mythiclib/skills/custom/mythic.md)] 的更多信息。

## 箭齐射机械师 {#arrow-volley-mechanic}

与神话怪物的箭齐射机制类似，该机制以所需的散布和所需的偏移量发射一束箭。然而，**这会使用玩家的属性来缩放箭头**，这样发射的箭具有与用弓手动发射相同的效果。

请注意，箭头将从所有玩家装备中获得属性奖励，包括玩家当前使用的任何武器，即使它不是弓。

|基础属性|别名 |描述 |默认值 |
| --- | --- | --- | --- |
| amount | arrows, a | 将发射的箭的数量。 | 20 |
| spread | s | 箭头的分布，使用较大的值来注意。 | 45 |
| fireticks | ft, f | 勾选箭头将继续着火。 | 0 |
| 删除延迟 | rd, r | 经过这么多次刻后，箭头将被删除。 | 200 |
| velocity | v | 箭头的速度。 | 20 |
| 统计规模 | ss | 将每支箭造成的伤害乘以该系数。 | 1 |
| 按箭头缩放 | spa | 属性比例基础属性支持占位符，将其设置为true将为每个箭头再次解析这些占位符。 | false |
| 箭头项目 | item. ai | 物品的过滤器要发射，最好是箭头。对于某些插件很重要。 | v ARROW ~ |
| 完整活动 | fe | 将其设置为true将导致箭头为每个箭头调用 EntityShootBowEvent 事件，这使得所有插件都检测到它并执行操作，就像玩家实际上发射了这样的弓一样。使用默认值“false”，只有MMOItems运行这些计算，这意味着如果你有其他插件（例如 mcMMO），它们不会将其效果应用于箭头，这可能是你需要的，也可能不是你的情况。 | false |

这些选项会影响箭的发射位置，但它们始终会指向技能的目标。

| 基础属性 | Aliases | 描述 | Default Value |
| --- | --- | --- | --- |
| 来源 | fo | 箭从技能的原点发射。 | false |
| 开始X偏移 | sxo | 在 X 坐标中移动箭头生成。 | 0 |
| 起始Y偏移 | syo | 在 Y 坐标中移动箭头生成。 | 3 |
| 开始Z偏移 | szo | 在 Z 坐标中移动箭头生成。 | 0 |
| 起始偏移量 | sfo | 相对于施法者向前移动箭头的生成位置。 | 0 |
| 开始偏移 | sso | 相对于施法者向右移动箭头生成点。 | 0 |

*请注意，此机制仅适用于玩家，如果由 NPC 或怪物发射，则会减少到MythicMobs的通常 ArrowVolley，并且仅支持该机制的参数（最值得注意的是，箭头的生成位置的偏移将不起作用）。*

<details markdown="1">

<summary>用法示例</summary>

黑箭MMOItems的可怕箭雨按比例调整后只能造成20%正常伤害。 *需要 XBow2RL 等其他插件才能使箭头物品发挥作用。*

```yml
ExampleSkill:
  Skills:
  - MMOItemsVolley{amount=10;spread=30;fireTicks=20;removeDelay=100;velocity=20;syo=1.2;sso=2} @Forward{f=15.0;y=0.0}
```

使玩家从右侧发射一堆箭。每支箭造成的伤害与玩家从弓箭射出的伤害相同。

```yml
ExampleSkill2:
  Skills:
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
  - delay 2
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
  - delay 2
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
  - delay 2
  - MMOItemsVolley{a=4;s=30;rD=100;v=20;syo=5.2;sfo=5;statsScale=0.2;ai="m AMMO BLACK_ARROW";fe=true} @TargetLocation
```

</details>

## 在MMO项目上使用光环 {#onmmoitemuse-aura}

与当你发射弓箭时会激发的神话生物的射击光环类似，当玩家使用MMOItems武器的任何特殊攻击时（不是当它们击中怪物时，而是当它们射击时），该光环将会触发

请注意，这永远不会对怪物触发，因为怪物无法使用特殊攻击。

| 基础属性 | Aliases | 描述 | Default Value |
| --- | --- | --- | --- |
| skill | s | 光环触发时运行的技能的名称，**名为技能**。 | (none) |
| weapons | w | 你正在收听哪种类型的武器（逗号分隔列表，无空格）？十字弓、手套、鲁特琴、步枪、法杖或鞭子 | MUSKET |
| 取消事件 | ce | 取消事件，防止武器实际触发。 | false |

#### 称为技能元数据 {#called-skill-metadata}

|元 |描述 |
| --- | --- |
| 脚轮 | 没有变化，onMMOItemUse 机制的施法者 |
| 目标 | 没有变化，目标接收 onMMOItemUse 光环。 |
| 触发 | 受到此武器攻击的敌人，仅支持 GAUNTLET、MUSKET、STAFF 和 WHIP。 |
| 产地 | 没有变化，无论起源在哪里。 |

（用法请参见下面的示例）

<details markdown="1">

<summary>用法示例</summary>

下次玩家right-clicks带着手套时，他们将执行组合拳。

```yml
ExampleSkill:
  Skills:
  - onMMOItemUse{auraName=Flash;d=600;c=1;s=ComboPunch;w=GAUNTLET;;cE=true} @Self
      
ComboPunch: 
  Skills:

  # Punch
  - velocity{m=set;x=0.15;y=0.02;z=0} @Trigger
  - mmodamage{a=7;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
  - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1.25}
  - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
  - delay 5

  # Punch
  - velocity{m=set;x=-0.15;y=0.02;z=0} @Trigger
  - mmodamage{a=7;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
  - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1.25}
  - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
  - delay 5

  # Punch
  - velocity{m=set;x=0.15;y=0.02;z=0} @Trigger
  - mmodamage{a=7;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
  - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1.25}
  - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
  - delay 10

  # Throw
  - throw{velocity=20;velocityY=7} @Trigger
  - mmodamage{a=13;preventImmunity=true;t=PHYSICAL,SKILL} @Trigger
  - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=1}
  - effect:sound{s=entity.player.attack.knockback;volume=1.2;pitch=0.5}
  - effect:particles{particle=largeexplode;amount=1;hS=0.4;vS=0.2;speed=0.01;y=1.3} @Trigger
```

使员工攻击在接下来的15秒内引起绿色爆炸

```yml
ExampleSkill2:
  Skills:
  - onMMOItemUse{d=300;s=GreenExplosion;w=STAFF,WHIP} @Self
```

</details>

## 掉落表 {#drop-tables}

你可以将物品从 MI 添加到MythicMobs删除表：有关 [此页面](../items/drop-tables.md#adding-mmoitems-to-mythicmobs-drop-tables)的更多信息]。

---

原文：[🧟 MythicMobs](https://docs.phoenixdevt.fr/mmoitems/compatibility/mythic) · 原文归档：2026-10-19
