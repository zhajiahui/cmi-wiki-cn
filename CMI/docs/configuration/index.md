---
title: 配置文件
source_kind: configuration-comments
translation_review: reviewed
---

# 配置文件

本节翻译 2026-10-19 提供的 CMI 配置注释，保留配置项名称和注释中的示例。原包未标明 CMI 版本。

页面按文件和配置项排列，不展示服务器的实际设置值。

| 文件 | 注释说明 |
| --- | --- |
| `config.yml` | [主配置](main.md) |
| `CustomAlias/CustomAlias.yml` | [自定义别名](customalias.md) |
| `Dialogs/ExampleFirst.yml` | 原文件没有注释，示例中的显示文字已在本地覆盖包中汉化 |
| `Dialogs/ExampleSecond.yml` | 原文件没有注释，示例中的显示文字已在本地覆盖包中汉化 |
| `Kits/Kits.yml` | [礼包](kits.md) |
| `Settings/Afk.yml` | [暂离与闲置](afk.md) |
| `Settings/Alias.yml` | [命令别名](alias.md) |
| `Settings/BackUps.yml` | [数据备份](backups.md) |
| `Settings/Chat.yml` | [聊天](chat.md) |
| `Settings/ChatFilter.yml` | [聊天过滤](chatfilter.md) |
| `Settings/Combat.yml` | [战斗状态](combat.md) |
| `Settings/CommandCost.yml` | [命令费用](commandcost.md) |
| `Settings/CustomHeads.yml` | [自定义头颅](customheads.md) |
| `Settings/DataBaseInfo.yml` | [数据库连接](databaseinfo.md) |
| `Settings/DeathMessages.yml` | [死亡消息](deathmessages.md) |
| `Settings/EventCommands.yml` | [事件命令](eventcommands.md) |
| `Settings/EventPriorities.yml` | [事件优先级](eventpriorities.md) |
| `Settings/Homes.yml` | [家](homes.md) |
| `Settings/Modules.yml` | [功能模块](modules.md) |
| `Settings/ParticleEffects.yml` | [粒子效果](particleeffects.md) |
| `Settings/PlayTimeRewards.yml` | 原文件为空 |
| `Settings/RandomTeleportations.yml` | [随机传送](randomteleportations.md) |
| `Settings/Ranks.yml` | [自动晋级](ranks.md) |
| `Settings/Scavenge.yml` | [物品分解](scavenge.md) |
| `Settings/Schedules.yml` | [定时任务](schedules.md) |
| `Settings/TabList.yml` | [TAB 列表](tablist.md) |

## 翻译备注

- `ChatFilter.yml` 的 `:DDD` 示例同时写了“2 个字母”和“3 个大写字母”，数量存在矛盾；译文保留原说明。
- `Scavenge.yml` 对提取失败后附魔降级的两条说明都提到 `100`，却分别表示避免降级和总是降级；译文保留原说明。
- `Ranks.yml` 中 `Branch2Rank1` 的原广播指向 `Branch1Rank1`，汉化保留这个指向。
- `config.yml` 的重生优先级注释提到“随机重生条件”，原文没有进一步解释；译文按原文保留。
