---
title: 公会
source: https://docs.phoenixdevt.fr/mmocore/features/guilds
source_snapshot: '2026-10-19'
---

# 公会 {#🛡️-guilds}

公会（也称为派系、王国...）是RPG服务器的常见功能。它们允许玩家团队合作、共享资源并共同努力实现共同目标。

MMOCore不提供公会系统，但兼容以下公会插件：

- [FactionsBridge](https://www.spigotmc.org/resources/factionsbridge.89716/)支持的任何插件（>15插件）
- [终极部落 V6](https://polymart.org/resource/ultimate-clans-v6.1162)
- [公会](https://www.spigotmc.org/resources/guilds-30-sale.66176/)

请注意，当使用 FactionsBridge 支持的任何公会插件运行MMOCore时，你需要安装 FactionsBridge。

## 选择你的公会插件 {#choosing-your-guild-plugin}

转到`MMOCore/config.yml`并将`guild-plugin`设置为你要使用的任何插件。编辑此选项时请确保重新启动服务器。

```yml
# Edit the plugin handling guilds here.
# Supported values (just copy and paste):
# - FACTIONSBRIDGE (and any supported Factions/Guild plugin)
# - MMOCORE (Default built-in guild system)
# - NONE (Used to fully disable guilds)
# - GUILDS (by Glare)
# - ULTIMATE_CLANS
guild-plugin: MMOCORE
```

使用任何不是MMOCore的公会插件都会禁用MMOCore的所有公会功能，包括公会注册表和`/guild`命令。

## MMOCore公会 {#mmocore-guilds}

MMOCore 内部实现了一个占位用的公会系统，但几乎没有实际功能，目前也没有继续开发它的计划。

---

原文：[🛡️ Guilds](https://docs.phoenixdevt.fr/mmocore/features/guilds) · 原文归档：2026-10-19
