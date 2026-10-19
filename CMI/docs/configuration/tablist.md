---
title: TAB 列表（TabList.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/TabList.yml
---

# TAB 列表（TabList.yml）

文件：`plugins/CMI/Settings/TabList.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `TabList`

要关闭 Tab 列表处理，请到 Modules.yml 设置

### `TabList.Async`

是否异步更新 Tab 列表<br>
启用可提高整体性能，但部分插件可能无法正常处理异步占位符请求

### `TabList.GroupedEnabled`

开启或关闭分组 Tab 列表格式<br>
不使用分组格式时，关闭可节省资源<br>
关闭后，只使用默认格式，不再检查自定义格式，以节省资源

### `TabList.Updates.AutoInterval`

每隔 X 秒自动更新所有在线玩家的 Tab 列表<br>
页眉页脚为静态内容时，可设为 -1 关闭自动更新<br>
只在玩家事件发生时更新已足够的话，也可设为 -1

### `TabList.addTabListHeader`

设为 false，不添加 Tab 页眉

### `TabList.addTabListFooter`

设为 false，不添加 Tab 页脚

### `TabList.GeneralFormat`

支持 PlaceholderAPI 自定义变量<br>
CMI 也能自行解析部分占位符，无需 PlaceholderAPI<br>
完整列表可在游戏内执行 /cmi placeholders 查看

### `TabList.GeneralFormat.PlayerName`

其他玩家在 Tab 列表中看到的玩家名称格式

### `TabList.useGeneralHeader`

设为 true，GroupFormat 未指定 PlayerName、Header 或 Footer 时，回退到 GeneralFormat 默认值

### `TabList.GroupFormat`

玩家自定义格式<br>
拥有 cmi.tablist.\[number\] 权限的玩家使用对应分组格式<br>
ID 必须是数字，拥有多个匹配权限时使用较大的 ID<br>
递增编号即可添加任意数量的组

### `TabList.Sorting.Enabled`

仅适用于 1.19.3+：开启或关闭 Tab 排序，按指定条件排列

### `TabList.Sorting.Order`

玩家排序条件的先后顺序<br>
可用值：Weight、Group、Name、NickName、Balance、World<br>
可添加 ASC 或 DESC 指定某项的顺序，例如 'Weight-DESC'<br>
Weight 取玩家 cmi.tablistweight.\[value\] 权限中的最大值，例如 cmi.tablistweight.5<br>
排序与页眉或页脚同时更新
