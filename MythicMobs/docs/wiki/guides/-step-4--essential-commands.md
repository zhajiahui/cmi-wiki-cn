---
title: （步骤 4）基础命令
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/%28Step-4%29-Essential-Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# （步骤 4）基础命令

MythicMobs 有[许多命令]。虽然每个命令都有自己的用途，但在深入使用前，你可能想先了解其中更常用的命令，本指南正是为此而写！

# 重载插件 {#reload-the-plugin}

`/mm reload`  
如果不重载，你所做的所有更改都不会应用！

# 基础操作 {#essentials}

### 生成生物 {#spawn-a-mob}

`/mm mobs spawn [mobtype]`  
生成指定的生物。

### 移除生物 {#remove-a-mob}

`/mm mobs kill [mobtype]`：击杀指定类型的生物。  
`/mm mobs killall`：击杀所有非持久生物。
`/mm mobs killall <radius>`：击杀指定半径内的所有非持久生物。

### 获取物品 {#get-an-item}

`/mm items get [itemname]`  
获取指定物品。

# 实用功能 {#utility}

### 调试等级 {#debug-level}

`/mm debug [level]`  
这就是调试命令！它会根据传入的 level 参数，在控制台输出正在执行的机制和事件的更多信息。使用 `/mm debug 4` 会显示“最高到等级 4”的调试消息，而 `/mm debug 0` 会关闭所有调试消息。

### Listactive {#listactive}

`/mm mobs listactive <mobtype>`  
列出所有活动生物，可以按生物类型筛选，还能通过对应条目获取更多信息、传送到生物处，或击杀、移除它们。

### 获取坐标 {#get-coordinates}

`/mm utilities getcoordinates`  
获取自己所在位置、所指位置和目标位置的格式化坐标。

### 获取物品信息 {#get-item-info}

`/mm utilities getiteminfo`  
查看手持物品上的所有 NBT。

### 获取路径 {#get-path}

`/mm utilities getpathstring`  
使用此命令可以放置方块并获取一组坐标，用于 patrol AI 行为目标或类似场景。

### 列出所有实体 {#list-all-entities}

`mm utilities listallentities <radius/mobtype>`  
列出所有实体，并按距离或类型筛选。

**[>> 第 5 步](-step-5--extra-notes.md)**
