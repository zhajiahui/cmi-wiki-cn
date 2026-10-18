---
title: 经济与税费
source: https://docs.phoenixdevt.fr/bounty-hunters/features/economy
source_snapshot: '2026-10-19'
---

# 经济与税费 {#💸-economy-taxes}

如果没有适当的经济和税收系统，悬赏插件会是什么样子？ 🤑

## 税收 {#taxes}

为了防止你的玩家滥用悬赏，你可以使用税收让他们在创建/删除悬赏之前三思而后行。使用该配置，你可以配置每当玩家创建悬赏、向某人的悬赏添加资金或拿走他放在某人头上的钱时将获得的奖励百分比。

> **提示**
>
> 我们建议对悬赏索赔征收高额税，例如10%，以稳定你的经济，因为这相当于增值税。
>
> 然后，你还可以在悬赏移除时使用较小的税，例如1-3%，以阻止玩家创建虚假或无用的悬赏。如果你对悬赏删除而不是创建征税，则将鼓励玩家创建悬赏，这对你的服务器活动有好处！

```yml
bounty-tax:

  # Tax taken when claiming a bounty.
  # Most important tax, basically VAT
  bounty-claim:
    flat: 0
    scale: 5
    #min: 10       # Absolute minimum of tax taken
    #max: 1000     # Absolute maximum of tax taken
    #min-scale: 3  # Minimum % of the bounty amount taken as tax
    #max-scale: 50 # maximum % of the bounty amount taken as tax. Can't be more than half

  # Tax taken when creating a bounty (to fight abuse).
  # By default, no discouragement from creating bounties.
  bounty-creation:
    flat: 0
    scale: 0
    #...

  # Tax taken when a player removes the bounty he set.
  # Discourages players from creating fake or useless bounties.
  bounty-removal:
    flat: 0
    scale: 3
    #...

  # Tax when targeting a player
  # Avoids players spamming the chat with target messages
  # (You can also remove those messages instead of using a tax)
  target-set:
    flat: 100
    scale: 1
    #...
```

## 最低/最高奖励 {#minimum-maximum-reward}

使用此配置选项，你可以决定玩家可以添加到悬赏的最小和最大金额。

```yml
# Min and max bounty rewards.
# Set max to 0 to remove the max restriction.
min-reward: 0
max-reward: 0
```

---

原文：[💸 Economy & Taxes](https://docs.phoenixdevt.fr/bounty-hunters/features/economy) · 原文归档：2026-10-19
