---
title: 用户命令
source_url: https://luckperms.net/wiki/User-Commands
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

本页是**命令用法**主页的子页面。[点击此处返回。](command-usage.md)

请记住主页中的以下要点：

* 在 BungeeCord 上运行插件时，使用 `/lpb` 而不是 `/lp`
* 在 Velocity 上运行插件时，使用 `/lpv` 而不是 `/lp`
* 必填参数用尖括号标记，例如 `<required>`
* 可选参数用方括号标记，例如 `[optional]`
* 如果参数包含空格，必须用引号包住整个参数，例如 `"  "`

___

<a id="index"></a>
### 目录
*  [/lp user \<user\> `info`](user-commands.md#lp-user-user-info)
*  [/lp user \<user\> `permission`](permission-commands.md)
*  [/lp user \<user\> `parent`](parent-commands.md)
*  [/lp user \<user\> `meta`](meta-commands.md)
*  [/lp user \<user\> `editor`](user-commands.md#lp-user-user-editor)
*  [/lp user \<user\> `promote` \<track\> [context...]](user-commands.md#lp-user-user-promote-track-context-flags)
*  [/lp user \<user\> `demote` \<track\> [context...]](user-commands.md#lp-user-user-demote-track-context-flags)
*  [/lp user \<user\> `showtracks`](user-commands.md#lp-user-user-showtracks)
*  [/lp user \<user\> `clear` [context...]](user-commands.md#lp-user-user-clear-context)
*  [/lp user \<user\> `clone` \<user\>](user-commands.md#lp-user-user-clone-user)

___
<a id="lp-user-user-info"></a>
#### `/lp user <user> info`  
**权限**：luckperms.user.info  
显示用户信息，包括用户名、主权限组、父级和当前上下文。

___
<a id="lp-user-user-editor"></a>
#### `/lp user <user> editor`  
**权限**：luckperms.user.editor  
打开网页界面，以编辑指定权限组的权限。保存更改后，系统会给出一条命令，必须执行该命令，更改才会生效。

___
<a id="lp-user-user-promote-track-context-flags"></a>
#### `/lp user <user> promote <track> [context...] [flags...]`  
**权限**：luckperms.user.promote  
**参数**：  
* `<track>` - 沿哪条晋升路线晋升
* `[context...]` - 晋升所处的[上下文](context.md)
**标志**：
* `[--dont-add-to-first]` - 如果用户没有该晋升路线上的父级权限组，命令会执行失败
* `[-s]` - 静默执行，不输出用户在晋升路线上的进度

此命令会让用户沿晋升路线晋升。首先，命令会检查用户在给定上下文中是否位于指定晋升路线上。如果不在，除非使用了相应标志，否则会将用户加入该晋升路线的第一个权限组。如果用户同时位于晋升路线上的多个位置，命令会执行失败。其他情况下，用户会沿晋升路线升到下一级，并从原有权限组中移除。如果此操作影响其主权限组，主权限组也会一并更新。

___
<a id="lp-user-user-demote-track-context-flags"></a>
#### `/lp user <user> demote <track> [context...] [flags...]`  
**权限**：luckperms.user.demote  
**参数**：  
* `<track>` - 沿哪条晋升路线降级
* `[context...]` - 降级所处的[上下文](context.md)
**标志**：
* `[--dont-remove-from-first]` - 如果用户位于晋升路线的第一个位置，命令会执行失败
* `[-s]` - 静默执行，不输出用户在晋升路线上的进度

此命令会让用户沿晋升路线降级。首先，命令会检查用户在给定上下文中是否位于指定晋升路线上。如果不在，或同时位于晋升路线上的多个位置，命令会执行失败。否则，用户会沿晋升路线降到下一级，并从原有权限组中移除。如果此操作影响其主权限组，主权限组也会一并更新。

___
<a id="lp-user-user-showtracks"></a>
#### `/lp user <user> showtracks`  
**权限**：luckperms.user.showtracks  
列出用户当前所在的所有晋升路线。

___
<a id="lp-user-user-clear-context"></a>
#### `/lp user <user> clear [context...]`  
**权限**：luckperms.user.clear  
**参数**：  
* `[context...]` - 用于筛选的[上下文](context.md)

清除用户的权限、父级权限组和元数据。

___
<a id="lp-user-user-clone-user"></a>
#### `/lp user <user> clone <user>`  
**权限**：luckperms.user.clone  
**参数**：  
* `<user>` - 另一个用户的名称

将该用户的数据克隆到另一个用户。

___
