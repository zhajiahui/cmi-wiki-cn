---
title: "加入时由于飞行被踢出"
source_url: "https://wiki.itemsadder.com/faq/kick-flight-on-join"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 加入时由于飞行被踢出

## 被踢问题

某些服务器可能会认为你在安装资源包时正在飞行，这取决于你的出生地点。

可能出现错误：<mark style="color:red;">"Flying is not enabled on this server"</mark>（服务器未启用飞行），或被**反作弊插件**踢出。

## 如何修复？

在 **ItemsAdder** 的 `config.yml` 文件中禁用 `hide-hud` 功能。

```yaml
  protect-player:
    black-screen: true
    hide-hud: false
```

## 仍然有问题

在 `server.properties` 文件中启用此选项：

```properties
allow-flight=true
```

此设置不会让玩家获得飞行能力，只会让 Minecraft 服务器不再因玩家未经允许飞行而将其踢出。\
为防止玩家利用此设置作弊，最好使用**反作弊插件**。
