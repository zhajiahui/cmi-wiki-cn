---
title: 常见问题
source_url: https://wiki.mythiccraft.io/mythicmobs/FAQ
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 常见问题 {#f-a-q}

## MythicMobs 付费版包含哪些内容？ {#whats-included-in-mythicmobs-premium}

[MythicMobs Premium](https://mythiccraft.io/index.php?resources/mythicmobs.1/product-purchases) 提供许多 Premium 专属权益，包括：

- Discord 中的专属 Premium 身份组。
- 使用高级版支持频道和工单系统。
- 更早获取最新版本。
- 获取开发构建版本。
- 在大多数技能、掉落数量和选项中使用数学表达式和占位符。
- 在任何投射物技能中使用命中条件。
- 使用自定义伤害类型和伤害修正。
- 使用多种支持条件的自定义 AI 目标和目标选择器。

今后还会继续添加更多 Premium 专属功能。

你可以[点击这里](https://mythiccraft.io/index.php?resources/mythicmobs.1/product-purchases)将账号升级为 Premium。

对于希望多捐助一些，或拥有大型服务器的用户，Premium+ 套餐提供了额外权益：

- Discord 中的专属 Premium+ 身份组。
- 优先处理支持工单。
- 许可证可用于你拥有的多台服务器。

## 让被动生物攻击目标时，生物消失了！ {#my-mob-disappears-when-i-try-to-make-a-passive-mob-attack-something}

被动生物类型（绵羊、猪、牛等）无法攻击任何实体，因为其基础生物本身没有造成伤害的能力。在较旧的 Minecraft 版本中，这种行为可能导致服务器崩溃；在较新的版本中，生物则会直接消失。最好的解决方式是使用敌对生物类型（例如僵尸），再通过 LibsDisguises 将它伪装成被动生物。

## 如何为生物设置自定义头颅？ {#how-can-i-get-custom-heads-on-my-mob}

将头颅拿在手中，使用 `mm i import` 命令将其导入为 MythicItem。然后像设置其他头盔一样设置这个物品。

## 如何制作施放法术而非近战攻击的“施法者”生物？ {#how-do-i-make-caster-mobs-that-cast-spells-instead-of-using-melee-attacks}

最好的方法是使用通过 onTimer 施放的投射物。更详细的示例见[投射物](skills/mechanics/projectile.md) Wiki 页面。

## 如何在玩家伪装中使用颜色代码？ {#how-do-i-use-color-codes-in-player-disguises}

请使用 Disguise: 选项，并用单引号（‘ ‘）将颜色代码括起来。

## 粒子散布得太开了！ {#my-particles-are-too-spread-out}

将粒子技能的 hS 和 vS 设为 0.1。火焰粒子本身分布较广，因为它们实际上是烈焰人和熔炉使用的粒子，播放时会分散开来。

要让粒子更集中，需要同时缩小水平和垂直方向的半径。将半径设得很小，就能让粒子呈现出一条笔直的火焰线。

## 为什么生物生命值无法设为超过 2000？ {#why-cant-i-set-a-mobs-health-above-2000}

这是 Spigot 的问题。打开 spigot.yml 配置文件，提高 max-health 属性的值即可。

## 如何创建拥有多个技能、但不会同时使用全部技能的复杂生物？同时使用技能太强了！ {#how-do-i-create-a-complex-multi-skilled-mob-that-wont-use-all-of-its-skills-at-the-same-time-its-too-op}

有很多方法可以错开生物的技能，让施放更难预测、间隔更分散，也更随机。

- 可以使用 RandomSkill 技能，按一定间隔施放随机技能。
- 将 "GCD"（全局冷却）技能与 "OffGCD" 条件配合使用。
- 降低技能的触发概率，并缩短冷却时间。
- 通过 setstance 机制和 stance 条件使用姿态。

## 如何使用自己的自定义音效？（答案由 MythicMobs 论坛的 SeanArmor 提供） {#i-want-to-use-my-own-custom-sound-effect-how-do-i-do-this-answer-provided-by-seanarmor-on-the-mythicmobs-forums}

要使用自定义声音，必须将它们添加到服务器所用的资源包中。没有使用包含这些自定义声音的资源包的玩家，将无法听见它们。

前往 [www.wowhead.com/sounds](http://www.wowhead.com/sounds) 或其他声音网站，下载声音文件，再使用 [audio.online-convert.com/convert-to-ogg](http://audio.online-convert.com/convert-to-ogg) 转换文件。

也可以使用 SeanArmor 的方法（不确定是否有效）：将文件的扩展名改为 .ogg。

然后将新的 .ogg 声音文件放入资源包文件夹，并使用 effect:sound{something.something.yoursoundname}。

其中 something.something 是文件的文件夹路径。如果 .ogg 文件直接放在资源包文件夹中，在技能中只需填写不带 .ogg 扩展名的名称。如果它位于其他文件夹中，例如 (FolderA/FolderB/yoursound.ogg)，则应填写 effect:sound{FolderA.FolderB.yoursound}。
