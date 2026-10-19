---
title: Wiki 收录范围
source_kind: translation-inventory
translation_review: reviewed
---

# Wiki 收录范围

本页列出插件包所含主插件的官方 Wiki 正文。API、SDK 接口参考单独排除；安装、配置、命令、权限、内容制作和排错资料按官方目录收录。

文档以归档时的官方页面为准，随包插件版本见[插件与配置](index.md)。官网持续更新的文档不等同于随包版本的专用手册。原文中的历史版本说明和限制保留。

| 插件 | 已收录正文 | API 排除项 | 缺源或失效项 | 收录情况 |
| --- | ---: | ---: | ---: | --- |
| [CMILib](../cmilib/wiki/home.md) | 4 页 | 2 | 0 | 已收录当前可取得的非 API 正文 |
| [LuckPerms](../luckperms/wiki/home.md) | 45 页 | 2 | 0 | 已收录当前可取得的非 API 正文 |
| [PlaceholderAPI](../placeholderapi/wiki/home.md) | 15 页 | 3 | 0 | 已收录当前可取得的非 API 正文 |
| [ProtocolLib](../protocollib/wiki/home.md) | 8 页 | 8 | 1 | 可取得的正文已收录；失效项见下方 |
| [packetevents](../packetevents/wiki/index.md) | 5 页 | 10 | 1 | 可取得的正文已收录；失效项见下方 |
| [Vault](../vault/wiki/readme.md) | 3 页 | 2 | 4 | 可取得的正文已收录；失效项见下方 |
| [LoneLibs](../lonelibs/wiki/readme.md) | 2 页 | 1 | 0 | 已收录当前可取得的非 API 正文 |
| [Citizens](../citizens/wiki/main-page.md) | 179 页 | 5 | 62 | 可取得的正文已收录；失效项见下方 |
| [Multiverse-Core](../multiverse-core/wiki/core.md) | 22 页 | 2 | 0 | 已收录当前可取得的非 API 正文 |
| [WorldEdit](../worldedit/wiki/index.md) | 29 页 | 15 | 0 | 已收录当前可取得的非 API 正文 |
| [WorldGuard](../worldguard/wiki/index.md) | 26 页 | 12 | 1 | 可取得的正文已收录；失效项见下方 |
| [AttributePlus](../attributeplus/wiki/master.md) | 40 页 | 7 | 0 | 已收录当前可取得的非 API 正文 |
| [CrackShot](../crackshot/wiki/Home.md) | 9 页 | 1 | 0 | 已收录当前可取得的非 API 正文 |
| [CrackShotX](../crackshotx/index.md) | 0 页 | 0 | 1 | 随包 1.1.0 对应的官方文档尚未确认 |
| [ItemsAdder](../itemsadder/wiki/index.md) | 304 页 | 9 | 0 | 已收录当前可取得的非 API 正文 |
| [MythicMobs](../mythicmobs/wiki/index.md) | 969 页 | 2 | 14 | 可取得的正文已收录；失效项见下方 |
| [NeigeItems](../neigeitems/wiki/public-readme.md) | 16 份公开资料 | 3 | 1 | 公开资料；完整 Wiki 为付费内容，尚缺正文 |
| [spark](../spark/wiki/home.md) | 18 页 | 2 | 0 | 已收录当前可取得的非 API 正文 |
| [bStats](../bstats/wiki/home.md) | 11 页 | 4 | 4 | 可取得的正文已收录；失效项见下方 |
| [pStats](../pstats/index.md) | 0 页 | 0 | 2 | 未发现独立官方 Wiki |

API 排除项既包括整页接口参考，也包括混合页面中的接口片段，因此不能用此列与正文页数直接相加。缺源项包括空白页、失效引用及无法确认的文档入口。原站的同页别名不重复计数。

NeigeItems 的公开仓库资料未替代其付费 Wiki。CrackShotX 和 pStats 尚无可确认的独立完整文档，保留已提供的配置入口。

## CMILib

### API 排除项

- [https://www.zrips.net/cmilib/](https://www.zrips.net/cmilib/)：仅排除页内接口片段。Maven 依赖声明属于 SDK 接入，其余说明和全部历史下载项均译。
- [https://github.com/Zrips/CMILib/blob/master/README.md](https://github.com/Zrips/CMILib/blob/master/README.md)：仅排除页内接口片段。仅排除 Maven、Gradle 接入参考，普通安装、更新、支持和插件表完整保留。

## LuckPerms

### API 排除项

- [https://luckperms.net/wiki/Developer-API-Usage](https://luckperms.net/wiki/Developer-API-Usage)：插件 API 接口与编程用法文档
- [https://luckperms.net/wiki/Developer-API](https://luckperms.net/wiki/Developer-API)：插件 API 接口与编程用法文档

## PlaceholderAPI

### API 排除项

- [https://wiki.placeholderapi.com/developers/configuration-api-hytale/](https://wiki.placeholderapi.com/developers/configuration-api-hytale/)：API 接口或占位符扩展实现编程文档
- [https://wiki.placeholderapi.com/developers/creating-a-placeholderexpansion/](https://wiki.placeholderapi.com/developers/creating-a-placeholderexpansion/)：API 接口或占位符扩展实现编程文档
- [https://wiki.placeholderapi.com/developers/using-placeholderapi/](https://wiki.placeholderapi.com/developers/using-placeholderapi/)：API 接口或占位符扩展实现编程文档

## ProtocolLib

### API 排除项

- [https://github.com/dmulloy2/ProtocolLib/wiki/Adding-ProtocolLib-as-a-Dependency](https://github.com/dmulloy2/ProtocolLib/wiki/Adding-ProtocolLib-as-a-Dependency)：插件开发依赖或 ProtocolLib API 类型、监听器及操作接口参考。
- [https://github.com/dmulloy2/ProtocolLib/wiki/Packet-listeners-and-adapters](https://github.com/dmulloy2/ProtocolLib/wiki/Packet-listeners-and-adapters)：插件开发依赖或 ProtocolLib API 类型、监听器及操作接口参考。
- [https://github.com/dmulloy2/ProtocolLib/wiki/PacketContainer](https://github.com/dmulloy2/ProtocolLib/wiki/PacketContainer)：插件开发依赖或 ProtocolLib API 类型、监听器及操作接口参考。
- [https://github.com/dmulloy2/ProtocolLib/wiki/ProtocolManager](https://github.com/dmulloy2/ProtocolLib/wiki/ProtocolManager)：插件开发依赖或 ProtocolLib API 类型、监听器及操作接口参考。
- [https://dev.bukkit.org/projects/protocollib/pages/tutorial](https://dev.bukkit.org/projects/protocollib/pages/tutorial)：旧版 Java API 数据包监听、读写及发送开发教程。
- [https://dmulloy2.net/ProtocolLib/javadoc/](https://dmulloy2.net/ProtocolLib/javadoc/)：JavaDoc API 接口参考目录，按目录整体排除。
- [https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/Readme.md](https://github.com/dmulloy2/ProtocolLib/blob/d89a5deb3eb625b16846da57fbbb04bfdd0d031d/Readme.md)：仅排除页内接口片段。API 接入和数据包代码示例排除；普通说明、资源、编译与兼容性完整保留。
- [https://www.spigotmc.org/resources/protocollib.1997/](https://www.spigotmc.org/resources/protocollib.1997/)：仅排除页内接口片段。仅排除 SDK 接入、TinyProtocol 和 Maven 示例；服主正文、命令、配置和支持信息完整保留。
### 缺源或失效项

- [https://dev.bukkit.org/projects/protocollib/pages/main](https://dev.bukkit.org/projects/protocollib/pages/main)：官方明确说明此页自动生成并故意留空，无可翻译的使用正文。

## packetevents

### API 排除项

- [https://docs.packetevents.com/introduction/a-developers-introduction/](https://docs.packetevents.com/introduction/a-developers-introduction/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/introduction/development-setup/](https://docs.packetevents.com/introduction/development-setup/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/processing-and-sending/advanced-packetevents-example-combining-our-knowledge/](https://docs.packetevents.com/processing-and-sending/advanced-packetevents-example-combining-our-knowledge/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/processing-and-sending/master/](https://docs.packetevents.com/processing-and-sending/master/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/sending-and-simulating-packets/](https://docs.packetevents.com/sending-and-simulating-packets/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/setup-when-bundling/a-beginners-guide-to-bundling/](https://docs.packetevents.com/setup-when-bundling/a-beginners-guide-to-bundling/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/setup-when-bundling/master/](https://docs.packetevents.com/setup-when-bundling/master/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://docs.packetevents.com/setup-when-bundling/tweaking-packetevents/](https://docs.packetevents.com/setup-when-bundling/tweaking-packetevents/)：PacketEvents SDK 开发环境、实例生命周期、设置接口或数据包监听/发送接口参考。
- [https://javadocs.packetevents.com/](https://javadocs.packetevents.com/)：JavaDoc API 参考目录，按目录整体排除。
- [https://docs.packetevents.com/development-setup](https://docs.packetevents.com/development-setup)：README 旧接入地址，已验证跳转至现行 SDK 接入页面。
### 缺源或失效项

- [https://docs.packetevents.com/404/](https://docs.packetevents.com/404/)：仓库自定义 404 模板，不是文档章节。

## Vault

### API 排除项

- [https://milkbowl.github.io/VaultAPI/](https://milkbowl.github.io/VaultAPI/)：VaultAPI JavaDoc 接口参考目录，按目录整体排除。
- [https://dev.bukkit.org/projects/vault](https://dev.bukkit.org/projects/vault)：仅排除页内接口片段。仅排除 Java 接口接入和 Maven 仓库参考；配置、权限、支持项、统计字段和退出说明已全译。
### 缺源或失效项

- [https://github.com/MilkBowl/Vault/wiki/Home](https://github.com/MilkBowl/Vault/wiki/Home)：HTTP 页面可读，但当前仅为欢迎语、留言或第三方服务器广告，未构成可确认的官方使用文档。
- [https://github.com/MilkBowl/Vault/wiki/%23-An-editable-page-for-some-reason](https://github.com/MilkBowl/Vault/wiki/%23-An-editable-page-for-some-reason)：HTTP 页面可读，但当前仅为欢迎语、留言或第三方服务器广告，未构成可确认的官方使用文档。
- [https://github.com/MilkBowl/Vault/wiki/Official-Vault-MC-Server-!](https://github.com/MilkBowl/Vault/wiki/Official-Vault-MC-Server-!)：HTTP 页面可读，但当前仅为欢迎语、留言或第三方服务器广告，未构成可确认的官方使用文档。
- [https://github.com/MilkBowl/Vault/wiki/_Footer](https://github.com/MilkBowl/Vault/wiki/_Footer)：HTTP 页面可读，但当前仅为欢迎语、留言或第三方服务器广告，未构成可确认的官方使用文档。

## LoneLibs

### API 排除项

- [https://github.com/JavaPlugins/LoneLibs/blob/master/README.md](https://github.com/JavaPlugins/LoneLibs/blob/master/README.md)：仅排除页内接口片段。仅排除 API Maven 依赖接入示例；弃用说明和完整所含库清单已译。

## Citizens

### API 排除项

- [1.x/API](https://wiki.citizensnpcs.co/1.x/API)：API/SDK integration reference or Java trait example
- [API](https://wiki.citizensnpcs.co/API)：API/SDK integration reference or Java trait example
- [Denizen API](https://wiki.citizensnpcs.co/Denizen_API)：API/SDK integration reference or Java trait example
- [Denizen API Command Template](https://wiki.citizensnpcs.co/Denizen_API_Command_Template)：API/SDK integration reference or Java trait example
- [TestCharacterType](https://wiki.citizensnpcs.co/TestCharacterType)：API/SDK integration reference or Java trait example
### 缺源或失效项

- [Citizens Wiki/CitizensUI](https://wiki.citizensnpcs.co/Citizens_Wiki/CitizensUI)：Official page exists but its current revision has no body
- [Custom Denizen Commands](https://wiki.citizensnpcs.co/Custom_Denizen_Commands)：Official page exists but its current revision has no body
- [Denizen config.yml](https://wiki.citizensnpcs.co/Denizen_config.yml)：Official page exists but its current revision has no body
- [Denizen temp](https://wiki.citizensnpcs.co/Denizen_temp)：Official page exists but its current revision has no body
- [Denizen/](https://wiki.citizensnpcs.co/Denizen/)：Official body unavailable
- [Denizen/0.7/Getting Started](https://wiki.citizensnpcs.co/Denizen/0.7/Getting_Started)：Official page exists but its current revision has no body
- [Denizen/Quick Guide to Using Denizen](https://wiki.citizensnpcs.co/Denizen/Quick_Guide_to_Using_Denizen)：Official page exists but its current revision has no body
- [Basic Example Quests](https://wiki.citizensnpcs.co/Basic_Example_Quests)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Commands and Permissions](https://wiki.citizensnpcs.co/Commands_and_Permissions)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Mobs.yml](https://wiki.citizensnpcs.co/Mobs.yml)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Evil NPCs](https://wiki.citizensnpcs.co/Evil_NPCs)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Npc profiles.yml](https://wiki.citizensnpcs.co/Npc_profiles.yml)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Quests.yml](https://wiki.citizensnpcs.co/Quests.yml)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Quester](https://wiki.citizensnpcs.co/Quester)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Formatting Questing Text](https://wiki.citizensnpcs.co/Formatting_Questing_Text)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Guard](https://wiki.citizensnpcs.co/Guard)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Healer](https://wiki.citizensnpcs.co/Healer)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Installing](https://wiki.citizensnpcs.co/Installing)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [List of Initial node types](https://wiki.citizensnpcs.co/List_of_Initial_node_types)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [List of Objective node types](https://wiki.citizensnpcs.co/List_of_Objective_node_types)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [List of Requirement node types](https://wiki.citizensnpcs.co/List_of_Requirement_node_types)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Notes from aufdemrand](https://wiki.citizensnpcs.co/Notes_from_aufdemrand)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [List of Rewards node types](https://wiki.citizensnpcs.co/List_of_Rewards_node_types)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Message Formatting](https://wiki.citizensnpcs.co/Message_Formatting)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [More Example Quests](https://wiki.citizensnpcs.co/More_Example_Quests)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Npc-profiles.yml](https://wiki.citizensnpcs.co/Npc-profiles.yml)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [1.x/Quest Text Formatting Tips](https://wiki.citizensnpcs.co/1.x/Quest_Text_Formatting_Tips)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [A Two-Part Example Quest](https://wiki.citizensnpcs.co/A_Two-Part_Example_Quest)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [More example quests](https://wiki.citizensnpcs.co/More_example_quests)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Questing Cook-Book](https://wiki.citizensnpcs.co/Questing_Cook-Book)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Advanced Questing Ideas](https://wiki.citizensnpcs.co/Advanced_Questing_Ideas)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Quick Start](https://wiki.citizensnpcs.co/Quick_Start)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Wizard](https://wiki.citizensnpcs.co/Wizard)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen Actions](https://wiki.citizensnpcs.co/Denizen_Actions)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Interact Script Requirements](https://wiki.citizensnpcs.co/Interact_Script_Requirements)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Color Codes](https://wiki.citizensnpcs.co/Denizen/Color_Codes)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Interact Scripts](https://wiki.citizensnpcs.co/Denizen/Interact_Scripts)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Interact Scripts/Interact Requirements](https://wiki.citizensnpcs.co/Denizen/Interact_Scripts/Interact_Requirements)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Example Scripts/Advanced Scripts](https://wiki.citizensnpcs.co/Denizen/Example_Scripts/Advanced_Scripts)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/config.yml](https://wiki.citizensnpcs.co/Denizen/config.yml)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Writing Scripts](https://wiki.citizensnpcs.co/Denizen/0.7/Writing_Scripts)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Assigning Scripts](https://wiki.citizensnpcs.co/Denizen/0.7/Assigning_Scripts)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Interact Scripts/Triggers](https://wiki.citizensnpcs.co/Denizen/Interact_Scripts/Triggers)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Activity Scripts/Activities](https://wiki.citizensnpcs.co/Denizen/Activity_Scripts/Activities)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Location Bookmark](https://wiki.citizensnpcs.co/Location_Bookmark)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Interact Scripts/Custom Interact Requirements](https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Custom_Interact_Requirements)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/In Game Commands](https://wiki.citizensnpcs.co/Denizen/In_Game_Commands)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Flags](https://wiki.citizensnpcs.co/Denizen/0.7/Flags)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Listeners](https://wiki.citizensnpcs.co/Denizen/0.7/Listeners)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Interact Scripts/Custom Requirements](https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Custom_Requirements)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Interact Scripts/Custom Triggers](https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Custom_Triggers)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Activity Scripts/Custom Activities](https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts/Custom_Activities)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/0.7/Activity Scripts/Event API](https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts/Event_API)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Assignments](https://wiki.citizensnpcs.co/Denizen/Assignments)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Commands/If](https://wiki.citizensnpcs.co/Denizen/Commands/If)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Script Requirements](https://wiki.citizensnpcs.co/Denizen/Script_Requirements)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Other](https://wiki.citizensnpcs.co/Denizen/Other)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Supported Plugins](https://wiki.citizensnpcs.co/Supported_Plugins)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Wallet](https://wiki.citizensnpcs.co/Wallet)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Activities](https://wiki.citizensnpcs.co/Activities)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Click Triggers](https://wiki.citizensnpcs.co/Click_Triggers)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag
- [Denizen/Replaceables](https://wiki.citizensnpcs.co/Denizen/Replaceables)：Official page link is a red link: target absent from the official page directory and parse response has no exists flag

## Multiverse-Core

### API 排除项

- [API Usages](https://mvplugins.org/core/developers/api-usage/)：Developer API and SDK integration reference
- [Developer API Starter](https://mvplugins.org/core/developers/developer-api-starter/)：Developer API and SDK integration reference

## WorldEdit

### API 排除项

- [Actors](https://worldedit.enginehub.org/en/latest/api/concepts/actors/)：说明 Actor、Locatable 与 EditSessionEvent 等 Java API 类型和回调。
- [Adapters](https://worldedit.enginehub.org/en/latest/api/concepts/adapters/)：说明 BukkitAdapter 等适配器如何转换平台 API 对象。
- [Blocks](https://worldedit.enginehub.org/en/latest/api/concepts/blocks/)：说明 BlockType、BlockState、BaseBlock 的构造与 Java 方法。
- [Edit Sessions](https://worldedit.enginehub.org/en/latest/api/concepts/edit-sessions/)：说明 EditSession 创建、构建器和事件接口。
- [Extents](https://worldedit.enginehub.org/en/latest/api/concepts/extents/)：说明 Extent 接口、AbstractDelegateExtent 与 setBlock 扩展。
- [API Concepts](https://worldedit.enginehub.org/en/latest/api/concepts/)：API Concepts 目录，列出的子项均为接口类型和编程用法。
- [Local Sessions](https://worldedit.enginehub.org/en/latest/api/concepts/local-sessions/)：说明通过 SessionManager 获取及操作 LocalSession 的 Java API。
- [Patterns and Masks](https://worldedit.enginehub.org/en/latest/api/concepts/patterns-and-masks/)：说明通过 Java 类构造 Pattern 和 Mask，而非游戏内字符串语法。
- [Regions](https://worldedit.enginehub.org/en/latest/api/concepts/regions/)：说明 Region、Iterable<BlockVector3> 与编程遍历。
- [Registries](https://worldedit.enginehub.org/en/latest/api/concepts/registries/)：说明通过平台无关注册表 API 按 ID 获取方块等对象。
- [Clipboard Examples](https://worldedit.enginehub.org/en/latest/api/examples/clipboard/)：原文明确标注为剪贴板 API 文档，提供 Java 复制、粘贴及存储示例。
- [API Examples](https://worldedit.enginehub.org/en/latest/api/examples/)：原文明确说明此目录为 WorldEdit API 的常见编程用例。
- [LocalSession Examples](https://worldedit.enginehub.org/en/latest/api/examples/local-sessions/)：原文明确标注为程序化访问会话数据的 API 文档。
- [Developer API](https://worldedit.enginehub.org/en/latest/api/)：Developer API 入口，说明接口库、编程依赖和 API 使用条件。
- [Internal APIs](https://worldedit.enginehub.org/en/latest/api/internal-apis/)：定义 Java 访问规则下的内部 API 边界及不稳定接口。

## WorldGuard

### API 排除项

- [As a Dependency](https://worldguard.enginehub.org/en/latest/developer/dependency/)：说明插件如何声明 WorldGuard API 编译依赖，以及 API 版本兼容性。
- [WorldGuard API](https://worldguard.enginehub.org/en/latest/developer/)：WorldGuard API 入口，明确说明通过 API 访问数据并链接 JavaDocs。
- [Internal APIs](https://worldguard.enginehub.org/en/latest/developer/internal-apis/)：定义 Java 访问规则下的内部 API 边界及不稳定接口。
- [From Bukkit Objects](https://worldguard.enginehub.org/en/latest/developer/native-objects/)：说明用 WorldGuardPlugin.wrapPlayer 等方法转换 Bukkit 对象。
- [Custom Flags and Session Handlers](https://worldguard.enginehub.org/en/latest/developer/regions/custom-flags/)：说明第三方插件注册自定义旗标和 SessionHandler 的 Java API。
- [Region Events](https://worldguard.enginehub.org/en/latest/developer/regions/events/)：说明 DisallowedPVPEvent 事件及取消该事件的 API 行为。
- [Flag Calculation](https://worldguard.enginehub.org/en/latest/developer/regions/flag-calculation/)：说明 ApplicableRegionSet、Flags 与旗标查询方法的编程用法。
- [Working with Regions](https://worldguard.enginehub.org/en/latest/developer/regions/)：原文明确说明通过 region data API 从其他插件访问区域数据。
- [Managers](https://worldguard.enginehub.org/en/latest/developer/regions/managers/)：说明 RegionContainer、RegionManager 与 Java 区域读取方法。
- [Regions](https://worldguard.enginehub.org/en/latest/developer/regions/protected-region/)：说明 ProtectedRegion 各子类及其字段、方法与 Java 示例。
- [Querying Protection](https://worldguard.enginehub.org/en/latest/developer/regions/protection-query/)：说明用 Flags.BUILD、RegionQuery 等 Java API 查询保护。
- [Spatial Queries](https://worldguard.enginehub.org/en/latest/developer/regions/spatial-queries/)：说明 RegionManager、ApplicableRegionSet 与查询缓存 API。
### 缺源或失效项

- [Search](https://worldguard.enginehub.org/en/latest/search/)：HTTPSConnectionPool(host='worldguard.enginehub.org', port=443): Max retries exceeded with url: /en/latest/search/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

## AttributePlus

### API 排除项

- [脚本方法](https://ersha.gitbook.io/attributeplus-pro/shu-xing-jiao-ben/jiao-ben-api)：仅列出 AttrScriptUtils/Utils 方法签名和参数的接口参考。
- [开发文档](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang)：开发者事件、组件接口和注解的索引参考，无配置或操作教程。
- [API](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/api)：AttributeAPI 方法签名的纯接口参考。
- [AttributeComponent](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/attributecomponent)：SubAttribute 构造器与完整接口类参考。
- [AttributeType](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/attributecomponent/attributetype)：AttributeType 枚举常量的接口参考；普通脚本属性类型教程另页已完整收录。
- [AttributeName](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/attributecomponent/shu-xing-ming-shuo-ming)：AttributeName 接口字段名参考。
- [ReadComponent](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/readcomponent)：DescriptionRead 接口、读取类型和优先级声明参考。

## CrackShot

### API 排除项

- [接入 CrackShot（开发接口参考）](https://github.com/Shampaggon/CrackShot/wiki/Hooking-into-CrackShot)：CSUtility 函数、参数、返回值及 Bukkit 事件接口参考；普通配置、命令、权限和 FAQ 全文保留。

## CrackShotX

### 缺源或失效项

- CrackShotX 1.1.0 对应官方 Wiki：随包描述缺少作者/官网，公开检索未取得对应官方导航、sitemap 或仓库；未确认旧文档版本归属，内部页面总数未知。

## ItemsAdder

### API 排除项

- [Denizen API](https://wiki.itemsadder.com/developers/denizen-api)：API interface reference
- [Java API](https://wiki.itemsadder.com/developers/java-api)：API interface reference
- [Events](https://wiki.itemsadder.com/developers/java-api/events)：API interface reference
- [Usage](https://wiki.itemsadder.com/developers/java-api/examples)：API interface reference
- [HUDs, GUIs, images and more](https://wiki.itemsadder.com/developers/java-api/huds-guis-images-and-more)：API interface reference
- [API Utilities](https://wiki.itemsadder.com/developers/java-api/old-api)：API interface reference
- [Skript API](https://wiki.itemsadder.com/developers/skript-api)：API interface reference
- [Expert users](https://wiki.itemsadder.com/developers/skript-api/expert-users-1)：API interface reference
- [Simple](https://wiki.itemsadder.com/developers/skript-api/simple)：API interface reference

## MythicMobs

### API 排除项

- [https://wiki.mythiccraft.io/mythicmobs/API](https://wiki.mythiccraft.io/mythicmobs/API)：API接口章节
- [https://wiki.mythiccraft.io/mythicmobs/API/Placeholders](https://wiki.mythiccraft.io/mythicmobs/API/Placeholders)：API接口章节
### 缺源或失效项

- [https://wiki.mythiccraft.io/mythicmobs/changelogs/5.10.x_changelogs](https://wiki.mythiccraft.io/mythicmobs/changelogs/5.10.x_changelogs)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/examples/Armors](https://wiki.mythiccraft.io/mythicmobs/examples/Armors)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/examples/Weapons](https://wiki.mythiccraft.io/mythicmobs/examples/Weapons)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/examples/Tools](https://wiki.mythiccraft.io/mythicmobs/examples/Tools)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ExampleMechanic2](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ExampleMechanic2)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/conditions/start](https://wiki.mythiccraft.io/mythicmobs/conditions/start)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/databases/items/overview](https://wiki.mythiccraft.io/mythicmobs/databases/items/overview)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/databases/items/potions](https://wiki.mythiccraft.io/mythicmobs/databases/items/potions)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/databases/mobs/aigoals](https://wiki.mythiccraft.io/mythicmobs/databases/mobs/aigoals)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/skills/conditions/PackVersion](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/PackVersion)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/skills/conditions/PackVersionGreater](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/PackVersionGreater)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle/Particle-Types/BlockCrack](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle/Particle-Types/BlockCrack)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/skills/stringvariables](https://wiki.mythiccraft.io/mythicmobs/skills/stringvariables)：官方地址返回 HTTP 404
- [https://wiki.mythiccraft.io/mythicmobs/wikis/Mobs/Options](https://wiki.mythiccraft.io/mythicmobs/wikis/Mobs/Options)：官方地址返回 HTTP 404

## NeigeItems

### API 排除项

- [README Development](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/README.md#development)：开发者依赖接入配置。
- [README API](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/README.md#api)：Java API 函数及插件接入接口示例；与用户配置示例分开。
- [Javadoc](https://ankhorg.github.io/NeigeItems-Kotlin/)：官方 README 指向的 Java 接口参考站。
### 缺源或失效项

- [完整官方 Wiki（付费入口声明，未提供公开目录 URL）](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/README.md#L7)：当前主分支与 1.22.0 README 均明确标注 Wiki 付费；公开仓库无用户 Wiki 导航或目录，无法枚举付费墙后的页面。

## spark

### API 排除项

- [https://spark.lucko.me/docs/Developer-API](https://spark.lucko.me/docs/Developer-API)：开发者 API 接口、事件和代码示例。
- [https://spark.lucko.me/docs/misc/Raw-spark-data](https://spark.lucko.me/docs/misc/Raw-spark-data)：JSON/HTTP 端点、JSONPath 参数、Protobuf 模式和解析示例，属于数据 API/格式接口参考。

## bStats

### API 排除项

- [https://bstats.org/docs/rest-api](https://bstats.org/docs/rest-api)：公开 HTTP REST API 端点与返回数据参考。
- [https://bstats.org/add-plugin](https://bstats.org/add-plugin)：六步 Metrics SDK 接入向导，主体为依赖及实例化接口；一般注册说明已在服务主页全文收录。
- [https://bstats.org/](https://bstats.org/)：仅排除页内接口片段。只排除 Metrics/SimplePie Java API 示例；其余服务说明、接入步骤、展示统计和赞助内容全译。
- [https://bstats.org/docs/custom-charts](https://bstats.org/docs/custom-charts)：仅排除页内接口片段。仅排除 Java/PHP API 实现示例及语言切换控件；图表用途、网站注册步骤、全部图表类型和开发状态保留。
### 缺源或失效项

- [https://bstats.org/getting-started](https://bstats.org/getting-started)：官方 sitemap 仍列出的旧地址，本次返回 HTTP 404；现行入口另有覆盖或明确 API 排除。
- [https://bstats.org/getting-started/metrics-class](https://bstats.org/getting-started/metrics-class)：官方 sitemap 仍列出的旧地址，本次返回 HTTP 404；现行入口另有覆盖或明确 API 排除。
- [https://bstats.org/help/custom-charts](https://bstats.org/help/custom-charts)：官方 sitemap 仍列出的旧地址，本次返回 HTTP 404；现行入口另有覆盖或明确 API 排除。
- [https://bstats.org/help/rest-api](https://bstats.org/help/rest-api)：官方 sitemap 仍列出的旧地址，本次返回 HTTP 404；现行入口另有覆盖或明确 API 排除。

## pStats

### 缺源或失效项

- [https://pstats.devs.beer/](https://pstats.devs.beer/)：HTTP 200 的统计前端，不是 Wiki。已检查首页 HTML 和公开 JS 路由，未发现独立文档、安装配置手册、命令或帮助目录。
- [https://pstats.devs.beer/sitemap.xml](https://pstats.devs.beer/sitemap.xml)：HTTP 404，未提供文档站点地图。
