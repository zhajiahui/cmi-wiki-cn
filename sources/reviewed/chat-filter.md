## 简介

CMI 的聊天过滤功能可以帮助服主管理和审核服务器中的内容。它独立于命令的执行前等待和冷却机制，可用于检测命令刷屏、大写字母刷屏、聊天脏话等行为。

通过正则表达式和自定义设置，服主可以配置出适合自己社区和服务器的聊天过滤规则。

在 `~/plugins/CMI/Settings/ChatFilter.yml` 文件中进行设置，文件包含以下几个部分：

- 启用或禁用聊天过滤功能。
- 通过 `ipBlock` 屏蔽广告。
- 屏蔽脏话，可添加多条规则。除了脏话，也可以屏蔽特定短语、政治话题或某些词语。
- 通过白名单放行指定域名。
- 屏蔽重复消息。
- 防止滥用大写字母，支持白名单，并且会忽略玩家名称。
- 与 CMI 聊天管理功能集成。

## 使用要求

要让聊天过滤生效，需要编辑 `~/plugins/CMI/Settings/ChatFilter.yml`，将文件顶部的 `Enabled:` 设为 `true`。

推荐使用 CMI 管理聊天，但并非必须。

## 命令

此功能没有直接使用的命令。不过，可以对触发聊天过滤的玩家执行自定义命令。这些命令在 `~/plugins/CMI/Settings/ChatFilter.yml` 中设置。除了自动封禁玩家，也可以考虑使用 CMI 的这些功能：`jail`、`cuff`、`mute`、`ban`、临时封禁（temp ban）、`kick`、`mail`、`clearchat`，或其他插件的任何有效命令。

可以使用特殊命令。

## 权限

可以向团队成员授予通知权限，并根据需要，向高级或特殊的组、等级授予部分绕过过滤的权限。

```text
cmi.chatfilter.bypass.[groupname] - Allows to bypass particular chat filter group
cmi.commandfilter.bypass - Allows to bypass command spam filter
cmi.chatfilter.capbypass - Allows to bypass chat caps filter
cmi.chatfilter.inform - Informs player when someone breaks chat filter rules
cmi.chatfilter.spambypass - Allows to bypass chat spam filter
```

## 占位符

此功能没有专用占位符。不过，如果使用 CMI 的警告功能，可以使用 `%cmi_user_warning_count%` 和 `%cmi_user_warning_points%`。此外还有几个用于监听的占位符，方便工作人员查看玩家正在刷屏的内容。

## 提示：正则表达式与测试

正则表达式可能较难掌握。强烈建议先在开发环境中充分测试。

可以使用这些网站编写正则表达式：<https://regexone.com/> 和 <https://regex101.com/>。

也可以尝试 Alax 制作的非官方工具，但该工具不受支持：<https://dkalaxdk.github.io/CMIRegexFilter/>。

## 启用或禁用聊天过滤

要开始过滤广告、不当词语、重复消息、命令或大写字母刷屏，将下面的 `Enabled` 从 `false` 改为 `true`，完成各项配置后执行 `/cmi reload`。

```text
Enabled: true
```

## 使用 ipBlock 屏蔽广告

CMI 可以阻止玩家发送域名和 IP 地址。`ipBlock` 可以启用或禁用。

可以定义一个组，让团队成员或某个特殊组不受此规则屏蔽。也可以将触发情况记录到控制台，便于追踪是谁触发了 `ipBlock`。

```text
# Defines filter group and defines required permission node to bypass this filter: cmi.chatfilter.bypass.[groupName]
Group: Advertising
# When set to true, each time player triggers filter, console will receive information about who triggered it, which filter and with what message
InformConsole: true
```

通过正则表达式，可以精细匹配并屏蔽玩家发送的域名和 IP 地址，也可以指定用什么内容替换匹配到的词语。

```text
# Regex expression to filter by. How to use regex https://regexone.com/
Regex:
- '[a-zA-Z0-9\-\.]+\s?(\.|dot|\(dot\)|-|;|:|,|_|\/)\s?([a-zA-Z]{2}|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel)\b'
- \b[0-9]{1,3}(\.|dot|\(dot\)|-|;|:|,|(\W|\d|_)*\s)+[0-9]{1,3}(\.|dot|\(dot\)|-|;|:|,|(\W|\d|_)*\s)+[0-9]{1,3}(\.|dot|\(dot\)|-|;|:|,|(\W|\d|_)*\s)+[0-9]{1,3}\b
# With what we need to replace word, if not defined found expression will not be changed
ReplaceWith: ''
```

`ipBlock` 的下一部分用于设置如何处理被屏蔽的消息：是否同时检查私聊，是否将消息从聊天中完全移除，或者仍让所有人看到消息。也可以设置如何通知工作人员。

```text
# With what we need to replace word, if not defined found expression will not be changed
ReplaceWith: ''
# possible: none, others, all
# Where 'none' means everyone will receive this message
# 'others' means that sender will get message but not other players, this is usefull to prevent advertising and silently block it
# 'all' means that no one will receive sent message
BlockType: others
# When enabled rule will be applied to private messages
includePrivateMessages: true
# Players with cmi.chatfilter.inform permission will receive defined message when rule is broken
msgToStaff: '&4!&6[playerName] &4advertising with: &r[message]'
```

如果需要，可以为 `ipBlock` 设置一条或多条命令，在某人的消息被屏蔽时执行。例如，自动禁言或踢出玩家、向其发送 Boss 血条消息或操作栏消息、通过 `/cmi mail` 同时通知版主和玩家，或者将玩家关入监狱。这里可以使用特殊命令、`[senderName]` 变量及其他全局变量。下面是几个示例。

不执行任何命令：

```text
# List of commands to perform when rule is broken. Use [senderName] to include message sender name. Supports global variables same as locale file
Commands: []
```

执行一条命令：

```text
 # List of commands to perform when rule is broken. Use [senderName] to include message sender name. Supports global variables same as locale file
Commands:
- cmi mail [senderName] Please refrain from Advertising, see /rules
```

执行多条命令：

```text
# List of commands to perform when rule is broken. Use [senderName] to include message sender name. Supports global variables same as locale file
Commands:
- cmi mail [senderName] Please refrain from Advertising, see /rules
- cmi kick [senderName] Please refrain from Advertising, see /rules
- cmi note [senderName] add Broke rule Advertising
```

`ipBlock` 的最后一部分可以灵活设置。除了 `ipBlock`，配置中还列出了 `swearing1`、`swearing2` 两个示例，可以按需添加更多规则。例如，不想让玩家提到 `bedwars`、`hypixel` 或某个政治用语，就可以在这里为它们添加屏蔽部分。复制其中一段，再按需配置即可。每一部分可以添加多个正则表达式，也可以为每个词单独建立一段规则。这样就能针对不同词语采取不同处理，例如某些词只发出警告，而仇恨言论则自动封禁。

## 为屏蔽列表设置白名单

如果仍希望成员能向别人发送你的 Discord、论坛、YouTube 频道等链接，或者允许 Twitter、Twitch 等指定域名，但屏蔽其他所有域名，可以通过正则表达式将例外加入白名单。也可以为特定组授予聊天过滤绕过权限，让其绕过所有规则，或只绕过某个指定的规则组。

```text
# List of regex filter to exlude from block list. Usefull if you want to block all ip/host address but want to allow usage of your own server.
WhiteList:
- \bgoogle.\s?([a-zA-Z]{2,4})\b
- \bspigotmc.\s?([a-zA-Z]{2,4})\b
```

## 防止玩家发送重复消息

`~/plugins/CMI/Settings/ChatFilter.yml` 的第二部分是 `DuplicatedMessagePrevention:`，用于防止玩家在短时间内发送相似消息。可以启用此功能，也可以为组授予绕过权限。

```text
# When set to true, plugin will prevent spamming of same or similar messages in short time range. Can be bypassed with cmi.chatfilter.spambypass permission
Use: true
```

以下选项用于调整消息刷屏的判定频率：

```text
# How much in percentage message is counted as same
Percentage: 80
# Defines how often in seconds you can send same/similar message
Interval: 5
# How many commands you can repeat before stopped for cooldown
MinAmount: 2
```

命令刷屏过滤目前仍位于 `~/plugins/CMI/config.yml` 中，其选项与消息刷屏过滤基本相同。搜索 **`CommandFilter:`** 即可找到。

## 过滤包含大量大写字母的聊天消息（大写刷屏）

`~/plugins/CMI/Settings/ChatFilter.yml` 的最后一部分用于设置如何处理包含多个大写字母的聊天消息。将过滤选项设为 `true` 即可启用。玩家名称不会计入统计。

```text
# When nebaled we will try to prevent chat messages with multiple capitalized letters by defined criteria
# Can be bypassed with cmi.chatfilter.capbypass permission node
Filter: true
```

还可以调整判定大写刷屏的阈值。

```text
# Defines amount of letters we can ignore
# For example ':DDD' would be made of 2 letters with 3 capitalized letters which would make it 75% capitalized
IgnoreUnder: 6
# Amount in percentage of capitalized letters we should not cross over.
# In example 'GOOD thing' would be 4 capitalized and 5 not, spaces gets ignored, whic makes it 44% capitalized and passes check
Percentage: 50
```

同样可以选择不执行命令，或者执行一条、多条命令。上文已给出相应示例，可以应用到下面的选项中：

```text
# Commands:
- asConsole! cmi titlemsg [playerName] &cToo many caps! -keep:20
```

也可以为大写字母设置白名单，避免过滤规则过于敏感，导致简短的问候或常用词语也触发规则。

```text
# List of messages, excluding color codes, player can use even if it 100% capitalized
WhiteList:
- AFAIK
- AFK
- BRB
- IMHO
- OMG
- ROFL
- ROFLMAO
- LQTM
- LSMH
- LMHO
```

配置好 `~/plugins/CMI/Settings/ChatFilter.yml` 后，还需要考虑授予玩家哪些权限。也可以按需配合 `config.yml` 中的命令执行前等待和冷却选项，进一步调整玩家在服务器上的行为。
