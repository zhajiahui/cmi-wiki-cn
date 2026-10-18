---
title: 命令
source: https://docs.phoenixdevt.fr/mmocore/general/commands
source_snapshot: '2026-10-19'
---

# 命令 {#💾-commands}

以下是MMOCore中所有可用命令的列表。你还可以探索这些in-game，因为完全支持tab-completion。

|命令 |用途 |
| --- | --- |
| `/mmocore` | 显示主帮助页面。 |
| `/mmocore reload` | 编辑配置文件后重新加载整个插件。无需重新启动服务器！ |

### 货币 {#currency}

| Command | 用途 |
| --- | --- |
| `/mmocore note` | 给玩家一张价值 X 美元的纸币。可以【](../misc/economy.md)存入银行。 |
| `/mmocore coins` | 根据输入的金额赠送玩家金币。可以存入银行。 |

### 任务 {#quests}

| Command | 用途 |
| --- | --- |
| `/mmocore quest start` | 强制开始寻找玩家。 |
| `/mmocore quest cancel` | 强制取消玩家的当前任务。 |

### 传送点 {#waypoints}

| Command | 用途 |
| --- | --- |
| `/mmocore waypoints unlock` | 手动解锁一组玩家的航路点。 |
| `/mmocore waypoints lock` | 手动锁定一组玩家的航路点。 |
| `/mmocore waypoints teleport` | 手动将玩家传送到设定的路径点。 |
| `/mmocore waypoints open` | 打开航点菜单并检查玩家是否站在航点上 |

### 管理员 {#admin}

| Command | 用途 |
| --- | --- |
| `/mmocore admin exportdata` | 将 yml 文件中的所有现有玩家数据导出到 sql 数据库。因此，你可以将数据存储更改为SQL，同时保留所有玩家数据。 |
| `/mmocore admin attr-realloc-points <give/set>` | 手动将基础属性重新分配点分配给玩家。 |
| `/mmocore admin attribute-points <give/set>` | 手动将基础属性点提供给玩家。 |
| `/mmocore admin attribute <give/take>` | 增加了一个玩家的基础属性 |
| `/mmocore admin force-class` | 强制设置玩家的职业，不会同时更新其等级、技能等数据。使用前请确认相关职业拥有相同的技能和技能树。 |
| `/mmocore admin class-points` | 给予玩家[职业点数](../features/classes.md#class-points)。 |
| `/mmocore admin exp give <player> <profession/main> <value> <split>` | 给予玩家副职业或主职业经验。 |
| `/mmocore admin exp set <player> <profession/main> <value>` | 设置玩家的副职业或主职业经验。 |
| `/mmocore admin exp take <player> <profession/main> <value>` | 从玩家上取下职业/副职业经验。 |
| `/mmocore admin hideab <player> <ticks>` | 将玩家的动作栏隐藏 X 个刻。 |
| `/mmocore admin info` | 请参阅玩家的等级摘要。 |
| `/mmocore admin level <profession/main>` | 与经验命令相同的参数，给出 X等级。 |
| `/mmocore admin nocd` | 由管理员用来测试技能，而不受技能、冷却时间或魔力使用情况的影响。 |
| `/mmocore admin reset <player>` | 硬重置玩家的信息i.e职业、等级、经验... |
| `/mmocore admin resource-health <give/set/take>` | 修改玩家的生命值。 |
| `/mmocore admin resource-mana <give/set/take>` | 修改玩家的魔力。 |
| `/mmocore admin resource-stamina <give/set/take>` | 修改玩家的耐力。 |
| `/mmocore admin resource-stellium <give/set/take>` | 修改玩家的stellium。 |
| `/mmocore admin skill-points <give/set>` | 将 [技能指向](../skills/intro.md#upgrading-a-skill)到玩家，以便他们可以升级其技能。 |
| `/mmocore admin skill-realloc-points <give/set>` | 将技能重新分配点赋予玩家。 |
| `/mmocore admin skill <give/set>` | 直接为玩家的技能提供积分。 |
| `/mmocore admin skill <lock/unlock>` | 锁定/解锁某个玩家的 [技能](https://docs.phoenixdevt.fr/mmocore/skills/intro#unlocking-skills)。 |
| `/mmocore admin slot <lock/unlock>` | 锁定/解锁玩家的插槽](../features/classes.md#skill-slots)。 |
| `/mmocore admin slot bind <slot> <skill>` | 将技能绑定到某个插槽。即使指定的技能没有为玩家解锁，这也会起作用，但不会解锁它。 |
| `/mmocore admin slot unbind <slot>` | 解除技能与某个槽位的绑定。 |

### 职业 {#classes}

|`/mmocore class force <player> <class>`|强制设置玩家的职业而不加载职业数据| |`/mmocore class select <player> <class>`|设置玩家的职业并加载其职业数据 | |`/mmocore class check <player>`|打印玩家的当前职业|

### 经验值提升 {#exp-boosts}

| Command | 用途 |
| --- | --- |
| `/mmocore booster create <profession/main> (player)` | 创建具有指定功率和长度的 [经验助推器](../level/boosters.md)。 |
| `/mmocore booster list` | 显示活跃的 EXP 增强器。 |
| `/mmocore booster remove` | 删除指定ID的助推器。 |

---

原文：[💾 Commands](https://docs.phoenixdevt.fr/mmocore/general/commands) · 原文归档：2026-10-19
