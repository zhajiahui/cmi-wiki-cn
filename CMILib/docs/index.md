---
title: "CMILib"
source_kind: plugin-overview
translation_review: reviewed
---

# CMILib

CMILib 为多个插件提供通用功能，包括动作栏消息、悬停文本、Boss 血条、物品材质和实体识别。

随包版本为 **`1.6.0.1`**。在这批插件中，CMI 将 CMILib 声明为必需依赖（`depend`）；AttributePlus 将其声明为软依赖（`softdepend`）。

CMILib 自身未声明其他必需插件，软依赖为 PlaceholderAPI 和 MVdWPlaceholderAPI，均属于可选联动。

## 管理命令

`/cmil` 是命令入口，`/cmil reload` 用于重载配置和语言文件。官方命令处理器检查的基础命令权限为 `cmil.command`。

语言、皮肤更新、界面图标和聊天颜色等选项见[配置说明](configuration/index.md)。

## 官方资料

- [CMILib 官方简介](https://www.zrips.net/cmilib/)
- [重载命令源码](https://github.com/Zrips/CMILib/blob/ed53ef3ff44f880e40ba6e74b3165a53f9be011f/src/main/java/net/Zrips/CMILib/commands/list/reload.java)
- [命令处理器](https://github.com/Zrips/CMILib/blob/ed53ef3ff44f880e40ba6e74b3165a53f9be011f/src/main/java/net/Zrips/CMILib/commands/CommandsHandler.java)与[权限定义](https://github.com/Zrips/CMILib/blob/ed53ef3ff44f880e40ba6e74b3165a53f9be011f/src/main/java/net/Zrips/CMILib/Permissions/CMILPerm.java)
- [官方 FAQ](https://www.zrips.net/cmilib/faq/)
