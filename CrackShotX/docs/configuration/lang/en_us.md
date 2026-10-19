---
title: lang/en_US.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: lang/en_US.yml
source_version: 1.1.0
---

# lang/en_US.yml

文件：`lang/en_US.yml`。版本：`1.1.0`。

语言与界面文字。

## `Command.No_Permission` { #commandno_permission }

```yaml title="lang/en_US.yml · Command.No_Permission"
# 服主可在此修改消息；删除条目后，会使用内置英文文本。
# 保留 <name> 占位符；支持 & 颜色代码。

# /csx 命令发送者：没有权限
Command.No_Permission: "&c你没有使用这个命令的权限。"
```

## `Command.Unknown` { #commandunknown }

```yaml title="lang/en_US.yml · Command.Unknown"
# /csx 命令发送者：未知子命令
Command.Unknown: "&c没有这个子命令。可以用的有：/csx、/csx reload、/csx panel、/csx give、/csx revoke、/csx history"
```

## `Command.Reloaded` { #commandreloaded }

```yaml title="lang/en_US.yml · Command.Reloaded"
# /csx reload 命令发送者：已重载
Command.Reloaded: "&a配置已重新加载。"
```

## `Command.Header` { #commandheader }

```yaml title="lang/en_US.yml · Command.Header"
# /csx 命令发送者：状态信息的首行
Command.Header: "&6CrackShotX &f<version> &7（CrackShot <cs_version>，服务端 <mc_version>）"
```

## `Command.Status_Title` { #commandstatus_title }

```yaml title="lang/en_US.yml · Command.Status_Title"
# /csx 命令发送者：功能列表标题
Command.Status_Title: "&7功能状态："
```

## `Command.Status_Enabled` { #commandstatus_enabled }

```yaml title="lang/en_US.yml · Command.Status_Enabled"
# /csx 命令发送者：已启用的功能
Command.Status_Enabled: "&f- <module>：&a已启用<detail>"
```

## `Command.Status_Disabled` { #commandstatus_disabled }

```yaml title="lang/en_US.yml · Command.Status_Disabled"
# /csx 命令发送者：已关闭的功能及原因
Command.Status_Disabled: "&f- <module>：&7未启用。<reason>"
```

## `Module.Visual_Fix.Name` { #modulevisual_fixname }

```yaml title="lang/en_US.yml · Module.Visual_Fix.Name"
# /csx 与控制台：功能名称
Module.Visual_Fix.Name: "弹道视觉修复"
```

## `Module.Visual_Fix.Detail` { #modulevisual_fixdetail }

```yaml title="lang/en_US.yml · Module.Visual_Fix.Detail"
# /csx 与控制台：显示修正功能使用的数据包库
Module.Visual_Fix.Detail: "（使用 <library>）"
```

## `Reason.Disabled_In_Config` { #reasondisabled_in_config }

```yaml title="lang/en_US.yml · Reason.Disabled_In_Config"
# /csx 与控制台：功能未启用的原因（在 config.yml 中关闭）
Reason.Disabled_In_Config: "已在 config.yml 里关闭。"
```

## `Reason.No_Packet_Library` { #reasonno_packet_library }

```yaml title="lang/en_US.yml · Reason.No_Packet_Library"
# /csx 与控制台：功能未启用的原因（未安装数据包库）
Reason.No_Packet_Library: "没有检测到 PacketEvents 或 ProtocolLib，装上其中一个即可。"
```

## `Reason.Library_Not_Found` { #reasonlibrary_not_found }

```yaml title="lang/en_US.yml · Reason.Library_Not_Found"
# /csx 与控制台：功能未启用的原因（未安装配置指定的数据包库）
Reason.Library_Not_Found: "配置里指定了 <library>，但服务器没有装它。"
```

## `Reason.Protocol_Not_Affected` { #reasonprotocol_not_affected }

```yaml title="lang/en_US.yml · Reason.Protocol_Not_Affected"
# /csx 与控制台：功能未启用的原因（此服务端版本无需修正）
Reason.Protocol_Not_Affected: "这个版本的协议不会截断弹丸速度，不需要修复。"
```

## `Reason.Unknown_Version` { #reasonunknown_version }

```yaml title="lang/en_US.yml · Reason.Unknown_Version"
# /csx 与控制台：功能未启用的原因（无法识别服务端版本）
Reason.Unknown_Version: "认不出服务端的版本号，为避免改错包，没有启用。"
```

## `Reason.Failed` { #reasonfailed }

```yaml title="lang/en_US.yml · Reason.Failed"
# /csx 与控制台：功能未启用的原因（启动失败）
Reason.Failed: "启动失败，已停用。原因：<error>"
```

## `Console.Module_Enabled` { #consolemodule_enabled }

```yaml title="lang/en_US.yml · Console.Module_Enabled"
# 控制台：启动或重载时已启用某项功能
Console.Module_Enabled: "<module>：已启用<detail>"
```

## `Console.Module_Disabled` { #consolemodule_disabled }

```yaml title="lang/en_US.yml · Console.Module_Disabled"
# 控制台：启动或重载时某项功能仍未启用
Console.Module_Disabled: "<module>：未启用。<reason>"
```

## `Panel.Title` { #paneltitle }

```yaml title="lang/en_US.yml · Panel.Title"
# 面板：武器页面标题
Panel.Title: "枪械面板 <page>/<pages>"
```

## `Panel.Players_Title` { #panelplayers_title }

```yaml title="lang/en_US.yml · Panel.Players_Title"
# 面板：接收玩家页面标题
Panel.Players_Title: "发给谁 <page>/<pages>"
```

## `Panel.History_Title` { #panelhistory_title }

```yaml title="lang/en_US.yml · Panel.History_Title"
# 面板：历史记录页面标题
Panel.History_Title: "发放记录 <page>/<pages>"
```

## `Panel.Prev` { #panelprev }

```yaml title="lang/en_US.yml · Panel.Prev"
# 面板：翻页按钮
Panel.Prev: "&e上一页"
```

## `Panel.Next` { #panelnext }

```yaml title="lang/en_US.yml · Panel.Next"
# 面板：翻页按钮
Panel.Next: "&e下一页"
```

## `Panel.Category.Name` { #panelcategoryname }

```yaml title="lang/en_US.yml · Panel.Category.Name"
# 面板：分类按钮
Panel.Category.Name: "&e分类：&f<category>"
```

## `Panel.Category.All` { #panelcategoryall }

```yaml title="lang/en_US.yml · Panel.Category.All"
# 面板：分类按钮中的“全部”
Panel.Category.All: "全部"
```

## `Panel.Category.Lore` { #panelcategorylore }

```yaml title="lang/en_US.yml · Panel.Category.Lore"
# 面板：分类按钮提示
Panel.Category.Lore: "&7左键下一个，右键上一个"
```

## `Panel.Search.Name` { #panelsearchname }

```yaml title="lang/en_US.yml · Panel.Search.Name"
# 面板：搜索按钮
Panel.Search.Name: "&e搜索"
```

## `Panel.Search.Lore_Idle` { #panelsearchlore_idle }

```yaml title="lang/en_US.yml · Panel.Search.Lore_Idle"
# 面板：搜索按钮提示（未在搜索）
Panel.Search.Lore_Idle: "&7点一下，然后在聊天栏输入关键词"
```

## `Panel.Search.Lore_Active` { #panelsearchlore_active }

```yaml title="lang/en_US.yml · Panel.Search.Lore_Active"
# 面板：搜索按钮提示（正在搜索）
Panel.Search.Lore_Active: "&7正在找：&f<keyword>\n&7左键换一个词，右键清掉"
```

## `Panel.Target.Name` { #paneltargetname }

```yaml title="lang/en_US.yml · Panel.Target.Name"
# 面板：接收玩家按钮
Panel.Target.Name: "&e发给：&f<targets>"
```

## `Panel.Target.Self` { #paneltargetself }

```yaml title="lang/en_US.yml · Panel.Target.Self"
# 面板：接收玩家按钮中的“自己”
Panel.Target.Self: "自己"
```

## `Panel.Target.Many` { #paneltargetmany }

```yaml title="lang/en_US.yml · Panel.Target.Many"
# 面板：接收玩家按钮中的人数
Panel.Target.Many: "<count> 名玩家"
```

## `Panel.Target.Lore` { #paneltargetlore }

```yaml title="lang/en_US.yml · Panel.Target.Lore"
# 面板：接收玩家按钮提示
Panel.Target.Lore: "&7点一下选别的玩家"
```

## `Panel.Info.Name` { #panelinfoname }

```yaml title="lang/en_US.yml · Panel.Info.Name"
# 面板：武器数量
Panel.Info.Name: "&f共 <count> 把武器"
```

## `Panel.Multi.Name_On` { #panelmultiname_on }

```yaml title="lang/en_US.yml · Panel.Multi.Name_On"
# 面板：多选按钮（已开启）
Panel.Multi.Name_On: "&e多选：&a开"
```

## `Panel.Multi.Name_Off` { #panelmultiname_off }

```yaml title="lang/en_US.yml · Panel.Multi.Name_Off"
# 面板：多选按钮（已关闭）
Panel.Multi.Name_Off: "&e多选：&7关"
```

## `Panel.Multi.Lore` { #panelmultilore }

```yaml title="lang/en_US.yml · Panel.Multi.Lore"
# 面板：多选按钮提示
Panel.Multi.Lore: "&7打开以后，点武器是勾选，\n&7再点右边的按钮一起发"
```

## `Panel.Give_Selected` { #panelgive_selected }

```yaml title="lang/en_US.yml · Panel.Give_Selected"
# 面板：多选模式中的发放按钮
Panel.Give_Selected: "&a发放选中的 <count> 把"
```

## `Panel.Revoke.Name` { #panelrevokename }

```yaml title="lang/en_US.yml · Panel.Revoke.Name"
# 面板：撤回按钮
Panel.Revoke.Name: "&c撤回上一次发放"
```

## `Panel.Revoke.Lore_Last` { #panelrevokelore_last }

```yaml title="lang/en_US.yml · Panel.Revoke.Lore_Last"
# 面板：撤回按钮提示（有可撤回的物品）
Panel.Revoke.Lore_Last: "&7<time> 发给 <targets> 的 <count> 件\n&7只收得回背包里还在的同种武器\n&7左键撤回，按住 Shift 点左键看全部记录"
```

## `Panel.Revoke.Lore_None` { #panelrevokelore_none }

```yaml title="lang/en_US.yml · Panel.Revoke.Lore_None"
# 面板：撤回按钮提示（尚未发放物品）
Panel.Revoke.Lore_None: "&7还没有发放过"
```

## `Panel.Weapon.Lore` { #panelweaponlore }

```yaml title="lang/en_US.yml · Panel.Weapon.Lore"
# 面板：武器图标提示
Panel.Weapon.Lore: "&8内部名：<weapon>\n&8文件：<file>\n&7左键拿一件，按住 Shift 点左键拿一组"
```

## `Panel.Weapon.Lore_Pick` { #panelweaponlore_pick }

```yaml title="lang/en_US.yml · Panel.Weapon.Lore_Pick"
# 面板：多选模式下的武器图标提示（未选中）
Panel.Weapon.Lore_Pick: "&7点一下勾选"
```

## `Panel.Weapon.Lore_Picked` { #panelweaponlore_picked }

```yaml title="lang/en_US.yml · Panel.Weapon.Lore_Picked"
# 面板：多选模式下的武器图标提示（已选中）
Panel.Weapon.Lore_Picked: "&a已勾选，再点一下取消"
```

## `Panel.Players.Self` { #panelplayersself }

```yaml title="lang/en_US.yml · Panel.Players.Self"
# 面板：接收玩家页面中的“仅自己”按钮
Panel.Players.Self: "&e只发给自己"
```

## `Panel.Players.Done` { #panelplayersdone }

```yaml title="lang/en_US.yml · Panel.Players.Done"
# 面板：接收玩家页面中的“完成”按钮
Panel.Players.Done: "&a选好了"
```

## `Panel.Players.Picked` { #panelplayerspicked }

```yaml title="lang/en_US.yml · Panel.Players.Picked"
# 面板：接收玩家页面中已选中的玩家
Panel.Players.Picked: "&a已选中，再点一下取消"
```

## `Panel.History.Entry` { #panelhistoryentry }

```yaml title="lang/en_US.yml · Panel.History.Entry"
# 面板：历史记录页面中的一条记录
Panel.History.Entry: "&f#<id> &7<time>"
```

## `Panel.History.Lore` { #panelhistorylore }

```yaml title="lang/en_US.yml · Panel.History.Lore"
# 面板：记录提示（可撤回）
Panel.History.Lore: "&7操作人：<admin>\n&7<summary>\n&7点一下撤回这一次"
```

## `Panel.History.Lore_Revoked` { #panelhistorylore_revoked }

```yaml title="lang/en_US.yml · Panel.History.Lore_Revoked"
# 面板：记录提示（已撤回）
Panel.History.Lore_Revoked: "&7操作人：<admin>\n&7<summary>\n&8已经撤回过了"
```

## `Panel.Search_Prompt` { #panelsearch_prompt }

```yaml title="lang/en_US.yml · Panel.Search_Prompt"
# 面板使用者：点击搜索后，等待输入关键词
Panel.Search_Prompt: "&e在聊天栏输入要找的关键词。输入 cancel 取消。"
```

## `Panel.Search_Cancelled` { #panelsearch_cancelled }

```yaml title="lang/en_US.yml · Panel.Search_Cancelled"
# 面板使用者：已取消搜索
Panel.Search_Cancelled: "&7没有搜索。"
```

## `Panel.Search_None` { #panelsearch_none }

```yaml title="lang/en_US.yml · Panel.Search_None"
# 面板使用者：未找到结果
Panel.Search_None: "&7没有找到名字里带\"<keyword>\"的武器。"
```

## `Panel.Given` { #panelgiven }

```yaml title="lang/en_US.yml · Panel.Given"
# 发放者：武器已发放
Panel.Given: "&a已发放 #<id>：<summary>"
```

## `Panel.Given_Partial` { #panelgiven_partial }

```yaml title="lang/en_US.yml · Panel.Given_Partial"
# 发放者：接收玩家的物品栏已满，只发放了部分物品
Panel.Given_Partial: "&e<player> 的背包放不下，<weapon> 只给了 <given> 件。"
```

## `Panel.Revoke_Confirm` { #panelrevoke_confirm }

```yaml title="lang/en_US.yml · Panel.Revoke_Confirm"
# 撤回者：再次点击确认
Panel.Revoke_Confirm: "&e再点一次，确认撤回 #<id>。"
```

## `Panel.Revoked` { #panelrevoked }

```yaml title="lang/en_US.yml · Panel.Revoked"
# 撤回者：撤回完成
Panel.Revoked: "&a已撤回 #<id>：应收 <expected> 件，实收 <actual> 件。"
```

## `Panel.Revoke_Offline` { #panelrevoke_offline }

```yaml title="lang/en_US.yml · Panel.Revoke_Offline"
# 撤回者：接收玩家已离线，未取回其物品
Panel.Revoke_Offline: "&7<player> 不在线，给这名玩家的 <count> 件没有收回。"
```

## `Panel.Revoke_None` { #panelrevoke_none }

```yaml title="lang/en_US.yml · Panel.Revoke_None"
# 撤回者：没有可撤回的物品
Panel.Revoke_None: "&7没有可以撤回的发放记录。"
```

## `Panel.Revoke_Done` { #panelrevoke_done }

```yaml title="lang/en_US.yml · Panel.Revoke_Done"
# 撤回者：此记录已撤回
Panel.Revoke_Done: "&7#<id> 已经撤回过了。"
```

## `Panel.Revoke_Not_Found` { #panelrevoke_not_found }

```yaml title="lang/en_US.yml · Panel.Revoke_Not_Found"
# 撤回者：没有此编号的记录
Panel.Revoke_Not_Found: "&c没有编号是 <id> 的发放记录。"
```

## `Panel.No_Weapon` { #panelno_weapon }

```yaml title="lang/en_US.yml · Panel.No_Weapon"
# 发放者：未知武器名称
Panel.No_Weapon: "&c没有叫 <weapon> 的武器。"
```

## `Panel.No_Player` { #panelno_player }

```yaml title="lang/en_US.yml · Panel.No_Player"
# 发放者：玩家不在线
Panel.No_Player: "&c玩家 <player> 不在线。"
```

## `Panel.No_Others` { #panelno_others }

```yaml title="lang/en_US.yml · Panel.No_Others"
# 发放者：没有向其他玩家发放物品的权限
Panel.No_Others: "&c你只能发给自己。"
```

## `Panel.Players_Only` { #panelplayers_only }

```yaml title="lang/en_US.yml · Panel.Players_Only"
# 控制台：执行了 /csx panel 等仅限玩家的命令
Panel.Players_Only: "&c这个命令只能由玩家使用。"
```

## `Panel.History_Line` { #panelhistory_line }

```yaml title="lang/en_US.yml · Panel.History_Line"
# /csx history 命令发送者：一条记录
Panel.History_Line: "&f#<id> &7<time> &f<admin> &7→ <summary><revoked>"
```

## `Panel.History_Revoked` { #panelhistory_revoked }

```yaml title="lang/en_US.yml · Panel.History_Revoked"
# /csx history 命令发送者：记录后面的“已撤回”标记
Panel.History_Revoked: " &8（已撤回）"
```

## `Panel.History_Empty` { #panelhistory_empty }

```yaml title="lang/en_US.yml · Panel.History_Empty"
# /csx history 命令发送者：暂无记录
Panel.History_Empty: "&7还没有发放记录。"
```

## `Module.Panel.Name` { #modulepanelname }

```yaml title="lang/en_US.yml · Module.Panel.Name"
# /csx 与控制台：功能名称
Module.Panel.Name: "管理员枪械面板"
```

## `Panel.Log.Give` { #panelloggive }

```yaml title="lang/en_US.yml · Panel.Log.Give"
# 历史记录与审计日志：“发放”操作
Panel.Log.Give: "发放"
```

## `Panel.Log.Revoke` { #panellogrevoke }

```yaml title="lang/en_US.yml · Panel.Log.Revoke"
# 历史记录与审计日志：“撤回”操作
Panel.Log.Revoke: "撤回"
```

## `Panel.Log.Console` { #panellogconsole }

```yaml title="lang/en_US.yml · Panel.Log.Console"
# 历史记录与审计日志：操作人为控制台
Panel.Log.Console: "控制台"
```

## `Panel.Log.Many` { #panellogmany }

```yaml title="lang/en_US.yml · Panel.Log.Many"
# 历史记录与审计日志：接收玩家较多时显示“及其他 N 人”
Panel.Log.Many: "等 <count> 人"
```

## `Panel.Usage_Give` { #panelusage_give }

```yaml title="lang/en_US.yml · Panel.Usage_Give"
# /csx give 命令发送者：用法错误
Panel.Usage_Give: "&c用法：/csx give <players> <weapons> [amount]。多个名称用英文逗号分隔；* 表示全部在线玩家。"
```

## `Panel.Usage_Revoke` { #panelusage_revoke }

```yaml title="lang/en_US.yml · Panel.Usage_Revoke"
# /csx revoke 命令发送者：用法错误
Panel.Usage_Revoke: "&c用法：/csx revoke [编号]"
```

## `Panel.Usage_History` { #panelusage_history }

```yaml title="lang/en_US.yml · Panel.Usage_History"
# /csx history 命令发送者：用法错误
Panel.Usage_History: "&c用法：/csx history [页]"
```

## `Console.Panel_Write_Failed` { #consolepanel_write_failed }

```yaml title="lang/en_US.yml · Console.Panel_Write_Failed"
# 控制台：历史记录或审计日志写入失败
Console.Panel_Write_Failed: "发放记录或审计日志写入失败：<error>"
```

## `Module.MythicMobs.Name` { #modulemythicmobsname }

```yaml title="lang/en_US.yml · Module.MythicMobs.Name"
# /csx 与控制台：功能名称
Module.MythicMobs.Name: "MythicMobs 怪物对接"
```

## `Module.MythicMobs.Detail` { #modulemythicmobsdetail }

```yaml title="lang/en_US.yml · Module.MythicMobs.Detail"
# /csx 与控制台：当前使用的 MythicMobs 版本
Module.MythicMobs.Detail: " (MythicMobs <version>)"
```

## `MythicMobs.Unknown_Weapon` { #mythicmobsunknown_weapon }

```yaml title="lang/en_US.yml · MythicMobs.Unknown_Weapon"
# 控制台：生物掉落配置指定了不存在的武器
MythicMobs.Unknown_Weapon: "<where> 的掉落里写了 CrackShot 武器 <weapon>，但没有这把武器，这一行不会掉东西。"
```

## `MythicMobs.Bad_Multiplier` { #mythicmobsbad_multiplier }

```yaml title="lang/en_US.yml · MythicMobs.Bad_Multiplier"
# 控制台：生物的武器伤害倍率无效
MythicMobs.Bad_Multiplier: "怪物 <mob> 的 CrackShot.DamageMultiplier 写的是 <value>，不是有效的倍率，按 1 处理。"
```

## `Reason.Plugin_Not_Found` { #reasonplugin_not_found }

```yaml title="lang/en_US.yml · Reason.Plugin_Not_Found"
# /csx 与控制台：功能未启用的原因（未安装插件）
Reason.Plugin_Not_Found: "服务器没有装 <plugin>。"
```

## `Reason.Plugin_Version` { #reasonplugin_version }

```yaml title="lang/en_US.yml · Reason.Plugin_Version"
# /csx 与控制台：功能未启用的原因（插件版本不受支持）
Reason.Plugin_Version: "<plugin> 的版本是 <version>，对不上，没有启用。"
```

## `Reason.Mythic_Not_Registered` { #reasonmythic_not_registered }

```yaml title="lang/en_US.yml · Reason.Mythic_Not_Registered"
# /csx 与控制台：功能未启用的原因（未注册掉落与条件）
Reason.Mythic_Not_Registered: "掉落和条件还没登记上，多半是热加载插件造成的。执行一次 /mm reload 就好。"
```

## `Module.AttributePlus.Name` { #moduleattributeplusname }

```yaml title="lang/en_US.yml · Module.AttributePlus.Name"
# /csx 与控制台：功能名称
Module.AttributePlus.Name: "AttributePlus 属性对接"
```

## `Module.AttributePlus.Detail` { #moduleattributeplusdetail }

```yaml title="lang/en_US.yml · Module.AttributePlus.Detail"
# /csx 与控制台：当前使用的 AttributePlus 版本
Module.AttributePlus.Detail: "(AttributePlus <version>)"
```

## `AttributePlus.Version_Untested` { #attributeplusversion_untested }

```yaml title="lang/en_US.yml · AttributePlus.Version_Untested"
# 控制台：未经测试的 AttributePlus 版本
AttributePlus.Version_Untested: "这个版本的 AttributePlus（<version>）没有验证过，属性对接没有启用。验证过的版本是 <tested>。"
```

## `AttributePlus.Internal_Changed` { #attributeplusinternal_changed }

```yaml title="lang/en_US.yml · AttributePlus.Internal_Changed"
# 控制台：AttributePlus 内部结构发生变化
AttributePlus.Internal_Changed: "AttributePlus 内部的接口和预期的不一样，属性对接已停用。武器伤害照 CrackShot 自己的算。"
```

## `Module.NeigeItems.Name` { #moduleneigeitemsname }

```yaml title="lang/en_US.yml · Module.NeigeItems.Name"
# /csx 与控制台：功能名称
Module.NeigeItems.Name: "NeigeItems 物品对接"
```

## `Module.NeigeItems.Detail` { #moduleneigeitemsdetail }

```yaml title="lang/en_US.yml · Module.NeigeItems.Detail"
# /csx 与控制台：NeigeItems 版本及绑定的枪械和弹药数量
Module.NeigeItems.Detail: "（NeigeItems <version>，<weapons> 种枪，<ammo> 种弹药）"
```

## `NeigeItems.Unknown_Item` { #neigeitemsunknown_item }

```yaml title="lang/en_US.yml · NeigeItems.Unknown_Item"
# 控制台：绑定指定的物品不存在
NeigeItems.Unknown_Item: "config.yml 的 NeigeItems.<section> 里写了物品 <item>，NeigeItems 里没有这件物品，这一行不生效。"
```

## `NeigeItems.Unknown_Weapon` { #neigeitemsunknown_weapon }

```yaml title="lang/en_US.yml · NeigeItems.Unknown_Weapon"
# 控制台：绑定指定的武器不存在
NeigeItems.Unknown_Weapon: "config.yml 的 NeigeItems.<section> 里写了武器 <weapon>，CrackShot 里没有这把武器，这一行不生效。"
```

## `NeigeItems.Duplicate_Item` { #neigeitemsduplicate_item }

```yaml title="lang/en_US.yml · NeigeItems.Duplicate_Item"
# 控制台：同一物品被重复绑定
NeigeItems.Duplicate_Item: "物品 <item> 在 NeigeItems.Weapons 里写了不止一次，用第一次写的 <weapon>。"
```

## `Module.PlaceholderAPI.Name` { #moduleplaceholderapiname }

```yaml title="lang/en_US.yml · Module.PlaceholderAPI.Name"
# /csx 与控制台：功能名称
Module.PlaceholderAPI.Name: "PlaceholderAPI 变量"
```

## `Module.WorldGuard.Name` { #moduleworldguardname }

```yaml title="lang/en_US.yml · Module.WorldGuard.Name"
# /csx 与控制台：功能名称
Module.WorldGuard.Name: "WorldGuard 区域限制"
```

## `Module.WorldGuard.Detail` { #moduleworldguarddetail }

```yaml title="lang/en_US.yml · Module.WorldGuard.Detail"
# /csx 与控制台：当前使用的 WorldGuard 版本
Module.WorldGuard.Detail: " (WorldGuard <version>)"
```

## `Region.Shoot_Denied` { #regionshoot_denied }

```yaml title="lang/en_US.yml · Region.Shoot_Denied"
# 玩家：在禁止射击的区域内开枪
Region.Shoot_Denied: "&c这里不能开枪。"
```

## `Region.Weapon_Denied` { #regionweapon_denied }

```yaml title="lang/en_US.yml · Region.Weapon_Denied"
# 玩家：使用此区域不允许的武器
Region.Weapon_Denied: "&c这里不能用<weapon>。"
```

## `Region.Place_Denied` { #regionplace_denied }

```yaml title="lang/en_US.yml · Region.Place_Denied"
# 玩家：在禁止放置的区域内放置地雷或 C4
Region.Place_Denied: "&c这里不能放置爆炸物。"
```

## `Console.Language_Invalid` { #consolelanguage_invalid }

```yaml title="lang/en_US.yml · Console.Language_Invalid"
# 控制台：config.yml 中的 Language 无效
Console.Language_Invalid: "config.yml 的 Language 写的是 <value>，只认 zh_CN 和 en_US，先按 zh_CN 处理。"
```

## `Console.Config_Failed_Startup` { #consoleconfig_failed_startup }

```yaml title="lang/en_US.yml · Console.Config_Failed_Startup"
# 控制台：启动时无法读取 config.yml
Console.Config_Failed_Startup: "<file> 读不出来，先按默认设置启动。原因：<error>"
```

## `Console.Config_Failed_Reload` { #consoleconfig_failed_reload }

```yaml title="lang/en_US.yml · Console.Config_Failed_Reload"
# 控制台：重载时无法读取 config.yml
Console.Config_Failed_Reload: "<file> 读不出来，继续用原来的设置。原因：<error>"
```

## `Command.Reload_Failed` { #commandreload_failed }

```yaml title="lang/en_US.yml · Command.Reload_Failed"
# /csx reload 命令发送者：配置无法读取，未重载
Command.Reload_Failed: "&c配置文件读不出来，没有重新加载，原因见控制台。"
```

## `Reason.Unknown_Library` { #reasonunknown_library }

```yaml title="lang/en_US.yml · Reason.Unknown_Library"
# /csx 与控制台：功能未启用的原因（config.yml 中的数据包库未知）
Reason.Unknown_Library: "config.yml 的 Visual_Fix.Packet_Library 写的是 <library>，只认 auto、PacketEvents、ProtocolLib。"
```

## `Reason.Placeholder_Taken` { #reasonplaceholder_taken }

```yaml title="lang/en_US.yml · Reason.Placeholder_Taken"
# /csx 与控制台：功能未启用的原因（占位符前缀已被占用）
Reason.Placeholder_Taken: "已经有别的插件注册了 crackshot 这组变量，没有启用。"
```

## `Reason.Flags_Not_Registered` { #reasonflags_not_registered }

```yaml title="lang/en_US.yml · Reason.Flags_Not_Registered"
# /csx 与控制台：功能未启用的原因（未注册区域标志）
Reason.Flags_Not_Registered: "区域标志没能在 WorldGuard 启动前注册上，区域限制没有启用。请完整重启服务器，不要用热加载插件的工具加载 CrackShotX。"
```

## `Reason.Flag_Conflict` { #reasonflag_conflict }

```yaml title="lang/en_US.yml · Reason.Flag_Conflict"
# /csx 与控制台：功能未启用的原因（同名区域标志已存在）
Reason.Flag_Conflict: "WorldGuard 里已经有一个同名的区域标志 <flag>，类型对不上，可能是别的插件注册的。区域限制没有启用。"
```

## `NeigeItems.Version_Untested` { #neigeitemsversion_untested }

```yaml title="lang/en_US.yml · NeigeItems.Version_Untested"
# 控制台：未经测试的 NeigeItems 版本
NeigeItems.Version_Untested: "NeigeItems <version> 没有验证过（验证过的是 <tested>），对接照常启用。如果枪或弹药表现不对，先换回 <tested> 试试。"
```
