---
title: 技能机制标签
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Tags/Mechanic-Tags
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 技能机制标签 {#mechanic-tags}

***自动生成的***文档，列出了所有机制，按标签/功能分组。

标签由 Wiki 编辑团队添加，并不对应插件代码中的功能，只是用于辅助查找。

每个技能机制可以拥有多个标签，并会列在其每个标签对应的分类下。

1. [AI](mechanic-tags.md#ai)
2. [属性](mechanic-tags.md#attribute)
3. [Boss 血条](mechanic-tags.md#bossbar)
4. [伤害](mechanic-tags.md#damage)
5. [伪装](mechanic-tags.md#disguise)
6. [效果](mechanic-tags.md#effect)
   1. [粒子](mechanic-tags.md#particle)
   2. [Sound](mechanic-tags.md#sound)
7. [经验](mechanic-tags.md#experience)
8. [生命值](mechanic-tags.md#health)
9. [物品栏](mechanic-tags.md#inventory)
10. [物品](mechanic-tags.md#item)
11. [物品匹配器](mechanic-tags.md#itemmatcher)
12. [消息](mechanic-tags.md#message)
13. [元](mechanic-tags.md#meta)
    1. [流程控制](mechanic-tags.md#flow)
14. [元机制](mechanic-tags.md#meta-mechanic)
    1. [光环](mechanic-tags.md#aura)
    2. [Thenable](mechanic-tags.md#thenable)
15. [坐骑](mechanic-tags.md#mount)
16. [移动](mechanic-tags.md#movement)
    1. [旋转](mechanic-tags.md#rotation)
    2. [传送](mechanic-tags.md#teleport)
17. [仅支持 Paper](mechanic-tags.md#paper-only)
18. [Pin](mechanic-tags.md#pin)
19. [仅限 Premium](mechanic-tags.md#premium-only)
20. [Projectile](mechanic-tags.md#projectile)
21. [随机](mechanic-tags.md#random)
22. [记分板](mechanic-tags.md#scoreboard)
23. [召唤](mechanic-tags.md#summon)
24. [仇恨](mechanic-tags.md#threat)
25. [变量](mechanic-tags.md#variable)
26. [世界](mechanic-tags.md#world)
27. [未标记](mechanic-tags.md#untagged)

[>> 到顶部](mechanic-tags.md)

## AI {#ai}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [ClearTarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ClearTarget) | MythicMobs | 强制此机制的目标重置其当前目标。 |
| [FollowPath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FollowPath) | MythicMobs | 创建一个使持有生物沿路径移动的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura) |
| [FollowPath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FollowPath) | MythicMobs | 创建一个使持有生物沿路径移动的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura) |
| [FormLine](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FormLine) | MythicMobs | 使施法生物沿直线路径移动到指定位置 |
| [Goto](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/goto) | MythicMobs | 使生物寻路到指定位置 |
| [ResetAI](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ResetAI) | MythicMobs | 尝试将施法生物的 AI 重置为其基础类型的默认 AI。 |
| [Runaigoalselector](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/runaigoalselector) | MythicMobs | 更改寻路目标 |
| [Runaitargetselector](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/runaitargetselector) | MythicMobs | 更改目标选择的寻路目标 |
| [Setai](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setai) | MythicMobs | 切换目标的 AI |
| [SetPathfindingMalus](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetPathfindingMalus) | MythicMobs | 设置生物的寻路代价，影响该实体在计算路径时如何评估不同类型的方块 |
| [Settonguetarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/settonguetarget) | MythicMobs | 将青蛙施法者的舌头目标设置为目标实体。 |
| [Togglesitting](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/togglesitting) | MythicMobs | 切换猫、狗、狐狸和鹦鹉的坐下状态 |
| [Wolfsit](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/wolfsit) | MythicMobs | 设置目标狼的坐下状态 |
| [GoatRam](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/GoatRam) | MythicMobs | 使施法的山羊生物冲撞目标实体。 |

[>> 到顶部](mechanic-tags.md)

## Attribute {#attribute}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Attribute](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Attribute) | MythicMobs | 设置目标实体[属性](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html)的基础值 |
| [AttributeModifier](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/AttributeModifier) | MythicMobs | 为支持属性的目标添加属性修饰符。 |

[>> 到顶部](mechanic-tags.md)

## BossBar {#bossbar}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Barcreate](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/barcreate) | MythicMobs | 在施法生物上创建自定义 Boss 血条（施法者须为非玩家实体） |
| [Barremove](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/barremove) | MythicMobs | 移除施法生物上的自定义 Boss 血条（施法者须为非玩家实体） |
| [Barset](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/barset) | MythicMobs | 修改施法生物上的自定义 Boss 血条（施法者须为非玩家实体） |

[>> 到顶部](mechanic-tags.md)

## Damage {#damage}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Consume](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/consume) | MythicMobs | 对每个目标实体造成指定伤害，并治疗施法方…… |
| [Basedamage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/basedamage) | MythicMobs | 按生物伤害值的一定百分比对目标实体造成伤害 |
| [Damage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/damage) | MythicMobs | 对目标实体造成伤害 |
| [ModifyDamage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ModifyDamage) | MythicMobs | 修改触发此技能的伤害事件。 |
| [Percentdamage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/percentdamage) | MythicMobs | 按玩家最大生命值的一定百分比造成伤害，其中 1 为…… |
| [Hit](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/hit) | MythicMobs | 模拟施法者的一次物理攻击 |
| [Explosion](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/explosion) | MythicMobs | 在目标实体或位置制造爆炸 |
| [Lightning](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/lightning) | MythicMobs | 在目标实体或位置引发雷击，造成…… |
| [Suicide](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/suicide) | MythicMobs | 立即杀死生物 |

[>> 到顶部](mechanic-tags.md)

## Disguise {#disguise}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Disguise](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/disguise) | MythicMobs | 对施法生物执行伪装字符串 |
| [DisguiseModify](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/DisguiseModify) | MythicMobs | 修改目标实体*已经*应用的伪装 |
| [Undisguise](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/undisguise) | MythicMobs | 若生物当前有伪装，则移除该伪装 |
| [Disguisetarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/disguisetarget) | MythicMobs | 对目标生物执行伪装字符串 |
| [Doppleganger](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/doppleganger) | MythicMobs | 复制目标玩家的外观。 |

[>> 到顶部](mechanic-tags.md)

## Effect {#effect}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [BlockMask](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/BlockMask) | MythicMobs | 在指定目标周围创建方块遮罩 |
| [BlockUnmask](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/BlockUnmask) | MythicMobs | blockunmask 效果用于还原 blockmask 效果所做的方块更改 |
| [BlockWave](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/BlockWave) | MythicMobs | 创建由指定方块组成的波浪，可使用不同形状、速度和方块 |
| [BloodyScreen](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/BloodyScreen) | MythicMobs | 显示接近世界边界时的效果 |
| [Bossborder](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/bossborder) | MythicMobs | 使用以施法者为中心的原版世界边界将目标玩家限制在其中 |
| [EnderBeam](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EnderBeam) | MythicMobs | 召唤一个向目标发射光束的末地水晶 |
| [Ender](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Ender) | MythicMobs | 在目标选择器的位置播放末影之眼破碎效果 |
| [FakeExplosion](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FakeExplosion) | MythicMobs | 在指定目标处创建爆炸效果 |
| [Firework](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/firework) | MythicMobs | 在目标处创建烟花效果。 |
| [Flames](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/flames) | MythicMobs | 在目标选择器的位置创建火焰效果。 |
| [Geyser](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/geyser) | MythicMobs | 在目标实体或位置处，使液体从地面喷出，形成喷泉 |
| [GuardianBeam](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/GuardianBeam) | MythicMobs | 在原点与目标之间绘制守卫者光束。 |
| [Hide](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/hide) | MythicMobs | 在指定时间内向目标玩家隐藏施法者 |
| [Itemspray](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/itemspray) | MythicMobs | 在目标位置产生临时物品爆散效果。 |
| [FakeLightning](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FakeLightning) | MythicMobs | 在指定目标处生成一道“假”闪电 |
| [PlayAnimation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayAnimation) | MythicMobs | 强制实体播放动画。 |
| [Showentity](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/showentity) | MythicMobs | 若施法者通过 [hide](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/hide) 技能机制隐藏，则向目标玩家重新显示施法者 |
| [Skybox](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Skybox) | MythicMobs | 更改目标玩家的天空背景 |
| [Smoke](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Smoke) | MythicMobs | 在目标选择器的位置生成一团烟雾 |
| [SmokeSwirl](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SmokeSwirl) | MythicMobs | 在目标实体或位置创建旋转的烟雾漩涡 |
| [Time](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Time) | MythicMobs | 设置世界时间 |
| [TotemOfUndying](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/TotemOfUndying) | MythicMobs | 播放不死图腾复活玩家的效果，并可指定使用资源包中的 CustomModelData |
| [BlockCrack](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/BlockCrack) | MythicCrucible | 向指定接收对象显示目标方块的裂纹效果 |

### Particle {#particle}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Particle](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Particle) | MythicMobs | 在目标实体或位置创建粒子效果 |
| [Atom](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Atom) | MythicMobs | 在指定位置创建环绕的原子效果 |
| [ParticleBox](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleBox) | MythicMobs | 在目标实体或位置创建粒子方框 |
| [ParticleEquation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleEquation) | MythicMobs | 根据方程生成粒子效果 |
| [ParticleLine](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleLine) | MythicMobs | 在施法者与目标实体或位置之间创建粒子线 |
| [ParticleLineHelix](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleLineHelix) | MythicMobs | 在目标实体或位置创建粒子线螺旋效果 |
| [ParticleLineRing](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleLineRing) | MythicMobs | 创建粒子线圆环 |
| [ParticleOrbital](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleOrbital) | MythicMobs | 创建粒子轨道效果，使粒子围绕目标实体或位置运动 |
| [ParticleRing](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleRing) | MythicMobs | 在目标实体或位置周围创建粒子圆环 |
| [ParticleSphere](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleSphere) | MythicMobs | 在目标实体或位置创建粒子球体 |
| [ParticleTornado](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ParticleTornado) | MythicMobs | 创建龙卷风形状的粒子效果 |

### Sound {#sound}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Sound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Sound) | MythicMobs | 在目标实体或位置播放原版游戏或资源包中的声音 |
| [StopSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/StopSound) | MythicMobs | 停止为目标实体播放原版游戏或资源包中的声音 |
| [PlayBlockBreakSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockBreakSound) | MythicMobs | 播放目标方块的破坏声音 |
| [PlayBlockFallSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockFallSound) | MythicMobs | 播放目标方块的掉落声音 |
| [PlayBlockHitSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockHitSound) | MythicMobs | 播放目标方块被击打（受损）时的声音 |
| [PlayBlockPlaceSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockPlaceSound) | MythicMobs | 播放目标方块的放置声音 |
| [PlayBlockStepSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockStepSound) | MythicMobs | 播放目标方块的脚步声（实体在其上行走时播放的声音） |

[>> 到顶部](mechanic-tags.md)

## Experience {#experience}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [ClearExperienceLevels](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ClearExperienceLevels) | MythicMobs | 清空目标玩家的经验等级。 |
| [ClearExperience](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ClearExperience) | MythicMobs | 清除目标玩家的经验 |
| [GiveExperienceLevels](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/GiveExperienceLevels) | MythicMobs | 给予目标玩家经验等级。 |
| [TakeExperienceLevels](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/TakeExperienceLevels) | MythicMobs | 扣除目标玩家的经验等级 |

[>> 到顶部](mechanic-tags.md)

## Health {#health}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Consume](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/consume) | MythicMobs | 对每个目标实体造成指定伤害，并治疗施法方…… |
| [Heal](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/heal) | MythicMobs | 为目标实体恢复指定数值的生命值 |
| [Healpercent](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/healpercent) | MythicMobs | 按目标实体最大生命值的一定百分比恢复其生命值 |
| [Sethealth](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/sethealth) | MythicMobs | 设置目标实体的生命值。 |
| [Setmaxhealth](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setmaxhealth) | MythicMobs | 设置目标实体的最大生命值。 |

[>> 到顶部](mechanic-tags.md)

## 背包 {#inventory}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [BreakBlockAndGiveItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/breakBlockAndGiveItem) | MythicMobs | 破坏目标位置的方块并给予物品 |
| [Closeinventory](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/closeinventory) | MythicMobs | 关闭目标的背包界面（仅对玩家生效） |
| [Removehelditem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/removehelditem) | MythicMobs | 从施法玩家的手持物品中扣除指定数量 |
| [Consumeslot](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/consumeslot) | MythicMobs | 移除玩家背包指定槽位中的物品 |
| [EquipCopy](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EquipCopy) | MythicMobs | 使施法者装备目标装备的副本。 |
| [Equip](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/equip) | MythicMobs | 为生物装备物品 |
| [FillChest](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/fillChest) | MythicMobs | 使用物品列表或[掉落表](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/drops/DropTables)填充箱子 |
| [Giveitemfromslot](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/giveitemfromslot) | MythicMobs | 将施法者槽位中的物品复制一份给予目标 |
| [Giveitemfromtarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/giveitemfromtarget) | MythicMobs | 给予施法者物品；fakelooting 设为 true 时，播放从目标实体或位置拾取物品的动画 |
| [Giveitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/giveitem) | MythicMobs | 给予目标一件物品。 |
| [Saddle](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/saddle) | MythicMobs | 为目标实体装上或移除鞍 |
| [StealItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/StealItem) | MythicMobs | 从目标处偷取一件物品，并放到生物手中。 |
| [Takeitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/takeitem) | MythicMobs | 从目标玩家的背包中移除指定数量的物品 |

[>> 到顶部](mechanic-tags.md)

## Item {#item}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [BreakBlockAndGiveItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/breakBlockAndGiveItem) | MythicMobs | 破坏目标位置的方块并给予物品 |
| [Removehelditem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/removehelditem) | MythicMobs | 从施法玩家的手持物品中扣除指定数量 |
| [Consumeslot](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/consumeslot) | MythicMobs | 移除玩家背包指定槽位中的物品 |
| [Decapitate](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/decapitate) | MythicMobs | 掉落目标玩家头颅的副本 |
| [Dropitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/dropitem) | MythicMobs | 掉落一组物品，或选择…… |
| [EquipCopy](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EquipCopy) | MythicMobs | 使施法者装备目标装备的副本。 |
| [Equip](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/equip) | MythicMobs | 为生物装备物品 |
| [FillChest](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/fillChest) | MythicMobs | 使用物品列表或[掉落表](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/drops/DropTables)填充箱子 |
| [Giveitemfromslot](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/giveitemfromslot) | MythicMobs | 将施法者槽位中的物品复制一份给予目标 |
| [Giveitemfromtarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/giveitemfromtarget) | MythicMobs | 给予施法者物品；fakelooting 设为 true 时，播放从目标实体或位置拾取物品的动画 |
| [Giveitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/giveitem) | MythicMobs | 给予目标一件物品。 |
| [Itemspray](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/itemspray) | MythicMobs | 在目标位置产生临时物品爆散效果。 |
| [Pickupitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/pickupitem) | MythicMobs | 若施法者为玩家，拾取目标物品 |
| [SetDisplayEntityItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setDisplayEntityItem) | MythicMobs | 设置物品展示实体的物品组件 |
| [StealItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/StealItem) | MythicMobs | 从目标处偷取一件物品，并放到生物手中。 |
| [Stopusingitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/stopusingitem) | MythicMobs | 使目标活体实体停止使用物品，即…… |
| [Takeitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/takeitem) | MythicMobs | 从目标玩家的背包中移除指定数量的物品 |

[>> 到顶部](mechanic-tags.md)

## ItemMatcher {#itemmatcher}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [StealItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/StealItem) | MythicMobs | 从目标处偷取一件物品，并放到生物手中。 |
| [Takeitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/takeitem) | MythicMobs | 从目标玩家的背包中移除指定数量的物品 |

[>> 到顶部](mechanic-tags.md)

## Message {#message}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Log](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Log) | MythicMobs | 直接向控制台记录消息 |
| [Jsonmessage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/jsonmessage) | MythicMobs | 向目标玩家发送 JSON 格式的聊天消息 |
| [Message](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/message) | MythicMobs | 若目标为玩家，向其发送聊天消息 |
| [Randommessage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/randommessage) | MythicMobs | 向目标玩家发送随机消息。 |
| [Sendactionmessage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/sendactionmessage) | MythicMobs | 向目标玩家的动作栏发送消息 |
| [SendTitle](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SendTitle) | MythicMobs | 向所有目标玩家显示“标题”和/或“副标题”消息 |
| [Sendtoast](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/sendtoast) | MythicMobs | 向所有目标玩家显示类似进度提示的“toast”消息 |
| [Speak](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/speak) | MythicMobs | 让施法者通过聊天和对话气泡说话 |

[>> 到顶部](mechanic-tags.md)

## 元机制 {#meta}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Command](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/command) | MythicMobs | 对传入的每个目标执行命令 |
| [ModifyDamage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ModifyDamage) | MythicMobs | 修改触发此技能的伤害事件。 |
| [Globalcooldown](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/globalcooldown) | MythicMobs | Global Cooldown 技能可设置施法者的全局…… |
| [Log](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Log) | MythicMobs | 直接向控制台记录消息 |
| [Modifyprojectile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/modifyprojectile) | MythicMobs | 修改激活此技能机制的 projectile、missile 或 orbital |
| [PrintParentTree](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PrintParentTree) | MythicMobs | 输出执行此机制的元技能及其 SkillTree 的调试信息。 |
| [Projectilevelocity](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/projectilevelocity) | MythicMobs | 修改调用此机制的 [Projectile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/projectile) 或 [Missile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/missile) 的速度 |
| [Remove](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/remove) | MythicMobs | 移除目标实体 |
| [Removeowner](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/removeowner) | MythicMobs | 移除施法者的 Mythic 主人和原版主人 |
| [SetChunkForceLoaded](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetChunkForceLoaded) | MythicMobs | 设置某个位置所在区块的强制加载状态。 |
| [Setowner](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setowner) | MythicMobs | 将 Mythic 生物的 "owner" 属性设为指定目标 |
| [SetParent](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetParent) | MythicMobs | 将施法 MythicMob 的 "Parent" 设为目标实体 |
| [Setprojectilebulletmodel](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setprojectilebulletmodel) | MythicMobs | 设置当前投射物弹体的 CustomModelData |
| [SetProjectileDirection](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetProjectileDirection) | MythicMobs | 将发起调用的弹射物的移动方向设为朝向给定目标。 |
| [Tracklocation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/tracklocation) | MythicMobs | 将施法生物的追踪位置设为目标位置 |
| [Signal](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/signal) | MythicMobs | 向指定目标选择器发送信号 |
| [Setskillcooldown](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setskillcooldown) | MythicMobs | 将指定元技能的冷却时间设为指定值（以秒为单位） |
| [Switch](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Switch) | MythicMobs | switch 可将条件与一组（cases）值进行比较 |
| [Endprojectile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/endprojectile) | MythicMobs | 终止调用此机制的投射物，并在此过程中激活其 onEnd 技能 |

### 流程控制 {#flow}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Cancelevent](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/cancelevent) | MythicMobs | 取消触发该技能的事件 |
| [CancelSkill](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/CancelSkill) | MythicMobs | 触发时取消[元技能](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Metaskills)的执行 |
| [Delay](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/delay) | MythicMobs | 使当前技能树延迟 X 刻 |
| [Wait](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Wait) | MythicMobs | 暂停元技能（类似 [delay](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/delay) 技能机制），直到满足一组条件 |

[>> 到顶部](mechanic-tags.md)

## Meta-Mechanic {#meta-mechanic}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Aura](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/aura) | MythicMobs | Aura 技能机制作为目标实体上的状态效果，可以…… |
| [Beam](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/beam) | MythicMobs | 在施法者与目标之间创建由指定材质组成的光束。 |
| [Chain](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/chain) | MythicMobs | Chain 可制作在目标之间弹跳的技能，例如…… |
| [Chainmissile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/chainmissile) | MythicMobs | 向目标发射会连锁追踪的导弹 |
| [Skill](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/skill) | MythicMobs | 执行另一个[元技能](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Metaskills)，该元技能必须位于…… |
| [ForEach](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ForEach) | MythicMobs | 对技能机制的每个目标*分别执行一次*指定元技能 |
| [ForEachValue](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ForEachValue) | MythicMobs | 对指定列表/映射格式值中的每个值*分别执行一次*指定元技能 |
| [Variableskill](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/variableskill) | MythicMobs | 与 [Skill 技能机制](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/skill)类似，执行另一个元技能，但允许在 skill 属性中使用占位符 |
| [Pickupitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/pickupitem) | MythicMobs | 若施法者为玩家，拾取目标物品 |
| [Polygon](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/polygon) | MythicMobs | Polygon 元机制可按多边形图案执行其他技能 |
| [Projectile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/projectile) | MythicMobs | Projectile 技能会发射一个可添加装饰的元“投射物”…… |
| [Randomskill](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/randomskill) | MythicMobs | 从给定的[技能](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/skill)列表中随机执行一个技能 |
| [Raytrace](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/raytrace) | MythicMobs | 向目标进行射线追踪 |
| [Raytraceto](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/raytraceto) | MythicMobs | 类似 [Raytrace](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/raytrace) 技能机制，向目标进行射线追踪，但增加了有关射线起点和终点的属性 |
| [Shoot](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shoot) | MythicMobs | 向目标实体或位置发射箭或物品投射物 |
| [Shootshulkerbullet](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shootshulkerbullet) | MythicMobs | 向目标实体发射潜影贝子弹，命中后使其漂浮 |
| [Setskillcooldown](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setskillcooldown) | MythicMobs | 将指定元技能的冷却时间设为指定值（以秒为单位） |
| [Slash](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/slash) | MythicMobs | Slash 元机制可按斩击形状执行其他技能 |
| [Sudoskill](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/sudoskill) | MythicMobs | SudoSkill 技能机制可强制目标实体“施放”…… |
| [Switch](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Switch) | MythicMobs | switch 可将条件与一组（cases）值进行比较 |
| [Totem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/totem) | MythicMobs | totem 技能机制会放置一个不可见的“图腾”，类似…… |
| [Volley](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/volley) | MythicMobs | 向目标实体或……齐射箭或物品投射物 |

### Aura {#aura}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Aura](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/aura) | MythicMobs | Aura 技能机制作为目标实体上的状态效果，可以…… |
| [Auraremove](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/auraremove) | MythicMobs | 移除目标上的光环 |
| [BlackScreen](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/BlackScreen) | MythicMobs | 使玩家的屏幕变黑 |
| [Bouncy](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Bouncy) | MythicMobs | 为目标应用使其具有弹性的光环 |
| [Cast](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/cast) | MythicMobs | Cast 是一种 [Aura] 技能机制，类似…… |
| [FollowPath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FollowPath) | MythicMobs | 创建一个使持有生物沿路径移动的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura) |
| [FollowPath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FollowPath) | MythicMobs | 创建一个使持有生物沿路径移动的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura) |
| [FormLine](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FormLine) | MythicMobs | 使施法生物沿直线路径移动到指定位置 |
| [Hide](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/hide) | MythicMobs | 在指定时间内向目标玩家隐藏施法者 |
| [Orbital](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/orbital) | MythicMobs | Orbital 技能会发射一种特殊类型的…… |
| [Terminable](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Terminable) | MythicMobs | 创建一个[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/aura)，每刻检查一组条件是否满足；满足时立即取消 onStart 技能的执行。 |
| [Onjump](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/onjump) | MythicMobs | 为目标施加一个在其跳跃时触发技能的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura)。 |

### 可衔接 {#thenable}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Dropitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/dropitem) | MythicMobs | 掉落一组物品，或选择…… |
| [PushBlock](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PushBlock) | MythicMobs | 使用活塞逻辑，沿给定方向推动目标位置的方块。 |
| [Remove](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/remove) | MythicMobs | 移除目标实体 |
| [StealItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/StealItem) | MythicMobs | 从目标处偷取一件物品，并放到生物手中。 |
| [Summon](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/summon) | MythicMobs | 在目标周围召唤给定类型的生物。 |
| [Wait](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Wait) | MythicMobs | 暂停元技能（类似 [delay](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/delay) 技能机制），直到满足一组条件 |
| [Furnitureremoveat](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/furnitureremoveat) | MythicCrucible | 移除目标位置的家具。 |

[>> 到顶部](mechanic-tags.md)

## Mount {#mount}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Dismount](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/dismount) | MythicMobs | 生物骑乘其他对象时，使其离开坐骑。 |
| [Ejectpassenger](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ejectpassenger) | MythicMobs | 使当前骑乘生物的所有乘客离开。 |
| [Mount](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/mount) | MythicMobs | 使施法生物召唤指定的 MythicMob 并骑乘它。 |
| [Mountme](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/mountme) | MythicMobs | 使目标骑乘施法生物。 |
| [Mounttarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/mounttarget) | MythicMobs | 使生物“骑乘”指定目标选择器选中的对象，就像骑乘……一样。 |
| [Remount](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/remount) | MythicMobs | 使施法生物重新骑乘其生成时骑乘的生物。 |
| [Summonpassenger](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/summonpassenger) | MythicMobs | 召唤一个骑乘施法者的生物。 |

[>> 到顶部](mechanic-tags.md)

## 移动 {#movement}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Disengage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/disengage) | MythicMobs | 使施法者向后跳跃，远离目标实体。 |
| [FollowPath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FollowPath) | MythicMobs | 创建一个使持有生物沿路径移动的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura) |
| [FollowPath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FollowPath) | MythicMobs | 创建一个使持有生物沿路径移动的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura) |
| [FormLine](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/FormLine) | MythicMobs | 使施法生物沿直线路径移动到指定位置 |
| [Goto](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/goto) | MythicMobs | 使生物寻路到指定位置 |
| [Jump](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/jump) | MythicMobs | 使生物以给定速度跳跃。 |
| [Leap](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/leap) | MythicMobs | 使生物在空中向目标跃去。 |
| [Lunge](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/lunge) | MythicMobs | 为目标施加向前的速度。 |
| [Propel](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/propel) | MythicMobs | 推动此机制的施法者朝目标移动。 |
| [Pull](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/pull) | MythicMobs | 以基础速度将所有目标实体拉向施法者，…… |
| [Throw](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/throw) | MythicMobs | 将所有目标抛向远离生物或原点的方向。 |
| [DirectionalVelocity](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/DirectionalVelocity) | MythicMobs | 沿指定向量改变目标实体的速度。 |
| [Velocity](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/velocity) | MythicMobs | 修改目标实体的速度。 |

### 旋转 {#rotation}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Look](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/look) | MythicMobs | 使实体看向其目标。 |
| [MatchRotation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/MatchRotation) | MythicMobs | 将目标的偏航角和俯仰角设为与指定 target 属性所指对象相同的值。 |
| [Recoil](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Recoil) | MythicMobs | 使目标的屏幕抖动，以模拟后坐力。 |
| [RotateTowards](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/RotateTowards) | MythicMobs | 使施法者转向目标位置，偏航角和俯仰角相对于当前角度的变化不超过指定最大增量。 |
| [SetPitch](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetPitch) | MythicMobs | 设置目标实体头部的俯仰角。 |
| [Setrotation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setrotation) | MythicMobs | 更改目标的旋转角度，仅适用于非玩家实体。 |
| [Spin](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Spin) | MythicMobs | 使目标实体在给定持续时间内旋转。 |

### Teleport {#teleport}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Forcepull](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/forcepull) | MythicMobs | 将所有目标实体传送到 <spread> 范围内的某个位置。 |
| [Swap](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/swap) | MythicMobs | 交换施法者与目标的位置。 |
| [Teleportin](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/teleportin) | MythicMobs | 相对于施法者的偏航角传送目标。 |
| [Teleport](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/teleport) | MythicMobs | 将施法者传送至目标位置或实体。 |
| [Teleportto](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/teleportto) | MythicMobs | 将一个或多个目标实体传送至指定位置。 |
| [Teleporty](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/teleporty) | MythicMobs | 将施法者传送至指定 Y 坐标。 |

[>> 到顶部](mechanic-tags.md)

## Paper-Only {#paper-only}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [GoatRam](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/GoatRam) | MythicMobs | 使施法的山羊生物冲撞目标实体。 |
| [Onjump](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/onjump) | MythicMobs | 为目标施加一个在其跳跃时触发技能的[光环](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/aura)。 |
| [PlayBlockBreakSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockBreakSound) | MythicMobs | 播放目标方块的破坏声音 |
| [PlayBlockFallSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockFallSound) | MythicMobs | 播放目标方块的掉落声音 |
| [PlayBlockHitSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockHitSound) | MythicMobs | 播放目标方块被击打（受损）时的声音 |
| [PlayBlockPlaceSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockPlaceSound) | MythicMobs | 播放目标方块的放置声音 |
| [PlayBlockStepSound](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PlayBlockStepSound) | MythicMobs | 播放目标方块的脚步声（实体在其上行走时播放的声音） |

[>> 到顶部](mechanic-tags.md)

## Pin {#pin}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [MovePin](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/MovePin) | MythicMobs | 将给定[定位点](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Pins)移至目标位置。 |

[>> 到顶部](mechanic-tags.md)

## Premium-Only {#premium-only}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Chainmissile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/chainmissile) | MythicMobs | 向目标发射会连锁追踪的导弹 |
| [Raytrace](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/raytrace) | MythicMobs | 向目标进行射线追踪 |
| [Raytraceto](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/raytraceto) | MythicMobs | 类似 [Raytrace](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/raytrace) 技能机制，向目标进行射线追踪，但增加了有关射线起点和终点的属性 |
| [Fawepaste](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/fawepaste) | MythicMobs | 使用此处的 FAWE 插件粘贴结构模板：[FAWE](https://www.spigotmc.org/resources/fast-async-worldedit.13932/)。 |
| [WorldEditReplace](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/WorldEditReplace) | MythicMobs | 使用 WorldEdit 替换区域中的方块。 |

[>> 到顶部](mechanic-tags.md)

## Projectile {#projectile}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Arrowvolley](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/arrowvolley) | MythicMobs | 向目标齐射一轮箭矢，并可配置多种属性。 |
| [Missile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/missile) | MythicMobs | missile 机制与 projectile 机制类似，可使用任意[弹射物可继承属性](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/projectile#inheritable-attributes)。 |
| [Chainmissile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/chainmissile) | MythicMobs | 向目标发射会连锁追踪的导弹 |
| [Orbital](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/orbital) | MythicMobs | Orbital 技能会发射一种特殊类型的…… |
| [Projectile](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/projectile) | MythicMobs | Projectile 技能会发射一个可添加装饰的元“投射物”…… |
| [Shootfireball](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shootfireball) | MythicMobs | 从生物处向目标实体或位置发射火球。 |
| [Shoot](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shoot) | MythicMobs | 向目标实体或位置发射箭或物品投射物 |
| [Shootpotion](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shootpotion) | MythicMobs | 向目标实体或位置投掷药水，产生喷溅效果。 |
| [Shootshulkerbullet](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shootshulkerbullet) | MythicMobs | 向目标实体发射潜影贝子弹，命中后使其漂浮 |
| [Shootskull](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shootskull) | MythicMobs | 从生物处向目标实体或……发射凋灵之首。 |
| [Volley](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/volley) | MythicMobs | 向目标实体或……齐射箭或物品投射物 |

[>> 到顶部](mechanic-tags.md)

## 随机 {#random}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Randommessage](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/randommessage) | MythicMobs | 向目标玩家发送随机消息。 |
| [Randomskill](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/randomskill) | MythicMobs | 从给定的[技能](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/mechanics/skill)列表中随机执行一个技能 |

[>> 到顶部](mechanic-tags.md)

## 计分板 {#scoreboard}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Modifyglobalscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/modifyglobalscore) | MythicMobs | 修改虚拟玩家 `__GLOBAL__` 的记分项数值。 |
| [Modifymobscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/modifymobscore) | MythicMobs | 修改施法生物的记分项数值。 |
| [Modifyscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/modifyscore) | MythicMobs | 修改指定名称的虚拟玩家的记分项数值。 |
| [Modifytargetscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/modifytargetscore) | MythicMobs | 修改指定目标选择器所选目标的记分项数值。 |
| [Setmobscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setmobscore) | MythicMobs | 修改施法生物的记分项数值。 |
| [Setscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setscore) | MythicMobs | 修改指定名称的虚拟玩家的记分项数值。 |
| [Settargetscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/settargetscore) | MythicMobs | 修改指定目标选择器所选目标的记分项数值。 |
| [Addtag](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/addtag) | MythicMobs | 为目标添加记分板标签。 |
| [Removetag](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/removetag) | MythicMobs | 移除目标的记分板标签。 |

[>> 到顶部](mechanic-tags.md)

## Summon {#summon}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [SummonAreaEffectCloud](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SummonAreaEffectCloud) | MythicMobs | 在目标位置周围创建粒子云。 |
| [SummonFallingBlock](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SummonFallingBlock) | MythicMobs | 在目标位置召唤指定材质的下落方块。 |
| [Summon](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/summon) | MythicMobs | 在目标周围召唤给定类型的生物。 |
| [Summonpassenger](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/summonpassenger) | MythicMobs | 召唤一个骑乘施法者的生物。 |

[>> 到顶部](mechanic-tags.md)

## Threat {#threat}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [ClearTarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ClearTarget) | MythicMobs | 强制此机制的目标重置其当前目标。 |
| [Rally](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/rally) | MythicMobs | 召集附近给定类型的生物，集中攻击给定目标。 |
| [Settarget](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/settarget) | MythicMobs | 将生物的目标设为目标实体。 |
| [Threat](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/threat) | MythicMobs | 修改生物对目标的仇恨值。 |
| [Taunt](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Taunt) | MythicMobs | 修改目标实体对施法者的仇恨值。 |
| [Clearthreat](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/clearthreat) | MythicMobs | 使生物清空其仇恨表。 |

[>> 到顶部](mechanic-tags.md)

## 变量 {#variable}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Variableadd](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/variableadd) | MythicMobs | 为指定……上的[变量](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/variables)增加一个数值。 |
| [Variablemath](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/variablemath) | MythicMobs | 将变量设为数学方程的结果，其中 'x' 表示…… |
| [VariableMove](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/VariableMove) | MythicMobs | 在不同名称或注册表之间移动已创建的变量。 |
| [Setvariablelocation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setvariablelocation) | MythicMobs | 设置一个字符串类型的值。 |
| [Setvariable](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setvariable) | MythicMobs | 设置一个[变量](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/variables)。 |
| [Variablesubtract](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/variablesubtract) | MythicMobs | 从指定……上的[变量](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/variables)中减去一个数值。 |
| [Variableunset](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/variableunset) | MythicMobs | 取消设置一个[变量](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/skills/variables)。 |

[>> 到顶部](mechanic-tags.md)

## World {#world}

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Blockdestabilize](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/blockdestabilize) | MythicMobs | 将目标位置的方块变为下落方块，使其开始下落，如同受到重力影响。 |
| [Blockphysics](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/blockphysics) | MythicMobs | 强制更新目标位置的方块物理状态。 |
| [Bonemeal](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/bonemeal) | MythicMobs | 对目标方块施加骨粉效果。 |
| [BreakBlockAndGiveItem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/breakBlockAndGiveItem) | MythicMobs | 破坏目标位置的方块并给予物品 |
| [Breakblock](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/breakblock) | MythicMobs | 破坏目标位置的方块。 |
| [EnderDragonResetCrystals](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EnderDragonResetCrystals) | MythicMobs | 目标位置所在维度正在进行末影龙战斗时，生成 EnderDragon 水晶。 |
| [Explosion](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/explosion) | MythicMobs | 在目标实体或位置制造爆炸 |
| [FillChest](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/fillChest) | MythicMobs | 使用物品列表或[掉落表](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/drops/DropTables)填充箱子 |
| [Pickupitem](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/pickupitem) | MythicMobs | 若施法者为玩家，拾取目标物品 |
| [Prison](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/prison) | MythicMobs | 将目标实体封在临时的方块囚笼中。 |
| [PushBlock](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/PushBlock) | MythicMobs | 使用活塞逻辑，沿给定方向推动目标位置的方块。 |
| [Pushbutton](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/pushbutton) | MythicMobs | 按下给定坐标处的按钮。 |
| [SetBlockOpen](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetBlockOpen) | MythicMobs | 设置目标方块的打开状态。 |
| [Setblocktype](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setblocktype) | MythicMobs | 更改目标位置的方块类型。 |
| [Spring](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/spring) | MythicMobs | 在目标实体或位置创建临时液体“泉源”。 |
| [ThunderLevel](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ThunderLevel) | MythicMobs | 为每个玩家单独产生无雨的雷暴效果。 |
| [Time](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/Time) | MythicMobs | 设置世界时间 |
| [Togglelever](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/togglelever) | MythicMobs | 切换给定坐标处拉杆的开关状态。 |
| [Togglepiston](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/togglepiston) | MythicMobs | 切换目标位置活塞的状态。 |
| [Undopaste](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/undopaste) | MythicMobs | 根据粘贴操作的 ID 或使用的结构模板，撤销之前通过 [fawePaste](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/mechanics/fawepaste/) 机制完成的粘贴。 |
| [Weather](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/weather) | MythicMobs | 更改施法生物所在世界的天气。 |
| [Fawepaste](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/fawepaste) | MythicMobs | 使用此处的 FAWE 插件粘贴结构模板：[FAWE](https://www.spigotmc.org/resources/fast-async-worldedit.13932/)。 |
| [BlockCrack](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/BlockCrack) | MythicCrucible | 向指定接收对象显示目标方块的裂纹效果 |

[>> 到顶部](mechanic-tags.md)

## 无标签 {#untagged}

这些机制尚未被标记。

| 技能机制 | 插件 | 说明 |
| --- | --- | --- |
| [Activatespawner](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/activatespawner) | MythicMobs | 激活 MythicMobs [刷怪器](../../spawners.md)，使其生成生物。 |
| [AddTrade](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/AddTrade) | MythicMobs | 更改村民的交易。 |
| [Animatearmorstand](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/animatearmorstand) | MythicMobs | 使盔甲架在指定时间内变为某种姿势。 |
| [ArmAnimation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ArmAnimation) | MythicMobs | 使施法的**玩家**挥动手臂。 |
| [SwingOffhand](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SwingOffhand) | MythicMobs | 使施法玩家挥动副手。 |
| [CinematicCamera](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/CinematicCamera) | MythicMobs | 为目标玩家播放平滑的过场动画镜头路径，使其视角沿一系列关键帧移动。 |
| [CinematicCancel](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/CinematicCancel) | MythicMobs | 打断目标玩家正在播放的 [cinematicCamera](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/CinematicCamera)，立即恢复其镜头和控制权。 |
| [Currencygive](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/currencygive) | MythicMobs | 给予玩家货币。 |
| [Currencytake](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/currencytake) | MythicMobs | 扣除玩家的货币。 |
| [DetermineCondition](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/DetermineCondition) | MythicMobs | 确定通过 [MetaskillCondition](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Conditions/MetaskillCondition) 条件作为条件使用的元技能的结果。 |
| [DisplayTransformation](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/DisplayTransformation) | MythicMobs | 设置目标展示实体的变换。 |
| [EnderDragonSetPhase](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EnderDragonSetPhase) | MythicMobs | 设置目标 EnderDragon 实体的阶段。 |
| [EnderDragonSetRespawnPhase](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EnderDragonSetRespawnPhase) | MythicMobs | 目标位置所在维度正在进行 EnderDragon 战斗时，设置 EnderDragon 的重生阶段。 |
| [EnderDragonSpawnPortal](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/EnderDragonSpawnPortal) | MythicMobs | 生成 EnderDragon 战斗的传送门。 |
| [Extinguish](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/extinguish) | MythicMobs | 清除目标实体的所有燃烧刻数。 |
| [Feed](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/feed) | MythicMobs | 为目标玩家补充饥饿值。 |
| [ForEachPin](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ForEachPin) | MythicMobs | 对多点定位标记中的每个定位点执行给定元技能。 |
| [Freeze](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/freeze) | MythicMobs | 设置在细雪中被冻结的刻数。 |
| [Hologram](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/hologram) | MythicMobs | 在目标位置生成全息显示。 |
| [Ignite](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ignite) | MythicMobs | 点燃目标实体。 |
| [OnKeyPress](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/OnKeyPress) | MythicMobs | 为目标实体施加一个在玩家按下指定按键时触发技能的光环。 |
| [OnKeyRelease](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/OnKeyRelease) | MythicMobs | 为目标实体施加一个在玩家松开指定按键时触发技能的光环。 |
| [OpenCustomMenu](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/OpenCustomMenu) | MythicMobs | 打开一个[自定义菜单](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Custom-Menus)。 |
| [OpenTrades](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/OpenTrades) | MythicMobs | 为目标玩家打开施法村民的交易界面。 |
| [Oxygen](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/oxygen) | MythicMobs | 为目标玩家补充指定数量的氧气。 |
| [Posearmorstand](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/posearmorstand) | MythicMobs | 移动盔甲架的肢体，数值单位为弧度。 |
| [Potionclear](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/potionclear) | MythicMobs | 清除目标实体的所有药水效果。 |
| [Potion](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/potion) | MythicMobs | 对目标实体施加药水效果，通常…… |
| [Sendresourcepack](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/sendresourcepack) | MythicMobs | 向目标玩家发送资源包。 |
| [Setcollidable](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setcollidable) | MythicMobs | 设置此机制的目标是否具有可碰撞的碰撞箱。 |
| [SetCustomMenuButton](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetCustomMenuButton) | MythicMobs | 将已打开的[自定义菜单](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Custom-Menus)中的指定槽位设为指定按钮。 |
| [SetDragonPodium](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetDragonPodium) | MythicMobs | 将龙的基座位置设为目标位置，即龙盘旋时环绕的中心点。 |
| [SetFaction](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setFaction) | MythicMobs | 设置或更改目标生物的阵营。 |
| [SetFlying](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetFlying) | MythicMobs | 设置目标玩家是否正在飞行。 |
| [Setgamemode](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setgamemode) | MythicMobs | 设置目标玩家的游戏模式。 |
| [Setgliding](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setgliding) | MythicMobs | 使装备鞘翅的实体开始或停止滑翔。 |
| [Setglobalscore](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setglobalscore) | MythicMobs | 修改虚拟玩家 `__GLOBAL__` 的记分项数值。 |
| [SetInteractionSize](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetInteractionSize) | MythicMobs | 设置目标 `INTERACTION` [类型](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/mythiccraft/MythicMobs/-/wikis/Mobs/Mobs#type)实体的大小。 |
| [SetItemGroupCooldown](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetItemGroupCooldown) | MythicMobs | 为目标玩家设置物品组冷却。 |
| [Setleashholder](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setleashholder) | MythicMobs | 将施法者的拴绳持有者设为目标实体。 |
| [Setlevel](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setlevel) | MythicMobs | 使施法生物改变等级。 |
| [Setmaterialcooldown](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setmaterialcooldown) | MythicMobs | 为目标玩家指定材质的物品设置冷却。 |
| [Setmobcolor](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setmobcolor) | MythicMobs | 更改目标的颜色，仅适用于可改变颜色的生物，例如…… |
| [Setname](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setname) | MythicMobs | 设置施法者的显示名称。 |
| [Setnodamageticks](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setnodamageticks) | MythicMobs | 设置目标的无敌刻数。 |
| [SetPose](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetPose) | MythicMobs | 设置实体的[姿势](https://jd.papermc.io/paper/1.21.6/org/bukkit/entity/Pose.html)。 |
| [SetRaiderCanJoinRaid](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setRaiderCanJoinRaid) | MythicMobs | 设置目标袭击者实体是否可以加入袭击。 |
| [Setraiderpatrolblock](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setraiderpatrolblock) | MythicMobs | 设置目标袭击者巡逻给定位置。 |
| [Setraiderpatrolleader](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setraiderpatrolleader) | MythicMobs | 设置目标袭击者是否为袭击者巡逻队长。 |
| [Setspeed](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setspeed) | MythicMobs | 更改目标的速度属性。 |
| [Setstance](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setstance) | MythicMobs | 将目标 Mythic Mob 的“stance”属性设为给定值。 |
| [SetTextDisplay](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/SetTextDisplay) | MythicMobs | 设置目标文本展示实体的文本组件。 |
| [Setgravity](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/setgravity) | MythicMobs | 设置目标实体是否受重力影响。 |
| [Shieldbreak](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shieldbreak) | MythicMobs | 目标玩家正在格挡时，中断其盾牌格挡。 |
| [Shield](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shield) | MythicMobs | 增加伤害吸收生命值。 |
| [Shieldpercent](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/shieldpercent) | MythicMobs | 为目标实体施加吸收护盾，数值为其……的一定百分比。 |
| [CloseDialog](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/CloseDialog) | MythicMobs | 关闭目标玩家打开的任何[对话框](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Dialogs)。 |
| [ShowDialog](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Mechanics/ShowDialog) | MythicMobs | 向目标玩家显示[对话框](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Dialogs)。 |
| [ConsumeAmmo](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ConsumeAmmo) | MythicCrucible | 消耗弹药来执行技能。 |
| [ReloadAmmo](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ReloadAmmo) | MythicCrucible | 在施法者的物品栏中查找配置的弹药物品，被覆盖时则查找其他物品。每找到一个，就将其消耗并为物品补充弹药。 |
| [Consumeitem](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/Consumeitem) | MythicCrucible | 移除施法玩家物品栏中的部分物品。 |
| [ConsumeUsedItem](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ConsumeUsedItem) | MythicCrucible | 移除触发技能树的物品。 |
| [ProjectileHit](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ProjectileHit) | MythicCrucible | 模拟一次弓箭弹射物的命中。 |
| [GiveAmmo](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/GiveAmmo) | MythicCrucible | 将玩家武器的弹药数量设为最大值。 |
| [InventoryClear](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/InventoryClear) | MythicCrucible | 清空目标玩家的物品栏。 |
| [OpenBackpack](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/OpenBackpack) | MythicCrucible | 打开在玩家物品栏中找到的第一个背包。 |
| [Parsearmor](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/parsearmor) | MythicCrucible | 更新目标玩家盔甲部件的状态。 |
| [ParseWeapon](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ParseWeapon) | MythicCrucible | 更新目标玩家主手物品的状态。 |
| [UpdateLore](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/UpdateLore) | MythicCrucible | 重新解析物品配置中的描述。 |
| [RemoveTriggeringItem](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/RemoveTriggeringItem) | MythicCrucible | 移除触发 SkillTree 的物品实体。 |
| [ResetAttackCooldown](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ResetAttackCooldown) | MythicCrucible | 重置手持物品的攻击冷却。 |
| [SetCompassLocation](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetCompassLocation) | MythicCrucible | 设置指南针指向的位置。 |
| [SetCompassLodestone](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetCompassLodestone) | MythicCrucible | 将指南针指向的位置设置为磁石位置。 |
| [Setcrossbowcharged](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/setcrossbowcharged) | MythicCrucible | 设置目标玩家手持弩的 CustomModelData，并在外观上将其设为已装填或未装填状态。 |
| [SetItemCustomModelData](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetItemCustomModelData) | MythicCrucible | 设置所用物品的 CustomModelData。 |
| [SetItemDisplay](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetItemDisplay) | MythicCrucible | 设置物品的显示名称。 |
| [SetLore](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetLore) | MythicCrucible | 设置物品的新描述。 |
| [ModelSet](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/ModelSet) | MythicCrucible | 为施法者手持物品设置指定的模型/[CustomModelData](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/skills/mechanics/SetItemCustomModelData)。 |
| [SetSlotModel](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetSlotModel) | MythicCrucible | 为指定槽位的物品设置指定的 CustomModelData。 |
| [SnapshotUsedBow](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SnapshotUsedBow) | MythicCrucible | 保存手持弓状态的快照，供后续弹射物伤害机制使用。 |
| [Modeltoggle](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/modeltoggle) | MythicCrucible | 每次触发此机制时，在两个指定值之间切换物品的 CustomModelData。 |
| [UpgradeItem](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/UpgradeItem) | MythicCrucible | 提升指定槽位物品的[等级](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Levels)。 |
| [FurnitureVariableSet](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/FurnitureVariableSet) | MythicCrucible | 为目标家具实体设置变量。 |
| [Furnitureinventory](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/furnitureinventory) | MythicCrucible | 为目标玩家打开具有指定槽位数量和名称的物品栏。 |
| [OpenFurniturePainter](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/OpenFurniturePainter) | MythicCrucible | 为目标玩家打开家具的绘色界面。 |
| [PlaceFurnitureAt](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/PlaceFurnitureAt) | MythicCrucible | 使施法玩家在指定位置放置家具。 |
| [Furnitureremove](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/furnitureremove) | MythicCrucible | 移除施放此机制的家具。 |
| [FurnitureSetAt](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/FurnitureSetAt) | MythicCrucible | 在目标位置设置家具。 |
| [Furniturecolor](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/furniturecolor) | MythicCrucible | 将施法家具的[颜色](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Furniture#color)设为指定颜色。 |
| [Furniturestate](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/furniturestate) | MythicCrucible | 将施法家具的[状态](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Furniture#furniture-states)设为指定状态。 |
| [Furniturestate](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/furniturestate) | MythicCrucible | 将施法家具的[状态](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Furniture#furniture-states)设为指定状态。 |
| [SetItemNBT](https://git.lumine.io/mythiccraft/mythiccrucible/-/wikis/Skills/Mechanics/SetItemNBT) | MythicCrucible | 为物品设置 NBT 值。 |
| [AnimateModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/AnimateModel) | ModelEngine | 通过程序控制模型骨骼的动画，不依赖已有动画。 |
| [Brightness](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Brightness) | ModelEngine | 配置模型的方块光照和天空光照。 |
| [ChangeParent](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/ChangeParent) | ModelEngine | 将某根骨骼的父骨骼更改为另一根骨骼。 |
| [ChangePart](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/ChangePart) | ModelEngine | 将渲染骨骼所用的模型更改为其他模型。 |
| [CycleParts](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/CycleParts) | ModelEngine | 按预定义的序列，将渲染骨骼所用的模型更改为其他模型。 |
| [Enchant](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Enchant) | ModelEngine | 为整个模型或指定骨骼添加附魔光效。 |
| [Glow](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Glow) | ModelEngine | 配置模型的发光效果和发光颜色。 |
| [ModelPlayerSkin](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/ModelPlayerSkin) | ModelEngine | 将模型的玩家肢体骨骼设置为目标玩家的皮肤。 |
| [PartVisibility](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/PartVisibility) | ModelEngine | 切换渲染骨骼的可见性。 |
| [Segment](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Segment) | ModelEngine | 配置分段骨骼或尾部骨骼。 |
| [Tint](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Tint) | ModelEngine | 为整个模型或指定骨骼上色。 |
| [Move](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Move) | ModelEngine | 直接控制实体向指定方向移动。 |
| [NoFall](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/NoFall) | ModelEngine | 取消实体的下落。 |
| [SyncYaw](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/SyncYaw) | ModelEngine | 将实体的偏航角同步为头部或身体的偏航角。 |
| [ModelUndisguise](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/ModelUndisguise) | ModelEngine | 取消目标玩家的伪装。 |
| [BodyRotation](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/BodyRotation) | ModelEngine | 配置模型实体的身体旋转。 |
| [CullConfig](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/CullConfig) | ModelEngine | 配置模型实体的剔除。 |
| [Model](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Model) | ModelEngine | 为目标实体添加或移除模型。 |
| [PairModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/PairModel) | ModelEngine | 强制向目标玩家显示或隐藏模型实体。 |
| [Petrify](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Petrify) | ModelEngine | 创建模型的雕像。 |
| [BindHitbox](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/BindHitbox) | ModelEngine | 召唤一个实体，并将其绑定到子碰撞箱。 |
| [HitboxConfig](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/HitboxConfig) | ModelEngine | 配置子碰撞箱的伤害传递倍率。 |
| [LinkItemBone](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/LinkItemBone) | ModelEngine | 将装备槽位关联到物品骨骼，使其自动更新物品。 |
| [Leash](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Leash) | ModelEngine | 在视觉上将目标拴到模型的拴绳骨骼上。 |
| [LeashSelf](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/LeashSelf) | ModelEngine | 在视觉上将一根拴绳骨骼拴到同一模型的另一根拴绳骨骼上。 |
| [DefaultState](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/DefaultState) | ModelEngine | 配置活动模型的默认动画。 |
| [LockModelHead](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/LockModelHead) | ModelEngine | 将模型的头部锁定在原位。 |
| [LockModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/LockModel) | ModelEngine | 锁定或解锁模型实体的旋转。 |
| [ModifyState](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/ModifyState) | ModelEngine | 修改目标活动模型正在播放的动画。 |
| [RemapModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/RemapModel) | ModelEngine | 将新模型逐部分重新映射到当前模型。 |
| [RenderInit](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/RenderInit) | ModelEngine | 如果此前已通过设置 `initrender` 将模型应用于模型实体，则向玩家显示该模型。 |
| [RootMotion](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/RootMotion) | ModelEngine | 设置模型的根运动选项。 |
| [Scale](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/Scale) | ModelEngine | 缩放模型的碰撞箱或渲染比例。 |
| [State](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/State) | ModelEngine | 播放或停止模型的动画。 |
| [StateToggle](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/StateToggle) | ModelEngine | 切换模型的某个状态。 |
| [SubModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/SubModel) | ModelEngine | 强制创建或删除模型中的骨骼。 |
| [SwapEntity](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/SwapEntity) | ModelEngine | 将活动模型的所有者从一个实体切换为目标实体。 |
| [DismountAllModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/DismountAllModel) | ModelEngine | 使模型或指定坐骑骨骼上的所有乘客下坐骑。 |
| [DismountModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/DismountModel) | ModelEngine | 使指定坐骑骨骼列表上的驾驶者或指定乘客下坐骑。 |
| [MountModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/MountModel) | ModelEngine | 将实体放到模型的驾驶座或指定坐骑骨骼上。 |
| [SetModelTag](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/SetModelTag) | ModelEngine | 设置名称标签骨骼的文字。 |
| [SetModelTagVisible](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/SetModelTagVisible) | ModelEngine | 设置名称标签骨骼的可见性。 |
| [VFXChangeModel](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXChangeModel) | ModelEngine | 更改 VFX 的模型。 |
| [VFXEnchant](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXEnchant) | ModelEngine | 为 VFX 添加或移除附魔光效。 |
| [VFX](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFX) | ModelEngine | 为实体或弹射物分配或移除 VFX。 |
| [VFXPosReset](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXPosReset) | ModelEngine | 将 VFX 的位置重置为 0 0 0。 |
| [VFXRotReset](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXRotReset) | ModelEngine | 将 VFX 的旋转角度重置为 0 0 0。 |
| [VFXScaleReset](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXScaleReset) | ModelEngine | 将 VFX 的缩放比例重置为 1 1 1。 |
| [VFXPos](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXPos) | ModelEngine | 设置 VFX 的位置。 |
| [VFXRot](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXRot) | ModelEngine | 设置 VFX 的旋转角度。 |
| [VFXScale](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXScale) | ModelEngine | 缩放 VFX。 |
| [VFXSetVis](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXSetVis) | ModelEngine | 设置 VFX 的可见性。 |
| [VFXTint](https://git.lumine.io/mythiccraft/model-engine-4/-/wikis/Skills/Mechanics/VFXTint) | ModelEngine | 为 VFX 上色，或使其颜色从一种渐变为另一种。 |
| [BindSpell](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/BindSpell) | MythicRPG | 将已学会的[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)强制绑定到目标玩家的快捷栏槽位。 |
| [CancelCast](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/CancelCast) | MythicRPG | 取消目标玩家正在进行的[法术施放](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells/Casting#cast-time)。 |
| [CastSpell](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/CastSpell) | MythicRPG | 在目标玩家上施放一个已学会的[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)，并经过完整施法流程。 |
| [GiveMythicExperience](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/GiveMythicExperience) | MythicRPG | 给予玩家经验。 |
| [Interrupt](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/Interrupt) | MythicRPG | 打断目标正在进行的法术施放。 |
| [ModifyCastTime](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/ModifyCastTime) | MythicRPG | 修改目标玩家当前[施法](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells/Casting#cast-time)的剩余时间。 |
| [ModifyResource](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/ModifyResource) | MythicRPG | 为目标玩家的指定 reagent 增加给定数量。 |
| [ModifySpellCooldown](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/ModifySpellCooldown) | MythicRPG | 修改目标玩家已学会的[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)的冷却。 |
| [QuickcastingActivate](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/QuickcastingActivate) | MythicRPG | 在可行时，为施法玩家启用快速施法。 |
| [QuickcastingDeactivate](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/QuickcastingDeactivate) | MythicRPG | 在可行时，为施法玩家禁用快速施法。 |
| [SetActiveRPGProfile](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/SetActiveRPGProfile) | MythicRPG | 将施法玩家当前的 RPG 档案切换到给定槽位。 |
| [SetArchetype](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/SetArchetype) | MythicRPG | 设置目标玩家的原型。 |
| [BindSpell](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/BindSpell) | MythicRPG | 将已学会的[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)强制绑定到目标玩家的快捷栏槽位。 |
| [ForgetSpell](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/ForgetSpell) | MythicRPG | 使目标玩家遗忘一个[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)。 |
| [TeachSpell](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/TeachSpell) | MythicRPG | 教给玩家一个[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)。 |
| [UnsetSpellBinding](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/UnsetSpellBinding) | MythicRPG | 清除目标玩家给定快捷栏槽位当前绑定的[法术](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Spells)。 |
| [WaystoneClearRespawn](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneClearRespawn) | MythicRPG | 解除目标玩家的[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)重生点绑定。 |
| [WaystoneDiscover](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneDiscover) | MythicRPG | 将目标玩家标记为已发现某个[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)。 |
| [WaystoneForget](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneForget) | MythicRPG | 将目标玩家对某个[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)的状态重置为 UNDISCOVERED。 |
| [WaystoneHide](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneHide) | MythicRPG | 无论玩家的实际状态如何，都强制对该玩家隐藏[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)。 |
| [WaystoneOpenMenu](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneOpenMenu) | MythicRPG | 为目标玩家打开[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)传送菜单。 |
| [WaystoneReveal](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneReveal) | MythicRPG | 无论玩家的实际状态如何，都强制向该玩家显示[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)。 |
| [WaystoneSetRespawn](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneSetRespawn) | MythicRPG | 将目标玩家的重生点绑定到某个[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)。 |
| [WaystoneSetState](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneSetState) | MythicRPG | 用于将目标玩家对某个[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)的状态设置为三种状态之一的底层机制。 |
| [WaystoneTeleport](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Skills/Mechanics/WaystoneTeleport) | MythicRPG | 将目标玩家直接传送至[传送石](https://git.lumine.io/mythiccraft/mythicrpg/-/wikis/Waypoints)，跳过菜单。 |
| [GrantAchievement](https://git.lumine.io/mythiccraft/mythicachievements/-/wikis/Skills/Mechanics/GrantAchievement) | MythicAchievements | 授予玩家一个 Mythic 成就。 |
| [IncrementAchievement](https://git.lumine.io/mythiccraft/mythicachievements/-/wikis/Skills/Mechanics/IncrementAchievement) | MythicAchievements | 将成就条件的进度增加指定数量。 |
