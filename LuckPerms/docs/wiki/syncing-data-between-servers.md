---
title: 服务器之间同步数据
source_url: https://luckperms.net/wiki/Syncing-data-between-servers
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

可以方便地在不同服务器之间同步数据。

<a id="requirements"></a>
## 要求
要同步数据，**必须**使用远程存储类型。所有服务器都需要连接到同一个数据库。

更多信息见[存储类型](storage-types.md)页面。需要使用该页面列出的某一种“**远程数据库**”。

<a id="instantly-propagating-updates"></a>
## 即时传播更新
仅让服务器连接到同一个数据库，并不足以让数据在服务器之间即时同步。LuckPerms 需要先知道数据发生了变化，才能更新。

可以通过多种方式实现。

这些设置都位于配置中的 `Update propagation & messaging service` 部分。

<a id="sync-interval"></a>
### 同步间隔
可以设置同步间隔，让 LuckPerms 定期从数据库拉取最新更改。   
此项通过配置控制，默认为 `-1`（表示禁用该任务）。

```yml
sync-minutes: -1
```

<a id="watch-files"></a>
### 监视文件
如果使用基于文件的存储类型（YAML、JSON 或 HOCON），LuckPerms 可以监听这些数据文件的变化，并在检测到更改后自动更新。

这意味着，只需编辑其中一个数据文件并保存，更改就会应用到服务器。   
此项通过配置控制，默认启用。

```yml
watch-files: true
```

<a id="lp-sync"></a>
### /lp sync
`/lp sync` 命令会让插件从数据库或文件中拉取最新更改。

<a id="messaging-services"></a>
### 消息服务
配置完成后，发生更改时，群组服中的其他服务器会收到通知，并从数据库请求最新的数据副本。

此服务**不存储数据**，只用于传递消息。

可以通过配置中的 `messaging-service` 选项设置消息服务。

<a id="possible-options"></a>
#### 可选值
| 服务 | 说明 | 
|---------|-------------|
| sql | 使用 SQL 数据库构建队列系统来通信。使用远程 SQL 存储时，默认选择此方式。 |
| pluginmsg | 使用插件消息通道与代理端通信。必须在代理端和所有连接的后端服务器上安装 LuckPerms。存在多个代理端时，此方式不适用。 |
| lilypad | 使用 LilyPad Connect 的发布/订阅系统通信。 |
| redis | 连接到 Redis 实例，并使用发布/订阅功能通信。 |
| rabbitmq | 连接到 RabbitMQ 实例，并通过 AMQP 使用发布/订阅功能通信。 |
| nats | 连接到 Nats 实例，并使用发布/订阅功能通信。 | 
| custom | 强制 messaging-service 使用你通过 LuckPerms API 提供的自定义实现。 |

也可以通过 LuckPerms API 提供此服务的自定义实现。务必将配置中的 messaging-service 选项设为 `custom`，否则启动时会抛出错误。
