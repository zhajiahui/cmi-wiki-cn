---
title: 占位符
---

# 占位符

语言文件可以包含 **PlaceholderAPI** 占位符，并在 CMI 消息中显示。**PlaceHolderAPI** 只会使用以 **%cmi_** 开头的占位符，但 CMI 的大多数地方都可以使用其中的**所有**占位符。

最新的占位符列表始终可以在游戏中执行 **/cmi placeholders** 查看。

也可以在一个占位符中嵌套另一个占位符。例如，**%cmi_equationint_{cmi_user_maxperm_cmi.command.sethome_1}+1****%** 中包含 2 个占位符。首先处理由 **{** 和 **}** 包围的占位符，在这个例子中，它会根据权限节点返回最大值。随后再按普通数学表达式计算，并返回结果。

以下是一些**自定义／非静态**占位符：

## 礼包冷却时间

**%cmi_user_kitcd_[kitName]%** 显示礼包剩余的冷却时间。如果礼包已经可以使用，则显示短横线（`-`）。

## 投票排行榜

**%cmi_votetop_[1-10]%** 显示按投票数排名的前 10 名。

## 物品价格

**%cmi_worth_buy_[itemIdName:data]%** 显示 worth 文件中的物品购买价格。  
**%cmi_worth_sell_[itemIdName:data]%** 显示 worth 文件中的物品出售价格。

例如：**%cmi_worth_buy_diamondsword%**

## 玩家元数据

**%cmi_user_meta_[key]%** 用于自定义占位符。通过 `/cmi usermeta [playerName] [add/remove/clear/list/increment] (key) (value) (-s)` 命令设置。例如，执行 **/cmi usermeta Zrips add testkey Coffee** 后，在 CMI 或其他插件中使用 **%cmi_user_meta_testkey%**，就会得到 **Coffee**。每名玩家的自定义元数据**数量**不受限制，但强烈建议控制在合理范围内。  
**increment** 可以修改数值。例如，执行 **/cmi usermeta Zrips increment counting +0.5** 后，结果为 0.5；再次执行后，结果为 1。可以使用负数减去相应的值。  
**%cmi_user_metaint_[key]%** 会尝试将元数据的值作为**整数**输出。

## 监狱

**%cmi_jail_reason_[jailName]_[cellid]%** 按指定的监狱名称和牢房 ID，显示玩家被监禁的原因，前提是在监禁时设置了原因。如果同一牢房中有多名玩家，则显示最近被关入的玩家的信息。  
**%cmi_jail_time_[jailName]_[cellid]%** 按指定的监狱名称和牢房 ID，显示剩余监禁时间。如果同一牢房中有多名玩家，则显示最近被关入的玩家的信息。  
**%cmi_jail_username_[jailName]_[cellid]%** 按指定的监狱名称和牢房 ID，显示被监禁的玩家名称。如果同一牢房中有多名玩家，则显示最近被关入的玩家的信息。

## 权限检查

**%cmi_user_maxperm_[corePerm]_[defaultValue]%** — 获取权限中的最大数值。例如，玩家拥有以下权限：

- **cmi.command.sethome.1**
- **cmi.command.sethome.3**
- **cmi.command.sethome.4**

那么 **%cmi_user_maxperm_cmi.command.sethome_0%** 就会返回 **4**。其中 0 是默认值，当玩家没有任何带有数值的此类权限节点时使用。

如果占位符中设置的默认值高于玩家权限中的数值，就会使用默认值。在这个例子中，如果使用 **%cmi_user_maxperm_cmi.command.sethome_6%**，就会返回 **6**，而不是 **4**。

## 随机值

**%cmi_random_[from]_[to]%** 返回所给范围内的随机值。例如，**%cmi_random_1_5%** 可能返回 **1 2 3 4 5** 中的任意一个值。可以在一些特殊命令中使用它，让命令执行时产生随机结果。

## BungeeCord

这些占位符用于 BungeeCord 网络。为了获得最佳效果，需要配置网络中各服务器的信息，具体可查看 config.yml 文件中的 **BungeeCord** 部分。

**%cmi_bungee_total_[serverName]%** — 返回该服务器的最大在线人数  
**%cmi_bungee_current_[serverName]%** — 返回当前玩家人数  
**%cmi_bungee_motd_[serverName]%** — 返回该服务器的 motd  
**%cmi_bungee_onlinestatus_[serverName]%** — 返回服务器的在线／离线状态

## 数学表达式求解

**%cmi_equation_[equation]%** 或 **%cmi_equationint_[equation]%** 会计算数学表达式并返回结果。前者可以返回 **2.4** 这样的小数，后者只会返回 **2** 这样的整数。

表达式可以像 **2+2** 一样简单，也可以像 **sin(6)+pi*tan(5)/1.5** 一样复杂。

## 统计数据

**%cmi_user_stats_[mainStat(:optionalSubStat)]%** 按指定条件返回玩家的统计数据，格式与晋升系统使用的格式相同。例如，**%cmi_user_stats_MonsterKills%** 返回击杀怪物的总数，**%cmi_user_stats_MonsterKills:zombie%** 则返回击杀僵尸的总数。  
这个占位符可以返回 **3** 种类型的值：*纯数值*（如生物击杀数）、时间（如总在线时长）和距离。

## 占位符完整列表

在游戏中执行 **/cmi placeholders** 可以查看静态占位符，并看到它们可能输出的值：

- **%cmi_user_charges_left%** – 刷怪笼剩余充能次数
- **%cmi_user_charges_max%** – 刷怪笼允许的最大充能次数
- **%cmi_user_charges_time%** – 距离下一次刷怪笼充能的时间
- **%cmi_user_charges_cooldown%** – 刷怪笼充能冷却时间
- **%cmi_user_display_name%** – 带格式的玩家显示名称
- **%cmi_p_[playerName]_display_name%** – 带格式的玩家显示名称
- **%cmi_user_cleannickname%** – 玩家已设置的昵称；未设置时显示玩家名称。不含颜色代码
- **%cmi_user_nickname%** – 玩家已设置的昵称；未设置时显示玩家名称
- **%cmi_user_name%** – 玩家的原始名称
- **%cmi_p_[playerName]_name%** – 玩家的原始名称
- **%cmi_user_uuid%** – 玩家 UUID
- **%cmi_user_uuid_[playerName]%** – 玩家 UUID
- **%cmi_user_deathloc%** – 玩家上次死亡的位置
- **%cmi_user_backloc%** – 玩家的返回位置
- **%cmi_user_cuffed%** – 玩家是否被铐住
- **%cmi_p_[playerName]_cuffed%** – 玩家是否被铐住
- **%cmi_user_muted%** – 玩家是否被禁言
- **%cmi_p_[playerName]_muted%** – 玩家是否被禁言
- **%cmi_user_inpvp%** – 玩家是否处于 PvP 模式
- **%cmi_user_god%** – 玩家是否开启无敌模式
- **%cmi_p_[playerName]_god%** – 玩家是否开启无敌模式
- **%cmi_user_sneaking%** – 玩家是否正在潜行
- **%cmi_user_mail_count%** – 玩家的邮件数量
- **%cmi_user_warning_count%** – 玩家的警告数量
- **%cmi_user_warning_points%** – 玩家的警告点数
- **%cmi_user_afk%** – 挂机状态
- **%cmi_user_afk_symbol%** – 挂机标记
- **%cmi_user_afk_msg%** – 挂机消息（如果有）
- **%cmi_user_afk_for%** – 玩家已挂机的时长
- **%cmi_user_afk_in%** – 玩家进入自动挂机模式的时间
- **%cmi_user_spy%** – 监听状态
- **%cmi_user_cmdspy%** – 命令监听状态
- **%cmi_user_signspy%** – 告示牌监听状态
- **%cmi_user_joinedcounter%** – 玩家是否已加入 counter
- **%cmi_user_banned%** – 玩家是否被封禁
- **%cmi_p_[playerName]_banned%** – 玩家是否被封禁
- **%cmi_user_maxhomes%** – 玩家最多可以拥有的家数量
- **%cmi_user_homeamount%** – 玩家已有的家数量
- **%cmi_user_homelist%** – 玩家的家列表
- **%cmi_user_missingexp%** – 距离下一级还差的经验值
- **%cmi_user_missingexpp%** – 距离下一级还差的经验百分比
- **%cmi_user_exp%** – 当前等级内已有的经验值
- **%cmi_user_expp%** – 当前等级内已有的经验百分比
- **%cmi_user_totalexp%** – 玩家拥有的总经验值
- **%cmi_user_level%** – 玩家等级
- **%cmi_user_ping%** – 延迟
- **%cmi_user_gamemode%** – 游戏模式
- **%cmi_user_op%** – OP 状态
- **%cmi_user_pweather%** – 玩家的个人天气
- **%cmi_user_weather%** – 玩家所在世界的天气
- **%cmi_user_weatherduration%** – 玩家所在世界的天气持续时间
- **%cmi_user_canfly%** – 玩家是否具有飞行能力
- **%cmi_user_flying%** – 玩家当前是否正在飞行
- **%cmi_user_vanished_symbol%** – 隐身标记
- **%cmi_user_balance_formated%**
- **%cmi_user_balance_formatted%** – 带格式的玩家余额
- **%cmi_user_balance%** – 不带格式的玩家余额
- **%cmi_user_prefix%** – 权限插件设置的玩家前缀
- **%cmi_user_suffix%** – 权限插件设置的玩家后缀
- **%cmi_user_group%** – 玩家主要权限组的名称
- **%cmi_user_nameplate_prefix%** – 玩家头顶名称的前缀
- **%cmi_user_nameplate_suffix%** – 玩家头顶名称的后缀
- **%cmi_user_tfly%** – 临时飞行的剩余时间，单位为秒
- **%cmi_user_tfly_formated%**
- **%cmi_user_tfly_formatted%** – 带格式的临时飞行时间
- **%cmi_user_flightcharge%** – 飞行能量
- **%cmi_user_tgod%** – 临时无敌模式的时间，单位为秒
- **%cmi_user_tgod_formated%**
- **%cmi_user_tgod_formatted%** – 带格式的临时无敌模式时间
- **%cmi_user_votecount%** – 投票数
- **%cmi_user_dailyvotecount%** – 每日投票数
- **%cmi_user_chatcolor%** – 玩家的聊天颜色
- **%cmi_user_rank%**
- **%cmi_user_rank_displayname%** – 当前等级的显示名称
- **%cmi_user_rank_name%** – 当前等级的名称
- **%cmi_user_nextranks%** – 后续等级列表
- **%cmi_user_nextrankpercent%** – 下一等级的晋升进度百分比
- **%cmi_user_nextvalidranks%** – 玩家可以晋升到的等级列表
- **%cmi_user_canrankup%** – 玩家可以晋升时返回 true
- **%cmi_user_country%** – GeoIP 功能提供的玩家所在国家，例如 Germany
- **%cmi_user_country_code%** – GeoIP 功能提供的玩家所在国家代码，例如 UK
- **%cmi_user_city%** – GeoIP 功能提供的玩家所在城市名称
- **%cmi_user_name_colorcode%** – nameplate 命令中 -c: 参数设置的 Bukkit 颜色代码
- **%cmi_user_glow_code%** – glow 命令设置的 Bukkit 颜色代码
- **%cmi_user_glow_name%** – glow 命令设置的颜色名称，例如 Red
- **%cmi_user_jailed%** – 玩家是否被监禁，返回 true 或 false
- **%cmi_p_[playerName]_jailed%** – 玩家是否被监禁，返回 true 或 false
- **%cmi_user_jailname%** – 玩家当前所在的监狱名称，例如 Prison
- **%cmi_p_[playerName]_jailname%** – 玩家当前所在的监狱名称，例如 Prison
- **%cmi_user_jailcell%** – 玩家当前所在的牢房 ID，例如 1
- **%cmi_p_[playerName]_jailcell%** – 玩家当前所在的牢房 ID，例如 1
- **%cmi_user_jailtime%** – 剩余监禁时间，例如 1hour 5minutes
- **%cmi_p_[playerName]_jailtime%** – 剩余监禁时间，例如 1hour 5minutes
- **%cmi_user_jailreason%** – 被监禁的原因
- **%cmi_p_[playerName]_jailreason%** – 被监禁的原因
- **%cmi_user_jailedby%** – 执行监禁者的名称
- **%cmi_p_[playerName]_jailedby%** – 执行监禁者的名称
- **%cmi_user_riding%** – 玩家正在骑乘的实体名称
- **%cmi_user_beingriddenby%** – 正在骑乘该玩家的玩家名称
- **%cmi_user_bungeeserver%** – Bungee 服务器名称
- **%cmi_user_rt_cooldown%** – 随机传送的剩余冷却时间
- **%cmi_user_rt_cooldown_[worldName]%** – 指定世界中随机传送的剩余冷却时间
- **%cmi_user_playtime_formatted%** – 带格式的在线时长
- **%cmi_user_playtime_days%** – 以天为单位的在线时长
- **%cmi_user_playtime_dayst%** – 以天为单位、包含小数的在线时长
- **%cmi_user_playtime_hours%** – 以小时为单位的在线时长
- **%cmi_user_playtime_hoursf%** – 以小时为单位的总在线时长
- **%cmi_user_playtime_hourst%** – 以小时为单位、包含小数的总在线时长
- **%cmi_user_playtime_minutes%** – 以分钟为单位的在线时长
- **%cmi_user_playtime_minutest%** – 以分钟为单位的总在线时长
- **%cmi_user_playtime_seconds%** – 以分钟为单位的在线时长
- **%cmi_user_playtime_secondst%** – 以分钟为单位的总在线时长
- **%cmi_user_prewards_count%** – 可领取的在线时长奖励数量
- **%cmi_user_world_formatted%** – 使用自定义标识显示的玩家当前所在世界名称
- **%cmi_user_online%** – 返回玩家的在线状态
- **%cmi_p_[playerName]_online%** – 返回玩家的在线状态
- **%cmi_user_itemcount_[itemIdName(:data)]%** – 玩家背包中指定材质的物品数量
- **%cmi_user_maxperm_[corePerm]_[defaultValue]%** – 指定权限节点中的最大数值；权限不存在时返回默认值
- **%cmi_user_toggle_[holograms|shiftedit|totembar|compass|tagsound|chatspy|cmdspy|signspy|msg|tp|pay|chatbubble|pmsound|rideme|pvenumbers|pvpnumbers|durability|receivepets|deathmessages|notarget|schest|staffchat|autoflightrecharge]%** – 指定功能开启时输出 1，关闭时输出 0
- **%cmi_user_togglename_[holograms|shiftedit|totembar|compass|tagsound|chatspy|cmdspy|signspy|msg|tp|pay|chatbubble|pmsound|rideme|pvenumbers|pvpnumbers|durability|receivepets|deathmessages|notarget|schest|staffchat|autoflightrecharge]%** – 指定功能开启时输出带格式的 True，关闭时输出带格式的 False
- **%cmi_user_holo_page_[hologramName]%** – 玩家当前查看的全息文字页码
- **%cmi_equation_[equation]%** – 指定数学表达式的计算结果，保留小数
- **%cmi_equationint_[equation]%** – 指定数学表达式的计算结果，不保留小数
- **%cmi_color_[text]%** – 为文本添加颜色；用 _ 代替空格，要添加下划线则写成 __
- **%cmi_stripcolor_[text]%** – 移除文本中的颜色代码
- **%cmi_iteminhand_displayname%** – 主手物品的显示名称，或带格式的材质名称
- **%cmi_iteminhand_realname%** – 主手物品带格式的材质名称
- **%cmi_iteminhand_type%** – 主手物品的材质名称
- **%cmi_iteminhand_itemdata%** – 主手物品的数据值，1.13+ 版本返回 0
- **%cmi_iteminhand_amount%** – 主手物品数量
- **%cmi_iteminhand_durability%** – 主手物品的剩余耐久度
- **%cmi_iteminhand_maxdurability%** – 主手物品的最大耐久度
- **%cmi_iteminhand_custommodeldata%** – 主手物品的自定义模型数据
- **%cmi_iteminhand_worth%** – 返回主手全部物品的 worth 价格总和
- **%cmi_iteminhand_worth_one%** – 返回主手单个物品的 worth 价格
- **%cmi_iteminhand_worthc%** – 返回主手全部物品的 worth 价格总和，不带格式
- **%cmi_iteminhand_worthc_one%** – 返回主手单个物品的 worth 价格，不带格式
- **%cmi_material_realname_$1%** – 主手物品带格式的材质名称
- **%cmi_schedule_nextin_[schedName]%** – 距离定时任务下次触发的剩余时间
- **%cmi_schedule_endat_[schedName]%** – 距离定时任务执行最后一条命令的剩余时间
- **%cmi_baltop_cname_[1-10]%** – 排行榜指定名次的玩家名称，不带格式
- **%cmi_baltop_name_[1-10]%** – 排行榜指定名次的玩家名称
- **%cmi_baltop_money_[1-10]%** – 排行榜指定名次的玩家余额
- **%cmi_baltop_shortmoney_[1-10]%** – 排行榜指定名次的玩家余额
- **%cmi_playtimetop_cname_[1-10]%** – 排行榜指定名次的玩家名称，不带格式
- **%cmi_playtimetop_name_[1-10]%** – 排行榜指定名次的玩家名称
- **%cmi_playtimetop_time_[1-10]%** – 排行榜指定名次的玩家在线时长
- **%cmi_votetop_[1-10]%** – 排行榜指定名次的玩家名称
- **%cmi_votetopcount_[1-10]%** – 排行榜指定名次的玩家投票数
- **%cmi_worth_buy_[itemIdName(:data)]%** – 物品价格
- **%cmi_worth_sell_[itemIdName(:data)]%** – 物品出售价格
- **%cmi_worthc_buy_[itemIdName(:data)]%** – 不带格式的物品价格
- **%cmi_worthc_sell_[itemIdName(:data)]%** – 不带格式的物品出售价格
- **%cmi_bungee_total_[serverName]%** – 指定服务器允许的最大玩家人数
- **%cmi_bungee_current_[serverName]%** – 指定服务器当前的玩家人数
- **%cmi_bungee_motd_[serverName]%** – 指定服务器的 motd
- **%cmi_bungee_onlinestatus_[serverName]%** – 服务器的在线状态，返回 true/false
- **%cmi_tps_1%** – 最近 1 秒的 TPS
- **%cmi_tps_60%** – 最近 60 秒的 TPS
- **%cmi_tps_300%** – 最近 5 分钟的 TPS
- **%cmi_tps_[range]_colored%** – 指定时间范围内的 TPS
- **%cmi_tps_[range]%** – 指定时间范围内的 TPS
- **%cmi_random_player_name%** – 返回一名随机在线玩家的名称
- **%cmi_lastrandom_player_name%** – 返回上一次随机选中的在线玩家名称
- **%cmi_random_[from]_[to]%** – 指定范围内的随机数
- **%cmi_lastrandom_[playerName]%** – 随机占位符上一次分配给该玩家的随机数
- **%cmi_user_rank_percent_[rankName]%** – 指定等级的晋升进度百分比
- **%cmi_user_meta_[key]%** – 玩家指定键对应的元数据
- **%cmi_user_metaint_[key]%** – 玩家指定键对应的元数据，以数值形式显示
- **%cmi_chatmute_time%** – 全服聊天禁言的剩余时间
- **%cmi_chatmute_reason%** – 全服聊天禁言的原因
- **%cmi_user_baltop%** – 玩家在余额排行榜中的名次
- **%cmi_user_playtimetop%** – 玩家在在线时长排行榜中的名次
- **%cmi_user_stats_[mainStat(:optionalSubStat)]%** – 玩家统计数据
- **%cmi_user_kitcd_[kitName]%** – 指定礼包的冷却时间
- **%cmi_user_kit_available%** – 可以领取的礼包数量
- **%cmi_user_kit_available_[kitName]%** – 礼包是否可用，返回 true/false
- **%cmi_user_kit_hasaccess_[kitName]%** – 玩家是否可以使用该礼包，返回 true/false
- **%cmi_jail_time_[jailName]_[cellId]%** – 牢房的监禁时间
- **%cmi_jail_username_[jailName]_[cellId]%** – 被关在指定牢房中的玩家名称
- **%cmi_jail_reason_[jailName]_[cellId]%** – 指定牢房的监禁原因
- **%cmi_weather_[worldName]%** – 世界天气
- **%cmi_weatherduration_[worldName]%** – 世界天气的持续时间
- **%cmi_afk_count%** – 挂机玩家数量
- **%cmi_maintenance_state%** – 维护状态
- **%cmi_maintenance_message%** – 维护消息
- **%cmi_chat_range%** – 聊天消息的范围
- **%cmi_server_uptime%** – 服务器已运行的时长
- **%cmi_server_uptime_seconds%** – 服务器已运行的时长，单位为秒
- **%cmi_server_worlds%** – 以列表形式显示服务器上所有现有世界
- **%cmi_server_vanished%** – 在线隐身玩家数量
- **%cmi_server_users%** – 已记录的玩家数量
- **%player_world%** – 玩家当前所在世界的名称
- **%cmi_player_world%** – 玩家当前所在世界的名称
- **%player_x%** – 玩家当前的 x 坐标
- **%cmi_player_x%** – 玩家当前的 x 坐标
- **%player_y%** – 玩家当前的 y 坐标
- **%cmi_player_y%** – 玩家当前的 y 坐标
- **%player_z%** – 玩家当前的 z 坐标
- **%cmi_player_z%** – 玩家当前的 z 坐标
- **%player_biome%** – 玩家当前所在生物群系的名称
- **%cmi_player_biome%** – 玩家当前所在生物群系的名称
- **%vault_eco_balance_formatted%** – 带格式的玩家余额。已弃用
- **%server_online%** – 在线玩家人数
- **%cmi_server_online%** – 在线玩家人数
- **%server_max_players%** – 允许的最大玩家人数
- **%cmi_server_max_players%** – 允许的最大玩家人数
- **%server_online_[worldName]%** – 指定世界的在线人数。世界名称中不要使用 _
- **%cmi_server_online_[worldName]%** – 指定世界的在线人数。世界名称中不要使用 _
- **%server_unique_joins%** – 加入过服务器的独立玩家数量
- **%cmi_server_unique_joins%** – 加入过服务器的独立玩家数量
- **%onlineplayers_names%** – 带格式的在线玩家列表
- **%cmi_onlineplayers_names%** – 带格式的在线玩家列表
- **%onlineplayers_displaynames%** – 带格式的在线玩家列表，尽可能使用玩家的显示名称
- **%cmi_onlineplayers_displaynames%** – 带格式的在线玩家列表，尽可能使用玩家的显示名称
- **%server_time_[timeFormat]_[timeZone]%** – 按指定格式和时区显示的服务器时间
- **%cmi_server_time_[timeFormat]_[timeZone]%** – 按指定格式和时区显示的服务器时间
- **%server_time_[timeFormat]%** – 服务器本地时间
- **%cmi_server_time_[timeFormat]%** – 服务器本地时间
- **%world_time12_[worldName]%** – 12 小时制的世界时间
- **%cmi_world_time12_[worldName]%** – 12 小时制的世界时间
- **%world_time24_[worldName]%** – 24 小时制的世界时间
- **%cmi_world_time24_[worldName]%** – 24 小时制的世界时间

---

[查看原文](https://www.zrips.net/cmi/placeholders/)
