---
title: 聊天（Chat.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/Chat.yml
---

# 聊天（Chat.yml）

文件：`plugins/CMI/Settings/Chat.yml`

## `Chat` { #chat }

```yaml title="Chat.yml · Chat（1/3）"
Chat:
  # 启用后，使用新版聊天处理系统
  # 服务端兼容时，建议保持开启
  # 仅适用于 Paper 1.17+ 服务器
  # 切换聊天处理方式后，需要完整重启服务器
  UsePaperType: true
  ModifyChatFormat:
    # 尝试将聊天消息修改为指定格式
    # 关闭此项并由第三方插件处理聊天时，如果格式出现问题，也可以关闭 ClickHoverMessages
    Enabled: false
    # 设为 true，普通和私聊消息附带悬停信息，并支持点击快速回复；纯净消息除外，支持 PlaceholderAPI
    # 要修改已发送消息的默认悬停文字，请编辑语言文件中的 Chat 部分
    # UsePaperType 启用时不生效
    ClickHoverMessages: true
  DiscordSRV:
    # 启用 DiscordSRV 插件支持
    Enabled: true
    # DiscordSRV 中全局聊天频道的名称
    GlobalChannel: global
    # 可在聊天格式中使用 {discord}，标记消息来自 Discord 而非游戏内
    Label: '&2[&7D&2]'
    UnlinkedLabel: '&4[&cD&4]'
    # 启用且设置了聊天范围时，将所有范围聊天消息都发送给 DiscordSRV
    # 关闭后，Discord 只显示喊话，以及拥有 cmi.chat.rangebypass 权限的玩家发送的消息
    RangedMessages: true
  # 启用 DynMap 网页聊天支持
  DynMapChat: true
  # 设为 false，/r 回复最近主动私聊的对象；若之前没有主动交谈的对象，则回复最近给你发消息的人
  # 设为 true，/r 始终回复最后发来私聊的人；同时收到多人消息时，可能造成混淆
  ReplyToLastMessenger: false
  # ReplyToLastMessenger 为 false 时，根据 timeOut 判断回复对象
  # 最近 120 秒内有过交谈时，即使第三个人发来私聊，仍回复原来的玩家，120 秒为默认值
  # 距离上次交谈超过 120 秒后，回复最近发来私聊的人
  LastMessengerTimeOut: 120
  # 设为 true，发送者需要 cmi.command.msg.[groupname].send 权限，其中 [groupName] 为接收者的主权限组
  PrivateMessagesGroups: false
  # 设为 false，聊天中的网址不缩写为默认的 [LINK] 格式
  TranslateLink: true
  # 识别聊天网址并替换为短文本的正则表达式
  # 示例：
  # (https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})
  # ((http|https|ftp|ftps)\:\/\/)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,3}(\/\S*)?
  # ((http|https|ftp|ftps)\:\/\/)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,3}(\/\S*)?([^\s]+)
  LinkRegex: (^| )((http|https|ftp|ftps)\:\/\/)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,3}(\/\S*)?([^\s|^\)]+)
  HoverItems:
    # 设为 true，将聊天中的指定标记替换为玩家手持物品，标记列表见下方
    Enabled: true
    # 启用后，用物品图标替代聊天中的物品标记。仅适用于物品，不适用于方块，因为部分方块没有可稳定使用的图标
    ReplaceWithIcon: true
    # 识别聊天物品标记的正则表达式；仅在 CMI 聊天悬停格式启用时有效
    # 若要支持 [item:helmet] 或 [item:5]，使用 (\[item(?::(\w+))?\])；此类正则的第二个分组必须包含自定义值
    # 可用值包括 [item:mainhand] [item:offhand] [item:helmet] [item:chestplate] [item:pants] [item:boots] 和 [item:0-40]，数字 0 到 40 表示物品栏槽位
    # 仅识别 [item] 时，使用 (\[item\])
    ItemRegex:
    - (\[item(?::(\w+))?\])
  Bungee:
    # 注意！需要安装 CMI Bungee 插件，可在 zrips.net 找到
    # 或从 https://www.zrips.net/cmi/ 下载
    # 是否启用 BungeeCord 跨服私聊
    # 需要先启用 BungeeCord 支持才生效
    Messages: true
    # 是否启用 BungeeCord 跨服公共聊天
    # 向指定服务器发消息需要 cmi.bungee.publicmessages.[servername] 权限
    PublicMessages: true
    # 启用后，只发给单个玩家的公共消息不会转发到整个群组服
    # 仅在在线人数超过一人，且聊天范围为全局时生效
    PublicMessagesSingleIgnore: false
    # 是否启用 BungeeCord 跨服管理聊天
    StaffMessages: true
  # 普通聊天格式。可用变量：{displayName} {world} {prefix} {suffix} {group} {shout} {shoutcolor} {message} {nicknameprefix}。支持 %player_server% %cmi_user_chatcolor% 等 PlaceholderAPI 变量
  # 从 1.21.9 Paper 起，可使用 {head} 加入玩家头像
  # 注意！不要直接给此处的 {message} 使用渐变色；请通过 GeneralMessageFormat 设置
  GeneralFormat: '{head} {prefix}&f{displayName}&7: &r{message}'
  # 消息正文的格式，允许在消息中使用渐变色
  # 必须包含 {message}，否则忽略此设置
  # 1.16+ 可使用渐变色，例如 '{#b3a28f>}{message}{#d7b8e6<}'
  # 渐变可超过 2 种颜色，只需重复 {message}，例如 '{#b3a28f>}{message}{#5c6999<>}{message}{#d7b8e6<}'
  # 使用 %cmi_user_chatcolor% 添加玩家选择的聊天颜色
  GeneralMessageFormat: '{message}'
```

```yaml title="Chat.yml · Chat（2/3）"
Chat:
  Ranged:
    # 普通聊天的传播范围
    # 设为 -1 取消范围限制
    General: -1
    # 喊话的传播范围
    # 喊话以 ! 开头，玩家需要 cmi.chat.shout 权限
    # 需要启用 GeneralRange
    # 设为 0，喊话覆盖全部世界；设为 -1，关闭喊话
    Shout: 200
    # 喊话消息的基础颜色代码
    ShoutColor: ''
    # 每条喊话的费用
    ShoutCost: 0
    # 消息范围限制列表
    # 玩家数量，后接范围
    # 在线人数达到该数量时，使用对应范围
    Dynamic:
      Use: false
      Limits:
      - 1-0
      - 10-1000
      - 20-500
      - 30-400
      - 40-300
      - 50-200
  # 将消息发到公共聊天，而不是当前聊天室的前缀
  # 设为空文本即可关闭此功能
  ChatRoomShout: '!'
  # 空聊天室保留多久后移除，单位为秒
  # 只影响最后一名玩家离开后的空聊天室
  ChatRoomLife: 3600
  # 点击公共、私聊等消息时填入的建议命令。可用 [playerName]、[playerDisplayName]、[playerNickName] 插入玩家名称
  ClickSuggestions:
    pubmsg: '/msg [playerNickName] '
    privmsg: '/msg [playerNickName] '
    staffmsg: '/msg [playerNickName] '
    helpop: '/msg [playerNickName] '
    chatroom: '/msg [playerNickName] '
    discord: '/msg [playerNickName] '
  # 点击玩家名称时，由玩家执行的命令，每种类型一条
  # 设置此项后，ClickSuggestions 的建议命令改为 Shift+左键触发
  # 默认以玩家身份执行；要从控制台执行，在开头添加 asConsole!
  ClickCommands:
    pubmsg: ''
    privmsg: ''
    staffmsg: ''
    helpop: ''
    chatroom: ''
    discord: ''
  # 使用递增数字区分各组；有多个匹配权限时，使用数字较大的一行
  # 可按需要添加任意行
  # 使用权限为 cmi.chatgroup.[id]
  # 权限示例：cmi.chatgroup.2

  # 注意！不要直接给此处的 {message} 使用渐变色；请通过 GroupMessageFormat 设置
  GroupFormat:
    '1': '{prefix}&f{displayName}&f: &r{message}'
    '2': '{prefix}&f{displayName}&7: &r{message}'
    '3': '{prefix}&f{displayName}&8: &r{message}'
  # 使用递增数字区分各组；有多个匹配权限时，使用数字较大的一行
  # 可按需要添加任意行
  # 使用权限为 cmi.chatmessagegroup.[id]
  # 权限示例：cmi.chatmessagegroup.2
  GroupMessageFormat:
    '1': '{message}'
    '2': '{message}'
    '3': '{message}'
```

```yaml title="Chat.yml · Chat（3/3）"
Chat:
  Colors:
    PublicMessage:
      # 设为 true，过滤公共聊天中的颜色代码，玩家仅能使用权限允许的颜色
      # cmi.colors.publicmessage.[colorName]
      # 颜色：black(&0), darkblue(&1), darkgreen(&2), darkaqua(&3), darkred(&4), darkpurple(&5), gold(&6), gray(&7), darkgray(&8), blue(&9), green(&a), aqua(&b), red(&c), lightpurple(&d), yellow(&e), white(&f), magic(&k), bold(&l), strikethrough(&m), underline(&n), italic(&o), reset(&r)
      Enabled: true
    PrivateMessage: true
    # 设为 true，过滤 /me 消息中的颜色代码，玩家仅能使用权限允许的颜色
    # cmi.colors.me.[colorName]
    me: true
    # 设为 true，直接移除玩家无权使用的颜色代码，而不是保留在文字中
    CleanUp:
      publicmessage: true
      privatemessage: true
      me: true
      signs: false
      books: true
      itemname: true
      itemlore: true
      # 检查玩家无权使用的颜色代码时，忽略的字符串列表
      # 这些内容绕过颜色代码限制，可用于允许特定聊天格式
      # 仅影响公共聊天和私聊
      WhiteList:
      - '&c❤&7'
    # 设为 true，玩家修改昵称时过滤颜色代码
    # cmi.colors.nickname.[colorName]
    NickName: true
    # 决定 /cmi chatcolor 的内容。可选颜色由 cmi.colors.publicmessage.[colorCode] 决定，并用于 %cmi_user_chatcolor% 占位符
    Picker:
    - '&f'
    - '&2'
    - '&3'
    - '&7'
    - '&8'
    - '&a'
    - '&b'
    - '&c'
    - '&e'
    - '&6'
    - '{#00e625}'
    - '{#brown}'
  # 设为 true，不显示忽略列表中玩家的公共聊天
  IgnorePublicMessage: true
  Tag:
    # 是否启用提及系统。公共聊天中在名称前加 @，会提醒被提及的玩家
    Enabled: true
    # 设为 true，公共聊天中出现玩家名称时都会着色并提醒对方
    # 比普通 @ 提及更消耗性能，请按需开启
    HardCoreMode: false
    # @ 名称或昵称的颜色，发送者需要 cmi.tag.color 权限
    Color: '&c'
    # 玩家被提及时执行的命令
    # [playerName] 等变量会替换为被提及的玩家名称
    # 可使用 [senderName] 插入发起提及的玩家名称
    CommandsOnTag:
    - asConsole! cmi sound BLOCK_NOTE_BLOCK_HARP:3:1 [playerName] -s
    # 只在被提及玩家处于 AFK 状态时执行命令
    OnlyWhenAfk: false
    # 设为 true，移除 @ 符号
    RemoveEta: false
```

## `ChatBubble` { #chatbubble }

```yaml title="Chat.yml · ChatBubble"
ChatBubble:
  # 是否为公共聊天启用聊天气泡
  # 每名玩家可通过 /options 单独关闭
  PublicMessages: true
  # 聊天气泡的显示高度
  Offset: 2.5
  # 聊天气泡的基础显示时间，单位为秒
  ShowFor: 5
  # 气泡最长显示时间
  MaxShowFor: 10
  # 消息中每个字符额外增加的显示秒数
  # 让短消息较快消失，长消息显示更久
  ExtraTime: 0.02
  # 聊天气泡缩放比例，默认为 1
  PlateScale: 1.0
  # 超过此宽度后自动换行
  LineWidth: 255
  Background:
    # 默认颜色代码；文字本身有颜色时可覆盖此值
    # 留空使用默认透明颜色
    # 颜色代码示例：{#black}
    Color: '{#black}'
    # 取值为 0 到 1，0 为无背景色，1 为完全不透明
    Opacity: 0.5
  # 是否添加文字阴影
  Shadow: true
  # 玩家有多个匹配权限时，优先使用数值较高的组
  # 颜色使用十六进制格式，可选带透明通道的 RGBA 格式
  Groups:
    '0':
      BackgroundColor: '#000000DC'
      Shadow: true
      LineWidth: 255
      Scale: 0.5
    '1':
      BackgroundColor: '#AEC6FFDC'
      Shadow: true
      LineWidth: 255
      Scale: 0.5
    '2':
      BackgroundColor: '#BAFFC9DC'
      Shadow: true
      LineWidth: 255
      Scale: 0.5
    '3':
      BackgroundColor: '#FFFFBADC'
      Shadow: true
      LineWidth: 255
      Scale: 0.5
```
