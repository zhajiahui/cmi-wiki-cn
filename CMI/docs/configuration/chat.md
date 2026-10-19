---
title: 聊天（Chat.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/Chat.yml
---

# 聊天（Chat.yml）

文件：`plugins/CMI/Settings/Chat.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `Chat`

### `Chat.UsePaperType`

启用后，使用新版聊天处理系统<br>
服务端兼容时，建议保持开启<br>
仅适用于 Paper 1.17+ 服务器<br>
切换聊天处理方式后，需要完整重启服务器

### `Chat.ModifyChatFormat.Enabled`

尝试将聊天消息修改为指定格式<br>
关闭此项并由第三方插件处理聊天时，如果格式出现问题，也可以关闭 ClickHoverMessages

### `Chat.ModifyChatFormat.ClickHoverMessages`

设为 true，普通和私聊消息附带悬停信息，并支持点击快速回复；纯净消息除外，支持 PlaceholderAPI<br>
要修改已发送消息的默认悬停文字，请编辑语言文件中的 Chat 部分<br>
UsePaperType 启用时不生效

### `Chat.DiscordSRV.Enabled`

启用 DiscordSRV 插件支持

### `Chat.DiscordSRV.GlobalChannel`

DiscordSRV 中全局聊天频道的名称

### `Chat.DiscordSRV.Label`

可在聊天格式中使用 {discord}，标记消息来自 Discord 而非游戏内

### `Chat.DiscordSRV.RangedMessages`

启用且设置了聊天范围时，将所有范围聊天消息都发送给 DiscordSRV<br>
关闭后，Discord 只显示喊话，以及拥有 cmi.chat.rangebypass 权限的玩家发送的消息

### `Chat.DynMapChat`

启用 DynMap 网页聊天支持

### `Chat.ReplyToLastMessenger`

设为 false，/r 回复最近主动私聊的对象；若之前没有主动交谈的对象，则回复最近给你发消息的人<br>
设为 true，/r 始终回复最后发来私聊的人；同时收到多人消息时，可能造成混淆

### `Chat.LastMessengerTimeOut`

ReplyToLastMessenger 为 false 时，根据 timeOut 判断回复对象<br>
最近 120 秒内有过交谈时，即使第三个人发来私聊，仍回复原来的玩家，120 秒为默认值<br>
距离上次交谈超过 120 秒后，回复最近发来私聊的人

### `Chat.PrivateMessagesGroups`

设为 true，发送者需要 cmi.command.msg.\[groupname\].send 权限，其中 \[groupName\] 为接收者的主权限组

### `Chat.TranslateLink`

设为 false，聊天中的网址不缩写为默认的 \[LINK\] 格式

### `Chat.LinkRegex`

识别聊天网址并替换为短文本的正则表达式<br>
示例：

```text
(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})
((http|https|ftp|ftps)\:\/\/)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,3}(\/\S*)?
((http|https|ftp|ftps)\:\/\/)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,3}(\/\S*)?([^\s]+)
```

### `Chat.HoverItems.Enabled`

设为 true，将聊天中的指定标记替换为玩家手持物品，标记列表见下方

### `Chat.HoverItems.ReplaceWithIcon`

启用后，用物品图标替代聊天中的物品标记。仅适用于物品，不适用于方块，因为部分方块没有可稳定使用的图标

### `Chat.HoverItems.ItemRegex`

识别聊天物品标记的正则表达式；仅在 CMI 聊天悬停格式启用时有效<br>
若要支持 \[item:helmet\] 或 \[item:5\]，使用 (\\\[item(?::(\\w+))?\\\])；此类正则的第二个分组必须包含自定义值<br>
可用值包括 \[item:mainhand\] \[item:offhand\] \[item:helmet\] \[item:chestplate\] \[item:pants\] \[item:boots\] 和 \[item:0-40\]，数字 0 到 40 表示物品栏槽位<br>
仅识别 \[item\] 时，使用 (\\\[item\\\])

### `Chat.Bungee.Messages`

注意！需要安装 CMI Bungee 插件，可在 zrips.net 找到<br>
或从 https://www.zrips.net/cmi/ 下载<br>
是否启用 BungeeCord 跨服私聊<br>
需要先启用 BungeeCord 支持才生效

### `Chat.Bungee.PublicMessages`

是否启用 BungeeCord 跨服公共聊天<br>
向指定服务器发消息需要 cmi.bungee.publicmessages.\[servername\] 权限

### `Chat.Bungee.PublicMessagesSingleIgnore`

启用后，只发给单个玩家的公共消息不会转发到整个群组服<br>
仅在在线人数超过一人，且聊天范围为全局时生效

### `Chat.Bungee.StaffMessages`

是否启用 BungeeCord 跨服管理聊天

### `Chat.GeneralFormat`

普通聊天格式。可用变量：{displayName} {world} {prefix} {suffix} {group} {shout} {shoutcolor} {message} {nicknameprefix}。支持 %player\_server% %cmi\_user\_chatcolor% 等 PlaceholderAPI 变量<br>
从 1.21.9 Paper 起，可使用 {head} 加入玩家头像<br>
注意！不要直接给此处的 {message} 使用渐变色；请通过 GeneralMessageFormat 设置

### `Chat.GeneralMessageFormat`

消息正文的格式，允许在消息中使用渐变色<br>
必须包含 {message}，否则忽略此设置<br>
1.16+ 可使用渐变色，例如 '{#b3a28f&gt;}{message}{#d7b8e6&lt;}'<br>
渐变可超过 2 种颜色，只需重复 {message}，例如 '{#b3a28f&gt;}{message}{#5c6999&lt;&gt;}{message}{#d7b8e6&lt;}'<br>
使用 %cmi\_user\_chatcolor% 添加玩家选择的聊天颜色

### `Chat.Ranged.General`

普通聊天的传播范围<br>
设为 -1 取消范围限制

### `Chat.Ranged.Shout`

喊话的传播范围<br>
喊话以 ! 开头，玩家需要 cmi.chat.shout 权限<br>
需要启用 GeneralRange<br>
设为 0，喊话覆盖全部世界；设为 -1，关闭喊话

### `Chat.Ranged.ShoutColor`

喊话消息的基础颜色代码

### `Chat.Ranged.ShoutCost`

每条喊话的费用

### `Chat.Ranged.Dynamic`

消息范围限制列表<br>
玩家数量，后接范围<br>
在线人数达到该数量时，使用对应范围

### `Chat.ChatRoomShout`

将消息发到公共聊天，而不是当前聊天室的前缀<br>
设为空文本即可关闭此功能

### `Chat.ChatRoomLife`

空聊天室保留多久后移除，单位为秒<br>
只影响最后一名玩家离开后的空聊天室

### `Chat.ClickSuggestions`

点击公共、私聊等消息时填入的建议命令。可用 \[playerName\]、\[playerDisplayName\]、\[playerNickName\] 插入玩家名称

### `Chat.ClickCommands`

点击玩家名称时，由玩家执行的命令，每种类型一条<br>
设置此项后，ClickSuggestions 的建议命令改为 Shift+左键触发<br>
默认以玩家身份执行；要从控制台执行，在开头添加 asConsole!

### `Chat.GroupFormat`

使用递增数字区分各组；有多个匹配权限时，使用数字较大的一行<br>
可按需要添加任意行<br>
使用权限为 cmi.chatgroup.\[id\]<br>
权限示例：cmi.chatgroup.2

注意！不要直接给此处的 {message} 使用渐变色；请通过 GroupMessageFormat 设置

### `Chat.GroupMessageFormat`

使用递增数字区分各组；有多个匹配权限时，使用数字较大的一行<br>
可按需要添加任意行<br>
使用权限为 cmi.chatmessagegroup.\[id\]<br>
权限示例：cmi.chatmessagegroup.2

### `Chat.Colors.PublicMessage.Enabled`

设为 true，过滤公共聊天中的颜色代码，玩家仅能使用权限允许的颜色

```text
cmi.colors.publicmessage.[colorName]
```

颜色：black(&amp;0), darkblue(&amp;1), darkgreen(&amp;2), darkaqua(&amp;3), darkred(&amp;4), darkpurple(&amp;5), gold(&amp;6), gray(&amp;7), darkgray(&amp;8), blue(&amp;9), green(&amp;a), aqua(&amp;b), red(&amp;c), lightpurple(&amp;d), yellow(&amp;e), white(&amp;f), magic(&amp;k), bold(&amp;l), strikethrough(&amp;m), underline(&amp;n), italic(&amp;o), reset(&amp;r)

### `Chat.Colors.me`

设为 true，过滤 /me 消息中的颜色代码，玩家仅能使用权限允许的颜色

```text
cmi.colors.me.[colorName]
```

### `Chat.Colors.CleanUp`

设为 true，直接移除玩家无权使用的颜色代码，而不是保留在文字中

### `Chat.Colors.CleanUp.WhiteList`

检查玩家无权使用的颜色代码时，忽略的字符串列表<br>
这些内容绕过颜色代码限制，可用于允许特定聊天格式<br>
仅影响公共聊天和私聊

### `Chat.Colors.NickName`

设为 true，玩家修改昵称时过滤颜色代码

```text
cmi.colors.nickname.[colorName]
```

### `Chat.Colors.Picker`

决定 /cmi chatcolor 的内容。可选颜色由 cmi.colors.publicmessage.\[colorCode\] 决定，并用于 %cmi\_user\_chatcolor% 占位符

### `Chat.IgnorePublicMessage`

设为 true，不显示忽略列表中玩家的公共聊天

### `Chat.Tag.Enabled`

是否启用提及系统。公共聊天中在名称前加 @，会提醒被提及的玩家

### `Chat.Tag.HardCoreMode`

设为 true，公共聊天中出现玩家名称时都会着色并提醒对方<br>
比普通 @ 提及更消耗性能，请按需开启

### `Chat.Tag.Color`

@ 名称或昵称的颜色，发送者需要 cmi.tag.color 权限

### `Chat.Tag.CommandsOnTag`

玩家被提及时执行的命令<br>
\[playerName\] 等变量会替换为被提及的玩家名称<br>
可使用 \[senderName\] 插入发起提及的玩家名称

### `Chat.Tag.OnlyWhenAfk`

只在被提及玩家处于 AFK 状态时执行命令

### `Chat.Tag.RemoveEta`

设为 true，移除 @ 符号

## `ChatBubble`

### `ChatBubble.PublicMessages`

是否为公共聊天启用聊天气泡<br>
每名玩家可通过 /options 单独关闭

### `ChatBubble.Offset`

聊天气泡的显示高度

### `ChatBubble.ShowFor`

聊天气泡的基础显示时间，单位为秒

### `ChatBubble.MaxShowFor`

气泡最长显示时间

### `ChatBubble.ExtraTime`

消息中每个字符额外增加的显示秒数<br>
让短消息较快消失，长消息显示更久

### `ChatBubble.PlateScale`

聊天气泡缩放比例，默认为 1

### `ChatBubble.LineWidth`

超过此宽度后自动换行

### `ChatBubble.Background.Color`

默认颜色代码；文字本身有颜色时可覆盖此值<br>
留空使用默认透明颜色<br>
颜色代码示例：{#black}

### `ChatBubble.Background.Opacity`

取值为 0 到 1，0 为无背景色，1 为完全不透明

### `ChatBubble.Shadow`

是否添加文字阴影

### `ChatBubble.Groups`

玩家有多个匹配权限时，优先使用数值较高的组<br>
颜色使用十六进制格式，可选带透明通道的 RGBA 格式
