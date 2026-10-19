---
title: WorldEdit
source_kind: plugin-overview
translation_review: reviewed
---

# WorldEdit

WorldEdit 是游戏内的 Minecraft 地图编辑器，可用命令和笔刷批量修改方块、生成形状、复制和粘贴区域。

随包版本：`7.4.6+7648-00664b0`。对应发布提交为 `00664b08c5d281ef47924f999320ec17a43b19e1`。

## 前置要求

本次整理的是 Bukkit 版，需要支持 Bukkit 插件的服务器。官方安装说明列出 Bukkit、Spigot 和 Paper 的安装步骤。

该构建未声明必须安装的其他插件，`Vault` 为可选软依赖。

## 常用命令与权限

| 命令 | 用途 | 相关权限 |
| --- | --- | --- |
| `//wand` | 获取选区工具 | `worldedit.wand` |
| `//pos1 [coordinates]`、`//pos2 [coordinates]` | 设置选区的两个位置 | `worldedit.selection.pos` |
| `//set <pattern>` | 设置选区内的方块 | `worldedit.region.set` |
| `//replace [from] <to>` | 替换选区内的方块 | `worldedit.region.replace` |
| `//copy` | 复制选区 | `worldedit.clipboard.copy` |
| `//paste` | 粘贴剪贴板内容 | `worldedit.clipboard.paste` |
| `/undo [times] [player]`，别名 `//undo` | 撤销历史操作 | `worldedit.history.undo`、`worldedit.history.undo.self` |
| `/redo [times] [player]`，别名 `//redo` | 重做历史操作 | `worldedit.history.redo`、`worldedit.history.redo.self` |
| `/worldedit help`，也可用 `//help` | 查看命令帮助 | `worldedit.help` |
| `/worldedit reload` | 重载配置 | `worldedit.reload` |

以上为常用命令的基本形式，完整参数和权限说明见[官方命令参考][WE-CMD]与[官方权限表][WE-PERM]。权限列保留官方列出的相关节点，不表示同一格中的多个节点必须同时授予。官方还提供 `worldedit.*`，用于完整访问 WorldEdit。

## 配置说明

[查看配置文件中文说明](configuration/index.md)。官方配置参考见 [官方配置参考][WE-CONFIG]；Bukkit 版的嵌套 YAML 键可对照对应版本的[默认配置][WE-DEFAULT]。

## 官方资料

- [WorldEdit 官方项目页](https://enginehub.org/worldedit/)
- [WorldEdit 官方文档][WE-INTRO]
- [WorldEdit 官方仓库](https://github.com/EngineHub/WorldEdit)
- [7.4.6 对应构建的插件描述文件][WE-PLUGIN]
- [官方安装说明][WE-INSTALL]
- [7.4.6 发布提交][WE-RELEASE]

[WE-INTRO]: https://worldedit.enginehub.org/en/latest/
[WE-RELEASE]: https://github.com/EngineHub/WorldEdit/commit/00664b08c5d281ef47924f999320ec17a43b19e1
[WE-INSTALL]: https://worldedit.enginehub.org/en/latest/install/
[WE-PLUGIN]: https://github.com/EngineHub/WorldEdit/blob/00664b08c5d281ef47924f999320ec17a43b19e1/worldedit-bukkit/src/main/resources/plugin.yml
[WE-CMD]: https://worldedit.enginehub.org/en/latest/commands/
[WE-PERM]: https://worldedit.enginehub.org/en/latest/permissions/
[WE-CONFIG]: https://worldedit.enginehub.org/en/latest/config/
[WE-DEFAULT]: https://github.com/EngineHub/WorldEdit/blob/00664b08c5d281ef47924f999320ec17a43b19e1/worldedit-bukkit/src/main/resources/defaults/config.yml
