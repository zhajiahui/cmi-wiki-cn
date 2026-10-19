---
title: 父级命令
source_url: https://luckperms.net/wiki/Parent-Commands
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
*  [`info`](parent-commands.md#lp-usergroup-usergroup-parent-info-page-sorting-mode)
*  [`set` \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-set-group-context)
*  [`add` \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-add-group-context)
*  [`remove` \<group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-remove-group-context)
*  [`settrack` \<track\> \<index | group\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-settrack-track-indexgroup-context)
*  [`addtemp` \<group\> \<duration\> [temporary modifier] [context...]](parent-commands.md#lp-usergroup-usergroup-parent-addtemp-group-duration-temporary-modifier-context)
*  [`removetemp` \<group\> [duration] [context...]](parent-commands.md#lp-usergroup-usergroup-parent-removetemp-group-duration-context)
*  [`clear` [context...]](parent-commands.md#lp-usergroup-usergroup-parent-clear-context)
*  [`cleartrack` \<track\> [context...]](parent-commands.md#lp-usergroup-usergroup-parent-cleartrack-track-context)
*  [`switchprimarygroup` \<group\>](parent-commands.md#lp-user-user-parent-switchprimarygroup-group)

___
<a id="lp-usergroup-usergroup-parent-info-page-sorting-mode"></a>
#### `/lp user/group <user|group> parent info [page] [sorting mode]`  
**权限**： luckperms.user.parent.info 或 luckperms.group.parent.info  
**参数**：  
* `[page]` - 要查看的页码
* `[sorting mode]` - 结果的排序方式
  

列出用户或权限组的父权限组（它们继承的权限组）。

"sorting mode" 参数用于指定列表的排序方式，共有 4 个选项。

| 排序模式 | 说明 |
|--------------------------|--------------------------------------------------------------------------|
| `priority`               | 按平台的继承规则对列表排序 |
| `!priority`/`reverse`    | 按优先级排序后反转列表 |
| `abc`/`alphabetically`   | 按字母顺序排序（A - Z） |
| `!abc`/`!alphabetically` | 按字母顺序排序后反转列表（Z - A） |

___
<a id="lp-usergroup-usergroup-parent-set-group-context"></a>
#### `/lp user/group <user|group> parent set <group> [context...]`  
**权限**： luckperms.user.parent.set 或 luckperms.group.parent.set  
**参数**：  
* `<group>` - 要设置的权限组
* `[context...]` - 设置权限组时使用的[上下文](context.md)

设置用户或权限组的父级。与 "parent add" 命令不同，此命令会清除给定上下文中已设置的所有权限组。add 命令则只是在用户或权限组已有的权限组基础上再“添加”一个。如果执行此命令时没有提供上下文参数，还会更新用户的主权限组。

___
<a id="lp-usergroup-usergroup-parent-add-group-context"></a>
#### `/lp user/group <user|group> parent add <group> [context...]`  
**权限**： luckperms.user.parent.add 或 luckperms.group.parent.add  
**参数**：  
* `<group>` - 要添加的权限组
* `[context...]` - 添加权限组时使用的[上下文](context.md)

为用户或权限组添加父级。与 "parent set" 命令不同，此命令只会在用户或权限组现有的父级基础上添加指定父级，不会移除用户已有的任何父级，也不会影响用户的主权限组。

___
<a id="lp-usergroup-usergroup-parent-remove-group-context"></a>
#### `/lp user/group <user|group> parent remove <group> [context...]`  
**权限**： luckperms.user.parent.remove 或 luckperms.group.parent.remove  
**参数**：  
* `<group>` - 要移除的权限组
* `[context...]` - 移除权限组时使用的[上下文](context.md)

移除用户或权限组的一个父级。  
如果移除的权限组是用户的主权限组，主权限组将重置为 default。

___
<a id="lp-usergroup-usergroup-parent-settrack-track-indexgroup-context"></a>
#### `/lp user/group <user|group> parent settrack <track> <index|group> [context...]`  
**权限**： luckperms.user.parent.settrack 或 luckperms.group.parent.settrack  
**参数**：  
* `<track>` - 要在其中设置位置的晋升路线
* `<index|group>` - 要设置为的权限组，或该权限组在指定晋升路线中的位置索引
* `[context...]` - 设置权限组时使用的[上下文](context.md)

设置用户或权限组在指定晋升路线上的位置。此命令的行为与 set 命令相同，但只会清除指定晋升路线中已有的权限组，其他父权限组不受影响。
___
<a id="lp-usergroup-usergroup-parent-addtemp-group-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> parent addtemp <group> <duration> [temporary modifier] [context...]`  
**权限**： luckperms.user.parent.addtemp 或 luckperms.group.parent.addtemp  
**参数**：  
* `<group>` - 要添加的权限组
* `<duration>` - 权限组成员资格到期前的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 添加权限组时使用的[上下文](context.md)

为用户或权限组添加临时父级。时长可以填写一段时间，也可以填写权限到期时的 Unix 时间戳。例如，"1mo3d13h45m" 表示权限在 1 个月 3 天 13 小时 45 分钟后到期，而 "1482694200" 表示权限在 2016 年 12 月 25 日晚上 7:30 到期。  

"temporary modifier" 参数用于指定权限时长的累加方式，共有 3 个选项。

| 修饰符键 | 说明 |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的时长加到新时长上 |
| `replace`    | 保留最长的时长，舍弃其他节点 |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接执行失败 |

___
<a id="lp-usergroup-usergroup-parent-removetemp-group-duration-context"></a>
#### `/lp user/group <user|group> parent removetemp <group> [duration] [context...]`  
**权限**： luckperms.user.parent.removetemp 或 luckperms.group.parent.removetemp  
**参数**：  
* `<group>` - 要移除的权限组
* `[duration]` - 要从临时权限组成员资格中扣除的时长；省略此参数可将其完全移除
* `[context...]` - 移除权限组时使用的[上下文](context.md)

移除用户或权限组的一个临时父级。

___
<a id="lp-usergroup-usergroup-parent-clear-context"></a>
#### `/lp user/group <user|group> parent clear [context...]`  
**权限**： luckperms.user.parent.clear 或 luckperms.group.parent.clear  
**参数**：  
* `[context...]` - 用于筛选的[上下文](context.md)

移除用户或权限组的所有父级。  
这会将其重新加入 `default` 权限组。

___
<a id="lp-usergroup-usergroup-parent-cleartrack-track-context"></a>
#### `/lp user/group <user|group> parent cleartrack <track> [context...]`  
**权限**： luckperms.user.parent.cleartrack 或 luckperms.group.parent.cleartrack  
**参数**：  
* `<track>` - 要在其中移除父级的晋升路线
* `[context...]` - 用于筛选的[上下文](context.md)

移除用户或权限组在指定晋升路线上的所有父级。

___
<a id="lp-user-user-parent-switchprimarygroup-group"></a>
#### `/lp user <user> parent switchprimarygroup <group>`  
**权限**： luckperms.user.parent.switchprimarygroup  
**参数**：  
* `<group>` - 要切换到的权限组

此命令仅适用于用户，因为权限组没有“主权限组”。

此命令用于修改用户的主权限组。如果用户尚未加入指定权限组，就会将其加入。此命令不应替代 "parent set" 命令使用。用户原有的主权限组不会从其父级中移除。（一个用户可以拥有多个父权限组）

如果 LuckPerms 配置中的 `primary-group-calculation` 不是 "stored"，应使用 [`parent add`](parent-commands.md#lp-usergroup-usergroup-parent-add-group-context) 或 [`parent set`](parent-commands.md#lp-usergroup-usergroup-parent-set-group-context) 命令，而不是此命令。

___

