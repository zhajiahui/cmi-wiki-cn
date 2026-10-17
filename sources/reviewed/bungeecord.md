CMI 支持 BungeeCord 和 Velocity。本页说明支持与不支持的功能。今后希望能进一步完善对 BungeeCord 和 Velocity 的支持，但不作承诺。

BungeeCord 是 Minecraft 群组网络的代理程序，更多信息见：<https://www.spigotmc.org/wiki/bungeecord/>；Velocity 也是群组网络代理程序，更多信息见：<https://docs.papermc.io/velocity>。

两者的工作机制相同，因此下方列出的现有命令、权限和占位符均适用于两者。

## 命令与权限：

```text
/cmi bbroadcast (!) [message] (-s:[serverName,serverName])
-> cmi.command.bbroadcast - Sends special message to all players on all servers

/cmi msg [playerName] [message]
-> cmi.command.msg.togglebypass - Allows to send private messages even if player has pm toggled off
-> cmi.command.msg - Sends message to player
-> cmi.command.msg.[maingroupname].send - Allows to send private messages to specific player groups
-> cmi.command.msg.clean - Allows to send clean messages to player using ! at beginning
-> cmi.command.msg.noreply - Allows to send clean messages to player by using !- at beginning without option to reply
-> cmi.command.msg.vanish - Allows to send private messages to vanished players

/cmi reply [message]
-> cmi.command.reply - Reply to last message sender

/cmi sendall [serverName]
-> cmi.command.sendall.bypass - Prevents player from being sent to target server
-> cmi.command.sendall - Send all online players to target server

/cmi server [serverName] (playerName) (-f)
-> cmi.command.server.others - Connect to bungeecord server
-> cmi.command.server - Connect to bungeecord server

/cmi serverlist
-> cmi.command.serverlist - Show server list
-> cmi.command.serverlist.others - Show server list

/cmi staffmsg [message/toggle/on/off]
-> cmi.command.staffmsg - Sends message to staff channel

-> cmi.bungee.publicmessages.[servername] - Allows to send public messages to target server
```

## 占位符

```text
%cmi_user_bungeeserver%
%cmi_bungee_total_[serverName]%
%cmi_bungee_current_[serverName]%
%cmi_bungee_motd_[serverName]%
%cmi_bungee_onlinestatus_[serverName]%
```

## CMI 的 Settings/Chat.yml 配置：

```text
BungeeCord:
  # You can disable bungeecord support entirely if you are exrperiencing issues with it
  # When setting this to false some features like public messages over bungee cord, private messages over bungeecord, portals over bungecoord and other features will stop working
  # Keep in mind that regular behavior of those features will remain intacted
  Enabled: true
  # When set to true player names from entire bungee network will be included into tab complete
  NamesInTabComplete: true
```

以及：

```text
  Bungee:
    # Attention! This will require you to have CMI Bungee plugin which can be found at zrips.net
    # Or direct download https://www.zrips.net/cmi/
    # Do you want to enable private messaging over bungeecord
    Messages: true
    # Do you want to enable public messaging over bungeecord
    # Player needs to have cmi.bungee.publicmessages.[servername] permission node to be able to send messages to target server
    PublicMessages: true
    # Do you want to enable staff messaging over bungeecord
    StaffMessages: true
```

## 安装步骤：

- 如果还没有 CMI 授权，请先[购买 CMI 授权](https://www.spigotmc.org/resources/3742/)，用于你的群组网络。
- 在*每个独立的后端服务器*上安装 CMI 和 CMILib，***代理服务器除外***。
- 按照本文的说明配置 CMI，启用 CMI 聊天功能，并启用 BungeeCord 支持。Velocity 的操作相同。
- 下载 [CMI Bungee 文件](https://www.zrips.net/cmib/)或 [CMI Velocity 文件](https://www.zrips.net/cmiv/)，**只放在代理服务器上**。
- 设置完成后，启动群组网络，留意控制台或 latest.log，检查是否出现问题。

## CMI 的 BungeeCord / Velocity 文件能帮助同步 x y z 吗？

目前大概还不行。它不会同步背包、金钱，也不会同步传送点和家等数据。Zrips 是否有意增加更多支持？根据我了解到的情况，是有的，但目前没有预计完成时间。

目前，它主要用于同步公共聊天、私聊和管理组消息，并更好地支持 /cmi server、/cmi serverlist、穿过传送门，以及切换服务器时的自定义消息。

## CMI 聊天与 BungeeCord / Velocity 聊天

要使用 CMI 的 BungeeCord 聊天功能，必须启用 CMI 的聊天管理功能。编辑 CMI 的 Settings/Chat.yml 文件：

```text
Chat:
  # Will try to modify chat to display it in a defined format
  ModifyChatFormat: true
```

然后逐一检查其他与聊天有关的选项。

记得设置相应权限，例如：`cmi.bungee.publicmessages.[servername]`。

## 常见问题：

**如果运行 3 个服务器，而且都在同一个群组网络中，需要购买三份授权吗？**  
不需要，一份授权就覆盖整个群组网络。

**聊天是全服互通的吗？**  
是的，聊天会显示在群组网络中的所有服务器上。

**可以同步所有服务器上的金钱吗？**  
目前没有这项功能。不过可以借助名为 MySQL Player Data Bridge 的第三方插件（我们不为这种配置提供支持）。

**可以在所有服务器之间同步传送点吗？**  
目前 CMI 没有这项功能。

**可以在所有服务器之间同步家吗？**  
和传送点一样，目前 CMI 没有这项功能。

**可以使用传送门将玩家传送到群组网络中的另一个服务器吗？**  
可以，使用 CMI 的[传送门功能](https://www.zrips.net/cmi/portals/)即可实现。

**可以使用 /server 和 /serverlist 来代替 /cmi server 和 /cmi serverlist 吗？**  
打开 CMI 的 Alias.yml 文件，在其中启用这些命令。

**如果一条命令无法在某个服务器上执行，还能将它发送过去吗？**  
目前 CMI 没有这项功能。

**如果一条命令没有将玩家转移到另一个服务器，还能这样做吗？**  
可以，用 /cmi aliaseditor 创建使用 /cmi server 和／或占位符的别名。

**可以在服务器之间共享背包吗？**  
目前没有这项功能。不过可以借助名为 MySQL Player Data Bridge 的第三方插件（我们不为这种配置提供支持）。

**所有 CMI 实例可以共用一个数据库吗？**  
不可以。默认使用 SQLite，也可以选择 MySQL；但每个服务器的 tablePrefix 选项必须各不相同，以免出现问题。

**为什么 CMI BungeeCord / Velocity 文件没有生成任何文件夹？**  
这是正常现象。CMI 的 BungeeCord 文件目前不会生成任何额外文件或文件夹。可以在任意后端服务器上执行 /cmi version，确认 CMI 是否已与 BungeeCord / Velocity 对接，输出应显示 BungeeCord 已对接。

**支持 Velocity 吗？**  
已加入支持，需要最新版的 CMI、CMILib jar 文件，以及可免费下载的 [CMIV（Velocity）jar](https://www.zrips.net/cmiv/) 文件。

**可以显示自定义的服务器切换消息，避免显示加入或离开服务器的消息吗？**  
可以，在 config.yml 中找到 `ServerSwitch:` 并设为 true。启用后，如果 BungeeCord 服务器上安装了 CMIB，或 Velocity 上安装了 CMIV，插件会尝试检测玩家前往的服务器，并在可以判断时显示服务器切换消息，代替退出消息。
