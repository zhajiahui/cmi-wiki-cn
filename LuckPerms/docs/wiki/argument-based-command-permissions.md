---
title: "基于参数的命令权限"
source_url: https://luckperms.net/wiki/Argument-based-command-permissions
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

本页介绍 [`argument-based-command-permissions`](configuration.md#argument-based-command-permissions) 配置选项。

**要使以下任何权限生效，必须先在 [config.yml](configuration.md#argument-based-command-permissions) 中启用 [`argument-based-command-permissions: true`](configuration.md#argument-based-command-permissions)**！

启用此选项后，当玩家尝试修改或查看权限数据时，LuckPerms 会执行额外的权限检查。

这些权限可以更细致地控制玩家能做哪些修改，例如阻止玩家授予特定权限组，或阻止他们在某些上下文中进行修改。

这些额外检查可以分为 3 部分。

<a id="contents"></a>
### 目录

* [**玩家修改或查看自己及其他用户时的检查**](argument-based-command-permissions.md#checks-when-a-player-modifiesviews-themselves-or-other-users)
    * [修改自己](argument-based-command-permissions.md#modify-self)
    * [修改其他玩家](argument-based-command-permissions.md#modify-another-player)
    * [查看自己](argument-based-command-permissions.md#view-self)
    * [查看其他玩家](argument-based-command-permissions.md#view-another-player)
* [**玩家修改或查看权限组时的检查**](argument-based-command-permissions.md#checks-when-a-player-modifiesviews-a-group)
    * [修改权限组](argument-based-command-permissions.md#modify-a-group)
    * [查看权限组](argument-based-command-permissions.md#view-a-group)
* [**玩家在特定上下文中进行修改时的检查**](argument-based-command-permissions.md#checks-when-a-player-makes-changes-in-a-specific-context)
    * [在全局上下文中修改](argument-based-command-permissions.md#change-in-the-global-context)
    * [在一组特定上下文中修改](argument-based-command-permissions.md#change-in-a-specific-set-of-contexts)
* [**玩家使用一组特定参数进行修改时的检查**](argument-based-command-permissions.md#checks-when-a-player-makes-changes-with-a-set-of-specific-arguments)

<a id="checks-when-a-player-modifiesviews-themselves-or-other-users"></a>
## 玩家修改或查看自己及其他用户时的检查

<a id="modify-self"></a>
### 修改自己

当玩家尝试用命令修改自己的数据时，LuckPerms 会先检查 `[base command permission].modify.self`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.modify.user.self`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example"></a>
#### 示例
例如，执行 `/lp user Luck clear` 时，LuckPerms 会依次检查以下权限。

* `luckperms.user.clear`
* `luckperms.user.clear.modify.self`（如果这项检查返回 true，就不再检查下一项权限）
* `luckperms.modify.user.self`

只要任意一项检查返回 false，就不允许该操作。

<a id="modify-another-player"></a>
### 修改其他玩家

当玩家尝试用命令修改其他用户的数据时，LuckPerms 会先检查 `[base command permission].modify.others`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.modify.user.others`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-1"></a>
#### 示例
例如，执行 `/lp user Notch clear` 时，LuckPerms 会依次检查以下权限。

* `luckperms.user.clear`
* `luckperms.user.clear.modify.others`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.modify.user.others`

只要任意一项检查返回 false，就不允许该操作。

<a id="view-self"></a>
### 查看自己

当玩家尝试用命令查看自己的数据时，LuckPerms 会先检查 `[base command permission].view.self`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.view.user.self`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-2"></a>
#### 示例
例如，执行 `/lp user Luck permission info` 时，LuckPerms 会依次检查以下权限。

* `luckperms.user.permission.info`
* `luckperms.user.permission.info.view.self`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.view.user.self`

只要任意一项检查返回 false，就不允许该操作。

<a id="view-another-player"></a>
### 查看其他玩家

当玩家尝试用命令查看其他用户的数据时，LuckPerms 会先检查 `[base command permission].view.others`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.view.user.others`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-3"></a>
#### 示例
例如，执行 `/lp user Notch permission info` 时，LuckPerms 会依次检查以下权限。

* `luckperms.user.permission.info`
* `luckperms.user.permission.info.view.others`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.view.user.others`

只要任意一项检查返回 false，就不允许该操作。

<a id="checks-when-a-player-modifiesviews-a-group"></a>
## 玩家修改或查看权限组时的检查

<a id="modify-a-group"></a>
### 修改权限组

当玩家尝试用命令修改权限组时，LuckPerms 会先检查 `[base command permission].modify.[group name]`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.modify.group.[group name]`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-4"></a>
#### 示例
例如，执行 `/lp group admin clear` 时，LuckPerms 会依次检查以下权限。

* `luckperms.group.clear`
* `luckperms.group.clear.modify.admin`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.modify.group.admin`

只要任意一项检查返回 false，就不允许该操作。

<a id="view-a-group"></a>
### 查看权限组

当玩家尝试用命令查看权限组的数据时，LuckPerms 会先检查 `[base command permission].view.[group name]`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.view.group.[group name]`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-5"></a>
#### 示例
例如，执行 `/lp group admin permission info` 时，LuckPerms 会依次检查以下权限。

* `luckperms.group.permission.info`
* `luckperms.group.permission.info.view.admin`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.view.group.admin`

只要任意一项检查返回 false，就不允许该操作。

<a id="checks-when-a-player-makes-changes-in-a-specific-context"></a>
## 玩家在特定上下文中进行修改时的检查

当玩家尝试用命令修改带有上下文的数据（即可以应用于特定服务器、世界或上下文的数据）时，LuckPerms 会检查额外权限。

<a id="change-in-the-global-context"></a>
### 在全局上下文中修改
如果修改发生在全局上下文中，LuckPerms 会先检查 `[base command permission].usecontext.global`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.usecontext.global`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-6"></a>
#### 示例
例如，执行 `/lp group admin permission set test.node true` 时，LuckPerms 会依次检查以下权限。

* `luckperms.group.permission.set`
* `luckperms.group.permission.set.usecontext.global`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.usecontext.global`

只要任意一项检查返回 false，就不允许该操作。

<a id="change-in-a-specific-set-of-contexts"></a>
### 在一组特定上下文中修改
如果修改不是在全局上下文中进行的，LuckPerms 会对所用的每个上下文执行以下检查。

首先检查 `[base command permission].usecontext.[context key].[context value]`。如果结果为 true，就允许该操作；如果结果为 false，就不允许该操作。

如果玩家没有为这项检查设置权限值（也就是说，结果未定义），LuckPerms 就会接着检查 `luckperms.usecontext.[context key].[context value]`，以此确定结果。如果两项检查都没有返回 true，就不允许该操作。

<a id="example-7"></a>
#### 示例
例如，执行 `/lp group admin permission set test.node true server=factions world=nether` 时，LuckPerms 会依次检查以下权限。

* `luckperms.group.permission.set`
* `luckperms.group.permission.set.usecontext.server.factions`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.usecontext.server.factions`
* `luckperms.group.permission.set.usecontext.world.nether`（如果这项检查返回 true/false，就不再检查下一项权限）
* `luckperms.usecontext.world.nether`

只要任意一项检查返回 false，就不允许该操作。

<a id="checks-when-a-player-makes-changes-with-a-set-of-specific-arguments"></a>
## 玩家使用一组特定参数进行修改时的检查

部分命令会执行这些检查，具体取决于传给命令的参数。

例如，`parent add` 命令会根据要添加的父级检查一项额外权限。

执行 `/lp user Luck parent add admin` 时，除其他权限检查外，LuckPerms 还会检查 `luckperms.user.parent.add.admin`。这样就可以允许玩家使用某条命令，但将其限制为只能使用特定参数。

下表列出了会被检查的参数。

| 命令              | 额外检查的参数        |
|-------------------|-----------------------|
| permission set    | node                  |
| permission unset  | node                  |
| parent add        | group                 |
| parent set        | group                 |
| parent settrack   | group.track           |
| parent remove     | group                 |
| parent cleartrack | track                 |
| meta set          | key                   |
| meta unset        | key                   |
| promote           | track.next-group      |
| demote            | track.old-group       |

<a id="promote-other-players-but-not-to-or-past-their-own-level-on-a-track"></a>
## 允许晋升其他玩家，但不得达到或超过自己在晋升路线上的等级

这是一个很常见的问题，设置起来也很简单。只需添加以下权限：


<a id="for-sponge-and-spigot"></a>
### 适用于 Sponge 和 Spigot：

| 权限                                                                              | 值                    |
|-----------------------------------------------------------------------------------|-----------------------|
| `luckperms.user.promote`                                                          | true                  |
| `luckperms.user.promote.*` <--- 仅 Sponge 需要这一项                               | false                 |
| `luckperms.user.promote.modify.others `                                           | true                  |
| `luckperms.user.promote.<track>.*`                                                | true                  |
| `luckperms.user.promote.<track>.<{all,groups,they,cannot,promote,to,or,past}>`    | false                 |

最后一个节点要包含这条晋升路线中玩家无权晋升到、也无权晋升越过的所有权限组。各权限组之间用 `,` 分隔，并全部放在 {} 内。例如，可以设置 `luckperms.user.promote.staff.{admin,owner}`，阻止玩家在 staff 晋升路线中将他人晋升到 admin 或更高等级。

此外，如果希望权限组或用户可以使用全局上下文执行晋升（不要求满足特定的上下文条件），还需要添加 `luckperms.usecontext.global` 节点。 
