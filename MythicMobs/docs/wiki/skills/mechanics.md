---
title: 技能机制
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 技能机制

技能机制（或基本技能）是MythicMobs中内置的简单技能。你可以在生物的技能列表中单独调用这些基本技能，也可以通过将这些机制组合在一起来创建自己的元技能。

有些机制能选择实体、位置或两者，也有些不选择任何目标。可使用[目标选择器](targeters.md)控制技能目标。

你还可以在[此处](tags/mechanic-tags.md)标签找到一些列出的机制

1. [附加机制](mechanics.md#additional-mechanics)
2. [机制](mechanics.md#mechanics)
   1. [元机制](mechanics.md#meta-mechanics)
3. [通用属性](mechanics.md#universal-attributes)
4. [示例](mechanics.md#examples)

# 额外技能机制 {#additional-mechanics}

由附加插件添加的机制的链接。如果没有安装该插件，这些链接中的任何机制都将无法工作。

- [ModelEngine 4](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics)
- [MythicCrucible](https://wiki.mythiccraft.io/mythiccrucible/Skills/Mechanics)
- [MythicEnchantments](https://wiki.mythiccraft.io/mythicenchants/Mechanics/Mechanics)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#mechanics)

# 技能机制 {#mechanics}

这些技能通常针对实体（玩家或其他生物），但有些技能也能够针对位置。

| 技能机制 | 说明 |
| --- | --- |
| [ActivateSpawner](mechanics/activatespawner.md) | 激活目标位置的 MythicMobs 刷怪器。 |
| [AddTrade](mechanics/addtrade.md) | 更改村民的交易。 |
| [AnimateArmorStand](mechanics/animatearmorstand.md) | 为盔甲架播放动作。 |
| [ArmAnimation](mechanics/armanimation.md) | 让施法者挥动手臂。 |
| [ArrowVolley](mechanics/arrowvolley.md) | 发射一轮箭矢。 |
| [Attribute](mechanics/attribute.md) | 目标实体支持属性时，为其设置一项属性。 |
| [AttributeModifier](mechanics/attributemodifier.md) | 为支持属性的目标添加属性修饰符。 |
| [AuraRemove](mechanics/auraremove.md) | 移除目标实体的一个[光环](mechanics/aura.md)。 |
| [BarCreate](mechanics/barcreate.md) | 为施法生物创建自定义 Boss 血条。 |
| [BarRemove](mechanics/barremove.md) | 移除施法生物的自定义 Boss 血条。 |
| [BarSet](mechanics/barset.md) | 修改施法生物的自定义 Boss 血条。 |
| [BlackScreen](mechanics/blackscreen.md) | 在指定持续时间内使目标的屏幕变黑。 |
| [BlockDestabilize](mechanics/blockdestabilize.md) | 使目标方块下落，如同受到重力影响。 |
| [BlockMask](mechanics/blockmask.md) | 暂时将某个方块伪装成另一种方块。 |
| [BlockUnmask](mechanics/blockunmask.md) | 取消已伪装方块的伪装。 |
| [BlockPhysics](mechanics/blockphysics.md) | 在目标位置触发方块物理更新。 |
| [BlockWave](mechanics/blockwave.md) | 在目标位置创建方块波浪。 |
| [BloodyScreen](mechanics/bloodyscreen.md) | 使目标的屏幕泛红。 |
| [BoneMeal](mechanics/bonemeal.md) | 对目标方块施加骨粉效果。 |
| [BossBorder](mechanics/bossborder.md) | 在生物周围创建无法逃出的边界。 |
| [Bouncy](mechanics/bouncy.md) | 为目标施加使其具有弹跳效果的[光环](mechanics/aura.md)。 |
| [BreakBlock](mechanics/breakblock.md) | 破坏目标位置的方块。 |
| [BreakBlockAndGiveItem](mechanics/breakblockandgiveitem.md) | 破坏目标位置的方块，并给予物品或掉落表中的物品。 |
| [ClearExperience](mechanics/clearexperience.md) | 清空目标玩家的经验点数。 |
| [ClearExperienceLevels](mechanics/clearexperiencelevels.md) | 清空目标玩家的经验等级。 |
| [ClearTarget](mechanics/cleartarget.md) | 强制此机制的目标重置其当前目标。 |
| [GiveExperienceLevels](mechanics/giveexperiencelevels.md) | 给予目标玩家经验等级。 |
| [TakeExperienceLevels](mechanics/takeexperiencelevels.md) | 扣除目标玩家的经验等级。 |
| [CloseInventory](mechanics/closeinventory.md) | 关闭目标玩家的物品栏界面。 |
| [Command](mechanics/command.md) | 为每个目标执行一条命令。 |
| [Consume](mechanics/consume.md) | 对每个命中的目标造成伤害，并恢复生命值。 |
| [ConsumeSlot](mechanics/consumeslot.md) | 移除玩家物品栏指定槽位中的物品。 |
| [DirectionalVelocity](mechanics/directionalvelocity.md) | 沿指定向量改变目标实体的速度。 |
| [Disengage](mechanics/disengage.md) | 使施法者向后跳跃，远离目标实体。 |
| [Disguise](mechanics/disguise.md) | 更改施法者的伪装。 |
| [DisguiseModify](mechanics/disguisemodify.md) | 修改施法者已应用的伪装。 |
| [DisguiseTarget](mechanics/disguisetarget.md) | 更改目标的伪装。 |
| [Undisguise](mechanics/undisguise.md) | 移除施法者的伪装。 |
| [Dismount](mechanics/dismount.md) | 使施法者离开当前骑乘的坐骑或载具。 |
| [DisplayTransformation](mechanics/displaytransformation.md) | 设置目标展示实体的变换。 |
| [ClearThreat](mechanics/clearthreat.md) | 使生物清空其仇恨表。 |
| [CurrencyGive](mechanics/currencygive.md) | 给予玩家货币。需要 Vault 和经济插件。 |
| [CurrencyTake](mechanics/currencytake.md) | 扣除玩家的货币。需要 Vault 和经济插件。 |
| [Damage](mechanics/damage.md) | 对目标造成指定数值的伤害。 |
| [BaseDamage](mechanics/basedamage.md) | 按生物伤害属性的一定百分比对目标造成伤害。 |
| [PercentDamage](mechanics/percentdamage.md) | 按目标生命值的一定百分比对其造成伤害。 |
| [Decapitate](mechanics/decapitate.md) | 根据目标掉落一个玩家头颅物品。 |
| [Doppleganger](mechanics/doppleganger.md) | 复制目标玩家的外观。 |
| [DropItem](mechanics/dropitem.md) | 在目标位置掉落物品或掉落表中的物品。 |
| [EjectPassenger](mechanics/ejectpassenger.md) | 使骑乘施法者的所有实体离开。 |
| [Ender](mechanics/ender.md) | 产生“Ender”效果。 |
| [EnderBeam](mechanics/enderbeam.md) | 创建指向目标的 EnderCrystal 光束效果。 |
| [EnderDragonResetCrystals](mechanics/enderdragonresetcrystals.md) | 生成 EnderDragon 的水晶。 |
| [EnderDragonSetPhase](mechanics/enderdragonsetphase.md) | 设置 EnderDragon 的阶段。 |
| [EnderDragonSetRespawnPhase](mechanics/enderdragonsetrespawnphase.md) | 设置 EnderDragon 的重生阶段。 |
| [EnderDragonSpawnPortal](mechanics/enderdragonspawnportal.md) | 生成 EnderDragon 战斗的传送门。 |
| [Equip](mechanics/equip.md) | 使施法生物装备一件物品。 |
| [EquipCopy](mechanics/equipcopy.md) | 使施法者装备目标装备的副本。 |
| [Explosion](mechanics/explosion.md) | 引发爆炸。 |
| [FakeExplosion](mechanics/fakeexplosion.md) | 产生假爆炸。 |
| [Extinguish](mechanics/extinguish.md) | 清除目标实体的燃烧刻数。 |
| [FawePaste](mechanics/fawepaste.md) | 使用 FAWE（Fast Async World Edit）粘贴结构模板。 |
| [Feed](mechanics/feed.md) | 为目标玩家补充饥饿值。 |
| [Fear](mechanics/fear.md) | 施加一个使目标因恐惧而四处奔跑的光环。 |
| [FillChest](mechanics/fillchest.md) | 用物品或掉落表中的物品填充箱子。 |
| [Firework](mechanics/firework.md) | 在目标处创建烟花效果。 |
| [Flames](mechanics/flames.md) | 在目标选择器的位置创建火焰效果。 |
| [Fly](mechanics/fly.md) | 施加一个使目标玩家能够飞行的[光环](mechanics/aura.md)。 |
| [ForcePull](mechanics/forcepull.md) | 将目标传送至施法者。 |
| [Freeze](mechanics/freeze.md) | 使用细雪的冰冻效果，将目标冻结指定刻数。 |
| [Geyser](mechanics/geyser.md) | 创建水或熔岩“喷泉”。 |
| [GiveItem](mechanics/giveitem.md) | 给予目标一件物品。 |
| [GiveItemFromSlot](mechanics/giveitemfromslot.md) | 将施法者给定槽位中的物品给予目标。 |
| [GiveItemFromTarget](mechanics/giveitemfromtarget.md) | 给予施法者物品，同时播放从目标实体或目标位置拾取物品的动画。 |
| [Glow](mechanics/glow.md) | 使目标发光。 |
| [GoatRam](mechanics/goatram.md) | 使施法的山羊生物冲撞目标实体。 |
| [GoTo](mechanics/goto.md) | 向目标选择器所选的位置移动，支持实体或位置。 |
| [GuardianBeam](mechanics/guardianbeam.md) | 在原点与目标之间绘制守卫者光束。 |
| [Heal](mechanics/heal.md) | 治疗目标。 |
| [HealPercent](mechanics/healpercent.md) | 按目标最大生命值的一定百分比治疗目标。 |
| [Hide](mechanics/hide.md) | 在指定时间内，对目标玩家隐藏施法者。 |
| [Hit](mechanics/hit.md) | 模拟生物的一次物理攻击。 |
| [Hologram](mechanics/hologram.md) | 在目标位置生成全息显示。 |
| [Ignite](mechanics/ignite.md) | 点燃目标。 |
| [ItemSpray](mechanics/itemspray.md) | 在目标位置产生临时物品爆散效果。 |
| [JSONMessage](mechanics/jsonmessage.md) | 向目标玩家发送 JSON 格式的消息。 |
| [Jump](mechanics/jump.md) | 使施法者跳跃。 |
| [Leap](mechanics/leap.md) | 使施法者向目标跳跃。 |
| [Lightning](mechanics/lightning.md) | 在目标处落雷。 |
| [FakeLightning](mechanics/fakelightning.md) | 在目标处产生假闪电。 |
| [Log](mechanics/log.md) | 向控制台记录一条消息。 |
| [Look](mechanics/look.md) | 使施法者看向目标。 |
| [Lunge](mechanics/lunge.md) | 使施法者向前冲向目标。 |
| [MatchRotation](mechanics/matchrotation.md) | 将施法者的偏航角和俯仰角设为与目标相同的值。 |
| [Message](mechanics/message.md) | 向目标玩家发送消息。 |
| [ModifyDamage](mechanics/modifydamage.md) | 修改触发此技能的伤害事件。 |
| [ModifyGlobalScore](mechanics/modifyglobalscore.md) | 修改虚拟玩家 __GLOBAL__ 的记分板数值。 |
| [ModifyTargetScore](mechanics/modifytargetscore.md) | 修改目标的记分板数值。 |
| [ModifyMobScore](mechanics/modifymobscore.md) | 修改施法生物的记分板数值。 |
| [ModifyScore](mechanics/modifyscore.md) | 修改虚拟玩家的分数。 |
| [Mount](mechanics/mount.md) | 为施法者召唤生物，并骑乘该生物。 |
| [MountMe](mechanics/mountme.md) | 强制目标实体骑乘施法者。 |
| [MountTarget](mechanics/mounttarget.md) | 骑乘目标。 |
| [MovePin](mechanics/movepin.md) | 将给定定位点移至目标位置。 |
| [OpenCustomMenu](mechanics/opencustommenu.md) | 打开[自定义菜单] |
| [OpenTrades](mechanics/opentrades.md) | 为目标玩家打开施法村民的交易界面。 |
| [Oxygen](mechanics/oxygen.md) | 为目标玩家补充氧气。 |
| [Particle](mechanics/particle.md) | 在目标周围创建粒子效果。 |
| [ParticleBox](mechanics/particlebox.md) | 在目标周围绘制粒子方框。 |
| [ParticleEquation](mechanics/particleequation.md) | 根据方程生成粒子。 |
| [ParticleLine](mechanics/particleline.md) | 绘制一条通向目标的粒子线。 |
| [ParticleLineHelix](mechanics/particlelinehelix.md) | 绘制由线条组成的螺旋效果。 |
| [ParticleLineRing](mechanics/particlelinering.md) | 绘制由线条连接的粒子圆环。 |
| [ParticleOrbital](mechanics/particleorbital.md) | 在目标周围绘制环绕运行的粒子效果。 |
| [ParticleRing](mechanics/particlering.md) | 在目标周围绘制粒子圆环。 |
| [ParticleSphere](mechanics/particlesphere.md) | 在目标周围绘制粒子球体。 |
| [ParticleTornado](mechanics/particletornado.md) | 在目标处绘制持续存在的粒子“龙卷风”。 |
| [Atom](mechanics/atom.md) | 创建原子形状的粒子。 |
| [PickUpItem](mechanics/pickupitem.md) | 拾取目标物品。 |
| [PlayAnimation](mechanics/playanimation.md) | 强制实体播放动画。 |
| [PlayBlockBreakSound](mechanics/playblockbreaksound.md) | 播放方块破坏声。 |
| [PlayBlockFallSound](mechanics/playblockfallsound.md) | 播放方块下落声。 |
| [PlayBlockHitSound](mechanics/playblockhitsound.md) | 播放方块被击中的声音。 |
| [PlayBlockPlaceSound](mechanics/playblockplacesound.md) | 播放方块放置声。 |
| [PlayBlockStepSound](mechanics/playblockstepsound.md) | 播放踩踏方块的声音。 |
| [PoseArmorStand](mechanics/posearmorstand.md) | 更改目标 ArmorStand 的姿势。 |
| [Potion](mechanics/potion.md) | 对目标施加药水效果。 |
| [PotionClear](mechanics/potionclear.md) | 移除目标实体的所有药水效果。 |
| [Prison](mechanics/prison.md) | 将目标囚禁在方块中。 |
| [PrintParentTree](mechanics/printparenttree.md) | 输出执行此机制的元技能及其 SkillTree 的调试信息。 |
| [Propel](mechanics/propel.md) | 推动施法者朝目标移动。 |
| [Pull](mechanics/pull.md) | 将目标拉向生物。 |
| [PushBlock](mechanics/pushblock.md) | 沿给定方向推动目标位置的方块。 |
| [PushButton](mechanics/pushbutton.md) | 按下目标位置的按钮。 |
| [RayTrace](mechanics/raytrace.md) | 向目标进行直线追踪。 |
| [RayTraceTo](mechanics/raytraceto.md) | 使用指向目标位置的射线检测结果执行技能。 |
| [Rally](mechanics/rally.md) | 使附近的其他生物攻击目标。 |
| [RandomMessage](mechanics/randommessage.md) | 向目标玩家发送随机消息。 |
| [Recoil](mechanics/recoil.md) | 使目标的屏幕抖动，以模拟后坐力。 |
| [Remount](mechanics/remount.md) | 如果施法者生成时骑乘的生物仍然存活，则重新骑乘该生物。 |
| [Remove](mechanics/remove.md) | 移除目标生物。 |
| [RemoveHeldItem](mechanics/removehelditem.md) | 移除目标玩家手持物品中的一部分。 |
| [RemoveOwner](mechanics/removeowner.md) | 移除目标生物的所有者。 |
| [ResetAI](mechanics/resetai.md) | 尝试将施法生物的 AI 重置为其基础类型的默认 AI。 |
| [RotateTowards](mechanics/rotatetowards.md) | 使施法者转向目标位置。 |
| [RunAIGoalSelector](mechanics/runaigoalselector.md) | 更改施法者的 [AIGoalSelectors](../mobs/custom-ai.md#ai-goal-selectors)。 |
| [RunAITargetSelector](mechanics/runaitargetselector.md) | 更改施法者的 [AITargetSelectors](../mobs/custom-ai.md#ai-target-selectors)。 |
| [Saddle](mechanics/saddle.md) | 为目标实体装备或移除鞍。 |
| [SendActionMessage](mechanics/sendactionmessage.md) | 向目标玩家发送快捷栏上方消息。 |
| [SendResourcePack](mechanics/sendresourcepack.md) | 向目标玩家发送资源包。 |
| [SendTitle](mechanics/sendtitle.md) | 向目标玩家发送标题/副标题消息。 |
| [SendToast](mechanics/sendtoast.md) | 向目标玩家发送成就弹窗提示。 |
| [SetAI](mechanics/setai.md) | 禁用或启用目标生物的 AI。 |
| [SetBlockOpen](mechanics/setblockopen.md) | 设置目标方块的打开状态。 |
| [SetBlockType](mechanics/setblocktype.md) | 更改目标位置的方块类型。 |
| [SetChunkForceLoaded](mechanics/setchunkforceloaded.md) | 设置某个位置所在区块的强制加载状态。 |
| [SetCollidable](mechanics/setcollidable.md) | 设置目标是否具有可碰撞的碰撞箱。 |
| [SetCustomMenuButton](mechanics/setcustommenubutton.md) | 将已打开的[自定义菜单]中的指定槽位设置为指定按钮。 |
| [SetDragonPodium](mechanics/setdragonpodium.md) | 将龙的基座位置设置为目标位置。 |
| [SetGameMode](mechanics/setgamemode.md) | 设置目标玩家的游戏模式。 |
| [SetGliding](mechanics/setgliding.md) | 如果目标拥有鞘翅，则使其滑翔。 |
| [SetGlobalScore](mechanics/setglobalscore.md) | 设置虚拟玩家 __GLOBAL__ 的记分板数值。 |
| [SetGravity](mechanics/setgravity.md) | 设置目标实体是否受重力影响。 |
| [SetHealth](mechanics/sethealth.md) | 设置目标实体的生命值。 |
| [SetInteractionSize](mechanics/setinteractionsize.md) | 设置目标 `INTERACTION` 实体的大小。 |
| [SetItemGroupCooldown](mechanics/setitemgroupcooldown.md) | 为目标玩家设置物品组冷却。 |
| [setDisplayEntityItem](mechanics/setdisplayentityitem.md) | 设置 `ITEM_DISPLAY` 实体的物品组件。 |
| [SetLeashHolder](mechanics/setleashholder.md) | 更改生物拴绳的持有者。 |
| [SetLevel](mechanics/setlevel.md) | 更改施法生物的等级。 |
| [SetMaterialCooldown](mechanics/setmaterialcooldown.md) | 为末影珍珠、紫颂果等可使用的材质设置冷却。 |
| [SetMaxHealth](mechanics/setmaxhealth.md) | 设置目标实体的最大生命值。 |
| [SetMobColor](mechanics/setmobcolor.md) | 如果目标是可以改变颜色的生物，则更改其颜色。 |
| [SetMobScore](mechanics/setmobscore.md) | 设置施法生物的记分板数值。 |
| [SetName](mechanics/setname.md) | 更改施法者实体的名称。 |
| [setRaiderCanJoinRaid](mechanics/setraidercanjoinraid.md) | 设置目标袭击者实体是否可以加入袭击。 |
| [SetRaiderPatrolBlock](mechanics/setraiderpatrolblock.md) | 设置目标袭击者巡逻某个位置。 |
| [SetRaiderPatrolLeader](mechanics/setraiderpatrolleader.md) | 设置袭击者巡逻队长。 |
| [SetFaction](mechanics/setfaction.md) | 更改目标实体的阵营。 |
| [SetFlying](mechanics/setflying.md) | 设置目标玩家是否正在飞行。 |
| [SetNoDamageTicks](mechanics/setnodamageticks.md) | 设置目标的 nodamageticks。 |
| [SetOwner](mechanics/setowner.md) | 使目标成为施法生物的所有者。 |
| [SetParent](mechanics/setparent.md) | 使目标成为施法生物的父实体。 |
| [SetPathfindingMalus](mechanics/setpathfindingmalus.md) | 设置生物对给定地形类型的寻路惩罚值。 |
| [SetPitch](mechanics/setpitch.md) | 设置目标实体头部的俯仰角。 |
| [SetPose](mechanics/setpose.md) | 设置实体的姿势。 |
| [SetRotation](mechanics/setrotation.md) | 设置目标的旋转角度。 |
| [SetTarget](mechanics/settarget.md) | 设置施法者的目标。 |
| [SetTargetScore](mechanics/settargetscore.md) | 设置目标的分数。 |
| [SetTextDisplay](mechanics/settextdisplay.md) | 设置目标文本展示实体的文本组件。 |
| [SetTongueTarget](mechanics/settonguetarget.md) | 将青蛙施法者的舌头目标设置为目标实体。 |
| [SetScore](mechanics/setscore.md) | 设置虚拟玩家的记分板数值。 |
| [SetSpeed](mechanics/setspeed.md) | 设置目标实体的速度属性。 |
| [SetStance](mechanics/setstance.md) | 设置目标生物的姿态。 |
| [Shield](mechanics/shield.md) | 为目标实体施加伤害吸收护盾。 |
| [ShieldBreak](mechanics/shieldbreak.md) | 强制玩家放下盾牌，并使其进入冷却。 |
| [ShieldPercent](mechanics/shieldpercent.md) | 按目标实体最大生命值的一定百分比，为其施加伤害吸收护盾。 |
| [ShootFireball](mechanics/shootfireball.md) | 向目标发射火球。 |
| [ShootPotion](mechanics/shootpotion.md) | 向目标投掷药水。 |
| [ShootSkull](mechanics/shootskull.md) | 向目标发射凋灵之首。 |
| [ShootShulkerBullet](mechanics/shootshulkerbullet.md) | 向目标实体发射潜影弹。 |
| [ShowEntity](mechanics/showentity.md) | 向目标玩家显示原本隐藏的施法者。 |
| [Signal](mechanics/signal.md) | 向生物发送信号。 |
| [Skybox](mechanics/skybox.md) | 改变目标玩家的天空盒。 |
| [Smoke](mechanics/smoke.md) | 产生一团烟雾。 |
| [SmokeSwirl](mechanics/smokeswirl.md) | 产生持续存在的螺旋烟雾。 |
| [Sound](mechanics/sound.md) | 播放来自 Minecraft 原版或资源包的音效。 |
| [StealItem](mechanics/stealitem.md) | 从目标处偷取一件物品，并放到生物手中。 |
| [StopSound](mechanics/stopsound.md) | 停止播放某个音效。 |
| [Speak](mechanics/speak.md) | 让生物在聊天中说话，并可设置对话气泡。 |
| [Spin](mechanics/spin.md) | 使目标旋转。 |
| [Spring](mechanics/spring.md) | 在目标处创建临时液体泉源。 |
| [Stun](mechanics/stun.md) | 施加使目标实体眩晕的[光环](mechanics/aura.md)。 |
| [StopUsingItem](mechanics/stopusingitem.md) | 阻止目标实体使用物品。 |
| [Suicide](mechanics/suicide.md) | 使施法者死亡。 |
| [Summon](mechanics/summon.md) | 在目标处召唤其他生物。 |
| [SummonAreaEffectCloud](mechanics/summonareaeffectcloud.md) | 在目标处召唤粒子云。 |
| [SummonFallingBlock](mechanics/summonfallingblock.md) | 召唤下落的方块。 |
| [SummonPassenger](mechanics/summonpassenger.md) | 召唤一个骑乘目标的生物。 |
| [Swap](mechanics/swap.md) | 与目标交换位置。 |
| [SwingOffhand](mechanics/swingoffhand.md) | 使施法玩家挥动副手。 |
| [AddTag](mechanics/addtag.md) | 为目标添加记分板标签。 |
| [RemoveTag](mechanics/removetag.md) | 移除目标的记分板标签。 |
| [TakeItem](mechanics/takeitem.md) | 移除目标玩家物品栏中的物品。 |
| [Taunt](mechanics/taunt.md) | 修改目标实体对施法者的仇恨值。 |
| [Teleport](mechanics/teleport.md) | 传送到目标处。 |
| [TeleportY](mechanics/teleporty.md) | 竖直传送施法者。 |
| [TeleportIn](mechanics/teleportin.md) | 相对于施法者的偏航角传送目标。 |
| [TeleportTo](mechanics/teleportto.md) | 将目标传送到指定位置。 |
| [Time](mechanics/time.md) | 更改时间。 |
| [Threat](mechanics/threat.md) | 修改生物对目标的仇恨值。 |
| [Throw](mechanics/throw.md) | 抛出目标实体。 |
| [ThunderLevel](mechanics/thunderlevel.md) | 为每个玩家单独创建客户端的无雨雷暴效果。 |
| [ToggleLever](mechanics/togglelever.md) | 切换目标位置拉杆的状态。 |
| [TogglePiston](mechanics/togglepiston.md) | 切换目标位置活塞的状态。 |
| [ToggleSitting](mechanics/togglesitting.md) | 切换猫、狗、狐狸和鹦鹉的坐下状态。 |
| [TotemOfUndying](mechanics/totemofundying.md) | 播放玩家复活的效果。 |
| [TrackLocation](mechanics/tracklocation.md) | 将生物追踪的位置设为目标位置。 |
| [UndoPaste](mechanics/undopaste.md) | 撤销之前的一次粘贴操作。 |
| [Velocity](mechanics/velocity.md) | 修改目标实体的速度。 |
| [Weather](mechanics/weather.md) | 修改目标世界的天气。 |
| [WolfSit](mechanics/wolfsit.md) | 强制目标狼坐下。 |
| [WorldEditReplace](mechanics/worldeditreplace.md) | 使用 WorldEdit 替换区域中的方块。 |

## 元技能机制 {#meta-mechanics}

这些技能机制具有特殊的高级功能，大多数用于调用其他技能。如果你指定一个目标，则由这些目标调用的所有其他技能都将“继承”该目标（如果适用）。

| 技能机制 | 说明 |
| --- | --- |
| **[Skill](mechanics/skill.md)** | 执行一个元技能，是技能配置的基础。 |
| **[VariableSkill](mechanics/variableskill.md)** | 执行一个元技能，支持占位符。 |
| [Aura](mechanics/aura.md) | 对目标实体施加光环，可在 onStart/onTick/onEnd 等阶段执行技能，所有这些技能均从该目标发起。 |
| [Beam](mechanics/beam.md) | 在施法者与目标之间创建由指定材质组成的光束。 |
| [CancelEvent](mechanics/cancelevent.md) | 取消触发当前技能树的事件。仅适用于某些触发器。 |
| [CancelSkill](mechanics/cancelskill.md) | 触发时取消元技能的执行。 |
| [Cast](mechanics/cast.md) | 施加一个[光环](mechanics/aura.md)，通过各种高级选项“施放”元技能。 |
| [Chain](mechanics/chain.md) | 在彼此靠近的多个目标之间连锁执行技能。 |
| [ChainMissile](mechanics/chainmissile.md) | 在实体之间连锁传递的追踪弹。**仅 Premium 版**机制！ |
| [Delay](mechanics/delay.md) | 将当前技能列表的执行延迟指定刻数。 |
| [DetermineCondition](mechanics/determinecondition.md) | 确定通过 [MetaskillCondition](conditions/metaskillcondition.md) 条件作为条件使用的元技能的结果。 |
| [EndProjectile](mechanics/endprojectile.md) | 终止弹射物。仅可在弹射物机制中使用。 |
| [ForEach](mechanics/foreach.md) | 对此机制的每个目标分别执行一次元技能。 |
| [ForEachValue](mechanics/foreachvalue.md) | 对指定值中的每个条目或键值对分别执行一次元技能。 |
| [ForEachPin](mechanics/foreachpin.md) | 对多点定位标记中的每个定位点分别执行一次元技能。 |
| [GlobalCooldown](mechanics/globalcooldown.md) | 设置施法者的全局冷却计时器。 |
| [Missile](mechanics/missile.md) | 向目标发射追踪弹射物。 |
| [ModifyProjectile](mechanics/modifyprojectile.md) | 修改弹射物、追踪弹或环绕弹射物。 |
| [OnAttack](mechanics/onattack.md) | 为目标施加一个在其攻击时触发技能的[光环](mechanics/aura.md)。 |
| [OnDamaged](mechanics/ondamaged.md) | 为目标施加一个在其受伤时触发技能的[光环](mechanics/aura.md)。 |
| [OnShoot](mechanics/onshoot.md) | 为目标施加一个在其用弓射击时触发技能的[光环](mechanics/aura.md)。 |
| [OnBlockBreak](mechanics/onblockbreak.md) | 为目标施加一个在其破坏方块时触发技能的[光环](mechanics/aura.md)。 |
| [OnBlockPlace](mechanics/onblockplace.md) | 为目标施加一个在其放置方块时触发技能的[光环](mechanics/aura.md)。 |
| [OnChat](mechanics/onchat.md) | 为目标施加一个在其聊天时触发技能的[光环](mechanics/aura.md)。 |
| [OnSwing](mechanics/onswing.md) | 为目标施加一个在其挥动手臂或左键点击时触发技能的[光环](mechanics/aura.md)。 |
| [OnInteract](mechanics/oninteract.md) | 为目标施加一个[光环](mechanics/aura.md)，在其手持方块或看着有轮廓的方块（非 AIR）进行交互或右键点击时触发技能。 |
| [OnJump](mechanics/onjump.md) | 为目标施加一个在其跳跃时触发技能的[光环](mechanics/aura.md)，此机制仅适用于 PAPER。 |
| [OnDeath](mechanics/ondeath.md) | 为目标施加一个在其死亡时触发技能的[光环](mechanics/aura.md)。 |
| [Orbital](mechanics/orbital.md) | 施加一个使弹射物绕目标运行的[光环](mechanics/aura.md)。 |
| [FollowPath](mechanics/followpath.md) | 施加一个使生物沿路径移动的[光环](mechanics/aura.md)。 |
| [FormLine](mechanics/formline.md) | 施加一个使生物沿*直线*路径移动的[光环](mechanics/aura.md)。 |
| [Polygon](mechanics/polygon.md) | 创建可高度自定义的多边形图案，能够执行元技能。 |
| [Projectile](mechanics/projectile.md) | 向目标发射可高度自定义的弹射物。 |
| [ProjectileVelocity](mechanics/projectilevelocity.md) | 修改发起调用的弹射物或追踪弹的速度。 |
| [RandomSkill](mechanics/randomskill.md) | 从列表中随机执行一个技能。 |
| [SetSkillCooldown](mechanics/setskillcooldown.md) | 将给定元技能的冷却设为给定值。 |
| [SetProjectileDirection](mechanics/setprojectiledirection.md) | 将发起调用的弹射物的移动方向设为朝向给定目标。 |
| [SetProjectileBulletModel](mechanics/setprojectilebulletmodel.md) | 设置弹射物的模型，仅适用于 DISPLAY 弹体。 |
| [Shoot](mechanics/shoot.md) | 向目标发射物品弹射物，类似于箭、鸡蛋和雪球。 |
| [Slash](mechanics/slash.md) | 创建可高度自定义的斩击图案，能够执行元技能。 |
| [SudoSkill](mechanics/sudoskill.md) | 使目标执行技能。 |
| [Switch](mechanics/switch.md) | 用作 switch/case。 |
| [StatAura](mechanics/stataura.md) | 对目标施加一个为其提供指定属性的光环。 |
| [Totem](mechanics/totem.md) | 在某个位置创建可以执行其他技能的静止“图腾”。 |
| [Terminable](mechanics/terminable.md) | 创建一个[光环](mechanics/aura.md)，在满足某些条件时取消其 onStart 元技能的执行。 |
| [Volley](mechanics/volley.md) | 使用各种选项，向目标齐射一轮物品弹射物。 |
| [VariableAdd](mechanics/variableadd.md) | 为数值变量增加指定数值。 |
| [VariableMath](mechanics/variablemath.md) | 对数值变量进行数学运算。 |
| [SetVariable](mechanics/setvariable.md) | 设置变量的值。 |
| [SetVariableLocation](mechanics/setvariablelocation.md) | 将变量设置为目标位置。 |
| [VariableUnset](mechanics/variableunset.md) | 取消设置变量。 |
| [VariableSubtract](mechanics/variablesubtract.md) | 从数值变量中减去指定数值。 |
| [VariableMove](mechanics/variablemove.md) | 在不同名称或注册表之间移动已创建的变量。 |
| [Wait](mechanics/wait.md) | 暂停元技能，直到满足一组条件。 |
| [CinematicCamera](mechanics/cinematiccamera.md) | 为目标玩家播放过场动画镜头路径。 |
| [CinematicCancel](mechanics/cinematiccancel.md) | 取消目标玩家正在播放的过场动画。 |
| [CloseDialog](mechanics/closedialog.md) | 关闭目标玩家打开的任何对话框。 |
| [OnKeyPress](mechanics/onkeypress.md) | 施加一个在玩家按下按键时触发技能的光环。 |
| [OnKeyRelease](mechanics/onkeyrelease.md) | 施加一个在玩家松开按键时触发技能的光环。 |

# 通用属性 {#universal-attributes}

以下属性适用于所有技能机制。

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| cooldown | cd | 单位为秒，允许小数。 | 0 |
| delay |  | 将机制的执行延迟指定刻数。 | 0 |
| repeat |  | 机制的重复次数。如果 repeatInterval 设为 `0`，此值表示执行次数，而不是重复次数。 | 0 |
| repeatInterval | repeatI | 两次重复执行之间必须经过的刻数。 | 0 |
| targetInterval | targetI | 两次目标选择之间必须经过的刻数。 | 0 |
| origin |  | *[PREMIUM]** 将原点改为所提供目标选择器选中的目标。解析出多个目标时无效。`origin=@Forward{f=10}` origin 属性的目标选择器会独立于机制的目标选择器解析，因此使用 `origin=@targetedlocation` 之类的值时，返回的是元技能继承的目标，而不是机制明确指定的目标。 |  |
| power |  | [威力](../mobs/power.md)倍率 | 1 |
| fromorigin | fo, sourceisorigin, castfromorigin | 是否从原点施放机制。这仅适用于少数机制，通常也会在它们的属性列表中列出。 | false |
| targetisorigin |  | 是否将机制的目标设为原点。 | false |
| targetcreative |  | 是否以创造模式玩家为目标。 | false |
| splitPower | powersplit, powersplitbetweentargets | 是否在目标之间分摊威力。 | false |
| faulty |  | 机制是否使用旧版向量公式。 | true |
| chance |  | 机制的执行概率。例如，0.1 表示 10% 的概率。 | 1 |
| forcesync | sync | 是否强制机制与 Minecraft 主线程同步运行。这*通常*会降低性能，虽然一般难以察觉，但**某些机制必须将此项设为 true**，*例如 [cancelevent](mechanics/cancelevent.md) 机制：如果机制执行过晚、事件已经发生，就无法再取消该事件*。 | false |

# 示例 {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - message{m="This message will only be shown once every 5 seconds!";cooldown=5} @trigger ~onInteract
  - message{m="This one 5 times in a row over 2 seconds!";repeat=4;repeatInterval=10} @trigger ~onInteract
```
