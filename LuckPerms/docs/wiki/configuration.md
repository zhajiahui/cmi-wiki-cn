---
title: 配置
source_url: https://luckperms.net/wiki/Configuration
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 的主配置文件位于以下位置。

| 平台          | 位置                                                                                                                          |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Bukkit/Spigot | [`/plugins/LuckPerms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/bukkit/src/main/resources/config.yml)        |
| BungeeCord    | [`/plugins/LuckPerms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/bungee/src/main/resources/config.yml)        |
| Sponge        | [`/config/luckperms/luckperms.conf`](https://github.com/LuckPerms/LuckPerms/blob/master/sponge/src/main/resources/luckperms.conf) |
| Fabric        | [`/config/luckperms/luckperms.conf`](https://github.com/LuckPerms/LuckPerms/blob/master/fabric/src/main/resources/luckperms.conf) |
| Forge         | [`/config/luckperms/luckperms.conf`](https://github.com/LuckPerms/LuckPerms/blob/master/forge/src/main/resources/luckperms.conf)  |
| Nukkit        | [`/plugins/LuckPerms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/nukkit/src/main/resources/config.yml)        |
| Velocity      | [`/plugins/luckperms/config.yml`](https://github.com/LuckPerms/LuckPerms/blob/master/velocity/src/main/resources/config.yml)      |

上方链接指向各平台的默认配置文件。请注意，新增选项时，配置文件不会自动更新。如果文件中找不到某项设置，就会使用其默认值。

<a id="index"></a>
# 目录
<a id="essential-settings"></a>
### 基本设置
* [`server`](configuration.md#server)
* [`use-server-uuid-cache`](configuration.md#use-server-uuid-cache)

<a id="storage-settings"></a>
### 存储设置
* [`storage-method`](configuration.md#storage-method)
* [`data`](configuration.md#data)
* [`pool-settings`](configuration.md#pool-settings)
* [`split-storage`](configuration.md#split-storage)

<a id="update-propagation--messaging-service"></a>
### 更新传播与消息服务
* [`sync-minutes`](configuration.md#sync-minutes)
* [`watch-files`](configuration.md#watch-files)
* [`messaging-service`](configuration.md#messaging-service)
* [`auto-push-updates`](configuration.md#auto-push-updates)
* [`push-log-entries`](configuration.md#push-log-entries)
* [`broadcast-received-log-entries`](configuration.md#broadcast-received-log-entries)
* [`redis`](configuration.md#redis)
* [`rabbitmq`](configuration.md#rabbitmq)

<a id="customization-settings"></a>
### 自定义设置
* [`temporary-add-behaviour`](configuration.md#temporary-add-behaviour)
* [`primary-group-calculation`](configuration.md#primary-group-calculation)
* [`argument-based-command-permissions`](configuration.md#argument-based-command-permissions)
* [`log-notify`](configuration.md#log-notify)
* [`meta-formatting`](configuration.md#meta-formatting)

<a id="permission-calculation--inheritance"></a>
### 权限计算与继承
* [`inheritance-traversal-algorithm`](configuration.md#inheritance-traversal-algorithm)

<a id="permission-resolution-settings"></a>
##### 权限解析设置
* [`include-global`](configuration.md#include-global)
* [`include-global-world`](configuration.md#include-global-world)
* [`apply-global-groups`](configuration.md#apply-global-groups)
* [`apply-global-world-groups`](configuration.md#apply-global-world-groups)

<a id="meta-lookup-settings"></a>
##### 元数据查询设置
* [`meta-value-selection-default`](configuration.md#meta-value-selection-default)
* [`meta-value-selection`](configuration.md#meta-value-selection)

<a id="inheritance-settings"></a>
##### 继承设置
* [`apply-wildcards`](configuration.md#apply-wildcards)
* [`apply-regex`](configuration.md#apply-regex)
* [`apply-shorthand`](configuration.md#apply-shorthand)

<a id="bukkit"></a>
###### Bukkit
* [`apply-bukkit-child-permissions`](configuration.md#apply-bukkit-child-permissions)
* [`apply-bukkit-default-permissions`](configuration.md#apply-bukkit-default-permissions)
* [`apply-bukkit-attachment-permissions`](configuration.md#apply-bukkit-attachment-permissions)

<a id="bungee"></a>
###### Bungee
* [`apply-bungee-config-permissions`](configuration.md#apply-bungee-config-permissions)

<a id="sponge"></a>
###### Sponge
* [`apply-sponge-implicit-wildcards`](configuration.md#apply-sponge-implicit-wildcards)
* [`apply-sponge-default-subjects`](configuration.md#apply-sponge-default-subjects)

<a id="extra-settings"></a>
##### 其他设置
* [`world-rewrite`](configuration.md#world-rewrite)
* [`group-weight`](https://luckperms.net/wiki/Configuration#group-weight)

<a id="fine-tuning-options"></a>
### 细调选项
<a id="server-operator--vault-bukkit-version-only"></a>
##### 服务器管理员 / Vault（仅限 Bukkit 版）
* [`enable-ops`](configuration.md#enable-ops)
* [`auto-op`](configuration.md#auto-op)
* [`commands-allow-op`](configuration.md#commands-allow-op)
* [`use-vault-server`](configuration.md#use-vault-server)
* [`vault-server`](configuration.md#vault-server)
* [`vault-include-global`](configuration.md#vault-include-global)
* [`vault-ignore-world`](configuration.md#vault-ignore-world)
* [`vault-debug`](configuration.md#vault-debug)

<a id="miscellaneous-settings"></a>
### 杂项设置
* [`debug-logins`](configuration.md#debug-logins)
* [`allow-invalid-usernames`](configuration.md#allow-invalid-usernames)
* [`prevent-primary-group-removal`](configuration.md#prevent-primary-group-removal)
* [`contexts.json`](configuration.md#contextsjson)

<a id="config-sources"></a>
# 配置来源

LuckPerms 会尝试从多个来源读取配置设置，顺序如下。

1. **系统属性**
2. **环境变量**
3. **配置文件**（`config.yml` 或 `luckperms.conf`，取决于平台）
4. 若均未找到，则使用默认值

<a id="system-properties"></a>
### 系统属性

[系统属性](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html)是配置 Java 应用程序的通用方式。既可以通过命令行参数设置，也可以通过 [`java.lang.System`](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/System.html) API 在程序中设置。

例如，要使用系统属性实现 LuckPerms config.yml 中以下 YAML 配置的效果：

```yaml
server: example

storage-method: mysql
data:
  address: 192.168.0.100
```

……请使用以下参数启动服务器：

```
java
  -Dluckperms.server=example
  -Dluckperms.storage-method=mysql
  -Dluckperms.data.address=192.168.0.100
  -jar server.jar
```

<a id="environment-variables"></a>
### 环境变量

[环境变量](https://en.wikipedia.org/wiki/Environment_variable)是配置各类应用程序的通用方式。定义方法取决于运行环境。下方给出了类 Unix shell 的示例；例如，在 Docker 容器中运行服务器时，也可以[方便地设置环境变量](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file)。

例如，要使用环境变量实现 LuckPerms config.yml 中以下 YAML 配置的效果：

```yaml
server: example

storage-method: mysql
data:
  address: 192.168.0.100
```

……请按以下方式启动服务器：

```bash
export LUCKPERMS_SERVER="example"
export LUCKPERMS_STORAGE_METHOD="mysql"
export LUCKPERMS_DATA_ADDRESS="192.168.0.100"

java -jar server.jar
```

<a id="descriptions"></a>
# 选项说明

<a id="server"></a>
### `server`
服务器名称，用于设置仅在特定服务器生效的权限。   

如果设为 "global"，则会忽略此设置。有关特定服务器权限和权限组的工作方式，详见[此处](advanced-setup.md)。

<a id="example"></a>
##### 示例
```yaml
server: global
```

___
<a id="use-server-uuid-cache"></a>
### `use-server-uuid-cache`

当 LuckPerms 缓存中没有某位玩家的记录时，是否使用服务器自身的 UUID 缓存或查询功能。

禁用此设置后，LP 只使用自己的缓存。

<a id="example-1"></a>
##### 示例
```yaml
use-server-uuid-cache: false
```

___
<a id="storage-method"></a>
### `storage-method`
插件应使用的存储方式。

支持的存储类型完整列表见[此处](storage-types.md)。

**可选值：** `mysql`、`mariadb`、`postgresql`、`sqlite`、`h2`、`json`、`yaml`、`hocon`、`mongodb`

如果 MySQL 服务器支持，建议优先选择 `mariadb`，而不是 `mysql`。通常也建议优先选择 `h2`，而不是 `sqlite`。

<a id="example-2"></a>
##### 示例
```yaml
storage-method: h2
```

___
<a id="data"></a>
### `data`
此部分用于指定各种存储方式使用的连接凭据。

* **`address`** - 数据库的主机地址。默认使用数据库引擎的标准端口。如果使用非默认端口，请在此处按 `host:port` 的格式指定。
* **`database`** - LuckPerms 应使用的数据库
* **`username`** - 使用的用户名
* **`password`** - 使用的密码。留空表示不使用身份验证。


<a id="example-3"></a>
##### 示例
```yaml
data:
  address: localhost
  database: minecraft
  username: root
  password: ''
```

___
<a id="pool-settings"></a>
### `pool-settings`

这些设置适用于 MySQL 连接池。默认值适合大多数用户。除非清楚自己在做什么，否则不要更改这些设置！

设置 MySQL 连接池的最大大小。这个值基本上决定了与后端数据库建立的实际连接数上限。
有关如何确定连接池大小的更多信息，见：

https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing

<a id="example-4"></a>
##### 示例
```yaml
data:
  pool-settings:
    maximum-pool-size: 10
```

___
<a id="split-storage"></a>
### `split-storage`
分离存储部分允许为不同类型的数据使用不同的存储方式。

**数据分为以下几类：**

* **`user`** - 用户数据，包括权限、父级和元数据
* **`group`** - 权限组数据，包括权限、父级和元数据
* **`track`** - 晋升路线（也称为“阶梯”）的数据
* **`uuid`** - `uuid <-- --> username` 的缓存。在 `/lp user` 命令中使用用户名而非 UUID 时，LuckPerms 会使用此缓存。
* **`log`** - LuckPerms 保存的操作日志

可用的存储类型已在上文说明。

<a id="example-5"></a>
##### 示例
```yaml
split-storage:
  enabled: true
  methods:
    user: mariadb
    group: yaml
    track: yaml
    uuid: mariadb
    log: mariadb
```

___
<a id="sync-minutes"></a>
### `sync-minutes`
此选项控制 LuckPerms 执行同步任务的频率。

同步任务会从存储中刷新所有数据，确保插件使用最新数据。

此功能默认禁用，因为大多数用户都用不到。不过，如果使用远程存储，又没有配置消息服务，可以考虑将此值设为 3 之类的数值。

设为 -1 可完全禁用此任务。

<a id="example-6"></a>
##### 示例
```yaml
data:
  sync-minutes: 3
```

___
<a id="watch-files"></a>
### `watch-files`
使用基于文件的存储类型时，LuckPerms 会监视数据文件的变化，并在检测到变化后安排自动更新。

如果不希望这样做，请将此选项设为 false。

<a id="example-7"></a>
##### 示例
```yaml
watch-files: true
```

___
<a id="messaging-service"></a>
### `messaging-service`
消息服务的设置。

启用并配置后，LuckPerms 会通过消息系统将更改通知其他已连接的服务器。使用 "/luckperms networksync" 命令推送更改。此服务**不存储数据**，只用于传递消息。

如果决定启用此功能，应将 "sync-minutes" 设为 -1，因为此时 LuckPerms 无需再轮询数据库来检查更改。

**可选值：**
* **`sql`** - 使用 SQL 数据库构建队列系统来通信。仅在 `storage-method` 设为 MySQL 或 MariaDB 时有效。如果此选项设为 'none'，且正在使用 SQL 存储，就会默认选择此方式。设为 `notsql` 可禁用此行为。
* **`pluginmsg`** - 使用插件消息通道通信。必须在 BungeeCord/Velocity 代理端及所有连接的后端服务器上安装 LuckPerms。存在多个代理端时，此方式不适用。所有 LP 实例都需要设置此选项。建议优先使用 `sql`，而不是此选项！
* **`lilypad`** - 使用 LilyPad 的发布/订阅功能推送更改。需要安装 LilyPad-Connect 插件。
* **`redis`** - 使用 Redis 的发布/订阅功能推送更改。
* **`rabbitmq`** - 使用 RabbitMQ 的发布/订阅功能（AMQP）推送更改。
* **`none`** - 不使用任何消息服务！

<a id="example-8"></a>
##### 示例
```yaml
messaging-service: none
```

___
<a id="auto-push-updates"></a>
### `auto-push-updates`
是否在通过命令作出更改后，让 LuckPerms 自动推送更新。

<a id="example-9"></a>
##### 示例
```yaml
auto-push-updates: true
```

___
<a id="push-log-entries"></a>
### `push-log-entries`
是否让 LuckPerms 通过消息服务向已连接的服务器推送日志条目。

<a id="example-10"></a>
##### 示例
```yaml
push-log-entries: true
```

___
<a id="broadcast-received-log-entries"></a>
### `broadcast-received-log-entries`
是否让 LuckPerms 向当前平台上的玩家广播收到的日志条目。

如果在后端服务器和 BungeeCord 代理端都安装了 LuckPerms，应在后端或代理端的其中一侧将此选项设为 false，避免玩家重复收到同一条日志通知。

<a id="example-11"></a>
##### 示例
```yaml
broadcast-received-log-entries: true
```

___
<a id="redis"></a>
### `redis`
Redis 的设置。

* **`address`** - Redis 使用的主机地址（单节点）。默认使用标准端口（6379）。如果使用非默认端口，请在此处按 `host:port` 的格式指定。
* **`addresses`** - Redis 使用的各主机地址（集群）。
* **`password`** - 使用的密码。留空表示不使用身份验证。

<a id="example-12"></a>
##### 示例
Redis 单节点示例：
```yaml
redis:
  enabled: true
  address: localhost
  password: 'passw0rd'
```

Redis 集群示例：
```yaml
redis:
  enabled: true
  addresses:
    - redis-node1
    - redis-node2
  password: 'passw0rd'
```

---
<a id="rabbitmq"></a>
### `rabbitmq`
RabbitMQ（AMQP）的设置。

* **`address`** - RabbitMQ 使用的主机地址。默认使用标准 AMQP 端口（5672）。如果使用非默认端口，请在此处按 `host:port` 的格式指定。
* **`vhost`** - LuckPerms 使用的虚拟主机。大多数情况下，可以（也应该）保留默认值。有关虚拟主机的更多信息，见[此处](https://www.rabbitmq.com/vhosts.html)。
* **`username`** - 使用的用户名。默认为 guest，该用户拥有 / 虚拟主机的所有权限。有关访问控制的更多信息，见[此处](https://www.rabbitmq.com/access-control.html)。
* **`password`** - 使用的密码。默认为 guest，即 guest 用户的密码（见上文）。

<a id="example-13"></a>
##### 示例
```yaml
rabbitmq:
  enabled: true
  address: localhost
  vhost: '/'
  username: 'guest'
  password: 'guest'
```

___
<a id="temporary-add-behaviour"></a>
### `temporary-add-behaviour`

控制临时权限、父级和元数据的时长如何累计。默认行为为 `deny`。

* **`accumulate`** - 将现有节点的剩余时长直接加到新时长上
* **`replace`** - 只保留最长的时长，忽略其他节点
* **`deny`** - 尝试添加重复的临时节点时，命令直接执行失败

<a id="example-14"></a>
##### 示例
```yaml
temporary-add-behaviour: deny
```

___
<a id="primary-group-calculation"></a>
### `primary-group-calculation`

LuckPerms 应如何确定用户的主权限组。默认为 `parents-by-weight`。

* **`stored`** - 使用文件或数据库中该用户记录里保存的值
* **`parents-by-weight`** - 使用用户权重最高的父级
* **`all-parents-by-weight`** - 与上项相同，但会将直接和间接继承的所有父级都纳入计算

<a id="example-15"></a>
##### 示例
```yaml
primary-group-calculation: parents-by-weight
```

___
<a id="argument-based-command-permissions"></a>
### `argument-based-command-permissions`

玩家使用命令修改权限数据时，LuckPerms 是否应执行额外的权限检查。

有关此系统的详细说明，见[此处](argument-based-command-permissions.md)。

<a id="example-16"></a>
##### 示例
```yaml
argument-based-command-permissions: true
```

___
<a id="log-notify"></a>
### `log-notify`

每次权限被修改时，插件是否应向用户发送日志通知。通知只会发送给拥有相应接收权限的用户。

也可以在游戏中使用 `/lp log notify off` 暂时禁用通知。

<a id="example-17"></a>
##### 示例
```yaml
log-notify: true
```

___
<a id="meta-formatting"></a>
### `meta-formatting`

LuckPerms 应如何组合前缀与后缀。

有关此系统的详细说明，见[此处](prefix-suffix-stacking.md)。

___
<a id="inheritance-traversal-algorithm"></a>
### `inheritance-traversal-algorithm`

LuckPerms 遍历“继承树”时应使用的算法。

* **`breadth-first`** - 参见：https://en.wikipedia.org/wiki/Breadth-first_search
* **`depth-first-pre-order`** - 参见：https://en.wikipedia.org/wiki/Depth-first_search
* **`depth-first-post-order`** - 参见：https://en.wikipedia.org/wiki/Depth-first_search

<a id="example-18"></a>
##### 示例
```yaml
inheritance-traversal-algorithm: depth-first-pre-order
```

___
<a id="include-global"></a>
### `include-global`
是否为此服务器上的玩家应用全局权限（即未指定服务器的权限）。

如果此选项设为 false，就只有明确指定在此服务器生效的权限才会生效。如果上方的 "server" 选项设为 global，请不要将此选项设为 false。有关特定服务器权限和权限组的工作方式，详见[此处](advanced-setup.md)。

<a id="example-19"></a>
##### 示例
```yaml
include-global: true
```

___
<a id="include-global-world"></a>
### `include-global-world`

与上方选项类似，但作用于世界。如果设为 false，就只会将为特定世界设置的权限授予用户。未指定世界上下文的权限一律不会生效。

<a id="example-20"></a>
##### 示例
```yaml
include-global-world: true
```

___
<a id="apply-global-groups"></a>
### `apply-global-groups`
此选项的作用方式与 "include-global" 相同，但控制的是权限组继承。

计算玩家权限时，插件会遍历继承树，递归解析权限组成员关系。如果此设置为 false，导致某个权限组未被“应用”，该权限组的所有父级也都不会纳入考虑，继承查询会在此处停止。

这意味着，即使玩家在某个特定服务器上间接继承了一个权限组，只要继承关系经过了一个未限定服务器的权限组，那个权限组就不会生效。

例如，将此设置设为 false，并采用以下配置：

```
User "Luck" inherits from group "admin" globally, and admin inherits from "default" on a specific server.
```

尽管 Luck 在该特定服务器上继承了 default，但 default 也不会生效，因为继承查询在 admin 处就停止了。因此，admin 的父级权限组根本不会纳入考虑。

<a id="example-21"></a>
##### 示例
```yaml
apply-global-groups: true
```

___
<a id="apply-global-world-groups"></a>
### `apply-global-world-groups`

与上方选项类似，但作用于世界。如果设为 false，就只会为用户分配并解析在特定世界设置的权限组。未指定世界上下文的权限组一律不会生效。

<a id="example-22"></a>
##### 示例
```yaml
apply-global-world-groups: true
```

___
<a id="meta-value-selection-default"></a>
### `meta-value-selection-default`

定义元数据值的选择方式。默认值为 `inheritance`。

* **`inheritance`** - 选择最先继承到的元数据值
* **`highest-number`** - 选择数值最大的元数据值
* **`lowest-number`** - 选择数值最小的元数据值

<a id="example-23"></a>
##### 示例
```yaml
meta-value-selection-default: inheritance
```

___
<a id="meta-value-selection"></a>
### `meta-value-selection`

为各个键分别定义元数据值的选择方式。

可用的设置见上方选项。

<a id="example-24"></a>
##### 示例
```yaml
meta-value-selection:
  max-homes: highest-number
```

___
<a id="apply-wildcards"></a>
### `apply-wildcards`
插件是否应应用通配符权限。

如果插件作者没有自行提供通配符权限，启用此选项后，LuckPerms 就可以代为解析。尤其是 Bukkit，原本并不赞同这种做法，但它已成为服务器管理员的常见用法。在 Sponge 上，此设置控制 "node.part.\*" 形式的通配符是否生效。

<a id="example-25"></a>
##### 示例
```yaml
apply-wildcards: true
```

___
<a id="apply-regex"></a>
### `apply-regex`
插件是否应解析正则表达式权限。

如果设为 true，LuckPerms 会检测以 "r=" 开头标记的正则表达式权限节点，并对所有匹配该节点的权限请求返回相应结果。如果没有设置任何正则表达式权限，启用此选项不会影响性能。有关此功能的更多信息，见[此处](advanced-setup.md#regex)。

<a id="example-26"></a>
##### 示例
```yaml
apply-regex: true
```

___
<a id="apply-shorthand"></a>
### `apply-shorthand`
插件是否应解析并应用简写形式（GLOB 风格）的权限。

有关此功能的更多信息，见[此处](advanced-setup.md#shorthand-permissions)。

<a id="example-27"></a>
##### 示例
```yaml
apply-shorthand: true
```

___
<a id="apply-bukkit-child-permissions"></a>
### `apply-bukkit-child-permissions`
插件是否应应用 Bukkit 子权限。

插件作者可以为自己的插件定义自定义权限结构；启用此设置后，LuckPerms 会解析并使用这些结构。

此功能默认启用，因为它是 Bukkit 的标准功能，大多数服务器管理员都希望它正常生效。不过，如果不想使用这套系统，也可以直接禁用。

<a id="example-28"></a>
##### 示例
```yaml
apply-bukkit-child-permissions: true
```

___
<a id="apply-bukkit-default-permissions"></a>
### `apply-bukkit-default-permissions`
插件是否应应用 Bukkit 默认权限。

插件作者可以定义默认授予所有用户的权限，也可以设置哪些权限应当或不应当授予 OP 玩家。如果此选项设为 false，LuckPerms 会忽略这些默认值。

此功能默认启用，因为它是 Bukkit 的标准功能，大多数服务器管理员都希望它正常生效。不过，如果不想使用这套系统，也可以直接禁用。

<a id="example-29"></a>
##### 示例
```yaml
apply-bukkit-default-permissions: true
```

___
<a id="apply-bukkit-attachment-permissions"></a>
### `apply-bukkit-attachment-permissions`
插件是否应应用 Bukkit 附加权限。

服务器上的其他插件可以为玩家添加自己的“权限附件”。这样就能为玩家授予额外权限，直到本次会话结束或这些权限被移除。如果此选项设为 false，LuckPerms 在判断玩家是否应拥有某个权限时，不会将这些附加权限纳入考虑。

启用此功能后，性能也可能略有提升。结合禁用 OP 系统，这套系统可以有效阻止插件恶意尝试向玩家随意授予权限。

此功能默认启用，因为它是 Bukkit 的标准功能，大多数服务器管理员都希望它正常生效。不过，如果不想使用这套系统，也可以直接禁用。

<a id="example-30"></a>
##### 示例
```yaml
apply-bukkit-attachment-permissions: true
```

___
<a id="apply-bungee-config-permissions"></a>
### `apply-bungee-config-permissions`
插件是否应应用 BungeeCord config.yml 中定义的权限和权限组。

如果设为 false，LuckPerms 会忽略这些值。

此功能默认禁用，因为权限本应在 LuckPerms 中定义，这样才能在游戏中与其他数据一起查看和编辑。

<a id="example-31"></a>
##### 示例
```yaml
apply-bungee-config-permissions: false
```

___
<a id="apply-sponge-implicit-wildcards"></a>
### `apply-sponge-implicit-wildcards`
插件是否应按照 Sponge 的隐式通配符继承系统来解析并应用权限。

也就是说：如果用户获授了 `example`，就还应自动获得 `example.function`、`example.another`、`example.deeper.nesting` 等权限。

如果此选项设为 false，就不会应用这套系统。

此功能默认启用，因为它是 Sponge 的标准功能，大多数服务器管理员和插件作者都希望它正常生效。不过，如果不想使用这套系统，也可以禁用。

<a id="example-32"></a>
##### 示例
```hocon
apply-sponge-implicit-wildcards=true
```

___
<a id="apply-sponge-default-subjects"></a>
### `apply-sponge-default-subjects`
插件是否应应用 Sponge 默认主体的权限。

插件可以操作一组默认授予所有用户的权限。如果此选项设为 false，插件在判断玩家是否拥有某个权限时，会忽略这些数据。

此功能默认启用，因为它是 Sponge 的标准功能，大多数服务器管理员和插件作者都希望它正常生效。不过，如果不想使用这套系统，也可以禁用。

<a id="example-33"></a>
##### 示例
```hocon
apply-sponge-default-subjects=true
```

___
<a id="world-rewrite"></a>
### `world-rewrite`

为送入上下文计算的世界设置“别名”。这些别名会与真实世界名称一起提供。会递归应用。

<a id="example-34"></a>
##### 示例
```yaml
world-rewrite:
  world_nether: world
  world_the_end: world
```

___
<a id="enable-ops"></a>
### `enable-ops`
是否使用原版 OP 系统。

如果设为 false，所有用户的 OP 身份都会被撤销，op/deop 命令也会被禁用。

<a id="example-35"></a>
##### 示例
```yaml
enable-ops: true
```

___
<a id="auto-op"></a>
### `auto-op`
如果设为 true，任何拥有 "luckperms.autoop" 权限的用户都会自动获得服务器管理员（OP）身份。

此权限可以继承，也可以限定在特定服务器或世界、设为临时权限等。此外，将此选项设为 true 会强制把上方的 "enable-ops" 选项设为 false。除拥有该权限节点的用户外，所有用户的 OP 身份都会被撤销，op/deop 命令也会被禁用。

务必注意，此设置只在玩家刚加入服务器及切换世界时检查。因此，仅从用户身上移除此权限，并不会自动撤销其 OP 身份。玩家可能需要重新登录，更改才会生效。

建议使用此选项，而不是授予单独的 '\*' 权限。

<a id="example-36"></a>
##### 示例
```yaml
auto-op: false
```

___
<a id="commands-allow-op"></a>
### `commands-allow-op`
是否允许 OP 玩家使用 LuckPerms 命令。

设为 false 后，只有拥有相应权限的用户才可以使用这些命令。

<a id="example-37"></a>
##### 示例
```yaml
commands-allow-op: true
```

___
<a id="use-vault-server"></a>
### `use-vault-server`
是否使用下方的 `vault-server` 选项。

此选项设为 false 时，Vault 操作会使用上方 "server" 中定义的服务器值。

<a id="example-38"></a>
##### 示例
```yaml
use-vault-server: false
```

___
<a id="vault-server"></a>
### `vault-server`
Vault 操作使用的服务器名称。

如果不想让 Vault 操作限定到特定服务器，请设为 "global"。

仅当上方的 `use-vault-server` 设为 true 时才会生效。

<a id="example-39"></a>
##### 示例
```yaml
vault-server: global
```

___
<a id="vault-include-global"></a>
### `vault-include-global`
获取元数据或玩家所属权限组时，是否将全局权限纳入考虑。

<a id="example-40"></a>
##### 示例
```yaml
vault-include-global: true
```

___
<a id="vault-ignore-world"></a>
### `vault-ignore-world`
Vault 操作是否应忽略传入的所有世界参数。

默认情况下，如果没有提供世界参数，就会将权限设置在玩家当前所在的世界。（Vault 这设计真是 10/10。）设为 true 可改变此行为。

<a id="example-41"></a>
##### 示例
```yaml
vault-ignore-world: false
```

___
<a id="vault-debug"></a>
### `vault-debug`
插件使用 Vault 功能时，LuckPerms 是否应向控制台输出调试信息。

<a id="example-42"></a>
##### 示例
```yaml
vault-debug: false
```

___
<a id="debug-logins"></a>
### `debug-logins`

LuckPerms 处理登录时，是否应输出额外日志。

遇到 UUID 转发问题或数据未加载的问题时，这些日志会有帮助。

调试消息如下所示：
```
[INFO]: [LP] Processing pre-login for c1d60c50-70b5-4722-8057-87767557e50d - Luck
[INFO]: UUID of player Luck is c1d60c50-70b5-4722-8057-87767557e50d
[INFO]: [LP] Processing login for c1d60c50-70b5-4722-8057-87767557e50d - Luck
[INFO]: Luck[/xxx:xxx] logged in with entity id xxx at ([xxx]x, x, x)
```

<a id="example-43"></a>
##### 示例
```yaml
debug-logins: false
```

___
<a id="allow-invalid-usernames"></a>
### `allow-invalid-usernames`

如果设为 true，LuckPerms 将允许用户名中包含字母和数字以外的字符。

请注意，受存储实现的设计限制，用户名仍必须不超过 16 个字符。

<a id="example-44"></a>
##### 示例
```yaml
allow-invalid-usernames: false
```

___
<a id="prevent-primary-group-removal"></a>
### `prevent-primary-group-removal`

如果设为 false，插件将允许使用 `parent remove` 命令移除用户的主权限组，并将其主权限组重设为 default。

<a id="example-45"></a>
##### 示例
```yaml
prevent-primary-group-removal: false
```

___




<a id="contextsjson"></a>
## contexts.json
`contexts.json` 文件与 LuckPerms 主配置文件位于同一目录，可用于设置以下两项内容。

<a id="static-contexts"></a>
### 静态上下文
静态上下文是永不变化的[上下文](context.md)，默认应用于服务器上的所有玩家。

LuckPerms 默认提供一个名为 "server" 的静态上下文。它的值通过主配置文件中的 `server` 选项设置。

例如，我的群组服中有 3 个派系服务器，各有不同的名称。在每个服务器的 LP 配置中，我分别将服务器名称设为 `factions1`、`factions2` 和 `factions3`。不过，我想在所有这些服务器上授予某个权限。

为此，可以在所有派系服务器上添加一个名为 `servertype` 的静态上下文，并将其设为 `factions`。
```json
{
  "static-contexts": {
  	"servertype": "factions"
  },
}
```

然后，就可以使用 `/lp group default permission set some.permission true servertype=factions`，在所有派系服务器上设置这个权限。


<a id="default-contexts"></a>
### 默认上下文
默认上下文是执行服务器上的所有命令时，如果没有明确指定，就会默认使用的[上下文](context.md)。

```json
{
  "default-contexts": {
  	"server": "survival"
  },
}
```

采用上述设置后，执行 `/lp user Luck permission set some.permission true`，就会为我将 `some.permission` 设为 true，生效的上下文为 `server=survival`。
