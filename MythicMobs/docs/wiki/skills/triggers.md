---
title: 触发器
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 触发器

触发器用于确定如何从生物技能配置部分触发技能。

**触发器不得用于元技能内部，也不应写在元技能中。**

触发器只能用于*激活*元技能本身（在生物的配置文件中）。

> 每个触发器都以 `on` 字符串开头。该字符串**区分大小写**，因此请确保正确写入，否则触发器将无法工作

## 使用触发器 {#using-triggers}

触发器在生物配置的技能部分定义，前面必须加波浪号 (~)。使用 Timer 触发器时，还需指定以游戏刻为单位的时间。

```yml
SkeletalWizard_Fire:
  Type: WITHER_SKELETON
  Display: '&Skeletal Fire Wizard'
  Health: 50
  Damage: 0.5
  Skills:
  - ignite{ticks=100} @target ~onAttack
  - skill{s=FireShield} @trigger ~onDamaged 0.1
  - skill{s=AOEFire} ~onTimer:300
```

在此示例中，生物近战攻击时会点燃目标，受到伤害时会使用 "FireShield" 技能，并每隔 300 个游戏刻（即 15 秒）使用一次 "AOEFire" 技能。

## 不使用触发器…… {#not-using-triggers}

技能触发器在确定技能何时应该触发方面提供了更大的灵活性。 **强烈**建议你使用高级触发器来触发所有技能，而不是使用旧的遗留方法。

如果技能没有触发器，它将默认为`~onCombat`触发器，该触发器将在这些事件发生时执行：

- 当生物造成或受到伤害时
- 当生物出现时
- 当生物死亡时

```yml
SkeletalWarrior:
  Mobtype: skeleton
  Display: '<blue>A Skeletal Warrior</blue>'
  Skills:
  - skill{s=Bash} =10%-90%
```

在此示例中，生物生命值介于 10% 和 90% 之间时，造成或受到伤害都会触发 Bash 技能。

# @trigger 目标选择器 {#the-at-trigger-targeter}

你可能已经注意到，上面的示例中使用了 [`@trigger`](targeters/trigger.md) 目标选择器，[目标选择器](targeters.md)章节中也列出了它。`@trigger` 会选中“引发”技能的实体。例如，玩家攻击了带有 ~onDamaged 技能的生物时，就会选中该玩家；生物收到信号时，就会选中发送信号的生物，依此类推。

# 额外触发器 {#additional-triggers}

以下链接列出了扩展插件提供的触发器。只有安装对应插件后，这些触发器才能使用。

- [MythicCrucible](https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers)
- [MythicEnchantments](https://git.mythiccraft.io/mythiccraft/mythicenchants/-/wikis/Triggers/Triggers)

# 触发器 {#triggers}

**所有可用触发器表：**

| 触发器 | 触发时机 |
| --- | --- |
| [onCombat](triggers/oncombat.md) | Default |
| [onAttack](triggers/onattack.md) | 生物命中其他对象时。 |
| [onDamaged](triggers/ondamaged.md) | 生物受伤时。 |
| [onSpawn](triggers/onspawn.md) | 生物生成时。 |
| [onDespawn](triggers/ondespawn.md) | 生物消失时。 |
| [onReady](triggers/onready.md) | 生物首次从刷怪器生成时触发。 |
| [onLoad](triggers/onload.md) | 服务器重启后，生物被加载时。 |
| [onSpawnOrLoad](triggers/onspawnorload.md) | 生物[生成](triggers/onspawn.md)或[加载](triggers/onload.md)时。 |
| [onDeath](triggers/ondeath.md) | 生物死亡时。 |
| [onTimer](triggers/ontimer.md) | 每隔 # 刻，其中 # 为以刻为单位的间隔。 |
| [onInteract](triggers/oninteract.md) | 生物被右键点击时。 |
| [onPlayerKill](triggers/onplayerkill.md) | 生物击杀玩家时。 |
| [onEnterCombat](triggers/onentercombat.md) | 生物进入战斗时，需要启用仇恨表。 |
| [onDropCombat](triggers/ondropcombat.md) | 生物离开战斗时，需要启用仇恨表。 |
| [onChangeTarget](triggers/onchangetarget.md) | 生物切换目标时，需要启用仇恨表。 |
| [onExplode](triggers/onexplode.md) | 生物爆炸时，通常仅用于苦力怕。 |
| [onPrime](triggers/onprime.md) | 苦力怕开始为爆炸蓄力时。 |
| [onCreeperCharge](triggers/oncreepercharge.md) | 苦力怕被闪电击中，变为闪电苦力怕时。 |
| [onTeleport](triggers/onteleport.md) | 生物传送时，通常仅用于末影人。 |
| [onSignal](triggers/onsignal.md) | 生物收到信号时。 |
| [onShoot](triggers/onshoot.md) | 生物发射弹射物时。 |
| [onBowHit](triggers/onbowhit.md) | 生物发射的弹射物命中实体时。 |
| [onTame](triggers/ontame.md) | 生物被驯服时。 |
| [onBreed](triggers/onbreed.md) | 生物与另一个生物繁殖时。 |
| [onTrade](triggers/ontrade.md) | 村民完成交易时，需要 Paper。 |
| [onChangeWorld](triggers/onchangeworld.md) | 生物切换世界时。 |
| [onBucket](triggers/onbucket.md) | 牛被挤奶，或实体被装入桶中时，例如美西螈。 |
| [onSkillDamage](triggers/onskilldamage.md) | 生物通过机制对其他实体造成伤害时。 |
| [onHear](triggers/onhear.md) | 生物听到声音时，需[启用此功能](../mobs/mobs.md#hearing)。 |
| [onProjectileHit](triggers/onprojectilehit.md) | 生物的特殊弹射物命中实体时。 |
| [onProjectileLand](triggers/onprojectileland.md) | 生物的特殊弹射物命中方块时。 |
| [onDismounted](triggers/ondismounted.md) | 有乘客从生物身上下坐骑时。 |
| [onCinematicStart](triggers/oncinematicstart.md) | 开始为玩家播放过场动画镜头路径时。 |
| [onCinematicEnd](triggers/oncinematicend.md) | 玩家的过场动画镜头路径结束时，包括播放完成、取消、退出或死亡。 |
| [onEnterBounds](triggers/onenterbounds.md) | 生物进入定义的区域时。 |
| [onExitBounds](triggers/onexitbounds.md) | 生物离开定义的区域时。 |
| [onPlayerEnter](triggers/onplayerenter.md) | 玩家进入定义的区域时。 |
| [onPlayerExit](triggers/onplayerexit.md) | 玩家离开定义的区域时。 |
