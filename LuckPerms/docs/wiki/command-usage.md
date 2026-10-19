---
title: 命令用法
source_url: https://luckperms.net/wiki/Command-Usage
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

如果提供的参数无效，控制台或聊天栏中会显示命令用法。**直接输入 /lp** 即可列出用户有权使用的所有命令。

如果输入命令后只显示插件版本，说明你没有使用任何命令的权限。需要先在服务器控制台[为自己授予 LuckPerms 命令的使用权限](usage.md#granting-full-access-to-luckperms)。

<a id="aliases"></a>
### 命令别名
下表列出了各平台的命令别名。这些命令的作用完全相同，可以按自己的习惯选用。

| Bukkit / Sponge / Fabric / Forge / Nukkit   | BungeeCord         | Velocity             |
| ----------------------------------- | ------------------ | -------------------- |
| `/lp`                               | `/lpb`             | `/lpv`               |
| `/luckperms`                        | `/luckpermsbungee` | `/luckpermsvelocity` |
| `/permissions`（*已弃用*）       |                    |                      |
| `/perms`（*已弃用*）             |                    |                      |
| `/perm`（*已弃用*）              |                    |                      |

**`Important:`** BungeeCord 和 Velocity 上的命令别名不同，这样你就可以选择命令的执行位置。如果别名相同，命令就会始终由代理端处理，你也就始终无法控制后端服务器上的 LuckPerms！

如果使用 Bukkit/Spigot，默认情况下，所有拥有 OP 权限的用户都可以使用 LuckPerms 命令。可以在配置中修改这一设置。

<a id="overview"></a>
# 概览
<a id="arguments-key"></a>
#### 参数标记说明：
* `<required>` - 执行命令时*必须*指定此参数
* `[optional]` - 此参数可以省略；未提供时会使用默认值。

如果参数中需要包含空格，必须用引号将参数括起来。`"  "`

下文使用的别名（`/lp`）可以替换成上方命令别名一节列出的任意别名。

<a id="general-commands"></a>
### 常规命令
用于操作 LuckPerms 各项功能的常规命令。

*  [/lp](general-commands.md#lp)
*  [/lp `sync`](general-commands.md#lp-sync)
*  [/lp `info`](general-commands.md#lp-info)
*  [/lp `editor`](general-commands.md#lp-editor-type-filter)
*  [/lp `verbose` \<on | record | off | upload\> [filter]](general-commands.md#lp-verbose-onrecordoffupload-filter)
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

<a id="user-commands"></a>
### 用户命令
用于查看或修改指定用户的命令。

命令格式为 `/lp user <user> ...`，其中 `<user>` 是要查询或修改的用户的用户名或 UUID。
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

<a id="group-commands"></a>
### 权限组命令
用于查看或修改指定权限组的命令。

命令格式为 `/lp group <group> ...`，其中 `<group>` 是要查询或修改的权限组名称。
*  [/lp group \<group\> `info`](group-commands.md#lp-group-group-info)
*  [/lp group \<group\> `permission`](permission-commands.md)
*  [/lp group \<group\> `parent`](parent-commands.md)
*  [/lp group \<group\> `meta`](meta-commands.md)
*  [/lp group \<group\> `editor`](group-commands.md#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](group-commands.md#lp-group-group-listmembers-page)
*  [/lp group \<group\> `setweight` \<weight\>](group-commands.md#lp-group-group-setweight-weight)
*  [/lp group \<group\> `setdisplayname` \<name\>](group-commands.md#lp-group-group-setdisplayname-name)
*  [/lp group \<group\> `showtracks`](group-commands.md#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](group-commands.md#lp-group-group-clear-context)
*  [/lp group \<group\> `rename` \<new name\>](group-commands.md#lp-group-group-rename-new-name)
*  [/lp group \<group\> `clone` \<name of clone\>](group-commands.md#lp-group-group-clone-new-name)

<a id="permission-commands"></a>
### 权限命令
用于查看或修改指定用户或权限组的权限数据的命令。

命令格式为 `/lp user <user> permission ...` 或 `/lp group <group> permission ...`
*  [`info`](permission-commands.md#lp-usergroup-usergroup-permission-info-page-sorting-mode)
*  [`set` \<node\> \<true/false\> [context...]](permission-commands.md#lp-usergroup-usergroup-permission-set-node-truefalse-context)
*  [`unset` \<node\> [context...]](permission-commands.md#lp-usergroup-usergroup-permission-unset-node-context)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](permission-commands.md#lp-usergroup-usergroup-permission-settemp-node-truefalse-duration-temporary-modifier-context)
*  [`unsettemp` \<node\> [duration] [context...]](permission-commands.md#lp-usergroup-usergroup-permission-unsettemp-node-duration-context)
*  [`check` \<node\>](permission-commands.md#lp-usergroup-usergroup-permission-check-node)
*  [`clear` [context...]](permission-commands.md#lp-usergroup-usergroup-permission-clear-context)

<a id="parent-commands"></a>
### 父级命令
用于查看或修改指定用户或权限组的继承属性（父级）的命令。

命令格式为 `/lp user <user> parent ...` 或 `/lp group <group> parent ...`
*  [`info`](parent-commands.md#lp-usergroup-usergroup-parent-info-page-sorting-mode)
*  [`set` \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-set-group-context)
*  [`add` \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-add-group-context)
*  [`remove` \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-remove-group-context)
*  [`settrack` \<track\> \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-settrack-track-indexgroup-context)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](parent-commands.md#lp-usergroup-usergroup-parent-addtemp-group-duration-temporary-modifier-context)
*  [`removetemp` \<group\> [duration] [context...]](parent-commands.md#lp-usergroup-usergroup-parent-removetemp-group-duration-context)
*  [`clear` [context...]](parent-commands.md#lp-usergroup-usergroup-parent-clear-context)
*  [`cleartrack` \<track\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-cleartrack-track-context)
*  [`switchprimarygroup` \<group\>](parent-commands.md#lp-user-user-parent-switchprimarygroup-group)

<a id="meta-commands"></a>
### 元数据命令
用于查看或修改指定用户或权限组的元数据的命令。

命令格式为 `/lp user <user> meta ...` 或 `/lp group <group> meta ...`
*  [`info`](meta-commands.md#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-set-key-value-context)
*  [`unset` \<key\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-unset-key-value-context)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-settemp-key-value-duration-temporary-modifier-context)
*  [`unsettemp` \<key\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-unsettemp-key-context)
*  [`addprefix` \<priority\> \<prefix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addprefix-priority-prefix-context)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addsuffix-priority-suffix-context)
*  [`setprefix` [priority] \<prefix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context)
*  [`setsuffix` [priority] \<suffix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-setsuffix-priority-suffix-context)
*  [`removeprefix` \<priority\> [prefix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removeprefix-priority-prefix-context)
*  [`removesuffix` \<priority\> [suffix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removesuffix-priority-suffix-context)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addtempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addtempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`settempprefix` [priority] \<prefix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-settempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`settempsuffix` [priority] \<suffix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-settempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`removetempprefix` \<priority\> [prefix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removetempprefix-priority-prefix-context)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removetempsuffix-priority-suffix-context)
*  [`clear` [context...]](meta-commands.md#lp-usergroup-usergroup-meta-clear-type-context)

<a id="track-commands"></a>
### 晋升路线命令
用于查看或修改指定晋升路线的命令。

命令格式为 `/lp track <track> ...`，其中 `<track>` 是要查询或修改的晋升路线名称。
*  [/lp track \<track\> `info`](track-commands.md#lp-track-track-info)
*  [/lp track \<track\> `editor`](track-commands.md#lp-track-track-editor)
*  [/lp track \<track\> `append` \<group\>](track-commands.md#lp-track-track-append-group)
*  [/lp track \<track\> `insert` \<group\> \<position\>](track-commands.md#lp-track-track-insert-group-position)
*  [/lp track \<track\> `remove` \<group\>](track-commands.md#lp-track-track-remove-group)
*  [/lp track \<track\> `clear`](track-commands.md#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](track-commands.md#lp-track-track-rename-new-name)
*  [/lp track \<track\> `clone` \<name of clone\>](track-commands.md#lp-track-track-clone-new-name)

<a id="log-commands"></a>
### 日志命令
用于查看操作日志的命令。
*  [/lp log `recent` [user] [page]](log-commands.md#lp-log-recent-user-page)
*  [/lp log `search` \<query\> [page]](log-commands.md#lp-log-search-query-page)
*  [/lp log `notify` [on|off]](log-commands.md#lp-log-notify-onoff)
*  [/lp log `userhistory` \<user\> [page]](log-commands.md#lp-log-userhistory-user-page)
*  [/lp log `grouphistory` \<group\> [page]](log-commands.md#lp-log-grouphistory-group-page)
*  [/lp log `trackhistory` \<track\> [page]](log-commands.md#lp-log-trackhistory-track-page)
