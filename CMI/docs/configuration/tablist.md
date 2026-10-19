---
title: TAB 列表（TabList.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/TabList.yml
---

# TAB 列表（TabList.yml）

文件：`plugins/CMI/Settings/TabList.yml`

## `TabList` { #tablist }

```yaml title="TabList.yml · TabList"
# 要关闭 Tab 列表处理，请到 Modules.yml 设置
TabList:
  # 是否异步更新 Tab 列表
  # 启用可提高整体性能，但部分插件可能无法正常处理异步占位符请求
  Async: true
  UpdateTabListNames: true
  # 开启或关闭分组 Tab 列表格式
  # 不使用分组格式时，关闭可节省资源
  # 关闭后，只使用默认格式，不再检查自定义格式，以节省资源
  GroupedEnabled: true
  Updates:
    # 每隔 X 秒自动更新所有在线玩家的 Tab 列表
    # 页眉页脚为静态内容时，可设为 -1 关闭自动更新
    # 只在玩家事件发生时更新已足够的话，也可设为 -1
    AutoInterval: 60
    OnJoin: true
    OnLeave: true
    afkStateChange: true
    OnWorldChange: true
    OnDeath: false
    OnTeleport: false
    OnNickChange: true
  # 设为 false，不添加 Tab 页眉
  addTabListHeader: true
  # 设为 false，不添加 Tab 页脚
  addTabListFooter: true
  # 支持 PlaceholderAPI 自定义变量
  # CMI 也能自行解析部分占位符，无需 PlaceholderAPI
  # 完整列表可在游戏内执行 /cmi placeholders 查看
  GeneralFormat:
    # 其他玩家在 Tab 列表中看到的玩家名称格式
    PlayerName: '[playerDisplayName]'
    Header:
      '1':
      - '&f------------------------------------'
      - "&7欢迎"
      - "&7在线人数 &f%server_online%&7/&f%server_max_players%"
      - '&f------------------------------------'
    Footer:
      '1':
      - '&f------------------------------------'
      - '&7%player_world% &f%player_x%:&7%player_y%:&f%player_z%'
      - "&7金钱：&f%vault_eco_balance_formatted% &7时间：&f%server_time_HH:mm:ss%"
      - '&f------------------------------------'
  useGeneralName: false
  # 设为 true，GroupFormat 未指定 PlayerName、Header 或 Footer 时，回退到 GeneralFormat 默认值
  useGeneralHeader: false
  useGeneralFooter: false
  # 玩家自定义格式
  # 拥有 cmi.tablist.[number] 权限的玩家使用对应分组格式
  # ID 必须是数字，拥有多个匹配权限时使用较大的 ID
  # 递增编号即可添加任意数量的组
  GroupFormat:
    '1':
      PlayerName: '&2{&r[playerDisplayName]&2}'
      Header:
        '1':
        - '&f------------------------------------'
        - "&7在线人数 &f%server_online%&7/&f%server_max_players%"
        - '&f------------------------------------'
      Footer:
        '1':
        - '&f------------------------------------'
        - '&7%player_world% &f%player_x%:&7%player_y%:&f%player_z%'
        - "&7时间：&f%server_time_HH:mm:ss%"
        - '&f------------------------------------'
    '2':
      PlayerName: '&c[&r[playerDisplayName]&c]'
      Header:
        '1':
        - '&f------------------------------------'
        - "&7在线人数 &f%server_online%&7/&f%server_max_players%"
        - '&f------------------------------------'
      Footer:
        '1':
        - '&f------------------------------------'
        - "&7金钱：&f%vault_eco_balance_formatted% &7时间：&f%server_time_HH:mm:ss%"
        - '&f------------------------------------'
  Sorting:
    # 仅适用于 1.19.3+：开启或关闭 Tab 排序，按指定条件排列
    Enabled: false
    # 玩家排序条件的先后顺序
    # 可用值：Weight、Group、Name、NickName、Balance、World
    # 可添加 ASC 或 DESC 指定某项的顺序，例如 'Weight-DESC'
    # Weight 取玩家 cmi.tablistweight.[value] 权限中的最大值，例如 cmi.tablistweight.5
    # 排序与页眉或页脚同时更新
    Order:
    - Weight-DESC
    - Group-ASC
    - Name-ASC
    - NickName-ASC
    - Balance-ASC
    - World-ASC
```
