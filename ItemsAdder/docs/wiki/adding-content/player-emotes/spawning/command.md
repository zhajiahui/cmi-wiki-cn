---
title: "命令"
source_url: "https://wiki.itemsadder.com/adding-content/player-emotes/spawning/command"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 命令

此方法处于测试阶段，仅适用于 **Minecraft 1.17+**

## 在世界中生成自定义玩家实体

使用 **ItemsAdder**，你还可以在世界中生成自定义玩家，并且可以为其添加动画。

## 召唤自定义玩家实体

`/iaentity summonplayer <playerName|skinUrl>`

### 通过玩家名称

`/iaentity summonplayer LoneDev`

### 通过自定义皮肤

`/iaentity summonplayer https://minesk.in/8b4bf861ea544edd8529707276d24853`

## 设置自定义皮肤

### 更改最近的自定义玩家实体的皮肤

使用 **ItemsAdder** 命令更改皮肤：\
`/iaentity playerskin <playerName|skinUrl>`\
示例：

* `/iaentity playerskin LoneDev`
* `/iaentity playerskin https://minesk.in/8b4bf861ea544edd8529707276d24853`

[custom-skin.md](../../entities/custom-skin.md)

## 创建自定义动画

[animations.md](../animations.md)
