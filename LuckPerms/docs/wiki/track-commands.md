---
title: "晋升路线命令"
source_url: https://luckperms.net/wiki/Track-Commands
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

本页是**命令用法**主页的子页面。[点击此处返回。](command-usage.md)

请记住主页中的几个要点：

* 在 BungeeCord 上运行插件时，使用 `/lpb` 而不是 `/lp`
* 在 Velocity 上运行插件时，使用 `/lpv` 而不是 `/lp`
* 必填参数用尖括号表示，例如 `<required>`
* 可选参数用方括号表示，例如 `[optional]`
* 如果参数中需要包含空格，必须用引号将参数括起来，例如 `"  "`

___

<a id="index"></a>
### 目录
*  [/lp track \<track\> `info`](track-commands.md#lp-track-track-info)
*  [/lp track \<track\> `editor`](track-commands.md#lp-track-track-editor)
*  [/lp track \<track\> `append` \<group\>](track-commands.md#lp-track-track-append-group)
*  [/lp track \<track\> `insert` \<group\> \<position\>](track-commands.md#lp-track-track-insert-group-position)
*  [/lp track \<track\> `remove` \<group\>](track-commands.md#lp-track-track-remove-group)
*  [/lp track \<track\> `clear`](track-commands.md#lp-track-track-clear)
*  [/lp track \<track\> `rename` \<new name\>](track-commands.md#lp-track-track-rename-new-name)
*  [/lp track \<track\> `clone` \<name of clone\>](track-commands.md#lp-track-track-clone-new-name)

___
<a id="lp-track-track-info"></a>
#### `/lp track <track> info`  
**权限**：luckperms.track.info  
显示晋升路线中的权限组。

___
<a id="lp-track-track-editor"></a>
#### `/lp track <track> editor`  

**权限**：luckperms.track.editor  
打开网页界面，编辑指定晋升路线的权限。保存修改后，会提供一条命令，执行该命令后修改才会生效。

___

<a id="lp-track-track-append-group"></a>
#### `/lp track <track> append <group>`  

**权限**：luckperms.track.append  
**参数**：  
* `<group>` - 要添加的权限组

将权限组添加到晋升路线末尾。

___
<a id="lp-track-track-insert-group-position"></a>
#### `/lp track <track> insert <group> <position>`  
**权限**：luckperms.track.insert  
**参数**：  
* `<group>` - 要插入的权限组
* `<position>` - 插入权限组的位置

将权限组插入此晋升路线的指定位置。位置为 1 时，会将其放在晋升路线开头。

___
<a id="lp-track-track-remove-group"></a>
#### `/lp track <track> remove <group>`  
**权限**：luckperms.track.remove  
**参数**：  
* `<group>` - 要移除的权限组

从晋升路线中移除一个权限组。

___
<a id="lp-track-track-clear"></a>
#### `/lp track <track> clear`  
**权限**：luckperms.track.clear  
移除晋升路线中的所有权限组。

___
<a id="lp-track-track-rename-new-name"></a>
#### `/lp track <track> rename <new name>`  
**权限**：luckperms.track.rename  
**参数**：  
* `<new name>` - 晋升路线的新名称

更改晋升路线的名称。

___
<a id="lp-track-track-clone-new-name"></a>
#### `/lp track <track> clone <new name>`  
**权限**：luckperms.track.clone  
**参数**：  
* `<new name>` - 副本的名称

以不同的名称创建此晋升路线的完整副本。

___