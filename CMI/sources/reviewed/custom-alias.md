CMI 可以创建自定义命令，用来执行一条或多条预设命令。

[![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-24-00-1.gif)](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_15-24-00-1.gif)

自定义别名支持[特殊指令](https://www.zrips.net/cmi/commands/specialized/)。

创建只执行一条命令的简单别名，使用 **/cmi aliaseditor new [alias]-[original command]**。例如，要将 **/h** 设为 **/cmi heal** 的别名，执行 **/cmi aliaseditor new h-cmi heal [playerName] $1-**。其中，**[playerName]** 会替换为执行别名命令的玩家名称，**$1-** 表示将别名后附加的所有参数放在这个位置。例如，**/h zrips 10** 实际会执行 **/cmi heal zrips 10**。

可以使用内置编辑器添加多条命令。执行 **/cmi aliaseditor**，向下找到要修改的别名，点击后就会显示命令列表。你可以编辑、删除、调整顺序或添加命令。

包含 2 条命令的别名示例：  
**– asConsole! moneycost:20#?! cmi heal [playerName] -s  
–**asConsole**! msg [playerName] !&2You just been healed by God’s of minecraft!**  
这会从玩家余额中扣除 20 金钱。余额不足时，玩家会收到提示，这是 **?** 符号的作用，详见特殊指令说明。由于条件变量中使用了 **#**，余额不足时也不会执行第二条命令。条件变量始终以 **!** 结尾，**? #** 是可选符号。余额足够时，会从控制台执行 **/cmi heal Zrips -s**，静默完成命令，再执行第二条命令，向目标玩家发送消息。

命令之间带有延迟的别名：  
**–**asConsole**! cmi launch [playerName]  
– delay! 3  
–**asConsole**! cmi launch [playerName]**  
玩家会朝视线方向被发射到空中，3 秒后再次被发射。

还可以使用 **?** 变量。它应放在别名本身中，主要用于在玩家输入错误的子命令时显示帮助。例如，设置 **/cmi aliaseditot new tipi sub-asConsole! cmi msg [playerName] apple** 和 **/cmi aliaseditot new tipi ?-asConsole! cmi msg [playerName] carrot** 后，玩家执行 **/tipi** 会收到 **carrot**，执行 **/tipi bla** 也会收到 **carrot**，而执行 **/tipi sub** 会收到 **apple**。

## 自定义 Tab 补全

可以完全禁用 Tab 补全，也可以自定义补全内容。默认情况下，插件会尝试根据自定义别名中的第一条命令提供补全建议，但结果可能不符合需要。此时可以指定固定词语，或使用下方列出的一些动态变量，定义自己的补全内容。

点击 customAlias 编辑器中灰色的 **CustomTab** 文字，即可修改自定义 Tab 补全。

Tab 补全可以分支，也就是说，选了不同的参数，接下来得到的补全建议也会完全不同。以下面的简单示例为例：

```text
- first subFirst
- second subSecond
```

最初会提示“first second”；选择“second”后，只会提示“subSecond”。  
如需提供多个选项，用逗号“,”分隔，例如：

```text
- first subFirst,subSecond,[playername]
```

这样除了可以选择“subFirst”和“sunSecond”，还会将在线玩家名称加入补全建议。

默认情况下，Tab 补全会覆盖这条命令可能已有的补全内容。若想保留原有补全并添加自己的内容，需要在别名编辑器中启用 **AddTab** 按钮，将两者合并。

## 动态 Tab 补全变量

- **[allPlayername]** – 所有玩家，包括隐身玩家。
- **[playername]** – 所有玩家，不包括隐身玩家。
- **[allIGNPlayername]** – 所有玩家，不包括隐身玩家，且只使用真实玩家名称。
- **[mutedplayername]** – 所有被禁言的在线玩家。
- **[damageCause]** – 各种伤害原因。
- **[bannedplayername]** – 被封禁的玩家名称。
- **[gamemode]** – 游戏模式。
- **[worlds]** – 世界。
- **[itemname]** – 材质。
- **[EntityType]** – 实体类型。
- **[cleanEntityType]** – 不含 _ 的实体类型。
- **[kit]** – 有权使用的礼包名称。
- **[kitnames]** – 有权使用的礼包配置名称。
- **[kitp]** – 有权预览的礼包。
- **[chatroom]** – 聊天室。
- **[biome]** – 生物群系。
- **[treeType]** – 树木类型。
- **[maxplayers]** – 服务器最大玩家数量上限。
- **[potioneffect]** – 药水效果。
- **[effect]** – 粒子效果。
- **[merchants]** – 村民职业。
- **[enchant]** – 附魔名称。
- **[halfViewRange]** – 服务器最大视距的一半。
- **[doubleViewRange]** – 服务器最大视距的两倍。
- **[ViewRange]** – 服务器视距。
- **[maxenchantlevel]** – 最高附魔等级，根据前一个变量确定附魔。
- **[currentItemName]** – 主手物品名称。
- **[loreLine]** – 主手物品的物品描述行号列表。
- **[currentItemLore]** – 主手物品的物品描述列表。
- **[currentX]** – 玩家当前的 X 坐标。
- **[currentY]** – 玩家当前的 Y 坐标。
- **[currentZ]** – 玩家当前的 Z 坐标。
- **[currentWorld]** – 玩家所在世界的名称。
- **[currentPitch]** – 玩家的俯仰角。
- **[currentYaw]** – 玩家的偏航角。
- **[itemFlag]** – 物品标志值。
- **[nickName]** – 用户的显示名称。
- **[nickNames]** – 所有在线用户的昵称。
- **[homes]** – 用户的家列表。
- **[warps]** – 有权使用的传送点。
- **[allwarps]** – 所有传送点。
- **[playerwarps]** – 有权使用的传送点。
- **[rankname]** – 等级名称。
- **[statstype]** – 统计项名称。
- **[statssubtype]** – 子统计项名称，根据前一个变量确定主统计项。
- **[motd]** – 服务器的 motd。
- **[bungeeserver]** – Bungee 服务器。
- **[scheduleName]** – 计划任务名称。
- **[ctext]** – 自定义文本名称。
- **[jail]** – 监狱名称。
- **[cellId]** – 牢房 ID，根据前一个变量确定监狱。
- **[sound]** – 声音名称。
- **[placeholders]** – 占位符。
- **[warncategory]** – 警告类别。
- **[projectiletype]** – 弹射物类型。
- **[holograms]** – 全息显示名称。
- **[mobtype]** – 生物类型。
- **[signLine]** – 告示牌行文本，根据前一个变量确定行号。
- **[allportals]** – 所有传送门，包括已禁用的传送门。
- **[portals]** – 所有已启用的传送门。
- **[playeritems]** – 玩家背包中的所有物品列表。
- **[gamerule]** – 世界游戏规则列表。
- **[attachedCommand]** – 玩家主手物品上附加的命令列表。
- **[customalias]** – 自定义别名列表。
