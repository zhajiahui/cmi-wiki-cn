---
title: "PlaceholderAPI"
source_kind: plugin-overview
translation_review: reviewed
---

# PlaceholderAPI

PlaceholderAPI 让服主以统一的占位符格式显示不同插件提供的信息。具体占位符可由对应插件直接提供，也可通过扩展提供；扩展可从 Expansion Cloud 下载。PlaceholderAPI 默认不附带占位符。

随包版本为 **`2.12.3`**。PlaceholderAPI 自身未声明必需插件或软依赖。本批 AttributePlus 将它列为必需依赖（`depend`）；Citizens、CMILib、CrackShotX、ItemsAdder、MMOItems、Multiverse-Core、MythicLib、MythicMobs、NeigeItems 将它列为软依赖（`softdepend`）。

## 扩展与占位符命令

命令入口为 `/placeholderapi`，别名为 `/papi`。

| 命令 | 用途 | 权限 |
| --- | --- | --- |
| `/papi parse <player|me|--null> <text>` | 解析文本中的占位符并显示结果 | `placeholderapi.parse` |
| `/papi ecloud download <expansion> [version]` | 从 eCloud 下载扩展，可指定版本 | `placeholderapi.ecloud.download` |
| `/papi list` | 列出已注册、启用的扩展 | `placeholderapi.list` |
| `/papi reload` | 重载配置并注册从 eCloud 下载的扩展 | `placeholderapi.reload` |

从 eCloud 下载扩展后，需要执行 `/papi reload` 才会正确注册。常规管理权限为 `placeholderapi.admin`，eCloud 命令另有 `placeholderapi.ecloud.*`，两者的覆盖范围不同。

更新检查、eCloud、显示格式等选项见[配置说明](configuration/index.md)。

## 官方资料

- [PlaceholderAPI 项目简介](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/7d21d2f1d73f045b86812c70e6c6975b102c6d89/README.md)
- [官方命令文档](https://wiki.placeholderapi.com/users/commands/)
- [命令别名与权限声明](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/7d21d2f1d73f045b86812c70e6c6975b102c6d89/src/main/resources/plugin.yml)
- [官方默认配置及注释](https://github.com/PlaceholderAPI/PlaceholderAPI/blob/7d21d2f1d73f045b86812c70e6c6975b102c6d89/src/main/resources/config.yml)
