---
title: 事件优先级（EventPriorities.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/EventPriorities.yml
---

# 事件优先级（EventPriorities.yml）

文件：`plugins/CMI/Settings/EventPriorities.yml`

## `ChatPriorities` { #chatpriorities }

```yaml title="EventPriorities.yml · ChatPriorities"
# 修改后需要重启服务器才生效
# 可用优先级：LOWEST、LOW、NORMAL、HIGH、HIGHEST、MONITOR
# 会修改事件的监听器不应使用 MONITOR 优先级
# 设为 NONE 可能完全关闭该监听器
ChatPriorities:
  #
  # 公共聊天格式处理
  # 默认优先级：HIGHEST
  Format: HIGHEST
  #
  # 公共聊天颜色处理
  # 默认优先级：NORMAL
  Color: NORMAL
  #
  # 公共聊天物品展示处理
  # 默认优先级：NORMAL
  Item: NORMAL
  #
  # 公共聊天网址处理
  # 默认优先级：NORMAL
  Url: NORMAL
  #
  # 公共聊天玩家提及处理
  # 默认优先级：NORMAL
  Tag: NORMAL
  #
  # 公共聊天玩家头像处理
  # 默认优先级：NORMAL
  # 从版本 1.21.9 起适用
  ChatHead: NORMAL
  #
  # 公共聊天精灵图处理
  # 默认优先级：NORMAL
  # 从版本 1.21.9 起适用
  ChatSprite: NORMAL
  #
  # 公共聊天禁言处理
  # 默认优先级：LOWEST
  Mute: LOWEST
  #
  # 玩家禁言处理
  # 默认优先级：LOW
  PlayerMute: LOW
  #
  # 玩家影子禁言处理
  # 默认优先级：LOW
  PlayerShadowMute: LOW
  #
  # 聊天室使用 ! 将消息发到公共聊天的处理
  # 默认优先级：LOWEST
  ChatRoom: LOWEST
  #
  # 管理聊天室使用 ! 将消息发到公共聊天的处理
  # 默认优先级：LOWEST
  Staff: LOWEST
  #
  # 喊话消息处理
  # 默认优先级：LOWEST
  Shout: LOWEST
  #
  # BungeeCord 消息处理
  # 默认优先级：MONITOR
  Bungee: MONITOR
  #
  # DynMap 消息处理
  # 默认优先级：MONITOR
  Dynmap: MONITOR
  #
  # 聊天气泡处理
  # 默认优先级：MONITOR
  # 从版本 1.20.0 起适用
  Bubble: MONITOR
  #
  # 公共聊天大写字母过滤
  # 默认优先级：LOW
  Caps: LOW
  #
  # 公共聊天违禁词过滤
  # 默认优先级：LOW
  Filter: LOW
  #
  # 公共聊天表情简易替换
  # 默认优先级：LOWEST
  SimpleReplacer: LOWEST
  #
  # 命令防刷屏处理
  # 默认优先级：LOW
  CommandSpam: LOW
  #
  # 聊天防刷屏处理
  # 默认优先级：LOW
  ChatSpam: LOW
  #
  # 告示牌广告处理
  # 默认优先级：MONITOR
  SignAd: MONITOR
```
