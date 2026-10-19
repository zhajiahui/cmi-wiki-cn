---
title: WorldEdit 插件介绍来源
source_kind: plugin-overview
translation_review: reviewed
---

# WorldEdit 插件介绍来源

核对日期：2026-10-19。介绍对应版本：`7.4.6+7648-00664b0`。以下为本次直接读取的官方文档及官方仓库片段；网页仅整理空白和换行，源码摘录可能选自不同位置。

## WorldEdit 7.4.6 发布提交

来源：[https://github.com/EngineHub/WorldEdit/commit/00664b08c5d281ef47924f999320ec17a43b19e1](https://github.com/EngineHub/WorldEdit/commit/00664b08c5d281ef47924f999320ec17a43b19e1)

取得：本轮 GitHub 只读工具直接取得对应提交内容。

```text
sha: 00664b08c5d281ef47924f999320ec17a43b19e1
message: Release 7.4.6
author date: 2026-10-15T03:29:49Z
```

## WorldEdit 官方简介

来源：[https://worldedit.enginehub.org/en/latest/](https://worldedit.enginehub.org/en/latest/)

取得：HTTP 200；2026-10-19T12:48:39.374Z。

```text
WorldEdit is an easy-to-use in-game Minecraft map editor. Through a combination of commands and “brushes,” you can sculpt your world or simply perform numerous terraforming tasks.
Quickly create, replace or delete thousands of blocks in seconds
No longer waste time doing mundane activities like fix badly flowing water!
Quickly create basic shapes like spheres, cylinders, and so on
Copy areas, paste them, load them, and save them as .schematics
Do cool things like input mathematical expressions to generate terrain
Use “brush tools” to carve out mountains, ravines, and so on
Use your compass to quickly teleport to areas by left clicking or using /jumpto
Choose an area and have it instantly restored from backups
```

## WorldEdit 安装要求与 Bukkit 安装

来源：[https://worldedit.enginehub.org/en/latest/install/](https://worldedit.enginehub.org/en/latest/install/)

取得：HTTP 200；2026-10-19T12:47:01.661Z。

```text
WorldEdit runs on the Java edition of Minecraft, either on your single player/local game or a dedicated server.
WorldEdit can’t be used on Realms, Windows 10 Edition, Bedrock Edition, or Pocket Edition versions. These versions of Minecraft have limited or no mod support. Note that “Windows 10 Edition” refers to a specific Edition of Minecraft, not the Java Edition running on a Windows 10 computer.
Before you install WorldEdit, you will first have to install a “mod loader” like NeoForge, Fabric, Spigot, Bukkit, or Sponge. We’ll advise you to choosing your mod loader below.
Choosing a Mod Loader#

Bukkit / Spigot / Paper#
Once you’ve set up your Bukkit-based server (instructions can be found on the respective Paper/Spigot sites), download WorldEdit from Modrinth. Make sure you get the right WorldEdit download for your Minecraft version.
In your server folder, create a “plugins” folder if one does not yet exist. (It should be created when you first run the server).
Move the WorldEdit .jar file into the plugins folder.
Start your server.
Check your server log for errors. If you encounter errors, see the FAQ page.
NeoForge Single-Player#
```

## WorldEdit 对应构建 plugin.yml

来源：[https://github.com/EngineHub/WorldEdit/blob/00664b08c5d281ef47924f999320ec17a43b19e1/worldedit-bukkit/src/main/resources/plugin.yml](https://github.com/EngineHub/WorldEdit/blob/00664b08c5d281ef47924f999320ec17a43b19e1/worldedit-bukkit/src/main/resources/plugin.yml)

取得：本轮 GitHub 只读工具直接取得对应提交内容。

```text
name: WorldEdit
main: com.sk89q.worldedit.bukkit.WorldEditPlugin
version: "${internalVersion}"
load: STARTUP
api-version: 1.21.4
folia-supported: true
softdepend: [Vault]
author: EngineHub
website: https://enginehub.org/worldedit
```

## WorldEdit 常用命令用法与权限

来源：[https://worldedit.enginehub.org/en/latest/commands/](https://worldedit.enginehub.org/en/latest/commands/)

取得：HTTP 200；2026-10-19T12:47:01.730Z。

```text
//wand
Description
Get the wand item
You must have also have permission to use at least one of the features of the requested wand.
Permissions
worldedit.wand
Usage
//wand [-n]

//pos1
Description
Set position 1
Permissions
worldedit.selection.pos
Usage
//pos1 [coordinates]
  [coordinates]

//pos2
Description
Set position 2
Permissions
worldedit.selection.pos
Usage
//pos2 [coordinates]
  [coordinates]

//set
Description
Sets all the blocks in the region
Permissions
worldedit.region.set
Usage
//set <pattern>
  <pattern>

//replace (or //re, //rep)
Description
Replace all blocks in the selection with another
Permissions
worldedit.region.replace
Usage
//replace [from] <to>
  [from]

//copy
Description
Copy the selection to the clipboard
Permissions
worldedit.clipboard.copy
Usage
//copy [-be] [-m <mask>]
  [-e]

//paste
Description
Paste the clipboard’s contents
Permissions
worldedit.clipboard.paste
Usage
//paste [-abenosv] [-m <sourceMask>]
  [-a]

/undo (or //undo)
Description
Undoes the last action (from history)
Permissions
worldedit.history.undo, worldedit.history.undo.self
Usage
/undo [times] [player]
  [times]

/redo (or //redo)
Description
Redoes the last action (from history)
Permissions
worldedit.history.redo, worldedit.history.redo.self
Usage
/redo [times] [player]
  [times]

/worldedit help
Description
Displays help for WorldEdit commands
Permissions
worldedit.help
Usage
/worldedit help [-s] [-p <page>] [command...]
  [-s]

/worldedit reload
Description
Reload configuration
Permissions
worldedit.reload
Usage
/worldedit reload
/worldedit cui
```

## WorldEdit 权限说明及对应表

来源：[https://worldedit.enginehub.org/en/latest/permissions/](https://worldedit.enginehub.org/en/latest/permissions/)

取得：HTTP 200；2026-10-19T12:48:39.377Z。

```text
By default, no one can use WorldEdit. In order for yourself, moderators, and players to use WorldEdit, you must provide the proper permissions. One way is to provide op to moderators and administrators (unless disabled in the configuration), but providing the permission nodes on this page (through a permissions plugin) is the more flexible.
You can give the worldedit.* permission to give yourself and other administrators full access to WorldEdit.

/worldedit help
worldedit.help
/worldedit reload
worldedit.reload
/undo
worldedit.history.undo, worldedit.history.undo.self
/redo
worldedit.history.redo, worldedit.history.redo.self
//pos
worldedit.selection.pos
//pos1
worldedit.selection.pos
//pos2
worldedit.selection.pos
//wand
worldedit.wand
/toggleeditwand
worldedit.wand.toggle
//set
worldedit.region.set
//replace
worldedit.region.replace
//copy
worldedit.clipboard.copy
//paste
worldedit.clipboard.paste
//help
worldedit.help
worldedit.region.set
worldedit:region.set
worldedit.region.set
```

## WorldEdit 配置位置与参考字段

来源：[https://worldedit.enginehub.org/en/latest/config/](https://worldedit.enginehub.org/en/latest/config/)

取得：HTTP 200；2026-10-19T12:47:01.734Z。

```text
Configuration#
Although WorldEdit is primarily command driven, there are some configuration options which may change or limit the behavior of WorldEdit’s commands and tools.
Configuration Files#
Once you have run your server with WorldEdit installed, you will find the main configuration file generated in a location which depends on your platform.
Bukkit Server#
Configuration options for the Bukkit version of WorldEdit are found in plugins/WorldEdit/config.yml, relative to the server root.

defaultChangeLimit
-1
The default amount of blocks that can be set in one operation.
maxChangeLimit
-1
The maximum amount of blocks for the change limit (set with //limit in-game)
```

## WorldEdit 7.4.6 默认 Bukkit 配置片段

来源：[https://github.com/EngineHub/WorldEdit/blob/00664b08c5d281ef47924f999320ec17a43b19e1/worldedit-bukkit/src/main/resources/defaults/config.yml](https://github.com/EngineHub/WorldEdit/blob/00664b08c5d281ef47924f999320ec17a43b19e1/worldedit-bukkit/src/main/resources/defaults/config.yml)

取得：本轮 GitHub 只读工具直接取得对应提交内容。

```text
# WorldEdit's Configuration File
# - DO NOT USE TABS. You MUST use spaces or Bukkit will complain and post
#   errors. If you use an editor, like Notepad++ (recommended for Windows
#   users), you must configure it to "replace tabs with spaces."
# - Don't get rid of indentations. They are indented so some entries that are
#   in categories, like "max-blocks-changed", are placed in the "limits"
#   category.

limits:
    max-blocks-changed:
        default: -1
        maximum: -1
```

