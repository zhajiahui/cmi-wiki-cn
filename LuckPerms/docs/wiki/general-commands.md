---
title: 常规命令
source_url: https://luckperms.net/wiki/General-Commands
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

本页是**命令用法**的子页面。[点击此处返回。](command-usage.md)

主页面中的几个要点：

* 在 BungeeCord 上运行插件时，使用 `/lpb`，而不是 `/lp`
* 在 Velocity 上运行插件时，使用 `/lpv`，而不是 `/lp`
* 必填参数用尖括号标出，例如 `<required>`
* 可选参数用方括号标出，例如 `[optional]`
* 如果参数中需要包含空格，必须用引号将参数括起来，例如 `"  "`

___

<a id="index"></a>
### 目录
*  [/lp](general-commands.md#lp)
*  [/lp `sync`](general-commands.md#lp-sync)
*  [/lp `info`](general-commands.md#lp-info)
*  [/lp `editor`](general-commands.md#lp-editor-type-filter)
*  [/lp `verbose` \<on | record | off | upload\> [filter]](general-commands.md#lp-verbose-onrecordoffupload-filter)
*  [/lp `verbose command` \<me | player\> \<command\>](general-commands.md#lp-verbose-command-meplayer-command)
*  [/lp `tree` [scope] [player]](general-commands.md#lp-tree-scope-player)
*  [/lp `search` [comparison] \<permission\>](general-commands.md#lp-search-comparison-permission)
*  [/lp `networksync`](general-commands.md#lp-networksync)
*  [/lp `import` \<file | code --upload\> [--replace]](general-commands.md#lp-import-filecode---upload---replace)
*  [/lp `export` \<file\> [--upload]](general-commands.md#lp-export-file--upload)
*  [/lp `reloadconfig`](general-commands.md#lp-reloadconfig)
*  [/lp `bulkupdate`](general-commands.md#lp-bulkupdate-data-type-action-action-field-action-value-constraints)
*  [/lp `translations`](general-commands.md#lp-translations)
*  [/lp `creategroup` \<group\> [weight] [displayname]](general-commands.md#lp-creategroup-name-weight-displayname)
*  [/lp `deletegroup` \<group\>](general-commands.md#lp-deletegroup-name)
*  [/lp `listgroups`](general-commands.md#lp-listgroups)
*  [/lp `createtrack` \<track\>](general-commands.md#lp-createtrack-name)
*  [/lp `deletetrack` \<track\>](general-commands.md#lp-deletetrack-name)
*  [/lp `listtracks`](general-commands.md#lp-listtracks)

___
<a id="lp"></a>
#### `/lp`  
**权限**：不适用  
LuckPerms 的基础命令。列出用户有权使用的 LuckPerms 命令，并简要说明各命令的作用及其接受的参数。  

___
<a id="lp-sync"></a>
#### `/lp sync`  
**权限**： luckperms.sync  
刷新当前已加载的所有数据。如果存储中的数据发生了变化，此命令会更新服务器上的数据副本，使其包含这些变更。

___
<a id="lp-info"></a>
#### `/lp info`  
**权限**： luckperms.info  
列出 LuckPerms 的一些信息和数据，包括调试输出、统计信息、设置，以及配置中的重要值。

___
<a id="lp-editor-type-filter"></a>
#### `/lp editor [type] [filter]`  
**权限**： luckperms.editor  
**参数**：  
* `[type]` - 编辑器会话中要包含的数据类型。可以是 "all"、"users"、"online" 或 "groups"
* `[filter]` - 如果会话包含用户（例如 type = "all"、"users" 或 "online"），则会排除节点不以给定筛选内容开头的用户。权限组不受此筛选条件影响

打开用于编辑权限数据的网页界面。保存修改后，会提供一条命令；执行该命令后，修改才会生效。

___
<a id="lp-verbose-onrecordoffupload-filter"></a>
#### `/lp verbose <on|record|off|upload> [filter]`  
**权限**： luckperms.verbose  
**参数**：  
* `<on|record|off|upload>` - 启用或禁用日志记录，或上传已记录的输出
* `[filter]` - 用于筛选输出的条件

控制 LuckPerms 的详细日志系统。你可以借此监听服务器上针对玩家的所有权限检查。每当插件检查权限时，该检查都会传递给详细日志处理器。  

如果权限检查符合你的筛选条件，就会通知你。  

`on` 会启用此系统，并在检查符合筛选条件时在聊天栏中向你发送提示。`record` 的作用相同，但不会在聊天栏中通知你检查结果。`off` 会禁用检查记录，`upload` 则会将最先记录的结果上传到网页查看器，并向你提供链接。

筛选条件可以匹配权限的开头或被检查的用户。可以使用 `&`（与）和 `|`（或）符号，以及 `!` 来反转匹配结果。也支持括号 `( )`。  

**例如：**  
* `Luck & (essentials | worldedit)` - 匹配针对我的用户、且权限以 "essentials" 或 "worldedit" 开头的所有检查
* `!Luck & !anticheat` - 匹配并非针对我的用户、且权限不以 "anticheat" 开头的所有检查
* `anticheat & !anticheat.check` - 匹配权限以 "anticheat" 开头、但不以 "anticheat.check" 开头的所有检查  
  

更多信息见[**此处**](verbose.md)

___
<a id="lp-verbose-command-meplayer-command"></a>
#### `/lp verbose command <me|player> <command>`
**权限**： luckperms.verbose  
**参数**：
* `<me|player>` - 要进行详细权限检查的玩家。使用 `me` 选择自己
* `<command>` - 用于详细权限检查的命令

控制 LuckPerms 的详细日志系统。你可以借此以指定玩家的身份执行命令，并监听该命令在服务器上针对这名玩家进行的所有权限检查。

___
<a id="lp-tree-scope-player"></a>
#### `/lp tree [scope] [player]`  
**权限**： luckperms.tree  
**参数**：  
* `[scope]` - 权限树的根节点（指定 `.` 可包含所有权限）
* `[player]` - 要检查的在线玩家的名称

为服务器上已注册的权限生成树状视图。这棵树根据插件向服务器公开的数据构建，并随着插件检查权限而逐渐扩展。

所有参数都是可选的。默认选择为 `.`（仅一个点，表示全部）。

scope 参数可以让你只生成权限树的一部分。例如，scope 为 `luckperms.user` 时，只会返回以 "luckperms.user" 开头的分支。

___
<a id="lp-search-comparison-permission"></a>
#### `/lp search [comparison] <permission>`  
**权限**： luckperms.search  
**参数**：  
* `[comparison]` - 搜索内容与结果之间的关系

| 比较符 | 含义 | 作用 |
|------------|-----------------|--------------------------------------------------------------------------------|
| `==`       | "等于" | 默认比较符：返回与所搜索的 `<permission>` 相等的权限。 |
| `!=`       | "不等于" | 返回与所搜索的 `<permission>` 不相等的权限。 |
| `~~`       | "类似于" | 返回与所搜索的 `<permission>` “类似”的权限。（SQL 风格） |
| `!~`       | "不类似于 | 返回与所搜索的 `<permission>` “不类似”的权限。（SQL 风格） |

* `<permission>` - 要搜索的权限

在所有用户和权限组中搜索指定权限，并分页列出找到的全部条目。

___
<a id="lp-networksync"></a>
#### `/lp networksync`  
**权限**： luckperms.sync  
从存储提供程序刷新所有缓存数据，然后通过插件的消息服务（如果已配置）向其他所有已连接的服务器发送“ping”，请求它们也执行同步。

___
<a id="lp-import-filecode---upload---replace"></a>
#### `/lp import <file|code --upload> [--replace]`  
**权限**： luckperms.import  
**参数**：  
* `<file>` - 要导入的来源文件
* `<code> --upload` - 用于从网页导入的代码
* `[--replace]` - 如果提供此标志，将使用导入的数据覆盖并替换现有权限；否则会合并两者。


将文件或网页中的数据导入 LuckPerms。如果从文件导入，文件必须是由 Luckperms v5 导出的 JSON GZIP 类型文件。如果从网页导入，代码必须是在使用 `--upload` 标志导出时生成的。文件应放在插件目录中。从文件导入时，导入文件名中应包含 `.json.gz` 扩展名。导入文件或网页导出数据时，可以在命令末尾加上 `--replace` 标志，以覆盖并替换现有权限设置。如果未提供 `--replace` 标志，则会将现有权限设置与导入的设置合并。

___
<a id="lp-export-file--upload"></a>
#### `/lp export <file|--upload>`  
**权限**： luckperms.export  
**参数**：  
* `<file>` - 要导出到的文件
* `<--upload>` - 添加此标志后，会导出到网页，并提供用于从网页导入的代码。
* `[--without-users]` - 添加此标志后，只导出全部权限组数据，不包含任何用户数据。
* `[--without-groups]` - 添加此标志后，只导出全部用户数据，不包含任何权限组数据。

将 LuckPerms 数据导出到文件或网页数据存储中。导出的文件既可以用作备份，也可以用于在不同 LuckPerms 实例之间迁移数据。网页导出的数据会过期，不应将其用作备份。文件和网页导出的数据都可以通过 import 命令重新导入。生成的文件会保存在插件目录中。

___
<a id="lp-reloadconfig"></a>
#### `/lp reloadconfig`  
**权限**： luckperms.reloadconfig  
重新加载配置文件中的部分值。此命令不会重新加载所有配置项，其中一些配置项需要完整重启服务器才会生效（例如存储设置）。

___
<a id="lp-bulkupdate-data-type-action-action-field-action-value-constraints"></a>
#### `/lp bulkupdate <data type> <action> [action field] [action value] [constraints...]`  
**权限**：**仅限控制台**  
**参数**：  
* `<data type>` - 要修改的数据类型。（可以是 `all`、`users` 或 `groups`）
* `<action>` - 要对数据执行的操作。（可以是 `update` 或 `delete`）
* `[action field]` - 要操作的字段，仅更新操作需要此参数。（可以是 `permission`、`server` 或 `world`）
* `[action value]` - 用来替换的新值，仅更新操作需要此参数
* `[constraints]` - 更新必须满足的约束条件

批量修改所有权限数据。有关此命令的详细使用指南，见[此处](bulk-editing.md)。

___
<a id="lp-translations"></a>
#### `/lp translations`  
**权限**： luckperms.translations  
显示已加载的翻译信息，并支持安装社区提供的翻译包。

___
<a id="lp-creategroup-name-weight-displayname"></a>
#### `/lp creategroup <name> [weight] [displayname]`  
**权限**： luckperms.creategroup  
**参数**：  

* `<name>` - 权限组名称
* `[weight]` - 权限组的权重
* `[displayname]` - 权限组的显示名称

创建一个新权限组。

___
<a id="lp-deletegroup-name"></a>
#### `/lp deletegroup <name>`  
**权限**： luckperms.deletegroup  
**参数**：  
* `<name>` - 权限组名称

永久删除一个权限组。

___
<a id="lp-listgroups"></a>
#### `/lp listgroups`  
**权限**： luckperms.listgroups  
列出当前所有权限组。

___
<a id="lp-createtrack-name"></a>
#### `/lp createtrack <name>`  
**权限**： luckperms.createtrack  
**参数**：  
* `<name>` - 晋升路线名称

创建一条新的晋升路线。

___
<a id="lp-deletetrack-name"></a>
#### `/lp deletetrack <name>`  
**权限**： luckperms.deletetrack  
**参数**：  
* `<name>` - 晋升路线名称

永久删除一条晋升路线。

___
<a id="lp-listtracks"></a>
#### `/lp listtracks`  
**权限**： luckperms.listtracks  
列出当前所有晋升路线。

___
