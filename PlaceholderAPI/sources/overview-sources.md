---
title: "PlaceholderAPI 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# PlaceholderAPI 官方资料摘录

核对日期：2026-10-19。随包版本为 `2.12.3`。

## 占位符与扩展的关系

来源：[官方 README](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/7d21d2f1d73f045b86812c70e6c6975b102c6d89/README.md)。

> PlaceholderAPI is a plugin for Spigot servers that allows server owners to display information from various plugins with a uniform format.

> Support for specific plugins are provided either by the plugin itself or through expansions.

来源：[官方默认配置注释](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/7d21d2f1d73f045b86812c70e6c6975b102c6d89/src/main/resources/config.yml)。

> No placeholders are provided with this plugin by default.

> Download placeholders: /papi ecloud

## 命令和权限

来源：[官方 Commands](https://wiki.placeholderapi.com/users/commands/)、[plugin.yml](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/7d21d2f1d73f045b86812c70e6c6975b102c6d89/src/main/resources/plugin.yml)。

> Reloads the config settings. You need to use this command after downloading Expansions from the eCloud or they won't be properly registered.

上段为 `/papi reload` 的官方说明。命令页同时列有 `/papi parse <player|me|--null> <text>`、`/papi ecloud download <expansion> [version]` 和 `/papi list`。

```yaml
commands:
  placeholderapi:
    description: "PlaceholderAPI Command"
    aliases: ["papi"]
```

权限文件分别声明 `placeholderapi.parse`、`placeholderapi.ecloud.download`、`placeholderapi.list`、`placeholderapi.reload`。`placeholderapi.admin` 的子权限为常规管理命令；eCloud 的子权限另列在 `placeholderapi.ecloud.*` 下。

## 随包依赖声明

随包 JAR 的 `plugin.yml` 中，PlaceholderAPI 的 `depend` 与 `softdepend` 均为空。AttributePlus 的 `depend` 包含 PlaceholderAPI；Citizens、CMILib、CrackShotX、ItemsAdder、MMOItems、Multiverse-Core、MythicLib、MythicMobs、NeigeItems 的 `softdepend` 包含 PlaceholderAPI。
