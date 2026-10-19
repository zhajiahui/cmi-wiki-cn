---
title: lang/en_US.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: lang/en_US.yml
source_version: 0.98.13-x6
---

# lang/en_US.yml

文件：`lang/en_US.yml`。版本：`0.98.13-x6`。

语言与界面文字。

## `Command` { #command }

```yaml title="lang/en_US.yml · Command"
# 英文消息；保留原有输出。

Command:
  # Command.Aliases：向玩家显示。
  Aliases: "§7░ §c别名：§7/shot, /cra, /cs"
  # Command.Author：向玩家显示。
  Author: "§7░ §c作者：§7Shampaggon"
  # Command.Commands：向玩家显示。
  Commands: "§7░ §c命令："
  # Command.Console_Invalid：向控制台显示。
  Console_Invalid: "[CrackShot] 没有这个命令。"
  # Command.Console_Version：向控制台显示。
  Console_Version: "[CrackShot] 版本：<version>"
  # Command.Delivered：向命令发送者显示。
  Delivered: "已经给了 <player>。"
  # Command.Get_No_Permission：向玩家显示。
  Get_No_Permission: "你没有拿这件东西的权限。"
  # Command.Give_No_Permission：向命令发送者显示。
  Give_No_Permission: "你没有把这件东西给别人的权限。"
  # Command.Grabbed：向玩家显示。
  Grabbed: "已拿到 - <name><amount>"
  # Command.Help_Config_Reload：向玩家显示。
  Help_Config_Reload: "§7░ §c- §7/shot config reload"
  # Command.Help_Get：向玩家显示。
  Help_Get: "§7░ §c- §7/shot get <weapon> <#>"
  # Command.Help_Give：向玩家显示。
  Help_Give: "§7░ §c- §7/shot give <user> <weapon> <#>"
  # Command.Help_List：向玩家显示。
  Help_List: "§7░ §c- §7/shot list [all §lOR§r§7 <page>]"
  # Command.Help_Reload：向玩家显示。
  Help_Reload: "§7░ §c- §7/shot reload"
  # Command.Invalid：向命令发送者显示。
  Invalid: "没有这个命令。"
  # Command.Invalid_Amount：向玩家显示。
  Invalid_Amount: "'<amount>' 不是有效的数量。"
  # Command.Invalid_Page：向玩家显示。
  Invalid_Page: "页码不对。"
  # Command.Inventory_Full：向玩家显示。
  Inventory_Full: "你的背包满了。"
  # Command.List_All：向玩家显示。
  List_All: "§7░ §c武器（全部）："
  # Command.List_Page：向玩家显示。
  List_Page: "§7░ §c武器（第 <count>/<amount> 页）："
  # Command.No_Permission：向命令发送者显示。
  No_Permission: "你没有权限这样做。"
  # Command.Player_Inventory_Full：向命令发送者显示。
  Player_Inventory_Full: "<player> 的背包满了。"
  # Command.Player_Not_Found：向命令发送者显示。
  Player_Not_Found: "找不到叫 '<player>' 的玩家。"
  # Command.Reloaded：向命令发送者显示。
  Reloaded: "配置已重新加载。"
  # Command.Store_Title：向玩家显示。
  Store_Title: "§f商店编号 <amount>"
  # Command.Version：向玩家显示。
  Version: "§7░ §c版本：§7<version>"
  # Command.Weapon_Not_Found：向命令发送者显示。
  Weapon_Not_Found: "没有叫 '<weapon>' 的武器。"
```

## `Config_Error` { #config_error }

```yaml title="lang/en_US.yml · Config_Error"
Config_Error:
  # Config_Error.Airstrike_Block：向玩家显示。
  Airstrike_Block: "武器 '<weapon>' 的 Airstrikes 里 '<value>' 不是有效的方块。"
  # Config_Error.Ammo_Reload_Node：向玩家显示。
  Ammo_Reload_Node: "武器 '<weapon>'：Take_Ammo_On_Reload 要写在 Reload 模块里，不是 Ammo 模块里。"
  # Config_Error.Ammo_Take：向玩家显示。
  Ammo_Take: "武器 '<weapon>' 开了 Ammo，但 Take_Ammo_On_Reload 和 Take_Ammo_Per_Shot 至少要有一个是 true。"
  # Config_Error.Attachment_Accessory：向玩家显示。
  Attachment_Accessory: "武器 '<weapon>' 的配件 '<name>' 不对：配件必须是 accessory 类型。"
  # Config_Error.Attachment_Dual_Wield：向玩家显示。
  Attachment_Dual_Wield: "武器 '<weapon>' 不能同时用配件和双持。"
  # Config_Error.Attachment_Explosive：向玩家显示。
  Attachment_Explosive: "武器 '<weapon>' 是配件，不能用 Explosive_Devices 模块。"
  # Config_Error.Attachment_Missing：向玩家显示。
  Attachment_Missing: "武器 '<weapon>' 没写配件对应的武器内部名。"
  # Config_Error.Automatic_Burst：向玩家显示。
  Automatic_Burst: "武器 '<weapon>' 同时开了 Fully_Automatic 和 Burstfire，只能留一个。"
  # Config_Error.Automatic_Delay：向玩家显示。
  Automatic_Delay: "武器 '<weapon>' 开了 Fully_Automatic 时，Delay_Between_Shots 要删掉，或者不大于 1。"
  # Config_Error.Bomblet_Limit：向玩家显示。
  Bomblet_Limit: "<amount> 的 <count> 次方是 <value> 个子炸弹，超过了 CrackShot 的上限 1000。把武器 '<weapon>' 的 Number_Of_Splits 或 Number_Of_Bomblets 调小。"
  # Config_Error.Bonus_Drops：向控制台显示。
  Bonus_Drops: "武器 '<weapon>' 的 Bonus_Drops 里 '<value>' 不是有效的物品编号。"
  # Config_Error.Bonus_Drops_Logged：向控制台显示。
  Bonus_Drops_Logged: "武器 '<weapon>' 的 Bonus_Drops 里 '<value>' 不是有效的物品编号。"
  # Config_Error.Crafting_Count：向控制台显示。
  Crafting_Count: "武器 '<weapon>' 的合成配方（<value>）写了 <count> 格，应该是 9 格。"
  # Config_Error.Device_Item：向玩家显示。
  Device_Item: "武器 '<weapon>' 的 Device_Info 没写有效的物品编号。"
  # Config_Error.Device_Minecart：向玩家显示。
  Device_Minecart: "武器 '<weapon>' 的 Device_Info 里 '<value>' 不是有效的矿车类型。"
  # Config_Error.Enchantment_Level：向控制台显示。
  Enchantment_Level: "武器 '<weapon>' 的 Enchantment_To_Check 没写有效的附魔等级。"
  # Config_Error.Energy_Spawn：向控制台显示。
  Energy_Spawn: "武器 '<weapon>' 是能量弹，不能用 Spawn_Entity_On_Hit 模块。"
  # Config_Error.Entity_Amount：向控制台显示。
  Entity_Amount: "武器 '<weapon>' 的 EntityType_Baby_Explode_Amount 里 '<value>' 不是有效的数字。"
  # Config_Error.Entity_Format：向控制台显示。
  Entity_Format: "武器 '<weapon>' 的 '<value>' 格式不对。"
  # Config_Error.Entity_Type：向控制台显示。
  Entity_Type: "武器 '<weapon>' 的 '<value>' 不是有效的生物。"
  # Config_Error.Explosion_Constructor：向控制台显示。
  Explosion_Constructor: "找不到能用的 EntityExplodeEvent 构造方法。"
  # Config_Error.Explosion_Create：向控制台显示。
  Explosion_Create: "创建 EntityExplodeEvent 失败"
  # Config_Error.File_Invalid：向玩家显示。
  File_Invalid: "文件 '<file>' 里有配置错误，请看控制台里的报错并改正。"
  # Config_Error.File_Load_Failed：向玩家显示。
  File_Load_Failed: "文件 '<file>' 没能加载。"
  # Config_Error.Fire_Rate：向玩家显示。
  Fire_Rate: "武器 '<weapon>' 的 Fire_Rate 不对，只能是 1 到 16。"
  # Config_Error.Firearm_Action：向控制台显示。
  Firearm_Action: "武器 '<weapon>' 的 '<value>' 不是有效的枪机类型，只能是 slide、bolt、lever、pump、break 或 revolver。"
  # Config_Error.Firework_Format：向控制台显示。
  Firework_Format: "武器 '<weapon>' 的 '<value>' 格式不对，应该写成：类型-轨迹-闪烁-红-蓝-绿。"
  # Config_Error.Firework_Value：向控制台显示。
  Firework_Value: "武器 '<weapon>' 的 '<value>' 里有不对的烟花类型、闪烁、轨迹或颜色。"
  # Config_Error.Get_Item_Type：向玩家显示。
  Get_Item_Type: "没有写 Item_Type。"
  # Config_Error.Item_Name_Missing：向控制台显示。
  Item_Name_Missing: "武器 '<weapon>' 没写 Item_Name。"
  # Config_Error.Item_Name_Similar：向控制台显示。
  Item_Name_Similar: "武器 '<weapon>' 和 '<name>' 的显示名太像了（'<value>' 和 '<node>'），CrackShot 分不清。每把武器的 Item_Name 都要不一样。"
  # Config_Error.Item_Type_Invalid：向控制台显示。
  Item_Type_Invalid: "武器 '<weapon>' 的 Item_Type 不对。"
  # Config_Error.Item_Type_Missing：向控制台显示。
  Item_Type_Missing: "武器 '<weapon>' 没写 Item_Type。"
  # Config_Error.Item_Type_No_Value：向控制台显示。
  Item_Type_No_Value: "武器 '<weapon>' 没写 Item_Type。"
  # Config_Error.Melee_Attachment：向玩家显示。
  Melee_Attachment: "武器 '<weapon>' 的近战配件 '<name>' 找不到。"
  # Config_Error.Node_Missing：向玩家显示。
  Node_Missing: "武器 '<weapon>' 没有 '<node>' 这个节点。"
  # Config_Error.Node_Value：向玩家显示。
  Node_Value: "武器 '<weapon>' 的 '<node>' 写的值不对。"
  # Config_Error.One_Time_Ammo：向玩家显示。
  One_Time_Ammo: "武器 '<weapon>' 的 One_Time_Use 不能和 Ammo 模块一起用。"
  # Config_Error.Particle_Block：向控制台显示。
  Particle_Block: "武器 '<weapon>' 的粒子效果 '<value>' 里方块编号 '<name>' 不对。"
  # Config_Error.Particle_Number：向控制台显示。
  Particle_Number: "武器 '<weapon>' 的粒子效果 '<value>' 里数字 '<name>' 不对。"
  # Config_Error.Potion_Format：向控制台显示。
  Potion_Format: "武器 '<weapon>' 的 '<value>' 格式不对，应该写成：药水-持续时间-等级。"
  # Config_Error.Potion_Value：向控制台显示。
  Potion_Value: "武器 '<weapon>' 的 '<value>' 里有不对的药水类型、持续时间或等级。"
  # Config_Error.Projectile_Amount：向玩家显示。
  Projectile_Amount: "武器 '<weapon>' 没写 Projectile_Amount。"
  # Config_Error.Projectile_Splash：向玩家显示。
  Projectile_Splash: "武器 '<weapon>' 的 Projectile_Subtype 不是喷溅药水。"
  # Config_Error.Projectile_Subtype_Format：向玩家显示。
  Projectile_Subtype_Format: "武器 '<weapon>' 的 Projectile_Subtype 格式不对。"
  # Config_Error.Projectile_Subtype_Missing：向玩家显示。
  Projectile_Subtype_Missing: "武器 '<weapon>' 没写 Projectile_Subtype。"
  # Config_Error.Projectile_Subtype_Number：向玩家显示。
  Projectile_Subtype_Number: "武器 '<weapon>' 的 Projectile_Subtype 里有不对的数字。"
  # Config_Error.Projectile_Type：向玩家显示。
  Projectile_Type: "'<value>' 不是有效的弹丸类型。"
  # Config_Error.Region_Arguments：向玩家显示。
  Region_Arguments: "武器 '<weapon>' 的 World_And_Coordinates 参数个数不对。"
  # Config_Error.Region_Coordinates：向玩家显示。
  Region_Coordinates: "武器 '<weapon>' 的 World_And_Coordinates 写错了，请检查坐标。"
  # Config_Error.Reload_Amount：向玩家显示。
  Reload_Amount: "武器 '<weapon>' 开了 Reload，但没写有效的 Reload_Amount。"
  # Config_Error.Removal_Delay：向玩家显示。
  Removal_Delay: "武器 '<weapon>' 的 Removal_Or_Drag_Delay 写错了。"
  # Config_Error.Shop_Price：向玩家显示。
  Shop_Price: "武器 '<weapon>' 的 'Price: <value>' 没有有效的物品编号或数量。"
  # Config_Error.Shrapnel_Data：向玩家显示。
  Shrapnel_Data: "武器 '<weapon>' 的 '<value>' 子类型不对。"
  # Config_Error.Sound_Format：向控制台显示。
  Sound_Format: "武器 '<weapon>' 的声音 '<value>' 格式不对，应该写成：声音-音量-音调-延迟。"
  # Config_Error.Sound_Value：向控制台显示。
  Sound_Value: "武器 '<weapon>' 的声音 '<value>' 里有不对的数字或声音名。"
  # Config_Error.Super_Effective：向控制台显示。
  Super_Effective: "武器 '<weapon>' 的 Super_Effective 写的值不对。"
```

## `Console` { #console }

```yaml title="lang/en_US.yml · Console"
Console:
  # 控制台：语言选择无效时回退中文
  Language_Invalid: "general.yml 的 Language 写的是 <value>，只认 zh_CN 和 en_US，先按 zh_CN 处理。"
  # 控制台：缺少实体移除事件时停用元数据清理
  Metadata_Cleanup_Disabled: "当前服务端没有实体移除事件（1.20.4 起才有），实体元数据清理未启用，其余功能照常。"
  # Console.Activated：向控制台显示。
  Activated: "枪械模式已启用。"
  # Console.Ambiguous_BRICK：向控制台显示。
  Ambiguous_BRICK: "<file> 里武器 <weapon> 的 <node> 写了 BRICK。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是砖块，高版本上是红砖（物品）；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：砖块写 45，红砖写 336。"
  # Console.Ambiguous_GRASS：向控制台显示。
  Ambiguous_GRASS: "<file> 里武器 <weapon> 的 <node> 写了 GRASS。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是草方块，高版本上是草丛，较新的版本里干脆没有这个名字；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：草方块写 2，草丛写 31:1。"
  # Console.Ambiguous_MAP：向控制台显示。
  Ambiguous_MAP: "<file> 里武器 <weapon> 的 <node> 写了 MAP。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是地图，高版本上是空地图；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：地图写 358，空地图写 395。"
  # Console.Ambiguous_MELON：向控制台显示。
  Ambiguous_MELON: "<file> 里武器 <weapon> 的 <node> 写了 MELON。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是西瓜片，高版本上是西瓜（方块）；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：西瓜片写 360，西瓜写 103。"
  # Console.Ambiguous_NETHER_BRICK：向控制台显示。
  Ambiguous_NETHER_BRICK: "<file> 里武器 <weapon> 的 <node> 写了 NETHER_BRICK。这个名字在新旧版本里指的不是同一个东西：1.12.2 上是地狱砖块，高版本上是地狱砖（物品）；这台服务器（<version>）按 <value> 处理。想在两种版本上都一样，改写成数字编号：地狱砖块写 112，地狱砖写 405。"
  # Console.Exception：向控制台显示。
  Exception: "[CrackShot] <name>"
  # Console.File_Load_Failed：向控制台显示。
  File_Load_Failed: "<file> 没能加载。"
  # Console.General_Added：向控制台显示。
  General_Added: "已生成通用配置。"
  # Console.Global：向控制台显示。
  Global: "全局"
  # Console.Language_Load_Failed：向控制台显示。
  Language_Load_Failed: "语言文件 <file> 没能加载。"
  # Console.Messages_Added：向控制台显示。
  Messages_Added: "已生成消息配置。"
  # Console.Name_Issue：向控制台显示。
  Name_Issue: "<file> 里武器 <weapon> 的 <node>：<name>，<value>。"
  # Console.Name_Summary：向控制台显示。
  Name_Summary: "检查配置里的物品、声音这些名字，有 <count> 处在这台服务器上用不了："
  # Console.Name_Unavailable：向控制台显示。
  Name_Unavailable: "这个版本没有对应的东西"
  # Console.Name_Unknown：向控制台显示。
  Name_Unknown: "没有这个名字"
  # Console.No_Weapons：向控制台显示。
  No_Weapons: "没有加载到任何武器。"
  # Console.Outdated_Server：向控制台显示。
  Outdated_Server: "加载失败：CraftBukkit 版本太旧。"
  # Console.Recipe_Exception：向控制台显示。
  Recipe_Exception: "武器 <weapon> 的合成配方没能登记，已跳过（<name>）。"
  # Console.Recipe_Failed：向控制台显示。
  Recipe_Failed: "武器 <weapon> 的合成配方没能登记，已跳过。"
  # Console.Recipe_Identifier_Failed：向控制台显示。
  Recipe_Identifier_Failed: "配方标识创建失败"
  # Console.Recipe_Initialize_Failed：向控制台显示。
  Recipe_Initialize_Failed: "配方接口初始化失败"
  # Console.Recipe_Remove_Failed：向控制台显示。
  Recipe_Remove_Failed: "配方移除失败"
  # Console.Recipe_Restart：向控制台显示。
  Recipe_Restart: "合成配方改了以后要重启服务器才生效。"
  # Console.Recipe_Shaped_Failed：向控制台显示。
  Recipe_Shaped_Failed: "有序配方创建失败"
  # Console.Recipe_Shapeless_Failed：向控制台显示。
  Recipe_Shapeless_Failed: "无序配方创建失败"
  # Console.Reloaded：向控制台显示。
  Reloaded: "配置已重新加载。"
  # Console.Sounds_Failed：向控制台显示。
  Sounds_Failed: "声音没能加载。"
  # Console.Version_Unparsed：向控制台显示。
  Version_Unparsed: "认不出服务端的版本号，先按 0.0.0 处理；各项适配会按功能实际能不能用来判断。"
  # Console.Weapons_Added：向控制台显示。
  Weapons_Added: "已生成默认武器。"
  # Console.Zoom_Failed：向控制台显示。
  Zoom_Failed: "开镜效果没能加载。"
```

## `Prefix` { #prefix }

```yaml title="lang/en_US.yml · Prefix"
# Prefix：向玩家显示。
Prefix: "§7░ §c[-§l¬§cº§lc§7§ls§7] §c- §7"
```
