---
title: 区域命令
source_url: https://worldguard.enginehub.org/en/latest/regions/commands/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 区域命令 { #region-commands }

其他与区域保护无关的命令见[命令](../commands.md)页面；本页命令所需节点详见[权限](../permissions.md)页面。

部分命令可能在后台执行，稍后才返回结果。可用 `/wg running` 查看正在运行的后台命令；运行中及排队中的命令数量都有硬性上限。

区域命令既可用 `/region`，也可用 `/rg`。部分子命令有多个别名，例如 `/rg d` 是 `/rg define` 的简写。

!!! tip "提示"

    几乎所有这些命令都能在控制台使用，但有时需要指定 `-w` 选项（命令支持时）。

    也可使用 WorldEdit 的 [//world](https://worldedit.enginehub.org/en/latest/commands/#command-//world) 命令设置目标世界，控制台和游戏内均可使用。

## 创建和删除区域 { #creating-and-removing-regions }

### 定义区域 { #define }

```text
/rg define [-w <world>] [-g] <id> [<owner1>] [<owner2>] [... <ownerN>]
/rg create (...)
/rg def (...)
/rg d (...)
```

用给定 ID 创建新区域，可选指定一组所有者。区域范围取自当前的 WorldEdit 选区。

区域 ID 不区分大小写。同一世界中，同一个名称只能对应一个区域。

- `-g` 会创建没有实际空间范围的新“全局”区域，它与[全局区域](global-region.md)并非同一概念，可用于创建模板区域，详见[优先级与继承](priorities.md)

示例：创建名为“shop”的新区域，并将“sk89q”和“wizjany”设为所有者

```text
/rg define shop sk89q wizjany
```

### 删除区域 { #remove }

```text
/rg remove [-w <world>] [-f] [-u] <id>
/rg rem (...)
/rg delete (...)
/rg del (...)
```

删除一个区域。

如果指定区域有子区域，必须提供 `-u` 或 `-f`，两者不能同时使用。

- `-u` 让指定区域的子区域不再拥有父区域

- `-f` 删除指定区域的子区域

### 重新定义区域 { #redefine }

```text
/rg redefine [-w <world>] [-g]
/rg update (...)
/rg move (...)
```

使用当前 WorldEdit 选区替换现有区域的实际范围。

- `-g` 会创建没有实际空间范围的新“全局”区域，它与[全局区域](global-region.md)并非同一概念，可用于创建模板区域，详见[优先级与继承](priorities.md)

### 认领区域 { #claim }

```text
/rg claim <id>
```

认领一个区域，供玩家自助创建区域使用。详见[认领区域](claiming.md)。

## 修改成员关系 { #editing-memberships }

### 添加成员 { #add-member }

```text
/rg addmember [-w <world>] <id> <members...>
/rg addmem (...)
/rg am (...)
```

向区域添加任意数量的成员。使用 `g:<member>` 可添加权限组，而不是玩家。

示例：将“builder”组和玩家“sk89q”添加为“lobby”世界中“spawn”区域的成员。

```text
/rg addmember -w lobby spawn g:builder sk89q
```

### 添加所有者 { #add-owner }

```text
/rg addowner [-w <world>] <id> <owners...>
/rg ao (...)
```

向区域添加任意数量的所有者。使用 `g:<owner>` 可添加权限组，而不是玩家。

示例：将“admins”组和玩家“eduardo”添加为“lobby”世界中“spawn”区域的成员。

```text
/rg addowner -w lobby spawn g:admins eduardo
```

### 移除成员 { #remove-member }

```text
/rg removemember [-w <world>] [-a] <id> <members...>
/rg remmember (...)
/rg removemem (...)
/rg remmem (...)
/rg rm (...)
```

从区域中移除任意数量的成员。与添加命令相同，使用 `g:<member>` 指定权限组。

- `-a` 会移除区域的全部成员，并忽略 &lt;members…&gt; 参数

### 移除所有者 { #remove-owner }

```text
/rg removeowner [-w <world>] [-a] <id> <owners...>
/rg remowner
/rg ro (...)
```

从区域中移除任意数量的所有者。与添加命令相同，使用 `g:<owner>` 指定权限组。

- `-a` 会移除区域的全部所有者，并忽略 &lt;owners…&gt; 参数

## 获取信息 { #getting-information }

### 选择区域 { #select }

```text
/rg select [-w <world>] [<id>]
/rg sel (...)
/rg s (...)
```

将当前 WorldEdit 选区替换为现有区域的范围。未指定区域时，会尝试选择你当前所在的区域。

### 信息 { #information }

```text
/rg info [-u] [-s] [-w <world>] [<id>]
/rg i (...)
```

显示指定区域的信息；未指定时，显示当前所在区域的信息。如果当前处于多个区域中，则会列出这些区域。

- `-s` 会同时选中该区域，详见 `/rg select`

- `-u` 会显示 UUID，而不是玩家上次使用的名称

示例：显示[全局区域](global-region.md)的信息

```text
/rg info __global__
```

### 旗标 { #flags }

```text
/rg flags [-w <world>] [-p <page>] <id>
```

显示指定区域的分页交互式旗标列表。

明确设置的旗标值显示为白色，从父区域继承的旗标显示为浅灰色，未设置的旗标则以深灰色显示默认值。

点击旗标值可快速设置或取消设置；底部页码旁的箭头可用来翻页。

### 列表 { #list }

```text
/rg list [-i <id search>] [-p <player>] [-w <world>] [-s] [<page>]
```

列出已创建的区域。可以提供页码以查看指定页面。

如果玩家没有列出全部区域的权限，但有权列出自己的区域（即自己为成员或所有者的区域），命令会自动只显示这些区域。

- 可用 `-p <player>`，只列出指定玩家作为成员或所有者的区域

- 可用 `-i <id search>`，只列出 ID 包含搜索文字的区域

- 可用 `-s`，只匹配与当前 WorldEdit 选区实际相交的区域

示例：列出“sk89q”作为成员或所有者的区域

```text
/rg list -p sk89q
```

## 设置区域选项 { #setting-region-options }

### 旗标 { #flag }

```text
/rg flag <id> <flag> [-w <world>] [-g <group>] [-e] [<value>]
/rg f (...)
```

设置区域旗标，更多信息见[区域旗标](flags.md)。

要取消设置旗标，不提供值即可。

要把旗标设为空值，使用 `-e`。例如，将 `greeting` 设为空消息，可覆盖另一个范围更大、优先级更低的区域设置的欢迎消息。同时指定 `-e` 和一个值时，该值会被丢弃。

- `-g <group>` 指定区域组，详见[区域旗标](flags.md)

- `-e` 设置空值

示例：将“mall”区域的 `pvp` 设为“deny”，并将区域组设为“nonmembers”

```text
/rg flag mall pvp -g nonmembers deny
```

示例：取消“mall”区域的 `greeting` 设置

```text
/rg flag mall greeting
```

示例：将 `greeting` 设为空值

```text
/rg flag mall greeting -e
```

### 优先级 { #priority }

```text
/rg setpriority [-w <world>] <id> <priority>
/rg priority (...)
/rg pri (...)
```

设置区域优先级，更多信息见[优先级与继承](priorities.md)。

区域的默认优先级为 0。

### 父区域 { #parent }

```text
/rg setparent [-w <world>] <id> [<parent>]
/rg parent (...)
/rg par (...)
```

设置区域的父区域，更多信息见[优先级与继承](priorities.md)。

要取消父区域设置，不指定父区域即可。

示例：将“plot1”的父区域设为“mall”

```text
/rg setparent plot1 mall
```

示例：移除“plot1”的父区域

```text
/rg setparent plot1
```

## 其他命令 { #miscellaneous-commands }

### 传送 { #teleport }

```text
/rg teleport [-w <world>] [-c] [-s] <id>
/rg tp (...)
```

将你传送到 `spawn` 或 `teleport` [旗标](flags.md)指定的位置。

- `-s` 使用 spawn 旗标，而非 teleport 旗标

- `-c` 会将你传送到区域的几何中心，即使两个旗标都未设置也可使用，但必须处于旁观模式。

## 管理命令 { #management-commands }

### 加载 { #load }

```text
/rg load [-w <world>]
/rg reload (...)
```

从文件或数据库重新加载区域数据。如果最近在游戏内修改了区域数据，此操作可能导致数据丢失。

加载操作在后台运行，不会暂停服务器。上一次加载尚未结束时再次执行命令，新的加载任务会进入队列；队列中的操作数量有上限。

### 保存 { #save }

```text
/rg save [-w <world>]
/rg write (...)
```

将区域数据保存到磁盘。

!!! tip "提示"

    区域数据发生任何修改后，很快就会自动保存，因此无需手动执行此命令。

保存操作在后台运行，不会暂停服务器。上一次保存尚未结束时再次执行命令，新的保存任务会进入队列；队列中的操作数量有上限。

### 迁移数据库 { #migrate-database }

```text
/rg migratedb <from> <to>
```

从一种[存储驱动](storage.md)迁移到另一种。

“from”和“to”的有效取值为：

- `yaml`

- `mysql`

迁移不会自动启用目标存储驱动，必须在[配置](../config.md)中另行启用。

!!! warning "警告"

    执行迁移前务必备份。

!!! warning "警告"

    此命令不在后台运行，会暂停整个服务器。如果服务器软件会检测服务器停顿，可能在迁移时结束服务器进程并中断迁移。迁移被中断或失败后，可能需要先清空目标存储，再重新执行。

### 迁移 UUID { #migrate-uuid }

```text
/rg migrateuuid
```

将区域数据中的玩家名称转换为 Mojang UUID。

没有对应 UUID 的名称会被移除或保留，取决于[配置](../config.md)中的 `keep-names-that-lack-uuids` 设置。

!!! warning "警告"

    执行迁移前务必备份。

!!! warning "警告"

    此命令不在后台运行，会暂停整个服务器。如果服务器软件会检测服务器停顿，可能在迁移时结束服务器进程并中断迁移。

### 迁移区域高度 { #migrate-region-heights }

```text
/rg migrateheights [-w <world>]
```

将当前世界或指定世界中范围满足 min y &lt;= 0 且 max y &gt;= 255 的区域（即 MC 1.18 之前的世界高度范围），扩展到新的世界高度边界。

如果原先有大量区域按世界高度边界划定，从 1.17 或更早版本升级到 1.18 或更新版本时，此命令会很有用。注意，如果在 1.18 之前有意将区域设在世界边界之外，就需要手动将它们移到新的世界边界之外。

!!! warning "警告"

    执行迁移前务必备份。

!!! warning "警告"

    此命令不在后台运行，会暂停整个服务器。如果服务器软件会检测服务器停顿，可能在迁移时结束服务器进程并中断迁移。
