---
title: worlds/world_nether/blacklist.txt
source_kind: imported-configuration
translation_review: reviewed
source_file: worlds/world_nether/blacklist.txt
source_version: 7.0.17+2370-e42d8bc
---

# worlds/world_nether/blacklist.txt

文件：`worlds/world_nether/blacklist.txt`。版本：`7.0.17+2370-e42d8bc`。

方块与物品黑名单。

```text title="worlds/world_nether/blacklist.txt"
#
# WorldGuard 黑名单
#
# 黑名单可用于禁止特定操作，以及禁止使用特定方块和物品。
# 选择一组“要影响的物品”和一组“要执行的动作”。
#
###############################################################################
#
# 禁止挖掘和放置某些矿石的示例：
# [coal_ore,gold_ore,iron_ore]
# on-break=deny,log,kick
# on-place=deny,tell
#
# 可检测的事件：
# - on-break（此类型的方块即将被破坏时）
# - on-destroy-with（破坏方块时玩家手持的物品或方块）
# - on-place（放置方块时）
# - on-use（使用打火石、水桶等物品时）
# - on-interact（使用门、箱子等方块时）
# - on-drop（物品从玩家背包中被丢出时）
# - on-acquire（物品通过某种方式进入玩家背包时）
# - on-equip（物品被装备到玩家的盔甲栏时）
#      注意：由于 Bukkit API 的不足，on-equip 的保护范围会超出实际需要。
# - on-dispense（发射器即将发射物品时）
#
# 动作（供事件使用）：
# - deny（完全阻止，用于黑名单模式）
# - allow（用于白名单模式）
# - notify（通知拥有 'worldguard.notify' 权限的管理员）
# - log（记录到控制台、文件或数据库）
# - tell（告知玩家此操作不被允许）
# - kick（踢出玩家）
# - ban（封禁玩家）
#
# 选项：
# - ignore-groups（不受影响的组，以逗号分隔）
# - ignore-perms（拥有这些权限的玩家不受影响，以逗号分隔；可以
#   自行定义权限！）
# - comment（写给自己的备注，执行 'log' 和 'notify' 时会显示）
# - message（可选，用于替代默认提示显示给玩家的消息；%s 为物品名称）
#
###############################################################################
#
# 更多信息参见：
# https://worldguard.enginehub.org/en/latest/blacklist/
#
###############################################################################
#
# 下面是一些示例。
# 请记住：行首带有 # 的行会被忽略。
#

# 禁用岩浆桶
#[lava_bucket]
#ignore-perms=my.own.madeup.permission
#ignore-groups=admins,mods
#on-use=deny,tell

# 禁用某些矿石
#[coal_ore,gold_ore,iron_ore]
#ignore-groups=admins,mods
#on-break=notify,deny,log
```
