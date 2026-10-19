---
title: 定时任务（Schedules.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/Schedules.yml
---

# 定时任务（Schedules.yml）

文件：`plugins/CMI/Settings/Schedules.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `GiveDiamonds`

定时任务文件，可设置固定间隔或指定时间执行的命令<br>
Enabled：（true/false）只运行已启用的定时任务

```text
  有两种类型：按固定秒数间隔执行，或在指定时间执行
```

Delay：（数字）两次执行的间隔；600 表示每 10 分钟执行一次<br>
Randomize：（true/false）每次随机选择一条命令，全部用完前不重复，适合循环随机公告<br>
DuplicateRandomize：（true/false）每次随机选择一条命令，允许重复，适合循环随机公告<br>
SingleLinear：（true/false）每次按顺序执行一条，全部执行完前不重复，适合必须依次显示的内容<br>
PerformOn：指定执行时间，先填写条目名称，再设置时间范围

```text
  可用字段为 Month、Day、Hour、Minute、Second，均使用数字，小时采用 24 小时制
  示例
  PerformOn:
    FirstTimeFrame:
      Hour: 4
    SecondTimeFrame:
      Hour: 22
      Minute: 30
  可用星期名称指定执行日期，例如 - Day: Monday
  可用 FirstMonthDay 或 LastMonthDay 指定在每月的哪一天执行
  此示例在凌晨 4 点和 22:30 执行，适合在在线人数较少时备份服务器
```

Repeat：（true/false）设为 false，只执行一次；否则按间隔或指定时间持续重复执行<br>
MinPlayers：（人数）执行命令所需的最低在线人数<br>
MinPlayersCommands：在线人数低于要求时执行的命令列表<br>
MaxPlayers：（人数）在线人数高于此值时跳过任务<br>
Feedback：（true/false）设为 false，人数不足而跳过任务时，不在控制台提示<br>
DontTranslatePlaceholders：（true/false）设为 true，命令交给后续处理前，不预先解析其中占位符

```text
  默认 false，会提前解析占位符
  例外是 delay! 特殊指令参数，其中占位符始终提前解析
```

Commands：到达指定时间时执行的命令列表

```text
  同一行可写多条命令，使用 ;; 分隔，例如 command1;;command2;;command3
  以 msg! 开头并填写玩家名称时，向该在线玩家发送普通消息
  以 broadcast! 开头时，向服务器所有人发送普通广播
  以 actionbar! 开头时，向所有玩家发送后面的动作栏消息
  以 title! 开头时，向所有玩家发送后面的标题
  以 subtitle! 开头时，向所有玩家发送后面的副标题
  以 kickall! 开头时，用指定原因踢出全部玩家，适合停服前使用
  以 perm:[permissionNode]! 开头时，只在玩家有权限时执行；无法确定目标玩家时不生效。例如 perm:cmi.announce.vip! broadcast! Hello vip guys
  以 moneycost:[amount]! 开头时，只在玩家余额足够时执行
  以 expcost:[amount]! 开头时，只在玩家经验足够时执行
  以 allPlayers! 开头时，对所有在线玩家执行。命令本身需要包含 [allPlayers]，指定玩家名称插入位置
  插入 'delay! 5'，可在任务触发 5 秒后执行后续命令，适合停服倒计时等，见示例
  [randomPlayer] 选择随机在线玩家，排除拥有 cmi.scheduler.exclude 权限者。例如 - cmi give [randomPlayer] diamond %rand/1-5% 向随机玩家发放 1 到 5 颗钻石
```

支持 PlaceholderAPI 变量<br>
特殊指令详细说明见 https://www.zrips.net/cmi/commands/specialized/
