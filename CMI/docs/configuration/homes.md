---
title: 家（Homes.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/Homes.yml
---

# 家（Homes.yml）

文件：`plugins/CMI/Settings/Homes.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `Homes`

### `Homes.Confirmation`

启用后，覆盖同名家的位置前，要求玩家点击游戏内聊天消息确认<br>
也可直接执行 /cmi sethome \[homeName\] -override 确认

### `Homes.MaxGuiSlots`

/sethome \[homeName\] \[slotNumber\] 创建家时，允许指定的最大槽位编号

### `Homes.Gui.Use`

已保存多个家时，执行 /cmi home 打开界面

### `Homes.Gui.Options.Expanded`

启用后，家的界面区域从 10 个槽位扩展为 28 个

### `Homes.Gui.Options.Border`

留空则使用全局填充材质

### `Homes.Gui.Options.Infill`

界面未展开时，家的图标周围使用的材质

### `Homes.Gui.Options.InfoButton.Use`

额外按钮，可用于点击后显示补充信息

### `Homes.Groups`

家数量上限组，权限为 cmi.command.sethome.\[groupname\]<br>
找不到玩家所属上限组时，数量设为 1<br>
使用 cmi.command.sethome.unlimited 获得不限数量的家<br>
也可直接使用数字权限 cmi.command.sethome.\[number\]，指定家的数量上限

### `Homes.Limits.BlockExtraHomes`

超过数量上限时，禁止使用家<br>
已拥有的家超过上限时，不允许传送回家

### `Homes.Limits.NotifyOnLogin`

登录时提醒玩家已超过上限

### `Homes.BedInteraction`

需要 cmi.bedhome 权限<br>
设为 true，与床交互时创建普通的家位置<br>
设为 false，设置原版床重生位置

### `Homes.onlyShiftBed`

设为 true，只有潜行点击床才设置家

### `Homes.RemoveBedLocationOnBedBreak`

点击床创建家时，移除原版床重生位置

### `Homes.CheckBlockBreak`

启用后，创建家之前检查玩家是否能在该区域破坏方块<br>
可用于阻止在受保护区域设置家<br>
可通过 cmi.command.sethome.bypass 绕过

### `Homes.DefaultName`

默认家的名称，默认为 "Home"

### `Homes.DefaultBedName`

床位置对应的家名称，默认为 "Home"<br>
可用不同名称，区分通过床交互设置的家与通过命令创建的家

### `Homes.ValidNameRegex`

家名称允许使用的字符

### `Homes.WorldLimits.Use`

启用后，按以下条件限制创建家<br>
可通过 cmi.command.sethome.bypasslimit 绕过

### `Homes.WorldLimits.Groups.Example1.Amount`

此世界组中允许的家数量。设为 0，基本等于禁止在这些世界创建家；小于 0，则完全忽略该世界组

### `Homes.WorldLimits.Groups.Example1.Worlds`

应用限制的世界列表，可填写多个世界组成一组
