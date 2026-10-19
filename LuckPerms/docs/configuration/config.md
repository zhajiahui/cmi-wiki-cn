---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 5.5.71
---

# config.yml

文件：`config.yml`。版本：`5.5.71`。

主配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `server` { #server }

```yaml title="config.yml · server"
####################################################################################################
# +----------------------------------------------------------------------------------------------+ #
# |                                   __         __   ___  __         __                         | #
# |                        |    |  | /  ` |__/  |__) |__  |__)  |\/| /__`                        | #
# |                        |___ \__/ \__, |  \  |    |___ |  \  |  | .__/                        | #
# |                                                                                              | #
# |                                     https://luckperms.net                                    | #
# |                                                                                              | #
# |  WIKI：       https://luckperms.net/wiki                                                     | #
# |  DISCORD：    https://discord.gg/luckperms                                                   | #
# |  问题反馈：   https://github.com/LuckPerms/LuckPerms/issues                                  | #
# |                                                                                              | #
# |  此文件中各配置项的详细说明见：                                                              | #
# |   ==>  https://luckperms.net/wiki/Configuration                                              | #
# |                                                                                              | #
# |  新配置项不会自动添加到此文件中。如果找不到某个                                               | #
# |  配置项，则使用默认值。可通过上方链接获取最新版本的配置文件。                                 | #
# +----------------------------------------------------------------------------------------------+ #
####################################################################################################

# +----------------------------------------------------------------------------------------------+ #
# |                                                                                              | #
# |                                         基本设置                                            | #
# |                                                                                              | #
# |                            控制 LuckPerms 运行方式的重要设置。                              | #
# |                                                                                              | #
# +----------------------------------------------------------------------------------------------+ #

# 服务器名称，用于设置仅在特定服务器生效的权限。
#
# - 设为 "global" 时，此设置实际上会被忽略。
# - 设为其他值时，会为所有玩家添加一个 "server" 上下文，其值为此处设置的名称。
# - 参见：https://luckperms.net/wiki/Context
server: global
```

## `use-server-uuid-cache` { #use-server-uuid-cache }

```yaml title="config.yml · use-server-uuid-cache"
# 当 LuckPerms 中还没有某位玩家的
# 记录时，是否使用服务器自身的 UUID 缓存或查询机制。
#
# - 将此项设为 'false' 后，只有自首次安装 LuckPerms 以来加入过服务器的玩家，
#   才能在命令中使用其用户名。
# - 要解决此问题，可在命令中直接使用玩家的 uuid，或启用此项。
# - 将此项设为 'true' 后，会使用服务器自身的查询机制。该机制可能采用多种方式，
#   包括检查服务器的本地缓存，或向 Mojang API 发送请求。
use-server-uuid-cache: false
```

## `storage-method` { #storage-method }

```yaml title="config.yml · storage-method"
# +----------------------------------------------------------------------------------------------+ #
# |                                                                                              | #
# |                                         存储设置                                            | #
# |                                                                                              | #
# |                           控制 LuckPerms 使用何种存储方式保存数据。                         | #
# |                                                                                              | #
# +----------------------------------------------------------------------------------------------+ #

# 插件存储数据的方式。
#
# - Wiki 中详细说明了各种可选方式：
#   https://luckperms.net/wiki/Storage-types
#
# - 可选值：
#
#   |  远程数据库——需要在下方配置连接信息
#   |=> MySQL
#   |=> MariaDB(优先于 MySQL)
#   |=> PostgreSQL
#   |=> MongoDB
#
#   |  文件数据库/本地数据库——无需额外配置
#   |=> H2(优先于 SQLite)
#   |=> SQLite
#
#   |  可直接阅读和编辑的文本文件——无需额外配置
#   |=> YAML(.yml 文件)
#   |=> JSON(.json 文件)
#   |=> HOCON(.conf 文件)
#   |=> TOML(.toml 文件)
#   |
#   | 默认情况下，用户、权限组和晋升路线数据分别保存在不同文件中。切换为合并存储方式后，
#   | 可以将这些数据合并保存到同一个文件。
#   | 只需在 storage-method 的值末尾添加 '-combined'，例如 'yaml-combined'。
#
# - 默认使用 H2 数据库。
# - 如果要手动编辑“传统”存储文件中的数据，建议使用 YAML。
storage-method: h2
```

## `data` { #data }

```yaml title="config.yml · data"
# 以下部分定义远程数据库存储方式的设置。
#
# - 使用本地存储方式时，无需修改这里的任何设置！
# - 所有远程存储类型共用这些连接信息设置。
data:

  # 设置数据库的地址和端口。
  # - 默认使用对应数据库引擎的标准端口
  #   (MySQL: 3306, PostgreSQL: 5432, MongoDB: 27017)
  # - 如果使用其他端口，请按 "host:port" 格式填写。
  address: "HOST"

  # 用于存储 LuckPerms 数据的数据库名称。
  # - 此数据库必须事先创建。使用 MongoDB 时无需关注此设置。
  database: "DATABASE"

  # 数据库的认证信息。
  username: "USERNAME"
  password: ''

  # 这些设置适用于 MySQL 连接池。
  # - 默认值适合大多数用户。
  # - 除非清楚这些设置的作用，否则请勿修改！
  pool-settings:

    # 设置 MySQL 连接池的最大连接数。
    # - 此值基本上决定了与数据库后端之间
    #   实际连接数的上限。
    # - 关于如何确定连接池大小，可参阅：
    #   https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing
    maximum-pool-size: 10

    # 设置连接池尝试维持的最小空闲连接数。
    # - 为获得最佳性能并及时应对突增的需求，建议不单独调整
    #   此值，让连接池保持固定大小。
    #   (将此值设为与 'maximum-pool-size' 相同)
    minimum-idle: 10

    # 此设置控制池中连接的最长存活时间，单位：毫秒。
    # - 此值应至少短 30 秒，比较对象为数据库或基础设施规定的任何
    #   连接时间限制。
    maximum-lifetime: 1800000 # 30 分钟

    # 此设置控制连接池向连接发送 'ping' 的频率，以免连接
    # 因数据库或网络基础设施的超时机制而断开，单位：毫秒。
    # - 此值必须小于 maximum-lifetime，并大于 30000(30 秒)。
    # - 将此值设为零可禁用保活功能。
    keepalive-time: 0

    # 此设置控制插件从连接池获取连接时的最长等待时间，
    # 单位：毫秒；超过此时间即视为超时。
    connection-timeout: 5000 # 5 秒

    # 此设置可为连接定义额外属性。
    #
    # 默认设置了以下选项，以启用 utf8 编码。(如果使用 PostgreSQL，
    # 可能需要移除这些选项)
    #   useUnicode: true
    #   characterEncoding: utf8
    #
    # 也可取消下方 'useSSL' 和 'verifyServerCertificate'
    # 选项的注释，以禁用 SSL 连接。
    properties:
      useUnicode: true
      characterEncoding: utf8
      #useSSL: false
      #verifyServerCertificate: false

  # 所有 LuckPerms SQL 数据表使用的前缀。
  #
  # - 此设置仅适用于远程 SQL 存储类型(MySQL、MariaDB 等)。
  # - 如果要为不同服务器使用不同的数据表，可修改此项。
  table-prefix: "TABLE_PREFIX"

  # 所有 LuckPerms MongoDB 集合使用的前缀。
  #
  # - 此设置仅适用于 MongoDB 存储类型。
  # - 如果要为不同服务器使用不同的集合，可修改此项。默认
  # 不使用前缀。
  mongodb-collection-prefix: ''

  # 连接 MongoDB 实例时使用的连接字符串 URI。
  #
  # - 配置此项后，将覆盖上方 address、database、
  #   username 或 password 字段中定义的所有内容。
  # - 如果连接字符串以 'mongodb://' 或 'mongodb+srv://' 开头，请填写在
  #   下方。
  # - 更多信息见 https://docs.mongodb.com/manual/reference/connection-string/
  mongodb-connection-uri: ''
```

## `split-storage` { #split-storage }

```yaml title="config.yml · split-storage"
# 定义“分拆存储”的设置。
#
# - 此设置可为每种数据类型分别指定存储方式。
# - 上方的连接选项仍须正确配置，以适用于此处的每种存储类型。
split-storage:
  # 如果不打算使用分拆存储，请勿修改此项！
  enabled: false
  methods:
    # 未启用分拆存储时，无需修改这些选项。
    user: h2
    group: h2
    track: h2
    uuid: h2
    log: h2
```

## `sync-minutes` { #sync-minutes }

```yaml title="config.yml · sync-minutes"
# +----------------------------------------------------------------------------------------------+ #
# |                                                                                              | #
# |                                   更新传播与消息服务                                        | #
# |                                                                                              | #
# |                   控制 LuckPerms 同步数据并通知其他服务器数据变更的方式。                    | #
# |                 Wiki 中的 "Instant Updates" 页面详细说明了这些选项。                      | #
# |                                                                                              | #
# +----------------------------------------------------------------------------------------------+ #

# 此选项控制 LuckPerms 执行同步任务的频率。
#
# - 同步任务会从存储中刷新全部数据，确保插件使用的
#   是最新数据。
# - 大多数用户无需此功能，因此默认禁用。但如果使用远程
#   存储且未配置消息服务，可考虑将此值设为 3 等数值。
# - 设为 -1 可完全禁用此任务。
sync-minutes: -1
```

## `watch-files` { #watch-files }

```yaml title="config.yml · watch-files"
# 是否启用文件监视器。
#
# - 使用基于文件的存储类型时，LuckPerms 可以监视数据文件的变化，
#   并在检测到变化时自动更新。
# - 如果不需要此功能，请将此选项设为 false。
watch-files: true
```

## `messaging-service` { #messaging-service }

```yaml title="config.yml · messaging-service"
# 设置插件使用的消息服务。
#
# - 启用并配置后，LuckPerms 会通过消息服务将变更通知给其他已连接的
#   服务器。
# - 使用命令 "/lp networksync" 可手动推送变更。
# - 此服务不会存储数据，仅用于传递消息。
#
# - 如果启用此功能，应将 "sync-minutes" 设为 -1，因为 LuckPerms 无需再
#   轮询数据库以检查变更。
#
# - 可选值：
#   => sql       使用 SQL 数据库建立通信队列。仅在
#                'storage-method' 设为 MySQL 或 MariaDB 时生效。如果此选项
#                设为 'auto' 且使用 SQL 存储，默认会选用此方式。设为 'notsql' 可禁用。
#   => pluginmsg 使用插件消息通道与代理端通信。
#                代理端及其连接的所有后端服务器都必须安装 LuckPerms。
#                使用多个代理端时，此方式不生效。
#   => lilypad   使用 LilyPad 发布/订阅机制推送变更。需要安装 LilyPad-Connect
#                插件。
#   => redis     使用 Redis 发布/订阅机制推送变更。必须在下方配置服务器的
#                连接信息。
#   => rabbitmq  使用 RabbitMQ 发布/订阅机制推送变更。必须在下方配置服务器的
#                连接信息。
#   => nats      使用 Nats 发布/订阅机制推送变更。必须在下方配置服务器的
#                连接信息。
#   => custom    使用通过 LuckPerms API 提供的消息服务。
#   => auto      尝试自动使用 redis 或 sql 配置消息服务。
messaging-service: auto
```

## `auto-push-updates` { #auto-push-updates }

```yaml title="config.yml · auto-push-updates"
# 通过命令修改数据后，LuckPerms 是否自动推送更新。
auto-push-updates: true
```

## `push-log-entries` { #push-log-entries }

```yaml title="config.yml · push-log-entries"
# LuckPerms 是否通过消息服务向已连接的服务器推送操作日志条目。
push-log-entries: true
```

## `broadcast-received-log-entries` { #broadcast-received-log-entries }

```yaml title="config.yml · broadcast-received-log-entries"
# LuckPerms 是否将收到的操作日志条目广播给当前平台上的玩家。
#
# - 如果后端服务器和 BungeeCord 代理端都安装了 LuckPerms，
#   应在后端服务器或代理端中的一方将此选项设为 false，避免玩家
#   重复收到同一条日志通知。
broadcast-received-log-entries: true
```

## `redis` { #redis }

```yaml title="config.yml · redis"
# Redis 的设置。
# 默认使用端口 6379；如使用其他端口，请将地址设为 "host:port"。
# 可在名为 "addresses" 的字符串列表中，按相同格式指定多个 Redis 节点。
redis:
  enabled: false
  address: "HOST"
  username: ''
  password: ''
  # Redis Sentinel 的设置。
  # Sentinel 通过监视主节点/副本实例，为 Redis 提供高可用性。
  # Sentinel 节点默认使用端口 26379。
  sentinel:
    enabled: false
    master: "MASTER"
    addresses:
      - "HOST"
    username: ''
    password: ''
```

## `nats` { #nats }

```yaml title="config.yml · nats"
# Nats 的设置。
# 默认使用端口 4222；如使用其他端口，请将地址设为 "host:port"。
nats:
  enabled: false
  address: "HOST"
  username: ''
  password: ''
  token: ''
```

## `rabbitmq` { #rabbitmq }

```yaml title="config.yml · rabbitmq"
# RabbitMQ 的设置。
# 默认使用端口 5672；如使用其他端口，请将地址设为 "host:port"。
rabbitmq:
  enabled: false
  address: "HOST"
  vhost: "VHOST"
  username: "USERNAME"
  password: "PASSWORD"
```

## `temporary-add-behaviour` { #temporary-add-behaviour }

```yaml title="config.yml · temporary-add-behaviour"
# +----------------------------------------------------------------------------------------------+ #
# |                                                                                              | #
# |                                        自定义设置                                           | #
# |                                                                                              | #
# |                         供管理员自定义 LuckPerms 运行方式的设置。                           | #
# |                                                                                              | #
# +----------------------------------------------------------------------------------------------+ #

# 控制临时权限/父级/元数据的累积方式。
#
# - 默认行为为 "deny"。
# - 执行命令时也可指定此行为。更多信息见命令用法
#   文档。
#
# - 可选值：
#   => accumulate   将持续时间累加到现有到期时间上
#   => replace      新的到期时间晚于当前到期时间时，替换原有
#                   持续时间
#   => deny         如果尝试添加另一个到期时间相同的节点，命令会直接失败
temporary-add-behaviour: deny
```

## `primary-group-calculation` { #primary-group-calculation }

```yaml title="config.yml · primary-group-calculation"
# 控制 LuckPerms 如何确定用户的“主”权限组。
#
# - Wiki 详细说明了“主权限组”的含义及影响。
# - 推荐让 LuckPerms 根据用户的父权限组的相对权重，
#   自动确定用户的主权限组。
#
# - 可选值：
#   => stored                  使用文件/数据库中的用户记录所保存的值
#   => parents-by-weight       仅使用用户权重最高的父权限组
#   => all-parents-by-weight   与上项相同，但会基于所有直接和间接继承的
#                              父权限组计算
primary-group-calculation: parents-by-weight
```

## `argument-based-command-permissions` { #argument-based-command-permissions }

```yaml title="config.yml · argument-based-command-permissions"
# 用户执行 LP 命令时，插件是否检查“额外”权限。
#
# - 这些额外权限可更细致地控制用户可使用各命令执行哪些操作，以及
#   可以编辑哪些对象。
# - Wiki 中的 "Argument based command permissions" 页面说明了这些检查。
# - 基于参数的权限与“基础”权限不同，并非固定不变，而是取决于
#   命令中提供的参数。
argument-based-command-permissions: false
```

## `require-sender-group-membership-to-modify` { #require-sender-group-membership-to-modify }

```yaml title="config.yml · require-sender-group-membership-to-modify"
# 插件是否检查命令发送者属于指定权限组后，才允许其
# 编辑该权限组的数据，或向该组添加其他用户/从该组移除其他用户。
# 注意：这些限制不适用于网页编辑器！
require-sender-group-membership-to-modify: false
```

## `log-notify` { #log-notify }

```yaml title="config.yml · log-notify"
# 每次修改权限时，插件是否向用户发送操作日志通知。
#
# - 通知仅发送给拥有对应接收权限的用户。
# - 也可使用以下命令，为单个用户临时启用/禁用通知：
#   '/lp log notify <on|off>'
log-notify: true
```

## `log-notify-filtered-descriptions` { #log-notify-filtered-descriptions }

```yaml title="config.yml · log-notify-filtered-descriptions"
# 列出不应作为通知发送给用户的日志条目。
#
# - 列表中的每一项都是正则表达式，会与日志条目的说明进行匹配。
log-notify-filtered-descriptions:
```

## `auto-install-translations` { #auto-install-translations }

```yaml title="config.yml · auto-install-translations"
#   - "parent add example"

# LuckPerms 是否自动安装翻译包，并定期更新。
auto-install-translations: true
```

## `meta-formatting` { #meta-formatting }

```yaml title="config.yml · meta-formatting"
# 设置前缀和后缀的叠加方式。
#
# - 此功能可在聊天中玩家的用户名旁显示多个前缀或
#   后缀。
# - Wiki 中的 "Prefix & Suffix Stacking" 页面有更详细的说明。
#
# - 前缀和后缀的选项分别位于不同部分。
# - 'duplicates' 设置决定如何处理重复元素。可设为 'retain-all'、
#   'first-only' 或 'last-only'。
# - 'start-spacer' 的值会加在最终前缀/后缀的开头。
# - 'end-spacer' 的值会加在最终前缀/后缀的末尾。
# - 'middle-spacer' 的值会加在最终前缀/后缀的各元素之间。
#
# - 可用的格式选项：
#   => highest                        从玩家自身拥有或继承的全部值中，选择
#                                     权重最高的值。
#
#   => lowest                         与上项相同，但选择权重最低的值。
#
#   => highest_own                    选择权重最高的值，但不接受
#                                     任何继承的值。
#
#   => lowest_own                     与上项相同，但选择权重最低的值。
#
#   => highest_inherited              选择权重最高的值，但只接受
#                                     继承的值。
#
#   => lowest_inherited               与上项相同，但选择权重最低的值。
#
#   => highest_on_track_<track>       选择权重最高的值，但仅当该值
#                                     继承自指定晋升路线中的权限组时才接受。
#
#   => lowest_on_track_<track>        与上项相同，但选择权重最低的值。
#
#   => highest_not_on_track_<track>   选择权重最高的值，但仅当该值
#                                     继承自指定晋升路线之外的权限组时才接受。
#
#   => lowest_not_on_track_<track>    与上项相同，但选择权重最低的值。
#
#   => highest_from_group_<group>     选择权重最高的值，但仅当该值
#                                     继承自指定权限组时才接受。
#
#   => lowest_from_group_<group>      与上项相同，但选择权重最低的值。
#
#   => highest_not_from_group_<group> 选择权重最高的值，但仅当该值
#                                     并非继承自指定权限组时才接受。
#
#   => lowest_not_from_group_<group>  与上项相同，但选择权重最低的值。
meta-formatting:
  prefix:
    format:
      - "highest"
    duplicates: first-only
    start-spacer: ""
    middle-spacer: " "
    end-spacer: ""
  suffix:
    format:
      - "highest"
    duplicates: first-only
    start-spacer: ""
    middle-spacer: " "
    end-spacer: ""
```

## `inheritance-traversal-algorithm` { #inheritance-traversal-algorithm }

```yaml title="config.yml · inheritance-traversal-algorithm"
# +----------------------------------------------------------------------------------------------+ #
# |                                                                                              | #
# |                                    权限计算与继承                                           | #
# |                                                                                              | #
# |                       修改权限检查、元数据查询和继承关系解析的处理方式。                     | #
# |                                                                                              | #
# +----------------------------------------------------------------------------------------------+ #

# LuckPerms 遍历“继承树”时使用的算法。
#
# - 可选值：
#   => breadth-first            参见：https://en.wikipedia.org/wiki/Breadth-first_search
#   => depth-first-pre-order    参见：https://en.wikipedia.org/wiki/Depth-first_search
#   => depth-first-post-order   参见：https://en.wikipedia.org/wiki/Depth-first_search
inheritance-traversal-algorithm: depth-first-pre-order
```

## `post-traversal-inheritance-sort` { #post-traversal-inheritance-sort }

```yaml title="config.yml · post-traversal-inheritance-sort"
# 遍历算法解析继承树后，是否按“继承规则”
# 执行最终排序。
#
# “继承规则”指权限组权重、主权限组状态，以及
# 权限组节点按上下文确定的自然顺序等。
#
# 设为 'true' 后，继承规则的优先级将高于
# 继承树的结构。
#
# 具体来说，设为 'true' 时，会先将继承树扁平化，再应用规则；
# 设为 'false' 时，则在遍历的每一步应用规则。
post-traversal-inheritance-sort: false
```

## `context-satisfy-mode` { #context-satisfy-mode }

```yaml title="config.yml · context-satisfy-mode"
# 设置用于判断一组上下文是否满足条件的模式。
#
# - 可选值：
#   => at-least-one-value-per-key   集合 A 中的每个键，只要至少有一个对应的
#                                   键值项也存在于集合 B 中，就视为 B 满足 A。
#   => all-values-per-key           只有集合 A 中的所有键值项
#                                   都存在于集合 B 中，才视为 B 满足 A。
context-satisfy-mode: at-least-one-value-per-key
```

## `disabled-contexts` { #disabled-contexts }

```yaml title="config.yml · disabled-contexts"
# LuckPerms 内置了若干上下文。将上下文的键添加到
# 下方列表中，可禁用对应上下文。
disabled-contexts:
```

## `include-global` { #include-global }

```yaml title="config.yml · include-global"
#   - "world"

# +----------------------------------------------------------------------------------------------+ #
# | 权限解析设置                                                                                 | #
# +----------------------------------------------------------------------------------------------+ #

# 是否应用此服务器上用户的全局权限。
# 设为 false 时，此服务器上的用户只会应用服务器专属权限。
include-global: true
```

## `include-global-world` { #include-global-world }

```yaml title="config.yml · include-global-world"
# 是否应用此服务器上用户的全局世界权限。
# 设为 false 时，此服务器上的用户只会应用特定世界的权限。
include-global-world: true
```

## `apply-global-groups` { #apply-global-groups }

```yaml title="config.yml · apply-global-groups"
# 是否应用此服务器上用户的全局(不限定服务器)权限组。
apply-global-groups: true
```

## `apply-global-world-groups` { #apply-global-world-groups }

```yaml title="config.yml · apply-global-world-groups"
# 是否应用此服务器上用户的全局(不限定世界)权限组。
apply-global-world-groups: true
```

## `meta-value-selection-default` { #meta-value-selection-default }

```yaml title="config.yml · meta-value-selection-default"
# +----------------------------------------------------------------------------------------------+ #
# | 元数据查询设置                                                                               | #
# +----------------------------------------------------------------------------------------------+ #

# 设置元数据值的选择方式。
#
# - 可选值：
#   => inheritance      选择最先继承的元数据值
#   => highest-number   选择数值最大的元数据值
#   => lowest-number    选择数值最小的元数据值
meta-value-selection-default: inheritance
```

## `meta-value-selection` { #meta-value-selection }

```yaml title="config.yml · meta-value-selection"
# 为各个键分别设置元数据值的选择方式。
meta-value-selection:
```

## `apply-wildcards` { #apply-wildcards }

```yaml title="config.yml · apply-wildcards"
#   max-homes: highest-number

# +----------------------------------------------------------------------------------------------+ #
# | 继承设置                                                                                     | #
# +----------------------------------------------------------------------------------------------+ #

# 插件是否应用通配符权限。
#
# - 设为 true 时，LuckPerms 会识别通配符权限，并解析和应用所有匹配该通配符的
#   已注册权限。
apply-wildcards: true
```

## `apply-sponge-implicit-wildcards` { #apply-sponge-implicit-wildcards }

```yaml title="config.yml · apply-sponge-implicit-wildcards"
# LuckPerms 是否根据 Sponge 风格的隐式通配符继承机制，解析和应用
# 权限。
#
# - 即：如果用户获得了 "example"，玩家也会
#   自动获得 "example.function"、"example.another"、"example.deeper.nesting"
#   等权限。
apply-sponge-implicit-wildcards: false
```

## `apply-default-negated-permissions-before-wildcards` { #apply-default-negated-permissions-before-wildcards }

```yaml title="config.yml · apply-default-negated-permissions-before-wildcards"
# 插件是否先应用设为否定的 Bukkit 默认权限，再考虑通配符
# 授权。
#
# - 插件作者可明确声明某些权限不应自动授予 OP。
#   这通常用于所谓的“反向权限”，即授予后会产生
#   负面效果的权限。
# - 设为 true 时，LuckPerms 会先考虑插件声明的任何否定权限，
#   再考虑通配符。(与 OP 系统的处理方式类似)
# - 设为 false 时，LuckPerms 会先考虑所有通配符授权。
apply-default-negated-permissions-before-wildcards: false
```

## `apply-regex` { #apply-regex }

```yaml title="config.yml · apply-regex"
# 插件是否解析正则表达式权限。
#
# - 设为 true 时，LuckPerms 会识别节点开头标有 "r=" 的正则表达式权限，
#   并解析和应用所有匹配该正则表达式的已注册权限。
apply-regex: true
```

## `apply-shorthand` { #apply-shorthand }

```yaml title="config.yml · apply-shorthand"
# 插件是否展开并应用简写权限。
#
# - 设为 true 时，LuckPerms 会识别并展开简写节点模式。
apply-shorthand: true
```

## `apply-bukkit-child-permissions` { #apply-bukkit-child-permissions }

```yaml title="config.yml · apply-bukkit-child-permissions"
# 插件是否应用 Bukkit 子权限。
#
# - 插件作者可为其插件定义自定义权限结构；启用此项后，LuckPerms 会解析
#   并使用这些结构。
apply-bukkit-child-permissions: true
```

## `apply-bukkit-default-permissions` { #apply-bukkit-default-permissions }

```yaml title="config.yml · apply-bukkit-default-permissions"
# 插件是否应用 Bukkit 默认权限。
#
# - 插件作者可定义默认授予所有用户的权限，或设置哪些权限应当/不应当
#   授予拥有 OP 身份的玩家。
# - 设为 false 时，LuckPerms 会忽略这些默认设置。
apply-bukkit-default-permissions: true
```

## `apply-bukkit-attachment-permissions` { #apply-bukkit-attachment-permissions }

```yaml title="config.yml · apply-bukkit-attachment-permissions"
# 插件是否应用附加权限。
#
# - 服务器上的其他插件可以为玩家添加自己的“权限附件”。
# - 这样可为玩家授予额外权限，这些权限会持续到当前会话结束，
#   或被主动移除为止。
# - 设为 false 时，LuckPerms 在判断玩家是否有权使用某个权限时，
#   不会计入这些附加权限。
apply-bukkit-attachment-permissions: true
```

## `disabled-context-calculators` { #disabled-context-calculators }

```yaml title="config.yml · disabled-context-calculators"
# +----------------------------------------------------------------------------------------------+ #
# | 其他设置                                                                                     | #
# +----------------------------------------------------------------------------------------------+ #

# 计算上下文时应跳过的上下文计算器列表。
#
# - 可通过以下任一方式禁用上下文计算器：
#   => 指定计算器使用的 Java 类名(例如 com.example.ExampleCalculator)
#   => 指定计算器使用的 Java 包名的一部分(例如 com.example)
disabled-context-calculators: []
```

## `world-rewrite` { #world-rewrite }

```yaml title="config.yml · world-rewrite"
# 可为传入上下文计算过程的世界设置“别名”。
#
# - 除真实世界名外，还会提供这些别名，并递归应用。
# - 移除注释符号即可应用默认别名。
world-rewrite:
```

## `group-weight` { #group-weight }

```yaml title="config.yml · group-weight"
#   world_nether: world
#   world_the_end: world

# 为此服务器设置专用的权限组权重。
#
# - 也可使用 setweight 命令，直接在权限组数据中设置权重。
# - 此部分可按服务器分别设置权重。
group-weight:
```

## `enable-ops` { #enable-ops }

```yaml title="config.yml · enable-ops"
#   admin: 10




# +----------------------------------------------------------------------------------------------+ #
# |                                                                                              | #
# |                                         微调选项                                            | #
# |                                                                                              | #
# |              一些用途较专门的设置，用于调整运行行为。此部分还包含某些                         | #
# |              专用功能的开关。只有需要进一步微调 LuckPerms 的运行方式时，                       | #
# |                                    才需要修改这些选项。                                      | #
# |                                                                                              | #
# +----------------------------------------------------------------------------------------------+ #

# +----------------------------------------------------------------------------------------------+ #
# | 服务器管理员(OP)设置                                                                       | #
# +----------------------------------------------------------------------------------------------+ #

# 控制服务器是否允许存在 OP。
#
# - 设为 'false' 时，会移除所有玩家的 OP 身份，并禁用 /op 和 /deop
#   命令。请注意，spawn-protection 等原版功能需要服务器上存在 OP
#   才会生效。
enable-ops: true
```

## `auto-op` { #auto-op }

```yaml title="config.yml · auto-op"
# 启用或禁用 LuckPerms 中基于权限控制 OP 身份的专用系统。
#
# - 设为 true 时，任何拥有 "luckperms.autoop" 权限的用户都会自动获得
#   服务器 OP 身份。此权限可通过继承获得，也可限定在特定服务器/世界生效，
#   或设为临时权限等。
# - 此外，设为 true 会强制将上方的 "enable-ops" 选项设为 false。所有用户
#   都会被移除 OP 身份，除非拥有上述权限节点；op/deop 命令也会被
#   禁用。
# - 建议使用此选项，而非单独授予一个 '*' 权限。
auto-op: false
```

## `commands-allow-op` { #commands-allow-op }

```yaml title="config.yml · commands-allow-op"
# 拥有 OP 身份的玩家是否默认可以使用所有 LuckPerms 命令。
#
# - 设为 false 后，仅允许拥有相应权限的用户使用命令。
commands-allow-op: true
```

## `vault-unsafe-lookups` { #vault-unsafe-lookups }

```yaml title="config.yml · vault-unsafe-lookups"
# +----------------------------------------------------------------------------------------------+ #
# | Vault 集成设置                                                                               | #
# +----------------------------------------------------------------------------------------------+ #

# 是否允许通过 Vault 在服务器主线程上查询离线玩家。
#
# LuckPerms 会拦截插件尝试从服务器主线程执行的、可能引发问题的离线玩家
# 数据查询。此拦截会在出现这类查询时抛出异常(产生错误)，
# 阻止查询继续执行，否则很可能导致服务器
# 卡顿。
#
# 不过，如果愿意接受相应影响，可以将此选项
# 设为 'true' 来禁用拦截。
vault-unsafe-lookups: false
```

## `vault-group-use-displaynames` { #vault-group-use-displaynames }

```yaml title="config.yml · vault-group-use-displaynames"
# 通过 Vault API 返回权限组时，LuckPerms 是否使用权限组的“显示名称”。
#
# - 设为 true 时，返回权限组的显示名称。
# - 设为 false 时，返回权限组的标准名称/id。
vault-group-use-displaynames: true
```

## `vault-npc-group` { #vault-npc-group }

```yaml title="config.yml · vault-npc-group"
# 控制 LuckPerms 在处理 Vault 请求时为 NPC 玩家使用哪个权限组。
#
# - 由于 NPC 并非真实玩家，LuckPerms 不会为其加载任何用户数据。
#   因此，其他插件通过 Vault 检查 NPC 权限时就会遇到问题。
# - 为解决此问题，通过 Vault 检查 NPC 时会改用下方指定的权限组。
vault-npc-group: default
```

## `vault-npc-op-status` { #vault-npc-op-status }

```yaml title="config.yml · vault-npc-op-status"
# 控制 LuckPerms 在处理 Vault 请求时如何判定 NPC 玩家的 OP 身份。
#
# - 如果希望 NPC 拥有与“普通”玩家相同的权限，请设为 false。
# - 如果希望 NPC 拥有 OP 身份，请设为 true。
vault-npc-op-status: false
```

## `use-vault-server` { #use-vault-server }

```yaml title="config.yml · use-vault-server"
# 是否使用下方的 vault-server 选项。
#
# - 设为 false 时，使用上方 "server" 中定义的服务器值。
use-vault-server: false
```

## `vault-server` { #vault-server }

```yaml title="config.yml · vault-server"
# Vault 操作使用的服务器名称。
#
# - 如果不希望 Vault 操作限定于特定服务器，请将此项设为 "global"。
# - 仅在上方 use-vault-server 设为 true 时生效。
vault-server: global
```

## `vault-include-global` { #vault-include-global }

```yaml title="config.yml · vault-include-global"
# 获取元数据或玩家所属权限组时，是否考虑全局权限。
vault-include-global: true
```

## `vault-ignore-world` { #vault-ignore-world }

```yaml title="config.yml · vault-ignore-world"
# Vault 操作是否忽略所提供的所有世界参数。
vault-ignore-world: false
```

## `debug-logins` { #debug-logins }

```yaml title="config.yml · debug-logins"
# +----------------------------------------------------------------------------------------------+ #
# | 杂项设置(很少使用)                                                                         | #
# +----------------------------------------------------------------------------------------------+ #

# LuckPerms 处理登录时是否输出额外日志。
#
# - 排查 UUID 转发或数据未加载的问题时很有用。
debug-logins: false
```

## `allow-invalid-usernames` { #allow-invalid-usernames }

```yaml title="config.yml · allow-invalid-usernames"
# LuckPerms 是否允许用户名包含字母和数字以外的字符。
#
# - 请注意，由于存储实现方式的限制，用户名长度仍须不超过 16 个
#   字符。
allow-invalid-usernames: false
```

## `skip-bulkupdate-confirmation` { #skip-bulkupdate-confirmation }

```yaml title="config.yml · skip-bulkupdate-confirmation"
# LuckPerms 是否免去用户对 bulkupdate 操作的确认。
#
# - 设为 true 时，会立即执行操作。
# - 不建议启用，因为 bulkupdate 可能不可逆地删除大量
#   数据，而且此功能并非为自动执行而设计。
# - 如需自动化，应优先使用 LuckPerms API。
skip-bulkupdate-confirmation: false
```

## `disable-bulkupdate` { #disable-bulkupdate }

```yaml title="config.yml · disable-bulkupdate"
# LuckPerms 是否阻止 bulkupdate 操作。
#
# - 设为 true 时，bulkupdate 操作(即 /lp bulkupdate 命令)不会生效。
# - 设为 false 时，允许通过控制台执行 bulkupdate 操作。
disable-bulkupdate: false
```

## `prevent-primary-group-removal` { #prevent-primary-group-removal }

```yaml title="config.yml · prevent-primary-group-removal"
# LuckPerms 是否允许通过 'parent remove' 命令移除用户的主权限组。
#
# - 发生此情况时，插件会将该用户的主权限组重置为 default。
prevent-primary-group-removal: false
```

## `update-client-command-list` { #update-client-command-list }

```yaml title="config.yml · update-client-command-list"
# 权限变更时，LuckPerms 是否更新发送给客户端的命令列表。
update-client-command-list: true
```

## `register-command-list-data` { #register-command-list-data }

```yaml title="config.yml · register-command-list-data"
# LuckPerms 是否尝试为其命令注册 "Brigadier" 命令列表数据。
register-command-list-data: true
```

## `resolve-command-selectors` { #resolve-command-selectors }

```yaml title="config.yml · resolve-command-selectors"
# LuckPerms 是否尝试在 LP 命令中解析原版命令的目标选择器。
# 更多信息见：https://minecraft.wiki/w/Target_selectors
resolve-command-selectors: false
```

## `commands-read-only-mode` { #commands-read-only-mode }

```yaml title="config.yml · commands-read-only-mode"
# 插件是否为命令启用“只读”模式。
#
# 在此模式下，玩家或控制台只能执行读取或查看数据的
# 命令，无法执行任何修改数据的 LP 命令。
#
# 如果只为玩家启用只读模式，请注意，某些其他插件可能允许玩家
# 以控制台身份执行命令，从而间接执行 LP 命令。
#
# 注意：此设置不影响通过 API 与 LuckPerms 交互。
commands-read-only-mode:
  players: false
  console: false
```

## `disable-luckperms-commands` { #disable-luckperms-commands }

```yaml title="config.yml · disable-luckperms-commands"
# 是否禁用 LuckPerms 命令。设为 true 时，会阻止所有 LP 命令
# 执行。从某种意义上说，这是更严格的只读模式(见上文)。
#
# LuckPerms 仍会作为权限管理器运行，但服务器管理员将无法
# 通过命令进行修改。
#
# 如果只对玩家禁用命令，请注意，某些其他插件可能允许玩家
# 以控制台身份执行命令，从而间接执行命令。
#
# 如果同时对玩家和控制台禁用命令，LuckPerms 将完全不会尝试向服务器注册
# 命令；从某种意义上说，玩家和管理员都看不到它的命令。
#
# 注意：此设置不影响通过 API 与 LuckPerms 交互。
disable-luckperms-commands:
  players: false
  console: false
```
