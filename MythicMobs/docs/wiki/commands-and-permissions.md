---
title: 命令与权限
source_url: https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 命令与权限

## 命令 {#commands}

Mythic Mobs 的命令结构很简单，输入 **/mythicmobs** 即可查看。该命令会显示所有可用命令，每一级子命令也会提供相应菜单或操作说明。所有以 [] 括起的参数都是必填项，以 <> 括起的参数则为可选项。

> 可以通过[元技能](skills/metaskills.md)创建[自定义命令](skills/skill-commands.md)

## 标志 {#flags}

部分命令可以在第一个参数前添加标志，以改变命令的行为。

| 标志 | 说明 | 受影响的命令 | 示例 |
| --- | --- | --- | --- |
| -s | 静默命令不会在聊天栏中给出任何反馈 | `mm mobs spawn` `mm item give` `mm test cast` `mm test mechanic` | `/mm test cast -s [metaskill]` |
| -p | 使用此标志，在指定玩家处执行命令 | `mm mobs spawn` `mm spawners create` `mm spawners move` | `/mm m s -p <player> [mobname]` |
| -t | 在目标位置执行命令 | `mm mobs spawn` | `/mm m s -t [mobname]` |
| -n | 将生物模拟为自然生成（生成原因为 `NATURAL`，而非 `COMMAND`） | `mm mobs spawn` | `/mm m s -n [mobname]` |
| -p | 命令是否也击杀持久保存的生物 | `mm mobs killall` | `/mm m killall -p` |
| -f | 击杀所有属于指定阵营的生物 | `mm mobs kill` | `/mm m kill -f [factionname]` |
| -d | 物品栏已满时，是否将物品掉落到地面 | `mm item give` | `/mm i give -d [itemname]` |

## 通用命令 {#general-commands}

- **/mm**（别名：**/mythicmobs**）*插件的根命令，显示其他所有命令。*
- **/mm debug [level]**（别名：**/mm d [level]** *设置插件的调试等级。0 = OFF。*
- **/mm debugmode [true/false]** *启用调试模式，关闭随机生成、刷怪点和其他不利于调试的随机行为。*
- **/mm reload**（别名：**/mm r**）*重载插件。*
- **/mm save** *强制保存所有活动生物和刷怪点。*
- **/mm version** *显示 MythicMobs 版本。*

## 物品命令 {#item-commands}

- **/mm items**（别名：**/mm i**）*物品相关命令的根命令。*
- **/mm items get [item_name] <amount>** *从已配置的生物装备中获取物品并给予自己。*
- **/mm items give [player] [item_name] <amount>** *从已配置的生物装备中获取物品并给予指定玩家。*
- **/mm items give -s [player] [item_name] <amount>** *从已配置的生物装备中获取物品，静默给予指定玩家。*
- **/mm items give -d [player] [item_name] <amount>** *从已配置的生物装备中获取物品并给予指定玩家，超出背包容量的部分掉落在地上。*
- **/mm items list** * *列出所有已配置的生物装备。*
- **/mm item import <itemName> [fileName]** * *将手持物品导入 Items 文件夹。（文件名默认为 <itemName>.yml）*
- **/mm items browse** *打开 GUI，显示所有已加载的 Mythic 物品。*（仅限 Premium 版）

## 生物命令 {#mob-commands}

- **/mm mobs**（别名：**/mm m**）*生物相关命令的根命令。*
- **/mm mobs info [mob_name]** *显示 Mythic 生物的详细信息。*
- **/mm mobs list** *列出服务器已加载的生物。*
- **/mm mobs listactive** *列出当前已生成的生物及各自数量。*
- **/mm mobs kill [mob_name]** *移除所有具有指定名称的 Mythic 生物。*
- **/mm mobs kill -f [faction]** *移除所有属于指定派系的 Mythic 生物。*
- **/mm mobs killall** *移除所有活动的 Mythic 生物。*
- **/mm mobs killall -p** *移除所有持久化的 Mythic 生物。*
- **/mm mobs spawn [mob_name]:<level> <amount> <world,x,y,z,yaw,pitch>** *生成具有指定名称的生物。*
- **/mm mobs spawn -s [mob_name]:<level> <amount> <world,x,y,z,yaw,pitch>** *静默生成生物，不在控制台输出文本。*
- **/mm mobs stats** *显示服务器已加载生物的数量等实用信息。*

## 生物蛋命令 {#mob-egg-commands}

- **/mm egg**（别名：**/mm e**）*生成蛋相关命令的根命令。*
- **/mm egg get [mob_name] <amount>** *给予自己指定 Mythic 生物的生成蛋。*
- **/mm egg give [player] [mob_name] <amount>** *给予指定玩家相应 Mythic 生物的生成蛋。*

## 镜头命令 {#camera-commands}

镜头命令可以在游戏中编辑 [cinematicCamera](skills/mechanics/cinematiccamera.md) 路径。执行 **add** 会将当前位置、偏航角和俯仰角保存为路径文件中的一个关键帧，并重载该文件。路径必须已经存在于某个路径文件中，且至少包含一个关键帧；这些命令不会创建新路径或新文件。需要 **mythicmobs.command.camera** 权限。

- **/mm camera <pathId> add [index] [hold=N] [easing=NAME] [relative=true]** *在当前位置添加关键帧。`index` 指定插入位置，从 1 开始计数，省略或超出范围时追加到末尾；`hold` 设置该路径段的持续游戏刻数；`easing` 设置该段的缓动方式；`relative=true` 将关键帧标记为相对位置（`~`），但仍会原样写入当前坐标，因此播放前需要将其改为相对于锚点的偏移。*
- **/mm camera <pathId> remove [index]** *移除指定索引的关键帧，索引从 1 开始。省略或超出范围时移除最后一个。*

## 刷怪点命令 {#spawner-commands}

- 大多数刷怪点命令都可以使用特殊筛选器和通配符替代刷怪点名称，从而同时操作多个刷怪点。
- 使用 **g:group_name**，对整个刷怪点组执行命令。
- 使用 **r:radius**，对 **radius** 格方块范围内的所有刷怪点执行命令
- **?** 表示单个字符通配符。例如，执行 **/mm s set ?at leashrange 32** 会修改名为 Cat、Rat、Fat 的刷怪点，但不会修改 Matt。
- ***** 表示任意数量字符的通配符。例如，执行 **/mm s set T* leashrange 32** 会将所有名称以 T 开头的刷怪点的 leash range 设为 32
- **执行命令时，如果用 * 作为刷怪点名称，将修改所有刷怪点**
- **/mm spawners**（别名：**/mm s**）*刷怪点相关命令的根命令。*
- **/mm s create** *[spawner_name]* *[mob name]*
  - 在玩家准星指向的位置创建刷怪点。
  - 刷怪点会生成 mob_name 指定的生物，既可以是 Minecraft 内置生物，也可以是你在 ExampleMobs.yml 配置页中创建的生物名称。
  - **/mm s create Ruins_Skeleton1 DecayingSkeleton**
- **/mm s set [spawner_name] [setting] [value]**
  - 修改刷怪点的一项设置，完整设置列表见下文
  - 所有可设置的项目见[刷怪点选项](spawners.md)。
- **/mm s addcondition [spawner_name] [condition] [value]**
  - 添加刷怪点条件，用来判断计时结束后是否应生成生物。
  - 可用条件见[刷怪点条件](skills/conditions.md)
- **/mm s removecondition [spawner_name] [condition]**
  - 移除刷怪点条件。
  - **/mm s removecondition Ruins_Skeleton1 outside**
- **/mm s info [spawner_name]**
  - 列出指定刷怪点的相关信息。
  - **/mm s info Ruins_Skeleton1**（列出 Ruins_Skeleton1 刷怪点的信息）
- **/mm s listnear <distance>**
  - 列出附近的所有刷怪点。
  - 添加 distance 参数可以缩小查询范围。
  - **/mm s listnear 15**（显示 15 格方块范围内所有刷怪点的名称）
- **/mm s resettimers [name]**
  - 重置指定刷怪点的冷却计时和重置计时。
- **/mm s resettimers Ruins_Skeleton1**（重置 Ruins_Skeleton1 刷怪点）
- **/mm s activate [name]**
  - 激活指定刷怪点，强制生成一次生物。
- **/mm s activate** Ruins_Skeleton1**（使 Ruins_Skeleton1 刷怪点生成生物）
- **/mm s cut [search_string]**
  - 按照指定字符串剪切一组刷怪点。
- **/mm s cut g:BoneCastle**（剪切“BoneCastle”组中的所有刷怪点）
- **/mm s cut r:200**（剪切半径 200 格方块内的所有刷怪点）
- **/mm s cut Elementals_**（剪切所有名称以 Elementals_ 开头的刷怪点）
- **/mm s cut**（剪切所有刷怪点，请格外小心！）
- **/mm s paste**
  - 将剪切的刷怪点组粘贴到新的相对位置。
  - 可以多次粘贴刷怪点，但会替换上一次粘贴的结果，不会复制出额外的刷怪点。
- **/mm s undo**
  - 撤销上一次剪切操作，将刷怪点放回原位。
  - 仅在尚未剪切另一组刷怪点时有效。

## 标记点命令 {#pins-commands}

参见[标记点 Wiki 页面](pins.md#commands)

## 实用命令 {#utility-commands}

- **/mm test cast [skillname]**：以生物的方式执行技能。
- **/mm test mechanic [line]**：以生物的方式执行一行技能机制。
- **/mm i get [droptable]**：从掉落表中获取物品，效果如同击杀了掉落这些物品的生物。

## 信号命令 {#signal-commands}

- **/mm signal <UUID> <signal>**
- 向生物发送信号，以切换某些技能
- 必须使用生物的 UUID，使用生物名称无效
- 通常用作 tellraw 命令中的组件
- 要使用此功能，必须同时授予这 3 个权限
  - `mythicmobs.signal`
  - `mythicmobs.command.signal`
  - `mythicmobs.command.base`

## 菜单命令 {#menu-commands}

- **/mm menu open [menu name]**：打开对应的自定义菜单。需要 MythicMobs Premium 或 MythicRPG

# 权限 {#permissions}

目前 MythicMobs 只支持两个用于授予插件完整访问权限的权限节点。原因是 MythicMobs 中几乎所有命令都很容易被滥用，原作者目前认为没有必要为每项功能设置单独权限。之后有时间时仍会按需求添加更多权限，但此事的优先级不高。

## 通用设置 {#general}

- **mythicmobs.admin**：*授予插件所有命令的使用权限。*

## 命令 {#commands-2}

- 可以通过 **mythicmobs.command.<command>** 单独授予某个命令的使用权限
- **mythicmobs.command.camera**：*允许使用 **/mm camera** 命令编辑镜头动画路径。*
- **mythicmobs.command.info**：*允许使用 **/mm info** 命令。*
- **mythicmobs.command.mobs.list**：*允许使用 **/mm mobs list** 命令。*
- **mythicmobs.command.signal**：*允许使用“/mm signal
  <mob.uuid> <signal>”命令*
- **mythicmobs.command.test.cast**：*允许使用“/mm test cast”命令*
- **mythicmobs.command.test.addthreat**：*允许使用“/mm test addthreat”命令*
- **mythicmobs.command.test.reducethreat**：*允许使用“/mm test reducethreat”命令*
