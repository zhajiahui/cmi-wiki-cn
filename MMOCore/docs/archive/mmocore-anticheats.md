---
title: 反作弊兼容
source: https://docs.phoenixdevt.fr/archive/mmocore-anticheats
source_snapshot: '2026-10-19'
---

# 反作弊兼容 {#😈-anticheat-support}

MMOCore将自动挂钩到anti-cheat插件，并可以配置为在投射技能时禁用某些检查。

> **信息**
>
> 仅支持使用MythicMobs制作的技能

它的工作方式是指定不同的Anti-Cheat类型并在一定数量的刻内禁用它们。

## 将Anti-Cheat添加到 MythicMob技能 {#adding-anti-cheat-to-mythicmob-skills}

（为了设置 MythicMob技能，[转到此处](../../phoenix/archive/dead-link.md)）要将Anti-Cheat支持添加到你的 MythicMob技能，只需将`disabled-anti-cheats:`添加到你的技能YML 文件中。 （MMOCore中的那个）然后，你可以添加带有刻值的“标志”，具体取决于你需要禁用的Anti-Cheat系统。

禁用20刻的飞行和剪切的示例：

```yml
disabled-anti-cheats:
  flying: 20
  clipping: 20
```

对5刻和暴击对30刻禁用快速修复的示例。

```yml
disabled-anti-cheats:
  fast_heal: 5
  critical_hits: 30
```

## 可用的Anti-Cheat系统 {#available-anti-cheat-systems}

标志是需要首先放置的东西，功能是作弊应该做的事情。有关每个 hack 的作用的更多信息，请参阅Anti-Cheat插件文档。

|旗帜|功能|
| --- | --- |
| `general_exploits` | 未分类的一般黑客 |
| `no_swing` | 不挥手就击中玩家/方块 |
| `movement` | 极限跳跃、速度黑客等 |
| `clipping` | 经历碰撞 |
| `impossible_action` | Self-explanatory |
| `inventory_clear` | 立即丢弃所有物品 |
| `inventory_clicks` | 非法点击物品栏 |
| `auto_sprint` | 永远冲刺 |
| `jesus` | 水上行走 |
| `no_slowdown` | 防止“缓慢”药水效果 |
| `critical_hits` | 总是落地暴击 |
| `nuker` | 一次打破数千个区块 |
| `ghost_hand` | 通过碰撞与事物互动 |
| `liquids` | 疯狂放置/排出液体 |
| `block_reach` | Self-explanatory |
| `elytra` | 鞘翅非法运动 |
| `boat` | 非法船只活动 |
| `fast_bow` | 无需充电即可射出最大箭数 |
| `fast_click` | 减少攻击之间的冷却时间 |
| `fast_heal` | 愈合速度比允许的要快 |
| `flying` | WEEEEEEEEEEEEEEEEEEEE |
| `hit_reach` | Self-explanatory |
| `fast_break` | 瞬间打破方块 |
| `fast_place` | 立即放置许多块 |
| `speed` | 动物园！ |
| `no_fall` | 忽略跌落伤害 |
| `illegal_pos` | 非法职位 |
| `fast_eat` | 立即食用食物 |
| `velocity` | 对玩家应用无效速度 |
| `killaura` | 锁定目标 |

## 兼容的Anti-Cheat插件 {#compatible-anti-cheat-plugins}

- [斯巴达](https://www.spigotmc.org/resources/spartan-advanced-anti-cheat-hack-blocker.25638/)

---

原文：[😈 Anticheat Support](https://docs.phoenixdevt.fr/archive/mmocore-anticheats) · 原文归档：2026-10-19
