---
title: "权重"
source_url: https://luckperms.net/wiki/Weight
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

<a id="weights"></a>
# 权重
权重是 LuckPerms 运作方式中的重要组成部分，用于解决可能出现的冲突。

LuckPerms 有两套不同且相互独立的权重系统：一套是[**权限组权重**](weight.md#group-weights)，另一套是[**元数据权重**](weight.md#meta-weights)，用于前缀、后缀等。

在所有情况下，**权重数值越大，优先级越高**。 

* 设置权重时，建议在权限组之间留出较大的数值间隔，例如每次增加 100，而不是 1。这样，以后想插入权限组、前缀或后缀时，就无需重新设置所有权重。
* 权重可以是任意数值，甚至可以是负数！


<a id="group-weights"></a>
## 权限组权重
当用户拥有多个权限组，且各权限组的节点发生冲突时，权限组权重决定哪个权限组的节点优先。用一个例子最容易说明：

* 假设某位玩家同时属于 default 权限组和“admin”权限组。每个权限组中都只有一个权限节点，即 `essentials.fly`。
* 在 default 权限组中，`essentials.fly` 设为 `false`；在“admin”权限组中，`essentials.fly` 设为 `true`。如果没有设置权重，玩家最终采用哪个节点的结果就不稳定，也不明确，无法确切判断玩家是否能够飞行。
* 这时就需要用到 __权重__。在这个例子中，如果将 default 的权重设得高于“admin”，玩家就会**无法**飞行；如果将 admin 的权重设得高于 default，玩家就**能够**飞行。

同样，只要玩家拥有多个权限组，权重最高的权限组中的权限就会覆盖权重较低的权限组中与之冲突的权限。 

<a id="setting-group-weights"></a>
### 设置权限组权重
权限组权重有两种设置方式：使用[命令](group-commands.md#lp-group-group-setweight-weight)，或使用[网页编辑器](web-editor.md#luckperms-nodes)。

* 使用命令时，执行 /`lp group <group> setweight <weight>`。
* 使用网页编辑器时，为权限组添加 `weight.<weight>` 节点。


<a id="meta-weights"></a>
## 元数据权重

元数据权重与权限组权重非常相似，但用于前缀和后缀。与权限组权重的作用方式一样，当玩家继承了多个前缀或后缀时，显示的是权重最高的那一个。

<a id="setting-meta-weights"></a>
### 设置元数据权重
前缀或后缀的权重有两种设置方式：使用[命令](meta-commands.md)，或使用[网页编辑器](web-editor.md#luckperms-nodes)。

* 使用命令时，在向权限组或玩家添加或设置前缀、后缀时指定权重即可：`/lp user/group <user|group> meta setprefix/addprefix <weight> <prefix>`。
* 使用网页编辑器时，添加或修改 `prefix.<weight>.<prefix>` 节点即可更改权重。后缀也遵循相同原理。
