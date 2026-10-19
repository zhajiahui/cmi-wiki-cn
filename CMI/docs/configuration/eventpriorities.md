---
title: 事件优先级（EventPriorities.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/EventPriorities.yml
---

# 事件优先级（EventPriorities.yml）

文件：`plugins/CMI/Settings/EventPriorities.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `ChatPriorities`

修改后需要重启服务器才生效<br>
可用优先级：LOWEST、LOW、NORMAL、HIGH、HIGHEST、MONITOR<br>
会修改事件的监听器不应使用 MONITOR 优先级<br>
设为 NONE 可能完全关闭该监听器

### `ChatPriorities.Format`

公共聊天格式处理<br>
默认优先级：HIGHEST

### `ChatPriorities.Color`

公共聊天颜色处理<br>
默认优先级：NORMAL

### `ChatPriorities.Item`

公共聊天物品展示处理<br>
默认优先级：NORMAL

### `ChatPriorities.Url`

公共聊天网址处理<br>
默认优先级：NORMAL

### `ChatPriorities.Tag`

公共聊天玩家提及处理<br>
默认优先级：NORMAL

### `ChatPriorities.ChatHead`

公共聊天玩家头像处理<br>
默认优先级：NORMAL<br>
从版本 1.21.9 起适用

### `ChatPriorities.ChatSprite`

公共聊天精灵图处理<br>
默认优先级：NORMAL<br>
从版本 1.21.9 起适用

### `ChatPriorities.Mute`

公共聊天禁言处理<br>
默认优先级：LOWEST

### `ChatPriorities.PlayerMute`

玩家禁言处理<br>
默认优先级：LOW

### `ChatPriorities.PlayerShadowMute`

玩家影子禁言处理<br>
默认优先级：LOW

### `ChatPriorities.ChatRoom`

聊天室使用 ! 将消息发到公共聊天的处理<br>
默认优先级：LOWEST

### `ChatPriorities.Staff`

管理聊天室使用 ! 将消息发到公共聊天的处理<br>
默认优先级：LOWEST

### `ChatPriorities.Shout`

喊话消息处理<br>
默认优先级：LOWEST

### `ChatPriorities.Bungee`

BungeeCord 消息处理<br>
默认优先级：MONITOR

### `ChatPriorities.Dynmap`

DynMap 消息处理<br>
默认优先级：MONITOR

### `ChatPriorities.Bubble`

聊天气泡处理<br>
默认优先级：MONITOR<br>
从版本 1.20.0 起适用

### `ChatPriorities.Caps`

公共聊天大写字母过滤<br>
默认优先级：LOW

### `ChatPriorities.Filter`

公共聊天违禁词过滤<br>
默认优先级：LOW

### `ChatPriorities.SimpleReplacer`

公共聊天表情简易替换<br>
默认优先级：LOWEST

### `ChatPriorities.CommandSpam`

命令防刷屏处理<br>
默认优先级：LOW

### `ChatPriorities.ChatSpam`

聊天防刷屏处理<br>
默认优先级：LOW

### `ChatPriorities.SignAd`

告示牌广告处理<br>
默认优先级：MONITOR
