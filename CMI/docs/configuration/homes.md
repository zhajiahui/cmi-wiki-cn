---
title: 家（Homes.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/Homes.yml
---

# 家（Homes.yml）

文件：`plugins/CMI/Settings/Homes.yml`

连接信息、玩家标识和世界示例已使用占位符，使用时按本地配置填写。

## `Homes` { #homes }

```yaml title="Homes.yml · Homes"
Homes:
  # 启用后，覆盖同名家的位置前，要求玩家点击游戏内聊天消息确认
  # 也可直接执行 /cmi sethome [homeName] -override 确认
  Confirmation: true
  # /sethome [homeName] [slotNumber] 创建家时，允许指定的最大槽位编号
  MaxGuiSlots: 99
  Gui:
    # 已保存多个家时，执行 /cmi home 打开界面
    Use: true
    Options:
      # 启用后，家的界面区域从 10 个槽位扩展为 28 个
      Expanded: false
      # 留空则使用全局填充材质
      Border: ''
      # 界面未展开时，家的图标周围使用的材质
      Infill: WHITE_STAINED_GLASS_PANE
      InfoButton:
        # 额外按钮，可用于点击后显示补充信息
        Use: false
        Slot: 1
        Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDZiYTYzMzQ0ZjQ5ZGQxYzRmNTQ4OGU5MjZiZjNkOWUyYjI5OTE2YTZjNTBkNjEwYmI0MGE1MjczZGM4YzgyIn19fQ==
        Commands:
        - closeinv!
      CloseButton:
        Use: true
        Slot: 9
        Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmNjYmY5ODgzZGQzNTlmZGYyMzg1YzkwYTQ1OWQ3Mzc3NjUzODJlYzQxMTdiMDQ4OTVhYzRkYzRiNjBmYyJ9fX0=
        Commands:
        - closeinv!
      bedButton:
        Use: true
        Slot: 4
        Material: LIGHT_BLUE_BED
      homeButton:
        Use: true
        Slot: 5
        Material: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTJkN2E3NTFlYjA3MWUwOGRiYmM5NWJjNWQ5ZDY2ZTVmNTFkYzY3MTI2NDBhZDJkZmEwM2RlZmJiNjhhN2YzYSJ9fX0=
      deathButton:
        Use: true
        Slot: 6
        Material: TOTEM_OF_UNDYING
      backButton:
        Use: true
        Slot: 7
        Material: BONE
      prevButton:
        Slot: 46
      middleButton:
        Slot: 50
      nextButton:
        Slot: 54
  # 家数量上限组，权限为 cmi.command.sethome.[groupname]
  # 找不到玩家所属上限组时，数量设为 1
  # 使用 cmi.command.sethome.unlimited 获得不限数量的家
  # 也可直接使用数字权限 cmi.command.sethome.[number]，指定家的数量上限
  Groups:
    Newbie: 2
    Advanced: 3
    Vip: 5
  Limits:
    # 超过数量上限时，禁止使用家
    # 已拥有的家超过上限时，不允许传送回家
    BlockExtraHomes: true
    # 登录时提醒玩家已超过上限
    NotifyOnLogin: true
  # 需要 cmi.bedhome 权限
  # 设为 true，与床交互时创建普通的家位置
  # 设为 false，设置原版床重生位置
  BedInteraction: true
  # 设为 true，只有潜行点击床才设置家
  onlyShiftBed: false
  # 点击床创建家时，移除原版床重生位置
  RemoveBedLocationOnBedBreak: true
  # 启用后，创建家之前检查玩家是否能在该区域破坏方块
  # 可用于阻止在受保护区域设置家
  # 可通过 cmi.command.sethome.bypass 绕过
  CheckBlockBreak: false
  # 默认家的名称，默认为 "Home"
  DefaultName: Home
  # 床位置对应的家名称，默认为 "Home"
  # 可用不同名称，区分通过床交互设置的家与通过命令创建的家
  DefaultBedName: Home
  # 家名称允许使用的字符
  ValidNameRegex: '[^a-zA-Z0-9\-\_]'
  WorldLimits:
    # 启用后，按以下条件限制创建家
    # 可通过 cmi.command.sethome.bypasslimit 绕过
    Use: false
    Groups:
      Example1:
        # 此世界组中允许的家数量。设为 0，基本等于禁止在这些世界创建家；小于 0，则完全忽略该世界组
        Amount: 3
        # 应用限制的世界列表，可填写多个世界组成一组
        Worlds:
        - "WORLD_1"
      Example2:
        Amount: 5
        Worlds:
        - "WORLD_1"
        - "WORLD_2"
```
