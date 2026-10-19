---
title: WorldGuard 文档
source_url: https://worldguard.enginehub.org/en/latest/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# WorldGuard 文档 { #worldguard-documentation }

WorldGuard 提供适用于服主、地图制作者、普通生存服务器等各类使用者的多种功能。

- [在世界中创建区域](regions/index.md)，仅允许管理人员或指定玩家在其中建造

- 为服务器设置[额外游戏规则](config.md)，例如禁止凋灵破坏方块、禁用摔落伤害等

- 为世界中的[指定区域设置游戏规则](regions/flags.md)，如饱食度恢复、生命值恢复、禁用 PvP 和 TNT、控制生物伤害

- 将[特定物品](blacklist.md)和方块加入黑名单，禁止使用

- 导出服务器统计与信息（/wg report -p）

- 分析服务器 CPU 使用情况（/wg profile -p）

- 加入[实用命令](commands.md)，例如立即“停止所有火焰蔓延”的命令

- 在一定程度上[兼容其他插件和模组](regions/scope.md)，包括其他 Bukkit 插件和 FTB 模组

- 防范[多种破坏手段](regions/scope.md)，如树木生长、TNT 大炮、活塞机器等

- 也可以允许特定交互，例如使用门和拉杆

- [开源](https://www.github.com/EngineHub/WorldGuard)，也是历史最久的 Minecraft 项目之一，比 Bukkit 更早！

- 只启用自己需要的功能！**所有功能默认均关闭。**可以先安装 WorldGuard，稍后再配置。

## 文档 { #documentation }

- [安装](install.md)

- [配置](config.md)

  - [主机密钥](host-keys.md)

- [权限](permissions.md)

  - [建造权限](build-perms.md)

- [命令](commands.md)

- [黑名单](blacklist.md)

- [区域](regions/index.md)

  - [快速入门](regions/quick-start.md)

  - [区域查询工具](regions/wand.md)

  - [区域旗标](regions/flags.md)

  - [优先级与继承](regions/priorities.md)

  - [全局区域](regions/global-region.md)

  - [区域命令](regions/commands.md)

  - [认领区域](regions/claiming.md)

  - [存储驱动](regions/storage.md)

  - [保护范围](regions/scope.md)

  - [常见场景](regions/common-scenarios.md)

- [箱子保护](chest-protection.md)

- [WorldGuard API](https://worldguard.enginehub.org/en/latest/developer/)

  - [作为依赖](https://worldguard.enginehub.org/en/latest/developer/dependency/)

  - [使用区域 API](https://worldguard.enginehub.org/en/latest/developer/regions/)

    - [区域管理器](https://worldguard.enginehub.org/en/latest/developer/regions/managers/)

    - [区域](https://worldguard.enginehub.org/en/latest/developer/regions/protected-region/)

    - [自定义旗标与会话处理器](https://worldguard.enginehub.org/en/latest/developer/regions/custom-flags/)

    - [空间查询](https://worldguard.enginehub.org/en/latest/developer/regions/spatial-queries/)

    - [旗标计算](https://worldguard.enginehub.org/en/latest/developer/regions/flag-calculation/)

    - [查询保护状态](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)

    - [区域事件](https://worldguard.enginehub.org/en/latest/developer/regions/events/)

  - [转换 Bukkit 对象](https://worldguard.enginehub.org/en/latest/developer/native-objects/)

  - [内部 API](https://worldguard.enginehub.org/en/latest/developer/internal-apis/)

- [进阶主题](advanced/index.md)

  - [事件日志](advanced/event-logging.md)

- [常见问题](faq.md)

- [获取帮助](support.md)

- [源代码](source-code.md)

## 链接 { #links }

- [WorldGuard 官方主页](https://www.enginehub.org/worldguard)

- [Bukkit 版下载](https://dev.bukkit.org/bukkit-plugins/worldguard/files/)

- [实验性构建](https://builds.enginehub.org/job/worldguard?branch=master)

- [Discord 服务器](https://discord.gg/enginehub/)

## 索引与表 { #indices-and-tables }

- [索引](genindex.md)

- [搜索页面](https://worldguard.enginehub.org/en/latest/search/)
