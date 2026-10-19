---
title: 晋升路线
source_url: https://luckperms.net/wiki/Tracks
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 有一套自身的晋升路线系统，在某种程度上有些独特，不过大多数其他权限插件也有类似的功能。

可以将晋升路线理解为“阶梯”或“晋升路径”。

---

请注意，晋升路线只用于方便地晋升和降级用户，**不会影响继承关系**。

---

<a id="example-1"></a>
### 示例 1
例如，我有一条名为 "staff" 的晋升路线，包含以下权限组：

**default :arrow_right: helper :arrow_right: mod :arrow_right: admin**

然后，就可以使用这条晋升路线来晋升或降级用户。

例如，如果 "Notch" 位于 helper 权限组，而我想让他成为 mod，就会执行：

`/luckperms user Notch promote staff`

<a id="example-2"></a>
### 示例 2
我还可以为赞助者设置另一条晋升路线，包含：

**default :arrow_right: iron :arrow_right: gold :arrow_right: diamond**

这样，每当用户购买“等级升级”或类似内容时，就可以让他们沿此晋升路线晋升。

`/luckperms user Luck promote donator`

要让用户在晋升路线上退回一级，只需使用 demote 命令。

<a id="creating-a-track"></a>
## 创建晋升路线
只需先执行 `/luckperms createtrack <name>`，再执行 `/luckperms track <name> append <group>`，逐个添加权限组。还有其他命令可以帮助编辑晋升路线，详见命令用法页面。