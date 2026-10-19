---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 2.0.43-SNAPSHOT (build 4210)
---

# config.yml

文件：`config.yml`。版本：`2.0.43-SNAPSHOT (build 4210)`。

主配置。

## `npc` { #npc }

```yaml title="config.yml · npc（1/3）"
# Citizens 配置

npc:
  # 始终使用全息文字显示名称，而不只在使用十六进制颜色或占位符时使用
  always-use-name-holograms: false
  default:
    # Boss 血条的默认范围，单位为方块
    bossbar-view-range: 64
    # 破坏方块时使用的默认半径，单位为方块
    # 大于 0 时，NPC 会寻路到与目标方块相距此距离的位置
    block-breaker-radius: -1
    waypoints:
      # 是否默认缓存 /npc path 的路径
      # 可省去重复使用的固定路径的寻路过程
      cache-paths: false
    look-close:
      # 是否默认启用注视附近玩家
      enabled: false
      # 注视附近玩家的默认范围，单位为方块
      range: 10
      # 是否默认启用随机注视
      random-look-enabled: false
      # 随机注视的默认间隔
      random-look-delay: 3s
      # 注视玩家时是否默认检查视线是否被遮挡
      realistic-looking: false
      # 寻路时是否禁用注视附近玩家
      disable-while-navigating: true
    talk-close:
      # 是否默认与附近玩家交谈
      random-talker: false
      enabled: false
      # 与附近玩家交谈的默认范围，单位为方块
      range: 5
      text:
      - "你好，我是 <npc>！"
    # 实体生成后的默认无敌时长，Minecraft 默认值为 20 tick
    spawn-invincibility-duration: 1s
    # 创建 NPC 的默认费用
    npc-cost: 100.0
    # 生成时是否重置 NPC 的水平朝向（yaw）
    # 由于 Minecraft 的限制，目前通过挥臂动画实现
    reset-yaw-on-spawn: true
    enable-scoreboard-teams: true
  chat:
    options:
      # 即使文本是对特定玩家说的，附近玩家是否也能听到
      bystanders-hear-targeted-chat: false
      # 向旁观者显示的目标名称数量
      max-number-of-targets-to-show: 2
      multiple-targets-format: "<target>|, <target>| & <target>| & 其他人"
      # 附近玩家的范围，单位为方块
      range: 5
      # 是否在与玩家交谈之外，也与 NPC 交谈（从而让旁观者也能听到）
      talk-to-npcs: true
    format:
      # 默认文本格式（支持占位符）
      no-targets: '[<npc>]: <text>'
      # 附近玩家看到的默认文本格式（支持占位符）
      with-target-to-bystanders: '[<npc>] -> [<target>]: <text>'
      # 面向指定对象的文本的默认格式（支持占位符）
      to-target: '<npc>: <text>'
      # 附近玩家看到的默认文本格式（支持占位符）
      with-targets-to-bystanders: '[<npc>] -> [<targets>]: <text>'
```

```yaml title="config.yml · npc（2/3）"
npc:
  pathfinding:
    citizens:
      # 每 tick 进行寻路计算的方块数量
      blocks-per-tick: 250
      # 异步寻路使用的区块在内存中的保留时长。
      # 如果预计区块会在寻路期间频繁变化，请减小此值；如果区块很少变化，可增大此值，但会占用更多内存。
      async-chunk-cache-expiry: 5s
      # 寻路时是否检查碰撞箱，例如穿过栅栏间隙、门内或其他半格空间时
      check-bounding-boxes: false
      # 寻路时是否模拟跳跃；会增加寻路的 CPU 开销。
      # 推荐使用异步寻路器。目前仍为实验性功能。
      experimental-jumps: false
      # 寻路时最多检查的方块数量
      maximum-search-blocks: 1024
      # 寻路时是否开门（也应在通过后关门）
      open-doors: false
    # 通过显示虚假的目标方块调试寻路
    debug-paths: false
    # NPC 距离目的地达到此默认距离时，会直接传送到目的地，单位为方块
    # 适用于需要精确到达目的地的情况
    default-destination-teleport-margin: -1
    # NPC 移动到距离路径终点多远时视为路径已走完，默认移动距离以方块为单位
    # 注意：这与 path-distance-margin 指定的寻路距离不同
    default-distance-margin: 1
    # NPC 判定寻路完成时使用的默认寻路距离，单位为方块
    # 注意：这与 distance-margin 指定的移动距离不同
    # 如果想尝试精确寻路到目标目的地，请设为 0
    default-path-distance-margin: 0
    # 目标为实体等动态目标时，重新寻路的间隔
    update-path-rate: 1s
    # 默认寻路范围，单位为方块
    # 为避免卡顿，不宜设得过高；可尝试将路径分成较短的路段进行寻路
    default-range-blocks: 100.0
    # NPC 在同一位置停留多久后，会判定自身卡住且寻路失败的默认时长
    default-stationary-duration: -1
    # NPC 在距离目标多远时会停止寻路，改为直接朝目标行走，单位为方块
    # 目前仅适用于实体等动态目标
    straight-line-targeting-distance: 5
    # NPC 找不到路径或在同一方块中停留过久时，默认执行的动作
    # 支持的选项为：'teleport to destination' 或 'none'
    default-stuck-action: none
    minecraft:
      # 寻路到某个方块时，如果找不到直达路径，Minecraft 会选择一个“足够接近”的位置
      # 默认禁用
      disable-fallback-navigation: true
      # 寻路时最多检查的方块数量
      maximum-search-blocks: 1024
    # 开始攻击目标前的距离范围，单位为方块
    attack-range: 1.75
    # 寻路时默认允许的最大下落距离；设为 -1 使用默认值
    allowed-fall-distance: -1
    # 寻路器类型。
    # 可选值：CITIZENS、CITIZENS_ASYNC 或 MINECRAFT。
    # CITIZENS_ASYNC 是速度更快的新选项，但需要多个处理器核心和更多内存。
    pathfinder-type: MINECRAFT
  controllable:
    # 在地面上控制 NPC 时，移动速度的提升百分比
    ground-direction-modifier: 1.0
    # 可操控 NPC 能达到的最大飞行速度，使用 Minecraft 速度单位
    max-flying-speed: 0.75
    # 可操控 NPC 能达到的最大速度，使用 Minecraft 速度单位
    max-ground-speed: 0.5
    # 是否通过移动操作改变载具方向，而不是使用侧移操作
    use-boat-controls: true
  hologram:
    # 全息文字的默认渲染方式，必须为以下选项之一：
    # interaction - 需要 1.19+，相比 display 更接近原生名称标签的效果
    # display - 支持不同颜色的背景
    # display_vehicle - 将 display 实体作为乘客附在 NPC 上
    # areaeffectcloud - 最稳妥的选项
    # armorstand - 稳妥程度仅次于上一项，客户端上存在碰撞箱
    # armorstand_vehicle - 将盔甲架作为乘客附在 NPC 上，仅适用于名称标签
    default-renderer: display
    default-renderer-settings:
      seeThrough: false
      shadowed: false
      billboard: CENTER
      interpolationDelay: 0
      interpolationDuration: 0
    # 全息文字各行之间的默认间距
    default-line-height: 0.4
    # 是否始终每 tick 更新全息文字的位置
    always-update-position: false
    # 更新全息名称的间隔（包括占位符）
    update-rate: 1s
  limits:
    # 单个玩家默认最多可拥有的 NPC 数量（授予 citizens ignore-limits 权限可跳过此检查）
    default-limit: 10
    # 创建 NPC 时要检查的权限数量
    # 仅在通过权限设置的数量上限大于此值时才需修改
    max-permission-checks: 100
  text:
    # 与玩家交谈的默认最大间隔
    default-random-text-delay-max: 10s
    # 与玩家交谈的默认最小间隔
    default-random-text-delay-min: 5s
    # 对话气泡的默认显示时长
    speech-bubble-duration: 50t
    # 用于交谈的物品过滤条件
    talk-item: '*'
```

```yaml title="config.yml · npc（3/3）"
npc:
  tablist:
    # 是否从 Tab 玩家列表中移除 NPC
    disable: true
    # 发送 Tab 玩家列表移除数据包前的等待时长
    remove-packet-delay: 2t
  follow:
    # /npc follow 是否通过跨世界传送跟随目标
    teleport-across-worlds: false
  skins:
    # 向刚加入的玩家发送皮肤前的等待时长
    player-join-update-delay: 1s
    # 尝试加载 NPC 皮肤的次数（由于 Minecraft 会限制皮肤请求频率，通常不应少于 5 次
    max-retries: -1
    # 是否尝试为所有新建 NPC 查找对应的玩家皮肤
    # 如果设为 false，创建名为 Dinnerbone 的 NPC 时，该 NPC 会使用默认皮肤（steve/alex 等），而不会尝试获取 Dinnerbone 的皮肤
    try-fetch-default-skin: true
    # 再次尝试皮肤请求前的等待时长（通常是因为 Mojang 限制了请求频率）
    retry-delay: 5s
    rotation-update-degrees: 90.0
    # 是否每隔一段时间从 Minecraft 获取新皮肤
    use-latest-by-default: false
    # 可视距离，单位为方块
    view-distance: 100
    # 皮肤占位符的更新间隔
    placeholder-update-frequency: 5m
  chunks:
    # 是否保持 NPC 所在区块加载
    always-keep-loaded: false
  commands:
    # 命令再次可用前的全局冷却时间，必须以秒为单位
    global-cooldown: 1s
    error-messages:
      global-maximum-times-used: "已达到使用次数上限（{0}）。"
      maximum-times-used: "已达到使用次数上限（{0}）。"
      missing-item: "还缺少 {1} {0}"
      no-permission: "你没有执行此操作的权限。"
      not-enough-experience: "至少需要 {0} 经验。"
      not-enough-money: "至少需要 ${0}。"
      on-cooldown: "请等待 {minutes} 分钟 {seconds_over} 秒。"
      on-global-cooldown: "请等待 {minutes} 分钟 {seconds_over} 秒。"
  movement:
    # 在水中时移动速度的提升百分比
    water-speed-modifier: 1.15
  # 使用数据包 NPC 显示名称全息文字（实验性功能）
  use-packet-holograms: false
  packets:
    update-delay: 30
  player:
    # 是否从 Java 的玩家列表中移除 NPC
    remove-from-list: true
  selection:
    # 选中 NPC 时默认需要手持的物品
    item: stick
    message: "已选中 [[<npc>]]（ID [[<id>]]）。"
  # 是否由服务器拥有 NPC，而非由各个玩家拥有
  server-ownership: false
  shops:
    default-item:
      max-repeats-on-shift-click: ''
      result-message: ''
      already-purchased-message: ''
      lore: ''
      name: ''
      times-purchasable: ''
      cost-message: ''
      click-to-confirm-message: ''
    # 玩家查看任意 NPC 商店所需的全局查看权限
    # 默认为空（不需要权限）。
    global-view-permission: ''
    # 是否默认为所有商店物品添加默认物品描述占位符。
    add-default-item-description: false
```

## `general` { #general }

```yaml title="config.yml · general"
general:
  authlib:
    # 使用此 URL 查找 gameprofiles
    profile-url: https://sessionserver.mojang.com/session/minecraft/profile/
  # 将 Citizens 的调试输出发送到指定文件
  debug-file: ''
  # 启用 Citizens 调试
  debug-mode: false
  # 只有在区块从磁盘加载完成后才会生成实体
  # 默认等待区块加载一秒；如果磁盘较慢，可增大此值
  wait-for-entity-spawn: 1s
  color-scheme:
    message-error: <red>
    message-highlight: <yellow>
    message: <green>
  translation:
    # 控制翻译文件，默认使用系统语言；如果需要英语，请设为 'en'
    locale: ''
  # 颜色改变时是否重置文本格式。
  # 模拟旧版颜色代码的行为。
  reset-formatting-on-color-change: false
  # 保存资源包的路径
  resource-pack-path: plugins/Citizens/resourcepack
  reload-warning-enabled: true
```

## `advanced` { #advanced }

```yaml title="config.yml · advanced"
advanced:
  # 是否检查 Minecraft 版本兼容性（请勿修改）
  check-minecraft-version: true
```

## `storage` { #storage }

```yaml title="config.yml · storage"
storage:
  # 将 NPC 保存到磁盘的间隔
  save-task-frequency: 1hr
  file: saves.yml
```
