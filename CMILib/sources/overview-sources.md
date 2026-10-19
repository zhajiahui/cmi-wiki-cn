---
title: "CMILib 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# CMILib 官方资料摘录

核对日期：2026-10-19。以下摘录用于核对简介与命令；随包版本和前置关系另按随包 JAR 的 `plugin.yml` 核对。

## 通用库的用途

来源：[CMILib 官方简介](https://www.zrips.net/cmilib/)。

> CMILib is used in multiple plugins as a base core for most used actions like action bar messages, hover over messages, bossbar, material recognition, entity recognitions and so on.

对应中文：为多个插件提供动作栏、悬停文本、Boss 血条、材质及实体识别等通用功能。

## 命令与基础权限

来源：[reload.java](https://github.com/Zrips/CMILib/blob/ed53ef3ff44f880e40ba6e74b3165a53f9be011f/src/main/java/net/Zrips/CMILib/commands/list/reload.java)、[CommandsHandler.java](https://github.com/Zrips/CMILib/blob/ed53ef3ff44f880e40ba6e74b3165a53f9be011f/src/main/java/net/Zrips/CMILib/commands/CommandsHandler.java)、[CMILPerm.java](https://github.com/Zrips/CMILib/blob/ed53ef3ff44f880e40ba6e74b3165a53f9be011f/src/main/java/net/Zrips/CMILib/Permissions/CMILPerm.java)。

> Reloads plugins config and locale files

```java
public static final String label = "cmil";
command("Gives access to base usage of commands"),
return CommandsHandler.getLabel() + "." + perm;
```

上述行分别摘自命令处理器和权限枚举：命令标签为 `cmil`，基础权限生成结果为 `cmil.command`；`reload` 子命令重载配置和语言文件。没有将未核实的子命令权限按名称拼入简介。

## 随包元数据

- 版本：`1.6.0.1`。
- CMILib 的 `depend` 为空；`softdepend` 为 PlaceholderAPI、MVdWPlaceholderAPI。
- CMI 的 `depend` 包含 CMILib；AttributePlus 的 `softdepend` 包含 CMILib。

补充入口：[官方 FAQ](https://www.zrips.net/cmilib/faq/)。本次未找到覆盖全部选项的独立官方配置手册；配置选项的解释依据随包原始注释。
