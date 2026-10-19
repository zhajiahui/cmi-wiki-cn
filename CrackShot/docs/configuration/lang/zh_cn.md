---
title: lang/zh_CN.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: lang/zh_CN.yml
source_version: 0.98.13-x6
---

# lang/zh_CN.yml

文件：`lang/zh_CN.yml`。版本：`0.98.13-x6`。

语言与界面文字。

## `Command` { #command }

```yaml title="lang/zh_CN.yml · Command"
# CrackShot 的中文文字。服主可以直接改这里；删掉的条目会用插件自带的中文。

Command:
  # 玩家：命令帮助
  Aliases: "§7░ §c别名：§7/shot, /cra, /cs"
  # 玩家：命令帮助
  Author: "§7░ §c作者：§7Shampaggon"
  # 玩家：命令帮助
  Commands: "§7░ §c命令："
  # 控制台：命令写错
  Console_Invalid: "[CrackShot] 没有这个命令。"
  # 控制台：查看版本
  Console_Version: "[CrackShot] 版本：<version>"
  # 执行给枪命令的人：给出去了
  Delivered: "已经给了 <player>。"
  # 玩家：拿东西没有权限
  Get_No_Permission: "你没有拿这件东西的权限。"
  # 执行给枪命令的人：没有权限
  Give_No_Permission: "你没有把这件东西给别人的权限。"
  # 玩家：自己拿到了
  Grabbed: "已拿到 - <name><amount>"
  # 玩家：命令帮助
  Help_Config_Reload: "§7░ §c- §7/shot config reload"
  # 玩家：命令帮助
  Help_Get: "§7░ §c- §7/shot get 武器 数量"
  # 玩家：命令帮助
  Help_Give: "§7░ §c- §7/shot give 玩家 武器 数量"
  # 玩家：命令帮助
  Help_List: "§7░ §c- §7/shot list [all §l或§r§7 页码]"
  # 玩家：命令帮助
  Help_Reload: "§7░ §c- §7/shot reload"
  # 命令写错
  Invalid: "没有这个命令。"
  # 玩家：数量写错
  Invalid_Amount: "'<amount>' 不是有效的数量。"
  # 玩家：页码写错
  Invalid_Page: "页码不对。"
  # 玩家：自己的背包满了
  Inventory_Full: "你的背包满了。"
  # 玩家：武器列表的标题
  List_All: "§7░ §c武器（全部）："
  # 玩家：武器列表的标题
  List_Page: "§7░ §c武器（第 <count>/<amount> 页）："
  # 没有权限
  No_Permission: "你没有权限这样做。"
  # 执行给枪命令的人：对方背包满了
  Player_Inventory_Full: "<player> 的背包满了。"
  # 执行给枪命令的人：找不到玩家
  Player_Not_Found: "找不到叫 '<player>' 的玩家。"
  # 重新加载完成
  Reloaded: "配置已重新加载。"
  # 商店牌子的第一行
  Store_Title: "§f商店编号 <amount>"
  # 玩家：查看版本
  Version: "§7░ §c版本：§7<version>"
  # 武器名写错
  Weapon_Not_Found: "没有叫 '<weapon>' 的武器。"
```

## `Config_Error` { #config_error }

```yaml title="lang/zh_CN.yml · Config_Error"
Config_Error:
  # 正在用这把武器的玩家：配置写错
  Airstrike_Block: "武器 '<weapon>' 的 Airstrikes 里 '<value>' 不是有效的方块。"
  # 正在用这把武器的玩家：配置写错
  Ammo_Reload_Node: "武器 '<weapon>'：Take_Ammo_On_Reload 要写在 Reload 模块里，不是 Ammo 模块里。"
  # 正在用这把武器的玩家：配置写错
  Ammo_Take: "武器 '<weapon>' 开了 Ammo，但 Take_Ammo_On_Reload 和 Take_Ammo_Per_Shot 至少要有一个是 true。"
  # 正在用这把武器的玩家：配置写错
  Attachment_Accessory: "武器 '<weapon>' 的配件 '<name>' 不对：配件必须是 accessory 类型。"
  # 正在用这把武器的玩家：配置写错
  Attachment_Dual_Wield: "武器 '<weapon>' 不能同时用配件和双持。"
  # 正在用这把武器的玩家：配置写错
  Attachment_Explosive: "武器 '<weapon>' 是配件，不能用 Explosive_Devices 模块。"
  # 正在用这把武器的玩家：配置写错
  Attachment_Missing: "武器 '<weapon>' 没写配件对应的武器内部名。"
  # 正在用这把武器的玩家：配置写错
  Automatic_Burst: "武器 '<weapon>' 同时开了 Fully_Automatic 和 Burstfire，只能留一个。"
  # 正在用这把武器的玩家：配置写错
  Automatic_Delay: "武器 '<weapon>' 开了 Fully_Automatic 时，Delay_Between_Shots 要删掉，或者不大于 1。"
  # 正在用这把武器的玩家：配置写错
  Bomblet_Limit: "<amount> 的 <count> 次方是 <value> 个子炸弹，超过了 CrackShot 的上限 1000。把武器 '<weapon>' 的 Number_Of_Splits 或 Number_Of_Bomblets 调小。"
  # 控制台：配置写错
  Bonus_Drops: "武器 '<weapon>' 的 Bonus_Drops 里 '<value>' 不是有效的物品编号。"
  # 控制台：配置写错
  Bonus_Drops_Logged: "武器 '<weapon>' 的 Bonus_Drops 里 '<value>' 不是有效的物品编号。"
  # 控制台：配置写错
  Crafting_Count: "武器 '<weapon>' 的合成配方（<value>）写了 <count> 格，应该是 9 格。"
  # 正在用这把武器的玩家：配置写错
  Device_Item: "武器 '<weapon>' 的 Device_Info 没写有效的物品编号。"
  # 正在用这把武器的玩家：配置写错
  Device_Minecart: "武器 '<weapon>' 的 Device_Info 里 '<value>' 不是有效的矿车类型。"
  # 控制台：配置写错
  Enchantment_Level: "武器 '<weapon>' 的 Enchantment_To_Check 没写有效的附魔等级。"
  # 控制台：配置写错
  Energy_Spawn: "武器 '<weapon>' 是能量弹，不能用 Spawn_Entity_On_Hit 模块。"
  # 控制台：配置写错
  Entity_Amount: "武器 '<weapon>' 的 EntityType_Baby_Explode_Amount 里 '<value>' 不是有效的数字。"
  # 控制台：配置写错
  Entity_Format: "武器 '<weapon>' 的 '<value>' 格式不对。"
  # 控制台：配置写错
  Entity_Type: "武器 '<weapon>' 的 '<value>' 不是有效的生物。"
  # 控制台：插件内部错误
  Explosion_Constructor: "找不到能用的 EntityExplodeEvent 构造方法。"
  # 控制台：插件内部错误
  Explosion_Create: "创建 EntityExplodeEvent 失败"
  # 正在用这把武器的玩家：配置文件有错
  File_Invalid: "文件 '<file>' 里有配置错误，请看控制台里的报错并改正。"
  # 正在用这把武器的玩家：配置文件没能加载
  File_Load_Failed: "文件 '<file>' 没能加载。"
  # 正在用这把武器的玩家：配置写错
  Fire_Rate: "武器 '<weapon>' 的 Fire_Rate 不对，只能是 1 到 16。"
  # 控制台：配置写错
  Firearm_Action: "武器 '<weapon>' 的 '<value>' 不是有效的枪机类型，只能是 slide、bolt、lever、pump、break 或 revolver。"
  # 控制台：配置写错
  Firework_Format: "武器 '<weapon>' 的 '<value>' 格式不对，应该写成：类型-轨迹-闪烁-红-蓝-绿。"
  # 控制台：配置写错
  Firework_Value: "武器 '<weapon>' 的 '<value>' 里有不对的烟花类型、闪烁、轨迹或颜色。"
  # 正在用这把武器的玩家：配置写错
  Get_Item_Type: "没有写 Item_Type。"
  # 控制台：配置写错
  Item_Name_Missing: "武器 '<weapon>' 没写 Item_Name。"
  # 控制台：两把武器的显示名太像。<name> 是另一把武器的内部名，<value> 和 <node> 是两把武器的显示名
  Item_Name_Similar: "武器 '<weapon>' 和 '<name>' 的显示名太像了（'<value>' 和 '<node>'），CrackShot 分不清。每把武器的 Item_Name 都要不一样。"
  # 控制台：配置写错
  Item_Type_Invalid: "武器 '<weapon>' 的 Item_Type 不对。"
  # 控制台：配置写错
  Item_Type_Missing: "武器 '<weapon>' 没写 Item_Type。"
  # 控制台：配置写错
  Item_Type_No_Value: "武器 '<weapon>' 没写 Item_Type。"
  # 正在用这把武器的玩家：配置写错
  Melee_Attachment: "武器 '<weapon>' 的近战配件 '<name>' 找不到。"
  # 正在用这把武器的玩家：配置写错
  Node_Missing: "武器 '<weapon>' 没有 '<node>' 这个节点。"
  # 正在用这把武器的玩家：配置写错
  Node_Value: "武器 '<weapon>' 的 '<node>' 写的值不对。"
  # 正在用这把武器的玩家：配置写错
  One_Time_Ammo: "武器 '<weapon>' 的 One_Time_Use 不能和 Ammo 模块一起用。"
  # 控制台：配置写错
  Particle_Block: "武器 '<weapon>' 的粒子效果 '<value>' 里方块编号 '<name>' 不对。"
  # 控制台：配置写错
  Particle_Number: "武器 '<weapon>' 的粒子效果 '<value>' 里数字 '<name>' 不对。"
  # 控制台：配置写错
  Potion_Format: "武器 '<weapon>' 的 '<value>' 格式不对，应该写成：药水-持续时间-等级。"
  # 控制台：配置写错
  Potion_Value: "武器 '<weapon>' 的 '<value>' 里有不对的药水类型、持续时间或等级。"
  # 正在用这把武器的玩家：配置写错
  Projectile_Amount: "武器 '<weapon>' 没写 Projectile_Amount。"
  # 正在用这把武器的玩家：配置写错
  Projectile_Splash: "武器 '<weapon>' 的 Projectile_Subtype 不是喷溅药水。"
  # 正在用这把武器的玩家：配置写错
  Projectile_Subtype_Format: "武器 '<weapon>' 的 Projectile_Subtype 格式不对。"
  # 正在用这把武器的玩家：配置写错
  Projectile_Subtype_Missing: "武器 '<weapon>' 没写 Projectile_Subtype。"
  # 正在用这把武器的玩家：配置写错
  Projectile_Subtype_Number: "武器 '<weapon>' 的 Projectile_Subtype 里有不对的数字。"
  # 正在用这把武器的玩家：配置写错
  Projectile_Type: "'<value>' 不是有效的弹丸类型。"
  # 正在用这把武器的玩家：配置写错
  Region_Arguments: "武器 '<weapon>' 的 World_And_Coordinates 参数个数不对。"
  # 正在用这把武器的玩家：配置写错
  Region_Coordinates: "武器 '<weapon>' 的 World_And_Coordinates 写错了，请检查坐标。"
  # 正在用这把武器的玩家：配置写错
  Reload_Amount: "武器 '<weapon>' 开了 Reload，但没写有效的 Reload_Amount。"
  # 正在用这把武器的玩家：配置写错
  Removal_Delay: "武器 '<weapon>' 的 Removal_Or_Drag_Delay 写错了。"
  # 正在用这把武器的玩家：配置写错
  Shop_Price: "武器 '<weapon>' 的 'Price: <value>' 没有有效的物品编号或数量。"
  # 正在用这把武器的玩家：配置写错
  Shrapnel_Data: "武器 '<weapon>' 的 '<value>' 子类型不对。"
  # 控制台：配置写错
  Sound_Format: "武器 '<weapon>' 的声音 '<value>' 格式不对，应该写成：声音-音量-音调-延迟。"
  # 控制台：配置写错
  Sound_Value: "武器 '<weapon>' 的声音 '<value>' 里有不对的数字或声音名。"
  # 控制台：配置写错
  Super_Effective: "武器 '<weapon>' 的 Super_Effective 写的值不对。"
```

## `Console` { #console }

```yaml title="lang/zh_CN.yml · Console"
Console:
  # 控制台：语言选择无效时回退中文
  Language_Invalid: "general.yml 的 Language 写的是 <value>，只认 zh_CN 和 en_US，先按 zh_CN 处理。"
  # 控制台：缺少实体移除事件时停用元数据清理
  Metadata_Cleanup_Disabled: "当前服务端没有实体移除事件（1.20.4 起才有），实体元数据清理未启用，其余功能照常。"
  # 控制台：启动完成
  Activated: "枪械模式已启用。"
  # 控制台：配置里用了新旧版本含义不同的名字
  Ambiguous_BRICK: "<file> 里武器 <weapon> 的 <node> 写了 BRICK。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是砖块，高版本上是红砖（物品）；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：砖块写 45，红砖写 336。"
  # 控制台：配置里用了新旧版本含义不同的名字
  Ambiguous_GRASS: "<file> 里武器 <weapon> 的 <node> 写了 GRASS。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是草方块，高版本上是草丛，较新的版本里干脆没有这个名字；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：草方块写 2，草丛写 31:1。"
  # 控制台：配置里用了新旧版本含义不同的名字
  Ambiguous_MAP: "<file> 里武器 <weapon> 的 <node> 写了 MAP。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是地图，高版本上是空地图；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：地图写 358，空地图写 395。"
  # 控制台：配置里用了新旧版本含义不同的名字
  Ambiguous_MELON: "<file> 里武器 <weapon> 的 <node> 写了 MELON。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是西瓜片，高版本上是西瓜（方块）；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：西瓜片写 360，西瓜写 103。"
  # 控制台：配置里用了新旧版本含义不同的名字
  Ambiguous_NETHER_BRICK: "<file> 里武器 <weapon> 的 <node> 写了 NETHER_BRICK。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是地狱砖块，高版本上是地狱砖（物品）；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：地狱砖块写 112，地狱砖写 405。"
  # 控制台：插件内部错误，后面跟着错误详情
  Exception: "<name>"
  # 控制台：文件没能加载
  File_Load_Failed: "<file> 没能加载。"
  # 控制台：第一次运行时生成了默认文件
  General_Added: "已生成通用配置。"
  # 控制台：全局配置的标签
  Global: "全局"
  # 控制台：语言文件没能加载，后面跟着错误详情
  Language_Load_Failed: "语言文件 <file> 没能加载。"
  # 控制台：第一次运行时生成了默认文件
  Messages_Added: "已生成消息配置。"
  # 控制台：名字检查的一条明细
  Name_Issue: "<file> 里武器 <weapon> 的 <node>：<name>，<value>。"
  # 控制台：名字检查的开头
  Name_Summary: "检查配置里的物品、声音这些名字，有 <count> 处在这台服务器上用不了："
  # 控制台：名字检查的原因
  Name_Unavailable: "这个版本没有对应的东西"
  # 控制台：名字检查的原因
  Name_Unknown: "没有这个名字"
  # 控制台：一把武器都没加载到
  No_Weapons: "没有加载到任何武器。"
  # 控制台：服务端太旧
  Outdated_Server: "加载失败：CraftBukkit 版本太旧。"
  # 控制台：合成配方没能登记，后面跟着错误详情
  Recipe_Exception: "武器 <weapon> 的合成配方没能登记，已跳过（<name>）。"
  # 控制台：合成配方没能登记
  Recipe_Failed: "武器 <weapon> 的合成配方没能登记，已跳过。"
  # 控制台：插件内部错误
  Recipe_Identifier_Failed: "配方标识创建失败"
  # 控制台：插件内部错误
  Recipe_Initialize_Failed: "配方接口初始化失败"
  # 控制台：插件内部错误
  Recipe_Remove_Failed: "配方移除失败"
  # 控制台：改了合成配方
  Recipe_Restart: "合成配方改了以后要重启服务器才生效。"
  # 控制台：插件内部错误
  Recipe_Shaped_Failed: "有序配方创建失败"
  # 控制台：插件内部错误
  Recipe_Shapeless_Failed: "无序配方创建失败"
  # 控制台：重新加载完成
  Reloaded: "配置已重新加载。"
  # 控制台：声音没能加载，后面跟着错误详情
  Sounds_Failed: "声音没能加载。"
  # 控制台：认不出服务端版本
  Version_Unparsed: "认不出服务端的版本号，先按 0.0.0 处理；各项适配会按功能实际能不能用来判断。"
  # 控制台：第一次运行时生成了默认文件
  Weapons_Added: "已生成默认武器。"
  # 控制台：开镜效果没能加载
  Zoom_Failed: "开镜效果没能加载。"
```

## `Prefix` { #prefix }

```yaml title="lang/zh_CN.yml · Prefix"
# 发给玩家的消息前缀
Prefix: "§7░ §c[-§l¬§cº§lc§7§ls§7] §c- §7"
```
