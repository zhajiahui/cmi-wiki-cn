---
title: 日志命令
source_url: https://luckperms.net/wiki/Log-Commands
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
*  [/lp log `recent` [user] [page]](log-commands.md#lp-log-recent-user-page)
*  [/lp log `search` \<query\> [page]](log-commands.md#lp-log-search-query-page)
*  [/lp log `notify` [on|off]](log-commands.md#lp-log-notify-onoff)
*  [/lp log `userhistory` \<user\> [page]](log-commands.md#lp-log-userhistory-user-page)
*  [/lp log `grouphistory` \<group\> [page]](log-commands.md#lp-log-grouphistory-group-page)
*  [/lp log `trackhistory` \<track\> [page]](log-commands.md#lp-log-trackhistory-track-page)

___
<a id="lp-log-recent-user-page"></a>
#### `/lp log recent [user] [page]`  
**权限**： luckperms.log.recent  
**参数**：  
* `[user]` - 用于筛选的用户名或 UUID
* `[page]` - 要查看的页码

列出最近的操作。

___
<a id="lp-log-search-query-page"></a>
#### `/lp log search <query> [page]`  
**权限**： luckperms.log.search  
**参数**：  
* `<query>` - 要搜索的查询内容
* `[page]` - 要查看的页码

搜索与指定查询内容匹配的日志条目。

___
<a id="lp-log-notify-onoff"></a>
#### `/lp log notify [on|off]`  
**权限**： luckperms.log.notify  
**参数**：  
* `[on|off]` - 启用或禁用

为执行命令的发送者切换日志通知的开关状态。

___
<a id="lp-log-userhistory-user-page"></a>
#### `/lp log userhistory <user> [page]`  
**权限**： luckperms.log.userhistory  
**参数**：  
* `<user>` - 要搜索的用户
* `[page]` - 要查看的页码

搜索针对指定用户执行的操作日志。

___
<a id="lp-log-grouphistory-group-page"></a>
#### `/lp log grouphistory <group> [page]`  
**权限**： luckperms.log.grouphistory  
**参数**：  
* `<group>` - 要搜索的权限组
* `[page]` - 要查看的页码

搜索针对指定权限组执行的操作日志。

___
<a id="lp-log-trackhistory-track-page"></a>
#### `/lp log trackhistory <track> [page]`  
**权限**： luckperms.log.trackhistory  
**参数**：  
* `<track>` - 要搜索的晋升路线
* `[page]` - 要查看的页码

搜索针对指定晋升路线执行的操作日志。

___