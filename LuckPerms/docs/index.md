---
title: "LuckPerms"
source_kind: plugin-overview
translation_review: reviewed
---

# LuckPerms

LuckPerms 是权限管理插件。服主可以创建权限组、分配权限，控制玩家可使用的功能；权限可通过命令、配置文件或网页编辑器管理。

随包版本为 **`5.5.71`**。该版本未声明必需插件；LilyPad-Connect 和 ViaVersion 列在其软依赖（`softdepend`）中。本批 ItemsAdder 也将 LuckPerms 列为软依赖，表示可选集成。

## 常用管理命令

| 命令 | 用途 | 权限 |
| --- | --- | --- |
| `/lp` | 显示当前用户有权使用的 LuckPerms 命令 | 无单独权限要求 |
| `/lp editor [type] [filter]` | 打开网页权限编辑器；保存后执行编辑器给出的命令使改动生效 | `luckperms.editor` |
| `/lp sync` | 从存储刷新当前已加载的数据 | `luckperms.sync` |
| `/lp reloadconfig` | 重载部分配置值 | `luckperms.reloadconfig` |

`/lp reloadconfig` 不会重载所有设置。存储设置等选项需要完整重启服务器后生效。

主配置及其选项见[配置说明](configuration/index.md)。

## 官方资料

- [项目简介](https://github.com/LuckPerms/LuckPerms/blob/5fc3d583c412854e050b1e4ba8aa5036d8daf982/README.md)
- [常规命令](https://github.com/LuckPerms/wiki/blob/fc2919c3d5e6bfba82af31f9930273b00f08ddbf/pages/General-Commands.md)与[权限列表](https://github.com/LuckPerms/wiki/blob/fc2919c3d5e6bfba82af31f9930273b00f08ddbf/pages/Permissions.md)
- [官方配置文档](https://luckperms.net/wiki/Configuration)
