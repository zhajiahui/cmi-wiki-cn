---
title: 悬赏限制
source: https://docs.phoenixdevt.fr/bounty-hunters/features/claim-restrictions
source_snapshot: '2026-10-19'
---

# 悬赏限制 {#🛑-bounty-restrictions}

悬赏系统的一个常见问题是玩家在朋友或 alt 上滥用悬赏，以获取属性或奖励。BountyHunters提供了多种方法来限制玩家创建和声明悬赏的方式，以防止此类滥用。

<details markdown="1">

<summary>配置选项</summary>

```yml
# Setting any parameter to 'true' means a new restriction applies.
# Make sure you restart your server when changing one of these options.
claim-restrictions:

  # Players may not claim their own bounties.
  # Disabled by default due to the bounty claim tax. If players
  # claim their own bounties, they will lose tax money.
  own-bounties: false

  # Players cannot claim bounties on players who
  # have close bed spawn points (most likely friends).
  bed-spawn-point:
    enabled: false

    # Blocks threshold
    radius: 100

  # Players may not claim bounties if they are in the same team.
  scoreboard-teams: false

  # Players may ONLY claim bounties if
  # they are tracking the bounty target.
  targets-only: false

  # Compatibility with PartyAndFriends and BungeeFriends
  # Players may not kill their friends to claim bounties.
  friends: true

  # Compatibility with Towny
  # Players may not kill members of the same town to claim bounties.
  town-members: true

  # Compatibility with Lands
  # A player cannot interact with a target bounty
  # if the player's land trusts the target
  lands: true

  # Compatibility with SimpleClans
  simple-clans: true

  # Compatibility with UltimateClans
  ultimate-clans: true

  # Compatibility with FactionsUUID/SaberFactions etc.
  factions: true

  # Compatibility with Guilds
  guilds: true

  # Compatibility with KingdomsX
  kingdoms: true
```

</details>

例如，你可以阻止玩家向他们的朋友、公会成员、派系成员索取悬赏...所有支持的插件都列在上面的配置文件中。

你还可以阻止玩家声明自己的悬赏，如果你禁用悬赏声明/创建税，这可能会很有用。

BountyHunters还可以检测玩家的床生成点是否接近悬赏目标玩家的床生成点。如果是这样，他们将无法领取悬赏。你可以以块为单位配置检测半径。

---

原文：[🛑 Bounty Restrictions](https://docs.phoenixdevt.fr/bounty-hunters/features/claim-restrictions) · 原文归档：2026-10-19
