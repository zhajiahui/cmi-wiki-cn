---
title: 多服务器安装
source_url: https://luckperms.net/wiki/Network-Installation
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 从一开始就考虑了多服务器网络的使用场景。正确安装和配置后，权限数据会在服务器之间同步，并立即传遍整个网络。

在多服务器网络中安装 LuckPerms 时，常规的[安装步骤](installation.md)和[运行要求](installation.md#requirements)仍然适用。

不过，还需要满足一项额外要求。

**所有 LuckPerms 实例都必须连接到同一个存储系统。** 这意味着只能使用 `MySQL`、`MariaDB`、`PostgreSQL` 或 `MongoDB`。LuckPerms 必须连接到同一台 SQL / MongoDB 服务器，并访问同一个数据库或集合。
___

<a id="pre-setup"></a>
## 安装前的准备
开始前，需要检查以下事项。这些步骤并非可有可无，而是十分重要，请勿跳过！

LuckPerms 支持使用 `BungeeCord`、`Velocity` 或 `LilyPad` 的多服务器网络。

<a id="velocity"></a>
### Velocity

按照 Velocity 的[说明](https://docs.papermc.io/velocity/getting-started/)完成设置，并配置[现代转发](https://docs.papermc.io/velocity/player-information-forwarding/#configuring-modern-forwarding)。Fabric 服务器还需要在 `FabricProxy-Lite.toml` 中将 `hackEarlySend` 改为 `true`。

<a id="bungeecord"></a>
### BungeeCord
LuckPerms 保存数据时，使用玩家的唯一标识符（UUID）作为索引。玩家的 UUID 由服务端提供，不过其值可能取决于 `online-mode` 设置的状态。

使用 BungeeCord 时，**务必**正确设置和配置 BungeeCord 的 IP 转发系统。

在各 BungeeCord 代理端的 `config.yml` 文件中，需要设置：
```yml
ip_forward: true
```

在每台后端 Spigot 服务器的 `spigot.yml` 文件中，需要设置：
```yml
# This option is found under "settings"
bungeecord: true
```

在每台后端 Sponge 服务器的 `config/sponge/global.conf` 文件中，需要设置：
```hocon
sponge {
    bungeecord {
        ip-forwarding=true
    }
}
```

修改这些设置后，需要完整重启 Spigot/Sponge 服务器和 BungeeCord 代理端。

还应为多服务器网络正确配置防火墙，防止恶意用户伪造连接，直接接入后端服务器。SpigotMC 在[此处](https://www.spigotmc.org/wiki/firewall-guide/)提供了相关指南。

<a id="lilypad"></a>
### LilyPad
如果使用 LilyPad，应按照 [LilyPad 设置指南](http://www.lilypadmc.org/threads/connecting-your-bukkit-servers.13/)，确认后端服务器已安装并正确配置 `LilyPad-Connect` 插件。

___

<a id="installing-luckperms-across-your-network"></a>
## 在整个多服务器网络中安装 LuckPerms
在多服务器网络中安装 LP 比较简单，不过设置每个实例时，都需要修改一些配置选项。

通用的[安装指南](installation.md)详细介绍了如何在单台服务器实例上安装 LuckPerms。网络中的每台服务器都应按该指南安装。（大多数情况下，只需将插件 JAR 放入 plugins/mods 文件夹）

安装 LuckPerms 后，需要停止服务器，打开主配置文件，并特别留意以下选项：

<a id="server"></a>
#### [`server`](configuration.md#server)

如果想在这套多服务器配置中按服务器分别设置权限或分配权限组继承关系，需要修改配置文件中的 `server` 值。（它就在文件顶部，很容易找到！😄）

玩家连接到该实例时，此值会用于为所有玩家定义一个 "server" 上下文。

关于设置服务器和世界专属权限的更多信息，见[此处](advanced-setup.md)和[此处](context.md)。

<a id="storage-method"></a>
#### [`storage-method`](configuration.md#storage-method)

如本页开头所述，要让数据在实例之间同步，所有 LuckPerms 实例都必须连接到同一个数据库。

这意味着应将 `storage-method` 设为 'mysql'、'mariadb'、'postgresql' 或 'mongodb'。修改这些选项时，记得填写数据库连接信息！

<a id="messaging-service"></a>
#### [`messaging-service`](configuration.md#messaging-service)

“消息服务”是 LuckPerms 的一项功能，可以在发生修改时通知网络中的其他服务器，也可以在整个网络中分发日志条目。

* 如果运行多台服务器，它们没有连接到同一台运行 LuckPerms 的代理端，但使用同一个数据库，请将此选项设为 `sql`。
* 如果运行的是小型多服务器网络，只有一台运行 LuckPerms 的 BungeeCord/Velocity 代理端，应将此选项设为 `pluginmsg`。
* 如果运行 LilyPad 多服务器网络，请将其设为 `lilypad`。
* 如果多服务器网络中有不止一台 BungeeCord/Velocity 代理端，建议安装 Redis 服务器（既然你已经在运行多代理端网络，这里就假定你知道如何安装！），并将此选项设为 `redis`。修改此选项后，记得填写 Redis 凭据！

___

<a id="the-bungeecordvelocity-version-of-luckperms"></a>
## BungeeCord/Velocity 版 LuckPerms
一个常见误解是：安装代理端版 LuckPerms 后，就不必再在后端 Spigot/Sponge 服务器上安装。这是不对的。

在代理端安装 LuckPerms 后，它会做两件事：

* 处理**代理端插件**发起的权限检查。它*不会*拦截或处理后端服务器插件发起的权限检查。
* 当 `messaging-service` 设为 'pluginmsg' 时，在整个网络中转发更新通知和日志消息。

也就是说，如果希望 LuckPerms 响应后端 Spigot 或 Sponge 服务器上的权限检查，即使代理端已经安装，也仍需在相应后端服务器上安装。
