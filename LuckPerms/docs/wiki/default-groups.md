---
title: 默认权限组
source_url: https://luckperms.net/wiki/Default-Groups
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 处理默认设置和默认权限组的方式，可能是整个插件最不受欢迎的功能。最近，我们一直在为插件添加额外功能或替代方案，让用户获得比其他权限插件更细致的控制能力；也希望大家最终会把这套处理方式当作插件中最喜欢的部分，而不是最不喜欢的部分。

<a id="where-to-start"></a>
# 从何说起
我们的思路是这样的。

服务器上的用户大致分为两类。

1. 普通玩家。
2. 被加入其他权限组，或单独授予了特殊权限的玩家。

你不会想浪费宝贵的磁盘空间来存储第 #1 类玩家的数据，只需要保存管理人员和拥有特殊等级的玩家的数据。普通“成员”就是普通成员，没有必要存储他们的任何权限数据。

接下来的问题是，如何判断某个用户是否“普通”。设想以下情况。

1. 默认权限组设为 "default"。玩家加入时，会被分配到 "default"，随后保存数据。
2. 过了一段时间，你决定将默认权限组改为 "member"。
3. 结果，所有老玩家都在 "default" 权限组中，其他玩家却在 "member" 中。这就不合适了。

即使不保存“普通”用户，这个问题也仍可能发生。

1. 默认权限组设为 "default"。
2. 你想给 "Notch" 一个特殊的 "essentials.fly" 权限。Notch 的权限数据被保存下来，其中记录他是 "default" 权限组的成员，并拥有特殊的飞行权限。
3. 然后，你修改了默认权限组。所有“普通”成员都会获得新的默认权限组，但 Notch 仍然在 default！

因此，我们将默认权限组设计为**不可配置**。说真的，这让所有人都省事得多！不过，我们也理解，这样用起来有时会令人困扰。

可以选择以下做法。

<a id="keep-using-the-default-group-but-change-the-display-name"></a>
### 继续使用默认权限组，但更改“显示名称”
基于上述原因，我们强烈建议继续使用 default 权限组。

然后，只需使用 `/lp group default setdisplayname <name>` 设置显示名称即可！


<a id="configure-inheritance"></a>
### 配置继承关系
采用这种方式时，所有用户仍然属于 "default" 权限组。不过，可以为 default 配置一个父级权限组，让它从另一个名称不同的权限组继承权限。

```
/lp creategroup member
/lp group default parent add member
```
