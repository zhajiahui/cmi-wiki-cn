---
title: 权限组命令
source_url: https://luckperms.net/wiki/Group-Commands
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
*  [/lp group \<group\> `info`](group-commands.md#lp-group-group-info)
*  [/lp group \<group\> `permission`](permission-commands.md)
*  [/lp group \<group\> `parent`](parent-commands.md)
*  [/lp group \<group\> `meta`](meta-commands.md)
*  [/lp group \<group\> `editor`](group-commands.md#lp-group-group-editor)
*  [/lp group \<group\> `listmembers` [page]](group-commands.md#lp-group-group-listmembers-page)
*  [/lp group \<group\> `setweight` \<weight\>](group-commands.md#lp-group-group-setweight-weight)
*  [/lp group \<group\> `setdisplayname` \<name\> [context...]](group-commands.md#lp-group-group-setdisplayname-name)
*  [/lp group \<group\> `showtracks`](group-commands.md#lp-group-group-showtracks)
*  [/lp group \<group\> `clear` [context...]](group-commands.md#lp-group-group-clear-context)
*  [/lp group \<group\> `rename` \<new name\>](group-commands.md#lp-group-group-rename-new-name)
*  [/lp group \<group\> `clone` \<name of clone\>](group-commands.md#lp-group-group-clone-new-name)

___
<a id="lp-group-group-info"></a>
#### `/lp group <group> info`  
**权限**： luckperms.group.info  
显示权限组的信息。

___
<a id="lp-group-group-editor"></a>
#### `/lp group <group> editor`  
**权限**： luckperms.group.editor  
打开网页界面，编辑指定权限组的权限。保存修改后，会提供一条命令；执行该命令后，修改才会生效。

___
<a id="lp-group-group-listmembers-page"></a>
#### `/lp group <group> listmembers [page]`  
**权限**： luckperms.group.listmembers  
**参数**：  
* `[page]` - 要查看的页码

列出直接继承此权限组的其他用户和权限组。

___
<a id="lp-group-group-setweight-weight"></a>
#### `/lp group <group> setweight <weight>`  
**权限**： luckperms.group.setweight  
**参数**：  
* `<weight>` - 要设置的权重

设置权限组的权重值，决定汇总用户权限时考虑各权限组的先后顺序。数值越大，权重越高。

___
<a id="lp-group-group-setdisplayname-name"></a>
#### `/lp group <group> setdisplayname <name>`  
**权限**： luckperms.group.setdisplayname  
**参数**：  
* `<name>` - 要设置的名称
* `[context...]` - 设置显示名称时使用的[上下文](context.md)

设置权限组的显示名称。它实际上可以作为该权限组的“别名”。

___
<a id="lp-group-group-showtracks"></a>
#### `/lp group <group> showtracks`  
**权限**： luckperms.group.showtracks  
列出权限组当前所在的所有晋升路线。

___
<a id="lp-group-group-clear-context"></a>
#### `/lp group <group> clear [context]`  
**权限**： luckperms.group.clear  
**参数**：  
* `[context...]` - 用于筛选的[上下文](context.md)

清除权限组的权限、父权限组和元数据。

___
<a id="lp-group-group-rename-new-name"></a>
#### `/lp group <group> rename <new name>`  
**权限**： luckperms.group.rename  
**参数**：  
* `<new name>` - 权限组的新名称

修改权限组名称。注意，此权限组成员的继承记录不会随之更新，仍会指向旧权限组名称。要更新这些记录，需要使用批量修改功能修改现有条目。

___
<a id="lp-group-group-clone-new-name"></a>
#### `/lp group <group> clone <new name>`  
**权限**： luckperms.group.clone  
**参数**：  
* `<new name>` - 副本的名称

创建该权限组的完整副本，并使用不同的名称。

___