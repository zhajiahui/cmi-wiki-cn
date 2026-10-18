---
title: 首次运行
---

# 首次运行

插件无需依赖其他插件即可单独运行。部分功能可能受限，例如经济功能。除此以外，将插件文件放入 `~/plugins/` 文件夹，再启动服务器即可。

首次运行时，插件会生成默认文件，其中包括语言文件。你可以在语言文件中修改或翻译插件显示的消息。

CMI 默认不会向普通玩家开放指令。玩家需要拥有对应的权限节点，才能使用相应指令。

指令默认使用长格式，例如 `/cmi heal [playerName]`。有两种方式可以改为短指令：

- 在 `~/plugins/Settings/Alias.yml` 中启用预设的短指令，再执行 `/cmi reload` 或重启服务器。这样就可以使用 `/heal [playerName]`。
- 使用 `/cmi aliaseditor` 创建自己的短指令，例如 `/cmi aliaseditor new heal-cmi heal $1-`。

如果你正在从 EssentialsX 迁移，可以使用 `/cmi importfrom essentials [home/warp/nick/logoutlocation/money/mail]` 导入玩家数据，包括余额。

CMI 默认使用 SQLite 数据库。若要更换数据库类型，可以修改 `~/plugins/CMI/Settings/DataBaseInfo.yml` 中的存储方式，再重载插件。直接更改存储方式不会保留当前已有的数据。

若要在更换数据库类型时保留数据，使用 `/cmi migratedatabase`。该命令会根据当前存储方式，将数据从 SQLite 迁移到 MySQL，或从 MySQL 迁移到 SQLite。迁移前需要正确填写 MySQL 的密码、用户名、数据库名等信息。

经济系统和聊天管理默认关闭。可以在 `~/plugins/CMI/config.yml` 中启用；可能需要完整重启服务器才会完全生效。

---

[查看原文](https://www.zrips.net/cmi/first-run/)
