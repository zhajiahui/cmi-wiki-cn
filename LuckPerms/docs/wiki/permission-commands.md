---
title: "权限命令"
source_url: https://luckperms.net/wiki/Permission-Commands
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
*  [`info`](permission-commands.md#lp-usergroup-usergroup-permission-info-page-sorting-mode)
*  [`set` \<node\> \<true/false\> [context...]](permission-commands.md#lp-usergroup-usergroup-permission-set-node-truefalse-context)
*  [`unset` \<node\> [context...]](permission-commands.md#lp-usergroup-usergroup-permission-unset-node-context)
*  [`settemp` \<node\> \<true/false\> \<duration\> [temporary modifier] [context...]](permission-commands.md#lp-usergroup-usergroup-permission-settemp-node-truefalse-duration-temporary-modifier-context)
*  [`unsettemp` \<node\> [duration] [context...]](permission-commands.md#lp-usergroup-usergroup-permission-unsettemp-node-duration-context)
*  [`check` \<node\>](permission-commands.md#lp-usergroup-usergroup-permission-check-node)
*  [`clear` [context...]](permission-commands.md#lp-usergroup-usergroup-permission-clear-context)

___
<a id="lp-usergroup-usergroup-permission-info-page-sorting-mode"></a>
#### `/lp user/group <user|group> permission info [page] [sorting mode]`  
**权限**：luckperms.user.permission.info 或 luckperms.group.permission.info  
**参数**：  
* `[page]` - 要查看的页码
* `[sorting mode]` - 结果的排序方式

列出用户或权限组拥有的权限节点。

“sorting mode”参数用于指定列表的排序方式，共有 4 个选项可选。

| 排序方式                 | 说明                                                                     |
|--------------------------|--------------------------------------------------------------------------|
| `priority`               | 按照所在平台的继承规则对结果排序                                        |
| `!priority`/`reverse`    | 先按优先级排序，再反转列表                                              |
| `abc`/`alphabetically`   | 按字母顺序（A - Z）对列表排序                                           |
| `!abc`/`!alphabetically` | 先按字母顺序排序，再反转列表（Z - A）                                   |

___
<a id="lp-usergroup-usergroup-permission-set-node-truefalse-context"></a>
#### `/lp user/group <user|group> permission set <node> [true|false] [context...]`  
**权限**：luckperms.user.permission.set 或 luckperms.group.permission.set  
**参数**：  
* `<node>` - 要设置的权限节点
* `[true|false]` - 要为权限设置的值（默认为 `true`）
* `[context...]` - 设置权限所用的[上下文](context.md)

为用户或权限组设置（或授予）权限。设为“true”会授予该权限；设为“false”则会否定该权限。不添加任何上下文时，会在“global”上下文中设置该权限。

___
<a id="lp-usergroup-usergroup-permission-unset-node-context"></a>
#### `/lp user/group <user|group> permission unset <node> [context...]`  
**权限**：luckperms.user.permission.unset 或 luckperms.group.permission.unset  
**参数**：  
* `<node>` - 要取消设置的权限节点
* `[context...]` - 取消权限设置所用的[上下文](context.md)

取消设置（或移除）用户或权限组的一项权限。

___
<a id="lp-usergroup-usergroup-permission-settemp-node-truefalse-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> permission settemp <node> <true|false> <duration> [temporary modifier] [context...]`  
**权限**：luckperms.user.permission.settemp 或 luckperms.group.permission.settemp  
**参数**：  
* `<node>` - 要设置的权限节点
* `<true|false>` - 要为权限设置的值
* `<duration>` - 距权限到期的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 设置权限所用的[上下文](context.md)

为用户或权限组临时设置一项权限。设为“false”会否定该权限。时长可以是一段时间，也可以是权限到期时的 Unix 时间戳。例如，“1mo3d13h45m”会将权限设为在 1 个月 3 天 13 小时 45 分钟后到期，而“1482694200”则会将权限设为在 2016 年 12 月 25 日晚上 7:30 到期。

“temporary modifier”参数用于指定权限的累积方式，共有 3 个选项可选。

| 修饰符键     | 说明                                                                      |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的持续时间加到新的持续时间上                                    |
| `replace`    | 保留最长的持续时间，丢弃其他节点                                          |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接失败                                |

___
<a id="lp-usergroup-usergroup-permission-unsettemp-node-duration-context"></a>
#### `/lp user/group <user|group> permission unsettemp <node> [duration] [context...]`  
**权限**：luckperms.user.permission.unsettemp 或 luckperms.group.permission.unsettemp  
**参数**：  
* `<node>` - 要取消设置的权限节点
* `[duration]` - 要从临时权限中扣除的时长；省略此参数会将其完全移除
* `[context...]` - 取消权限设置所用的[上下文](context.md)

取消设置用户或权限组的一项临时权限。

___
<a id="lp-usergroup-usergroup-permission-check-node"></a>
#### `/lp user/group <user|group> permission check <node>`  
**权限**：luckperms.user.permission.check 或 luckperms.group.permission.check  
**参数**：  

* `<node>` - 要检查的权限节点

检查用户或权限组是否拥有某项权限，并提供有关哪些因素影响了检查结果的有用信息。

___
<a id="lp-usergroup-usergroup-permission-clear-context"></a>
#### `/lp user/group <user|group> permission clear [context...]`  
**权限**：luckperms.user.permission.clear 或 luckperms.group.permission.clear  
**参数**：  
* `[context...]` - 用于筛选的[上下文](context.md)

移除该用户或权限组的所有权限。

___
