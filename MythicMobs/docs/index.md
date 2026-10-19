---
title: MythicMobs 插件简介
source_kind: plugin-overview
translation_review: reviewed
---

# MythicMobs

MythicMobs 用于配置自定义生物及其技能、属性、装备、掉落、AI 和生成方式。技能可通过 YAML 配置，结合条件、目标选择器和触发器执行。自定义生物可以替换原版生物，也可以随机生成或通过自定义刷怪点生成。以上功能见[官方介绍](https://wiki.mythiccraft.io/mythicmobs)。

本次随包的真实版本为 **5.13.0-SNAPSHOT-1abf9862**。这是 JAR 内部版本，不能只根据文件名中的 `5.13.0` 将其视为正式版。

## 依赖

随包版本没有声明必需插件。

软依赖为 Multiverse-Core、Heroes、PhatLoots、Vault、MagicSpells、MiniaturePets、LibsDisguises、WorldGuard、Holograms、HolographicDisplays、PlaceholderAPI、PlotSquared、Residence。

## 核心命令和权限

以下依据[官方命令页](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)。该页约定 **`[]` 为必填，`<>` 为选填**，与一些插件的写法不同。

| 命令 | 用途 |
| --- | --- |
| `/mm`，或 `/mythicmobs` | 显示可用命令 |
| `/mm reload`，或 `/mm r` | 重载插件 |
| `/mm version` | 显示插件版本 |
| `/mm mobs list` | 列出生物配置 |
| `/mm mobs info [mob_name]` | 查看生物信息 |
| `/mm mobs spawn [mob_name]:<level> <amount> <world,x,y,z,yaw,pitch>` | 生成指定生物 |
| `/mm items get [item_name] <amount>` | 获取已配置的装备物品 |
| `/mm items give [player] [item_name] <amount>` | 给予玩家已配置的装备物品 |

官方完整管理权限为 `mythicmobs.admin`。官方说明单个命令权限使用 `mythicmobs.command.<command>` 形式，并明确列出 `mythicmobs.command.mobs.list`。随包版本还声明 `mythicmobs.reload` 和 `mythicmobs.signal`，不据此为其他命令推算节点。

当前官方文档持续更新，后续新增功能不直接视为这个 SNAPSHOT 构建的功能。

## 官方资料

- [官方 Wiki](https://wiki.mythiccraft.io/mythicmobs)
- [官方命令和权限](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
- [官方产品页](https://mythiccraft.io/index.php?resources/mythicmobs.1/)

[查看配置文件及中文说明](configuration/index.md)。
