---
title: 高级权限设置
source_url: https://luckperms.net/wiki/Advanced-Setup
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

<a id="intro"></a>
## 简介
LuckPerms 的基础用法相当简单，同时也提供了多种功能和内部规则，可用来建立高级权限系统。

<a id="server-and-world-specific-permissions"></a>
## 仅在指定服务器和世界生效的权限
LuckPerms 专为多服务器网络设计，可以定义仅在指定服务器和指定世界中生效的权限。

<a id="some-important-config-options"></a>
#### 一些重要的配置选项：
```yml
# The name of the server, used for server specific permissions. Set to 'global' to disable.
server: global
```
这是服务器的名称。如果想设置仅在指定服务器生效的权限，需要修改此选项，为服务器命名。同一网络中的服务器也可以使用相同名称。

```yml
# If users on this server should have their global permissions/groups applied.
include-global: true
```
include global 选项同样重要。

LuckPerms 中的权限分为服务器专属权限（仅在指定服务器上生效）和全局权限（在所有服务器上生效）。

将上述选项设为 **false** 后，只有为该服务器明确设置的权限才会生效。全局权限（即不限定服务器的权限）不会生效。

通过调整这两个选项，可以灵活配置各服务器独立的权限和权限组。

<a id="examples"></a>
### 示例
<a id="example-1"></a>
#### 示例 1
```yml
server: global
include-global: true
```
* /luckperms user Luck set minecraft.command.gamemode true **会生效**
* /luckperms user Luck set minecraft.command.gamemode true factions 在不名为 "factions" 的服务器上**不会生效**

<a id="example-2"></a>
#### 示例 2
```yml
server: lobby
include-global: true
```
* /luckperms user Luck set minecraft.command.gamemode true **会生效**
* /luckperms user Luck set minecraft.command.gamemode true lobby **会生效**

<a id="example-3"></a>
#### 示例 3
```yml
server: bungeecord
include-global: false
```
* /luckperms user Luck set minecraft.command.gamemode true **不会生效**
* /luckperms user Luck set bungeecord.command.alert true bungeecord **会生效**

<a id="example-4"></a>
#### 示例 4
```yml
server: global
include-global: false
```
**任何权限都不会生效**

如果没有定义服务器，同时又不包含全局权限，就不会有任何权限生效。

<a id="permission-calculation"></a>
## 权限计算
<a id="permissions-are-calculated-based-on-a-priority-system-as-follows"></a>
### 权限按以下优先级规则计算。

* **服务器专属权限会覆盖通用权限或全局权限。**

例如：用户拥有一个全局的 "fly.use" 权限，同时又在 "factions" 服务器上拥有一个被否定的 "fly.use" 权限。服务器专属权限会覆盖全局权限，因此用户会得到否定节点的结果（前提是用户位于该服务器上）。

* **世界专属权限会覆盖通用权限。**

例如：用户拥有一个全局的 "fly.use" 权限，同时又在 "world_nether" 世界中拥有一个被否定的 "fly.use" 权限。世界专属权限会覆盖全局权限，因此用户会得到否定节点的结果（当然，前提是用户位于该世界中）。

* **临时权限会覆盖非临时权限。**

例如：用户的 "test.node" 权限被设为 false，同时又拥有一个值为 true 的临时 "test.node" 权限。临时权限会覆盖永久权限，因此在该临时权限指定的有效期内，用户会得到值为 true 的节点。

* **普通权限会覆盖通配符或正则表达式权限**

例如：用户的 "luckperms.\*" 权限被设为 true，而 "luckperms.something" 权限被设为 false。非通配符权限会覆盖通配符权限，因此即使存在通配符，"luckperms.something" 仍会被设为 false。

* **临时权限会覆盖到期时间更晚的其他临时权限**

例如：用户拥有一个值为 true、1 天后到期的临时 "fly.use" 权限，同时又拥有一个值为 false、1 小时后到期的临时 "fly.use" 权限。1 小时后到期的权限会覆盖 1 天后到期的权限，因此在这 1 小时内，否定节点会优先生效。

* **更具体的通配符会覆盖更宽泛的通配符**

例如：用户的 "luckperms.\*" 被设为 true，但 "luckperms.user.\*" 被设为 false。那么，即使存在更宽泛的 "luckperms.*" 通配符，所有用户相关的权限仍会被设为 false。

* **对象自身的权限会覆盖继承的权限。**

例如：用户属于 default 权限组，该组授予了 "some.thing.perm" 权限，但用户自身的 "some.thing.perm" 权限被设为 false。用户自身的权限会覆盖继承的权限，因此用户会得到否定节点的结果。

<a id="temporary-permissions"></a>
## 临时权限
临时权限每 3 秒检查一次，以确认是否已经到期。无论同步间隔如何设置，都会进行此项检查。因此，你可以将临时权限设置为几秒后到期，它们会按时被移除。

<a id="shorthand-permissions"></a>
## 简写权限
LuckPerms 有自己的权限简写系统（不过与 PermissionsEx 相当相似 :P），允许以简写格式设置权限。

<a id="examples-1"></a>
### 示例
<a id="example-1-1"></a>
#### 示例 1
以 LuckPerms 的权限节点为例，假设你想允许用户为权限组和用户设置、取消设置权限。

不使用简写时，需要添加 4 个节点。
```
luckperms.user.setpermission
luckperms.user.unsetpermission
luckperms.group.setpermission
luckperms.group.unsetpermission
```
使用简写后，只需添加以下节点：

`luckperms.{user,group}.{setpermission,unsetpermission}`

用花括号将节点的一部分定义为简写组，再用逗号 `,` 分隔各项。

<a id="example-2-1"></a>
#### 示例 2
可以使用 `-` 字符定义字符范围。
不使用简写时，需要添加 4 个节点。
```
coolkits.kit.a
coolkits.kit.b
coolkits.kit.c
coolkits.kit.d
```
使用简写后，只需添加以下节点：

`coolkits.kit.{a-d}`

<a id="example-3-1"></a>
#### 示例 3
可以使用 `-` 字符定义数字范围。
不使用简写时，需要添加 4 个节点。
```
prisonmines.teleport.1
prisonmines.teleport.2
prisonmines.teleport.3
prisonmines.teleport.4
```
使用简写后，只需添加以下节点：

`prisonmines.teleport.{1-4}`

<a id="regex"></a>
## 正则表达式
LuckPerms 支持使用正则表达式定义权限节点。

使用正则表达式时，**必须**加上 "R=" 前缀，让 LuckPerms 将其视为正则表达式，而不是普通字符串。

例如，如果想让用户能够同时创建权限组和晋升路线，通常需要添加两个权限节点。但使用正则表达式时，只需添加一个：`luckperms\.create.*`。由于整个节点都会被解析，请记得转义所有需要转义的字符（包括点号）。
