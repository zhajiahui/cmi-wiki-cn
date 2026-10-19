---
title: 批量编辑
source_url: https://luckperms.net/wiki/Bulk-Editing
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 提供了一条命令，便于批量修改权限。请谨慎使用；用法不当很容易破坏或损坏现有配置。

使用前，最好先备份权限数据。可以复制数据库或文件，也可以使用 export 命令。

这条命令的设计基本上是精简版的 SQL 语法。因此，传入命令的数据可以直接转换为 SQL 查询，也可以用于修改 YAML 或 JSON 存储文件中的数据。熟悉 SQL 的用户可能会觉得，直接在数据库服务器中编写查询比使用此命令更方便。

这些命令**只能从控制台使用**，因为它们可能对服务器数据造成严重破坏。执行操作前，系统会要求输入确认码，防止用户通过 "sudo" 控制台的方式获得使用这些命令的机会。

命令用法如下……

<a id="lp-bulkupdate-data-type-action-action-field-action-value-constraint"></a>
## `/lp bulkupdate <data type> <action> [action field] [action value] [constraint...]`

乍看之下可能有些复杂，下面逐项说明……

| 参数 | 说明 |
|----------|-------------|
| `data type` | 要更改的数据类型。（可以是 "all"、"users" 或 "groups"） |
| `action` | 要对数据执行的操作。（可以是 "update" 或 "delete"） |
| `action field` | 操作的目标字段。仅 update 操作需要。（可以是 "permission"、"server" 或 "world"） |
| `action value` | 用于替换的新值。仅 update 操作需要 |
| `constraint` | 本次更新需要满足的约束条件 |

`data type` 很简单，只是告诉 LuckPerms 本次更新应影响哪些数据：仅用户、仅权限组，或用户和权限组两者。

`action` 决定对数据做什么，可以是 "update" 或 "delete"。Delete 表示删除所有符合约束条件的记录；Update 则将符合条件的值替换为另一个值。

`action field` 和 `action value` 参数是可选的，因为它们只适用于 "update" 操作。前者指定要更新的字段，后者指定该字段的新值。

`constraints` 参数用于限定更新范围。只有符合约束条件的权限或条目才会受影响。

<a id="constraints"></a>
### 约束条件
约束条件分为 3 部分：`field`、`comparison` 和 `value`。

可用的 `fields` 是 `permission`、`server` 和 `world`。Permission 就是文件中存储的权限节点（请记住，在底层，所有内容都存储为权限，连权限组成员关系和前缀也是如此）。server 和 world 字段表示权限生效的服务器或世界。如果权限没有指定其中某项的值，对应字段就会设为 "global"。

约束条件中的 `value` 部分，就是在所选比较方式下，期望该字段具有的值。

共有 4 种可用的比较方式。

| 比较符号 | 比较名称 | 说明 |
|-------------------|-----------------|-------------|
| `==`              | 等于        | 两个值相同。（忽略大小写） |
| `!=`              | 不等于      | 两个值不同。（忽略大小写） |
| `~~`              | 相似        | 两个值“相似”。使用 SQL 的 `LIKE` 语法。 |
| `!~`              | 不相似      | 两个值不“相似”。使用 SQL 的 `LIKE` 语法。 |

有关“相似”比较所用语法的更多信息，见[此处](https://www.w3schools.com/sql/sql_like.asp)和[此处](https://www.tutorialspoint.com/sql/sql-like-clause.htm)。

基本规则是：
* `%` - 百分号代表零个、一个或多个字符
* `_` - 下划线代表单个字符

<a id="some-examples"></a>
##### 示例
* `server ~~ hub_` 会匹配服务器值 "hub1"、"hub2"、"hub3" 等
* `permission !~ group.%` 会匹配任何不是权限组的权限
* `world == nether` 会匹配世界值恰好等于 "nether" 的条目

在命令中定义约束条件时，必须用 `" "` 引号包住整个约束条件。

如果想从带有特定世界或服务器上下文的权限或权限组中移除某个特定上下文，只需将世界和/或上下文设为 `global`。这实际上就会移除该上下文，让权限和/或权限组重新在全局生效。

<a id="command-examples"></a>
### 命令示例
<a id="lp-bulkupdate-all-update-permission-groupmod-permission--groupmoderator"></a>
#### `/lp bulkupdate all update permission group.mod "permission == group.moderator"`
更新所有条目，将出现的 "group.moderator" 权限全部替换为 "group.mod"。（实际上相当于重命名权限组。）

<a id="lp-bulkupdate-users-delete-server--hub-world--nether"></a>
#### `/lp bulkupdate users delete "server ~~ hub%" "world == nether"`
删除分配给用户的权限中，服务器名称以 "hub" 开头、且世界等于 "nether" 的所有权限。

<a id="lp-bulkupdate-all-delete-permission--essentialsfly"></a>
#### `/lp bulkupdate all delete "permission == essentials.fly"`
删除权限等于 "essentials.fly" 的所有权限条目。

<a id="lp-bulkupdate-all-delete-permission--groupvip"></a>
#### `/lp bulkupdate all delete "permission == group.vip"`
删除所有 VIP 权限组成员关系。

<a id="lp-bulkupdate-all-update-server-global-server--factions"></a>
#### `/lp bulkupdate all update server global "server == factions"`
将所有值为 "factions" 的服务器条目改为 "global"。

<a id="lp-bulkupdate-all-update-permission-essentialsban-permission--essentialsmute-server--survival"></a>
#### `/lp bulkupdate all update permission essentials.ban "permission == essentials.mute" "server == survival"`
将 "survival" 服务器上设置的所有 "essentials.mute" 权限条目改为 "essentials.ban"。

<a id="lp-bulkupdate-all-update-server-global-permission--groupmod-server--survival"></a>
#### `/lp bulkupdate all update server global "permission == group.mod" "server == survival"`
将所有 MOD 权限组成员关系改为使用全局上下文（实际上就是移除上下文）。
