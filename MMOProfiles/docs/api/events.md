---
title: 事件
source: https://docs.phoenixdevt.fr/mmoprofiles/api/events
source_snapshot: '2026-10-19'
---

# 事件 {#📮-events}

## 档案创建和删除 {#profile-creation-and-removal}

创建档案时，将调用`ProfileCreateEvent`。此事件包含玩家UUID和新创建的档案的档案UUID。你可以侦听此事件以在创建新档案时执行操作。该事件存储`CompletableFuture<Void>`，一旦所有数据模块验证该事件，该事件就完成。

当用户永久删除其个人资料之一时，将调用`ProfileRemoveEvent`。你可以使用此事件删除插件数据库中与已删除档案相对应的记录。该事件存储`CompletableFuture<Void>`，一旦所有数据模块验证该事件，该事件就完成。

## 档案选择和取消选择 {#profile-selection-and-unselection}

当玩家选择档案时，会调用`ProfileSelectEvent`。当所有数据模块都验证了此事件后，档案将应用于玩家，即玩家被传送到其先前的位置，其物品栏被恢复，等等...

当玩家通过注销、退出其档案或切换到另一个档案来取消选择档案时，将调用`ProfileUnloadEvent`。

在档案切换的情况下，保证在新档案的`ProfileSelectEvent`之前调用`ProfileUnloadEvent`。如果注销或在没有切换的情况下退出当前档案，则仅调用`ProfileUnloadEvent`。注销时，保证在`PlayerQuitEvent`之后调用`ProfileUnloadEvent`。

## Proxy-Mode活动 {#proxy-mode-events}

当启用proxy-mode档案时，当代理最终向后端服务器提供玩家的真实UUID和档案UUID时，在玩家加入后（在`PlayerJoinEvent`之后）至少调用`PlayerIdDispatchEvent`。

> **信息**
>
> 当玩家加入服务器时，玩家已经有了其欺骗的UUID，因为欺骗发生在proxy-level。因此，玩家的官方UUID（以及其他通用玩家信息）需要通过插件消息从代理转发到后端服务器。  当后端服务器从代理接收到此信息时，将调用`PlayerIdDispatchEvent`。

---

原文：[📮 Events](https://docs.phoenixdevt.fr/mmoprofiles/api/events) · 原文归档：2026-10-19
