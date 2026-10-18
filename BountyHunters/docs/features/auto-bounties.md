---
title: 自动悬赏
source: https://docs.phoenixdevt.fr/bounty-hunters/features/auto-bounties
source_snapshot: '2026-10-19'
---

# 自动悬赏 {#⛓️‍💥-automatic-bounties}

Auto悬赏允许你惩罚玩家*非法*杀人。非法击杀是对没有放置任何悬赏的玩家进行的击杀。此功能对于避免随机杀戮很有用，并鼓励玩家只杀掉身上有悬赏的人。

如果玩家上已经有悬赏，则auto-bounty系统将简单地增加当前的悬赏，而不是创建一个新的。

![](../assets/8e7c10adfa5c-auto_bounty_1.BFpNj-RU.png)

![](../assets/4699ed6091bf-auto_bounty_2.Cah5O6XY.png)

## 配置 {#configuration}

```yml
# When enabled, it will automatically place a bounty onto any
# player who kills a player with no bounty on them (illegal kill).
auto-bounty:
  enabled: false

  # Bounty reward
  reward: 100

  # Chance of applying
  chance: 100

  # If the auto bounty should keep increasing a bounty if it's already set
  increment: true
```

将`enabled`设置为`false`以完全禁用auto-bounty。`reward`定义默认的悬赏奖励。`chance`定义了玩家在非法杀人时触发auto-bounty系统的几率（以%为单位）。

---

原文：[⛓️‍💥 Automatic Bounties](https://docs.phoenixdevt.fr/bounty-hunters/features/auto-bounties) · 原文归档：2026-10-19
