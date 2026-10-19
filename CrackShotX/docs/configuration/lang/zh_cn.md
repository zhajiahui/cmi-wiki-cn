---
title: lang/zh_CN.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: lang/zh_CN.yml
source_version: 1.1.0
---

# lang/zh_CN.yml

文件：`lang/zh_CN.yml`。版本：`1.1.0`。

语言与界面文字。

## `Command.No_Permission` { #commandno_permission }

```yaml title="lang/zh_CN.yml · Command.No_Permission"
# CrackShotX 的中文文字。服主可以直接改这里；删掉的条目会用插件自带的中文。
# 尖括号里的 <名称> 会换成实际内容，照原样保留；可以用 & 颜色代码。

# 执行 /csx 的人：没有权限
Command.No_Permission: "&c你没有使用这个命令的权限。"
```

## `Command.Unknown` { #commandunknown }

```yaml title="lang/zh_CN.yml · Command.Unknown"
# 执行 /csx 的人：子命令写错
Command.Unknown: "&c没有这个子命令。可以用的有：/csx、/csx reload、/csx panel、/csx give、/csx revoke、/csx history"
```

## `Command.Reloaded` { #commandreloaded }

```yaml title="lang/zh_CN.yml · Command.Reloaded"
# 执行 /csx reload 的人：重载成功
Command.Reloaded: "&a配置已重新加载。"
```

## `Command.Header` { #commandheader }

```yaml title="lang/zh_CN.yml · Command.Header"
# 执行 /csx 的人：状态的第一行
Command.Header: "&6CrackShotX &f<version> &7（CrackShot <cs_version>，服务端 <mc_version>）"
```

## `Command.Status_Title` { #commandstatus_title }

```yaml title="lang/zh_CN.yml · Command.Status_Title"
# 执行 /csx 的人：功能列表的标题
Command.Status_Title: "&7功能状态："
```

## `Command.Status_Enabled` { #commandstatus_enabled }

```yaml title="lang/zh_CN.yml · Command.Status_Enabled"
# 执行 /csx 的人：已启用的功能
Command.Status_Enabled: "&f- <module>：&a已启用<detail>"
```

## `Command.Status_Disabled` { #commandstatus_disabled }

```yaml title="lang/zh_CN.yml · Command.Status_Disabled"
# 执行 /csx 的人：没启用的功能和原因
Command.Status_Disabled: "&f- <module>：&7未启用。<reason>"
```

## `Module.Visual_Fix.Name` { #modulevisual_fixname }

```yaml title="lang/zh_CN.yml · Module.Visual_Fix.Name"
# /csx 和控制台：功能名
Module.Visual_Fix.Name: "弹道视觉修复"
```

## `Module.Visual_Fix.Detail` { #modulevisual_fixdetail }

```yaml title="lang/zh_CN.yml · Module.Visual_Fix.Detail"
# /csx 和控制台：弹道视觉修复用的是哪个发包库
Module.Visual_Fix.Detail: "（使用 <library>）"
```

## `Reason.Disabled_In_Config` { #reasondisabled_in_config }

```yaml title="lang/zh_CN.yml · Reason.Disabled_In_Config"
# /csx 和控制台：没启用的原因（config.yml 里关了）
Reason.Disabled_In_Config: "已在 config.yml 里关闭。"
```

## `Reason.No_Packet_Library` { #reasonno_packet_library }

```yaml title="lang/zh_CN.yml · Reason.No_Packet_Library"
# /csx 和控制台：没启用的原因（没装发包库）
Reason.No_Packet_Library: "没有检测到 PacketEvents 或 ProtocolLib，装上其中一个即可。"
```

## `Reason.Library_Not_Found` { #reasonlibrary_not_found }

```yaml title="lang/zh_CN.yml · Reason.Library_Not_Found"
# /csx 和控制台：没启用的原因（指定的发包库没装）
Reason.Library_Not_Found: "配置里指定了 <library>，但服务器没有装它。"
```

## `Reason.Protocol_Not_Affected` { #reasonprotocol_not_affected }

```yaml title="lang/zh_CN.yml · Reason.Protocol_Not_Affected"
# /csx 和控制台：没启用的原因（这个服务端版本用不着修）
Reason.Protocol_Not_Affected: "这个版本的协议不会截断弹丸速度，不需要修复。"
```

## `Reason.Unknown_Version` { #reasonunknown_version }

```yaml title="lang/zh_CN.yml · Reason.Unknown_Version"
# /csx 和控制台：没启用的原因（认不出服务端版本）
Reason.Unknown_Version: "认不出服务端的版本号，为避免改错包，没有启用。"
```

## `Reason.Failed` { #reasonfailed }

```yaml title="lang/zh_CN.yml · Reason.Failed"
# /csx 和控制台：没启用的原因（启动时出错）
Reason.Failed: "启动失败，已停用。原因：<error>"
```

## `Console.Module_Enabled` { #consolemodule_enabled }

```yaml title="lang/zh_CN.yml · Console.Module_Enabled"
# 控制台：启动或重载时，一个功能启用了
Console.Module_Enabled: "<module>：已启用<detail>"
```

## `Console.Module_Disabled` { #consolemodule_disabled }

```yaml title="lang/zh_CN.yml · Console.Module_Disabled"
# 控制台：启动或重载时，一个功能没启用
Console.Module_Disabled: "<module>：未启用。<reason>"
```

## `Panel.Title` { #paneltitle }

```yaml title="lang/zh_CN.yml · Panel.Title"
# 面板：武器页的标题
Panel.Title: "枪械面板 <page>/<pages>"
```

## `Panel.Players_Title` { #panelplayers_title }

```yaml title="lang/zh_CN.yml · Panel.Players_Title"
# 面板：选发给谁那一页的标题
Panel.Players_Title: "发给谁 <page>/<pages>"
```

## `Panel.History_Title` { #panelhistory_title }

```yaml title="lang/zh_CN.yml · Panel.History_Title"
# 面板：发放记录页的标题
Panel.History_Title: "发放记录 <page>/<pages>"
```

## `Panel.Prev` { #panelprev }

```yaml title="lang/zh_CN.yml · Panel.Prev"
# 面板：翻页按钮
Panel.Prev: "&e上一页"
```

## `Panel.Next` { #panelnext }

```yaml title="lang/zh_CN.yml · Panel.Next"
# 面板：翻页按钮
Panel.Next: "&e下一页"
```

## `Panel.Category.Name` { #panelcategoryname }

```yaml title="lang/zh_CN.yml · Panel.Category.Name"
# 面板：分类按钮
Panel.Category.Name: "&e分类：&f<category>"
```

## `Panel.Category.All` { #panelcategoryall }

```yaml title="lang/zh_CN.yml · Panel.Category.All"
# 面板：分类按钮上的"全部"
Panel.Category.All: "全部"
```

## `Panel.Category.Lore` { #panelcategorylore }

```yaml title="lang/zh_CN.yml · Panel.Category.Lore"
# 面板：分类按钮的说明
Panel.Category.Lore: "&7左键下一个，右键上一个"
```

## `Panel.Search.Name` { #panelsearchname }

```yaml title="lang/zh_CN.yml · Panel.Search.Name"
# 面板：搜索按钮
Panel.Search.Name: "&e搜索"
```

## `Panel.Search.Lore_Idle` { #panelsearchlore_idle }

```yaml title="lang/zh_CN.yml · Panel.Search.Lore_Idle"
# 面板：搜索按钮的说明（还没搜）
Panel.Search.Lore_Idle: "&7点一下，然后在聊天栏输入关键词"
```

## `Panel.Search.Lore_Active` { #panelsearchlore_active }

```yaml title="lang/zh_CN.yml · Panel.Search.Lore_Active"
# 面板：搜索按钮的说明（正在搜）
Panel.Search.Lore_Active: "&7正在找：&f<keyword>\n&7左键换一个词，右键清掉"
```

## `Panel.Target.Name` { #paneltargetname }

```yaml title="lang/zh_CN.yml · Panel.Target.Name"
# 面板：发给谁按钮
Panel.Target.Name: "&e发给：&f<targets>"
```

## `Panel.Target.Self` { #paneltargetself }

```yaml title="lang/zh_CN.yml · Panel.Target.Self"
# 面板：发给谁按钮上的"自己"
Panel.Target.Self: "自己"
```

## `Panel.Target.Many` { #paneltargetmany }

```yaml title="lang/zh_CN.yml · Panel.Target.Many"
# 面板：发给谁按钮上的人数
Panel.Target.Many: "<count> 名玩家"
```

## `Panel.Target.Lore` { #paneltargetlore }

```yaml title="lang/zh_CN.yml · Panel.Target.Lore"
# 面板：发给谁按钮的说明
Panel.Target.Lore: "&7点一下选别的玩家"
```

## `Panel.Info.Name` { #panelinfoname }

```yaml title="lang/zh_CN.yml · Panel.Info.Name"
# 面板：武器总数
Panel.Info.Name: "&f共 <count> 把武器"
```

## `Panel.Multi.Name_On` { #panelmultiname_on }

```yaml title="lang/zh_CN.yml · Panel.Multi.Name_On"
# 面板：多选按钮（开）
Panel.Multi.Name_On: "&e多选：&a开"
```

## `Panel.Multi.Name_Off` { #panelmultiname_off }

```yaml title="lang/zh_CN.yml · Panel.Multi.Name_Off"
# 面板：多选按钮（关）
Panel.Multi.Name_Off: "&e多选：&7关"
```

## `Panel.Multi.Lore` { #panelmultilore }

```yaml title="lang/zh_CN.yml · Panel.Multi.Lore"
# 面板：多选按钮的说明
Panel.Multi.Lore: "&7打开以后，点武器是勾选，\n&7再点右边的按钮一起发"
```

## `Panel.Give_Selected` { #panelgive_selected }

```yaml title="lang/zh_CN.yml · Panel.Give_Selected"
# 面板：多选时一起发的按钮
Panel.Give_Selected: "&a发放选中的 <count> 把"
```

## `Panel.Revoke.Name` { #panelrevokename }

```yaml title="lang/zh_CN.yml · Panel.Revoke.Name"
# 面板：撤回按钮
Panel.Revoke.Name: "&c撤回上一次发放"
```

## `Panel.Revoke.Lore_Last` { #panelrevokelore_last }

```yaml title="lang/zh_CN.yml · Panel.Revoke.Lore_Last"
# 面板：撤回按钮的说明（有能撤回的）
Panel.Revoke.Lore_Last: "&7<time> 发给 <targets> 的 <count> 件\n&7只收得回背包里还在的同种武器\n&7左键撤回，按住 Shift 点左键看全部记录"
```

## `Panel.Revoke.Lore_None` { #panelrevokelore_none }

```yaml title="lang/zh_CN.yml · Panel.Revoke.Lore_None"
# 面板：撤回按钮的说明（还没发过）
Panel.Revoke.Lore_None: "&7还没有发放过"
```

## `Panel.Weapon.Lore` { #panelweaponlore }

```yaml title="lang/zh_CN.yml · Panel.Weapon.Lore"
# 面板：武器图标的说明
Panel.Weapon.Lore: "&8内部名：<weapon>\n&8文件：<file>\n&7左键拿一件，按住 Shift 点左键拿一组"
```

## `Panel.Weapon.Lore_Pick` { #panelweaponlore_pick }

```yaml title="lang/zh_CN.yml · Panel.Weapon.Lore_Pick"
# 面板：多选时武器图标的说明（没勾）
Panel.Weapon.Lore_Pick: "&7点一下勾选"
```

## `Panel.Weapon.Lore_Picked` { #panelweaponlore_picked }

```yaml title="lang/zh_CN.yml · Panel.Weapon.Lore_Picked"
# 面板：多选时武器图标的说明（已勾）
Panel.Weapon.Lore_Picked: "&a已勾选，再点一下取消"
```

## `Panel.Players.Self` { #panelplayersself }

```yaml title="lang/zh_CN.yml · Panel.Players.Self"
# 面板：选人页的"只发给自己"按钮
Panel.Players.Self: "&e只发给自己"
```

## `Panel.Players.Done` { #panelplayersdone }

```yaml title="lang/zh_CN.yml · Panel.Players.Done"
# 面板：选人页的"选好了"按钮
Panel.Players.Done: "&a选好了"
```

## `Panel.Players.Picked` { #panelplayerspicked }

```yaml title="lang/zh_CN.yml · Panel.Players.Picked"
# 面板：选人页里已选中的玩家
Panel.Players.Picked: "&a已选中，再点一下取消"
```

## `Panel.History.Entry` { #panelhistoryentry }

```yaml title="lang/zh_CN.yml · Panel.History.Entry"
# 面板：发放记录页的一条记录
Panel.History.Entry: "&f#<id> &7<time>"
```

## `Panel.History.Lore` { #panelhistorylore }

```yaml title="lang/zh_CN.yml · Panel.History.Lore"
# 面板：一条记录的说明（还能撤回）
Panel.History.Lore: "&7操作人：<admin>\n&7<summary>\n&7点一下撤回这一次"
```

## `Panel.History.Lore_Revoked` { #panelhistorylore_revoked }

```yaml title="lang/zh_CN.yml · Panel.History.Lore_Revoked"
# 面板：一条记录的说明（已经撤回）
Panel.History.Lore_Revoked: "&7操作人：<admin>\n&7<summary>\n&8已经撤回过了"
```

## `Panel.Search_Prompt` { #panelsearch_prompt }

```yaml title="lang/zh_CN.yml · Panel.Search_Prompt"
# 用面板的人：点了搜索，等着输入关键词
Panel.Search_Prompt: "&e在聊天栏输入要找的关键词。输入 cancel 取消。"
```

## `Panel.Search_Cancelled` { #panelsearch_cancelled }

```yaml title="lang/zh_CN.yml · Panel.Search_Cancelled"
# 用面板的人：没有搜索
Panel.Search_Cancelled: "&7没有搜索。"
```

## `Panel.Search_None` { #panelsearch_none }

```yaml title="lang/zh_CN.yml · Panel.Search_None"
# 用面板的人：没搜到
Panel.Search_None: "&7没有找到名字里带\"<keyword>\"的武器。"
```

## `Panel.Given` { #panelgiven }

```yaml title="lang/zh_CN.yml · Panel.Given"
# 发枪的人：发出去了
Panel.Given: "&a已发放 #<id>：<summary>"
```

## `Panel.Given_Partial` { #panelgiven_partial }

```yaml title="lang/zh_CN.yml · Panel.Given_Partial"
# 发枪的人：对方背包放不下，只给了一部分
Panel.Given_Partial: "&e<player> 的背包放不下，<weapon> 只给了 <given> 件。"
```

## `Panel.Revoke_Confirm` { #panelrevoke_confirm }

```yaml title="lang/zh_CN.yml · Panel.Revoke_Confirm"
# 撤回的人：再点一次确认
Panel.Revoke_Confirm: "&e再点一次，确认撤回 #<id>。"
```

## `Panel.Revoked` { #panelrevoked }

```yaml title="lang/zh_CN.yml · Panel.Revoked"
# 撤回的人：撤回完成
Panel.Revoked: "&a已撤回 #<id>：应收 <expected> 件，实收 <actual> 件。"
```

## `Panel.Revoke_Offline` { #panelrevoke_offline }

```yaml title="lang/zh_CN.yml · Panel.Revoke_Offline"
# 撤回的人：对方不在线，给这名玩家的那份没收回
Panel.Revoke_Offline: "&7<player> 不在线，给这名玩家的 <count> 件没有收回。"
```

## `Panel.Revoke_None` { #panelrevoke_none }

```yaml title="lang/zh_CN.yml · Panel.Revoke_None"
# 撤回的人：没有能撤回的记录
Panel.Revoke_None: "&7没有可以撤回的发放记录。"
```

## `Panel.Revoke_Done` { #panelrevoke_done }

```yaml title="lang/zh_CN.yml · Panel.Revoke_Done"
# 撤回的人：这一次已经撤回过
Panel.Revoke_Done: "&7#<id> 已经撤回过了。"
```

## `Panel.Revoke_Not_Found` { #panelrevoke_not_found }

```yaml title="lang/zh_CN.yml · Panel.Revoke_Not_Found"
# 撤回的人：编号写错
Panel.Revoke_Not_Found: "&c没有编号是 <id> 的发放记录。"
```

## `Panel.No_Weapon` { #panelno_weapon }

```yaml title="lang/zh_CN.yml · Panel.No_Weapon"
# 发枪的人：武器名写错
Panel.No_Weapon: "&c没有叫 <weapon> 的武器。"
```

## `Panel.No_Player` { #panelno_player }

```yaml title="lang/zh_CN.yml · Panel.No_Player"
# 发枪的人：玩家不在线
Panel.No_Player: "&c玩家 <player> 不在线。"
```

## `Panel.No_Others` { #panelno_others }

```yaml title="lang/zh_CN.yml · Panel.No_Others"
# 发枪的人：没有发给别人的权限
Panel.No_Others: "&c你只能发给自己。"
```

## `Panel.Players_Only` { #panelplayers_only }

```yaml title="lang/zh_CN.yml · Panel.Players_Only"
# 控制台：执行了只有玩家能用的命令（比如 /csx panel）
Panel.Players_Only: "&c这个命令只能由玩家使用。"
```

## `Panel.History_Line` { #panelhistory_line }

```yaml title="lang/zh_CN.yml · Panel.History_Line"
# 执行 /csx history 的人：一条记录
Panel.History_Line: "&f#<id> &7<time> &f<admin> &7→ <summary><revoked>"
```

## `Panel.History_Revoked` { #panelhistory_revoked }

```yaml title="lang/zh_CN.yml · Panel.History_Revoked"
# 执行 /csx history 的人：记录后面的"已撤回"
Panel.History_Revoked: " &8（已撤回）"
```

## `Panel.History_Empty` { #panelhistory_empty }

```yaml title="lang/zh_CN.yml · Panel.History_Empty"
# 执行 /csx history 的人：还没有记录
Panel.History_Empty: "&7还没有发放记录。"
```

## `Module.Panel.Name` { #modulepanelname }

```yaml title="lang/zh_CN.yml · Module.Panel.Name"
# /csx 和控制台：功能名
Module.Panel.Name: "管理员枪械面板"
```

## `Panel.Log.Give` { #panelloggive }

```yaml title="lang/zh_CN.yml · Panel.Log.Give"
# 发放记录和审计日志：操作是"发放"
Panel.Log.Give: "发放"
```

## `Panel.Log.Revoke` { #panellogrevoke }

```yaml title="lang/zh_CN.yml · Panel.Log.Revoke"
# 发放记录和审计日志：操作是"撤回"
Panel.Log.Revoke: "撤回"
```

## `Panel.Log.Console` { #panellogconsole }

```yaml title="lang/zh_CN.yml · Panel.Log.Console"
# 发放记录和审计日志：操作人是控制台
Panel.Log.Console: "控制台"
```

## `Panel.Log.Many` { #panellogmany }

```yaml title="lang/zh_CN.yml · Panel.Log.Many"
# 发放记录和审计日志：发给很多人时的"等几人"
Panel.Log.Many: "等 <count> 人"
```

## `Panel.Usage_Give` { #panelusage_give }

```yaml title="lang/zh_CN.yml · Panel.Usage_Give"
# 执行 /csx give 的人：写法不对
Panel.Usage_Give: "&c用法：/csx give <玩家> <武器> [数量]。玩家和武器都可以写多个，用英文逗号隔开；玩家写 * 表示所有在线玩家。"
```

## `Panel.Usage_Revoke` { #panelusage_revoke }

```yaml title="lang/zh_CN.yml · Panel.Usage_Revoke"
# 执行 /csx revoke 的人：写法不对
Panel.Usage_Revoke: "&c用法：/csx revoke [编号]"
```

## `Panel.Usage_History` { #panelusage_history }

```yaml title="lang/zh_CN.yml · Panel.Usage_History"
# 执行 /csx history 的人：写法不对
Panel.Usage_History: "&c用法：/csx history [页]"
```

## `Console.Panel_Write_Failed` { #consolepanel_write_failed }

```yaml title="lang/zh_CN.yml · Console.Panel_Write_Failed"
# 控制台：发放记录或审计日志写不进去
Console.Panel_Write_Failed: "发放记录或审计日志写入失败：<error>"
```

## `Module.MythicMobs.Name` { #modulemythicmobsname }

```yaml title="lang/zh_CN.yml · Module.MythicMobs.Name"
# /csx 和控制台：功能名
Module.MythicMobs.Name: "MythicMobs 怪物对接"
```

## `Module.MythicMobs.Detail` { #modulemythicmobsdetail }

```yaml title="lang/zh_CN.yml · Module.MythicMobs.Detail"
# /csx 和控制台：用的 MythicMobs 版本
Module.MythicMobs.Detail: "（MythicMobs <version>）"
```

## `MythicMobs.Unknown_Weapon` { #mythicmobsunknown_weapon }

```yaml title="lang/zh_CN.yml · MythicMobs.Unknown_Weapon"
# 控制台：怪物掉落里的武器名找不到
MythicMobs.Unknown_Weapon: "<where> 的掉落里写了 CrackShot 武器 <weapon>，但没有这把武器，这一行不会掉东西。"
```

## `MythicMobs.Bad_Multiplier` { #mythicmobsbad_multiplier }

```yaml title="lang/zh_CN.yml · MythicMobs.Bad_Multiplier"
# 控制台：怪物的武器伤害倍率写错
MythicMobs.Bad_Multiplier: "怪物 <mob> 的 CrackShot.DamageMultiplier 写的是 <value>，不是有效的倍率，按 1 处理。"
```

## `Reason.Plugin_Not_Found` { #reasonplugin_not_found }

```yaml title="lang/zh_CN.yml · Reason.Plugin_Not_Found"
# /csx 和控制台：没启用的原因（没装对应的插件）
Reason.Plugin_Not_Found: "服务器没有装 <plugin>。"
```

## `Reason.Plugin_Version` { #reasonplugin_version }

```yaml title="lang/zh_CN.yml · Reason.Plugin_Version"
# /csx 和控制台：没启用的原因（对应插件的版本不对）
Reason.Plugin_Version: "<plugin> 的版本是 <version>，对不上，没有启用。"
```

## `Reason.Mythic_Not_Registered` { #reasonmythic_not_registered }

```yaml title="lang/zh_CN.yml · Reason.Mythic_Not_Registered"
# /csx 和控制台：没启用的原因（掉落和条件没登记上）
Reason.Mythic_Not_Registered: "掉落和条件还没登记上，多半是热加载插件造成的。执行一次 /mm reload 就好。"
```

## `Module.AttributePlus.Name` { #moduleattributeplusname }

```yaml title="lang/zh_CN.yml · Module.AttributePlus.Name"
# /csx 和控制台：功能名
Module.AttributePlus.Name: "AttributePlus 属性对接"
```

## `Module.AttributePlus.Detail` { #moduleattributeplusdetail }

```yaml title="lang/zh_CN.yml · Module.AttributePlus.Detail"
# /csx 和控制台：用的 AttributePlus 版本
Module.AttributePlus.Detail: "（AttributePlus <version>）"
```

## `AttributePlus.Version_Untested` { #attributeplusversion_untested }

```yaml title="lang/zh_CN.yml · AttributePlus.Version_Untested"
# 控制台：AttributePlus 的版本没验证过
AttributePlus.Version_Untested: "这个版本的 AttributePlus（<version>）没有验证过，属性对接没有启用。验证过的版本是 <tested>。"
```

## `AttributePlus.Internal_Changed` { #attributeplusinternal_changed }

```yaml title="lang/zh_CN.yml · AttributePlus.Internal_Changed"
# 控制台：AttributePlus 内部的接口变了
AttributePlus.Internal_Changed: "AttributePlus 内部的接口和预期的不一样，属性对接已停用。武器伤害照 CrackShot 自己的算。"
```

## `Module.NeigeItems.Name` { #moduleneigeitemsname }

```yaml title="lang/zh_CN.yml · Module.NeigeItems.Name"
# /csx 和控制台：功能名
Module.NeigeItems.Name: "NeigeItems 物品对接"
```

## `Module.NeigeItems.Detail` { #moduleneigeitemsdetail }

```yaml title="lang/zh_CN.yml · Module.NeigeItems.Detail"
# /csx 和控制台：用的 NeigeItems 版本和绑定了几种枪、几种弹药
Module.NeigeItems.Detail: "（NeigeItems <version>，<weapons> 种枪，<ammo> 种弹药）"
```

## `NeigeItems.Unknown_Item` { #neigeitemsunknown_item }

```yaml title="lang/zh_CN.yml · NeigeItems.Unknown_Item"
# 控制台：绑定里的物品 ID 找不到
NeigeItems.Unknown_Item: "config.yml 的 NeigeItems.<section> 里写了物品 <item>，NeigeItems 里没有这件物品，这一行不生效。"
```

## `NeigeItems.Unknown_Weapon` { #neigeitemsunknown_weapon }

```yaml title="lang/zh_CN.yml · NeigeItems.Unknown_Weapon"
# 控制台：绑定里的武器名找不到
NeigeItems.Unknown_Weapon: "config.yml 的 NeigeItems.<section> 里写了武器 <weapon>，CrackShot 里没有这把武器，这一行不生效。"
```

## `NeigeItems.Duplicate_Item` { #neigeitemsduplicate_item }

```yaml title="lang/zh_CN.yml · NeigeItems.Duplicate_Item"
# 控制台：同一件物品绑了两次
NeigeItems.Duplicate_Item: "物品 <item> 在 NeigeItems.Weapons 里写了不止一次，用第一次写的 <weapon>。"
```

## `Module.PlaceholderAPI.Name` { #moduleplaceholderapiname }

```yaml title="lang/zh_CN.yml · Module.PlaceholderAPI.Name"
# /csx 和控制台：功能名
Module.PlaceholderAPI.Name: "PlaceholderAPI 变量"
```

## `Module.WorldGuard.Name` { #moduleworldguardname }

```yaml title="lang/zh_CN.yml · Module.WorldGuard.Name"
# /csx 和控制台：功能名
Module.WorldGuard.Name: "WorldGuard 区域限制"
```

## `Module.WorldGuard.Detail` { #moduleworldguarddetail }

```yaml title="lang/zh_CN.yml · Module.WorldGuard.Detail"
# /csx 和控制台：用的 WorldGuard 版本
Module.WorldGuard.Detail: "（WorldGuard <version>）"
```

## `Region.Shoot_Denied` { #regionshoot_denied }

```yaml title="lang/zh_CN.yml · Region.Shoot_Denied"
# 玩家：在禁枪的区域里开枪
Region.Shoot_Denied: "&c这里不能开枪。"
```

## `Region.Weapon_Denied` { #regionweapon_denied }

```yaml title="lang/zh_CN.yml · Region.Weapon_Denied"
# 玩家：在不让用这把枪的区域里开枪
Region.Weapon_Denied: "&c这里不能用<weapon>。"
```

## `Region.Place_Denied` { #regionplace_denied }

```yaml title="lang/zh_CN.yml · Region.Place_Denied"
# 玩家：在不让放的区域里放地雷或遥控炸药
Region.Place_Denied: "&c这里不能放置爆炸物。"
```

## `Console.Language_Invalid` { #consolelanguage_invalid }

```yaml title="lang/zh_CN.yml · Console.Language_Invalid"
# 控制台：config.yml 的 Language 写错
Console.Language_Invalid: "config.yml 的 Language 写的是 <value>，只认 zh_CN 和 en_US，先按 zh_CN 处理。"
```

## `Console.Config_Failed_Startup` { #consoleconfig_failed_startup }

```yaml title="lang/zh_CN.yml · Console.Config_Failed_Startup"
# 控制台：启动时 config.yml 读不出来
Console.Config_Failed_Startup: "<file> 读不出来，先按默认设置启动。原因：<error>"
```

## `Console.Config_Failed_Reload` { #consoleconfig_failed_reload }

```yaml title="lang/zh_CN.yml · Console.Config_Failed_Reload"
# 控制台：重载时 config.yml 读不出来
Console.Config_Failed_Reload: "<file> 读不出来，继续用原来的设置。原因：<error>"
```

## `Command.Reload_Failed` { #commandreload_failed }

```yaml title="lang/zh_CN.yml · Command.Reload_Failed"
# 执行 /csx reload 的人：配置读不出来，没有重载
Command.Reload_Failed: "&c配置文件读不出来，没有重新加载，原因见控制台。"
```

## `Reason.Unknown_Library` { #reasonunknown_library }

```yaml title="lang/zh_CN.yml · Reason.Unknown_Library"
# /csx 和控制台：没启用的原因（发包库写错）
Reason.Unknown_Library: "config.yml 的 Visual_Fix.Packet_Library 写的是 <library>，只认 auto、PacketEvents、ProtocolLib。"
```

## `Reason.Placeholder_Taken` { #reasonplaceholder_taken }

```yaml title="lang/zh_CN.yml · Reason.Placeholder_Taken"
# /csx 和控制台：没启用的原因（变量名被别的插件占了）
Reason.Placeholder_Taken: "已经有别的插件注册了 crackshot 这组变量，没有启用。"
```

## `Reason.Flags_Not_Registered` { #reasonflags_not_registered }

```yaml title="lang/zh_CN.yml · Reason.Flags_Not_Registered"
# /csx 和控制台：没启用的原因（区域标志没注册上）
Reason.Flags_Not_Registered: "区域标志没能在 WorldGuard 启动前注册上，区域限制没有启用。请完整重启服务器，不要用热加载插件的工具加载 CrackShotX。"
```

## `Reason.Flag_Conflict` { #reasonflag_conflict }

```yaml title="lang/zh_CN.yml · Reason.Flag_Conflict"
# /csx 和控制台：没启用的原因（区域标志重名）
Reason.Flag_Conflict: "WorldGuard 里已经有一个同名的区域标志 <flag>，类型对不上，可能是别的插件注册的。区域限制没有启用。"
```

## `NeigeItems.Version_Untested` { #neigeitemsversion_untested }

```yaml title="lang/zh_CN.yml · NeigeItems.Version_Untested"
# 控制台：NeigeItems 的版本没验证过
NeigeItems.Version_Untested: "NeigeItems <version> 没有验证过（验证过的是 <tested>），对接照常启用。如果枪或弹药表现不对，先换回 <tested> 试试。"
```
