---
title: Multiverse-Core 插件介绍来源
source_kind: plugin-overview
translation_review: reviewed
---

# Multiverse-Core 插件介绍来源

核对日期：2026-10-19。介绍对应版本：`5.8.1`。以下为本次直接读取的官方文档及官方仓库片段；网页仅整理空白和换行，源码摘录可能选自不同位置。

## Multiverse-Core 5.8.1 plugin.yml

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/resources/plugin.yml](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/resources/plugin.yml)

取得：本轮 GitHub 只读工具直接取得对应提交内容。

```text
name: Multiverse-Core
main: org.mvplugins.multiverse.core.MultiverseCore
website: 'https://modrinth.com/plugin/multiverse-core'
description: 'The original Bukkit Multi-World Plugin!'
softdepend: ['Vault', 'PlaceholderAPI']
api-version: 1.13
version: ${version}
```

## Multiverse-Core 官方文档入口

来源：[https://mvplugins.org/core/](https://mvplugins.org/core/)

取得：HTTP 200；2026-10-19T12:47:01.760Z。

```text
Basics
 Install Multiverse-Core from scratch or how to Upgrade from Multiverse 4!
 If you've never used Multiverse before you should check out the Basic Multiverse Tutorial .
 Read how to use Multiverse with Permissions 
 Found a bug? Contact us on our Discord 
 or open an issue on GitHub 
 .
Intermediate
 Add some more functionality with the sub plugins: Inventories , Portals , NetherPortals , SignPortals 
 Customize your world with World Properties 
 Generate some awesome new terrain with a Custom Generator Plugins 
Advanced
 A complete Command Reference 
 A simple Big List O' Permissions 
 Various Destinations you can teleport to
```

## Multiverse-Core 必需与可选前置

来源：[https://mvplugins.org/core/fundamentals/installation/](https://mvplugins.org/core/fundamentals/installation/)

取得：HTTP 200；2026-10-19T12:48:39.399Z。

```text
Prerequisites
 Ensure that all of the sub-modules are of the same major version.
 Make sure that you have multiverse-core if you are using any sub-modules, it is a dependency.
Optional Prerequisites
 We highly recommend a permissions plugin. You can use any plugin that implements the SuperPerms API. Here are some known working permission plugins (as of 2025):
 LuckPerms 
 (recommended)
 This guide (on the right) will take you through setting up permissions, but if you want to go there now, click here .
Download links
 Modrinth 
 Bukkit 
 Hangar 

Step 1
 Grab the jar.
Download the Multiverse-Core JAR from the release site 
 .
 There is NO Zip package available. Multiverse-Core (and MV Plugins) will create default configs for you on the first run.
 *Optional: Install the Multiverse-Portals or Multiverse-NetherPortals plugins!
 Place it in your plugins folder like so:
```

## Multiverse-Core 命令参考

来源：[https://mvplugins.org/core/fundamentals/commands-usage/](https://mvplugins.org/core/fundamentals/commands-usage/)

取得：HTTP 200；2026-10-19T12:48:39.405Z。

```text
In Multiverse, we have included a handy new in-game help system. To access this help, simply type /mv. In order to properly read this command reference, we'll walk through reading the "usage" of a command.
Command Case
 Whenever reading this wiki or the in-game /mv help, you should remember that items in ALL CAPS should be replaced with a variable. Items in lowercase should be typed exactly how they appear.
Optional vs. Required Params
 Items inside square braces ([]) are OPTIONAL where items inside (<>) are REQUIRED
Simple command example
 Let's look at a simple one first:
 /mv info [world] 

/mv create <name> <environment> [--seed <seed> --generator <generator[:id]> --world-type <worldtype> --adjust-spawn --no-structures --biome <biome> --generator-settings <json>] 
 At first, you will notice that there are 2 required params, name, and environment. Then you will see the flags afterward. If you want to use a seed you must add --seed gargamel to the command string. If you want a generator the same principle applies: --generator BukkitFullOfMoon. The order of flags does not matter. Full examples of this command are located at the Create Command reference .
```

## Multiverse-Core 5.8.1 ListCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ListCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ListCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.873Z。

```text
@Subcommand("list")
    @CommandPermission("multiverse.core.list.worlds")
    @Syntax("[--filter <filter>] [--page <page>] [--raw]")
            @Syntax("[--filter <filter>] [--page <page>] [--raw]")
        @CommandAlias("mvlist|mvl")
```

## Multiverse-Core 5.8.1 InfoCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/InfoCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/InfoCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.875Z。

```text
@Subcommand("info")
    @CommandPermission("multiverse.core.info")
    @Syntax("[world] [--page <page>] [--filter <filter>]")
            @Syntax("[world]")
            @Syntax("[--page <page>] [--filter <filter>]")
        @CommandAlias("mvinfo|mvi")
```

## Multiverse-Core 5.8.1 CreateCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/5.8.1/src/main/java/org/mvplugins/multiverse/core/commands/CreateCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/5.8.1/src/main/java/org/mvplugins/multiverse/core/commands/CreateCommand.java)

取得：HTTP 200；2026-10-19T12:56:46.152Z。

```text
@Subcommand("create")
    @CommandPermission("multiverse.core.create")
    @CommandCompletion("@empty @environments @flags:groupName=" + Flags.NAME)
    @Syntax("<name> <environment> [--seed <seed> --generator <generator[:id]> --world-type <worldtype> " +
            "--no-adjust-spawn --no-structures --generate-bonus-chest --force-spawn-position <x,y,z:pitch:yaw> " +
            "--biome <biome> --generator-settings <json-settings> --properties <prop1=value1,prop2=value2,...>]")
    
        @CommandAlias("mvcreate|mvc")
```

## Multiverse-Core 5.8.1 ImportCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ImportCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ImportCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.876Z。

```text
@Subcommand("import")
    @CommandPermission("multiverse.core.import")
    @Syntax("<name> <environment> [--generator <generator[:id]> --no-adjust-spawn --biome <biome> " +
            @Syntax("<name>")
            @Syntax("<environment>")
            @Syntax("[--generator <generator[:id]> --no-adjust-spawn --biome <biome> " +
        @CommandAlias("mvimport|mvim")
```

## Multiverse-Core 5.8.1 TeleportCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/TeleportCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/TeleportCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.878Z。

```text
@CommandAlias("mvtp")
    @Subcommand("teleport|tp")
    @CommandPermission("@mvteleport")
    @Syntax("[player] <destination> [--unsafe --silent]")
            @Syntax("[player]")
            @Syntax("<destination>")
            @Syntax("[--unsafe --silent]")
```

## Multiverse-Core 5.8.1 SpawnCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/SpawnCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/SpawnCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.879Z。

```text
@CommandAlias("mvspawn")
    @Subcommand("spawn")
    @CommandPermission("@mvspawn")
    @Syntax("[player] [--unsafe]")
            @Syntax("[player]")
            @Syntax("[--unsafe]")
```

## Multiverse-Core 5.8.1 SetSpawnCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/SetSpawnCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/SetSpawnCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.881Z。

```text
@CommandAlias("mvsetspawn")
    @Subcommand("setspawn")
    @CommandPermission("multiverse.core.spawn.set")
    @Syntax("[worldname:x,y,z[,yaw,pitch]] [--unsafe]")
            @Syntax("[worldname:x,y,z[,yaw,pitch]]")
            @Syntax("[--unsafe]")
        @CommandAlias("mvss")
```

## Multiverse-Core 5.8.1 ReloadCommand

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ReloadCommand.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/commands/ReloadCommand.java)

取得：HTTP 200；2026-10-19T12:57:39.880Z。

```text
@Subcommand("reload")
    @CommandPermission("multiverse.core.reload")
        @CommandAlias("mvreload|mvr")
```

## Multiverse-Core 5.8.1 世界访问和细分传送检查

来源：[https://github.com/Multiverse/Multiverse-Core/blob/5.8.1/src/main/java/org/mvplugins/multiverse/core/permissions/CorePermissionsChecker.java](https://github.com/Multiverse/Multiverse-Core/blob/5.8.1/src/main/java/org/mvplugins/multiverse/core/permissions/CorePermissionsChecker.java)

取得：HTTP 200；2026-10-19T12:57:11.608Z。

```text
public boolean hasWorldAccessPermission(@NotNull CommandSender sender, @NotNull MultiverseWorld world) {
        return hasPermission(sender, concatPermission(CorePermissions.WORLD_ACCESS, world.getName()));
    }

    /**
     * Checks if the sender is exempt from wor

public boolean checkSpawnPermission(
            @NotNull CommandSender teleporter,
            @NotNull Scope scope,
            @NotNull MultiverseWorld world) {
        if (config.getUseFinerTeleportPermissions()) {
            return hasSpawnPermission(teleporter, scope, world);
        }
        return hasSpawnPermission(teleporter, scope, null);
    }

    /**
     * Check if the issuer has any base spawn permission of `multiverse.core.spawn.self` or `multiverse.core.spawn.other`
     *
     * @param sender    The sender that ran the comm

if (config.getUseFinerTeleportPermissions()) {
            return hasTeleportPermission(teleporter, scope, destination.getIdentifier(), destination.getFinerPermissionSuffix().getOrNull());
        }
        return hasTeleportPermission(teleporter, scope, destination.getIdentifier(), null);
    }

    /**
     * Checks if the issuer has permission to teleport to at least one destination.
     *
     * @param sender    The sende
```

## Multiverse-Core 5.8.1 权限常量与注册

来源：[https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/permissions/CorePermissions.java](https://github.com/Multiverse/Multiverse-Core/blob/4de4e5a68edb2c7b74dcaa7643ac2575ccc1e9be/src/main/java/org/mvplugins/multiverse/core/permissions/CorePermissions.java)

取得：HTTP 200；2026-10-19T12:58:00.274Z。

```text
static final String JOINLOCATION_BYPASS = "mv.bypass.joinlocation";
    static final String WORLD_ACCESS = "multiverse.access";
    static final String WORLD_EXEMPT = "multiverse.exempt";
    static final String GAMEMODE_BYPASS = "mv.bypass.gamemode";
    static final String PLAYERLIMIT_BYPASS = "mv.bypass.playerlimit";
    static final String TELEPORT = "multiverse.teleport";
    static final String SPAWN = "multiverse.core.spawn";
                    concatPermission(WORLD_ACCESS, world.getName()), PermissionDefault.OP));
            pluginManager.removePermission(concatPermission(WORLD_ACCESS, world.getName()));
```

## Multiverse-Core 官方权限清单

来源：[https://mvplugins.org/core/reference/permissions-list/](https://mvplugins.org/core/reference/permissions-list/)

取得：HTTP 200；2026-10-19T12:48:39.412Z。

```text
All Multiverse-Core Permissions
Help Permissions
 multiverse.help - Allow users to use /mv help
Access Permissions
 multiverse.access.[worldname] - Allows users to use the specified world
 multiverse.exempt.[worldname] - Allows users to be exempted from paying for the world
 mv.bypass.gamemode.[worldname] - Allows users to bypass the configured gamemode when accessing the world
 mv.bypass.playerlimit.[worldname] - Allows users to bypass the configured playerlimit when accessing the world
 mv.bypass.joinlocation - Allows users to bypass the configured join-location in config.yml when logging into the server.
Teleport Permissions
 multiverse.teleport.self.[type].[finer-permission] - Allows users to teleport themselves to another world.
 multiverse.teleport.other.[type].[finer-permission] - Allows users to teleport themselves and others to another world.
 Note: If enforce-access is on (set to true), they can only teleport to worlds of which they have the multiverse.access.WORLD permission to. By default this is false and they have access to ALL worlds.
Teleport types:
 w = World
 p = Portal
 a = Anchor
 e = Exact destination (coordinates)
 pl = Player
 ca = Cannon
 b = Bed
 See Also: Details on Destinations 
Info Permissions
 multiverse.core.check - Allows checking whether a player can teleport to a destination
 multiverse.core.confirm 
 multiverse.core.coord 
 multiverse.core.info 
 multiverse.core.list.who 
 multiverse.core.list.who.all 
 multiverse.core.list.worlds 
 multiverse.core.version - Allows viewing the installed Multiverse version
World Management Permissions
 multiverse.core.create - Allows users to create worlds
 multiverse.core.clone - Allows users to copy worlds
 multiverse.core.import - Allows users to import worlds
 multiverse.core.modify - Allows users to modify worlds
 multiverse.core.regen 
 multiverse.core.remove 
 multiverse.core.load 
 multiverse.core.unload 
 multiverse.core.delete 
Spawn Permissions
 multiverse.core.spawn.other.[worldname] 
 multiverse.core.spawn.self.[worldname] 
 multiverse.core.spawn.set 
Entities Management Permissions
 multiverse.core.entityspawnconfig.info 
 multiverse.core.entityspawnconfig.modify 
 multiverse.core.purge 
 multiverse.core.purgeall 
Anchor Permissions
 multiverse.core.anchor.create 
 multiverse.core.anchor.list 
 multiverse.core.anchor.delete 
World Border Permissions
 multiverse.core.worldborder - Allows using all /mv worldborder sub-commands
Misc Permissions
 multiverse.core.config 
 multiverse.core.dumps - Allows uploading debug info
 multiverse.core.reload - Allows users to reload the config files
```

## Multiverse-Core 配置参考和示例注释

来源：[https://mvplugins.org/core/reference/configuration-file/](https://mvplugins.org/core/reference/configuration-file/)

取得：HTTP 200；2026-10-19T12:48:39.427Z。

```text
Here is the default config that ships with MV. Note the version number at the bottom. We will (try to) update this page with newer configs when they ship.
Make sure you're up to date
 If you type /mv version a version string will be dumped to the console, in it you will see a line:
 ...
XX:XX:XX [INFO] [Multiverse-Core] [Multiverse-Core] Dumping Config Values: (version 2.7)
...
 null
 This is the current version of your config. If it does not match the version in the example below, please grab an updated version of Multiverse-Core and all of the Multiverse Plugins you use .

New options are added to this file automatically. If you manually made changes #
# to this file while your server is running, please run `/mv reload` command. #
```

## Multiverse-Core 世界属性中的重生锚选项

来源：[https://mvplugins.org/core/fundamentals/world-properties/](https://mvplugins.org/core/fundamentals/world-properties/)

取得：HTTP 200；2026-10-19T12:57:11.610Z。

```text
Anchor Respawn 
 Auto-Heal 
 Auto Load 
 Bed Respawn 
 Difficulty
```

