---
title: 插件与配置
source_kind: imported-configuration
translation_review: reviewed
---

# 插件与配置

按插件查看说明、配置文件和前置关系。配置中的注释及可显示文字已整理为中文，代码块保留配置层级；命令、权限、配置键和占位符保持原样。

本批资料来自提供的插件包，共整理 **22 个目录、181 份配置与文本文件**。表中版本读取自 JAR 声明；bStats、pStats、spark 只有配置目录，包内没有对应的独立 JAR 版本。

CMI、Typewriter、MMOItems 和 MythicLib 的配置入口也列在下方，它们的官方文档仍可从原栏目进入。

## 已有 Wiki

| 插件 | 随包版本 | 配置 | 必需前置 |
| --- | --- | --- | --- |
| [CMI](../index.md) | `9.8.10.4` | [27 份](../configuration/index.md) | [CMILib](../cmilib/index.md) |
| [Typewriter](../typewriter/index.md) | `0.9.0-beta-177` | [1 份](../typewriter/configuration/index.md) | 未声明 |
| [MMOItems](../mmoitems/index.md) | `6.10.1-SNAPSHOT` | [55 份](../mmoitems/configuration/index.md) | [MythicLib](../mythiclib/index.md) |
| [MythicLib](../mythiclib/index.md) | `1.7.1-SNAPSHOT` | [13 份](../mythiclib/configuration/index.md) | 未声明 |

## 基础组件与权限

| 插件 | 随包版本 | 配置 | 必需前置 |
| --- | --- | --- | --- |
| [CMILib](../cmilib/index.md) | `1.6.0.1` | [1 份](../cmilib/configuration/index.md) | 未声明 |
| [LuckPerms](../luckperms/index.md) | `5.5.71` | [2 份](../luckperms/configuration/index.md) | 未声明 |
| [PlaceholderAPI](../placeholderapi/index.md) | `2.12.3` | [1 份](../placeholderapi/configuration/index.md) | 未声明 |
| [ProtocolLib](../protocollib/index.md) | `5.5.0-SNAPSHOT-d89a5de` | [1 份](../protocollib/configuration/index.md) | 未声明 |
| [packetevents](../packetevents/index.md) | `2.14.0` | 本包无独立配置 | 未声明 |
| [Vault](../vault/index.md) | `1.7.3-b131` | [1 份](../vault/configuration/index.md) | 未声明 |
| [LoneLibs](../lonelibs/index.md) | `1.0.65` | 本包无独立配置 | 未声明 |

## 世界、NPC 与保护

| 插件 | 随包版本 | 配置 | 必需前置 |
| --- | --- | --- | --- |
| [Citizens](../citizens/index.md) | `2.0.43-SNAPSHOT (build 4210)` | [2 份](../citizens/configuration/index.md) | 未声明 |
| [Multiverse-Core](../multiverse-core/index.md) | `5.8.1` | [3 份](../multiverse-core/configuration/index.md) | 未声明 |
| [WorldEdit](../worldedit/index.md) | `7.4.6+7648-00664b0` | [1 份](../worldedit/configuration/index.md) | 未声明 |
| [WorldGuard](../worldguard/index.md) | `7.0.17+2370-e42d8bc` | [9 份](../worldguard/configuration/index.md) | [WorldEdit](../worldedit/index.md) |

## 物品、属性与战斗

| 插件 | 随包版本 | 配置 | 必需前置 |
| --- | --- | --- | --- |
| [AttributePlus](../attributeplus/index.md) | `3.3.3.6` | [9 份](../attributeplus/configuration/index.md) | [PlaceholderAPI](../placeholderapi/index.md) |
| [CrackShot](../crackshot/index.md) | `0.98.13-x6` | [7 份](../crackshot/configuration/index.md) | 未声明 |
| [CrackShotX](../crackshotx/index.md) | `1.1.0` | [3 份](../crackshotx/configuration/index.md) | [CrackShot](../crackshot/index.md) |
| [ItemsAdder](../itemsadder/index.md) | `4.0.18` | [11 份](../itemsadder/configuration/index.md) | [ProtocolLib](../protocollib/index.md) |
| [MythicMobs](../mythicmobs/index.md) | `5.13.0-SNAPSHOT-1abf9862` | [16 份](../mythicmobs/configuration/index.md) | 未声明 |
| [NeigeItems](../neigeitems/index.md) | `1.22.0` | [15 份](../neigeitems/configuration/index.md) | 未声明 |

## 性能与统计

| 插件 | 随包版本 | 配置 | 必需前置 |
| --- | --- | --- | --- |
| [spark](../spark/index.md) | `未标明` | [1 份](../spark/configuration/index.md) | 未声明 |
| [bStats](../bstats/index.md) | `未标明` | [1 份](../bstats/configuration/index.md) | 未声明 |
| [pStats](../pstats/index.md) | `未标明` | [1 份](../pstats/configuration/index.md) | 未声明 |

## 前置关系

“必需前置”按本批 JAR 的 `depend` 字段列出。可选集成另见各插件说明；`softdepend` 不表示必须安装。CrackShotX 依赖 CrackShot，WorldGuard 依赖 WorldEdit，MMOItems 依赖 MythicLib，CMI 依赖 CMILib。

ItemsAdder 4.0.18 的必需依赖声明是 ProtocolLib；官方说明从 4.0.9 起不再需要 LoneLibs。[官方安装文档](https://wiki.itemsadder.com/plugin-usage/first-install/)

## 配置展示

配置按实际文件组织，中文说明与对应配置项放在一起。公开示例中的连接信息与服务器标识已换为占位符；数据库、玩家存档、备份、密钥、JAR 和生成资源不属于本次 Wiki 内容。
