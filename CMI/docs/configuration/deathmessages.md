---
title: 死亡消息（DeathMessages.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/DeathMessages.yml
---

# 死亡消息（DeathMessages.yml）

文件：`plugins/CMI/Settings/DeathMessages.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `EnableCustom`

开启或关闭自定义死亡消息<br>
消息设置见 DeathMessages 目录

可能尚未覆盖所有死亡情况，后续仍需更新<br>
遇到缺失的死亡情况时，请在 GitHub Issues 提交，并提供准确复现方式

## `AutoHideFrom`

在线人数达到多少时，自动隐藏死亡消息<br>
设为 -1 关闭

## `Range`

死亡消息的广播范围，单位为方块<br>
设置范围后，自动排除其他世界的玩家

## `Destination`

死亡消息的显示位置<br>
可用值：plain、actionBar

## `DisabledWorlds`

不广播其中死亡事件的世界

## `MutedWorlds`

不会向其中玩家发送死亡消息的世界

## `IgnoredPlayers`

不显示死亡消息的玩家名称

## `AntiSpam`

### `AntiSpam.TimeRange`

检查死亡消息刷屏的时间范围，单位为秒<br>
设为 -1 关闭<br>
超过限制后，死者仍会看到自己的死亡消息

### `AntiSpam.Count`

在上述时间范围内，最多广播同一玩家多少条死亡消息
