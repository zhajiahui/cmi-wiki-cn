---
title: 主配置（config.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: config.yml
---

# 主配置（config.yml）

文件：`plugins/CMI/config.yml`

连接信息、玩家标识和世界示例已使用占位符，使用时按本地配置填写。

## `Language` { #language }

```yaml title="config.yml · Language"
# ********************************************
# ** 更多选项请查看 Settings 文件夹 **
# ********************************************

# 要使用的语言文件
Language: CN
```

## `LanguageDownload` { #languagedownload }

```yaml title="config.yml · LanguageDownload"
# 是否自动从 GitHub 仓库下载默认语言文件
# 如果使用 EN，或已配置好所需语言且不需要下载其他语言，可以关闭此项。
LanguageDownload: true
```

## `Economy` { #economy }

```yaml title="config.yml · Economy"
Economy:
  # 开启或关闭 CMI 经济系统
  # 检测到 CMIInjector 时，此项会自动设为 true
  # 注意！要让经济系统与其他插件正常配合，需要安装注入器或重新编译的 Vault。
  # 两者均可在插件发布页顶部找到
  # 注意！如果在服务器运行时关闭 CMI 经济系统，必须完整重启服务器才能生效，避免读取玩家余额时出现问题。
  Enabled: false
  # 玩家是否需要点击聊天消息，确认转账
  Confirmation: false
  # 是否允许向离线玩家付款。主要影响 pay 命令，不会阻止从其他插件收款等操作。
  OfflinePayments: true
  # 设为 true，将玩家之间的转账写入日志
  LogEnabled: false
  log:
    Unknown: true
    Transfer: true
    IgnoredUsers:
    - "TARGET_1"
  Cheque:
    # 玩家可创建支票的最大金额
    # 设为 0 取消限制
    MaxValue: 1.0E8
    # 设为 true，玩家创建支票时必须手持一张纸。
    Paper: true
    # 设为 true，兑现支票需要 cmi.command.cheque.withdraw 权限
    Permission: false
    # 是否允许在创造模式下使用支票
    # 创造服请保持 false，否则玩家可能复制物品
    InCreative: false
    # 是否接受未使用编码数据的旧版支票物品
    # 为保证安全，保持 false
    AcceptNotEncoded: false
  PaymentWithShorts:
    # 设为 true，允许使用金额缩写付款，例如 10k 表示 10000
    # 同样，10.2k 表示 10200
    Allow: true
    # 允许的金额后缀及其对应数值
    # 后缀只能使用一个字母
    values:
    - k-1000
    - m-1000000
    - b-1000000000
    - t-1000000000000
    - q-1000000000000000
  BalTop:
    # 启用后，服务器启动时会预加载所有玩家余额，供 baltop 排行榜使用
    # 使用第三方经济插件时，可能增加首次加载时间
    # 设为 false，baltop 只包含余额刚发生变化的玩家，不会包含全部玩家
    # 不使用 CMI 的 baltop 时，请保持关闭
    LoadInAll: true
    # 不计入 baltop 排行榜的玩家
    Exclude:
    - "TARGET_1"
    # 启用后，baltop 使用金额缩写，例如将 12501234 显示为 12.5M
    DisplayWithShorts: false
    # 不计入 baltop 的名称列表
    # 可用于排除 Towny 的城镇账户
    ExcludeStartingWith:
    - town_
    - town-
    - towny_
    - towny-
    - debt-
    - debt_
    # 设为 true，将部分虚拟账户纳入 baltop 排行榜
    # 包括此前被标记为虚拟账户、用于城镇或类似用途的账户
    IncludeFakes: false
    # 设为 0 或更小的值关闭此功能
    # 玩家离线达到多少天后，不再计入余额排行榜
    # 需要重启服务器才能完全生效
    ExcludeInactive: 0
  Global:
    # 玩家的初始余额
    StartingAmount: 100.0
    # 最低余额，需要时可设为负数
    MinimalAmount: 0.0
    # 玩家余额上限，设为 -1 取消限制
    MaximumAmount: 1.0E8
    # 玩家单次向其他玩家转账的最低金额
    # 可防止玩家反复转账极小金额来刷屏
    MinimalPay: 0.5
    # 是否允许带小数的转账金额
    # 关闭后只允许整数金额；输入小数时会向下取整
    Fractions: true
    # 显示余额等信息时使用的货币符号
    CurrencySymbol: €
    # 金额显示格式
    MoneyFormat: '###,##0.00'
    # 将长数字缩写，例如将 12305122 显示为 12.3m
    UseShortNumbers: false
    # 此格式仅用于带后缀的金额，例如 '1.23k'；小于 1k 的金额使用 MoneyFormat
    shortNumbersFormat: '###,##0.0'
    # 金额缩写后缀
    ShortNumbersSuffixes:
    - ''
    - k-1000
    - m-1000000
    - b-1000000000
    - t-1000000000000
    - q-1000000000000000
    # 改用逗号分隔小数、句点分隔千位的格式，例如将 1,000,000.00 改为 1.000.000,00
    SwitchPlaces: false
    # 货币符号的位置
    Placing: '[money][symbol]'
    # /pay 命令的转账税
    # 目前仅对这条命令征税，不影响其他操作
    Tax:
      # 征税类型：None、Flat、Percentage
      # Flat：每次执行 pay 时收取固定金额
      # Percentage：按每次 pay 的转账金额收取一定比例
      Type: None
      # 固定税额或转账金额的百分比
      # 百分比范围为 0 到 100
      Amount: 4.0
      # 最低税额，主要用于按比例征税
      Min: 0.0
      # 最高税额，主要用于按比例征税
      # 设为 0 不限制最高税额
      Max: 1000.0
      # 设为 true，税额在转账金额之外另收。例如转账 100、税额 10，收款人获得 100，付款人扣除 110
      # 设为 false，税额从转账金额中扣除。例如转账 100、税额 10，收款人获得 90，付款人扣除 100
      # 建议保持 true，避免玩家不明白为何实际收款少于转账金额
      DeductOnTop: true
```

## `FileSave` { #filesave }

```yaml title="config.yml · FileSave"
FileSave:
  # 仅在磁盘 I/O 有问题，需要异步保存玩家文件以减少 Minecraft 服务端等待时间时，才设为 true
  Async: false
```

## `InteractiveCommands` { #interactivecommands }

```yaml title="config.yml · InteractiveCommands"
InteractiveCommands:
  # 识别告示牌上公开交互指令的正则表达式
  # 默认格式为 [ic:[icName]]，例如 [ic:trash]
  # 若要使用简洁格式，可使用此正则： (\[([a-zA-Z0-9]+)\])
  SignRegex: (\[ic:([a-zA-Z0-9]+)\])
  # 交互指令列表按与你的距离或按字母顺序排序
  SortByDistance: true
```

## `Optimizations` { #optimizations }

```yaml title="config.yml · Optimizations（1/4）"
Optimizations:
  # 关闭后，服务器启动或插件卸载时不会撤销虚拟操作员的 OP，同时禁用 asFakeOp! 特殊指令
  UseFakeOperator: false
  # 关闭后，执行自定义别名命令时不会检查可能出现的无限循环
  InfiniteLoopDetection: true
  # 设为 true，移除所有控制台消息中的颜色
  # 控制台仅支持单色时，保持 true
  MonochromeConsole: false
  # 玩家加入服务器后获得无敌状态的时长，单位为秒
  # 设为 0 关闭
  # 最多 60 秒
  ImmortalityOnJoin: 3
  # 开启或关闭维护模式
  Maintenance: false
  # 开启维护模式时，自动踢出所有没有 cmi.command.maintenance.bypass 权限的玩家
  MaintenanceAutoKick: true
  # 启用后，通过 Boss 栏提示服务器正处于维护模式
  MaintenanceBossBar: true
  # 设为 true，发光颜色、玩家碰撞、名称标签等功能会停止工作，CMI 也不再操作玩家队伍
  # 与其他使用玩家队伍实现功能的插件冲突时，可开启此项
  DisableTeamManagement: false
  ArmorStands:
    # 设为 true，通过模拟方块放置事件，检查其他插件是否阻止玩家操作盔甲架
    # 可减少玩家在没有区域建造权限时，仍能操作该区域盔甲架的情况
    CheckBlockPlace: false
    # 盔甲架编辑器允许设置的最小缩放比例
    # 基础最小比例，可通过 cmi.command.armorstand.scalemin.[value] 权限覆盖
    # 两者都设置时，取此项与权限所指定数值中的较小值
    MinScale: 0.5
    # 盔甲架编辑器允许设置的最大缩放比例
    # 基础最大比例，可通过 cmi.command.armorstand.scalemax.[value] 权限覆盖
    # 两者都设置时，取此项与权限所指定数值中的较大值
    MaxScale: 3.0
    Templates:
      # 设为 true，放置已保存的模板需要 cmi.command.armorstand.template.[templatename] 权限
      SpecificPermission: false
  AutoDownload:
    # 缺少 GeoIP.dat 时会在服务器启动时自动下载，可能需要重启后才生效
    GeoIp: false
    # 缺少 GeoLiteCity.dat 时会在服务器启动时自动下载，可能需要重启后才生效
    GeoLiteCity: false
  # 启用后，右键点击头颅会在动作栏显示其所有者名称
  ShowSkullOwner: true
  # 启用后，右键点击蜂箱会在动作栏显示蜂箱信息
  ShowBeeHiveInformation: true
  # 启用后，右键点击饰纹陶罐会在动作栏显示其中物品的信息
  ShowDecoratedPotInformation: true
  # 创建电梯告示牌时使用的标识，不区分大小写
  ElevatorIndicator:
  - '[CMIElevator]'
  - '[Elevator]'
  SignEdit:
    # 告示牌首行符合此内容时，不允许玩家通过 /cmi se 编辑
    BlackList:
    - '[Private]'
    - '[More Users]'
    - '[Everyone]'
    - '[AdminShop]'
    - '[ChestShop]'
    - '[CMIElevator]'
  # 电梯类型。在告示牌第二行使用此标识时，将玩家传送到牌子正前方，而不是保留原来的 x、z 坐标
  ElevatorStaticIndicator: '[*]'
  # 邮件、checkban、infopage 等位置的日期格式
  LongDateFormat2: dd/MM/yy HH:mm:ss
  # 物品栏界面等位置的日期格式
  ShortDateFormat: dd/MM/yy
  # 是否将 sell hand 操作记录到文件
  SellLog: true
  # 设为 true，执行需要玩家名称的命令时，如果找不到完整名称，会尝试匹配在线玩家的部分名称。例如 /cmi heal rips 可以治疗 Zrips
  # 适合名称较复杂的玩家
  PartialPlayerName: false
  # 使用部分名称匹配时，是否优先选择在线玩家
  # 需要同时启用 PartialPlayerName 才能完全生效
  # 这可能导致名称部分相同的玩家在线时，无法访问对应的离线玩家
  # 例如 Luuk666 在线时，可能无法访问离线玩家 Luuk
  # 可在名称后加 -exa- 强制精确匹配，例如 luuk-exa- 会返回离线玩家对象
  PrioritizeOnlinePlayers: false
  # 设为 true，帮助页中的命令按字母顺序排序
  # 设为 false，按优先级排序
  CommandSorting: true
  # 默认不允许 Rcon 命令。仅在已妥善配置远程控制台且确有需要时开启
  AllowRconCommands: false
  CustomCommandSender: []
  # 启用后，Rcon 返回消息不含颜色代码，便于阅读
  CleanRconCommands: false
  # 找不到命令时，用于选择最接近命令的匹配度，范围为 1–100
  # 例如 /cmi spawnmb 与 /cmi spawnmob 的匹配度为 87.5%
  # 设为 0 关闭
  SimilarCommandChecker: 75
  # 设为 true，玩家输入错误命令时，不执行自动匹配的命令
  # 无论如何，都会提示用法错误并显示最接近的命令
  SimilarCommandPrevention: false
  # 设为 true，隐藏帮助页中命令的 /cmi 前缀，例如将 /cmi back 显示为 /back
  # 已为命令设置别名或自定义别名时，会自动使用此功能
  # 这只影响显示，不改变命令的实际用法
  RemoveLabel: false
  # 设为 true，所有玩家都能将鼠标移到错误提示上，查看缺少的权限节点
  # 设为 false，只有拥有 cmi.permisiononerror 权限的玩家才能查看缺少的权限节点
  # 玩家默认拥有此权限；若要隐藏缺少的权限节点，请将该权限设为否定
  PermisionOnError: false
```

```yaml title="config.yml · Optimizations（2/4）"
Optimizations:
  # 设为 true，玩家尝试执行无权限的操作时，会在控制台显示消息
  PermisionInConsole: true
  Teleport:
    # 玩家需要 cmi.safeteleport 权限，传送时才会被放到安全位置
    # 设为 true，检查安全位置时先从目标位置向下搜索，失败后再向上搜索
    # 设为 false，先检查目标位置上方，再检查下方
    SafeLocationDownThenUp: false
    # 传送后玩家的无敌时长，单位为秒
    # 在指定时间内，也阻止刚传送的玩家伤害其他玩家
    # 设为 0 关闭此功能
    # 最多 60 秒
    Invulnerability: 5
    # 传送到此世界后玩家的无敌时长，单位为秒
    # 未单独设置的世界使用默认时长
    InvulnerabilityPerWorld:
    - "WORLD_1-5"
    # 以下情况会取消传送后的无敌状态
    DisableInvulnerability:
      # 玩家破坏或放置方块时取消
      OnBlockBreakPlace: true
      # 玩家与方块或实体交互时取消
      OnInteraction: true
    # 设为 true，tp 用法为 /cmi tp [WhoYouWantToTeleport] [WhereToTeleport]；设为 false，用法为 /cmi tp [whereToTeleport] [WhoYouWantToTeleport]
    SwitchPlaces: true
    CurrentLoc:
      # 仅适用于 tpa、tpahere 和 tpaall
      # 设为 true，接受传送请求后，传送到目标玩家当前的位置
      # 设为 false，传送到发出请求时目标玩家所在的位置
      tpa: true
      # 仅适用于 tpahere
      tpahere: true
    # jump 命令的默认距离，可通过 cmi.command.jump.[amount] 权限覆盖
    JumpDefault: 50
    Tpa:
      # 接受 tpa 或 tpahere 请求的有效时间，单位为秒
      Time: 60
      # 接受 tpa 或 tpahere 后，传送前的等待时间，单位为秒
      Warmup: 3
      # 等待 tpa 或 tpahere 传送期间，是否允许移动
      Move: false
      # 拒绝请求后，阻止对方再次发送传送请求的时长，单位为秒
      Block: 120
      # 最大传送距离，单位为方块
      # 设为 0 关闭此限制
      # 设为正数后，除了限制玩家间的距离，也会阻止向其他世界的玩家发送传送请求
      # 可通过 cmi.command.tpa.max.[blockcount] 权限覆盖
      MaxDistance: 0
    TpaHere:
      # 最大传送距离，单位为方块
      # 设为 0 关闭此限制
      # 可通过 cmi.command.tpahere.max.[blockcount] 权限覆盖
      MaxDistance: 0
    Tp:
      # 允许绕过“不安全位置”传送拦截的时间，单位为秒
      Bypass: 15
    # 设为 true，tpa 或 tpahere 请求中显示接受和拒绝按钮
    DenyConfirm: true
    BlackListedItems:
      # 物品栏中有黑名单物品时，阻止玩家传送。可通过 cmi.teleport.bypassblacklist 绕过
      Enabled: false
      EnabledFor:
        tp: true
        tpa: true
        tpahere: true
        warp: true
        home: true
        spawn: true
      # 要限制的物品及数量，未填写数量时默认为 0
      # 使用 : 分隔数量，例如 IronOre:5 表示物品栏中 ironOre 最多为 5 个，超出就无法传送
      List:
      - Diamond
      - DiamondBlock
      - DiamondOre
      - ironore:5
    Back:
      # 传送距离小于指定方块数时，不记录 /back 返回位置
      MinDistance: 5
      # 设为 false，使用 WorldEdit 指南针传送时不记录返回位置
      # 设为 true，记录每次传送，包括使用指南针进行的短距离跳跃
      WithWE: true
      # 不允许通过 /back 返回的世界
      BlackList:
      - "WORLD_1"
      # /back 返回位置的有效时间，单位为秒；设为 0 关闭过期限制
      Expiration: 0
    DBack:
      # 不允许通过 /dback 返回的世界
      BlackList:
      - "WORLD_1"
      # /dback 返回位置的有效时间，单位为秒；设为 0 关闭过期限制
      Expiration: 0
```

```yaml title="config.yml · Optimizations（3/4）"
Optimizations:
  Hat:
    Block:
      # 启用后，不允许将带有自定义描述的物品放入头盔槽
      # 不影响头盔类物品
      WithLore: false
      # 启用后，不允许装备非帽子类型的物品
      NoneHatItems: true
      # 启用后，不允许装备带附魔的非帽子物品
      NoneHatEnchanted: true
    Allow:
      # 启用后，玩家无需 cmi.inventoryhat 权限即可将生物头颅戴在头上
      # 关闭后，将生物头颅戴在头上需要 cmi.inventoryhat 权限
      MobHeads: true
    # 允许戴在头上的材质列表
    # 留空表示允许所有材质
    WhiteList: []
  helpop:
    # 设为 true，玩家不会看到自己发送的 helpop 内容，而会收到预设提示，告知问题已发给在线管理人员
    feedbackMessage: true
  IP:
    # 设为 true，记录玩家 IP，供日后识别其他账号等用途使用
    # 关闭后，部分命令的功能会受限
    # 这可能增加缓存大小，尤其是玩家使用动态 IP 时
    Record: false
    # 等待多少秒后，才将玩家 IP 写入数据库
    # 仅用于离线服务器，让玩家先完成登录，再记录 IP
    # 建议大于登录插件允许的登录时长，以记录真正有权使用该名称的玩家 IP
    delay: 30
  # /cmi maxhp 命令允许设置的生命值上限
  MaxHp: 1000
  # 设为 true，从玩家统计文件读取在线时长，而不是从 CMI 玩家数据读取
  # 对于运行较久并启用玩家统计的服务器，这可能获得更准确的在线时长
  # 建议保持 true
  PlayTimeFromStats: true
  # 是否自动更新在线时长排行榜
  # 按固定间隔更新玩家的在线时长排名，便于占位符读取
  PlayTimeAutoUpdater: true
  # 是否启用 CMI 在线时长记录
  # 启用后，按玩家在服务器游玩的每个小时分别记录在线时长
  # 不影响 rankup 和 /playtime，只让 /cplaytime 按小时显示更详细的在线时长
  CMIPlayTimeTracking: false
  # 不计入 playtimetop 排行榜的玩家名称
  PlaytimeTopExclude:
  - "TARGET_1"
  - "TARGET_2"
  - "TARGET_3"
  # 玩家离线达到多少天后，从 playtimetop 中排除
  # 设为 0 关闭
  PlaytimeTopOffline: 0
  ItemName:
    # 材质黑名单见 ItemRenaming.list

    # 设为 true，用 /itemname 改名的物品会添加布尔型 NBT 标记 'ModifiedName'
    MarkChanged: false
  ItemLore:
    # itemlore 命令允许的单行描述最大长度，不含颜色代码
    # 设为 0 取消限制
    MaxLength: 64
    # 禁止使用 itemName 命令改名的材质
    TypeBlackList:
    - gold_nugget
    # 设为 true，用 itemname 修改描述的物品会添加布尔型 NBT 标记 'ModifiedLore'
    MarkChanged: false
  OnDurabilityLoss:
    # 物品耐久度低于阈值时，是否提醒玩家
    # 玩家需要 cmi.informDurability 权限
    Tools:
      Use: true
      Percentage: 10
    Armor:
      Use: true
      Percentage: 10
  OnLimitedItemUse:
    # 提示物品剩余可使用次数
    Inform: true
  # 是否阻止动物或怪物进入船
  PreventEntityBoatEnter:
    Monsters: false
    Animals: false
    Villagers: false
  PreventBedExplosion:
    Nether: false
    TheEnd: false
  # 将位于下界基岩顶层上方的玩家传送到下方
  PreventPlayersOnNetherRoof: false
  # 下界顶层高度。设为 0 使用默认高度 128
  netherRoofHeight: 0
  # 玩家飞行或使用鞘翅滑翔到基岩下方时，将其传送到上方
  PreventPlayersBelowBedrock: false
  PreventIronGolem:
    # 设为 true，铁傀儡死亡时不掉落玫瑰
    Roses: false
  # 设为 true，钓竿不会将钩住的实体拉向玩家
  PreventHook: false
```

```yaml title="config.yml · Optimizations（4/4）"
Optimizations:
  Commands:
    # 设为 true，只执行 /cmi 而不指定子命令时，显示全部可用命令
    # 设为 false，返回“未找到命令”的提示
    ShowMainHelpPage: true
    Near:
      # 使用大致距离，而不是精确距离
      # 使用另一条包含玩家方向的语言文本
      # 例如将 123m 显示为 ~100m
      Approximate: true
      DefaultDistance: 200
      Invisibility:
        # 启用后，不在列表中显示具有隐身药水效果的玩家
        Hide: false
        # 仅在上面的 Hide 选项启用时生效
        # 混淆玩家名称，但仍在列表中显示其位置
        # 不用真实名称，而是使用固定 8 个字符、带 &k 格式的名称，避免通过名称长度猜出附近是谁
        Obfuscate: false
      # 启用后，点击玩家名称会执行 /cmi point [location]，通过粒子指向目标玩家
      PointTo: true
      # /near 命令显示的行数
      Count: 10
    lastonline:
      # lastonline 统计最近多少秒内离线的玩家数量，作为附加信息显示
      Timers:
        Time1: 3600
        Time2: 86400
        Time3: 604800
        Time4: 2592000
    CheckAccount:
      # checkaccount 命令排除的玩家或 IP
      ExcludedUsers:
      - "TARGET_1"
    Inv:
      # 不允许打开其物品栏的玩家
      # OP 仍可绕过此限制
      BlackList:
      - "TARGET_1"
      # 是否禁止对离线玩家使用 inv 命令
      DisableOffline: false
    Clear:
      # 设为 true，/cmi clear 必须确认后才执行
      Confirmation: true
      # 移除物品前需要检查的 NBT 路径。每行应以 NBT: 开头，为以后加入其他可选检查保留
      Exclude:
      - NBT:ItemJoin Name
      - NBT:ItemJoin.Name
    List:
      # 玩家自定义组按升序或降序排序
      ASCOrder: true
    Sc:
      # 启用后，复制告示牌文字时会检查玩家可用的颜色权限
      # 关闭后，原样复制文字及颜色，不作修改或限制
      ClearColors: true
    Give:
      # 启用后，give 命令中的物品遵守相同的附魔限制和权限要求
      LimitEnchants: false
  Multicraft:
    # 设为 true，防止 Multicraft 服务器的控制台刷屏
    DisableList: false
  DisableWorldChunkCheckInfo: false
```

## `PlaytimeRewards` { #playtimerewards }

```yaml title="config.yml · PlaytimeRewards"
PlaytimeRewards:
  # 开启或关闭在线时长奖励
  # 要自动发放奖励，必须启用此项
  Enabled: false
  # 启用后，玩家 AFK 时不累计可重复在线时长奖励的进度
  # 注意！Afk.StopPlayTime 为 true 时，此项不生效
  # StopPlayTime 为 true 时，AFK 时长会自动排除
  ExcludeAfk: false
  # 提醒玩家领取待领取奖励的间隔，单位为分钟
  RewardInform: 15
  # 列表中显示多少个一次性奖励
  # 显示从当前在线时长起接下来的 X 个奖励
  # 距离奖励还很远时，没有必要列出全部奖励
  OneTimeAmount: 2
  # 设为 true，领取指定在线时长奖励需要 cmi.prewards.[name] 权限
  RequiresPermission: false
```

## `Sleeping` { #sleeping }

```yaml title="config.yml · Sleeping"
Sleeping:
  Speedup:
    # 设为 true，玩家睡觉时可以加快夜晚流逝
    # 根据该世界中睡觉的玩家比例，加快时间流逝
    Enabled: true
    # 应用此功能的世界列表
    # 只有普通类型的世界支持加速时间，默认通常只有一个这样的世界
    # 设为 [] 将包含所有可用世界
    Worlds: []
    # 设为 true，只在一天中的 12542 到 24000 刻之间加速时间
    # 设为 false，玩家也能在雷暴等情况下加速白天
    OnlyDurringNight: true
    # 夜晚开始的时间
    # 单位为刻，例如 12542 对应 18:32:00
    NightStartsAt: 12542
    # 加速提示的显示类型：none、title、bossbar
    InfoType: title
    # 设为 true，计算加速比例时排除 AFK 玩家
    ExcludeAfk: true
    # 夜晚加速的基础倍数。数值越大，时间越快，所需睡觉玩家越少
    # 100 表示时间流逝速度为正常的 100 倍
    BaseSpeed: 100
    # 最低加速倍数，用于玩家数量超过基础倍数、计算结果回到默认速度的情况
    MinSpeed: 5
    # 开始加速前，至少需要多少名玩家睡觉
    # 支持两种格式：填写整数，例如 3，表示至少 3 名玩家睡觉才开始加速
    # 填写百分比，例如 50%，表示服务器中至少一半玩家睡觉才开始加速
    MinBeforeSpeeding: 50%
    # 设为 true，向在线玩家提示还缺多少人睡觉
    Inform: true
    # 玩家开始或停止睡觉时，加速提示消息的最小间隔，单位为秒
    InformDelay: 30
```

## `Compass` { #compass }

```yaml title="config.yml · Compass"
Compass:
  # 启用实验性的 Boss 栏指南针
  # 仅适用于 1.9+ 服务器
  BossBar: false
  # 需要手持指南针才会显示
  RequireCompass: false
  # 启用后，恢复指南针也能像普通指南针一样触发 Boss 栏显示
  RecoveryAsRegular: false
  # 需要手持恢复指南针，Boss 栏才会显示死亡位置
  RequireRecoveryCompass: false
  # 指南针更新间隔，单位为毫秒
  UpdateInterval: 200
  # 各方向之间保持相同间距，整体长度不限
  Shape: '------------SW-------------W-------------NW-------------N-------------NE-------------E-------------SE-------------S-'
  Color: '&7'
  ShowHome: true
  Home: ۩
  ShowSpawn: true
  Spawn: ⤋
  ShowDeath: true
  Death: ☠
  ShowCompassTarget: true
  CompassTarget: ꖴ
  # 仅适用于 1.16+ 服务器
  # 方向之间的颜色过渡
  Gradient:
    Use: true
    SouthColor: white
    WestColor: orange
    NorthColor: vulcan
    EastColor: bitter_lemon
```

## `ExploitPatcher` { #exploitpatcher }

```yaml title="config.yml · ExploitPatcher"
ExploitPatcher:
  # 启用后，防止经验瓶在传送门边缘被摧毁而造成复制
  PreventExpPortals: true
  # 启用后，阻止玩家执行可能引发问题的命令
  # 默认关闭以保留原版行为，但建议开启以避免问题
  NoCommandsInBed: false
  # 由于超大书本存在严重漏洞，建议开启此项
  # 设为 true，限制玩家可创建的书本页数
  # 页数由 cmi.book.pages.§f[20to100]§6 权限决定，默认允许创建 20 页
  LimitBooks: true
  # 启用后，阻止物品通过末地传送门和末地折跃门传送
  BlockEndPortalItemTransfers: true
  # 世界天气为晴天、玩家个人天气 pweather 为雨天时，禁止使用激流
  Riptide: true
  Placeholders:
    blocked:
      # 默认阻止 PAPI 的 %checkitem_...% 占位符，以避免潜在的严重问题
      # 只有另有专门防护时，才应关闭此项
      checkItem: true
```

## `Vault` { #vault }

```yaml title="config.yml · Vault"
Vault:
  # Vault 无法正确读取玩家权限组或余额时，可以尝试设为 false
  Money: true
  Group: true
```

## `Worth` { #worth }

```yaml title="config.yml · Worth"
Worth:
  # 包含此描述的物品无法通过 /cmi sell 出售
  # 忽略颜色代码和大小写
  BadLore:
  - Creative item by Gasha
  # 启用后，带自定义名称的物品无法通过 /cmi sell 出售
  CustomNameBlocking: false
  # 启用后，带自定义描述的物品无法通过 /cmi sell 出售
  LoreBlocking: false
  # 启用后，耐久度未完全修复的物品无法出售
  RequireFullDurability: false
  # 启用后，按剩余耐久度降低售价。例如剩余 30% 耐久度，价格降低 70%
  # 仅在 RequireFullDurability 关闭时生效
  DevalueByDurability: false
  AutoGenerate:
    # 根据材料价格自动计算成品价格时，额外增加的百分比
    # 例如木棍价格为 0.1、钻石为 44，diamond_hoe 的材料总价为 88.2；额外增加 2% 后变为 89.96
    # 可以设为负数
    PriceIncrease: 0
```

## `BossBar` { #bossbar }

```yaml title="config.yml · BossBar"
BossBar:
  # 在 1.9+ 服务器上开启或关闭 Boss 栏生命值显示
  # 只有拥有 cmi.bossbar.hpbar 权限的玩家才能看到
  # 为减少开销，此权限最多每分钟重新检查一次
  HpBarEnabled: false
  # 不在生命值 Boss 栏中显示的生物类型
  HpBarBlackList:
  - Ender_dragon
```

## `Ban` { #ban }

```yaml title="config.yml · Ban"
Ban:
  # 设为 true，被封禁玩家看到 CMI 修改后的提示，而不是原版提示
  OverrideLoginMessage: false
```

## `ReSpawn` { #respawn }

```yaml title="config.yml · ReSpawn"
ReSpawn:
  # 玩家重生后的无敌时长，单位为秒
  # 可用于防止玩家在重生点被反复击杀
  # 设为 0 关闭此限制
  # 最多 60 秒
  Immortality: 3
  # 若由第三方插件处理重生，将此项设为 false 后重载插件即可
  Enabled: true
  Global:
    # 世界未出现在 Specific 列表中时，使用的重生位置优先顺序
    # 可用位置：anchor、bedLocation、spawn、homeLocation、worldSpawn、warp![warpName]
    # spawn：用 /cmi setspawn 设置的位置，该位置的 RespawnLocation 应为 true
    # bedLocation：通过与床交互设置的位置。BedInteraction 应设为 false，玩家需要 cmi.bedhome 权限才能设置
    # homeLocation：玩家默认名称为 Home 的家。不存在时，尽可能使用列表中的第一个家
    # worldSpawn：此世界的默认出生点，不是 CMI 设置的出生点
    # anchor：与重生锚交互后设置的位置。通常只在下界死亡时使用，其他情况使用床的位置
    # warp![warpName]：任意有效传送点，传送时绕过该传送点的全部使用要求
    PriorityOrder:
    - anchor
    - bedLocation
    - spawn
    - homeLocation
    - worldSpawn
  # 指定世界的重生位置优先顺序
  # 若交由服务端或第三方插件处理重生，将重生优先列表设为 []，或设为随机重生条件
  Specific:
    world:
    - anchor
    - bedLocation
    - spawn
    - homeLocation
    - worldSpawn
    world_nether:
    - anchor
    - bedLocation
    - spawn
    - homeLocation
    - worldSpawn
    world_the_end:
    - anchor
    - bedLocation
    - spawn
    - homeLocation
    - worldSpawn
```

## `Holograms` { #holograms }

```yaml title="config.yml · Holograms"
Holograms:
  Defaults:
    # 全息图的默认可见距离
    # 决定玩家在多远的位置能看到全息图，以及何时隐藏
    viewRange: 16
    # 全息图的默认更新距离
    # 玩家进入此距离内，全息图才开始更新文字
    # 请设置合理范围，没有必要更新地图另一端的全息图
    updateRange: 8
    Interval:
      # 默认更新间隔，单位为刻；20 刻 = 1 秒
      # 设为 0 或更小的值时，不更新全息图
      # 仅影响包含动态内容的全息图
      Update: 0
    # 默认翻页间隔，单位为刻
    # 设为 0 或更小的值时，不自动翻页
    pageChangeInterval: 0
    Interaction:
      # 使用 CText 的行所加的前缀
      # 仅影响设置了命令的部分，不影响普通文字，即使普通文字带悬停提示
      BasePrefix: '{#white}'
      # 使用 CText 的行在鼠标悬停时所加的前缀
      # 可在全息图编辑器中单独覆盖
      HoverPrefix: '{#gray}'
```

## `Votifier` { #votifier }

```yaml title="config.yml · Votifier"
Votifier:
  # 设为 true，记录玩家的 Votifier 投票次数
  CountVotes: true
  # 同一 IP 在过去 24 小时内允许的投票次数
  # 设为 0 不限制次数
  MaxVotesInADay: 0
  # 同一投票服务的投票冷却时间
  # 大多数投票服务本身已有冷却限制
  # 需要额外限制快速重复投票时，可在此填写秒数
  GeneralCooldown: 0
  # 设为 false，成功投票后不执行命令
  PerformCommands: true
  # 玩家投票时执行的命令
  # 支持特殊指令和占位符
  # 可用 [serviceName] 变量插入服务地址
  CommandsOnVote:
  - "cmi broadcast !&6[playerDisplayName] &e投票了！"
  - cmi give [playerName] diamond
  # 不想发放额外奖励时，保持 false
  ExtraRewardsEnabled: false
  # 玩家累计达到指定投票次数后执行的命令
  ExtraRewards:
    '10':
    - cmi heal [playerName]
    - cmi money give [playerName] 100
    '100':
    - cmi heal [playerName]
    - cmi money give [playerName] 1000
    - cmi give [playerName] diamond 32
  # 不计入投票排行榜的玩家
  ExcludeList:
  - None
```

## `Ranks` { #ranks }

```yaml title="config.yml · Ranks"
Ranks:
  # 设为 true，通过权限检查玩家可使用的等级，并优先采用权重高于当前等级的等级
  # 例如记录的等级为第一级、但玩家有第三级权限时，优先采用第三级
  # 启用期间，/cmi setrank 等命令会将等级设为玩家有权使用的最高等级；只要仍有第三级权限，就无法降到更低等级
  # 降级前，需要先移除相应等级的权限
  PermissionCheck: false
  # 重新计算玩家权限组的间隔，单位为分钟
  # 设为 0 关闭
  Recalculation: 0
  AutoRankUp:
    # 检查玩家能否晋级的间隔，单位为秒
    # 设为 0 或更小的值，关闭自动晋级检查
    Delay: 60
    # 实验性选项：设为 true，异步检查玩家晋级条件
    # 启用后若出现相关错误，请关闭，并携带错误日志向 GitHub 反馈
    Async: false
    # 对每名玩家分别检查晋级条件的间隔，单位为秒
    # 与全局检查间隔不同，用于避免几名玩家同时晋级
    # 同时决定可晋级提示的间隔；每次提示后，间隔会按比例增加，避免聊天刷屏
    # 应大于或等于全局检查间隔
    PlayerDelay: 120
    # 是否在等级信息界面显示进度条
    progressBar: true
  # 设为 true，/cmi ranklist 只显示当前晋级路线中的等级，排除其他路线和等级树
  # 设为 false，显示所有已设置的等级
  ListSamePathOnly: false
  EffectUp: GColumn
  # 设为 true，时间要求使用小时格式，例如显示“50 小时”，而不是“2 天 2 小时”
  OnlyHours: false
  # OnlyHours 为 true 时，使用分钟补充显示，避免小数，例如显示“5 小时 30 分钟”，而不是“5.5 小时”
  includeMinutes: true
```

## `Signs` { #signs }

```yaml title="config.yml · Signs"
Signs:
  # 检查玩家是否进入动态告示牌触发区域的间隔，单位为毫秒
  # 数值较大可略微降低服务器负载
  # 无需设置得很小
  CheckInterval: 3000
  # 告示牌首行符合列表内容时，无法通过潜行右键编辑
  # 通常用于防止商店告示牌被修改
  editBlackList:
  - '[Shop]'
  # 启用后，必须潜行才能编辑告示牌
  RequireSneaking: false
  # 启用后，使用 1.21.7+ 新增的对话框编辑器编辑告示牌
  # 仅适用于 Paper 服务器
  DialogEditor: true
```

## `Skins` { #skins }

```yaml title="config.yml · Skins"
Skins:
  # 玩家登录且尚未设置皮肤时，自动应用皮肤
  # 始终按目标玩家名称获取皮肤
  AutoApply: false
  # 关闭皮肤时，先设为 Steve，再交由服务端处理
  # 设为 false 时，改用在线获取的皮肤
  SteveOnOff: true
  # 使用指定皮肤需要 cmi.command.skin.perm.[skinName] 权限
  RequireSpecificPerm: false
  # 从 Mojang 在线服务器更新皮肤信息的间隔，单位为分钟
  # 例如设为 1 小时，已有皮肤信息超过 1 小时后才重新获取
  # 仅在玩家加入服务器或手动更换皮肤时检查
  SkinUpdateTimer: 1320
```

## `Alert` { #alert }

```yaml title="config.yml · Alert"
Alert:
  # 执行 /cmi alert 后，对该玩家保留警报的时间，单位为分钟，默认为 24 小时
  Timer: 1440
```

## `Notes` { #notes }

```yaml title="config.yml · Notes"
Notes:
  # 启用后，被标记警报的玩家登录时，提醒管理人员该玩家附有备注
  ShowOnAlertEvent: true
```

## `GroundClean` { #groundclean }

```yaml title="config.yml · GroundClean"
GroundClean:
  WhiteList:
    # 清理地面物品时，保留的物品类型
    Material:
    - itemType
    # 清理地面物品时，保留的物品类型
    EntityType:
    - entityType
```

## `Command` { #command }

```yaml title="config.yml · Command"
Command:
  CommandFilter:
    Duplicate:
      # 设为 true，限制短时间重复执行相同或相似命令。可通过 cmi.commandfilter.bypass 绕过
      Use: false
      # 判定为相同命令的相似度百分比
      Percentage: 80
      # 重复执行相同或相似命令的间隔，单位为秒
      Interval: 5
      # 触发冷却前允许连续重复的命令次数
      MinAmount: 2
      # 不受限制的命令白名单
      WhiteList:
      - msg
      - tell
      - login
      - register
  Spy:
    # 出于安全和隐私考虑，命令监视不显示列表中的命令
    # 可通过 cmi.command.commandspy.bypass 权限绕过
    BlackListed:
    - register
    - login
    - l
    # 没有 cmi.security.admin 权限的玩家，使用命令监视时只能看到此列表中的命令
    # 留空表示显示除黑名单以外的全部命令
    CommandList: []
  Notes:
    # 玩家备注的保留时间，单位为天
    ExpiresIn: 30
  Mail:
    # 玩家邮件的保留时间，单位为天
    ExpiresIn: 30
    # 群发邮件只发送给过去 X 天内登录过的玩家
    mailAllDays: 7
    # 每名玩家最多保留的邮件数量
    # 达到邮件上限后，移除最早的邮件
    MaxMails: 50
    # 控制台发送邮件时使用的发件人名称
    # 用于显示发件人；玩家回复时，也会发送给此名称对应的玩家
    # 建议填写负责与玩家沟通的管理人员名称
    ConsoleMailSender: server
```

## `DisplayName` { #displayname }

```yaml title="config.yml · DisplayName"
DisplayName:
  # 由第三方插件修改玩家显示名称时，将此项设为 false
  Change: true
  # 玩家显示名称格式。默认显示昵称；未设置昵称时，显示真实玩家名称
  # 可用自定义变量：{prefix} {suffix} {nicknameprefix}
  # 支持占位符
  Format: '{nickName}'
  # 检查昵称是否合法的正则表达式
  # 默认只允许字母和数字
  # 若允许所有语言的字母，可使用 [^\p{L}0-9\-\_]
  ValidNicknameRegex: '[^a-zA-Z0-9\-\_]'
```

## `NickName` { #nickname }

```yaml title="config.yml · NickName"
NickName:
  # 没有绕过权限时，禁止将昵称改为列表中的名称
  # 使用小写
  # cmi.command.nick.bypassblacklist
  # 可通过 cmi.command.nick.bypassinuse 绕过名称或昵称已被占用的限制
  BlackList:
  - admin
  - administrator
  - server
  - staff
  - staf
  # 昵称最小长度，可通过 cmi.command.nick.bypass.length 绕过
  MinLength: 4
  # 昵称最大长度，可通过 cmi.command.nick.bypass.length 绕过
  MaxLength: 16
  # 启用后，不允许选择已存在的真实玩家名称
  # 可通过 cmi.command.nick.bypassrealname 权限绕过
  PreventRealNames: true
  # 为昵称添加前缀，表明它不是真实名称。可通过 {nicknameprefix} 加入显示名称
  Prefix: '~'
  # 设为 true，只有昵称与原名不同时才添加前缀，因此仅修改颜色或大小写时可不加前缀
  PrefixWhenDifferent: false
  TabComplete:
    # 设为 true，Tab 补全使用在线玩家的昵称，而不是真实名称
    ReplaceReal: true
    # 设为 true，在昵称上方同时显示真实名称；仅在 ReplaceName 启用时生效
    IncludeReal: false
```

## `Dye` { #dye }

```yaml title="config.yml · Dye"
Dye:
  # 设为 true，染色皮革盔甲的动态颜色绑定到获得该颜色的玩家，交给其他玩家后不再生效
  # 仅影响生物群系、生命值等动态盔甲颜色
  BoundToPlayer: false
```

## `ShowNewVersion` { #shownewversion }

```yaml title="config.yml · ShowNewVersion"
# 拥有 cmi.versioncheck 权限的玩家登录时，提示是否有新版本
ShowNewVersion: true
```

## `Spawners` { #spawners }

```yaml title="config.yml · Spawners"
Spawners:
  # 刷怪笼处理出现问题时，可设为 true，关闭 CMI 对刷怪笼的操作
  # 这会关闭刷怪笼放置、掉落、挖掘次数等功能
  FullDisable: false
  Break:
    # 注意！玩家必须拥有 cmi.dropspawner 权限，破坏刷怪笼时才会掉落
    # 开启或关闭刷怪笼破坏处理
    # 启用后，使用精准采集镐且拥有 cmi.dropspawner 权限时，破坏刷怪笼可获得掉落
    # 拥有 cmi.dropspawner.nosilk 权限时，无需精准采集镐也能获得刷怪笼
    Enabled: false
    # 启用后，刷怪笼物品按其生物类型设置自定义名称
    CustomName: false
    # 启用后，刷怪笼直接放入玩家物品栏，不掉落到地面
    # 物品栏已满时，仍会掉落到地面
    IntoInventory: false
    # 设为 true，破坏并获得指定类型的刷怪笼需要对应权限
    # 例如破坏猪刷怪笼并获得掉落需要 cmi.dropspawner.pig，僵尸刷怪笼需要 cmi.dropspawner.zombie
    RequiresExactPermission: false
    # 设为 false，破坏刷怪笼不掉经验，无论刷怪笼本身是否掉落
    # 设为 true，只在刷怪笼本身不掉落时掉经验
    DropExp: false
    # 获得刷怪笼所需的最低精准采集等级
    SilkTouchLevel: 1
    # 破坏刷怪笼后的掉落概率，范围为 0 到 100，单位为百分比
    BaseDropChance: 100.0
    StopDropping:
      # 是否在挖掘一定数量的刷怪笼后停止掉落
      Enabled: false
      # 玩家最多可挖掘的刷怪笼数量，达到后掉落概率设为 0
      # 按玩家统计中的刷怪笼总挖掘数计算，也包含未成功掉落的次数，请据此调整
      # 也可通过 cmi.dropspawner.stopafter.[positivevalue] 权限指定上限
      After: 0
      # 启用后，掉落概率按上述上限和已挖掘数量逐渐降低
      # 达到上述上限之前，掉落概率不会低于 1%
      Linear: false
  Place:
    # 开启或关闭刷怪笼放置处理
    # 启用后，按刷怪笼物品的生物类型放置
    # 关闭后，按普通方式放置，交由其他插件处理
    Enabled: true
    # 设为 true，按生物类型放置刷怪笼需要对应权限
    RequiresPermission: false
    # 需要先将 RequiresPermission 设为 true。启用此项后，每种刷怪笼都需要单独的放置权限
    # 例如放置猪刷怪笼需要 cmi.placespawner.pig，僵尸刷怪笼需要 cmi.placespawner.zombie
    # 设为 false，只需基础权限 cmi.placespawner 即可放置任意类型刷怪笼
    RequiresExactPermission: false
  Interact:
    Spawner:
      # 设为 true，使用刷怪蛋修改刷怪笼需要对应权限
      # 例如改为猪需要 cmi.egginteract.pig，改为僵尸需要 cmi.egginteract.zombie
      RequiresPermission: false
    TrialSpawner:
      # 设为 true，使用刷怪蛋修改试炼刷怪笼需要对应权限
      # 例如改为猪需要 cmi.trialegginteract.pig，改为僵尸需要 cmi.trialegginteract.zombie
      RequiresPermission: false
  # 设为 true，TNT 炸毁刷怪笼时有概率掉落
  TnTExplosionDrop:
    use: false
    # 刷怪笼掉落概率，单位为百分比
    Chance: 30
  # 设为 true，苦力怕炸毁刷怪笼时有概率掉落
  CreeperExplosionDrop:
    use: false
    Chance: 30
  Charges:
    # 启用后，根据 cmi.spawners.charge.[groupName] 权限将玩家分配到对应的刷怪笼挖掘次数组
    # 限制玩家能挖掘的刷怪笼数量
    # StartingCharge：首次加入该组时获得的挖掘次数
    # MaxCharge：可同时持有的挖掘次数上限
    # Cooldown：恢复一次挖掘次数的间隔
    # Bonus：可选项，放置刷怪笼时，将下一次次数恢复的冷却缩短多少秒
    # 可通过 cmi.spawners.charge.bypass 绕过限制
    Use: false
    # 设为 true，挖掘次数用尽后，破坏刷怪笼会将其摧毁而不掉落
    BreakWithoutCharge: false
    List:
      Noob:
        Use: false
        StartingCharge: 2
        MaxCharge: 5
        Cooldown: 3600
        Bonus: 10
      Advanced:
        Use: false
        StartingCharge: 3
        MaxCharge: 6
        Cooldown: 3000
        Bonus: 10
  Proximity:
    # 限制刷怪笼之间的最小放置间距
    Use: false
    # 以放置位置为中心的半径，单位为方块，最大范围为 16
    # 可通过 cmi.spawners.proximity.bypass 绕过
    Range: 3
```

## `ItemRenaming` { #itemrenaming }

```yaml title="config.yml · ItemRenaming"
ItemRenaming:
  # 设为 true，禁止通过铁砧或 itemname 命令为指定物品改名
  # 可使用正则表达式匹配指定名称
  # 可通过 cmi.anvil.itemrename.bypass 绕过
  Prevent: false
  # 设为 true，全面禁止通过铁砧或命令改名，不论物品材质
  # 可通过上面的权限绕过
  GlobalDisable: false
  # itemname 命令允许的物品名称最大长度，不含颜色代码
  # 设为 0 取消限制
  MaxLength: 64
  Anvil:
    # 启用后，为物品名称添加颜色时强制使用斜体，模拟原版物品改名效果
    ItalicByDefault: true
  # 启用后，除最终名称外，也检查原物品
  # 可让特定名称的物品完全无法改名，同时防止其他物品改为这些名称
  CheckSource: true
  # 材质列表，可在材质后附正则表达式。例如禁止将某种刷怪笼改名为另一种，但仍允许改为其他名称
  # 用 * 表示全部材质，例如 *:([A-z])
  List:
  - mobspawner:([A-z]+ (?i)\w*spawner)
```

## `SpawnMob` { #spawnmob }

```yaml title="config.yml · SpawnMob"
SpawnMob:
  # 一次最多可生成的乘客实体数量
  MaxQuantity: 25
  MaxPassengers: 10
```

## `Counter` { #counter }

```yaml title="config.yml · Counter"
Counter:
  # /counter start 使用的默认范围
  Range: 10
```

## `Mirror` { #mirror }

```yaml title="config.yml · Mirror"
Mirror:
  # 允许在距离镜像中心多远的位置建造，单位为方块
  # 主要防止忘记关闭镜像后，又在地图其他位置开始建造
  MaxRange: 50
  # 单次最多修改的方块数
  # 每个方块都需要单独检查，请保持较低数值，避免额外负载
  MaxBlocks: 16
  # 关闭后，镜像模式不执行方块破坏
  # 主要避免此功能被用于挖矿，而不是建造
  BreakDisabled: false
```

## `NetherPortal` { #netherportal }

```yaml title="config.yml · NetherPortal"
NetherPortal:
  # 可完全阻止创建下界传送门，通过 cmi.netherportalbypass 绕过
  PreventCreation: false
  # 下界传送门的最大高度，原版为 23
  MaxHeight: 23
  # 下界传送门的最大宽度，原版为 23
  MaxWidth: 23
```

## `Portals` { #portals }

```yaml title="config.yml · Portals"
Portals:
  # 检查玩家是否进入传送区域的间隔，单位为毫秒
  # 数值较大可略微降低负载，但玩家移动过快时，可能穿过只有 1 格深且无背墙的传送门而未被传送
  CheckInterval: 300
  # 检查玩家是否进入传送门粒子显示范围的间隔，单位为毫秒
  CheckParticleInterval: 500
  Defaults:
    # 默认是否允许没有目标位置的传送区域执行命令
    # 仅影响新建的传送区域
    # 设为 true，新建传送区域后，进入时会执行下方命令，而不会传送到其他位置
    # 可在游戏内传送门编辑器中，为每个传送区域单独修改
    PerformCommands: true
    # 发生传送时执行的命令
    Commands:
    - cmi effect [playerName] blindness 2 1 -s
```

## `Animations` { #animations }

```yaml title="config.yml · Animations"
Animations:
  # 允许空手点击楼梯，或看着楼梯使用命令坐下
  # 需要 cmi.command.sit.stairs 权限
  SitOnStairs: true
  StairsAsChairs: true
  SlabsAsChairs: true
  CarpetsAsChairs: false
  RemoveFromChairOnDamage: true
  # 只有快速双击后，玩家才会坐下
  DoubleClick: false
  # 启用双击坐下时，两次点击的允许间隔，单位为毫秒
  DoubleClickDelay: 200
  # 从玩家位置寻找有效椅子方块的范围，单位为方块
  ChairRange: 4
```

## `DamageControl` { #damagecontrol }

```yaml title="config.yml · DamageControl"
# 所有可用伤害原因：kill, world_border, entity_attack, entity_sweep_attack, projectile, suffocation, fall, fire, fire_tick, melting, lava, drowning, block_explosion, entity_explosion, void, lightning, suicide, starvation, poison, magic, wither, falling_block, thorns, dragon_breath, fly_into_wall, campfire, cramming, dryout, freeze, sonic_boom, custom
# 语法：[permissionNode]:[damageCause]:[multiplier]
# 例如 nolavadamage:lava:0 会让拥有 cmi.damagecontrol.nolavadamage 权限的玩家免疫熔岩伤害
# 负数会恢复玩家生命值，而不是造成伤害
# 同一伤害原因有多个匹配权限时，使用列表中最后一个计算最终伤害
DamageControl:
  # 启用后，可调整部分伤害数值
  Enabled: false
  List:
  - nowalldamage:fly_into_wall:0.5
  - dragon:dragon_breath:0.9
```

## `Totem` { #totem }

```yaml title="config.yml · Totem"
Totem:
  # 设为 true，玩家死亡时即使未手持不死图腾，也会使用图腾
  RemoveFromInventory: false
  # 从物品栏取用图腾是否需要权限
  # 需要先将 RemoveFromInventory 设为 true；启用此项后，玩家还需要 cmi.totem.frominventory 权限
  RequirePermission: false
  Cooldown:
    # 设为 true，玩家每隔 X 秒才能使用一次不死图腾
    Use: false
    Time: 600
  Warmup:
    # 设为 true，使用图腾后获得 X 秒保护时间，在此期间死亡可以复活
    # 图腾在激活时消耗；即使在保护时间内未触发复活，也不会退还
    Use: false
    Time: 10
  # 玩家携带图腾掉入虚空时，将其传送到重生位置并消耗图腾
  ProtectFromVoid: true
  Effects:
    # 给玩家施加效果的持续时间，单位为秒；设为 0 关闭
    Regeneration: 45
    FireResistance: 40
    Absorbtion: 5
  # 这些世界中的图腾交由服务端按默认行为处理
  BlackListedWorlds:
  - "WORLD_1"
  - "WORLD_2"
  # 完全禁用图腾的世界
  FullDisableInWorlds:
  - "WORLD_1"
```

## `Elytra` { #elytra }

```yaml title="config.yml · Elytra"
Elytra:
  # cmi.elytra - 允许使用鞘翅
  # cmi.elytra.boost - 允许普通加速
  # cmi.elytra.superboost - 允许超级加速
  # cmi.elytra.speedometer - 允许查看速度表
  Boost:
    # 达到此速度后不再提供加速
    SpeedLimit: 200
    # 启用后，超出速度上限时不消耗物品或经验
    SpeedLimitStop: false
    # 速度是否显示小数
    SpeedDecimals: true
    # 每次普通加速增加的速度
    GeneralMultyplier: 0.1
    # 每次超级加速增加的速度
    # 使用普通加速时按住潜行键
    SuperMultyplier: 0.3
    # 消耗指定物品代替经验
    UseItems: false
    # 物品材质名称
    # 每次加速时消耗的物品
    ConsumedItem: STONE
    # 物品材质名称
    # 设为 AIR，允许不手持特定物品加速
    # 设为 AIR 时，仍需手持任意物品，或点击鼠标左键才能生效
    Item: FEATHER
    # 物品材质名称
    # 设为 AIR，允许不手持特定物品起飞
    # 设为 AIR 时，仍需手持任意物品，或看着方块才能正常生效
    LaunchItem: FEATHER
    # 需要手持指定物品，仅在 UseItems 为 false 时生效
    RequiresItem: true
    # 每次普通加速消耗的经验点数
    Amount: 1
    # 每次超级加速消耗的经验点数
    SuperAmount: 5
    # 飞行时显示粒子
    ShowParticles: true
  Launch:
    Time: 2
  # 适用于 1.13+：是否禁止鞘翅飞行时使用三叉戟的激流附魔
  # 这种组合可能让玩家达到极高速度
  DisableRiptide: false
  Fix:
    # 禁止飞行时通过箭矢伤害自己来加速
    PreventSelfDamage: false
    # 禁止使用烟花火箭为鞘翅加速
    PreventRocketUsage: false
```

## `FlightCharge` { #flightcharge }

```yaml title="config.yml · FlightCharge"
FlightCharge:
  # 默认持续通过 Boss 栏显示剩余飞行能量。关闭后，只在能量发生修改时显示，不在飞行消耗期间显示
  ShowBossBar: true
  # 设为 true，获得飞行能量或重新登录后，自动开启飞行模式
  # 设为 false，玩家需要手动执行 /cmi flyc 开启飞行
  EnabledByDefault: true
  # 设为 true，从生存或冒险模式切换到创造或旁观模式时，关闭飞行能量模式
  # 从创造或旁观切换回生存或冒险时，也同样处理
  AutoSwitch: false
  # 每点飞行能量消耗的经验点数。可填 0.2 等小数，但不能小于或等于 0
  # 设为 0 关闭这种补充方式
  ExpRechargeCost: 1.0
  # 每点飞行能量的价格。可填 0.2 等小数，但不能小于或等于 0
  # 设为 0 关闭这种补充方式
  MoneyRechargeCost: 1.0
  # 玩家飞行能量上限
  # 飞行时每移动一个方块消耗一点能量
  # 悬停不动时，每秒消耗一点能量
  MaxChargeLevel: 1000
  # 悬停不动时，每秒消耗能量的倍率
  # 设为 0 关闭
  DeductOnIdling: 1.0
  # 设为大于 0 的值后，按飞行秒数扣除指定能量，不再按移动距离计算
  # 设为 0 关闭固定秒耗，改按移动方块数扣除能量
  DeductOnlyForTime: 0.0
  AutoRecharge:
    # 玩家通过 /autorecharge 开启自动补充后，剩余能量低于最大值的多少百分比时触发
    From: 10.0
    # 每次自动补充的能量占上限的百分比
    # 25 表示每次触发时补充最大能量的 25%
    Amount: 25.0
  # 玩家下落时，额外扣除能量的倍率
  # 仅影响超过 3 格高度的下落
  # 例如从 10 格高度落下，扣除 7 * 2 = 14 点能量
  # 用于防止通过跳下悬崖避开能量消耗
  # 设为 0 关闭此限制
  DeductOnFallMulti: 2
  # 从超过 3 格的高度下落时，是否对玩家造成伤害
  # 即使从 200 格高度落下也不会直接死亡，最低保留 1 点生命值
  # 仅影响主动跳下的玩家，不影响在半空中关闭飞行的玩家
  DamageOnFall: true
  # 需要启用 DamageOnFall 才生效
  # 在半空中关闭飞行时，是否对玩家造成伤害
  DamageOnToggle: false
  # 需要启用 DamageOnFall 才生效
  # 摔落伤害高于剩余生命值时，是否允许玩家死亡
  KillOnFall: false
  # 填写颜色名称后，玩家开始使用飞行能量飞行时会发光
  # 设为 'none' 关闭
  GlowColor: none
```

## `Point` { #point }

```yaml title="config.yml · Point"
Point:
  # point 命令的默认粒子。可用值：fireworks_spark, smoke, dragon_breath, crit, magic_crit, potion_swirl, potion_swirl_transparent, spell, instant_spell, witch_magic, note, portal, flying_glyph, flame, lava_pop, footstep, splash, particle_smoke, explosion_huge, explosion_large, explosion, void_fog, small_smoke, cloud, coloured_dust, dust, snowball_break, waterdrip, lavadrip, snow_shovel, slime, heart, villager_thundercloud, happy_villager, large_smoke, water_bubble, water_wake, suspended, barrier, mob_appearance, end_rod, damage_indicator, sweep_attack, totem, spit, squid_ink, bubble_pop, current_down, bubble_column_up, nautilus, dolphin, water_splash, campfire_signal_smoke, campfire_cosy_smoke, sneeze, composter, flash, falling_lava, landing_lava, falling_water, dripping_honey, falling_honey, landing_honey, falling_nectar, soul_fire_flame, ash, crimson_spore, warped_spore, soul, dripping_obsidian_tear, falling_obsidian_tear, landing_obsidian_tear, reverse_portal, white_ash, light, falling_spore_blossom, spore_blossom_air, small_flame, snowflake, dripping_dripstone_lava, falling_dripstone_lava, dripping_dripstone_water, falling_dripstone_water, glow_squid_ink, glow, wax_on, wax_off, electric_spark, scrape, block_marker, sonic_boom, sculk_soul, sculk_charge_pop, cherry_leaves, small_gust, trial_spawner_detection_ominous, vault_connection, infested, item_cobweb, ominous_spawning, raid_omen, trial_omen, poof, explosion_emitter, firework, bubble, fishing, underwater, enchanted_hit, effect, instant_effect, entity_effect, witch, dripping_water, dripping_lava, mycelium, enchant, item_snowball, item_slime, item, block, rain, elder_guardian, falling_dust, totem_of_undying, dust_color_transition, vibration, sculk_charge, shriek, egg_crack, dust_plume, white_smoke, gust, gust_emitter_large, gust_emitter_small, trial_spawner_detection, dust_pillar, pale_oak_leaves, tinted_leaves, block_crumble, trail, firefly
  DefaultParticle: DUST
```

## `Messages` { #messages }

```yaml title="config.yml · Messages"
Messages:
  Login:
    # 设为 true，不显示加入消息
    Disabled: false
    # 在线人数达到多少时，自动隐藏加入消息
    # 设为 -1 关闭
    AutoHideFrom: -1
    Custom:
      # 设为 true，使用自定义加入消息；可通过 cmi.messages.disablelogin 关闭指定玩家的消息
      Use: false
      # 启用后，如果 BungeeCord 安装了 CMIB，会尝试判断玩家切服情况，并尽可能用切服消息代替加入消息
      ServerSwitch: true
  Logout:
    # 设为 true，不显示退出消息
    Disabled: false
    # 在线人数达到多少时，自动隐藏退出消息
    # 设为 -1 关闭
    AutoHideFrom: -1
    Custom:
      # 设为 true，使用自定义退出消息；可通过 cmi.messages.disablequit 关闭指定玩家的消息
      Use: false
      # 启用后，如果 BungeeCord 安装了 CMIB，会尝试判断玩家切服情况，并尽可能用切服消息代替退出消息
      ServerSwitch: true
  # 翻译及自定义占位符见语言文件：[playername]、[totalUsers]、[onlinePlayers]
  FirstJoinMessage:
    Use: false
  # 启用后，用指定正则表达式检查玩家名称，匹配时不显示相应的加入或退出消息
  Filter:
    ForLogin: false
    ForLogout: false
    Regex:
    - b[a@][s\$][t\+][a@]rd
    - (c|k|ck|q)[o0](c|k|ck|q)[s\$]u(c|k|ck|q)[e3]r
    - mast(e|ur)b(8|ait|ate)
```

## `Books` { #books }

```yaml title="config.yml · Books"
Books:
  # getbook 命令生成书籍时使用的默认作者名称
  DefaultAuthor: Server
  # 设为 true，在书籍中添加编写日期
  AddDate: false
```

## `Motd` { #motd }

```yaml title="config.yml · Motd"
# 玩家登录时显示的 customtext 名称；填入不存在的 customText 名称即可关闭
Motd: welcomeMessage
```

## `Warnings` { #warnings }

```yaml title="config.yml · Warnings"
Warnings:
  # 应始终保留。警告玩家时未指定类别，就使用此项
  Default:
    # 此警告对玩家的有效时长，单位为秒
    LifeTime: 86400
    # 每次警告给予的警告点数
    Points: 1
    # 警告时未提供原因，使用的默认原因
    DefaultReason: "&7违反服务器规则"
  Categories:
    Swear:
      LifeTime: 86400
      Points: 3
      DefaultReason: "&7说脏话"
    Grief:
      LifeTime: 86400
      Points: 10
      DefaultReason: "&7恶意破坏"
    Bug:
      LifeTime: 86400
      Points: 30
      DefaultReason: "&7利用漏洞"
    Cheat:
      LifeTime: 86400
      Points: 50
      DefaultReason: "&7使用作弊工具"
  Perform:
    '3':
    - cmi mute [playerName] 10m
    - "cmi msg [playerName] !&c因累计 &73 &c次警告，被禁言 &710 &c分钟！"
    '5':
    - "cmi kick [playerName] &c因累计 5 次警告被踢出服务器！"
    '10':
    - "cmi tempban [playerName] 5m &c因累计 10 次警告被临时封禁！"
```

## `Spawn` { #spawn }

```yaml title="config.yml · Spawn"
Spawn:
  # 玩家登录时，强制传送到指定出生点
  # 可通过 cmi.spawnonjoin.bypass 权限绕过
  SpawnOnJoin: false
  # 忽略的世界列表。玩家在这些世界登录时，保留退出位置，不传送到对应出生点
  IgnoredWorlds: []
  # 设为 true，此位置也作为死亡重生点；否则只用于 /cmi spawn
  # RespawnLocation 表示是否将此位置作为死亡后的可用重生点
  # TeleportFrom 指定从哪些世界登录的玩家会被传送到此出生点
  Main:
    Location: ''
    RespawnLocation: false
    Rng: 0
    TeleportFrom: []
  # 玩家首次加入服务器时的出生位置
  FirstSpawn:
    Use: true
    World: "WORLD"
    X: "X"
    Y: "Y"
    Z: "Z"
    Pitch: "PITCH"
    Yaw: "YAW"
```

## `Newbie` { #newbie }

```yaml title="config.yml · Newbie"
Newbie:
  # 给予新玩家的礼包名称
  Kit: Newbie
```

## `Kits` { #kits }

```yaml title="config.yml · Kits"
Kits:
  # 设为 true，通过界面显示礼包列表，而不是聊天消息
  GUI: true
  # 设为 true，用默认物品填充礼包选择界面的空槽，见 CMILib
  FillEmptyFields: true
  # 启用后，玩家可预览有权领取的礼包，或具有 cmi.kit.[kitName].preview、cmi.kit.[kitName].* 权限的礼包
  KitPreview: true
  # {DATE} 的显示格式
  DateFormat: yyyy-MM-dd HH:mm:ss
  Buttons:
    # 礼包预览界面的图标
    # 将图标设为无效物品可隐藏按钮
    Cooldown: Watch
    Usages: STONE_PLATE
    Money: GOLD_INGOT
    Exp: EXP_BOTTLE
    Desc: GreenWool
    Back: Fence
  Complex:
    CloseButton:
      Use: true
      Slot: 9
      Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmNjYmY5ODgzZGQzNTlmZGYyMzg1YzkwYTQ1OWQ3Mzc3NjUzODJlYzQxMTdiMDQ4OTVhYzRkYzRiNjBmYyJ9fX0=
      Commands:
      - closeinv!
    InfoButton:
      # 额外按钮，可用于点击后显示补充信息
      Use: false
      Slot: 1
      Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDZiYTYzMzQ0ZjQ5ZGQxYzRmNTQ4OGU5MjZiZjNkOWUyYjI5OTE2YTZjNTBkNjEwYmI0MGE1MjczZGM4YzgyIn19fQ==
      Commands:
      - closeinv!
```

## `Warps` { #warps }

```yaml title="config.yml · Warps"
Warps:
  # 设为 true，通过界面显示传送点列表，而不是聊天消息
  GUI: true
  # 创建新传送点后自动打开界面
  GUIOnCreation: true
  # 传送点名称的最小长度
  MinLength: 4
  # 传送点名称的最大长度
  MaxLength: 16
  # 每页显示的传送点数量
  perPage: 50
  # 是否在传送点列表中显示创建者
  showCreator: false
  # 设为 true，新建传送点默认需要权限才能使用
  requirePerm: false
  Complex:
    CloseButton:
      Use: true
      Slot: 9
      Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmNjYmY5ODgzZGQzNTlmZGYyMzg1YzkwYTQ1OWQ3Mzc3NjUzODJlYzQxMTdiMDQ4OTVhYzRkYzRiNjBmYyJ9fX0=
      Commands:
      - closeinv!
    InfoButton:
      # 额外按钮，可用于点击后显示补充信息
      Use: false
      Slot: 1
      Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDZiYTYzMzQ0ZjQ5ZGQxYzRmNTQ4OGU5MjZiZjNkOWUyYjI5OTE2YTZjNTBkNjEwYmI0MGE1MjczZGM4YzgyIn19fQ==
      Commands:
      - closeinv!
```

## `DynamicViewRange` { #dynamicviewrange }

```yaml title="config.yml · DynamicViewRange"
DynamicViewRange:
  # 设为 true，启用动态视距。此功能仍为测试版，可能增加 CPU 负载
  # 服务器不使用此功能时，请不要开启
  Enabled: false
```

## `WorldLimits` { #worldlimits }

```yaml title="config.yml · WorldLimits"
WorldLimits:
  # 设为 true，切换世界时，对没有相应绕过权限的玩家应用该世界的飞行和游戏模式限制
  Enabled: false
  # 各世界的默认游戏模式
  # 拥有 cmi.worldlimit.gamemode.bypass 权限时，不改变游戏模式
  # 可用模式：creative、survival、adventure、spectator
  Gamemode:
  - "WORLD_1:Survival"
  # 拥有 cmi.worldlimit.fly.bypass 权限时，不改变飞行状态
  Fly:
  - "WORLD_1:False"
  # 启用后，玩家死亡前正在飞行，重生后仍可飞行
  ReenabledFlyAfterDeath: false
  # 拥有 cmi.worldlimit.elytra.bypass 权限时，不限制鞘翅飞行
  # 进入禁用鞘翅飞行的世界时，会尽可能卸下玩家的鞘翅
  ElytraFlight:
  - "WORLD_1:False"
  # 设为 false，只有拥有 cmi.worldlimit.fly.aboveroof 权限的玩家才能飞到世界建造高度以上
  FlyAboveRoof: true
  # 设为 false，只有拥有 cmi.worldlimit.fly.aboveroof 权限的玩家才能飞到世界建造高度以上
  FlyAboveRoofLimitations:
  - "WORLD_1-320"
  - "WORLD_2-128"
  - "WORLD_3-256"
  # 拥有 cmi.worldlimit.god.bypass 权限时，不改变上帝模式
  GodMode:
  - "WORLD_1:False"
  # 在指定世界阻止特定原因的实体生成。可用原因：NATURAL, JOCKEY, CHUNK_GEN, SPAWNER, TRIAL_SPAWNER, EGG, SPAWNER_EGG, LIGHTNING, BUILD_SNOWMAN, BUILD_IRONGOLEM, BUILD_COPPERGOLEM, BUILD_WITHER, VILLAGE_DEFENSE, VILLAGE_INVASION, BREEDING, SLIME_SPLIT, REINFORCEMENTS, NETHER_PORTAL, DISPENSE_EGG, INFECTION, CURED, OCELOT_BABY, SILVERFISH_BLOCK, MOUNT, TRAP, ENDER_PEARL, SHOULDER_ENTITY, DROWNED, SHEARED, EXPLOSION, RAID, PATROL, BEEHIVE, PIGLIN_ZOMBIFIED, SPELL, FROZEN, METAMORPHOSIS, DUPLICATION, COMMAND, ENCHANTMENT, OMINOUS_ITEM_SPAWNER, BUCKET, POTION_EFFECT, REANIMATE, REHYDRATION, CUSTOM, DEFAULT
  SpawnReasons:
    world:
    - None
    world_nether:
    - None
    world_the_end:
    - None
```

## `CheckForNameChange` { #checkfornamechange }

```yaml title="config.yml · CheckForNameChange"
# 检查玩家名称是否与上次记录的不同
CheckForNameChange:
  # 是否执行命令
  PerformCommandsOnNewName: false
  # 玩家使用新名称登录时执行的命令
  NameChangeCommands:
  - "asConsole! cmi broadcast !&2[oldname] 已使用新名字 [newname] 登录"
```

## `inv` { #inv }

```yaml title="config.yml · inv"
inv:
  # 是否在玩家死亡时保存物品栏
  SaveOnDeath: false
  # 设为 true，死亡时物品栏为空则不保存
  IgnoreEmpty: false
  # 设为 true，玩家必须拥有 cmi.saveinv 权限，死亡时才保存物品栏
  RequiresPermission: false
  # 每名玩家保留的物品栏记录数量
  SavedInventories: 5
  restore:
    # 设为 false，通过 /cmi invload 恢复物品栏时不恢复生命值
    HP: true
    # 设为 false，不恢复经验点数
    XP: true
    # 设为 false，不恢复饥饿值
    Food: true
    # 设为 false，不恢复饱和度
    Saturation: true
    # 设为 false，不恢复药水效果
    Potions: true
    # 设为 false，不恢复物品
    Items: true
    # 不保存的材质列表
    # 羊毛、潜影盒等有颜色变种的物品，可能需要列出每种颜色的材质
    BlackListedItems:
    - ''
```

## `hunger` { #hunger }

```yaml title="config.yml · hunger"
hunger:
  # 是否允许玩家的饥饿值超过 20
  overide: false
```

## `heal` { #heal }

```yaml title="config.yml · heal"
heal:
  RemoveNegative:
    # 治疗玩家时，是否移除负面药水效果
    use: true
    List:
    - blindness
    - confusion
    - harm
    - hunger
    - poison
    - slow
    - slow_digging
    - weakness
    - wither
```

## `Cuff` { #cuff }

```yaml title="config.yml · Cuff"
Cuff:
  # 设为 false，允许被铐住的玩家聊天
  Mute: true
  AllowedCommands:
  - msg
  - r
  - tell
```

## `Mute` { #mute }

```yaml title="config.yml · Mute"
Mute:
  # 设为 true，被禁言的玩家也无法发送私聊
  DenyPrivateMessages: true
```

## `Dispose` { #dispose }

```yaml title="config.yml · Dispose"
Dispose:
  # 垃圾桶界面的行数，范围为 1–6
  UILines: 4
  # 是否允许丢弃带附加指令的物品
  CustomModelData: true
  AttachedCommands: true
  # 禁止丢弃的材质黑名单
  Materials: []
```

## `ItemRepair` { #itemrepair }

```yaml title="config.yml · ItemRepair"
ItemRepair:
  RepairShare:
    # 开启后需要完整重启服务器才生效
    # 启用后，阻止玩家通过普通铁砧为其他人修复物品；本人修复后自己使用不受影响
    # 可通过 cmi.command.repair.repairshare.bypass 绕过
    ProtectNormalRepair: false
    # 启用后，阻止玩家通过 CMI 命令为其他人修复物品；本人修复后自己使用不受影响
    ProtectCommandRepair: false
    # 其他玩家拾取或在物品栏中选中物品时，将耐久度设为此值。设为 0 或更小的值不修改耐久度
    # 注意！应保持大于 0，否则物品会直接消失，玩家无法再通过其他方式修复，除非这正是预期行为
    Durability: 1
    # 设为 true，拥有 cmi.command.repair 权限的玩家可绕过保护，直接使用由其他玩家修复的物品
    BypassWithRepairPermission: true
    # 启用后，玩家不能使用该物品时会追加一行描述；物品所有者不会看到这行提示
    AddLore: true
    # 设为 true，取消交互事件，阻止使用物品
    CancelEvent: true
    # 设为 true，提示玩家该物品并非由自己修复
    InformWithMessage: true
  Repair:
    # 禁止通过 /repair 修复的自定义模型数据 ID 列表
    BlockedCustomDataID:
    - 298785423
    # 修复需要付费时，玩家必须点击聊天消息确认
    Confirmation: true
    # 设为 true，/cmi repair 按以下设置收取费用
    # 执行命令的玩家支付费用
    # 从控制台执行时，由被修复物品所属的玩家支付费用
    CostsMoney: false
    # 物品的基础修复价格
    # 启用耐久度检查后，此费用会根据物品损坏程度变化
    BasePrice: 100.0
    # 根据物品损坏程度计算修复费用
    CheckDurability: true
    # 根据 /cmi setworth 设置的物品价格追加费用
    # 取值范围为 0 到 100
    WorthPercentage: 10.0
    # 根据 /cmi setenchantworth 设置的附魔价格追加费用
    # 取值范围为 0 到 100
    # 有多个附魔时，将各项费用相加
    enchantWorthPercentage: 10.0
```

## `Cooldowns` { #cooldowns }

```yaml title="config.yml · Cooldowns"
Cooldowns:
  # 可以为任意命令设置冷却，防止连续立即使用
  # cmi heal:180 表示每 180 秒只能执行一次 /cmi heal
  # 冷却设为 -1 时，该命令只能执行一次
  # 管理员可通过 cmi.cooldownbypass.[commandname] 绕过
  # 始终使用完整命令名称，不要使用别名
  # ----------
  # 也可使用 cmi.cooldown.[some_command].[timer] 权限，例如 cmi.cooldown.cmi_heal.30 为 /cmi heal 设置 30 秒冷却
  # 要在带参数时才应用冷却，在命令末尾加 _。例如 cmi.cooldown.cmi_heal_.30 只限制治疗其他玩家的用法
  # 注意！必须先在列表中设置基础命令冷却，权限才会生效
  # -----
  # 注意！若要限制 /cmi home 传送，但不限制打开界面，在命令后保留空格，例如 "cmi home :10"
  Enabled: false
  List:
  - cmi heal:180
  - cmi feed:120
```

## `ShulkerBoxes` { #shulkerboxes }

```yaml title="config.yml · ShulkerBoxes"
ShulkerBoxes:
  # 设为 true，战斗期间不允许打开潜影盒
  # 战斗判定时间可在 combat 部分设置
  PreventInCombat: true
  # 设为 true，从物品栏编辑潜影盒内容需要 cmi.openshulker.edit 权限
  RequirePermission: false
  # 从物品栏打开潜影盒的费用，余额不足时不允许打开
  # 设为 0 关闭费用要求
  # 可通过 cmi.openshulker.free 权限绕过
  CostToOpen: 0.0
```

## `Vanish` { #vanish }

```yaml title="config.yml · Vanish"
Vanish:
  # 隐身编辑选项的默认状态
  # 玩家已经用 vanishedit 修改过隐身选项时，不受此默认值影响
  Defaults:
    damageToEntity: false
    playerDamage: false
    itemPickup: false
    mobAggro: false
    interaction: false
    noisyChest: false
    informOnLeave: false
    informOnJoin: false
    nightVision: true
    bossbar: true
    afkcommands: false
    PrivateMessages: false
    relogDisable: false
    noMessages: false
    fakeJoinLeave: false
    mobSpawning: false
    stopPlaytime: true
    sleepIgnore: true
    joinVanished: false
    deathMessages: false
    hookPlayers: false
```

## `Player` { #player }

```yaml title="config.yml · Player"
Player:
  Options:
    CloseButton:
      Use: true
      Slot: 9
      Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmNjYmY5ODgzZGQzNTlmZGYyMzg1YzkwYTQ1OWQ3Mzc3NjUzODJlYzQxMTdiMDQ4OTVhYzRkYzRiNjBmYyJ9fX0=
      Commands:
      - closeinv!
    InfoButton:
      # 额外按钮，可用于点击后显示补充信息
      Use: false
      Slot: 1
      Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDZiYTYzMzQ0ZjQ5ZGQxYzRmNTQ4OGU5MjZiZjNkOWUyYjI5OTE2YTZjNTBkNjEwYmI0MGE1MjczZGM4YzgyIn19fQ==
      Commands:
      - closeinv!
    # 玩家选项的默认状态
    # 玩家已经用 /cmi options 修改过选项时，不受此默认值影响
    Defaults:
      visibleHolograms: true
      shiftSignEdit: true
      totemBossBar: true
      bossBarCompass: true
      tagSound: true
      # 强烈不建议启用！
      chatSpy: false
      # 强烈不建议启用！
      cmdSpy: false
      # 强烈不建议启用！
      signSpy: false
      acceptingPM: true
      acceptingTPA: true
      acceptingMoney: true
      chatbubble: true
      pmSound: true
      rideMe: true
      pveDamageNumbers: true
      pvpDamageNumbers: true
      InformDurability: true
      receivePets: true
      deathMessages: true
      notarget: false
      showVehicleSpeed: false
      tpauto: false
    Icons:
      visibleHolograms: BLACK_STAINED_GLASS
      shiftSignEdit: OAK_SIGN
      totemBossBar: TOTEM_OF_UNDYING
      bossBarCompass: COMPASS
      tagSound: PAPER
      chatSpy: BUCKET
      cmdSpy: WATER_BUCKET
      signSpy: LAVA_BUCKET
      acceptingPM: MAP
      acceptingTPA: CLOCK
      acceptingMoney: KNOWLEDGE_BOOK
      chatbubble: LANTERN
      pmSound: STONE_BUTTON
      rideMe: SADDLE
      pveDamageNumbers: WOODEN_SWORD
      pvpDamageNumbers: DIAMOND_SWORD
      InformDurability: ANVIL
      receivePets: LEAD
      deathMessages: DEAD_BUSH
      notarget: BEDROCK
      showVehicleSpeed: MINECART
      tpauto: ENDER_PEARL
```

## `WarmUps` { #warmups }

```yaml title="config.yml · WarmUps"
WarmUps:
  # 可以为任意命令设置预热，避免立即执行
  # tp:5:false 表示执行 /tp 后等待 5 秒，且不能移出当前方块
  # tp:5:false-3 表示执行 /tp 后等待 5 秒，期间只能在原位置 3 格以内移动
  # false 为可选参数，设为 false 时预热期间禁止移动
  # 若只限制带参数的 warp，而不限制无参数用法，在命令后加空格，例如 'warp :5:false'
  # 为 CMI 命令设置预热时，使用完整命令而非别名，例如 'cmi warp:5:false'
  # 管理员可通过 cmi.warmupbypass.[commandname] 绕过
  # 注意！cmi home 使用特殊处理方式，请添加空格以避免重复预热，例如：- cmi home :5:false
  # 实验性功能：在预热设置中添加 GlyphHead，可在预热期间显示粒子效果，例如
  # - cmi warp :3:false:GlyphHead
  Enabled: false
  InformOnNoMove: true
  Disable:
    OnInventoryOpen: true
  showCounterBarInfo: false
  BossBarInfo:
    Enabled: false
    Color: blue
    # 可用值：1、6、10、12、20
    Segments: '1'
  List:
  - cmi tp :5:false
  - cmi back:3:true
  - cmi warp :3:false
  - cmi home :3:false
  - cmi home :3:false-2
```

## `Jail` { #jail }

```yaml title="config.yml · Jail"
Jail:
  # 检查玩家是否离开监狱区域的间隔，单位为毫秒
  # 数值较大可略微降低服务器负载
  CheckInterval: 500
  # 命令未提供时长时使用的默认监禁时间
  DefaultTime: 300
  # 监禁期间的聊天范围，单位为方块
  # 设为 0 允许聊天
  # 设为 -1，监禁期间完全禁止聊天
  ChatRange: 20
  # 设为 true，玩家离线时也计入服刑时间
  # 设为 false，只在玩家在线时减少剩余刑期
  CountWhileOffline: false
  # 设为 true，监禁期间进入 AFK 状态时，不减少剩余刑期
  # 设为 false，照常计算时间
  NoAfk: false
  # 监禁期间是否阻止玩家受到伤害
  PreventDamage: true
  # 监禁期间是否阻止玩家饥饿
  PreventHunger: true
  Commands:
    # 玩家入狱时执行的命令
    OnJail:
    - ''
    # 玩家出狱时执行的命令
    OnUnJail:
    - ''
  # 将 CMI 命令加入白名单时，使用完整名称，不要使用缩写别名
  WhiteListedCmds:
  - cmi msg
  - cmi reply
```

## `scan` { #scan }

```yaml title="config.yml · scan"
scan:
  # 低于此 TPS 时，开始调整扫描速度
  SoftCap: 19.0
  # 初始扫描速度，范围为 1 到 30
  DefaultSpeed: 15
  # 范围单位为区块：2 表示 9 个区块（3x3），1 表示当前区块，0 表示全局扫描
  DefaultRange: 2
  # 启用后，将 scan 结果写入文件，便于之后查看
  LogIntoFile: false
```

## `search` { #search }

```yaml title="config.yml · search"
search:
  # 启用后，将 search 结果写入文件，便于之后查看
  LogIntoFile: false
  # 设为 true，搜索时删除找到的物品，例如 /cmi search diamondaxe purge
  EnablePurge: false
```

## `purge` { #purge }

```yaml title="config.yml · purge"
# removeuser 在删除或移动玩家数据文件时，也使用相同配置
purge:
  # 服务器启动时清理文件
  CleanOnStart: false
  # 玩家离线多久后移动其数据
  OfflineDays: 90
  CMIData:
    # 是否清理 CMI 中的玩家数据记录
    Enabled: false
  PlayerData:
    # 是否清理玩家数据文件
    Enabled: true
    # 读取文件的来源文件夹
    SourceFolder: world/playerdata
    # 设为 false，将文件移动到备份文件夹；设为 true，直接删除
    DeleteFiles: false
    # DeleteFiles 为 false 时，文件移动到的目标文件夹
    DestinationFolder: world/playerdata_backup
  PlayerStats:
    # 是否清理玩家统计文件
    Enabled: true
    # 读取文件的来源文件夹
    SourceFolder: world/stats
    # 设为 false，将文件移动到备份文件夹；设为 true，直接删除
    DeleteFiles: false
    # DeleteFiles 为 false 时，文件移动到的目标文件夹
    DestinationFolder: world/stats_backup
  PlayerAdvancements:
    # 是否清理玩家进度文件
    Enabled: true
    # 读取文件的来源文件夹
    SourceFolder: world/Advancements
    # 设为 false，将文件移动到备份文件夹；设为 true，直接删除
    DeleteFiles: false
    # DeleteFiles 为 false 时，文件移动到的目标文件夹
    DestinationFolder: world/Advancements_backup
  Essentials:
    # 是否清理 Essentials 玩家数据文件
    Enabled: false
    # 读取文件的来源文件夹
    SourceFolder: plugins/Essentials/userdata
    # 设为 false，将文件移动到备份文件夹；设为 true，直接删除
    DeleteFiles: false
    # DeleteFiles 为 false 时，文件移动到的目标文件夹
    DestinationFolder: plugins/Essentials/userdata_backup
  LWC:
    # 是否清理 LWC 保护记录
    Enabled: false
```

## `Selection` { #selection }

```yaml title="config.yml · Selection"
Selection:
  # 选择区域时使用的工具材质名称
  Tool: wooden_shovel
```

## `Time` { #time }

```yaml title="config.yml · Time"
Time:
  # 预设时间
  Day: '12:00'
  Night: '24:00'
  Morning: 06:00
  Dusk: '18:00'
  AutoTime:
    # 将游戏时间与现实时间同步的间隔，单位为秒
    # 建议保持在约一分钟
    Interval: 60
    # 默认使用太阳平滑移动的方式切换时间
    # 可通过 time 命令的 -smooth 参数覆盖
    Smooth: true
    # 平滑切换速度
    # 100 表示太阳以正常速度的 100 倍移动，直到目标时间
    SmoothSpeed: 100
    # 自动时间同步影响的世界
    Worlds:
    - ''
  # 可以按需求修改原版时间流逝速度
  TimeSpeed:
    # 单位为秒。原版游戏内 24 小时对应现实中的 1200 秒
    world:
      Enabled: false
      # 默认值：600；开始于第 0 刻，结束于第 12000 刻
      day: 600
      # 默认值：90；开始于第 12000 刻，结束于第 13800 刻
      sunset: 90
      # 默认值：420；开始于第 13800 刻，结束于第 22200 刻
      night: 420
      # 默认值：90；开始于第 22200 刻，结束于第 24000 刻
      sunrise: 90
```

## `Enchanting` { #enchanting }

```yaml title="config.yml · Enchanting"
Enchanting:
  enchantLimits:
    # 关闭后，不再对附魔施加限制
    # 仅影响 enchant 命令，不影响正常附魔
    Enabled: true
    MaxLevel:
      density: 5
      swift_sneak: 3
      breach: 4
      protection_fall: 4
      arrow_infinite: 1
      arrow_fire: 1
      impaling: 5
      protection_environmental: 4
      knockback: 2
      depth_strider: 3
      luck: 3
      silk_touch: 1
      loyalty: 3
      vanishing_curse: 1
      protection_fire: 4
      channeling: 1
      binding_curse: 1
      quick_charge: 3
      damage_arthropods: 5
      frost_walker: 2
      multishot: 1
      protection_projectile: 4
      water_worker: 1
      soul_speed: 3
      wind_burst: 3
      loot_bonus_mobs: 3
      damage_undead: 5
      piercing: 4
      lure: 3
      lunge: 3
      riptide: 3
      arrow_damage: 5
      protection_explosions: 4
      mending: 1
      fire_aspect: 2
      oxygen: 3
      thorns: 3
      sweeping_edge: 3
      arrow_knockback: 2
      damage_all: 5
      dig_speed: 5
      loot_bonus_blocks: 3
      durability: 3
  # 设为 true，需要 cmi.enchantments.[enchantname] 权限
  RequireSpecificPermission: false
  # 启用后，只允许对物品添加适用的附魔
  # 可通过 cmi.command.enchant.bypassinvalid 绕过
  EnforceValidEnchants: true
  # 设为 true，需要 cmi.enchantments.[enchantname].[maxlevel] 权限才能附魔到指定最高等级
  # 有多个匹配权限时，取最高等级
  # 不会阻止玩家附魔到低于权限上限的等级
  # 没有指定等级权限的玩家，默认仍可使用 1 级附魔
  PermissionLevelLimit: false
```

## `BungeeCord` { #bungeecord }

```yaml title="config.yml · BungeeCord"
BungeeCord:
  # 若遇到问题，可以完全关闭 BungeeCord 支持
  # 设为 false 后，跨服公共消息、私聊、传送门等功能会停止工作
  # 这些功能在单个服务器内的普通用法不受影响
  Enabled: false
  TabComplete:
    # 设为 true，将整个 BungeeCord 网络的玩家名称加入 Tab 补全
    PlayerNames: false
    # 纳入 Tab 补全的服务器列表
    # 留空表示包含全部服务器
    Servers: []
  # 启用后，/back 可返回上一台服务器，而不只是该服内的上一个位置
  # 仅在玩家切入该服后尚未再次传送时生效
  BackToPreviousServer: false
```

## `Recipes` { #recipes }

```yaml title="config.yml · Recipes"
Recipes:
  Condense:
    # 压缩或解压物品时，检查是否有逆向配方，不能还原时不允许操作
    # 关闭后，忽略逆向配方检查
    # 关闭可能出现非预期结果，例如将 4 块木板转换成工作台
    RequireBackwards: true
    # 是否压缩由 4 个相同材料组成的配方
    # 启用此项且 RequireBackwards 关闭时，橡木木板可能被转换成工作台
    4Sized: true
```

## `BlueMap` { #bluemap }

```yaml title="config.yml · BlueMap"
BlueMap:
  Warps:
    # 是否在 BlueMap 中显示传送点
    # 大多数设置需要重启服务器才生效
    Enabled: true
    ToggledOffDefault: false
    # BlueMap 标记的名称
    Label: CMIWarps
    # 图标文件路径；图标大小通常约为 32x32 像素
    Icon: https://www.zrips.net/ICON_Warp.png
    # 此值通常应为图标尺寸的一半
    IconAnchor: 16
    # 不显示的传送点名称列表。隐藏的传送点默认已不显示
    BlackList: []
```

## `Sounds` { #sounds }

```yaml title="config.yml · Sounds"
# 若要完全关闭某个声音，设为 ""
Sounds:
  Enabled: true
  WarpGuiOpen: entity_bat_takeoff:0.5:1
  TeleportHome: block_beacon_activate:2:1
  TeleportWarp: entity_enderman_teleport:0.5:1
  TeleportSpawn: entity_enderman_teleport:0.5:1
  TeleportFail: entity_villager_no:2:1
  PrivateMessage: entity_endermite_death:2:1
  TpaRequest: block_anvil_land:0.5:2
  MailNotification: entity_creeper_hurt:1:0.5
  TeleportUp: entity_enderman_teleport:2:1
  TeleportDown: entity_enderman_teleport:0.2:1
  CommandWarmup: blockrespawnanchorcharge:1:1
  CommandWarmupRunning: blockrespawnanchorcharge:1:1
  CommandCooldown: blocknoteblockpling:0.5:0.5
```

## `PotionEffects` { #potioneffects }

```yaml title="config.yml · PotionEffects"
PotionEffects:
  # 设为 true，玩家离线时药水效果也继续计时
  # 药水效果剩余时间在登录时更新，因此查看离线玩家效果时，可能显示不准确
  DeductWhileOffline: false
```
