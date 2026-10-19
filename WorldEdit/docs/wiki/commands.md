---
title: 命令
source_url: https://worldedit.enginehub.org/en/latest/commands/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 命令 { #commands }

<a id="contents"></a>

- <a id="id1"></a> [常规命令](#general-commands)

- <a id="id2"></a> [移动命令](#navigation-commands)

- <a id="id3"></a> [选区命令](#selection-commands)

- <a id="id4"></a> [选区命令](#region-commands)

- <a id="id5"></a> [生成命令](#generation-commands)

- <a id="id6"></a> [原理图与剪贴板命令](#schematic-and-clipboard-commands)

- <a id="id7"></a> [工具命令](#tool-commands)

- <a id="id8"></a> [超级镐命令](#super-pickaxe-commands)

- <a id="id9"></a> [笔刷命令](#brush-commands)

- <a id="id10"></a> [生物群系命令](#biome-commands)

- <a id="id11"></a> [区块命令](#chunk-commands)

- <a id="id12"></a> [快照命令](#snapshot-commands)

- <a id="id13"></a> [脚本命令](#scripting-commands)

- <a id="id14"></a> [实用命令](#utility-commands)

!!! note "注意"

    `[ ]` 中的参数可选，`< >` 中的参数必填。

!!! tip "提示"

    在游戏中执行 `//help` 即可查看命令列表。

## [常规命令](#id1) { #general-commands }

<a id="command-/worldedit"></a>

`/worldedit`（或 `/we`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">WorldEdit 命令</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit <help|version|trace|reload|cui|tz|report>`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-help"></a>

`/worldedit help`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">显示 WorldEdit 命令帮助</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.help`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit help [-s] [-p <page>] [command...]`</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">列出指定命令的子命令，如果该命令存在子命令</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">要获取的页码</td>
</tr>
<tr>
<td markdown="span">`[command...]`</td>
<td markdown="span">要查看帮助的命令</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-version"></a>

`/worldedit version`（或 `/worldedit ver`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">查看 WorldEdit 版本</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit version`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-trace"></a>

`/worldedit trace`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">切换跟踪钩子</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit trace [hookMode]`</td>
</tr>
<tr>
<td markdown="span">`[hookMode]`</td>
<td markdown="span">要为跟踪钩子设置的模式</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-reload"></a>

`/worldedit reload`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">重载配置</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.reload`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit reload`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-cui"></a>

`/worldedit cui`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">完成 CUI 握手，仅供内部使用</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit cui`</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-tz"></a>

`/worldedit tz`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置快照使用的时区</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit tz <timezone>`</td>
</tr>
<tr>
<td markdown="span">`<timezone>`</td>
<td markdown="span">要设置的时区</td>
</tr>
</tbody>
</table>

<a id="command-/worldedit-report"></a>

`/worldedit report`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成 WorldEdit 报告</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.report`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/worldedit report [-p]`</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">将报告上传到 pastebin</td>
</tr>
</tbody>
</table>

<a id="command-/undo"></a>

`/undo`（或 `//undo`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">撤销上一次历史操作</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.history.undo`, `worldedit.history.undo.self`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/undo [times] [player]`</td>
</tr>
<tr>
<td markdown="span">`[times]`</td>
<td markdown="span">撤销次数</td>
</tr>
<tr>
<td markdown="span">`[player]`</td>
<td markdown="span">撤销此玩家的操作</td>
</tr>
</tbody>
</table>

<a id="command-/redo"></a>

`/redo`（或 `//redo`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">重做上一次历史操作</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.history.redo`, `worldedit.history.redo.self`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/redo [times] [player]`</td>
</tr>
<tr>
<td markdown="span">`[times]`</td>
<td markdown="span">重做次数</td>
</tr>
<tr>
<td markdown="span">`[player]`</td>
<td markdown="span">重做此玩家的操作</td>
</tr>
</tbody>
</table>

<a id="command-/clearhistory"></a>

`/clearhistory`（或 `//clearhistory`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">清空自己的操作历史</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.history.clear`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/clearhistory`</td>
</tr>
</tbody>
</table>

<a id="command-//limit"></a>

`//limit`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">修改方块修改数量上限</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.limit`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//limit [limit]`</td>
</tr>
<tr>
<td markdown="span">`[limit]`</td>
<td markdown="span">要设置的上限</td>
</tr>
</tbody>
</table>

<a id="command-//timeout"></a>

`//timeout`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">修改求值超时时间。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.timeout`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//timeout [limit]`</td>
</tr>
<tr>
<td markdown="span">`[limit]`</td>
<td markdown="span">要设置的超时时间</td>
</tr>
</tbody>
</table>

<a id="command-//fast"></a>

`//fast`

!!! warning "警告"

    此命令已弃用。//fast 与 //perf 功能重复，将在 WorldEdit 8 中移除。

    请改用 `//perf`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">切换快速模式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.fast`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//fast [fastMode]`</td>
</tr>
<tr>
<td markdown="span">`[fastMode]`</td>
<td markdown="span">快速模式的新状态</td>
</tr>
</tbody>
</table>

<a id="command-//perf"></a>

`//perf`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">切换影响性能的附带效果</p> <p markdown="span">注意，此命令今后必定会改变，目前不要依赖其确切格式。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.perf`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//perf [-h] [sideEffect] [newState]`</td>
</tr>
<tr>
<td markdown="span">`[sideEffect]`</td>
<td markdown="span">附带效果</td>
</tr>
<tr>
<td markdown="span">`[newState]`</td>
<td markdown="span">附带效果的新状态</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">显示信息框</td>
</tr>
</tbody>
</table>

<a id="command-//reorder"></a>

`//reorder`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置 WorldEdit 的重排模式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.reorder`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//reorder [reorderMode]`</td>
</tr>
<tr>
<td markdown="span">`[reorderMode]`</td>
<td markdown="span">重排模式</td>
</tr>
</tbody>
</table>

<a id="command-//drawsel"></a>

`//drawsel`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">切换当前选区的显示</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.drawsel`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//drawsel [drawSelection]`</td>
</tr>
<tr>
<td markdown="span">`[drawSelection]`</td>
<td markdown="span">选区显示的新状态</td>
</tr>
</tbody>
</table>

<a id="command-//world"></a>

`//world`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置覆盖使用的世界</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.world`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//world [world]`</td>
</tr>
<tr>
<td markdown="span">`[world]`</td>
<td markdown="span">覆盖使用的世界</td>
</tr>
</tbody>
</table>

<a id="command-//watchdog"></a>

`//watchdog`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">修改 watchdog 钩子的状态。</p> <p markdown="span">此功能取决于平台实现。并非所有平台都支持 watchdog 钩子，也并非都有 watchdog。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.watchdog`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//watchdog [hookMode]`</td>
</tr>
<tr>
<td markdown="span">`[hookMode]`</td>
<td markdown="span">要为 watchdog 钩子设置的模式</td>
</tr>
</tbody>
</table>

<a id="command-/gmask"></a>

`/gmask`（或 `//gmask`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置全局蒙版</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.global-mask`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/gmask [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">要设置的蒙版</td>
</tr>
</tbody>
</table>

<a id="command-/toggleplace"></a>

`/toggleplace`（或 `//toggleplace`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">在当前位置与 pos1 之间切换放置位置</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/toggleplace`</td>
</tr>
</tbody>
</table>

<a id="command-/placement"></a>

`/placement`（或 `//placement`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择要使用的放置位置</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.placement`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/placement <placementType> [multiplier] [offset]`</td>
</tr>
<tr>
<td markdown="span">`<placementType>`</td>
<td markdown="span">要使用的放置位置类型</td>
</tr>
<tr>
<td markdown="span">`[multiplier]`</td>
<td markdown="span">应用偏移的次数</td>
</tr>
<tr>
<td markdown="span">`[offset]`</td>
<td markdown="span">相对于所用放置位置的偏移量</td>
</tr>
</tbody>
</table>

<a id="command-/searchitem"></a>

`/searchitem`（或 `//searchitem`, `//l`, `//search`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">搜索物品</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.searchitem`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/searchitem [-bi] [-p <page>] <query...>`</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">只搜索方块</td>
</tr>
<tr>
<td markdown="span">`[-i]`</td>
<td markdown="span">只搜索物品</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">返回结果的页码</td>
</tr>
<tr>
<td markdown="span">`<query...>`</td>
<td markdown="span">搜索内容</td>
</tr>
</tbody>
</table>

<a id="command-//registry"></a>

`//registry`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">搜索指定注册表</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.registry`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//registry <registry> [-p <page>] [queryBits...]`</td>
</tr>
<tr>
<td markdown="span">`<registry>`</td>
<td markdown="span">要搜索的注册表</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">返回结果的页码</td>
</tr>
<tr>
<td markdown="span">`[queryBits...]`</td>
<td markdown="span">搜索内容</td>
</tr>
</tbody>
</table>

## [移动命令](#id2) { #navigation-commands }

<a id="command-/unstuck"></a>

`/unstuck`（或 `/!`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">从方块内部脱困</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.unstuck`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/unstuck`</td>
</tr>
</tbody>
</table>

<a id="command-/ascend"></a>

`/ascend`（或 `/asc`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">上升一层</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.ascend`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/ascend [levels]`</td>
</tr>
<tr>
<td markdown="span">`[levels]`</td>
<td markdown="span">要上升的层数</td>
</tr>
</tbody>
</table>

<a id="command-/descend"></a>

`/descend`（或 `/desc`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">下降一层</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.descend`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/descend [levels]`</td>
</tr>
<tr>
<td markdown="span">`[levels]`</td>
<td markdown="span">要下降的层数</td>
</tr>
</tbody>
</table>

<a id="command-/ceil"></a>

`/ceil`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">前往天花板</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.ceiling`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/ceil [-fg] [clearance]`</td>
</tr>
<tr>
<td markdown="span">`[clearance]`</td>
<td markdown="span">头顶要留出的方块数量</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">强制通过飞行使你停在原位</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">强制通过玻璃使你停在原位</td>
</tr>
</tbody>
</table>

<a id="command-/thru"></a>

`/thru`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">穿过墙壁</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.thru.command`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/thru`</td>
</tr>
</tbody>
</table>

<a id="command-/jumpto"></a>

`/jumpto`（或 `/j`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">传送到指定位置</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.jumpto.command`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/jumpto`</td>
</tr>
</tbody>
</table>

<a id="command-/up"></a>

`/up`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">向上移动一段距离</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.navigation.up`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/up [-fg] <distance>`</td>
</tr>
<tr>
<td markdown="span">`<distance>`</td>
<td markdown="span">向上移动的距离</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">强制通过飞行使你停在原位</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">强制通过玻璃使你停在原位</td>
</tr>
</tbody>
</table>

## [选区命令](#id3) { #selection-commands }

<a id="command-//pos"></a>

`//pos`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置位置</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//pos [pos1] [pos2...] [-s <selectorChoice>]`</td>
</tr>
<tr>
<td markdown="span">`[pos1]`</td>
<td markdown="span">主位置的坐标；未提供时使用玩家位置。</td>
</tr>
<tr>
<td markdown="span">`[pos2...]`</td>
<td markdown="span">要添加的次要位置坐标；未提供时使用玩家位置。</td>
</tr>
<tr>
<td markdown="span">`[-s <selectorChoice>]`</td>
<td markdown="span">要切换到的选区类型</td>
</tr>
</tbody>
</table>

<a id="command-//pos1"></a>

`//pos1`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置位置 1</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//pos1 [coordinates]`</td>
</tr>
<tr>
<td markdown="span">`[coordinates]`</td>
<td markdown="span">位置 1 的坐标</td>
</tr>
</tbody>
</table>

<a id="command-//pos2"></a>

`//pos2`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置位置 2</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.pos`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//pos2 [coordinates]`</td>
</tr>
<tr>
<td markdown="span">`[coordinates]`</td>
<td markdown="span">位置 2 的坐标</td>
</tr>
</tbody>
</table>

<a id="command-//hpos1"></a>

`//hpos1`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将位置 1 设为准星指向的方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.hpos`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//hpos1`</td>
</tr>
</tbody>
</table>

<a id="command-//hpos2"></a>

`//hpos2`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将位置 2 设为准星指向的方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.hpos`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//hpos2`</td>
</tr>
</tbody>
</table>

<a id="command-//chunk"></a>

`//chunk`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">将选区设为当前区块。</p> <p markdown="span">此命令选择高 256 格的区域，可用 y 坐标指定。例如 -c x,1,z 会选择 y=256 到 y=511。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.chunk`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//chunk [-cs] [coordinates]`</td>
</tr>
<tr>
<td markdown="span">`[coordinates]`</td>
<td markdown="span">要选择的区块</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">扩展选区，完整包含与选区相交的所有区块</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">使用区块坐标，而不是方块坐标</td>
</tr>
</tbody>
</table>

<a id="command-//wand"></a>

`//wand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">获取工具物品</p> <p markdown="span">还必须拥有使用所请求工具至少一项功能的权限。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.wand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//wand [-n]`</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">获取导航工具</td>
</tr>
</tbody>
</table>

<a id="command-/toggleeditwand"></a>

`/toggleeditwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">提醒玩家工具现已绑定，可用 /tool none 解除绑定。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.wand.toggle`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/toggleeditwand`</td>
</tr>
</tbody>
</table>

<a id="command-//contract"></a>

`//contract`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">收缩选区</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.contract`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//contract <amount> [reverseAmount] [direction]`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">选区收缩的距离</td>
</tr>
<tr>
<td markdown="span">`[reverseAmount]`</td>
<td markdown="span">向相反方向收缩的距离</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">收缩方向</td>
</tr>
</tbody>
</table>

<a id="command-//shift"></a>

`//shift`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">平移选区</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.shift`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//shift <amount> [direction]`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">选区平移的距离</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">收缩方向</td>
</tr>
</tbody>
</table>

<a id="command-//outset"></a>

`//outset`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">向外扩展选区</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.outset`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//outset [-hv] <amount>`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">向所有方向扩展的距离</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">只在水平方向扩展</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">只在垂直方向扩展</td>
</tr>
</tbody>
</table>

<a id="command-//inset"></a>

`//inset`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">向内收缩选区</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.inset`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//inset [-hv] <amount>`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">向所有方向收缩的距离</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">只在水平方向收缩</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">只在垂直方向收缩</td>
</tr>
</tbody>
</table>

<a id="command-//trim"></a>

`//trim`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">缩小选区，使其恰好包含匹配的方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.trim`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//trim [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">选区中要保留的方块蒙版</td>
</tr>
</tbody>
</table>

<a id="command-//size"></a>

`//size`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">获取选区信息</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.size`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//size [-c]`</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">改为获取剪贴板信息</td>
</tr>
</tbody>
</table>

<a id="command-//count"></a>

`//count`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">统计匹配蒙版的方块数量</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.analysis.count`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//count <mask>`</td>
</tr>
<tr>
<td markdown="span">`<mask>`</td>
<td markdown="span">要匹配的方块蒙版</td>
</tr>
</tbody>
</table>

<a id="command-//distr"></a>

`//distr`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">统计选区中的方块分布</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.analysis.distr`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//distr [-cd] [-p <page>] [-m <sourceMask>]`</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">改为统计剪贴板中的方块分布</td>
</tr>
<tr>
<td markdown="span">`[-d]`</td>
<td markdown="span">按方块状态分别统计</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">查看上一次分布统计的指定页。</td>
</tr>
<tr>
<td markdown="span">`[-m <sourceMask>]`</td>
<td markdown="span">只包含匹配指定蒙版的方块</td>
</tr>
</tbody>
</table>

<a id="command-//sel"></a>

`//sel`（或 `/;`, `//desel`, `//deselect`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择选区选择器</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//sel [-d] [selectorChoiceOrList]`</td>
</tr>
<tr>
<td markdown="span">`[selectorChoiceOrList]`</td>
<td markdown="span">要切换到的选区类型</td>
</tr>
<tr>
<td markdown="span">`[-d]`</td>
<td markdown="span">设置默认选择器</td>
</tr>
</tbody>
</table>

<a id="command-//expand"></a>

`//expand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">扩展选区</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.selection.expand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//expand <vert|<amount> [reverseAmount] [direction]>`</td>
</tr>
<tr>
<td markdown="span">`<amount>`</td>
<td markdown="span">选区扩展距离；也可用 vert 扩展到整个垂直列</td>
</tr>
<tr>
<td markdown="span">`[reverseAmount]`</td>
<td markdown="span">向相反方向扩展的距离</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">扩展方向</td>
</tr>
</tbody>
</table>

<a id="command-//expand-vert"></a>

`//expand vert`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将选区沿垂直方向扩展到世界高度边界。</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//expand vert`</td>
</tr>
</tbody>
</table>

## [选区命令](#id4) { #region-commands }

<a id="command-//set"></a>

`//set`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置选区中的全部方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.set`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//set <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//line"></a>

`//line`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">在长方体选区的角点或凸多面体选区的顶点之间绘制线段</p> <p markdown="span">仅适用于长方体或凸多面体选区</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.line`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//line [-h] <pattern> [thickness]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要放置的方块模式</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">线条粗细</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">只生成外壳</td>
</tr>
</tbody>
</table>

<a id="command-//curve"></a>

`//curve`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">绘制经过所选各点的样条曲线</p> <p markdown="span">仅适用于凸多面体选区</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.curve`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//curve [-h] <pattern> [thickness]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要放置的方块模式</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">曲线粗细</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">只生成外壳</td>
</tr>
</tbody>
</table>

<a id="command-//replace"></a>

`//replace`（或 `//re`, `//rep`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将选区内的方块替换为其他方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.replace`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//replace [from] <to>`</td>
</tr>
<tr>
<td markdown="span">`[from]`</td>
<td markdown="span">指定要替换哪些方块的蒙版</td>
</tr>
<tr>
<td markdown="span">`<to>`</td>
<td markdown="span">替换后使用的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//overlay"></a>

`//overlay`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">在选区内现有方块上方铺设方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.overlay`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//overlay <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">覆盖层的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//center"></a>

`//center`（或 `//middle`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置中心方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.center`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//center <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//naturalize"></a>

`//naturalize`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">顶部 3 层为泥土，下方为石头</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.naturalize`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//naturalize`</td>
</tr>
</tbody>
</table>

<a id="command-//walls"></a>

`//walls`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">在选区四周建墙</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.walls`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//walls <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//faces"></a>

`//faces`（或 `//outline`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">创建选区的墙壁、顶面和底面</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.faces`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//faces <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//smooth"></a>

`//smooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">平滑选区内的地形高度</p> <p markdown="span">示例：‘//smooth 1 grass_block,dirt,stone’ 只会平滑自然地表。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.smooth`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//smooth [iterations] [mask]`</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span">迭代次数</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">用于确定高度图的方块蒙版</td>
</tr>
</tbody>
</table>

<a id="command-//snowsmooth"></a>

`//snowsmooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">利用雪层平滑选区内的地形高度</p> <p markdown="span">示例：‘//snowsmooth 1 -m snow_block,snow’ 只会平滑积雪地形。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.snowsmooth`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//snowsmooth [iterations] [-l <snowBlockCount>] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span">迭代次数</td>
</tr>
<tr>
<td markdown="span">`[-l <snowBlockCount>]`</td>
<td markdown="span">设置雪层下方的雪块数量</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">用于确定高度图的方块蒙版</td>
</tr>
</tbody>
</table>

<a id="command-//move"></a>

`//move`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">移动选区内容</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.move`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//move [-abes] [multiplier] [offset] [replace] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[multiplier]`</td>
<td markdown="span">应用偏移的次数</td>
</tr>
<tr>
<td markdown="span">`[offset]`</td>
<td markdown="span">移动偏移量</td>
</tr>
<tr>
<td markdown="span">`[replace]`</td>
<td markdown="span">原位置留下的方块模式</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">将选区移到目标位置</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">忽略空气方块</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">同时复制实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时复制生物群系</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">设置包含蒙版，不匹配的方块会变为空气</td>
</tr>
</tbody>
</table>

<a id="command-//stack"></a>

`//stack`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">重复堆叠选区内容</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.stack`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//stack [-abers] [count] [offset] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[count]`</td>
<td markdown="span">要堆叠的副本数量</td>
</tr>
<tr>
<td markdown="span">`[offset]`</td>
<td markdown="span">每次堆叠时移动内容的距离</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">将选区移到最后一个堆叠副本处</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">忽略空气方块</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">同时复制实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时复制生物群系</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">使用方块作为距离单位</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">设置包含蒙版，不匹配的方块会变为空气</td>
</tr>
</tbody>
</table>

<a id="command-//regen"></a>

`//regen`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">重新生成选区内容</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.regen`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//regen [-bc] [seed]`</td>
</tr>
<tr>
<td markdown="span">`[seed]`</td>
<td markdown="span">重新生成使用的种子；未指定时使用世界种子</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时重新生成生物群系</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">将重新生成结果放入剪贴板</td>
</tr>
</tbody>
</table>

<a id="command-//deform"></a>

`//deform`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">通过表达式改变选区形状</p> <p markdown="span">表达式会针对每个方块执行，应修改 x、y、z 变量，使其指向要读取的新方块位置。详见 [https://ehub.to/we/expr](https://ehub.to/we/expr)</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.deform`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//deform [-clor] <expression...>`</td>
</tr>
<tr>
<td markdown="span">`<expression...>`</td>
<td markdown="span">要使用的表达式</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">使用游戏世界的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">使用放置位置的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">以选区中心为原点</td>
</tr>
<tr>
<td markdown="span">`[-l]`</td>
<td markdown="span">从剪贴板读取，而不是从世界读取</td>
</tr>
</tbody>
</table>

<a id="command-//hollow"></a>

`//hollow`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">掏空选区中的物体</p> <p markdown="span">厚度以曼哈顿距离计算。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.hollow`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//hollow [thickness] [pattern]`</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">要保留的外壳厚度</td>
</tr>
<tr>
<td markdown="span">`[pattern]`</td>
<td markdown="span">用来替换被掏空部分的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//forest"></a>

`//forest`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">在选区内生成森林</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.forest`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//forest [type] [density]`</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">要种植的树木类型</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">森林密度</td>
</tr>
</tbody>
</table>

<a id="command-//flora"></a>

`//flora`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">在选区内生成植物</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.region.flora`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//flora [density]`</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">森林密度</td>
</tr>
</tbody>
</table>

<a id="command-//update"></a>

`//update`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">对选区应用附带效果</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.update`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//update [sideEffectSet]`</td>
</tr>
<tr>
<td markdown="span">`[sideEffectSet]`</td>
<td markdown="span">要应用的附带效果</td>
</tr>
</tbody>
</table>

## [生成命令](#id5) { #generation-commands }

<a id="command-//hcyl"></a>

`//hcyl`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成空心圆柱。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.cylinder`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//hcyl <pattern> <radii> [height]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要生成的方块模式</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">圆柱半径，第 1 个对应 N/S（南北），第 2 个对应 E/W（东西）</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">圆柱高度</td>
</tr>
</tbody>
</table>

<a id="command-//cyl"></a>

`//cyl`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成圆柱。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.cylinder`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//cyl [-h] <pattern> <radii> [height]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要生成的方块模式</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">圆柱半径，第 1 个对应 N/S（南北），第 2 个对应 E/W（东西）</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">圆柱高度</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">生成空心圆柱</td>
</tr>
</tbody>
</table>

<a id="command-//cone"></a>

`//cone`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成圆锥。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.cone`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//cone [-h] <pattern> <radii> [height] [thickness]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要生成的方块模式</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">圆锥半径，第 1 个对应 N/S（南北），第 2 个对应 E/W（东西）</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">圆锥高度</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">生成空心圆锥</td>
</tr>
<tr>
<td markdown="span">`[thickness]`</td>
<td markdown="span">空心圆锥的厚度</td>
</tr>
</tbody>
</table>

<a id="command-//hsphere"></a>

`//hsphere`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成空心球体。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.sphere`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//hsphere [-r] <pattern> <radii>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要生成的方块模式</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">球体半径，顺序为 N/S（南北）、U/D（上下）、E/W（东西）</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">将球体底部提升到放置位置</td>
</tr>
</tbody>
</table>

<a id="command-//sphere"></a>

`//sphere`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成实心球体。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.sphere`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//sphere [-hr] <pattern> <radii>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要生成的方块模式</td>
</tr>
<tr>
<td markdown="span">`<radii>`</td>
<td markdown="span">球体半径，顺序为 N/S（南北）、U/D（上下）、E/W（东西）</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">将球体底部提升到放置位置</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">生成空心球体</td>
</tr>
</tbody>
</table>

<a id="command-/forestgen"></a>

`/forestgen`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成森林</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.forest`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/forestgen [size] [type] [density]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">森林大小，以方块为单位</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">森林类型</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">森林密度，范围为 0 到 100</td>
</tr>
</tbody>
</table>

<a id="command-/pumpkins"></a>

`/pumpkins`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成南瓜地</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.pumpkins`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/pumpkins [size]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">南瓜地大小</td>
</tr>
</tbody>
</table>

<a id="command-//feature"></a>

`//feature`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成 Minecraft 地物</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.feature`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//feature <feature>`</td>
</tr>
<tr>
<td markdown="span">`<feature>`</td>
<td markdown="span">要生成的地物</td>
</tr>
</tbody>
</table>

<a id="command-//structure"></a>

`//structure`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成 Minecraft 结构</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.structure`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//structure <feature>`</td>
</tr>
<tr>
<td markdown="span">`<feature>`</td>
<td markdown="span">要生成的结构</td>
</tr>
</tbody>
</table>

<a id="command-//hpyramid"></a>

`//hpyramid`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成空心金字塔</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.pyramid`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//hpyramid <pattern> <size>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
<tr>
<td markdown="span">`<size>`</td>
<td markdown="span">金字塔大小</td>
</tr>
</tbody>
</table>

<a id="command-//pyramid"></a>

`//pyramid`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生成实心金字塔</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.pyramid`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//pyramid [-h] <pattern> <size>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
<tr>
<td markdown="span">`<size>`</td>
<td markdown="span">金字塔大小</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">生成空心金字塔</td>
</tr>
</tbody>
</table>

<a id="command-//generate"></a>

`//generate`（或 `//gen`, `//g`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">根据公式生成形状。</p> <p markdown="span">详见 [https://ehub.to/we/expr](https://ehub.to/we/expr)</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.shape`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//generate [-chor] <pattern> <expression...>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
<tr>
<td markdown="span">`<expression...>`</td>
<td markdown="span">用于判断方块放置位置并设置方块类型的表达式</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">生成空心形状</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">使用游戏世界的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">使用放置位置的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">以选区中心为原点</td>
</tr>
</tbody>
</table>

<a id="command-//generatebiome"></a>

`//generatebiome`（或 `//genbiome`, `//gb`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">根据公式设置生物群系。</p> <p markdown="span">详见 [https://ehub.to/we/expr](https://ehub.to/we/expr)</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.generation.shape.biome`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//generatebiome [-chor] <target> <expression...>`</td>
</tr>
<tr>
<td markdown="span">`<target>`</td>
<td markdown="span">要设置的生物群系类型</td>
</tr>
<tr>
<td markdown="span">`<expression...>`</td>
<td markdown="span">用于判断方块放置位置并设置生物群系类型的表达式</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">生成空心形状</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">使用游戏世界的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">使用放置位置的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">以选区中心为原点</td>
</tr>
</tbody>
</table>

## [原理图与剪贴板命令](#id6) { #schematic-and-clipboard-commands }

<a id="command-/schematic"></a>

`/schematic`（或 `/schem`, `//schematic`, `//schem`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">用于保存和加载区域的原理图命令</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.schematic.delete`, `worldedit.schematic.list`, `worldedit.clipboard.load`, `worldedit.schematic.save`, `worldedit.schematic.formats`, `worldedit.schematic.load`, `worldedit.clipboard.save`, `worldedit.clipboard.share`, `worldedit.schematic.share`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic <list|formats|load|delete|save|share>`</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-list"></a>

`/schematic list`（或 `/schematic all`, `/schematic ls`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">列出已保存的原理图</p> <p markdown="span">注意：只有加载时才会完整验证文件格式。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.schematic.list`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic list [-dn] [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">要查看的页码。</td>
</tr>
<tr>
<td markdown="span">`[-d]`</td>
<td markdown="span">按日期排序，最早的在前</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">按日期排序，最新的在前</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-formats"></a>

`/schematic formats`（或 `/schematic listformats`, `/schematic f`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">列出可用格式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.schematic.formats`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic formats`</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-load"></a>

`/schematic load`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将原理图加载到剪贴板</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.load`, `worldedit.schematic.load`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic load <schematic> [format]`</td>
</tr>
<tr>
<td markdown="span">`<schematic>`</td>
<td markdown="span">文件名。</td>
</tr>
<tr>
<td markdown="span">`[format]`</td>
<td markdown="span">格式名称。</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-delete"></a>

`/schematic delete`（或 `/schematic d`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">删除已保存的原理图</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.schematic.delete`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic delete <schematic>`</td>
</tr>
<tr>
<td markdown="span">`<schematic>`</td>
<td markdown="span">文件名。</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-save"></a>

`/schematic save`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将剪贴板保存为原理图文件</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.save`, `worldedit.schematic.save`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic save [-f] <filename> [format]`</td>
</tr>
<tr>
<td markdown="span">`<filename>`</td>
<td markdown="span">文件名。</td>
</tr>
<tr>
<td markdown="span">`[format]`</td>
<td markdown="span">格式名称。</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">覆盖现有文件。</td>
</tr>
</tbody>
</table>

<a id="command-/schematic-share"></a>

`/schematic share`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将剪贴板作为原理图在线分享</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.share`, `worldedit.schematic.share`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/schematic share [schematicName] [destination] [format]`</td>
</tr>
<tr>
<td markdown="span">`[schematicName]`</td>
<td markdown="span">原理图名称，默认为 name-millis</td>
</tr>
<tr>
<td markdown="span">`[destination]`</td>
<td markdown="span">分享目标</td>
</tr>
<tr>
<td markdown="span">`[format]`</td>
<td markdown="span">格式名称</td>
</tr>
</tbody>
</table>

<a id="command-//copy"></a>

`//copy`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将选区复制到剪贴板</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.copy`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//copy [-be] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">同时复制实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时复制生物群系</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">设置包含蒙版，不匹配的方块会变为空气</td>
</tr>
</tbody>
</table>

<a id="command-//cut"></a>

`//cut`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将选区剪切到剪贴板</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.cut`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//cut [-be] [leavePattern] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[leavePattern]`</td>
<td markdown="span">用于填充原选区位置的方块模式</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">同时剪切实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时复制生物群系，原位置的生物群系不变</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">设置排除蒙版，不匹配的方块变为空气</td>
</tr>
</tbody>
</table>

<a id="command-//paste"></a>

`//paste`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">粘贴剪贴板内容</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.paste`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//paste [-abenosv] [-m <sourceMask>]`</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">跳过空气方块</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">包含结构空位方块</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">粘贴到原始位置</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">粘贴后选中该区域</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">不实际粘贴，只选中范围；隐含启用 -s</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">剪贴板有实体时，同时粘贴实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">剪贴板有生物群系时，同时粘贴生物群系</td>
</tr>
<tr>
<td markdown="span">`[-m <sourceMask>]`</td>
<td markdown="span">只粘贴匹配此蒙版的方块</td>
</tr>
</tbody>
</table>

<a id="command-//rotate"></a>

`//rotate`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">旋转剪贴板内容</p> <p markdown="span">以非破坏方式旋转剪贴板内容。角度以度为单位，正角度表示顺时针旋转，多次旋转可以叠加。不会进行插值，因此角度应为 90 度的整数倍。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.rotate`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//rotate <rotateY> [rotateX] [rotateZ]`</td>
</tr>
<tr>
<td markdown="span">`<rotateY>`</td>
<td markdown="span">绕 y 轴旋转的角度</td>
</tr>
<tr>
<td markdown="span">`[rotateX]`</td>
<td markdown="span">绕 x 轴旋转的角度</td>
</tr>
<tr>
<td markdown="span">`[rotateZ]`</td>
<td markdown="span">绕 z 轴旋转的角度</td>
</tr>
</tbody>
</table>

<a id="command-//flip"></a>

`//flip`（或 `//mirror`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">以原点为基准镜像剪贴板内容</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.flip`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//flip [direction]`</td>
</tr>
<tr>
<td markdown="span">`[direction]`</td>
<td markdown="span">镜像方向，默认为视线方向。</td>
</tr>
</tbody>
</table>

<a id="command-/clearclipboard"></a>

`/clearclipboard`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">清空剪贴板</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.clipboard.clear`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/clearclipboard`</td>
</tr>
</tbody>
</table>

<a id="command-//revolve"></a>

`//revolve`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将选区绕垂直轴旋转复制</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.revolve`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//revolve [-ber] <pasteCount> [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`<pasteCount>`</td>
<td markdown="span">粘贴次数</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">设置来源蒙版，不匹配的方块不参与旋转复制</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">反向旋转复制，即逆时针</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">复制实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">复制生物群系</td>
</tr>
</tbody>
</table>

## [工具命令](#id7) { #tool-commands }

<a id="command-/tool"></a>

`/tool`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">为手持物品绑定工具</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool <cycler|repl|farwand|floodfill|deltree|stacker|selwand|tree|none|info|lrbuild|navwand>`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-cycler"></a>

`/tool cycler`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块数据循环切换工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.data-cycler`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool cycler`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-repl"></a>

`/tool repl`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块替换工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.replacer`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool repl <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要放置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-/tool-farwand"></a>

`/tool farwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">远程选区工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.farwand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool farwand`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-floodfill"></a>

`/tool floodfill`（或 `/tool flood`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">泛洪填充工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.flood-fill`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool floodfill <pattern> <range>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">用于泛洪填充的方块模式</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">填充范围</td>
</tr>
</tbody>
</table>

<a id="command-/tool-deltree"></a>

`/tool deltree`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">悬空树木移除工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.deltree`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool deltree`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-stacker"></a>

`/tool stacker`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块堆叠工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.stack`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool stacker [range] [mask]`</td>
</tr>
<tr>
<td markdown="span">`[range]`</td>
<td markdown="span">堆叠的最大范围</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">堆叠停止条件的蒙版</td>
</tr>
</tbody>
</table>

<a id="command-/tool-selwand"></a>

`/tool selwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选区工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool selwand`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-tree"></a>

`/tool tree`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">树木生成工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.tree`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool tree [type]`</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">要生成的树木类型</td>
</tr>
</tbody>
</table>

<a id="command-/tool-none"></a>

`/tool none`（或 `/tool unbind`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">解除当前物品绑定的工具</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool none`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-info"></a>

`/tool info`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块信息工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.info`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool info`</td>
</tr>
</tbody>
</table>

<a id="command-/tool-lrbuild"></a>

`/tool lrbuild`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">远距离建造工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.lrbuild`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool lrbuild <primary> <secondary>`</td>
</tr>
<tr>
<td markdown="span">`<primary>`</td>
<td markdown="span">左键点击时使用的方块模式</td>
</tr>
<tr>
<td markdown="span">`<secondary>`</td>
<td markdown="span">右键点击时使用的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-/tool-navwand"></a>

`/tool navwand`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">导航工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tool navwand`</td>
</tr>
</tbody>
</table>

<a id="command-/none"></a>

`/none`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool none`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">解除当前物品绑定的工具</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/none`</td>
</tr>
</tbody>
</table>

<a id="command-/selwand"></a>

`/selwand`（或 `//selwand`）

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool selwand`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选区工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/selwand`</td>
</tr>
</tbody>
</table>

<a id="command-/navwand"></a>

`/navwand`（或 `//navwand`）

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool navwand`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">导航工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.setwand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/navwand`</td>
</tr>
</tbody>
</table>

<a id="command-/info"></a>

`/info`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool info`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块信息工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.info`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/info`</td>
</tr>
</tbody>
</table>

<a id="command-/tree"></a>

`/tree`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool tree`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">树木生成工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.tree`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tree [type]`</td>
</tr>
<tr>
<td markdown="span">`[type]`</td>
<td markdown="span">要生成的树木类型</td>
</tr>
</tbody>
</table>

<a id="command-/repl"></a>

`/repl`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool repl`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块替换工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.replacer`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/repl <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要放置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-/cycler"></a>

`/cycler`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool cycler`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">方块数据循环切换工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.data-cycler`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/cycler`</td>
</tr>
</tbody>
</table>

<a id="command-/floodfill"></a>

`/floodfill`（或 `/flood`）

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool floodfill`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">泛洪填充工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.flood-fill`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/floodfill <pattern> <range>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">用于泛洪填充的方块模式</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">填充范围</td>
</tr>
</tbody>
</table>

<a id="command-/deltree"></a>

`/deltree`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool deltree`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">悬空树木移除工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.deltree`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/deltree`</td>
</tr>
</tbody>
</table>

<a id="command-/farwand"></a>

`/farwand`

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool farwand`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">远程选区工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.farwand`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/farwand`</td>
</tr>
</tbody>
</table>

<a id="command-/lrbuild"></a>

`/lrbuild`（或 `//lrbuild`）

!!! warning "警告"

    此命令已弃用。全局工具命令名容易产生冲突，将在 WorldEdit 8 中移除。

    请改用 `/tool lrbuild`。

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">远距离建造工具</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.tool.lrbuild`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/lrbuild <primary> <secondary>`</td>
</tr>
<tr>
<td markdown="span">`<primary>`</td>
<td markdown="span">左键点击时使用的方块模式</td>
</tr>
<tr>
<td markdown="span">`<secondary>`</td>
<td markdown="span">右键点击时使用的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-//"></a>

`//`（或 `/,`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">切换超级镐功能</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`// [superPickaxe]`</td>
</tr>
<tr>
<td markdown="span">`[superPickaxe]`</td>
<td markdown="span">超级镐的新状态</td>
</tr>
</tbody>
</table>

<a id="command-/mask"></a>

`/mask`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置笔刷蒙版</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.options.mask`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/mask [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">要设置的蒙版</td>
</tr>
</tbody>
</table>

<a id="command-/material"></a>

`/material`（或 `//material`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置笔刷材料</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.options.material`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/material <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要使用的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-/range"></a>

`/range`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置笔刷作用距离</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.options.range`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/range <range>`</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">笔刷作用距离</td>
</tr>
</tbody>
</table>

<a id="command-/size"></a>

`/size`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置笔刷大小</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.options.size`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/size <size>`</td>
</tr>
<tr>
<td markdown="span">`<size>`</td>
<td markdown="span">笔刷大小</td>
</tr>
</tbody>
</table>

<a id="command-/tracemask"></a>

`/tracemask`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置用于终止工具射线检测的蒙版</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.options.tracemask`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/tracemask [mask]`</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">要设置的射线检测蒙版</td>
</tr>
</tbody>
</table>

## [超级镐命令](#id8) { #super-pickaxe-commands }

<a id="command-/superpickaxe"></a>

`/superpickaxe`（或 `/pickaxe`, `/sp`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">超级镐命令</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.superpickaxe.area`, `worldedit.superpickaxe.recursive`, `worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/superpickaxe <single|area|recursive>`</td>
</tr>
</tbody>
</table>

<a id="command-/superpickaxe-single"></a>

`/superpickaxe single`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">启用超级镐的单方块模式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.superpickaxe`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/superpickaxe single`</td>
</tr>
</tbody>
</table>

<a id="command-/superpickaxe-area"></a>

`/superpickaxe area`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">启用超级镐的范围模式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.superpickaxe.area`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/superpickaxe area <range>`</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">范围超级镐的作用范围</td>
</tr>
</tbody>
</table>

<a id="command-/superpickaxe-recursive"></a>

`/superpickaxe recursive`（或 `/superpickaxe recur`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">启用超级镐的递归模式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.superpickaxe.recursive`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/superpickaxe recursive <range>`</td>
</tr>
<tr>
<td markdown="span">`<range>`</td>
<td markdown="span">递归超级镐的作用范围</td>
</tr>
</tbody>
</table>

## [笔刷命令](#id9) { #brush-commands }

<a id="command-/brush"></a>

`/brush`（或 `/br`, `//brush`, `//br`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">笔刷命令</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush <forest|splatter|butcher|paint|none|clipboard|snowsmooth|gravity|heightmap|extinguish|feature|sphere|raise|smooth|cylinder|set|apply|deform|lower|erode|dilate|snow|biome|morph>`</td>
</tr>
</tbody>
</table>

<a id="command-/brush-forest"></a>

`/brush forest`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">森林笔刷，在范围内创建森林</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.forest`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush forest <shape> [radius] [density] <type>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">笔刷密度</td>
</tr>
<tr>
<td markdown="span">`<type>`</td>
<td markdown="span">要使用的树木类型</td>
</tr>
</tbody>
</table>

<a id="command-/brush-splatter"></a>

`/brush splatter`（或 `/brush splat`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择飞溅笔刷</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.splatter`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush splatter <pattern> [radius] [decay]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">飞溅半径</td>
</tr>
<tr>
<td markdown="span">`[decay]`</td>
<td markdown="span">飞溅衰减值，范围为 0 到 10</td>
</tr>
</tbody>
</table>

<a id="command-/brush-butcher"></a>

`/brush butcher`（或 `/brush kill`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">屠宰笔刷，杀死指定半径内的生物</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.butcher`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush butcher [-abfgnprtw] [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">杀死生物的范围半径</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">同时杀死宠物</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">同时杀死 NPC</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">同时杀死傀儡</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">同时杀死动物</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时杀死环境生物</td>
</tr>
<tr>
<td markdown="span">`[-t]`</td>
<td markdown="span">同时杀死使用命名牌命名的生物</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">同时杀死所有友好生物，等同于应用 -abgnpt 选项</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">同时破坏盔甲架</td>
</tr>
<tr>
<td markdown="span">`[-w]`</td>
<td markdown="span">同时杀死水生生物</td>
</tr>
</tbody>
</table>

<a id="command-/brush-paint"></a>

`/brush paint`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">绘制笔刷，对表面应用函数</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.paint`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush paint <shape> [radius] [density] <forest|item|set>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">笔刷密度</td>
</tr>
</tbody>
</table>

<a id="command-/brush-none"></a>

`/brush none`（或 `/brush unbind`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">解除当前物品绑定的笔刷</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush none`</td>
</tr>
</tbody>
</table>

<a id="command-/brush-clipboard"></a>

`/brush clipboard`（或 `/brush copy`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择剪贴板笔刷</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.clipboard`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush clipboard [-abeov] [-m <sourceMask>]`</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">不粘贴剪贴板中的空气</td>
</tr>
<tr>
<td markdown="span">`[-v]`</td>
<td markdown="span">包含结构空位方块</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">以目标位置为粘贴起点，而不是让粘贴内容以它为中心</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">剪贴板有实体时，同时粘贴实体</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">剪贴板有生物群系时，同时粘贴生物群系</td>
</tr>
<tr>
<td markdown="span">`[-m <sourceMask>]`</td>
<td markdown="span">跳过剪贴板中匹配此蒙版的方块</td>
</tr>
</tbody>
</table>

<a id="command-/brush-snowsmooth"></a>

`/brush snowsmooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">选择积雪地形平滑笔刷</p> <p markdown="span">示例：‘/brush snowsmooth 5 1 -l 3’</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.snowsmooth`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush snowsmooth [radius] [iterations] [-l <snowBlockCount>] [-m <mask>]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">平滑时的采样半径</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span">迭代次数</td>
</tr>
<tr>
<td markdown="span">`[-l <snowBlockCount>]`</td>
<td markdown="span">雪层下方的雪块数量</td>
</tr>
<tr>
<td markdown="span">`[-m <mask>]`</td>
<td markdown="span">用于确定高度图的方块蒙版</td>
</tr>
</tbody>
</table>

<a id="command-/brush-gravity"></a>

`/brush gravity`（或 `/brush grav`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">重力笔刷，模拟重力效果</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.gravity`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush gravity [radius] [-h <height>]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">应用重力效果的半径</td>
</tr>
<tr>
<td markdown="span">`[-h <height>]`</td>
<td markdown="span">改为影响指定高度范围内上下两侧的方块，而不是使用目标位置的 Y + radius</td>
</tr>
</tbody>
</table>

<a id="command-/brush-heightmap"></a>

`/brush heightmap`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">高度图笔刷，使用图片高度图升高或降低地形</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.heightmap`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush heightmap [-efr] <imageName> [radius] [intensity]`</td>
</tr>
<tr>
<td markdown="span">`<imageName>`</td>
<td markdown="span">图片名称</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[intensity]`</td>
<td markdown="span">笔刷强度</td>
</tr>
<tr>
<td markdown="span">`[-e]`</td>
<td markdown="span">删除方块，而非填充方块</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">不修改所选高度上方的方块</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">对笔刷高度加入少量随机变化。</td>
</tr>
</tbody>
</table>

<a id="command-/brush-extinguish"></a>

`/brush extinguish`（或 `/brush ex`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">灭火笔刷的快捷形式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.ex`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush extinguish [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">灭火半径</td>
</tr>
</tbody>
</table>

<a id="command-/brush-feature"></a>

`/brush feature`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">地物笔刷，绘制 Minecraft 世界生成地物</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.feature`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush feature <shape> [radius] [density] <type>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[density]`</td>
<td markdown="span">笔刷密度</td>
</tr>
<tr>
<td markdown="span">`<type>`</td>
<td markdown="span">要使用的地物类型</td>
</tr>
</tbody>
</table>

<a id="command-/brush-sphere"></a>

`/brush sphere`（或 `/brush s`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择球体笔刷</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.sphere`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush sphere [-h] <pattern> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">球体半径</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">改为创建空心球体</td>
</tr>
</tbody>
</table>

<a id="command-/brush-raise"></a>

`/brush raise`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">升高笔刷，将所有方块升高一格</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.raise`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush raise <shape> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
</tbody>
</table>

<a id="command-/brush-smooth"></a>

`/brush smooth`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">选择地形平滑笔刷</p> <p markdown="span">示例：‘/brush smooth 2 4 grass_block,dirt,stone’</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.smooth`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush smooth [radius] [iterations] [mask]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">平滑时的采样半径</td>
</tr>
<tr>
<td markdown="span">`[iterations]`</td>
<td markdown="span">迭代次数</td>
</tr>
<tr>
<td markdown="span">`[mask]`</td>
<td markdown="span">用于确定高度图的方块蒙版</td>
</tr>
</tbody>
</table>

<a id="command-/brush-cylinder"></a>

`/brush cylinder`（或 `/brush cyl`, `/brush c`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择圆柱笔刷</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.cylinder`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush cylinder [-h] <pattern> [radius] [height]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">圆柱半径</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">圆柱高度</td>
</tr>
<tr>
<td markdown="span">`[-h]`</td>
<td markdown="span">改为创建空心圆柱</td>
</tr>
</tbody>
</table>

<a id="command-/brush-set"></a>

`/brush set`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">设置笔刷，设置范围内的全部方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.set`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush set <shape> [radius] <pattern>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">要设置的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-/brush-apply"></a>

`/brush apply`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">应用笔刷，对每个方块应用函数</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.apply`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush apply <shape> [radius] <forest|item|set>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
</tbody>
</table>

<a id="command-/brush-deform"></a>

`/brush deform`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">变形笔刷，对范围应用表达式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.deform`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush deform [-or] <shape> [radius] [expression]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[expression]`</td>
<td markdown="span">要应用的表达式</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">使用游戏世界的坐标原点</td>
</tr>
<tr>
<td markdown="span">`[-o]`</td>
<td markdown="span">以放置位置为原点</td>
</tr>
</tbody>
</table>

<a id="command-/brush-lower"></a>

`/brush lower`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">降低笔刷，将所有方块降低一格</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.lower`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush lower <shape> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
</tbody>
</table>

<a id="command-/brush-erode"></a>

`/brush erode`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">形态笔刷的侵蚀预设，侵蚀范围内的方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush erode [brushSize]`</td>
</tr>
<tr>
<td markdown="span">`[brushSize]`</td>
<td markdown="span">笔刷大小</td>
</tr>
</tbody>
</table>

<a id="command-/brush-dilate"></a>

`/brush dilate`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">形态笔刷的膨胀预设，膨胀范围内的方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush dilate [brushSize]`</td>
</tr>
<tr>
<td markdown="span">`[brushSize]`</td>
<td markdown="span">笔刷大小</td>
</tr>
</tbody>
</table>

<a id="command-/brush-snow"></a>

`/brush snow`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">积雪笔刷，在范围内设置雪</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.snow`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush snow [-s] <shape> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">是否堆叠积雪</td>
</tr>
</tbody>
</table>

<a id="command-/brush-biome"></a>

`/brush biome`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">生物群系笔刷，设置范围内的生物群系</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.biome`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush biome [-c] <shape> [radius] <biomeType>`</td>
</tr>
<tr>
<td markdown="span">`<shape>`</td>
<td markdown="span">区域形状</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`<biomeType>`</td>
<td markdown="span">生物群系类型</td>
</tr>
<tr>
<td markdown="span">`[-c]`</td>
<td markdown="span">是否设置整个垂直列</td>
</tr>
</tbody>
</table>

<a id="command-/brush-morph"></a>

`/brush morph`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">形态笔刷，改变范围内的方块形态</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.brush.morph`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/brush morph [brushSize] [minErodeFaces] [numErodeIterations] [minDilateFaces] [numDilateIterations]`</td>
</tr>
<tr>
<td markdown="span">`[brushSize]`</td>
<td markdown="span">笔刷大小</td>
</tr>
<tr>
<td markdown="span">`[minErodeFaces]`</td>
<td markdown="span">触发侵蚀的最小暴露面数</td>
</tr>
<tr>
<td markdown="span">`[numErodeIterations]`</td>
<td markdown="span">侵蚀迭代次数</td>
</tr>
<tr>
<td markdown="span">`[minDilateFaces]`</td>
<td markdown="span">触发膨胀的最小面数</td>
</tr>
<tr>
<td markdown="span">`[numDilateIterations]`</td>
<td markdown="span">膨胀迭代次数</td>
</tr>
</tbody>
</table>

## [生物群系命令](#id10) { #biome-commands }

<a id="command-/biomelist"></a>

`/biomelist`（或 `/biomels`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">列出所有可用生物群系。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.biome.list`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/biomelist [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">页码。</td>
</tr>
</tbody>
</table>

<a id="command-/biomeinfo"></a>

`/biomeinfo`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">获取目标方块的生物群系。</p> <p markdown="span">默认使用选区内的全部方块。</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.biome.info`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/biomeinfo [-pt]`</td>
</tr>
<tr>
<td markdown="span">`[-t]`</td>
<td markdown="span">使用准星指向的方块。</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">使用当前所在的方块。</td>
</tr>
</tbody>
</table>

<a id="command-//setbiome"></a>

`//setbiome`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">设置当前方块或选区的生物群系。</p> <p markdown="span">默认使用选区内的全部方块</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.biome.set`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//setbiome [-p] <target>`</td>
</tr>
<tr>
<td markdown="span">`<target>`</td>
<td markdown="span">生物群系类型。</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">使用当前位置</td>
</tr>
</tbody>
</table>

<a id="command-//replacebiome"></a>

`//replacebiome`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="block">

<p markdown="span">替换当前方块或选区的生物群系。</p> <p markdown="span">默认使用选区内的全部方块</p>

</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.biome.set`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//replacebiome [-p] <from> <target>`</td>
</tr>
<tr>
<td markdown="span">`<from>`</td>
<td markdown="span">指定替换生物群系位置的蒙版</td>
</tr>
<tr>
<td markdown="span">`<target>`</td>
<td markdown="span">要设置的生物群系类型</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">使用当前位置</td>
</tr>
</tbody>
</table>

## [区块命令](#id11) { #chunk-commands }

<a id="command-/chunkinfo"></a>

`/chunkinfo`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">获取当前所在区块的信息</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.chunkinfo`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/chunkinfo`</td>
</tr>
</tbody>
</table>

<a id="command-/listchunks"></a>

`/listchunks`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">列出选区包含的区块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.listchunks`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/listchunks [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">页码。</td>
</tr>
</tbody>
</table>

<a id="command-/delchunks"></a>

`/delchunks`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">删除选区包含的区块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.delchunks`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/delchunks [-o <beforeTime>]`</td>
</tr>
<tr>
<td markdown="span">`[-o <beforeTime>]`</td>
<td markdown="span">只删除早于指定时间的区块。</td>
</tr>
</tbody>
</table>

## [快照命令](#id12) { #snapshot-commands }

<a id="command-/restore"></a>

`/restore`（或 `//restore`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">从备份快照恢复选区</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/restore [snapshot]`</td>
</tr>
<tr>
<td markdown="span">`[snapshot]`</td>
<td markdown="span">要恢复的快照</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot"></a>

`/snapshot`（或 `/snap`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">用于从备份恢复的快照命令</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.restore`, `worldedit.snapshots.list`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snapshot <before|use|sel|after|list>`</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-before"></a>

`/snapshot before`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择指定日期之前最近的快照</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snapshot before <date>`</td>
</tr>
<tr>
<td markdown="span">`<date>`</td>
<td markdown="span">允许使用的最早日期</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-use"></a>

`/snapshot use`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择要使用的快照</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snapshot use <name>`</td>
</tr>
<tr>
<td markdown="span">`<name>`</td>
<td markdown="span">要使用的快照</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-sel"></a>

`/snapshot sel`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">按列表 ID 选择快照</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snapshot sel <index>`</td>
</tr>
<tr>
<td markdown="span">`<index>`</td>
<td markdown="span">要选择的列表 ID</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-after"></a>

`/snapshot after`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">选择指定日期之后最近的快照</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.restore`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snapshot after <date>`</td>
</tr>
<tr>
<td markdown="span">`<date>`</td>
<td markdown="span">允许使用的最早日期</td>
</tr>
</tbody>
</table>

<a id="command-/snapshot-list"></a>

`/snapshot list`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">列出快照</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snapshots.list`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snapshot list [-p <page>]`</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">返回结果的页码</td>
</tr>
</tbody>
</table>

## [脚本命令](#id13) { #scripting-commands }

<a id="command-/cs"></a>

`/cs`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">执行 CraftScript</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.scripting.execute`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/cs <filename> [args...]`</td>
</tr>
<tr>
<td markdown="span">`<filename>`</td>
<td markdown="span">要加载的 CraftScript 文件名</td>
</tr>
<tr>
<td markdown="span">`[args...]`</td>
<td markdown="span">传给 CraftScript 的参数</td>
</tr>
</tbody>
</table>

<a id="command-/.s"></a>

`/.s`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">执行上一次的 CraftScript</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.scripting.execute`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/.s [args...]`</td>
</tr>
<tr>
<td markdown="span">`[args...]`</td>
<td markdown="span">传给 CraftScript 的参数</td>
</tr>
</tbody>
</table>

## [实用命令](#id14) { #utility-commands }

<a id="command-//fill"></a>

`//fill`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">填充洞穴</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.fill`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//fill <pattern> <radius> [depth]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">用于填充的方块</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">填充半径</td>
</tr>
<tr>
<td markdown="span">`[depth]`</td>
<td markdown="span">填充深度</td>
</tr>
</tbody>
</table>

<a id="command-//fillr"></a>

`//fillr`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">递归填充洞穴</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.fill.recursive`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//fillr <pattern> <radius> [depth]`</td>
</tr>
<tr>
<td markdown="span">`<pattern>`</td>
<td markdown="span">用于填充的方块</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">填充半径</td>
</tr>
<tr>
<td markdown="span">`[depth]`</td>
<td markdown="span">填充深度</td>
</tr>
</tbody>
</table>

<a id="command-//drain"></a>

`//drain`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">排空水池</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.drain`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//drain [-w] <radius>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">排水半径</td>
</tr>
<tr>
<td markdown="span">`[-w]`</td>
<td markdown="span">同时移除方块中的含水状态</td>
</tr>
</tbody>
</table>

<a id="command-/fixlava"></a>

`/fixlava`（或 `//fixlava`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将岩浆修复为静止状态</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.fixlava`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/fixlava <radius>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">修复半径</td>
</tr>
</tbody>
</table>

<a id="command-/fixwater"></a>

`/fixwater`（或 `//fixwater`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将水修复为静止状态</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.fixwater`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/fixwater <radius>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">修复半径</td>
</tr>
</tbody>
</table>

<a id="command-/removeabove"></a>

`/removeabove`（或 `//removeabove`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">移除头顶上方的方块。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.removeabove`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/removeabove [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">清除方形范围的边心距</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">头顶上方的最大清除高度</td>
</tr>
</tbody>
</table>

<a id="command-/removebelow"></a>

`/removebelow`（或 `//removebelow`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">移除脚下的方块。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.removebelow`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/removebelow [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">清除方形范围的边心距</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">脚下的最大清除高度</td>
</tr>
</tbody>
</table>

<a id="command-/removenear"></a>

`/removenear`（或 `//removenear`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">移除附近的方块。</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.removenear`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/removenear <mask> [radius]`</td>
</tr>
<tr>
<td markdown="span">`<mask>`</td>
<td markdown="span">要移除的方块蒙版</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">清除方形范围的半径</td>
</tr>
</tbody>
</table>

<a id="command-/replacenear"></a>

`/replacenear`（或 `//replacenear`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">替换附近的方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.replacenear`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/replacenear <radius> [from] <to>`</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">执行移除的方形范围半径</td>
</tr>
<tr>
<td markdown="span">`[from]`</td>
<td markdown="span">匹配要移除方块的蒙版</td>
</tr>
<tr>
<td markdown="span">`<to>`</td>
<td markdown="span">替换后使用的方块模式</td>
</tr>
</tbody>
</table>

<a id="command-/snow"></a>

`/snow`（或 `//snow`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">模拟降雪</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.snow`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/snow [-s] [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">降雪圆柱范围的半径</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">降雪圆柱范围的高度</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">堆叠雪层</td>
</tr>
</tbody>
</table>

<a id="command-/thaw"></a>

`/thaw`（或 `//thaw`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">使范围内的冰雪融化</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.thaw`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/thaw [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">融化圆柱范围的半径</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">融化圆柱范围的高度</td>
</tr>
</tbody>
</table>

<a id="command-/green"></a>

`/green`（或 `//green`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">将范围内的泥土转换为草方块</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.green`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/green [-f] [size] [height]`</td>
</tr>
<tr>
<td markdown="span">`[size]`</td>
<td markdown="span">转换圆柱范围的半径</td>
</tr>
<tr>
<td markdown="span">`[height]`</td>
<td markdown="span">转换圆柱范围的高度</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">同时转换砂土</td>
</tr>
</tbody>
</table>

<a id="command-/extinguish"></a>

`/extinguish`（或 `//ex`, `//ext`, `//extinguish`, `/ex`, `/ext`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">扑灭附近的火焰</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.extinguish`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/extinguish [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">执行移除的方形范围半径</td>
</tr>
</tbody>
</table>

<a id="command-/butcher"></a>

`/butcher`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">杀死全部或附近的生物</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.butcher`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/butcher [-abfgnprtw] [radius]`</td>
</tr>
<tr>
<td markdown="span">`[radius]`</td>
<td markdown="span">杀死生物的范围半径</td>
</tr>
<tr>
<td markdown="span">`[-p]`</td>
<td markdown="span">同时杀死宠物</td>
</tr>
<tr>
<td markdown="span">`[-n]`</td>
<td markdown="span">同时杀死 NPC</td>
</tr>
<tr>
<td markdown="span">`[-g]`</td>
<td markdown="span">同时杀死傀儡</td>
</tr>
<tr>
<td markdown="span">`[-a]`</td>
<td markdown="span">同时杀死动物</td>
</tr>
<tr>
<td markdown="span">`[-b]`</td>
<td markdown="span">同时杀死环境生物</td>
</tr>
<tr>
<td markdown="span">`[-t]`</td>
<td markdown="span">同时杀死使用命名牌命名的生物</td>
</tr>
<tr>
<td markdown="span">`[-f]`</td>
<td markdown="span">同时杀死所有友好生物，等同于应用 -abgnpt 选项</td>
</tr>
<tr>
<td markdown="span">`[-r]`</td>
<td markdown="span">同时破坏盔甲架</td>
</tr>
<tr>
<td markdown="span">`[-w]`</td>
<td markdown="span">同时杀死水生生物</td>
</tr>
</tbody>
</table>

<a id="command-/remove"></a>

`/remove`（或 `/rem`, `/rement`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">移除指定类型的全部实体</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.remove`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`/remove <remover> <radius>`</td>
</tr>
<tr>
<td markdown="span">`<remover>`</td>
<td markdown="span">要移除的实体类型</td>
</tr>
<tr>
<td markdown="span">`<radius>`</td>
<td markdown="span">移除范围的长方体半径</td>
</tr>
</tbody>
</table>

<a id="command-//calculate"></a>

`//calculate`（或 `//calc`, `//eval`, `//evaluate`, `//solve`）

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">计算数学表达式</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.calc`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//calculate <input...>`</td>
</tr>
<tr>
<td markdown="span">`<input...>`</td>
<td markdown="span">要计算的表达式</td>
</tr>
</tbody>
</table>

<a id="command-//help"></a>

`//help`

<table>
<colgroup>
</colgroup>
<tbody>
<tr>
<td markdown="span">**说明**</td>
<td markdown="span">显示 WorldEdit 命令帮助</td>
</tr>
<tr>
<td markdown="span">**权限**</td>
<td markdown="span">`worldedit.help`</td>
</tr>
<tr>
<td markdown="span">**用法**</td>
<td markdown="span">`//help [-s] [-p <page>] [command...]`</td>
</tr>
<tr>
<td markdown="span">`[-s]`</td>
<td markdown="span">列出指定命令的子命令，如果该命令存在子命令</td>
</tr>
<tr>
<td markdown="span">`[-p <page>]`</td>
<td markdown="span">要获取的页码</td>
</tr>
<tr>
<td markdown="span">`[command...]`</td>
<td markdown="span">要查看帮助的命令</td>
</tr>
</tbody>
</table>
