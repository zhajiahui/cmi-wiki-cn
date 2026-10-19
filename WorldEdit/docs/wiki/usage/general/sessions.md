---
title: 会话
source_url: https://worldedit.enginehub.org/en/latest/usage/general/sessions/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 会话 { #sessions }

在游戏内选择区域或更改偏好设置时，相关信息会保存在会话中。只要保持在线，会话就会一直有效。断开连接后，会话会在 10 分钟后丢弃，因此在此期间重新登录可以保留会话。连接服务器时，每个人的会话彼此独立。

会话包含多种信息，例如：

> - 当前选区
>
> - 历史记录
>
> - 方块更改数量限制
>
> - 选定用于恢复的备份快照
>
> - 剪贴板
>
> - 当前绑定的所有工具或笔刷

!!! warning "警告"

    单人游戏中，离开世界时 WorldEdit 会丢弃全部会话。因此，无法直接在世界之间复制内容，退出后也无法保留大多数工具绑定。

## 持久保存的数据 { #persistent-data }

会话中的部分数据会持久保存，即离线保存在服务器文件中，包括：

> - 选区工具的绑定
>
> - 移动工具的绑定
>
> - 服务器端 CUI 当前是否开启
>
> - 上次使用的脚本
>
> - 默认选区模式
