---
title: 占位符
source_url: https://luckperms.net/wiki/Placeholders
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 提供了一些占位符，可在支持它们的插件中使用。

<a id="placeholderapi"></a>
### PlaceholderAPI
要在支持 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) 的插件中使用 LuckPerms 占位符，需要安装 LuckPerms 占位符扩展。

要通过 clip 的 ecloud 系统自动安装最新版本的占位符扩展，只需先执行 `/papi ecloud download LuckPerms`，再执行 `/papi reload`。

要手动安装最新版本的占位符扩展，需要：

* 从[此处](https://ci.lucko.me/job/LuckPermsPlaceholders/)下载 `Expansion-LuckPerms.jar`
* 将它放入 `/plugins/PlaceholderAPI/expansions/`。

<a id="mvdwplaceholderapi"></a>
### MVdWPlaceholderAPI
要在支持 [MVdWPlaceholderAPI](https://www.spigotmc.org/resources/mvdwplaceholderapi.11182/) 的插件中使用 LuckPerms 占位符，需要安装 LuckPerms 占位符对接插件。

* 从[此处](https://ci.lucko.me/job/LuckPermsPlaceholders/)下载 `LuckPermsMVdWHook.jar`
* 将它放入 `/plugins/` 文件夹。

<a id="fabric-placeholderapi"></a>
### Fabric PlaceholderAPI
要在支持 [Fabric PlaceholderAPI](https://placeholders.pb4.eu/) 的模组中使用 Fabric 版 LuckPerms 占位符，需要安装 LuckPerms 占位符对接模组。它的占位符格式略有不同，详见其[文档](https://placeholders.pb4.eu/user/mod-placeholders/#luckperms)。

* 从[此处](https://ci.lucko.me/job/LuckPermsPlaceholders/)下载 `LuckPerms-Fabric-PlaceholderAPI-Hook.jar`
* 将它放入 `/mods/` 文件夹。



<a id="placeholders"></a>
## 占位符

对于带有**参数**的占位符，必须将参数附加在占位符末尾，并用下划线（`_`）分隔。

例如，`%luckperms_meta%` 占位符需要一个 `<meta key>` 参数。假设元数据键为 *home*，完整的占位符就是 `%luckperms_meta_home%`。

| 占位符 | 参数 | 说明 |
| ----------------------------------------------- | ---------------------------- | ------------------------------------------------------------ |
| `%luckperms_prefix%`                            |                              | 返回玩家的前缀 |
| `%luckperms_suffix%`                            |                              | 返回玩家的后缀 |
| `%luckperms_meta%`                              | `<meta key>`                 | 返回指定元数据键的一个值 |
| `%luckperms_meta_all%`                          | `<meta key>`                 | 返回指定元数据键已设置的所有值 |
| `%luckperms_prefix_element%`                    | `<element>`                  | 根据指定的“元数据堆叠”元素定义返回一个前缀元素。参见[前缀叠加](prefix-suffix-stacking.md) |
| `%luckperms_suffix_element%`                    | `<element>`                  | 根据指定的“元数据堆叠”元素定义返回一个后缀元素。参见[前缀叠加](prefix-suffix-stacking.md) |
| `%luckperms_context%`                           | `[context key]`（*可选*） | 返回玩家当前的所有上下文。如果通过参数指定了键，则只返回该键对应的值。 |
| `%luckperms_groups%`                            |                              | 返回玩家直接继承的权限组列表。 |
| `%luckperms_inherited_groups%`                  |                              | 返回玩家直接或间接继承的所有权限组的列表。 |
| `%luckperms_primary_group_name%`                |                              | 返回玩家的主权限组名称。 |
| `%luckperms_has_permission%`                    | `<permission>`               | 返回玩家是否直接拥有与指定权限完全一致的权限（这与权限检查并不相同！）。 |
| `%luckperms_inherits_permission%`               | `<permission>`               | 返回玩家是否继承了与指定权限完全一致的权限（这与权限检查并不相同！）。 |
| `%luckperms_check_permission%`                  | `<permission>`               | 返回对该玩家检查指定权限的结果。 |
| `%luckperms_in_group%`                          | `<group>`                    | 返回玩家是否直接属于指定权限组。 |
| `%luckperms_inherits_group%`                    | `<group>`                    | 返回玩家是否直接或间接属于指定权限组。 |
| `%luckperms_on_track%`                          | `<track>`                    | 返回玩家的“主权限组”是否位于此晋升路线中。（*已弃用：请避免依赖主权限组，改用下面的占位符！*） |
| `%luckperms_has_groups_on_track%`               | `<track>`                    | 返回玩家直接所属的权限组中，是否有任何一个位于指定晋升路线中。 |
| `%luckperms_highest_group_by_weight%`           |                              | 返回玩家权重最高的权限组名称，*不包括*通过其他权限组间接继承的权限组。 |
| `%luckperms_lowest_group_by_weight%`            |                              | 返回玩家权重最低的权限组名称，*不包括*通过其他权限组间接继承的权限组。 |
| `%luckperms_highest_inherited_group_by_weight%` |                              | 返回玩家权重最高的权限组名称，*包括*通过其他权限组间接继承的权限组。 |
| `%luckperms_lowest_inherited_group_by_weight%`  |                              | 返回玩家权重最低的权限组名称，*包括*通过其他权限组间接继承的权限组。 |
| `%luckperms_current_group_on_track%`            | `<track>`                    | 如果玩家当前位于指定晋升路线中，返回其所在权限组的名称。 |
| `%luckperms_next_group_on_track%`               | `<track>`                    | 如果玩家当前位于指定晋升路线中，返回下一个权限组的名称（即下一次晋升将加入的权限组）。 |
| `%luckperms_previous_group_on_track%`           | `<track>`                    | 如果玩家当前位于指定晋升路线中，返回前一个权限组的名称（即下一次降级将加入的权限组）。 |
| `%luckperms_first_group_on_tracks%`             | `<tracks>`                   | 根据以逗号分隔的晋升路线名称列表，查找玩家在任一指定晋升路线中继承的第一个权限组。 |
| `%luckperms_last_group_on_tracks%`              | `<tracks>`                   | 根据以逗号分隔的晋升路线名称列表，查找玩家在任一指定晋升路线中继承的最后一个权限组。 |
| `%luckperms_expiry_time%`                       | `<permission>`               | 获取直接分配给玩家的某个临时权限的剩余时长。 |
| `%luckperms_inherited_expiry_time%`             | `<permission>`               | 获取直接分配给玩家或由玩家继承的某个临时权限的剩余时长。 |
| `%luckperms_group_expiry_time%`                 | `<group name>`               | 获取直接分配给玩家的某个临时权限组成员资格的剩余时长。 |
| `%luckperms_inherited_group_expiry_time%`       | `<group name>`               | 获取直接分配给玩家或由玩家继承的某个临时权限组成员资格的剩余时长。 |

