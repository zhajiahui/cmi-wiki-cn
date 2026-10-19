---
title: 主配置（config.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: config.yml
---

# 主配置（config.yml）

文件：`plugins/CMI/config.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `Language`

\*\* 更多选项请查看 Settings 文件夹 \*\*

要使用的语言文件

## `LanguageDownload`

是否自动从 GitHub 仓库下载默认语言文件<br>
如果使用 EN，或已配置好所需语言且不需要下载其他语言，可以关闭此项。

## `Economy`

### `Economy.Enabled`

开启或关闭 CMI 经济系统<br>
检测到 CMIInjector 时，此项会自动设为 true<br>
注意！要让经济系统与其他插件正常配合，需要安装注入器或重新编译的 Vault。<br>
两者均可在插件发布页顶部找到<br>
注意！如果在服务器运行时关闭 CMI 经济系统，必须完整重启服务器才能生效，避免读取玩家余额时出现问题。

### `Economy.Confirmation`

玩家是否需要点击聊天消息，确认转账

### `Economy.OfflinePayments`

是否允许向离线玩家付款。主要影响 pay 命令，不会阻止从其他插件收款等操作。

### `Economy.LogEnabled`

设为 true，将玩家之间的转账写入日志

### `Economy.Cheque.MaxValue`

玩家可创建支票的最大金额<br>
设为 0 取消限制

### `Economy.Cheque.Paper`

设为 true，玩家创建支票时必须手持一张纸。

### `Economy.Cheque.Permission`

设为 true，兑现支票需要 cmi.command.cheque.withdraw 权限

### `Economy.Cheque.InCreative`

是否允许在创造模式下使用支票<br>
创造服请保持 false，否则玩家可能复制物品

### `Economy.Cheque.AcceptNotEncoded`

是否接受未使用编码数据的旧版支票物品<br>
为保证安全，保持 false

### `Economy.PaymentWithShorts.Allow`

设为 true，允许使用金额缩写付款，例如 10k 表示 10000<br>
同样，10.2k 表示 10200

### `Economy.PaymentWithShorts.values`

允许的金额后缀及其对应数值<br>
后缀只能使用一个字母

### `Economy.BalTop.LoadInAll`

启用后，服务器启动时会预加载所有玩家余额，供 baltop 排行榜使用<br>
使用第三方经济插件时，可能增加首次加载时间<br>
设为 false，baltop 只包含余额刚发生变化的玩家，不会包含全部玩家<br>
不使用 CMI 的 baltop 时，请保持关闭

### `Economy.BalTop.Exclude`

不计入 baltop 排行榜的玩家

### `Economy.BalTop.DisplayWithShorts`

启用后，baltop 使用金额缩写，例如将 12501234 显示为 12.5M

### `Economy.BalTop.ExcludeStartingWith`

不计入 baltop 的名称列表<br>
可用于排除 Towny 的城镇账户

### `Economy.BalTop.IncludeFakes`

设为 true，将部分虚拟账户纳入 baltop 排行榜<br>
包括此前被标记为虚拟账户、用于城镇或类似用途的账户

### `Economy.BalTop.ExcludeInactive`

设为 0 或更小的值关闭此功能<br>
玩家离线达到多少天后，不再计入余额排行榜<br>
需要重启服务器才能完全生效

### `Economy.Global.StartingAmount`

玩家的初始余额

### `Economy.Global.MinimalAmount`

最低余额，需要时可设为负数

### `Economy.Global.MaximumAmount`

玩家余额上限，设为 -1 取消限制

### `Economy.Global.MinimalPay`

玩家单次向其他玩家转账的最低金额<br>
可防止玩家反复转账极小金额来刷屏

### `Economy.Global.Fractions`

是否允许带小数的转账金额<br>
关闭后只允许整数金额；输入小数时会向下取整

### `Economy.Global.CurrencySymbol`

显示余额等信息时使用的货币符号

### `Economy.Global.MoneyFormat`

金额显示格式

### `Economy.Global.UseShortNumbers`

将长数字缩写，例如将 12305122 显示为 12.3m

### `Economy.Global.shortNumbersFormat`

此格式仅用于带后缀的金额，例如 '1.23k'；小于 1k 的金额使用 MoneyFormat

### `Economy.Global.ShortNumbersSuffixes`

金额缩写后缀

### `Economy.Global.SwitchPlaces`

改用逗号分隔小数、句点分隔千位的格式，例如将 1,000,000.00 改为 1.000.000,00

### `Economy.Global.Placing`

货币符号的位置

### `Economy.Global.Tax`

/pay 命令的转账税<br>
目前仅对这条命令征税，不影响其他操作

### `Economy.Global.Tax.Type`

征税类型：None、Flat、Percentage<br>
Flat：每次执行 pay 时收取固定金额<br>
Percentage：按每次 pay 的转账金额收取一定比例

### `Economy.Global.Tax.Amount`

固定税额或转账金额的百分比<br>
百分比范围为 0 到 100

### `Economy.Global.Tax.Min`

最低税额，主要用于按比例征税

### `Economy.Global.Tax.Max`

最高税额，主要用于按比例征税<br>
设为 0 不限制最高税额

### `Economy.Global.Tax.DeductOnTop`

设为 true，税额在转账金额之外另收。例如转账 100、税额 10，收款人获得 100，付款人扣除 110<br>
设为 false，税额从转账金额中扣除。例如转账 100、税额 10，收款人获得 90，付款人扣除 100<br>
建议保持 true，避免玩家不明白为何实际收款少于转账金额

## `FileSave`

### `FileSave.Async`

仅在磁盘 I/O 有问题，需要异步保存玩家文件以减少 Minecraft 服务端等待时间时，才设为 true

## `InteractiveCommands`

### `InteractiveCommands.SignRegex`

识别告示牌上公开交互指令的正则表达式<br>
默认格式为 \[ic:\[icName\]\]，例如 \[ic:trash\]<br>
若要使用简洁格式，可使用此正则： (\\\[(\[a-zA-Z0-9\]+)\\\])

### `InteractiveCommands.SortByDistance`

交互指令列表按与你的距离或按字母顺序排序

## `Optimizations`

### `Optimizations.UseFakeOperator`

关闭后，服务器启动或插件卸载时不会撤销虚拟操作员的 OP，同时禁用 asFakeOp! 特殊指令

### `Optimizations.InfiniteLoopDetection`

关闭后，执行自定义别名命令时不会检查可能出现的无限循环

### `Optimizations.MonochromeConsole`

设为 true，移除所有控制台消息中的颜色<br>
控制台仅支持单色时，保持 true

### `Optimizations.ImmortalityOnJoin`

玩家加入服务器后获得无敌状态的时长，单位为秒<br>
设为 0 关闭<br>
最多 60 秒

### `Optimizations.Maintenance`

开启或关闭维护模式

### `Optimizations.MaintenanceAutoKick`

开启维护模式时，自动踢出所有没有 cmi.command.maintenance.bypass 权限的玩家

### `Optimizations.MaintenanceBossBar`

启用后，通过 Boss 栏提示服务器正处于维护模式

### `Optimizations.DisableTeamManagement`

设为 true，发光颜色、玩家碰撞、名称标签等功能会停止工作，CMI 也不再操作玩家队伍<br>
与其他使用玩家队伍实现功能的插件冲突时，可开启此项

### `Optimizations.ArmorStands.CheckBlockPlace`

设为 true，通过模拟方块放置事件，检查其他插件是否阻止玩家操作盔甲架<br>
可减少玩家在没有区域建造权限时，仍能操作该区域盔甲架的情况

### `Optimizations.ArmorStands.MinScale`

盔甲架编辑器允许设置的最小缩放比例<br>
基础最小比例，可通过 cmi.command.armorstand.scalemin.\[value\] 权限覆盖<br>
两者都设置时，取此项与权限所指定数值中的较小值

### `Optimizations.ArmorStands.MaxScale`

盔甲架编辑器允许设置的最大缩放比例<br>
基础最大比例，可通过 cmi.command.armorstand.scalemax.\[value\] 权限覆盖<br>
两者都设置时，取此项与权限所指定数值中的较大值

### `Optimizations.ArmorStands.Templates.SpecificPermission`

设为 true，放置已保存的模板需要 cmi.command.armorstand.template.\[templatename\] 权限

### `Optimizations.AutoDownload.GeoIp`

缺少 GeoIP.dat 时会在服务器启动时自动下载，可能需要重启后才生效

### `Optimizations.AutoDownload.GeoLiteCity`

缺少 GeoLiteCity.dat 时会在服务器启动时自动下载，可能需要重启后才生效

### `Optimizations.ShowSkullOwner`

启用后，右键点击头颅会在动作栏显示其所有者名称

### `Optimizations.ShowBeeHiveInformation`

启用后，右键点击蜂箱会在动作栏显示蜂箱信息

### `Optimizations.ShowDecoratedPotInformation`

启用后，右键点击饰纹陶罐会在动作栏显示其中物品的信息

### `Optimizations.ElevatorIndicator`

创建电梯告示牌时使用的标识，不区分大小写

### `Optimizations.SignEdit.BlackList`

告示牌首行符合此内容时，不允许玩家通过 /cmi se 编辑

### `Optimizations.ElevatorStaticIndicator`

电梯类型。在告示牌第二行使用此标识时，将玩家传送到牌子正前方，而不是保留原来的 x、z 坐标

### `Optimizations.LongDateFormat2`

邮件、checkban、infopage 等位置的日期格式

### `Optimizations.ShortDateFormat`

物品栏界面等位置的日期格式

### `Optimizations.SellLog`

是否将 sell hand 操作记录到文件

### `Optimizations.PartialPlayerName`

设为 true，执行需要玩家名称的命令时，如果找不到完整名称，会尝试匹配在线玩家的部分名称。例如 /cmi heal rips 可以治疗 Zrips<br>
适合名称较复杂的玩家

### `Optimizations.PrioritizeOnlinePlayers`

使用部分名称匹配时，是否优先选择在线玩家<br>
需要同时启用 PartialPlayerName 才能完全生效<br>
这可能导致名称部分相同的玩家在线时，无法访问对应的离线玩家<br>
例如 Luuk666 在线时，可能无法访问离线玩家 Luuk<br>
可在名称后加 -exa- 强制精确匹配，例如 luuk-exa- 会返回离线玩家对象

### `Optimizations.CommandSorting`

设为 true，帮助页中的命令按字母顺序排序<br>
设为 false，按优先级排序

### `Optimizations.AllowRconCommands`

默认不允许 Rcon 命令。仅在已妥善配置远程控制台且确有需要时开启

### `Optimizations.CleanRconCommands`

启用后，Rcon 返回消息不含颜色代码，便于阅读

### `Optimizations.SimilarCommandChecker`

找不到命令时，用于选择最接近命令的匹配度，范围为 1–100<br>
例如 /cmi spawnmb 与 /cmi spawnmob 的匹配度为 87.5%<br>
设为 0 关闭

### `Optimizations.SimilarCommandPrevention`

设为 true，玩家输入错误命令时，不执行自动匹配的命令<br>
无论如何，都会提示用法错误并显示最接近的命令

### `Optimizations.RemoveLabel`

设为 true，隐藏帮助页中命令的 /cmi 前缀，例如将 /cmi back 显示为 /back<br>
已为命令设置别名或自定义别名时，会自动使用此功能<br>
这只影响显示，不改变命令的实际用法

### `Optimizations.PermisionOnError`

设为 true，所有玩家都能将鼠标移到错误提示上，查看缺少的权限节点<br>
设为 false，只有拥有 cmi.permisiononerror 权限的玩家才能查看缺少的权限节点<br>
玩家默认拥有此权限；若要隐藏缺少的权限节点，请将该权限设为否定

### `Optimizations.PermisionInConsole`

设为 true，玩家尝试执行无权限的操作时，会在控制台显示消息

### `Optimizations.Teleport.SafeLocationDownThenUp`

玩家需要 cmi.safeteleport 权限，传送时才会被放到安全位置<br>
设为 true，检查安全位置时先从目标位置向下搜索，失败后再向上搜索<br>
设为 false，先检查目标位置上方，再检查下方

### `Optimizations.Teleport.Invulnerability`

传送后玩家的无敌时长，单位为秒<br>
在指定时间内，也阻止刚传送的玩家伤害其他玩家<br>
设为 0 关闭此功能<br>
最多 60 秒

### `Optimizations.Teleport.InvulnerabilityPerWorld`

传送到此世界后玩家的无敌时长，单位为秒<br>
未单独设置的世界使用默认时长

### `Optimizations.Teleport.DisableInvulnerability`

以下情况会取消传送后的无敌状态

### `Optimizations.Teleport.DisableInvulnerability.OnBlockBreakPlace`

玩家破坏或放置方块时取消

### `Optimizations.Teleport.DisableInvulnerability.OnInteraction`

玩家与方块或实体交互时取消

### `Optimizations.Teleport.SwitchPlaces`

设为 true，tp 用法为 /cmi tp \[WhoYouWantToTeleport\] \[WhereToTeleport\]；设为 false，用法为 /cmi tp \[whereToTeleport\] \[WhoYouWantToTeleport\]

### `Optimizations.Teleport.CurrentLoc.tpa`

仅适用于 tpa、tpahere 和 tpaall<br>
设为 true，接受传送请求后，传送到目标玩家当前的位置<br>
设为 false，传送到发出请求时目标玩家所在的位置

### `Optimizations.Teleport.CurrentLoc.tpahere`

仅适用于 tpahere

### `Optimizations.Teleport.JumpDefault`

jump 命令的默认距离，可通过 cmi.command.jump.\[amount\] 权限覆盖

### `Optimizations.Teleport.Tpa.Time`

接受 tpa 或 tpahere 请求的有效时间，单位为秒

### `Optimizations.Teleport.Tpa.Warmup`

接受 tpa 或 tpahere 后，传送前的等待时间，单位为秒

### `Optimizations.Teleport.Tpa.Move`

等待 tpa 或 tpahere 传送期间，是否允许移动

### `Optimizations.Teleport.Tpa.Block`

拒绝请求后，阻止对方再次发送传送请求的时长，单位为秒

### `Optimizations.Teleport.Tpa.MaxDistance`

最大传送距离，单位为方块<br>
设为 0 关闭此限制<br>
设为正数后，除了限制玩家间的距离，也会阻止向其他世界的玩家发送传送请求<br>
可通过 cmi.command.tpa.max.\[blockcount\] 权限覆盖

### `Optimizations.Teleport.TpaHere.MaxDistance`

最大传送距离，单位为方块<br>
设为 0 关闭此限制<br>
可通过 cmi.command.tpahere.max.\[blockcount\] 权限覆盖

### `Optimizations.Teleport.Tp.Bypass`

允许绕过“不安全位置”传送拦截的时间，单位为秒

### `Optimizations.Teleport.DenyConfirm`

设为 true，tpa 或 tpahere 请求中显示接受和拒绝按钮

### `Optimizations.Teleport.BlackListedItems.Enabled`

物品栏中有黑名单物品时，阻止玩家传送。可通过 cmi.teleport.bypassblacklist 绕过

### `Optimizations.Teleport.BlackListedItems.List`

要限制的物品及数量，未填写数量时默认为 0<br>
使用 : 分隔数量，例如 IronOre:5 表示物品栏中 ironOre 最多为 5 个，超出就无法传送

### `Optimizations.Teleport.Back.MinDistance`

传送距离小于指定方块数时，不记录 /back 返回位置

### `Optimizations.Teleport.Back.WithWE`

设为 false，使用 WorldEdit 指南针传送时不记录返回位置<br>
设为 true，记录每次传送，包括使用指南针进行的短距离跳跃

### `Optimizations.Teleport.Back.BlackList`

不允许通过 /back 返回的世界

### `Optimizations.Teleport.Back.Expiration`

/back 返回位置的有效时间，单位为秒；设为 0 关闭过期限制

### `Optimizations.Teleport.DBack.BlackList`

不允许通过 /dback 返回的世界

### `Optimizations.Teleport.DBack.Expiration`

/dback 返回位置的有效时间，单位为秒；设为 0 关闭过期限制

### `Optimizations.Hat.Block.WithLore`

启用后，不允许将带有自定义描述的物品放入头盔槽<br>
不影响头盔类物品

### `Optimizations.Hat.Block.NoneHatItems`

启用后，不允许装备非帽子类型的物品

### `Optimizations.Hat.Block.NoneHatEnchanted`

启用后，不允许装备带附魔的非帽子物品

### `Optimizations.Hat.Allow.MobHeads`

启用后，玩家无需 cmi.inventoryhat 权限即可将生物头颅戴在头上<br>
关闭后，将生物头颅戴在头上需要 cmi.inventoryhat 权限

### `Optimizations.Hat.WhiteList`

允许戴在头上的材质列表<br>
留空表示允许所有材质

### `Optimizations.helpop.feedbackMessage`

设为 true，玩家不会看到自己发送的 helpop 内容，而会收到预设提示，告知问题已发给在线管理人员

### `Optimizations.IP.Record`

设为 true，记录玩家 IP，供日后识别其他账号等用途使用<br>
关闭后，部分命令的功能会受限<br>
这可能增加缓存大小，尤其是玩家使用动态 IP 时

### `Optimizations.IP.delay`

等待多少秒后，才将玩家 IP 写入数据库<br>
仅用于离线服务器，让玩家先完成登录，再记录 IP<br>
建议大于登录插件允许的登录时长，以记录真正有权使用该名称的玩家 IP

### `Optimizations.MaxHp`

/cmi maxhp 命令允许设置的生命值上限

### `Optimizations.PlayTimeFromStats`

设为 true，从玩家统计文件读取在线时长，而不是从 CMI 玩家数据读取<br>
对于运行较久并启用玩家统计的服务器，这可能获得更准确的在线时长<br>
建议保持 true

### `Optimizations.PlayTimeAutoUpdater`

是否自动更新在线时长排行榜<br>
按固定间隔更新玩家的在线时长排名，便于占位符读取

### `Optimizations.CMIPlayTimeTracking`

是否启用 CMI 在线时长记录<br>
启用后，按玩家在服务器游玩的每个小时分别记录在线时长<br>
不影响 rankup 和 /playtime，只让 /cplaytime 按小时显示更详细的在线时长

### `Optimizations.PlaytimeTopExclude`

不计入 playtimetop 排行榜的玩家名称

### `Optimizations.PlaytimeTopOffline`

玩家离线达到多少天后，从 playtimetop 中排除<br>
设为 0 关闭

### `Optimizations.ItemName.MarkChanged`

材质黑名单见 ItemRenaming.list

设为 true，用 /itemname 改名的物品会添加布尔型 NBT 标记 'ModifiedName'

### `Optimizations.ItemLore.MaxLength`

itemlore 命令允许的单行描述最大长度，不含颜色代码<br>
设为 0 取消限制

### `Optimizations.ItemLore.TypeBlackList`

禁止使用 itemName 命令改名的材质

### `Optimizations.ItemLore.MarkChanged`

设为 true，用 itemname 修改描述的物品会添加布尔型 NBT 标记 'ModifiedLore'

### `Optimizations.OnDurabilityLoss.Tools`

物品耐久度低于阈值时，是否提醒玩家<br>
玩家需要 cmi.informDurability 权限

### `Optimizations.OnLimitedItemUse.Inform`

提示物品剩余可使用次数

### `Optimizations.PreventEntityBoatEnter`

是否阻止动物或怪物进入船

### `Optimizations.PreventPlayersOnNetherRoof`

将位于下界基岩顶层上方的玩家传送到下方

### `Optimizations.netherRoofHeight`

下界顶层高度。设为 0 使用默认高度 128

### `Optimizations.PreventPlayersBelowBedrock`

玩家飞行或使用鞘翅滑翔到基岩下方时，将其传送到上方

### `Optimizations.PreventIronGolem.Roses`

设为 true，铁傀儡死亡时不掉落玫瑰

### `Optimizations.PreventHook`

设为 true，钓竿不会将钩住的实体拉向玩家

### `Optimizations.Commands.ShowMainHelpPage`

设为 true，只执行 /cmi 而不指定子命令时，显示全部可用命令<br>
设为 false，返回“未找到命令”的提示

### `Optimizations.Commands.Near.Approximate`

使用大致距离，而不是精确距离<br>
使用另一条包含玩家方向的语言文本<br>
例如将 123m 显示为 ~100m

### `Optimizations.Commands.Near.Invisibility.Hide`

启用后，不在列表中显示具有隐身药水效果的玩家

### `Optimizations.Commands.Near.Invisibility.Obfuscate`

仅在上面的 Hide 选项启用时生效<br>
混淆玩家名称，但仍在列表中显示其位置<br>
不用真实名称，而是使用固定 8 个字符、带 &amp;k 格式的名称，避免通过名称长度猜出附近是谁

### `Optimizations.Commands.Near.PointTo`

启用后，点击玩家名称会执行 /cmi point \[location\]，通过粒子指向目标玩家

### `Optimizations.Commands.Near.Count`

/near 命令显示的行数

### `Optimizations.Commands.lastonline.Timers`

lastonline 统计最近多少秒内离线的玩家数量，作为附加信息显示

### `Optimizations.Commands.CheckAccount.ExcludedUsers`

checkaccount 命令排除的玩家或 IP

### `Optimizations.Commands.Inv.BlackList`

不允许打开其物品栏的玩家<br>
OP 仍可绕过此限制

### `Optimizations.Commands.Inv.DisableOffline`

是否禁止对离线玩家使用 inv 命令

### `Optimizations.Commands.Clear.Confirmation`

设为 true，/cmi clear 必须确认后才执行

### `Optimizations.Commands.Clear.Exclude`

移除物品前需要检查的 NBT 路径。每行应以 NBT: 开头，为以后加入其他可选检查保留

### `Optimizations.Commands.List.ASCOrder`

玩家自定义组按升序或降序排序

### `Optimizations.Commands.Sc.ClearColors`

启用后，复制告示牌文字时会检查玩家可用的颜色权限<br>
关闭后，原样复制文字及颜色，不作修改或限制

### `Optimizations.Commands.Give.LimitEnchants`

启用后，give 命令中的物品遵守相同的附魔限制和权限要求

### `Optimizations.Multicraft.DisableList`

设为 true，防止 Multicraft 服务器的控制台刷屏

## `PlaytimeRewards`

### `PlaytimeRewards.Enabled`

开启或关闭在线时长奖励<br>
要自动发放奖励，必须启用此项

### `PlaytimeRewards.ExcludeAfk`

启用后，玩家 AFK 时不累计可重复在线时长奖励的进度<br>
注意！Afk.StopPlayTime 为 true 时，此项不生效<br>
StopPlayTime 为 true 时，AFK 时长会自动排除

### `PlaytimeRewards.RewardInform`

提醒玩家领取待领取奖励的间隔，单位为分钟

### `PlaytimeRewards.OneTimeAmount`

列表中显示多少个一次性奖励<br>
显示从当前在线时长起接下来的 X 个奖励<br>
距离奖励还很远时，没有必要列出全部奖励

### `PlaytimeRewards.RequiresPermission`

设为 true，领取指定在线时长奖励需要 cmi.prewards.\[name\] 权限

## `Sleeping`

### `Sleeping.Speedup.Enabled`

设为 true，玩家睡觉时可以加快夜晚流逝<br>
根据该世界中睡觉的玩家比例，加快时间流逝

### `Sleeping.Speedup.Worlds`

应用此功能的世界列表<br>
只有普通类型的世界支持加速时间，默认通常只有一个这样的世界<br>
设为 \[\] 将包含所有可用世界

### `Sleeping.Speedup.OnlyDurringNight`

设为 true，只在一天中的 12542 到 24000 刻之间加速时间<br>
设为 false，玩家也能在雷暴等情况下加速白天

### `Sleeping.Speedup.NightStartsAt`

夜晚开始的时间<br>
单位为刻，例如 12542 对应 18:32:00

### `Sleeping.Speedup.InfoType`

加速提示的显示类型：none、title、bossbar

### `Sleeping.Speedup.ExcludeAfk`

设为 true，计算加速比例时排除 AFK 玩家

### `Sleeping.Speedup.BaseSpeed`

夜晚加速的基础倍数。数值越大，时间越快，所需睡觉玩家越少<br>
100 表示时间流逝速度为正常的 100 倍

### `Sleeping.Speedup.MinSpeed`

最低加速倍数，用于玩家数量超过基础倍数、计算结果回到默认速度的情况

### `Sleeping.Speedup.MinBeforeSpeeding`

开始加速前，至少需要多少名玩家睡觉<br>
支持两种格式：填写整数，例如 3，表示至少 3 名玩家睡觉才开始加速<br>
填写百分比，例如 50%，表示服务器中至少一半玩家睡觉才开始加速

### `Sleeping.Speedup.Inform`

设为 true，向在线玩家提示还缺多少人睡觉

### `Sleeping.Speedup.InformDelay`

玩家开始或停止睡觉时，加速提示消息的最小间隔，单位为秒

## `Compass`

### `Compass.BossBar`

启用实验性的 Boss 栏指南针<br>
仅适用于 1.9+ 服务器

### `Compass.RequireCompass`

需要手持指南针才会显示

### `Compass.RecoveryAsRegular`

启用后，恢复指南针也能像普通指南针一样触发 Boss 栏显示

### `Compass.RequireRecoveryCompass`

需要手持恢复指南针，Boss 栏才会显示死亡位置

### `Compass.UpdateInterval`

指南针更新间隔，单位为毫秒

### `Compass.Shape`

各方向之间保持相同间距，整体长度不限

### `Compass.Gradient`

仅适用于 1.16+ 服务器<br>
方向之间的颜色过渡

## `ExploitPatcher`

### `ExploitPatcher.PreventExpPortals`

启用后，防止经验瓶在传送门边缘被摧毁而造成复制

### `ExploitPatcher.NoCommandsInBed`

启用后，阻止玩家执行可能引发问题的命令<br>
默认关闭以保留原版行为，但建议开启以避免问题

### `ExploitPatcher.LimitBooks`

由于超大书本存在严重漏洞，建议开启此项<br>
设为 true，限制玩家可创建的书本页数<br>
页数由 cmi.book.pages.§f\[20to100\]§6 权限决定，默认允许创建 20 页

### `ExploitPatcher.BlockEndPortalItemTransfers`

启用后，阻止物品通过末地传送门和末地折跃门传送

### `ExploitPatcher.Riptide`

世界天气为晴天、玩家个人天气 pweather 为雨天时，禁止使用激流

### `ExploitPatcher.Placeholders.blocked.checkItem`

默认阻止 PAPI 的 %checkitem\_...% 占位符，以避免潜在的严重问题<br>
只有另有专门防护时，才应关闭此项

## `Vault`

### `Vault.Money`

Vault 无法正确读取玩家权限组或余额时，可以尝试设为 false

## `Worth`

### `Worth.BadLore`

包含此描述的物品无法通过 /cmi sell 出售<br>
忽略颜色代码和大小写

### `Worth.CustomNameBlocking`

启用后，带自定义名称的物品无法通过 /cmi sell 出售

### `Worth.LoreBlocking`

启用后，带自定义描述的物品无法通过 /cmi sell 出售

### `Worth.RequireFullDurability`

启用后，耐久度未完全修复的物品无法出售

### `Worth.DevalueByDurability`

启用后，按剩余耐久度降低售价。例如剩余 30% 耐久度，价格降低 70%<br>
仅在 RequireFullDurability 关闭时生效

### `Worth.AutoGenerate.PriceIncrease`

根据材料价格自动计算成品价格时，额外增加的百分比<br>
例如木棍价格为 0.1、钻石为 44，diamond\_hoe 的材料总价为 88.2；额外增加 2% 后变为 89.96<br>
可以设为负数

## `BossBar`

### `BossBar.HpBarEnabled`

在 1.9+ 服务器上开启或关闭 Boss 栏生命值显示<br>
只有拥有 cmi.bossbar.hpbar 权限的玩家才能看到<br>
为减少开销，此权限最多每分钟重新检查一次

### `BossBar.HpBarBlackList`

不在生命值 Boss 栏中显示的生物类型

## `Ban`

### `Ban.OverrideLoginMessage`

设为 true，被封禁玩家看到 CMI 修改后的提示，而不是原版提示

## `ReSpawn`

### `ReSpawn.Immortality`

玩家重生后的无敌时长，单位为秒<br>
可用于防止玩家在重生点被反复击杀<br>
设为 0 关闭此限制<br>
最多 60 秒

### `ReSpawn.Enabled`

若由第三方插件处理重生，将此项设为 false 后重载插件即可

### `ReSpawn.Global.PriorityOrder`

世界未出现在 Specific 列表中时，使用的重生位置优先顺序<br>
可用位置：anchor、bedLocation、spawn、homeLocation、worldSpawn、warp!\[warpName\]<br>
spawn：用 /cmi setspawn 设置的位置，该位置的 RespawnLocation 应为 true<br>
bedLocation：通过与床交互设置的位置。BedInteraction 应设为 false，玩家需要 cmi.bedhome 权限才能设置<br>
homeLocation：玩家默认名称为 Home 的家。不存在时，尽可能使用列表中的第一个家<br>
worldSpawn：此世界的默认出生点，不是 CMI 设置的出生点<br>
anchor：与重生锚交互后设置的位置。通常只在下界死亡时使用，其他情况使用床的位置<br>
warp!\[warpName\]：任意有效传送点，传送时绕过该传送点的全部使用要求

### `ReSpawn.Specific`

指定世界的重生位置优先顺序<br>
若交由服务端或第三方插件处理重生，将重生优先列表设为 \[\]，或设为随机重生条件

## `Holograms`

### `Holograms.Defaults.viewRange`

全息图的默认可见距离<br>
决定玩家在多远的位置能看到全息图，以及何时隐藏

### `Holograms.Defaults.updateRange`

全息图的默认更新距离<br>
玩家进入此距离内，全息图才开始更新文字<br>
请设置合理范围，没有必要更新地图另一端的全息图

### `Holograms.Defaults.Interval.Update`

默认更新间隔，单位为刻；20 刻 = 1 秒<br>
设为 0 或更小的值时，不更新全息图<br>
仅影响包含动态内容的全息图

### `Holograms.Defaults.pageChangeInterval`

默认翻页间隔，单位为刻<br>
设为 0 或更小的值时，不自动翻页

### `Holograms.Defaults.Interaction.BasePrefix`

使用 CText 的行所加的前缀<br>
仅影响设置了命令的部分，不影响普通文字，即使普通文字带悬停提示

### `Holograms.Defaults.Interaction.HoverPrefix`

使用 CText 的行在鼠标悬停时所加的前缀<br>
可在全息图编辑器中单独覆盖

## `Votifier`

### `Votifier.CountVotes`

设为 true，记录玩家的 Votifier 投票次数

### `Votifier.MaxVotesInADay`

同一 IP 在过去 24 小时内允许的投票次数<br>
设为 0 不限制次数

### `Votifier.GeneralCooldown`

同一投票服务的投票冷却时间<br>
大多数投票服务本身已有冷却限制<br>
需要额外限制快速重复投票时，可在此填写秒数

### `Votifier.PerformCommands`

设为 false，成功投票后不执行命令

### `Votifier.CommandsOnVote`

玩家投票时执行的命令<br>
支持特殊指令和占位符<br>
可用 \[serviceName\] 变量插入服务地址

### `Votifier.ExtraRewardsEnabled`

不想发放额外奖励时，保持 false

### `Votifier.ExtraRewards`

玩家累计达到指定投票次数后执行的命令

### `Votifier.ExcludeList`

不计入投票排行榜的玩家

## `Ranks`

### `Ranks.PermissionCheck`

设为 true，通过权限检查玩家可使用的等级，并优先采用权重高于当前等级的等级<br>
例如记录的等级为第一级、但玩家有第三级权限时，优先采用第三级<br>
启用期间，/cmi setrank 等命令会将等级设为玩家有权使用的最高等级；只要仍有第三级权限，就无法降到更低等级<br>
降级前，需要先移除相应等级的权限

### `Ranks.Recalculation`

重新计算玩家权限组的间隔，单位为分钟<br>
设为 0 关闭

### `Ranks.AutoRankUp.Delay`

检查玩家能否晋级的间隔，单位为秒<br>
设为 0 或更小的值，关闭自动晋级检查

### `Ranks.AutoRankUp.Async`

实验性选项：设为 true，异步检查玩家晋级条件<br>
启用后若出现相关错误，请关闭，并携带错误日志向 GitHub 反馈

### `Ranks.AutoRankUp.PlayerDelay`

对每名玩家分别检查晋级条件的间隔，单位为秒<br>
与全局检查间隔不同，用于避免几名玩家同时晋级<br>
同时决定可晋级提示的间隔；每次提示后，间隔会按比例增加，避免聊天刷屏<br>
应大于或等于全局检查间隔

### `Ranks.AutoRankUp.progressBar`

是否在等级信息界面显示进度条

### `Ranks.ListSamePathOnly`

设为 true，/cmi ranklist 只显示当前晋级路线中的等级，排除其他路线和等级树<br>
设为 false，显示所有已设置的等级

### `Ranks.OnlyHours`

设为 true，时间要求使用小时格式，例如显示“50 小时”，而不是“2 天 2 小时”

### `Ranks.includeMinutes`

OnlyHours 为 true 时，使用分钟补充显示，避免小数，例如显示“5 小时 30 分钟”，而不是“5.5 小时”

## `Signs`

### `Signs.CheckInterval`

检查玩家是否进入动态告示牌触发区域的间隔，单位为毫秒<br>
数值较大可略微降低服务器负载<br>
无需设置得很小

### `Signs.editBlackList`

告示牌首行符合列表内容时，无法通过潜行右键编辑<br>
通常用于防止商店告示牌被修改

### `Signs.RequireSneaking`

启用后，必须潜行才能编辑告示牌

### `Signs.DialogEditor`

启用后，使用 1.21.7+ 新增的对话框编辑器编辑告示牌<br>
仅适用于 Paper 服务器

## `Skins`

### `Skins.AutoApply`

玩家登录且尚未设置皮肤时，自动应用皮肤<br>
始终按目标玩家名称获取皮肤

### `Skins.SteveOnOff`

关闭皮肤时，先设为 Steve，再交由服务端处理<br>
设为 false 时，改用在线获取的皮肤

### `Skins.RequireSpecificPerm`

使用指定皮肤需要 cmi.command.skin.perm.\[skinName\] 权限

### `Skins.SkinUpdateTimer`

从 Mojang 在线服务器更新皮肤信息的间隔，单位为分钟<br>
例如设为 1 小时，已有皮肤信息超过 1 小时后才重新获取<br>
仅在玩家加入服务器或手动更换皮肤时检查

## `Alert`

### `Alert.Timer`

执行 /cmi alert 后，对该玩家保留警报的时间，单位为分钟，默认为 24 小时

## `Notes`

### `Notes.ShowOnAlertEvent`

启用后，被标记警报的玩家登录时，提醒管理人员该玩家附有备注

## `GroundClean`

### `GroundClean.WhiteList.Material`

清理地面物品时，保留的物品类型

### `GroundClean.WhiteList.EntityType`

清理地面物品时，保留的物品类型

## `Command`

### `Command.CommandFilter.Duplicate.Use`

设为 true，限制短时间重复执行相同或相似命令。可通过 cmi.commandfilter.bypass 绕过

### `Command.CommandFilter.Duplicate.Percentage`

判定为相同命令的相似度百分比

### `Command.CommandFilter.Duplicate.Interval`

重复执行相同或相似命令的间隔，单位为秒

### `Command.CommandFilter.Duplicate.MinAmount`

触发冷却前允许连续重复的命令次数

### `Command.CommandFilter.Duplicate.WhiteList`

不受限制的命令白名单

### `Command.Spy.BlackListed`

出于安全和隐私考虑，命令监视不显示列表中的命令<br>
可通过 cmi.command.commandspy.bypass 权限绕过

### `Command.Spy.CommandList`

没有 cmi.security.admin 权限的玩家，使用命令监视时只能看到此列表中的命令<br>
留空表示显示除黑名单以外的全部命令

### `Command.Notes.ExpiresIn`

玩家备注的保留时间，单位为天

### `Command.Mail.ExpiresIn`

玩家邮件的保留时间，单位为天

### `Command.Mail.mailAllDays`

群发邮件只发送给过去 X 天内登录过的玩家

### `Command.Mail.MaxMails`

每名玩家最多保留的邮件数量<br>
达到邮件上限后，移除最早的邮件

### `Command.Mail.ConsoleMailSender`

控制台发送邮件时使用的发件人名称<br>
用于显示发件人；玩家回复时，也会发送给此名称对应的玩家<br>
建议填写负责与玩家沟通的管理人员名称

## `DisplayName`

### `DisplayName.Change`

由第三方插件修改玩家显示名称时，将此项设为 false

### `DisplayName.Format`

玩家显示名称格式。默认显示昵称；未设置昵称时，显示真实玩家名称<br>
可用自定义变量：{prefix} {suffix} {nicknameprefix}<br>
支持占位符

### `DisplayName.ValidNicknameRegex`

检查昵称是否合法的正则表达式<br>
默认只允许字母和数字<br>
若允许所有语言的字母，可使用 \[^\\p{L}0-9\\-\\\_\]

## `NickName`

### `NickName.BlackList`

没有绕过权限时，禁止将昵称改为列表中的名称<br>
使用小写

```text
cmi.command.nick.bypassblacklist
```

可通过 cmi.command.nick.bypassinuse 绕过名称或昵称已被占用的限制

### `NickName.MinLength`

昵称最小长度，可通过 cmi.command.nick.bypass.length 绕过

### `NickName.MaxLength`

昵称最大长度，可通过 cmi.command.nick.bypass.length 绕过

### `NickName.PreventRealNames`

启用后，不允许选择已存在的真实玩家名称<br>
可通过 cmi.command.nick.bypassrealname 权限绕过

### `NickName.Prefix`

为昵称添加前缀，表明它不是真实名称。可通过 {nicknameprefix} 加入显示名称

### `NickName.PrefixWhenDifferent`

设为 true，只有昵称与原名不同时才添加前缀，因此仅修改颜色或大小写时可不加前缀

### `NickName.TabComplete.ReplaceReal`

设为 true，Tab 补全使用在线玩家的昵称，而不是真实名称

### `NickName.TabComplete.IncludeReal`

设为 true，在昵称上方同时显示真实名称；仅在 ReplaceName 启用时生效

## `Dye`

### `Dye.BoundToPlayer`

设为 true，染色皮革盔甲的动态颜色绑定到获得该颜色的玩家，交给其他玩家后不再生效<br>
仅影响生物群系、生命值等动态盔甲颜色

## `ShowNewVersion`

拥有 cmi.versioncheck 权限的玩家登录时，提示是否有新版本

## `Spawners`

### `Spawners.FullDisable`

刷怪笼处理出现问题时，可设为 true，关闭 CMI 对刷怪笼的操作<br>
这会关闭刷怪笼放置、掉落、挖掘次数等功能

### `Spawners.Break.Enabled`

注意！玩家必须拥有 cmi.dropspawner 权限，破坏刷怪笼时才会掉落<br>
开启或关闭刷怪笼破坏处理<br>
启用后，使用精准采集镐且拥有 cmi.dropspawner 权限时，破坏刷怪笼可获得掉落<br>
拥有 cmi.dropspawner.nosilk 权限时，无需精准采集镐也能获得刷怪笼

### `Spawners.Break.CustomName`

启用后，刷怪笼物品按其生物类型设置自定义名称

### `Spawners.Break.IntoInventory`

启用后，刷怪笼直接放入玩家物品栏，不掉落到地面<br>
物品栏已满时，仍会掉落到地面

### `Spawners.Break.RequiresExactPermission`

设为 true，破坏并获得指定类型的刷怪笼需要对应权限<br>
例如破坏猪刷怪笼并获得掉落需要 cmi.dropspawner.pig，僵尸刷怪笼需要 cmi.dropspawner.zombie

### `Spawners.Break.DropExp`

设为 false，破坏刷怪笼不掉经验，无论刷怪笼本身是否掉落<br>
设为 true，只在刷怪笼本身不掉落时掉经验

### `Spawners.Break.SilkTouchLevel`

获得刷怪笼所需的最低精准采集等级

### `Spawners.Break.BaseDropChance`

破坏刷怪笼后的掉落概率，范围为 0 到 100，单位为百分比

### `Spawners.Break.StopDropping.Enabled`

是否在挖掘一定数量的刷怪笼后停止掉落

### `Spawners.Break.StopDropping.After`

玩家最多可挖掘的刷怪笼数量，达到后掉落概率设为 0<br>
按玩家统计中的刷怪笼总挖掘数计算，也包含未成功掉落的次数，请据此调整<br>
也可通过 cmi.dropspawner.stopafter.\[positivevalue\] 权限指定上限

### `Spawners.Break.StopDropping.Linear`

启用后，掉落概率按上述上限和已挖掘数量逐渐降低<br>
达到上述上限之前，掉落概率不会低于 1%

### `Spawners.Place.Enabled`

开启或关闭刷怪笼放置处理<br>
启用后，按刷怪笼物品的生物类型放置<br>
关闭后，按普通方式放置，交由其他插件处理

### `Spawners.Place.RequiresPermission`

设为 true，按生物类型放置刷怪笼需要对应权限

### `Spawners.Place.RequiresExactPermission`

需要先将 RequiresPermission 设为 true。启用此项后，每种刷怪笼都需要单独的放置权限<br>
例如放置猪刷怪笼需要 cmi.placespawner.pig，僵尸刷怪笼需要 cmi.placespawner.zombie<br>
设为 false，只需基础权限 cmi.placespawner 即可放置任意类型刷怪笼

### `Spawners.Interact.Spawner.RequiresPermission`

设为 true，使用刷怪蛋修改刷怪笼需要对应权限<br>
例如改为猪需要 cmi.egginteract.pig，改为僵尸需要 cmi.egginteract.zombie

### `Spawners.Interact.TrialSpawner.RequiresPermission`

设为 true，使用刷怪蛋修改试炼刷怪笼需要对应权限<br>
例如改为猪需要 cmi.trialegginteract.pig，改为僵尸需要 cmi.trialegginteract.zombie

### `Spawners.TnTExplosionDrop`

设为 true，TNT 炸毁刷怪笼时有概率掉落

### `Spawners.TnTExplosionDrop.Chance`

刷怪笼掉落概率，单位为百分比

### `Spawners.CreeperExplosionDrop`

设为 true，苦力怕炸毁刷怪笼时有概率掉落

### `Spawners.Charges.Use`

启用后，根据 cmi.spawners.charge.\[groupName\] 权限将玩家分配到对应的刷怪笼挖掘次数组<br>
限制玩家能挖掘的刷怪笼数量<br>
StartingCharge：首次加入该组时获得的挖掘次数<br>
MaxCharge：可同时持有的挖掘次数上限<br>
Cooldown：恢复一次挖掘次数的间隔<br>
Bonus：可选项，放置刷怪笼时，将下一次次数恢复的冷却缩短多少秒<br>
可通过 cmi.spawners.charge.bypass 绕过限制

### `Spawners.Charges.BreakWithoutCharge`

设为 true，挖掘次数用尽后，破坏刷怪笼会将其摧毁而不掉落

### `Spawners.Proximity.Use`

限制刷怪笼之间的最小放置间距

### `Spawners.Proximity.Range`

以放置位置为中心的半径，单位为方块，最大范围为 16<br>
可通过 cmi.spawners.proximity.bypass 绕过

## `ItemRenaming`

### `ItemRenaming.Prevent`

设为 true，禁止通过铁砧或 itemname 命令为指定物品改名<br>
可使用正则表达式匹配指定名称<br>
可通过 cmi.anvil.itemrename.bypass 绕过

### `ItemRenaming.GlobalDisable`

设为 true，全面禁止通过铁砧或命令改名，不论物品材质<br>
可通过上面的权限绕过

### `ItemRenaming.MaxLength`

itemname 命令允许的物品名称最大长度，不含颜色代码<br>
设为 0 取消限制

### `ItemRenaming.Anvil.ItalicByDefault`

启用后，为物品名称添加颜色时强制使用斜体，模拟原版物品改名效果

### `ItemRenaming.CheckSource`

启用后，除最终名称外，也检查原物品<br>
可让特定名称的物品完全无法改名，同时防止其他物品改为这些名称

### `ItemRenaming.List`

材质列表，可在材质后附正则表达式。例如禁止将某种刷怪笼改名为另一种，但仍允许改为其他名称<br>
用 \* 表示全部材质，例如 \*:(\[A-z\])

## `SpawnMob`

### `SpawnMob.MaxQuantity`

一次最多可生成的乘客实体数量

## `Counter`

### `Counter.Range`

/counter start 使用的默认范围

## `Mirror`

### `Mirror.MaxRange`

允许在距离镜像中心多远的位置建造，单位为方块<br>
主要防止忘记关闭镜像后，又在地图其他位置开始建造

### `Mirror.MaxBlocks`

单次最多修改的方块数<br>
每个方块都需要单独检查，请保持较低数值，避免额外负载

### `Mirror.BreakDisabled`

关闭后，镜像模式不执行方块破坏<br>
主要避免此功能被用于挖矿，而不是建造

## `NetherPortal`

### `NetherPortal.PreventCreation`

可完全阻止创建下界传送门，通过 cmi.netherportalbypass 绕过

### `NetherPortal.MaxHeight`

下界传送门的最大高度，原版为 23

### `NetherPortal.MaxWidth`

下界传送门的最大宽度，原版为 23

## `Portals`

### `Portals.CheckInterval`

检查玩家是否进入传送区域的间隔，单位为毫秒<br>
数值较大可略微降低负载，但玩家移动过快时，可能穿过只有 1 格深且无背墙的传送门而未被传送

### `Portals.CheckParticleInterval`

检查玩家是否进入传送门粒子显示范围的间隔，单位为毫秒

### `Portals.Defaults.PerformCommands`

默认是否允许没有目标位置的传送区域执行命令<br>
仅影响新建的传送区域<br>
设为 true，新建传送区域后，进入时会执行下方命令，而不会传送到其他位置<br>
可在游戏内传送门编辑器中，为每个传送区域单独修改

### `Portals.Defaults.Commands`

发生传送时执行的命令

## `Animations`

### `Animations.SitOnStairs`

允许空手点击楼梯，或看着楼梯使用命令坐下<br>
需要 cmi.command.sit.stairs 权限

### `Animations.DoubleClick`

只有快速双击后，玩家才会坐下

### `Animations.DoubleClickDelay`

启用双击坐下时，两次点击的允许间隔，单位为毫秒

### `Animations.ChairRange`

从玩家位置寻找有效椅子方块的范围，单位为方块

## `DamageControl`

所有可用伤害原因：kill, world\_border, entity\_attack, entity\_sweep\_attack, projectile, suffocation, fall, fire, fire\_tick, melting, lava, drowning, block\_explosion, entity\_explosion, void, lightning, suicide, starvation, poison, magic, wither, falling\_block, thorns, dragon\_breath, fly\_into\_wall, campfire, cramming, dryout, freeze, sonic\_boom, custom<br>
语法：\[permissionNode\]:\[damageCause\]:\[multiplier\]<br>
例如 nolavadamage:lava:0 会让拥有 cmi.damagecontrol.nolavadamage 权限的玩家免疫熔岩伤害<br>
负数会恢复玩家生命值，而不是造成伤害<br>
同一伤害原因有多个匹配权限时，使用列表中最后一个计算最终伤害

### `DamageControl.Enabled`

启用后，可调整部分伤害数值

## `Totem`

### `Totem.RemoveFromInventory`

设为 true，玩家死亡时即使未手持不死图腾，也会使用图腾

### `Totem.RequirePermission`

从物品栏取用图腾是否需要权限<br>
需要先将 RemoveFromInventory 设为 true；启用此项后，玩家还需要 cmi.totem.frominventory 权限

### `Totem.Cooldown.Use`

设为 true，玩家每隔 X 秒才能使用一次不死图腾

### `Totem.Warmup.Use`

设为 true，使用图腾后获得 X 秒保护时间，在此期间死亡可以复活<br>
图腾在激活时消耗；即使在保护时间内未触发复活，也不会退还

### `Totem.ProtectFromVoid`

玩家携带图腾掉入虚空时，将其传送到重生位置并消耗图腾

### `Totem.Effects.Regeneration`

给玩家施加效果的持续时间，单位为秒；设为 0 关闭

### `Totem.BlackListedWorlds`

这些世界中的图腾交由服务端按默认行为处理

### `Totem.FullDisableInWorlds`

完全禁用图腾的世界

## `Elytra`

### `Elytra.Boost`

cmi.elytra - 允许使用鞘翅<br>
cmi.elytra.boost - 允许普通加速<br>
cmi.elytra.superboost - 允许超级加速<br>
cmi.elytra.speedometer - 允许查看速度表

### `Elytra.Boost.SpeedLimit`

达到此速度后不再提供加速

### `Elytra.Boost.SpeedLimitStop`

启用后，超出速度上限时不消耗物品或经验

### `Elytra.Boost.SpeedDecimals`

速度是否显示小数

### `Elytra.Boost.GeneralMultyplier`

每次普通加速增加的速度

### `Elytra.Boost.SuperMultyplier`

每次超级加速增加的速度<br>
使用普通加速时按住潜行键

### `Elytra.Boost.UseItems`

消耗指定物品代替经验

### `Elytra.Boost.ConsumedItem`

物品材质名称<br>
每次加速时消耗的物品

### `Elytra.Boost.Item`

物品材质名称<br>
设为 AIR，允许不手持特定物品加速<br>
设为 AIR 时，仍需手持任意物品，或点击鼠标左键才能生效

### `Elytra.Boost.LaunchItem`

物品材质名称<br>
设为 AIR，允许不手持特定物品起飞<br>
设为 AIR 时，仍需手持任意物品，或看着方块才能正常生效

### `Elytra.Boost.RequiresItem`

需要手持指定物品，仅在 UseItems 为 false 时生效

### `Elytra.Boost.Amount`

每次普通加速消耗的经验点数

### `Elytra.Boost.SuperAmount`

每次超级加速消耗的经验点数

### `Elytra.Boost.ShowParticles`

飞行时显示粒子

### `Elytra.DisableRiptide`

适用于 1.13+：是否禁止鞘翅飞行时使用三叉戟的激流附魔<br>
这种组合可能让玩家达到极高速度

### `Elytra.Fix.PreventSelfDamage`

禁止飞行时通过箭矢伤害自己来加速

### `Elytra.Fix.PreventRocketUsage`

禁止使用烟花火箭为鞘翅加速

## `FlightCharge`

### `FlightCharge.ShowBossBar`

默认持续通过 Boss 栏显示剩余飞行能量。关闭后，只在能量发生修改时显示，不在飞行消耗期间显示

### `FlightCharge.EnabledByDefault`

设为 true，获得飞行能量或重新登录后，自动开启飞行模式<br>
设为 false，玩家需要手动执行 /cmi flyc 开启飞行

### `FlightCharge.AutoSwitch`

设为 true，从生存或冒险模式切换到创造或旁观模式时，关闭飞行能量模式<br>
从创造或旁观切换回生存或冒险时，也同样处理

### `FlightCharge.ExpRechargeCost`

每点飞行能量消耗的经验点数。可填 0.2 等小数，但不能小于或等于 0<br>
设为 0 关闭这种补充方式

### `FlightCharge.MoneyRechargeCost`

每点飞行能量的价格。可填 0.2 等小数，但不能小于或等于 0<br>
设为 0 关闭这种补充方式

### `FlightCharge.MaxChargeLevel`

玩家飞行能量上限<br>
飞行时每移动一个方块消耗一点能量<br>
悬停不动时，每秒消耗一点能量

### `FlightCharge.DeductOnIdling`

悬停不动时，每秒消耗能量的倍率<br>
设为 0 关闭

### `FlightCharge.DeductOnlyForTime`

设为大于 0 的值后，按飞行秒数扣除指定能量，不再按移动距离计算<br>
设为 0 关闭固定秒耗，改按移动方块数扣除能量

### `FlightCharge.AutoRecharge.From`

玩家通过 /autorecharge 开启自动补充后，剩余能量低于最大值的多少百分比时触发

### `FlightCharge.AutoRecharge.Amount`

每次自动补充的能量占上限的百分比<br>
25 表示每次触发时补充最大能量的 25%

### `FlightCharge.DeductOnFallMulti`

玩家下落时，额外扣除能量的倍率<br>
仅影响超过 3 格高度的下落<br>
例如从 10 格高度落下，扣除 7 \* 2 = 14 点能量<br>
用于防止通过跳下悬崖避开能量消耗<br>
设为 0 关闭此限制

### `FlightCharge.DamageOnFall`

从超过 3 格的高度下落时，是否对玩家造成伤害<br>
即使从 200 格高度落下也不会直接死亡，最低保留 1 点生命值<br>
仅影响主动跳下的玩家，不影响在半空中关闭飞行的玩家

### `FlightCharge.DamageOnToggle`

需要启用 DamageOnFall 才生效<br>
在半空中关闭飞行时，是否对玩家造成伤害

### `FlightCharge.KillOnFall`

需要启用 DamageOnFall 才生效<br>
摔落伤害高于剩余生命值时，是否允许玩家死亡

### `FlightCharge.GlowColor`

填写颜色名称后，玩家开始使用飞行能量飞行时会发光<br>
设为 'none' 关闭

## `Point`

### `Point.DefaultParticle`

point 命令的默认粒子。可用值：fireworks\_spark, smoke, dragon\_breath, crit, magic\_crit, potion\_swirl, potion\_swirl\_transparent, spell, instant\_spell, witch\_magic, note, portal, flying\_glyph, flame, lava\_pop, footstep, splash, particle\_smoke, explosion\_huge, explosion\_large, explosion, void\_fog, small\_smoke, cloud, coloured\_dust, dust, snowball\_break, waterdrip, lavadrip, snow\_shovel, slime, heart, villager\_thundercloud, happy\_villager, large\_smoke, water\_bubble, water\_wake, suspended, barrier, mob\_appearance, end\_rod, damage\_indicator, sweep\_attack, totem, spit, squid\_ink, bubble\_pop, current\_down, bubble\_column\_up, nautilus, dolphin, water\_splash, campfire\_signal\_smoke, campfire\_cosy\_smoke, sneeze, composter, flash, falling\_lava, landing\_lava, falling\_water, dripping\_honey, falling\_honey, landing\_honey, falling\_nectar, soul\_fire\_flame, ash, crimson\_spore, warped\_spore, soul, dripping\_obsidian\_tear, falling\_obsidian\_tear, landing\_obsidian\_tear, reverse\_portal, white\_ash, light, falling\_spore\_blossom, spore\_blossom\_air, small\_flame, snowflake, dripping\_dripstone\_lava, falling\_dripstone\_lava, dripping\_dripstone\_water, falling\_dripstone\_water, glow\_squid\_ink, glow, wax\_on, wax\_off, electric\_spark, scrape, block\_marker, sonic\_boom, sculk\_soul, sculk\_charge\_pop, cherry\_leaves, small\_gust, trial\_spawner\_detection\_ominous, vault\_connection, infested, item\_cobweb, ominous\_spawning, raid\_omen, trial\_omen, poof, explosion\_emitter, firework, bubble, fishing, underwater, enchanted\_hit, effect, instant\_effect, entity\_effect, witch, dripping\_water, dripping\_lava, mycelium, enchant, item\_snowball, item\_slime, item, block, rain, elder\_guardian, falling\_dust, totem\_of\_undying, dust\_color\_transition, vibration, sculk\_charge, shriek, egg\_crack, dust\_plume, white\_smoke, gust, gust\_emitter\_large, gust\_emitter\_small, trial\_spawner\_detection, dust\_pillar, pale\_oak\_leaves, tinted\_leaves, block\_crumble, trail, firefly

## `Messages`

### `Messages.Login.Disabled`

设为 true，不显示加入消息

### `Messages.Login.AutoHideFrom`

在线人数达到多少时，自动隐藏加入消息<br>
设为 -1 关闭

### `Messages.Login.Custom.Use`

设为 true，使用自定义加入消息；可通过 cmi.messages.disablelogin 关闭指定玩家的消息

### `Messages.Login.Custom.ServerSwitch`

启用后，如果 BungeeCord 安装了 CMIB，会尝试判断玩家切服情况，并尽可能用切服消息代替加入消息

### `Messages.Logout.Disabled`

设为 true，不显示退出消息

### `Messages.Logout.AutoHideFrom`

在线人数达到多少时，自动隐藏退出消息<br>
设为 -1 关闭

### `Messages.Logout.Custom.Use`

设为 true，使用自定义退出消息；可通过 cmi.messages.disablequit 关闭指定玩家的消息

### `Messages.Logout.Custom.ServerSwitch`

启用后，如果 BungeeCord 安装了 CMIB，会尝试判断玩家切服情况，并尽可能用切服消息代替退出消息

### `Messages.FirstJoinMessage`

翻译及自定义占位符见语言文件：\[playername\]、\[totalUsers\]、\[onlinePlayers\]

### `Messages.Filter`

启用后，用指定正则表达式检查玩家名称，匹配时不显示相应的加入或退出消息

## `Books`

### `Books.DefaultAuthor`

getbook 命令生成书籍时使用的默认作者名称

### `Books.AddDate`

设为 true，在书籍中添加编写日期

## `Motd`

玩家登录时显示的 customtext 名称；填入不存在的 customText 名称即可关闭

## `Warnings`

### `Warnings.Default`

应始终保留。警告玩家时未指定类别，就使用此项

### `Warnings.Default.LifeTime`

此警告对玩家的有效时长，单位为秒

### `Warnings.Default.Points`

每次警告给予的警告点数

### `Warnings.Default.DefaultReason`

警告时未提供原因，使用的默认原因

## `Spawn`

### `Spawn.SpawnOnJoin`

玩家登录时，强制传送到指定出生点<br>
可通过 cmi.spawnonjoin.bypass 权限绕过

### `Spawn.IgnoredWorlds`

忽略的世界列表。玩家在这些世界登录时，保留退出位置，不传送到对应出生点

### `Spawn.Main`

设为 true，此位置也作为死亡重生点；否则只用于 /cmi spawn<br>
RespawnLocation 表示是否将此位置作为死亡后的可用重生点<br>
TeleportFrom 指定从哪些世界登录的玩家会被传送到此出生点

### `Spawn.FirstSpawn`

玩家首次加入服务器时的出生位置

## `Newbie`

### `Newbie.Kit`

给予新玩家的礼包名称

## `Kits`

### `Kits.GUI`

设为 true，通过界面显示礼包列表，而不是聊天消息

### `Kits.FillEmptyFields`

设为 true，用默认物品填充礼包选择界面的空槽，见 CMILib

### `Kits.KitPreview`

启用后，玩家可预览有权领取的礼包，或具有 cmi.kit.\[kitName\].preview、cmi.kit.\[kitName\].\* 权限的礼包

### `Kits.DateFormat`

{DATE} 的显示格式

### `Kits.Buttons.Cooldown`

礼包预览界面的图标<br>
将图标设为无效物品可隐藏按钮

### `Kits.Complex.InfoButton.Use`

额外按钮，可用于点击后显示补充信息

## `Warps`

### `Warps.GUI`

设为 true，通过界面显示传送点列表，而不是聊天消息

### `Warps.GUIOnCreation`

创建新传送点后自动打开界面

### `Warps.MinLength`

传送点名称的最小长度

### `Warps.MaxLength`

传送点名称的最大长度

### `Warps.perPage`

每页显示的传送点数量

### `Warps.showCreator`

是否在传送点列表中显示创建者

### `Warps.requirePerm`

设为 true，新建传送点默认需要权限才能使用

### `Warps.Complex.InfoButton.Use`

额外按钮，可用于点击后显示补充信息

## `DynamicViewRange`

### `DynamicViewRange.Enabled`

设为 true，启用动态视距。此功能仍为测试版，可能增加 CPU 负载<br>
服务器不使用此功能时，请不要开启

## `WorldLimits`

### `WorldLimits.Enabled`

设为 true，切换世界时，对没有相应绕过权限的玩家应用该世界的飞行和游戏模式限制

### `WorldLimits.Gamemode`

各世界的默认游戏模式<br>
拥有 cmi.worldlimit.gamemode.bypass 权限时，不改变游戏模式<br>
可用模式：creative、survival、adventure、spectator

### `WorldLimits.Fly`

拥有 cmi.worldlimit.fly.bypass 权限时，不改变飞行状态

### `WorldLimits.ReenabledFlyAfterDeath`

启用后，玩家死亡前正在飞行，重生后仍可飞行

### `WorldLimits.ElytraFlight`

拥有 cmi.worldlimit.elytra.bypass 权限时，不限制鞘翅飞行<br>
进入禁用鞘翅飞行的世界时，会尽可能卸下玩家的鞘翅

### `WorldLimits.FlyAboveRoof`

设为 false，只有拥有 cmi.worldlimit.fly.aboveroof 权限的玩家才能飞到世界建造高度以上

### `WorldLimits.FlyAboveRoofLimitations`

设为 false，只有拥有 cmi.worldlimit.fly.aboveroof 权限的玩家才能飞到世界建造高度以上

### `WorldLimits.GodMode`

拥有 cmi.worldlimit.god.bypass 权限时，不改变上帝模式

### `WorldLimits.SpawnReasons`

在指定世界阻止特定原因的实体生成。可用原因：NATURAL, JOCKEY, CHUNK\_GEN, SPAWNER, TRIAL\_SPAWNER, EGG, SPAWNER\_EGG, LIGHTNING, BUILD\_SNOWMAN, BUILD\_IRONGOLEM, BUILD\_COPPERGOLEM, BUILD\_WITHER, VILLAGE\_DEFENSE, VILLAGE\_INVASION, BREEDING, SLIME\_SPLIT, REINFORCEMENTS, NETHER\_PORTAL, DISPENSE\_EGG, INFECTION, CURED, OCELOT\_BABY, SILVERFISH\_BLOCK, MOUNT, TRAP, ENDER\_PEARL, SHOULDER\_ENTITY, DROWNED, SHEARED, EXPLOSION, RAID, PATROL, BEEHIVE, PIGLIN\_ZOMBIFIED, SPELL, FROZEN, METAMORPHOSIS, DUPLICATION, COMMAND, ENCHANTMENT, OMINOUS\_ITEM\_SPAWNER, BUCKET, POTION\_EFFECT, REANIMATE, REHYDRATION, CUSTOM, DEFAULT

## `CheckForNameChange`

检查玩家名称是否与上次记录的不同

### `CheckForNameChange.PerformCommandsOnNewName`

是否执行命令

### `CheckForNameChange.NameChangeCommands`

玩家使用新名称登录时执行的命令

## `inv`

### `inv.SaveOnDeath`

是否在玩家死亡时保存物品栏

### `inv.IgnoreEmpty`

设为 true，死亡时物品栏为空则不保存

### `inv.RequiresPermission`

设为 true，玩家必须拥有 cmi.saveinv 权限，死亡时才保存物品栏

### `inv.SavedInventories`

每名玩家保留的物品栏记录数量

### `inv.restore.HP`

设为 false，通过 /cmi invload 恢复物品栏时不恢复生命值

### `inv.restore.XP`

设为 false，不恢复经验点数

### `inv.restore.Food`

设为 false，不恢复饥饿值

### `inv.restore.Saturation`

设为 false，不恢复饱和度

### `inv.restore.Potions`

设为 false，不恢复药水效果

### `inv.restore.Items`

设为 false，不恢复物品

### `inv.restore.BlackListedItems`

不保存的材质列表<br>
羊毛、潜影盒等有颜色变种的物品，可能需要列出每种颜色的材质

## `hunger`

### `hunger.overide`

是否允许玩家的饥饿值超过 20

## `heal`

### `heal.RemoveNegative.use`

治疗玩家时，是否移除负面药水效果

## `Cuff`

### `Cuff.Mute`

设为 false，允许被铐住的玩家聊天

## `Mute`

### `Mute.DenyPrivateMessages`

设为 true，被禁言的玩家也无法发送私聊

## `Dispose`

### `Dispose.UILines`

垃圾桶界面的行数，范围为 1–6

### `Dispose.CustomModelData`

是否允许丢弃带附加指令的物品

### `Dispose.Materials`

禁止丢弃的材质黑名单

## `ItemRepair`

### `ItemRepair.RepairShare.ProtectNormalRepair`

开启后需要完整重启服务器才生效<br>
启用后，阻止玩家通过普通铁砧为其他人修复物品；本人修复后自己使用不受影响<br>
可通过 cmi.command.repair.repairshare.bypass 绕过

### `ItemRepair.RepairShare.ProtectCommandRepair`

启用后，阻止玩家通过 CMI 命令为其他人修复物品；本人修复后自己使用不受影响

### `ItemRepair.RepairShare.Durability`

其他玩家拾取或在物品栏中选中物品时，将耐久度设为此值。设为 0 或更小的值不修改耐久度<br>
注意！应保持大于 0，否则物品会直接消失，玩家无法再通过其他方式修复，除非这正是预期行为

### `ItemRepair.RepairShare.BypassWithRepairPermission`

设为 true，拥有 cmi.command.repair 权限的玩家可绕过保护，直接使用由其他玩家修复的物品

### `ItemRepair.RepairShare.AddLore`

启用后，玩家不能使用该物品时会追加一行描述；物品所有者不会看到这行提示

### `ItemRepair.RepairShare.CancelEvent`

设为 true，取消交互事件，阻止使用物品

### `ItemRepair.RepairShare.InformWithMessage`

设为 true，提示玩家该物品并非由自己修复

### `ItemRepair.Repair.BlockedCustomDataID`

禁止通过 /repair 修复的自定义模型数据 ID 列表

### `ItemRepair.Repair.Confirmation`

修复需要付费时，玩家必须点击聊天消息确认

### `ItemRepair.Repair.CostsMoney`

设为 true，/cmi repair 按以下设置收取费用<br>
执行命令的玩家支付费用<br>
从控制台执行时，由被修复物品所属的玩家支付费用

### `ItemRepair.Repair.BasePrice`

物品的基础修复价格<br>
启用耐久度检查后，此费用会根据物品损坏程度变化

### `ItemRepair.Repair.CheckDurability`

根据物品损坏程度计算修复费用

### `ItemRepair.Repair.WorthPercentage`

根据 /cmi setworth 设置的物品价格追加费用<br>
取值范围为 0 到 100

### `ItemRepair.Repair.enchantWorthPercentage`

根据 /cmi setenchantworth 设置的附魔价格追加费用<br>
取值范围为 0 到 100<br>
有多个附魔时，将各项费用相加

## `Cooldowns`

### `Cooldowns.Enabled`

可以为任意命令设置冷却，防止连续立即使用<br>
cmi heal:180 表示每 180 秒只能执行一次 /cmi heal<br>
冷却设为 -1 时，该命令只能执行一次<br>
管理员可通过 cmi.cooldownbypass.\[commandname\] 绕过<br>
始终使用完整命令名称，不要使用别名<br>
也可使用 cmi.cooldown.\[some\_command\].\[timer\] 权限，例如 cmi.cooldown.cmi\_heal.30 为 /cmi heal 设置 30 秒冷却<br>
要在带参数时才应用冷却，在命令末尾加 \_。例如 cmi.cooldown.cmi\_heal\_.30 只限制治疗其他玩家的用法<br>
注意！必须先在列表中设置基础命令冷却，权限才会生效<br>
注意！若要限制 /cmi home 传送，但不限制打开界面，在命令后保留空格，例如 "cmi home :10"

## `ShulkerBoxes`

### `ShulkerBoxes.PreventInCombat`

设为 true，战斗期间不允许打开潜影盒<br>
战斗判定时间可在 combat 部分设置

### `ShulkerBoxes.RequirePermission`

设为 true，从物品栏编辑潜影盒内容需要 cmi.openshulker.edit 权限

### `ShulkerBoxes.CostToOpen`

从物品栏打开潜影盒的费用，余额不足时不允许打开<br>
设为 0 关闭费用要求<br>
可通过 cmi.openshulker.free 权限绕过

## `Vanish`

### `Vanish.Defaults`

隐身编辑选项的默认状态<br>
玩家已经用 vanishedit 修改过隐身选项时，不受此默认值影响

## `Player`

### `Player.Options.InfoButton.Use`

额外按钮，可用于点击后显示补充信息

### `Player.Options.Defaults`

玩家选项的默认状态<br>
玩家已经用 /cmi options 修改过选项时，不受此默认值影响

### `Player.Options.Defaults.chatSpy`

强烈不建议启用！

### `Player.Options.Defaults.cmdSpy`

强烈不建议启用！

### `Player.Options.Defaults.signSpy`

强烈不建议启用！

## `WarmUps`

### `WarmUps.Enabled`

可以为任意命令设置预热，避免立即执行<br>
tp:5:false 表示执行 /tp 后等待 5 秒，且不能移出当前方块<br>
tp:5:false-3 表示执行 /tp 后等待 5 秒，期间只能在原位置 3 格以内移动<br>
false 为可选参数，设为 false 时预热期间禁止移动<br>
若只限制带参数的 warp，而不限制无参数用法，在命令后加空格，例如 'warp :5:false'<br>
为 CMI 命令设置预热时，使用完整命令而非别名，例如 'cmi warp:5:false'<br>
管理员可通过 cmi.warmupbypass.\[commandname\] 绕过<br>
注意！cmi home 使用特殊处理方式，请添加空格以避免重复预热，例如：- cmi home :5:false<br>
实验性功能：在预热设置中添加 GlyphHead，可在预热期间显示粒子效果，例如

```text
- cmi warp :3:false:GlyphHead
```

### `WarmUps.BossBarInfo.Segments`

可用值：1、6、10、12、20

## `Jail`

### `Jail.CheckInterval`

检查玩家是否离开监狱区域的间隔，单位为毫秒<br>
数值较大可略微降低服务器负载

### `Jail.DefaultTime`

命令未提供时长时使用的默认监禁时间

### `Jail.ChatRange`

监禁期间的聊天范围，单位为方块<br>
设为 0 允许聊天<br>
设为 -1，监禁期间完全禁止聊天

### `Jail.CountWhileOffline`

设为 true，玩家离线时也计入服刑时间<br>
设为 false，只在玩家在线时减少剩余刑期

### `Jail.NoAfk`

设为 true，监禁期间进入 AFK 状态时，不减少剩余刑期<br>
设为 false，照常计算时间

### `Jail.PreventDamage`

监禁期间是否阻止玩家受到伤害

### `Jail.PreventHunger`

监禁期间是否阻止玩家饥饿

### `Jail.Commands.OnJail`

玩家入狱时执行的命令

### `Jail.Commands.OnUnJail`

玩家出狱时执行的命令

### `Jail.WhiteListedCmds`

将 CMI 命令加入白名单时，使用完整名称，不要使用缩写别名

## `scan`

### `scan.SoftCap`

低于此 TPS 时，开始调整扫描速度

### `scan.DefaultSpeed`

初始扫描速度，范围为 1 到 30

### `scan.DefaultRange`

范围单位为区块：2 表示 9 个区块（3x3），1 表示当前区块，0 表示全局扫描

### `scan.LogIntoFile`

启用后，将 scan 结果写入文件，便于之后查看

## `search`

### `search.LogIntoFile`

启用后，将 search 结果写入文件，便于之后查看

### `search.EnablePurge`

设为 true，搜索时删除找到的物品，例如 /cmi search diamondaxe purge

## `purge`

removeuser 在删除或移动玩家数据文件时，也使用相同配置

### `purge.CleanOnStart`

服务器启动时清理文件

### `purge.OfflineDays`

玩家离线多久后移动其数据

### `purge.CMIData.Enabled`

是否清理 CMI 中的玩家数据记录

### `purge.PlayerData.Enabled`

是否清理玩家数据文件

### `purge.PlayerData.SourceFolder`

读取文件的来源文件夹

### `purge.PlayerData.DeleteFiles`

设为 false，将文件移动到备份文件夹；设为 true，直接删除

### `purge.PlayerData.DestinationFolder`

DeleteFiles 为 false 时，文件移动到的目标文件夹

### `purge.PlayerStats.Enabled`

是否清理玩家统计文件

### `purge.PlayerStats.SourceFolder`

读取文件的来源文件夹

### `purge.PlayerStats.DeleteFiles`

设为 false，将文件移动到备份文件夹；设为 true，直接删除

### `purge.PlayerStats.DestinationFolder`

DeleteFiles 为 false 时，文件移动到的目标文件夹

### `purge.PlayerAdvancements.Enabled`

是否清理玩家进度文件

### `purge.PlayerAdvancements.SourceFolder`

读取文件的来源文件夹

### `purge.PlayerAdvancements.DeleteFiles`

设为 false，将文件移动到备份文件夹；设为 true，直接删除

### `purge.PlayerAdvancements.DestinationFolder`

DeleteFiles 为 false 时，文件移动到的目标文件夹

### `purge.Essentials.Enabled`

是否清理 Essentials 玩家数据文件

### `purge.Essentials.SourceFolder`

读取文件的来源文件夹

### `purge.Essentials.DeleteFiles`

设为 false，将文件移动到备份文件夹；设为 true，直接删除

### `purge.Essentials.DestinationFolder`

DeleteFiles 为 false 时，文件移动到的目标文件夹

### `purge.LWC.Enabled`

是否清理 LWC 保护记录

## `Selection`

### `Selection.Tool`

选择区域时使用的工具材质名称

## `Time`

### `Time.Day`

预设时间

### `Time.AutoTime.Interval`

将游戏时间与现实时间同步的间隔，单位为秒<br>
建议保持在约一分钟

### `Time.AutoTime.Smooth`

默认使用太阳平滑移动的方式切换时间<br>
可通过 time 命令的 -smooth 参数覆盖

### `Time.AutoTime.SmoothSpeed`

平滑切换速度<br>
100 表示太阳以正常速度的 100 倍移动，直到目标时间

### `Time.AutoTime.Worlds`

自动时间同步影响的世界

### `Time.TimeSpeed`

可以按需求修改原版时间流逝速度

### `Time.TimeSpeed.world`

单位为秒。原版游戏内 24 小时对应现实中的 1200 秒

### `Time.TimeSpeed.world.day`

默认值：600；开始于第 0 刻，结束于第 12000 刻

### `Time.TimeSpeed.world.sunset`

默认值：90；开始于第 12000 刻，结束于第 13800 刻

### `Time.TimeSpeed.world.night`

默认值：420；开始于第 13800 刻，结束于第 22200 刻

### `Time.TimeSpeed.world.sunrise`

默认值：90；开始于第 22200 刻，结束于第 24000 刻

## `Enchanting`

### `Enchanting.enchantLimits.Enabled`

关闭后，不再对附魔施加限制<br>
仅影响 enchant 命令，不影响正常附魔

### `Enchanting.RequireSpecificPermission`

设为 true，需要 cmi.enchantments.\[enchantname\] 权限

### `Enchanting.EnforceValidEnchants`

启用后，只允许对物品添加适用的附魔<br>
可通过 cmi.command.enchant.bypassinvalid 绕过

### `Enchanting.PermissionLevelLimit`

设为 true，需要 cmi.enchantments.\[enchantname\].\[maxlevel\] 权限才能附魔到指定最高等级<br>
有多个匹配权限时，取最高等级<br>
不会阻止玩家附魔到低于权限上限的等级<br>
没有指定等级权限的玩家，默认仍可使用 1 级附魔

## `BungeeCord`

### `BungeeCord.Enabled`

若遇到问题，可以完全关闭 BungeeCord 支持<br>
设为 false 后，跨服公共消息、私聊、传送门等功能会停止工作<br>
这些功能在单个服务器内的普通用法不受影响

### `BungeeCord.TabComplete.PlayerNames`

设为 true，将整个 BungeeCord 网络的玩家名称加入 Tab 补全

### `BungeeCord.TabComplete.Servers`

纳入 Tab 补全的服务器列表<br>
留空表示包含全部服务器

### `BungeeCord.BackToPreviousServer`

启用后，/back 可返回上一台服务器，而不只是该服内的上一个位置<br>
仅在玩家切入该服后尚未再次传送时生效

## `Recipes`

### `Recipes.Condense.RequireBackwards`

压缩或解压物品时，检查是否有逆向配方，不能还原时不允许操作<br>
关闭后，忽略逆向配方检查<br>
关闭可能出现非预期结果，例如将 4 块木板转换成工作台

### `Recipes.Condense.4Sized`

是否压缩由 4 个相同材料组成的配方<br>
启用此项且 RequireBackwards 关闭时，橡木木板可能被转换成工作台

## `BlueMap`

### `BlueMap.Warps.Enabled`

是否在 BlueMap 中显示传送点<br>
大多数设置需要重启服务器才生效

### `BlueMap.Warps.Label`

BlueMap 标记的名称

### `BlueMap.Warps.Icon`

图标文件路径；图标大小通常约为 32x32 像素

### `BlueMap.Warps.IconAnchor`

此值通常应为图标尺寸的一半

### `BlueMap.Warps.BlackList`

不显示的传送点名称列表。隐藏的传送点默认已不显示

## `Sounds`

若要完全关闭某个声音，设为 ""

## `PotionEffects`

### `PotionEffects.DeductWhileOffline`

设为 true，玩家离线时药水效果也继续计时<br>
药水效果剩余时间在登录时更新，因此查看离线玩家效果时，可能显示不准确
