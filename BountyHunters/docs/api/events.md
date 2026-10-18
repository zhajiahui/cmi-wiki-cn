---
title: 事件
source: https://docs.phoenixdevt.fr/bounty-hunters/api/events
source_snapshot: '2026-10-19'
---

# 事件 {#📮-events}

## 赏金创建事件可取消 {#bountycreateevent}

当悬赏即将注册时调用此事件。悬赏可以由玩家使用`/bounty`命令创建，也可以通过命令块或控制台使用相同的命令创建，或者通过 [auto悬赏功能](../features/auto-bounties.md)来创建，该功能将悬赏设置为非法杀死玩家的人。`event#getCause()`返回创建原因。其他插件可以使用`PLUGIN`事件原因。

## 赏金增加活动可取消 {#bountyincreaseevent}

当悬赏的奖励增加时，会调用此事件，因为玩家使用`/bounty`手动增加奖励，或者因为auto-bounty增加了玩家的悬赏。`event#getCause()`返回增加的原因。添加到悬赏的金额可以使用`event#setAdded(double)`进行编辑。

## 赏金到期事件可取消 {#bountyexpireevent}

当悬赏完全到期或悬赏总量下降时，会调用此事件。悬赏可能会因多种原因而减少：管理员运行`/bounty remove`、玩家删除了他们通过右键单击悬赏列表中的悬赏物品创建的悬赏，或者由于悬赏过期系统（如果启用）。

当悬赏过期时，会调用此事件，原因可能是管理员运行`/bounty remove`，也可能是由于玩家删除了他通过右键单击悬赏列表中的悬赏物品创建的悬赏。`event#getCause()`返回过期原因。

## 赏金领取活动可取消 {#bountyclaimevent}

当玩家在杀死悬赏目标后声明悬赏时，将调用此事件。

## 猎人升级活动 {#hunterlevelupevent}

当玩家通过声明悬赏升级时调用（此事件始终在声明事件之后调用）。

## HunterTarget活动可取消 {#huntertargetevent}

当玩家使用悬赏列表瞄准另一个玩家时调用。

---

原文：[📮 Events](https://docs.phoenixdevt.fr/bounty-hunters/api/events) · 原文归档：2026-10-19
