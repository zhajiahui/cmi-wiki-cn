---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 5.8.1
---

# config.yml

文件：`config.yml`。版本：`5.8.1`。

主配置。

## `world` { #world }

```yaml title="config.yml · world"
####################################################################################################
#                                                                                                  #
#                    █▀▄▀█ █░█ █░░ ▀█▀ █ █░█ █▀▀ █▀█ █▀ █▀▀   █▀▀ █▀█ █▀█ █▀▀                      #
#                    █░▀░█ █▄█ █▄▄ ░█░ █ ▀▄▀ ██▄ █▀▄ ▄█ ██▄   █▄▄ █▄█ █▀▄ ██▄                      #
#                                                                                                  #
#                                                                                                  #
#    Wiki：       https://mvplugins.org/core/                                                      #
#    DISCORD：    https://discord.gg/NZtfKky                                                       #
#    问题反馈：   https://github.com/Multiverse/Multiverse-Core/issues                             #
#    捐赠：       https://github.com/sponsors/Multiverse                                           #
#                                                                                                  #
#                                                                                                  #
#    新选项会自动添加到本文件。如果在服务器运行期间手动修改了本文件，                               #
#    请执行 `/mv reload` 命令。                                                                   #
#                                                                                                  #
####################################################################################################
  
  
world:
  # 启用后，Multiverse 会在启用或重载时自动导入 server.properties 中
  # `level-name` 指定的默认世界。如果服务器创建了下界和
  # 末地，也会一并导入。
  auto-import-default-worlds: true
  
  # 启用后，Multiverse 会在启动或重载时导入其他插件创建的
  # 所有其他世界。
  auto-import-3rd-party-worlds: true
  
  # 此设置用于阻止玩家进入没有访问权限的世界。
  # 设为 false 时，玩家可以进入任意世界。
  # 设为 true 时，玩家只能进入自己拥有
  # `mv.access.<worldname>` 权限的世界。
  enforce-access: false
  
  # 设置 Multiverse 是否在玩家切换世界时强制切换游戏模式。
  # 启用后，玩家会被强制切换为所进入世界的游戏模式，除非拥有
  # `mv.bypass.gamemode.<worldname>` 权限。
  enforce-gamemode: true
  
  # 设置 Multiverse 是否对各世界统一强制应用飞行能力设置。
  # 如果希望由其他插件管理玩家的飞行能力，请禁用此项。
  # 禁用后，世界属性 `allow-flight` 将不再生效。
  enforce-flight: true
  
  # 设置切换世界后，Multiverse 强制应用游戏模式和飞行能力设置前的延迟，单位为 tick。
  # 如果遇到其他插件覆盖游戏模式或飞行能力的问题，请增大此值。
  # 也可以设为 0，在世界切换事件中立即应用。
  gamemode-and-flight-enforce-delay: 1
  
  # 设置 Multiverse 是否应用 worlds.yml 中各世界的实体 `tick-rate` 配置。
  # 禁用后，将忽略 worlds.yml 中的 `tick-rate` 配置。
  # 如果希望由 paper-world.yml 或其他插件管理各世界的实体生成频率，请禁用此项。
  # !!!注意：此设置仅在服务器重启后生效！
  apply-entity-spawn-rate: true
  
  # 设置 Multiverse 是否在加载世界时应用该世界的实体 `spawn-limit` 配置。
  # 禁用后，将忽略 worlds.yml 中的 `spawn-limit` 配置。
  # 如果希望由 paper-world.yml 或其他插件管理各世界的实体数量上限，请禁用此项。
  # !!!注意：此设置仅在服务器重启后生效！
  apply-entity-spawn-limit: true
  
  # 设置 Multiverse 是否在世界加载时，根据该世界的实体生成配置清除实体。
  auto-purge-entities: false
  
  # 世界名称的格式，供 Multiverse 自动识别由主世界、下界和末地组成的世界组。
  # 用于 default-respawn-in-overworld，也可能用于其他功能。
  world-name-format:
    nether: '%overworld%_nether'
    end: '%overworld%_the_end'
  
  # 设置 Multiverse 是否在添加世界或修改别名时，对重复别名发出警告。
  # 虽然不强制要求，但强烈建议避免多个世界使用相同别名，也应避免
  # 别名与其他世界的名称相同，以免在列出世界和使用命令选择世界时产生混淆。
  warn-alias-conflicts: true
```

## `teleport` { #teleport }

```yaml title="config.yml · teleport"
teleport:
  # 设置 Multiverse 是否使用更细分的传送权限。
  # ----
  # /mvtp 和 /mvspawn 命令使用的新细分传送权限：
  #   - 对于指定的传送类型：`multiverse.teleport.<self|other>.<type>.<target>`
  #   - 对于指定世界的出生点：`multiverse.core.spawn.<self|other>.<worldname>`
  # 例如，设置 `multiverse.teleport.self.w.world2` 后，Multiverse 将只允许该玩家传送到 world2。
  # ----
  # 设为 false 时使用旧版权限：
  #   - 对于传送目的地：`multiverse.teleport.<self|other>.<type>`
  #   - 对于出生点：`multiverse.core.spawn.<self|other>`
  use-finer-teleport-permissions: true
  
  # 配置实体传送时如何处理乘客和载具。此配置
  # 仅适用于 /mvtp、join-destination 和 first-spawn-override，不影响其他插件或命令
  # 触发的任何传送。
  # ========= 可用选项：=========
  #   default: 由服务器处理乘客和载具。在 papermc 1.21.10+ 上，默认全部保留。
  #                                                        在较早的版本上，跨世界时会全部解除骑乘关系。
  #   dismount_passengers: 传送前解除该实体与其乘客的骑乘关系。
  #   dismount_vehicle: 传送前解除该实体与其载具的骑乘关系。
  #   dismount_all: 传送前解除该实体与所有乘客及载具的骑乘关系。
  #   retain_passengers: 乘客会与该实体一同传送。
  #   retain_vehicle: 载具会与该实体一同传送。
  #   retain_all: 所有乘客和载具都会与该实体一同传送。
  passenger-mode: default
  
  # 设置 `/mv teleport` 命令一次最多可传送的玩家数量
  concurrent-teleport-limit: 50
  
  # 设为 true 时，Multiverse 会对所有传送强制检查访问权限，
  # 包括其他插件触发的传送。只有与其他负责传送的插件
  # 发生冲突时，才应禁用此项。
  teleport-intercept: true
  
  # 设置查找安全传送位置时的水平搜索半径（x 轴和 z 轴）。
  # 增大此值会扩大搜索范围，但会增加性能开销。
  # 设为 0 可禁用。
  safe-location-horizontal-search-radius: 3
  
  # 设置查找安全传送位置时的垂直搜索半径（y 轴）。
  # 增大此值会扩大搜索范围，但会增加性能开销。
  # 设为 0 可禁用。
  safe-location-vertical-search-radius: 3
```

## `spawn` { #spawn }

```yaml title="config.yml · spawn"
spawn:
  # 设置 Multiverse 是否覆盖玩家首次加入服务器时的生成位置。
  # 如果需要每次登录都在固定位置生成，请参见下方的 `join-destination` 选项。
  # 禁用后，默认使用 server.properties 中的设置。
  first-spawn-override: false
  
  # 设置 Multiverse 为首次加入服务器的玩家使用的生成世界。
  # 仅当 first-spawn-override 设为 true 时生效。
  first-spawn-location: ''
  
  # 启用后，可为玩家设置每次加入服务器时的固定生成位置。
  # 另请参见下方的 `join-destination` 选项。
  enable-join-destination: false
  
  # 设置 Multiverse 为玩家每次登录使用的生成目的地。
  # 将上方的 enable-join-destination 设为 false 可禁用
  join-destination: ''
  
  # 仅当玩家死亡时所在世界未设置 `respawn-world` 属性，
  # 且玩家未设置床或重生锚时生效。
  # ----
  # 启用后，玩家在下界或末地死亡时会在主世界重生，与原版行为一致。
  # 自动选择哪个主世界，由上方的 `world-name-format` 配置部分决定。
  # 此选项优先于 `default-respawn-within-same-world` 选项。
  # ----
  # 如果希望由其他插件处理重生，或不想使用此原版行为，请设为 false。
  default-respawn-in-overworld: true
  
  # 仅当玩家死亡时所在世界未设置 `respawn-world` 属性，
  # 且玩家未设置床或重生锚时生效。
  # ----
  # 启用后，玩家会在死亡时所在的同一个世界重生。
  # 如果 /spawnpoint 设置的位置已在该世界内，且禁用了 `enforce-respawn-at-world-spawn`，
  # Multiverse 会使用该生成位置；否则使用玩家死亡时所在世界的世界出生点。
  # ----
  # 可使用命令 `/mv modify <worldname> set respawn-world <worldname>` 设置 `respawn-world` 属性
  # 可使用命令 `/mv modify <worldname> reset respawn-world` 重置 `respawn-world` 属性
  # ----
  # 如果希望由其他插件处理重生，请设为 false。
  default-respawn-within-same-world: true
  
  # 启用后，玩家始终会在计算得出的重生世界的世界出生点重生，
  # 除非玩家已设置床或重生锚，且分别启用了对应的 `bed-respawn` 或 `anchor-spawn`。
  # ----
  # 如果希望使用 /spawnpoint 等自定义生成位置，而不是世界出生点，请设为 false。
  enforce-respawn-at-world-spawn: true
```

## `portal` { #portal }

```yaml title="config.yml · portal"
portal:
  # 设置 Multiverse 是否接管 Bukkit 默认的传送门搜索半径。
  # 设为 false 时，由 Bukkit 自行决定搜索半径。
  use-custom-portal-search: false
  
  # 设置 Multiverse 查找传送门时使用的搜索半径。
  # 仅当 use-custom-portal-search 设为 true 时生效。
  custom-portal-search-radius: 128
```

## `messaging` { #messaging }

```yaml title="config.yml · messaging"
messaging:
  # 设置 Multiverse 是否在聊天消息前添加世界名称前缀。
  # 如果希望由其他插件处理聊天格式，请将此项设为 false。
  enable-chat-prefix: false
  
  # 设置 Multiverse 在聊天消息前添加世界名称前缀时使用的格式。
  # 仅当 enable-chat-prefix 设为 true 时生效。
  chat-prefix-format: '[%world%]%chat%'
  
  # 设置 Multiverse 是否注册 PlaceholderAPI 对接。
  # 仅在已安装 PlaceholderAPI 时生效。
  register-papi-hook: true
  
  # 设置 Multiverse 是否针对无效的 PlaceholderAPI 格式发出警告。
  # 仅在已安装 PlaceholderAPI 时生效，且只适用于 multiverse 占位符。
  warn-invalid-papi-format: true
  
  # 默认情况下，格式无效时会返回原始占位符字符串。
  # 设置 Multiverse 是否将格式无效的 PlaceholderAPI 占位符显示为空白。
  # 仅在已安装 PlaceholderAPI 时生效，且只适用于 multiverse 占位符。
  invalid-papi-format-returns-blank: false
  
  # 设置 Multiverse 使用的默认语言。
  default-locale: en
  
  # 设置 Multiverse 是否使用玩家客户端所选的语言。
  # 如果玩家的语言没有对应译文，则改用上方设置的默认语言。
  per-player-locale: true
```

## `command` { #command }

```yaml title="config.yml · command"
command:
  # 设为 true 时，Multiverse 会在命令和目的地中按世界别名识别世界。
  # 仍然接受普通世界名称。
  # 如果多个世界的别名相同，将使用找到的第一个世界。
  resolve-alias-name: true
  
  # 设为 true 时，Multiverse 只会在 Tab 补全中提示简单目的地格式。
  # 这表示只提示世界名称，不提示 `e:worldname:x,y,z` 或 `p:playername` 等其他目的地类型。
  # 注意：这不会阻止玩家使用这些目的地；是否可用由权限控制。
  simplified-destination-tab-completion: false
  
  # 设置执行危险操作前是否需要使用 `/mv confirm` 确认。
  #   enable: 需要执行 `/mv confirm`。
  #   player_only: 仅在玩家执行命令时需要执行 `/mv confirm`。
  #   disable_command_blocks: 命令方块无需执行 `/mv confirm`。
  #   disable_console: 控制台无需执行 `/mv confirm`。
  #   disable: 无需执行 `/mv confirm`。
  confirm-mode: enable
  
  # 设为 true 时，`/mv confirm` 会附带一个 3 位随机数字，必须输入该数字才能确认命令。
  # 例如：`/mv confirm 726`
  use-confirm-otp: true
  
  # `/mv confirm` 的超时时间，单位为秒
  confirm-timeout: 30
  
  # 设为 true 时，Tab 补全会显示旧版命令别名。
  # 这些是 `/mvclone` 等 mv4 旧版别名；它们会与 `/mv clone` 一起显示，使 Tab 补全列表显得拥挤。
  # !!!注意：此设置仅在服务器重启后生效！
  show-legacy-aliases: false
```

## `event-priority` { #event-priority }

```yaml title="config.yml · event-priority"
event-priority:
  # 以下配置用于修改 Bukkit 的某些事件的 EventPriority。
  # 只有需要让 Multiverse 的事件处理结果覆盖其他插件，或希望
  # 其他插件的处理结果覆盖 Multiverse 时，才应修改。
  # ----
  # !!!注意：此设置仅在服务器重启后生效！
  
  # 设置 PlayerPortalEvent 的优先级。
  player-portal: high
  
  # 设置 PlayerRespawnEvent 的优先级。
  player-respawn: low
  
  # 设置 PlayerSpawnLocationEvent 的优先级。
  player-spawn-location: normal
  
  # 设置 PlayerTeleportEvent 的优先级。
  player-teleport: highest
  
  # 设置 PlayerChangedWorldEvent 的优先级。
  player-changed-world: normal
```

## `misc` { #misc }

```yaml title="config.yml · misc"
misc:
  # 如果通过启动参数 `--bukkit-settings` 为 bukkit.yml 文件指定了自定义路径，请修改此项。
  # 注意：此配置项需要重启服务器才能生效。
  bukkit-yml-path: bukkit.yml
  
  # 如果通过启动参数 `--config` 为 server.properties 文件指定了自定义路径，请修改此项。
  # 注意：此配置项需要重启服务器才能生效。
  server-properties-path: server.properties
  
  # 启用后，Multiverse 会尝试自动检测服务器上已安装的世界生成器插件。
  # 此选项只影响 `/mv create` 命令的 Tab 补全和 `/mv generators` 命令的输出。
  # 禁用此项不会影响世界生成器插件本身的使用。
  auto-detect-generator-plugins: true
  
  # 此调试选项用于帮助排查 Multiverse 问题。
  # 如果遇到 Multiverse 问题，请将此项设为 3，然后将日志发布到 pastebin.com
  # 除此之外，无需修改，除非 Wiki 页面或开发者要求这样做。
  #   0 = 关闭，不输出调试消息
  #   1 = fine
  #   2 = finer
  #   3 = finest
  global-debug: 0
  
  # 设置控制台是否记录所有 Multiverse 插件进行的每次权限检查。
  # 仅当上方的 'global-debug' 设为 1 或更高时生效。
  debug-permissions: false
  
  # 设为 true 时，将不再显示启动时的控制台消息。
  silent-start: false
  
  # 如果不想捐赠，可将此项设为 false，Multiverse 就会停止提醒。
  # 如果想捐赠，这是我们的 GitHub Sponsors 页面：https://github.com/sponsors/Multiverse
  show-donation-message: true
```

## `version` { #version }

```yaml title="config.yml · version"
# 此项仅用于标识配置版本号，以便我们了解你使用的配置版本。
# 请勿修改此值
version: 5.2
```
