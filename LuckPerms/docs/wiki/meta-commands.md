---
title: 元数据命令
source_url: https://luckperms.net/wiki/Meta-Commands
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
*  [`info`](meta-commands.md#lp-usergroup-usergroup-meta-info)
*  [`set` \<key\> \<value\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-set-key-value-context)
*  [`unset` \<key\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-unset-key-value-context)
*  [`settemp` \<key\> \<value\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-settemp-key-value-duration-temporary-modifier-context)
*  [`unsettemp` \<key\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-unsettemp-key-context)
*  [`addprefix` \<priority\> \<prefix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addprefix-priority-prefix-context)
*  [`addsuffix` \<priority\> \<suffix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addsuffix-priority-suffix-context)
*  [`setprefix` [priority] \<prefix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-setprefix-priority-prefix-context)
*  [`setsuffix` [priority] \<suffix\> [context...]](meta-commands.md#lp-usergroup-usergroup-meta-setsuffix-priority-suffix-context)
*  [`removeprefix` \<priority\> [prefix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removeprefix-priority-prefix-context)
*  [`removesuffix` \<priority\> [suffix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removesuffix-priority-suffix-context)
*  [`addtempprefix` \<priority\> \<prefix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addtempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`addtempsuffix` \<priority\> \<suffix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-addtempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`settempprefix` [priority] \<prefix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-settempprefix-priority-prefix-duration-temporary-modifier-context)
*  [`settempsuffix` [priority] \<suffix\> \<duration\> [temporary modifier] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-settempsuffix-priority-suffix-duration-temporary-modifier-context)
*  [`removetempprefix` \<priority\> [prefix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removetempprefix-priority-prefix-context)
*  [`removetempsuffix` \<priority\> [suffix] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-removetempsuffix-priority-suffix-context)
*  [`clear` \[type\] [context...]](meta-commands.md#lp-usergroup-usergroup-meta-clear-type-context)

___
<a id="lp-usergroup-usergroup-meta-info"></a>
#### `/lp user/group <user|group> meta info`  
**权限**： luckperms.user.meta.info 或 luckperms.group.meta.info  
列出用户或权限组继承的元数据（选项）、前缀和后缀。

___
<a id="lp-usergroup-usergroup-meta-set-key-value-context"></a>
#### `/lp user/group <user|group> meta set <key> <value> [context...]`  
**权限**： luckperms.user.meta.set 或 luckperms.group.meta.set  
**参数**：  
* `<key>` - 要设置的键
* `<value>` - 要为该键设置的值
* `[context...]` - 设置元数据时使用的[上下文](context.md)

为用户或权限组设置一个元数据键值对。其他插件可以通过 Vault 或 Sponge Permissions API 读取和修改这些值。

___
<a id="lp-usergroup-usergroup-meta-unset-key-value-context"></a>
#### `/lp user/group <user|group> meta unset <key> <value> [context...]`  
**权限**： luckperms.user.meta.unset 或 luckperms.group.meta.unset  
**参数**：  
* `<key>` - 要取消设置的键
* `[context...]` - 取消设置元数据时使用的[上下文](context.md)

取消设置用户或权限组的一个元数据键值对。

___
<a id="lp-usergroup-usergroup-meta-settemp-key-value-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> meta settemp <key> <value> <duration> [temporary modifier] [context...]`  
**权限**： luckperms.user.meta.settemp 或 luckperms.group.meta.settemp  
**参数**：  
* `<key>` - 要设置的键
* `<value>` - 要为该键设置的值
* `<duration>` - 元数据到期前的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 设置元数据时使用的[上下文](context.md)

为用户或权限组设置一个临时元数据键值对。时长可以填写一段时间，也可以填写权限到期时的 Unix 时间戳。例如，"3d13h45m" 表示权限在 3 天 13 小时 45 分钟后到期；"1482694200" 表示权限在 2016 年 12 月 25 日晚上 7:30 到期。  
LuckPerms 使用的相对时间格式与 Java 中的 [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) 类似。例如，`1M` 表示一个月，而 `1m` 表示一分钟。

"temporary modifier" 参数用于指定权限时长的累加方式，共有 3 个选项。

| 修饰符键 | 说明 |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的时长加到新时长上 |
| `replace`    | 保留最长的时长，舍弃其他节点 |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接执行失败 |

___
<a id="lp-usergroup-usergroup-meta-unsettemp-key-context"></a>
#### `/lp user/group <user|group> meta unsettemp <key> [context...]`  
**权限**： luckperms.user.meta.unsettemp 或 luckperms.group.meta.unsettemp  
**参数**：  
* `<key>` - 要取消设置的键
* `[context...]` - 取消设置元数据时使用的[上下文](context.md)

取消设置用户或权限组的一个临时元数据键值对。

___
<a id="lp-usergroup-usergroup-meta-addprefix-priority-prefix-context"></a>
#### `/lp user/group <user|group> meta addprefix <priority> <prefix> [context...]`  
**权限**： luckperms.user.meta.addprefix 或 luckperms.group.meta.addprefix  
**参数**：  
* `<priority>` - 添加前缀时使用的优先级
* `<prefix>` - 实际的前缀字符串
* `[context...]` - 添加前缀时使用的[上下文](context.md)

为用户或权限组添加前缀。如果前缀包含空格，可以用 " " 引号将其括起来。

___
<a id="lp-usergroup-usergroup-meta-addsuffix-priority-suffix-context"></a>
#### `/lp user/group <user|group> meta addsuffix <priority> <suffix> [context...]`  
**权限**： luckperms.user.meta.addsuffix 或 luckperms.group.meta.addsuffix  
**参数**：  
* `<priority>` - 添加后缀时使用的优先级
* `<suffix>` - 实际的后缀字符串
* `[context...]` - 添加后缀时使用的[上下文](context.md)

为用户或权限组添加后缀。如果后缀包含空格，可以用 " " 引号将其括起来。

___
<a id="lp-usergroup-usergroup-meta-setprefix-priority-prefix-context"></a>
#### `/lp user/group <user|group> meta setprefix [priority] <prefix> [context...]`  
**权限**： luckperms.user.meta.setprefix 或 luckperms.group.meta.setprefix  
**参数**：  
* `[priority]` - 设置前缀时使用的优先级
* `<prefix>` - 实际的前缀字符串
* `[context...]` - 设置前缀时使用的[上下文](context.md)

为用户或权限组设置前缀。如果前缀包含空格，可以用 " " 引号将其括起来。与 `addprefix` 命令不同，此命令在添加新前缀时，会移除同一上下文中已有的前缀。另一个区别是，setprefix 命令中的 priority 参数是可选的；执行命令时，LuckPerms 会自动确定一个合适的优先级值。

___
<a id="lp-usergroup-usergroup-meta-setsuffix-priority-suffix-context"></a>
#### `/lp user/group <user|group> meta setsuffix [priority] <suffix> [context...]`  
**权限**： luckperms.user.meta.setsuffix 或 luckperms.group.meta.setsuffix  
**参数**：  
* `[priority]` - 设置后缀时使用的优先级
* `<suffix>` - 实际的后缀字符串
* `[context...]` - 设置后缀时使用的[上下文](context.md)

为用户或权限组设置后缀。如果后缀包含空格，可以用 " " 引号将其括起来。与 `addsuffix` 命令不同，此命令在添加新后缀时，会移除同一上下文中已有的后缀。另一个区别是，setsuffix 命令中的 priority 参数是可选的；执行命令时，LuckPerms 会自动确定一个合适的优先级值。

___
<a id="lp-usergroup-usergroup-meta-removeprefix-priority-prefix-context"></a>
#### `/lp user/group <user|group> meta removeprefix <priority> [prefix] [context...]`  
**权限**： luckperms.user.meta.removeprefix 或 luckperms.group.meta.removeprefix  
**参数**：  
* `<priority>` - 要移除的前缀所在的优先级
* `[prefix]` - 实际的前缀字符串
* `[context...]` - 移除前缀时使用的[上下文](context.md)

移除用户或权限组的前缀。如果前缀包含空格，可以用 " " 引号将其括起来。

___
<a id="lp-usergroup-usergroup-meta-removesuffix-priority-suffix-context"></a>
#### `/lp user/group <user|group> meta removesuffix <priority> [suffix] [context...]`  
**权限**： luckperms.user.meta.removesuffix 或 luckperms.group.meta.removesuffix  
**参数**：  
* `<priority>` - 要移除的后缀所在的优先级
* `[suffix]` - 实际的后缀字符串
* `[context...]` - 移除后缀时使用的[上下文](context.md)

移除用户或权限组的后缀。如果后缀包含空格，可以用 " " 引号将其括起来。

___
<a id="lp-usergroup-usergroup-meta-addtempprefix-priority-prefix-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> meta addtempprefix <priority> <prefix> <duration> [temporary modifier] [context...]`  
**权限**： luckperms.user.meta.addtempprefix 或 luckperms.group.meta.addtempprefix  
**参数**：  
* `<priority>` - 添加前缀时使用的优先级
* `<prefix>` - 实际的前缀字符串
* `<duration>` - 前缀到期前的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 添加前缀时使用的[上下文](context.md)

为用户或权限组添加临时前缀。如果前缀包含空格，可以用 " " 引号将其括起来。时长可以填写一段时间，也可以填写权限到期时的 Unix 时间戳。例如，"3d13h45m" 表示权限在 3 天 13 小时 45 分钟后到期；"1482694200" 表示权限在 2016 年 12 月 25 日晚上 7:30 到期。  
LuckPerms 使用的相对时间格式与 Java 中的 [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) 类似。例如，`1M` 表示一个月，而 `1m` 表示一分钟。

"temporary modifier" 参数用于指定权限时长的累加方式，共有 3 个选项。

| 修饰符键 | 说明 |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的时长加到新时长上 |
| `replace`    | 保留最长的时长，舍弃其他节点 |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接执行失败 |

___
<a id="lp-usergroup-usergroup-meta-addtempsuffix-priority-suffix-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> meta addtempsuffix <priority> <suffix> <duration> [temporary modifier] [context...]`  
**权限**： luckperms.user.meta.addtempsuffix 或 luckperms.group.meta.addtempsuffix  
**参数**：  
* `<priority>` - 添加后缀时使用的优先级
* `<suffix>` - 实际的后缀字符串
* `<duration>` - 后缀到期前的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 添加后缀时使用的[上下文](context.md)

为用户或权限组添加临时后缀。如果后缀包含空格，可以用 " " 引号将其括起来。时长可以填写一段时间，也可以填写权限到期时的 Unix 时间戳。例如，"3d13h45m" 表示权限在 3 天 13 小时 45 分钟后到期；"1482694200" 表示权限在 2016 年 12 月 25 日晚上 7:30 到期。  
LuckPerms 使用的相对时间格式与 Java 中的 [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) 类似。例如，`1M` 表示一个月，而 `1m` 表示一分钟。

"temporary modifier" 参数用于指定权限时长的累加方式，共有 3 个选项。

| 修饰符键 | 说明 |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的时长加到新时长上 |
| `replace`    | 保留最长的时长，舍弃其他节点 |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接执行失败 |

___
<a id="lp-usergroup-usergroup-meta-settempprefix-priority-prefix-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> meta settempprefix [priority] <prefix> <duration> [temporary modifier] [context...]`  
**权限**： luckperms.user.meta.settempprefix 或 luckperms.group.meta.settempprefix  
**参数**：  
* `[priority]` - 设置前缀时使用的优先级
* `<prefix>` - 实际的前缀字符串
* `<duration>` - 前缀到期前的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 设置前缀时使用的[上下文](context.md)

为用户或权限组设置临时前缀。如果前缀包含空格，可以用 " " 引号将其括起来。与 `addtempprefix` 命令不同，此命令在添加新前缀时，会移除同一上下文中已有的前缀。另一个区别是，settempprefix 命令中的 priority 参数是可选的；执行命令时，LuckPerms 会自动确定一个合适的优先级值。

时长可以填写一段时间，也可以填写权限到期时的 Unix 时间戳。例如，"3d13h45m" 表示权限在 3 天 13 小时 45 分钟后到期；"1482694200" 表示权限在 2016 年 12 月 25 日晚上 7:30 到期。  
LuckPerms 使用的相对时间格式与 Java 中的 [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) 类似。例如，`1M` 表示一个月，而 `1m` 表示一分钟。

"temporary modifier" 参数用于指定权限时长的累加方式，共有 3 个选项。

| 修饰符键 | 说明 |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的时长加到新时长上 |
| `replace`    | 保留最长的时长，舍弃其他节点 |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接执行失败 |

___
<a id="lp-usergroup-usergroup-meta-settempsuffix-priority-suffix-duration-temporary-modifier-context"></a>
#### `/lp user/group <user|group> meta settempsuffix [priority] <suffix> <duration> [temporary modifier] [context...]`  
**权限**： luckperms.user.meta.settempsuffix 或 luckperms.group.meta.settempsuffix  
**参数**：  
* `[priority]` - 设置后缀时使用的优先级
* `<suffix>` - 实际的后缀字符串
* `<duration>` - 后缀到期前的时长
* `[temporary modifier]` - 临时权限的应用方式
* `[context...]` - 设置后缀时使用的[上下文](context.md)

为用户或权限组设置临时后缀。如果后缀包含空格，可以用 " " 引号将其括起来。与 `addtempsuffix` 命令不同，此命令在添加新后缀时，会移除同一上下文中已有的后缀。另一个区别是，settempsuffix 命令中的 priority 参数是可选的；执行命令时，LuckPerms 会自动确定一个合适的优先级值。

时长可以填写一段时间，也可以填写权限到期时的 Unix 时间戳。例如，"3d13h45m" 表示权限在 3 天 13 小时 45 分钟后到期；"1482694200" 表示权限在 2016 年 12 月 25 日晚上 7:30 到期。  
LuckPerms 使用的相对时间格式与 Java 中的 [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) 类似。例如，`1M` 表示一个月，而 `1m` 表示一分钟。

"temporary modifier" 参数用于指定权限时长的累加方式，共有 3 个选项。

| 修饰符键 | 说明 |
|--------------|---------------------------------------------------------------------------|
| `accumulate` | 将已有节点的时长加到新时长上 |
| `replace`    | 保留最长的时长，舍弃其他节点 |
| `deny`       | 如果尝试添加重复的临时节点，命令会直接执行失败 |

___
<a id="lp-usergroup-usergroup-meta-removetempprefix-priority-prefix-context"></a>
#### `/lp user/group <user|group> meta removetempprefix <priority> [prefix] [context...]`  
**权限**： luckperms.user.meta.removetempprefix 或 luckperms.group.meta.removetempprefix  
**参数**：  
* `<priority>` - 要移除的前缀所在的优先级
* `[prefix]` - 实际的前缀字符串
* `[context...]` - 移除前缀时使用的[上下文](context.md)

移除用户或权限组的临时前缀。如果前缀包含空格，可以用 " " 引号将其括起来。

___
<a id="lp-usergroup-usergroup-meta-removetempsuffix-priority-suffix-context"></a>
#### `/lp user/group <user|group> meta removetempsuffix <priority> [suffix] [context...]`  
**权限**： luckperms.user.meta.removetempsuffix 或 luckperms.group.meta.removetempsuffix  
**参数**：  
* `<priority>` - 要移除的后缀所在的优先级
* `[suffix]` - 实际的后缀字符串
* `[context...]` - 移除后缀时使用的[上下文](context.md)

移除用户或权限组的临时后缀。如果后缀包含空格，可以用 " " 引号将其括起来。

___
<a id="lp-usergroup-usergroup-meta-clear-type-context"></a>
#### `/lp user/group <user|group> meta clear [type] [context...]`  
**权限**： luckperms.user.meta.clear 或 luckperms.group.meta.clear  
**参数**：  
* `[type]` - 要清除的元数据类型

| 类型 | 含义 |
|---------------------|---------------------------------------------|
| `any`/`all`/`*`     | 默认类型：清除所有元数据 |
| `chat`/`chatmeta`   | 清除所有前缀和后缀 |
| `meta`              | 清除非聊天元数据（不含前缀和后缀） |
| `prefix`/`prefixes` | 清除前缀 |
| `suffix`/`suffixes` | 清除后缀 |

* `[context...]` - 用于筛选的[上下文](context.md)

移除所有元数据、前缀和后缀。

___
