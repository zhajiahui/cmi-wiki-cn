---
title: 聊天室
---

# 聊天室

## 简介

聊天室可以为玩家创建临时或持久的群聊空间。它独立于公共聊天，并提供更多自定义设置。玩家同时只能加入一个聊天室，但可以查看多个聊天室的消息。

## 命令

```text
/cmi chat create [chatRoomName] (-private) (-locked) (-persistent)
```

创建聊天室时，需要为其指定一个唯一名称。名称没有特殊限制，只用于标识这个聊天室。

`-private` 会将聊天室设为仅限受邀加入，创建时需要拥有 `cmi.command.chat.create.private` 权限。不使用此参数时，聊天室为公开状态，任何人都可以加入。

`-locked` 主要用于强制玩家留在聊天室中，使其无法自行离开。例如，可以为工作人员创建一个“询问室”。需要拥有 `cmi.command.chat.create.locked` 权限。

`-persistent` 会创建服务器重启后仍保留的聊天室。默认情况下，聊天室是临时的，会在服务器重启后消失，也会在最后一位成员离开一段时间后消失。需要拥有 `cmi.command.chat.create.persistent` 权限。

```text
/cmi chat join [chatRoomName]
```

加入指定的聊天室。只能加入公开聊天室、已收到邀请的聊天室，或自己拥有的聊天室。`cmi.command.chat.joinbypass` 权限可以绕过加入限制。

```text
/cmi chat invite [playerName]
```

邀请指定玩家加入你当前所在的聊天室。玩家需要拥有 `cmi.command.chat.invite` 权限。

```text
/cmi chat leave
```

如果当前已加入聊天室，则离开该聊天室。玩家无法离开带有 `-locked` 的聊天室，除非拥有 `cmi.command.chat.leave.locked` 权限。

```text
/cmi chat kick [playerName]
```

将玩家踢出聊天室。只有聊天室所有者可以执行，并且需要拥有 `cmi.command.chat.kick` 权限。

```text
/cmi chat force [playerName] (chatRoomName)
```

强制玩家加入指定聊天室，会绕过该玩家的加入限制。命令发送者需要拥有 `cmi.command.chat.force` 权限，或者从控制台执行此命令。  
如果命令发送者是已经加入聊天室的玩家，可以省略聊天室名称。

```text
/cmi chat see (chatRoomName)
```

无需加入即可查看指定聊天室的消息。不能查看自己无权加入的聊天室。此命令需要 `cmi.command.chat.see` 权限；拥有 `cmi.command.chat.seebypass` 权限后，也能查看无权加入的聊天室。

```text
/cmi chat unsee (chatRoomName)
```

停止查看指定聊天室的消息。此命令需要 `cmi.command.chat.see` 权限。

```text
/cmi chat list
```

列出当前聊天室中的所有玩家。需要拥有 `cmi.command.chat.list` 权限。

```text
/cmi chat listrooms
```

列出所有当前活跃且你有权加入的聊天室。需要拥有 `cmi.command.chat.listrooms` 权限。

---

[查看原文](https://www.zrips.net/cmi/extra/chat-rooms/)
