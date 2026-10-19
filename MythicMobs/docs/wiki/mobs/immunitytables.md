---
title: 免疫表
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/ImmunityTables
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 免疫表 {#immunity-tables}

免疫表让生物分别记录各玩家的伤害，并为每个玩家单独计算 NoDamageTicks。这样，半秒内只能受伤一次的限制针对的是**每个玩家**，而非**所有玩家合计**。多个玩家同时攻击同一生物时，各自造成的伤害都能正常计入。

**启用免疫表**

为生物打开免疫表很容易。只需将 Modules.ImmunityTable:  true  添加到你的生物中，如下所示：

```yaml
BigHealthBoss:
  Type: pig_zombie
  Display: '&6Hungry Hungry Piggy Zombie'
  Health: 20000
  Modules:
    ImmunityTable: true
  Options:
    NoDamageTicks: 10
```

就是这样！

免疫表会考虑 NoDamageTicks 选项；你可以修改它，但这不是必需的。未指定时使用 Minecraft 的默认值 10。
