---
title: 玩家数据
source: https://docs.phoenixdevt.fr/bounty-hunters/api/players
source_snapshot: '2026-10-19'
---

# 玩家数据 {#👨‍🚀-player-data}

## 获取玩家数据 {#obtaining-player-data}

自2.3以来，玩家数据现在映射到`PlayerDataManager`实例内，你可以使用`BountyHunters.getInstance().getPlayerDataManager()`访问该实例。使用正确的方法，你可以检索相应的`PlayerData`实例。

## 方法 {#methods}

|吸气剂|二传手|描述 |
| --- | --- | --- |
| `getLevel()` | `setLevel(int)` | 猎人的[[等级 |
| `getClaimedBounties()` | `setClaimed..(int)` | 玩家声称了多少悬赏。 |
| `getSuccessfulBounties()` | `setSuccessful(int)` | 玩家创造了多少成功的悬赏。 |
| `getTitle()` | `setTitle(Title)` | 玩家的 [[当前标题 |
| `getAnimation()` | `setAnimation(Quote)` | 玩家的当前 [[悬赏动画 |
| `getIllegalKills()` | `setIllegalKills(int)` | 他非法杀人的数量。 |
| `getIllegalKillStreak()` | `setIllegalKillStreak(int)` | 自上次重生以来非法击杀的数量。 |
| `getRedeemableHeads()` | `add/remove...(UUID)` | 玩家的UUID，玩家可以兑换其头。 |

还可以用 `data.getProfileItem()` 获取玩家档案物品（注意，这个头颅物品**没有**头颅贴图），用 `data.getProgressBar()` 获取等级进度条，用 `data.getBountiesNeededToLevelUp()` 获取升级所需的悬赏数量。

### 额外的 {#extra}

|方法|用途 |
| --- | --- |
| `addLevels(int)` | 为玩家提供额外等级，但没有升级消息 |
| `addClaimedBounties(int)` | 给予额外索赔悬赏 |
| `addSuccessfulBounties(int)` | 增加由玩家创建并由其他人声明的悬赏的计数。 |
| `addIllegalKills(int)` | 将击杀数添加到非法击杀数和总计数中 |
| `hasUnlocked(LevelUpItem)` | 检查玩家是否已解锁物品 |

## 追踪玩家 {#player-hunting}

在此 [wiki 页面](../features/player-hunting.md)上了解玩家狩猎。

| Method | 用途 |
| --- | --- |
| `setHunting(Bounty)` | 强制玩家搜寻玩家 |
| `isHunting()` | 如果玩家正在狩猎，则为 True |
| `stopHunting()` | 退出玩家狩猎 |

## 操纵玩家电平 {#manipulating-the-player-level}

请记住，`PlayerData`实例**不**存储玩家解锁的物品（引用/标题）。每次在物品列表中提示玩家时，都会重新计算这些值。你可以使用`hasUnlocked(LevelUpItem)`检查玩家是否解锁了物品，其中`LevelUpItem`是`Quote`和`Title`都扩展的抽象类。

## 插件物品栏 {#plugin-inventories}

以下代码可用于打开悬赏列表到玩家。

```java
PlayerData playerData = BountyHunters.getInstance().getPlayerDataManager().getPlayerData(/* player UUID */);
PlayerGUI.BOUNTY_LIST.build(playerData).open();
```

可用的 GUI 包括`BOUNTY_LIST`、`HUNTER_LEADERBOARD`和`REDEEMABLE_HEADS`。

---

原文：[👨‍🚀 Player Data](https://docs.phoenixdevt.fr/bounty-hunters/api/players) · 原文归档：2026-10-19
