---
title: 聊天过滤（ChatFilter.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/ChatFilter.yml
---

# 聊天过滤（ChatFilter.yml）

文件：`plugins/CMI/Settings/ChatFilter.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `ChatFilter`

### `ChatFilter.Deny.ipBlock.Enabled`

未设为 true 时，不使用此过滤规则

### `ChatFilter.Deny.ipBlock.Group`

过滤组名称，同时决定绕过此规则的权限：cmi.chatfilter.bypass.\[groupName\]

### `ChatFilter.Deny.ipBlock.InformConsole`

设为 true，每次触发时，在控制台记录玩家、规则及原消息

### `ChatFilter.Deny.ipBlock.Regex`

用于过滤的正则表达式。正则用法见 https://regexone.com/

### `ChatFilter.Deny.ipBlock.ReplaceWith`

替换成的文字；未设置时，不修改匹配内容

### `ChatFilter.Deny.ipBlock.BlockType`

可用值：none、others、all<br>
'none'：所有人都能收到消息<br>
'others'：只有发送者能看到消息，其他人看不到，适合静默拦截广告<br>
'all'：所有人都收不到消息

### `ChatFilter.Deny.ipBlock.includePrivateMessages`

启用后，此规则也应用于私聊

### `ChatFilter.Deny.ipBlock.msgToStaff`

触发规则时，拥有 cmi.chatfilter.inform 权限的玩家会收到指定提示

### `ChatFilter.Deny.ipBlock.Commands`

触发规则时执行的命令。可用 \[senderName\] 插入发送者名称，也支持与语言文件相同的全局变量<br>
使用 \[message\] 插入玩家原始消息<br>
使用 \[updatedmessage\] 插入修改后的消息

### `ChatFilter.WhiteList`

从拦截规则中排除的正则列表，例如拦截全部 IP 或域名，但允许自己的服务器地址

### `ChatFilter.DuplicatedMessagePrevention.Use`

设为 true，阻止短时间内重复发送相同或相似消息。可通过 cmi.chatfilter.spambypass 绕过

### `ChatFilter.DuplicatedMessagePrevention.Percentage`

判定为相同消息的相似度百分比

### `ChatFilter.DuplicatedMessagePrevention.Interval`

重复发送相同或相似消息的最小间隔，单位为秒

### `ChatFilter.DuplicatedMessagePrevention.MinAmount`

触发冷却前允许连续重复的命令次数

### `ChatFilter.Caps.Filter`

启用后，按以下规则限制大量使用大写字母的消息<br>
可通过 cmi.chatfilter.capbypass 绕过

### `ChatFilter.Caps.IgnoreUnder`

可忽略的字符数量<br>
例如 ':DDD' 由 2 个字母组成，其中有 3 个大写字母，因此大写占比为 75%

### `ChatFilter.Caps.Percentage`

允许的大写字母百分比上限<br>
例如 'GOOD thing' 有 4 个大写和 5 个非大写字母，忽略空格后，大写比例为 44%，可通过检查

### `ChatFilter.Caps.LowerCase`

检测到过多大写字母时，是否转为小写

### `ChatFilter.Caps.CancelEvent`

检测到过多大写字母时，是否取消聊天事件

### `ChatFilter.Caps.Commands`

玩家使用过多大写字母时执行的命令

### `ChatFilter.Caps.WhiteList`

即使全部大写也允许的消息列表，不含颜色代码

### `ChatFilter.SimpleReplacer.Enabled`

为公共聊天和私聊启用简易替换

### `ChatFilter.SimpleReplacer.Replacements`

快速将 :heart: 等输入替换为 ❤

### `ChatFilter.Emojies`

emojipicker 命令可使用的表情
