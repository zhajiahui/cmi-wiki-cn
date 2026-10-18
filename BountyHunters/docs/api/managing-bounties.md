---
title: 悬赏
source: https://docs.phoenixdevt.fr/bounty-hunters/api/managing-bounties
source_snapshot: '2026-10-19'
---

# 悬赏 {#📜-bounties}

你可以使用`BountyManager`类来注册/取消注册悬赏或简单地检查现有的悬赏。你可以使用以下代码片段访问类实例：

```java
BountyManager manager = BountyHunters.getInstance().getBountyManager();
```

## 创建并注册悬赏 {#creating-registering-a-bounty}

要创建悬赏，你必须使用`Bounty`构造函数。

```java
Bounty bounty = new Bounty(creator, target, reward);
```

- 创建者 - OfflinePlayer
- 目标 - OfflinePlayer
- 奖励 - 双倍

要注册悬赏，请使用`bountyManager.registerBounty(bounty)`，它调用`BountyCreateEvent`事件。要注销悬赏，你需要使用`bountyManager.unregisterBounty(bounty)`。`Bounty`类不再具有任何注册或取消注册方法，以减少混乱和潜在的数据故障。

这些方法都重置了悬赏猎人。这意味着玩家狩猎悬赏目标将停止狩猎。

## 获取活跃的悬赏列表 {#getting-the-list-of-active-bounties}

使用`bountyManager.getBounties()`获取所有活动悬赏的集合，按创建顺序排序。

## 获取悬赏 {#getting-a-bounty}

你可以使用`bountyManager.getBounty(OfflinePlayer)`在玩家上获取悬赏。

先用 `bountyManager.hasBounty(OfflinePlayer)` 检查玩家是否有悬赏。若玩家没有悬赏，直接调用 `getBounty(OfflinePlayer)` 会抛出 NPE 错误。

---

原文：[📜 Bounties](https://docs.phoenixdevt.fr/bounty-hunters/api/managing-bounties) · 原文归档：2026-10-19
