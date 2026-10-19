---
title: 安装
source_url: https://worldedit.enginehub.org/en/latest/install/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 安装 { #installation }

<a id="contents"></a>

- [前置要求](#requirements)



  - [选择模组加载器](#choosing-a-mod-loader)

- [逐步安装](#installation-step-by-step)



  - [Bukkit / Spigot / Paper](#bukkit-spigot-paper)

  - [NeoForge 单人游戏](#neoforge-single-player)

  - [Fabric 单人游戏或服务器](#fabric-single-player-or-server)

  - [NeoForge 服务器 / Sponge](#neoforge-server-sponge)

  - [想显示选区边界线？](#want-to-see-selection-lines)

## 前置要求 { #requirements }

WorldEdit 运行于 Minecraft Java 版，既可用于单人或本地游戏，也可用于独立服务器。

**WorldEdit 无法用于 Realms、Windows 10 版、基岩版或携带版。**这些版本对模组的支持有限，或完全不支持。注意，“Windows 10 版”指 Minecraft 的一个特定版本，而不是在 Windows 10 电脑上运行的 Java 版。

安装 WorldEdit 前，必须先安装 NeoForge、Fabric、Spigot、Bukkit 或 Sponge 等“模组加载器”。下文会介绍如何选择。

### 选择模组加载器 { #choosing-a-mod-loader }

单人或本地游戏推荐以下两种选择之一：

- [NeoForge](https://neoforged.net/)

- 或者使用 [Fabric](https://fabricmc.net/)

如果运行 Minecraft 服务器，可以使用：

- [Paper](https://papermc.io/)，比 Spigot 更推荐，因为它有 WorldEdit 可以利用的改进

- [Spigot](https://www.spigotmc.org/)

- NeoForge，如果还使用其他 NeoForge 模组，推荐选择它

- [Sponge](https://www.spongepowered.org/)，也兼容 Forge 模组

注意：Paper 和 Spigot 使用自己的一套模组，通常称为“插件”，与 NeoForge、Fabric 和 Sponge 模组大多不兼容。*可以*先了解自己还想使用哪些模组或插件。一般而言，Paper 和 Spigot 的服务器管理插件和完全在服务端运行的玩法插件更多；NeoForge、Fabric 和 Sponge 则有更多大幅改变玩法的模组，通常也需要客户端安装。不过 WorldEdit 比较特别，上述两类平台都支持 😊，所以选看起来最方便的一种即可。🤙

## 逐步安装 { #installation-step-by-step }

### Bukkit / Spigot / Paper { #bukkit-spigot-paper }

搭建好基于 Bukkit 的服务器后（具体步骤见 Paper 或 Spigot 官网），[从 Modrinth 下载 WorldEdit](https://modrinth.com/plugin/worldedit/versions?l=bukkit)，确认下载的版本与 Minecraft 版本匹配。

1. 如果服务器目录中还没有“plugins”文件夹，请先创建；首次运行服务器时通常会自动创建。

2. 将 WorldEdit 的 .jar 文件移入 plugins 文件夹。

3. 启动服务器。

检查服务器日志是否有错误。出现错误时，请参阅[常见问题](faq.md)。

### NeoForge 单人游戏 { #neoforge-single-player }

首先安装 NeoForge。有许多第三方启动器可以方便地安装整合包；如果使用这类启动器，可通过启动器界面添加 WorldEdit 模组。否则，NeoForge 会在官方 Minecraft 启动器中安装一个可用的启动配置。无论以哪种方式装好 NeoForge，再[从 Modrinth 下载 WorldEdit](https://modrinth.com/plugin/worldedit/versions?l=neoforge)，确认与 Minecraft 版本和平台匹配。

1. 如果通过官方 Minecraft 启动器安装 NeoForge 启动配置，请按 [Mojang 的说明](https://help.minecraft.net/hc/en-us/articles/4409159214605)查找“.minecraft”文件夹。第三方启动器可能使用不同位置，请查阅对应启动器文档。

2. 如果“.minecraft”内还没有“mods”文件夹，请创建它；运行过一次 NeoForge 后通常已自动生成。

3. 将 WorldEdit 的 .jar 放入 mods 文件夹，再通过启动器启动 NeoForge。模组列表中应该能看到 WorldEdit。

出现错误时，请参阅[常见问题](faq.md)。

### Fabric 单人游戏或服务器 { #fabric-single-player-or-server }

首先安装 Fabric。[官网](https://fabricmc.net/wiki/install)提供不同安装方式的说明；单人游戏推荐采用 MultiMC 的安装步骤。

然后[从 Modrinth 下载 WorldEdit](https://modrinth.com/plugin/worldedit/versions?l=fabric)。确认与 Minecraft 版本和平台匹配；该网站也有 Forge 构建，注意不要下载错误版本。

Minecraft 1.14.x 还需要安装 [Fabric API 模组](https://modrinth.com/mod/fabric-api/versions)；1.15+ 不需要。

将 WorldEdit 的 .jar 添加到 MultiMC 实例的“loader mods”部分并勾选启用。如果使用官方 Mojang 启动器，则放入 mods 文件夹，位置见上方 NeoForge 安装步骤。

### NeoForge 服务器 / Sponge { #neoforge-server-sponge }

首先安装所选服务器软件。NeoForge 可下载安装器，在终端或命令提示符执行 `java -jar neoforge-installer.jar --installServer`；更完整的步骤可在网上查找。Sponge 提供[服务器安装文档](https://docs.spongepowered.org/stable/en/server/quickstart.html)。装好服务器软件后，NeoForge 用户从 [Modrinth](https://modrinth.com/plugin/worldedit/versions?l=neoforge) 下载 WorldEdit，Sponge 用户从 [Ore](https://ore.spongepowered.org/EngineHub/WorldEdit) 下载。

1. 如果没有“mods”文件夹，请创建；服务器首次运行后会自动生成。

2. 将 WorldEdit 的 .jar 放入 mods 文件夹。

3. 启动服务器。

检查服务器日志是否有错误。出现错误时，请参阅[常见问题](faq.md)。

### 想显示选区边界线？ { #want-to-see-selection-lines }

要显示选区边界线，可以选择以下方式：

1. 通过 `//drawsel` 使用服务端提供的有限选区边界显示。它只支持不超过 48x48x48 的长方体选区，旧版上限为 32x32x32，而且必须处于创造模式。这些限制来自 Minecraft 长期以来的结构方块实现。

2. 使用第三方客户端模组，例如 [WorldEdit CUI（Fabric）](https://modrinth.com/mod/worldedit-cui)。此模组需要 Fabric，因此必须先安装 Fabric。

!!! note "注意"

    使用 Minecraft 1.12 或更早版本时，除了下载旧版 WorldEdit（版本 6），可能还需要 [Mumfrey 开发的旧版 WorldEditCUI](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1292886-worldeditcui)。它需要的是 LiteLoader，安装步骤见对应页面。
