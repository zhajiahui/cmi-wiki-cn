---
title: WorldGuard 插件介绍来源
source_kind: plugin-overview
translation_review: reviewed
---

# WorldGuard 插件介绍来源

核对日期：2026-10-19。介绍对应版本：`7.0.17+2370-e42d8bc`。以下为本次直接读取的官方文档及官方仓库片段；网页仅整理空白和换行，源码摘录可能选自不同位置。

## WorldGuard 7.0.17 发布提交

来源：[https://github.com/EngineHub/WorldGuard/commit/e42d8bcda767c1e57f6ca801d088535a9f0783b3](https://github.com/EngineHub/WorldGuard/commit/e42d8bcda767c1e57f6ca801d088535a9f0783b3)

取得：本轮 GitHub 只读工具直接取得对应提交内容。

```text
sha: e42d8bcda767c1e57f6ca801d088535a9f0783b3
message: Release 7.0.17
author date: 2026-05-30T03:04:28Z
```

## WorldGuard 官方简介

来源：[https://worldguard.enginehub.org/en/latest/](https://worldguard.enginehub.org/en/latest/)

取得：HTTP 200；2026-10-19T12:48:39.380Z。

```text
WorldGuard has a host of functions for server owners, server map makers, regular survival servers, and everyone else in between.
Create zones in your world that only permit mods or certain players from building within
Set additional game rules on your server (deny wither block damage, falling damage, etc.)
Set game rules on specific areas (food regen, health regen, disable PvP, TNT, control mob damage) in your world
Blacklist certain items and blocks so they can’t be used
Dump useful statistics and information about your server (/wg report -p)
CPU profile your server (/wg profile -p)
Add useful commands like an immediate “STOP ALL FIRE SPREAD” command.
```

## WorldGuard 必需平台与 WorldEdit Bukkit 依赖

来源：[https://worldguard.enginehub.org/en/latest/install/](https://worldguard.enginehub.org/en/latest/install/)

取得：HTTP 200；2026-10-19T12:47:01.737Z。

```text
WorldGuard requires a version of the Minecraft server that supports the Bukkit API, which includes Spigot and Paper. The “vanilla” Minecraft server cannot run plugins. Other server implementations, such as Forge or Sponge, are also not supported by WorldGuard.
The other requirement is the WorldEdit Bukkit plugin, a very lightweight in-game map editor, also made by us. Please note that you need the Bukkit version of WorldEdit, not another implementation.
Installation¶
```

## WorldGuard 对应构建 plugin.yml

来源：[https://github.com/EngineHub/WorldGuard/blob/e42d8bcda767c1e57f6ca801d088535a9f0783b3/worldguard-bukkit/src/main/resources/plugin.yml](https://github.com/EngineHub/WorldGuard/blob/e42d8bcda767c1e57f6ca801d088535a9f0783b3/worldguard-bukkit/src/main/resources/plugin.yml)

取得：本轮 GitHub 只读工具直接取得对应提交内容。

```text
name: WorldGuard
main: com.sk89q.worldguard.bukkit.WorldGuardPlugin
version: "${internalVersion}"
depend: [WorldEdit]
api-version: "1.21.11"
folia-supported: true
```

## WorldGuard 区域命令

来源：[https://worldguard.enginehub.org/en/latest/regions/commands/](https://worldguard.enginehub.org/en/latest/regions/commands/)

取得：HTTP 200；2026-10-19T12:47:01.740Z。

```text
Either /region or /rg can be used for commands. Some sub-commands have multiple aliases (for example, /rg d can be used a shortcut to /rg define).
Tip
You can use almost all of these commands from console, but you may need to specify the -w flag (when available).
You can also use the //world command from WorldEdit to set the target world (both from console and in-game).
Creating and Removing Regions¶

/rg define).
Tip
You can use almost all of these commands from console, but you may need to specify the -w flag (when available).
You can also use the //world command from WorldEdit to set the target world (both from console and in-game).
Creating and Removing Regions¶
Define¶
/rg define [-w <world>] [-g] <id> [<owner1>] [<owner2>] [... <ownerN>]
/rg create (...)
/rg def (...)

/rg remove [-w <world>] [-f] [-u] <id>
/rg rem (...)
/rg delete (...)
/rg del (...)
Removes a region.
If the specified region has child regions, then either -u or -f must be specified. Both options cannot be specified together.
-u changes child regions of the specified region to have no parent
-f removes child regions of the specified region

/rg flag <id> <flag> [-w <world>] [-g <group>] [-e] [<value>]
/rg f (...)
Sets a flag on a region (see Region Flags for more information).
To unset a flag, don’t specify a value.
To set a flag to a blank value, use -e. This is useful for setting flags like greeting to a blank message to override the flag set in a different, larger, and lower priority region. If -e is specified in addition to a value, the value is discarded.
-g <group> specifies the region group (see Region Flags)
-e sets an empty value
Example: Setting the pvp flag of “mall” to “deny” with region group “nonmembers”
/rg flag mall pvp -g nonmembers deny
Example: Unsetting the greeting flag on “mall”
/rg flag mall greeting
Example: Setting the greeting flag to an empty value

/rg addmember [-w <world>] <id> <members...>
/rg addmem (...)
/rg am (...)
Adds any number of members to a region. Using g:<member> will add a permission group instead of a player.

/rg addowner [-w <world>] <id> <owners...>
/rg ao (...)
Adds any number of owners to a region. Using g:<owner> will add a permission group instead of a player.
Example: Adding the “admins” group and the player “eduardo” as members of a “spawn” region of the “lobby” world.

/rg info [-u] [-s] [-w <world>] [<id>]
/rg i (...)
Displays information about a specified region, or if no region is specified, the region that you are currently in. If you are in several regions, then a list will shown instead.
-s causes the command to select the region (see /rg select)
-u causes UUIDs to be shown rather than player’s last seen names
Example: Showing information about the Global Region

/rg list [-i <id search>] [-p <player>] [-w <world>] [-s] [<page>]
Lists the regions that have been created. A number can be provided to show a certain page.
If a player doesn’t have permission to list all regions but has permission to list their own (ones the player is a member or owner of), then the command will automatically only list the player’s own regions.
-p <player> can be specified to filter on regions that the given player is a member or owner of
```

## WorldGuard 管理命令

来源：[https://worldguard.enginehub.org/en/latest/commands/](https://worldguard.enginehub.org/en/latest/commands/)

取得：HTTP 200；2026-10-19T12:56:14.289Z。

```text
/wg reload
Reload WorldGuard’s configuration, blacklist, and region data.
/wg running
/wg queue
Show WorldGuard’s running tasks. An example of a running task is a UUID lookup of a player that occurs in the background.
```

## WorldGuard 区域权限和旗标权限分层

来源：[https://worldguard.enginehub.org/en/latest/permissions/](https://worldguard.enginehub.org/en/latest/permissions/)

取得：HTTP 200；2026-10-19T12:47:01.742Z。

```text
worldguard.reload
Be able to use /wg reload.

worldguard.region.define
Be able to use /rg define.
worldguard.region.claim
Be able to use /rg claim.
worldguard.region.unlimited
Bypass claiming limits.
worldguard.region.list
Be able to use /rg list.
worldguard.region.list.own
Be able to use /rg list and have it show one own’s regions.
Per-Region Permissions¶
The following permissions support a base permission (such as worldguard.region.redefine), but also allow you to use specific permissions that only apply if a player is an owner or member of a region (note that an owner is also a member):

worldguard.region.list
Be able to use /rg list.
worldguard.region.list.own
Be able to use /rg list and have it show one own’s regions.
worldguard.region.redefine.*
Be able to use /rg redefine.
worldguard.region.remove.*
Be able to use /rg remove.
worldguard.region.select.*
Be able to use /rg select.
worldguard.region.info.*
Be able to use /rg info and /rg flags.
worldguard.region.addmember.*
Be able to use /rg addmember.
worldguard.region.addowner.*
Be able to use /rg addowner.
worldguard.region.removemember.*
Be able to use /rg removemember.
worldguard.region.removeowner.*
Be able to use /rg removeowner.

The following permissions support a base permission (such as worldguard.region.redefine), but also allow you to use specific permissions that only apply if a player is an owner or member of a region (note that an owner is also a member):
worldguard.region.redefine.own.<region name>
worldguard.region.redefine.member.<region name>
worldguard.region.redefine.<region name>
Permissions systems that support wildcard permissions can be used to grant permissions to all regions in any given category, e.g.:
worldguard.region.redefine.own.*
Permission

worldguard.region.flag.regions.own.<region name>
worldguard.region.flag.regions.member.<region name>
worldguard.region.flag.regions.<region name>
However, to determine which types of flags can be set by the player, permissions of the following patterns can be given:
worldguard.region.flag.flags.<flag name>.<flag value>.own.<region name>
worldguard.region.flag.flags.<flag name>.<flag value>.member.<region name>
worldguard.region.flag.flags.<flag name>.<flag value>.<region name>
Examples for <flag value> are allow, deny, unset (if no value is specified), etc. More complex values are also checked, however, special characters such as ,, ., whitespaces, etc. are omitted.
Example: Letting players be able to only change flags on regions that they own, and limit the flags that they can change to use and chest-access
You would need to provide the following permissions:
worldguard.region.flag.regions.own.*
worldguard.region.flag.flags.use.*
worldguard.region.flag.flags.chest-access.*
Subpages¶
Build Permissions
```

## WorldGuard 全局配置和按世界覆盖

来源：[https://worldguard.enginehub.org/en/latest/config/](https://worldguard.enginehub.org/en/latest/config/)

取得：HTTP 200；2026-10-19T12:47:01.744Z。

```text
Configuration¶
Many of WorldGuard’s features exist as configuration options (potion blocking, scuba mode with pumpkins, etc.). Every configuration option available is listed on this page.
Configuration Files¶
Once you have run your server with WorldGuard installed, you will find the main configuration file inside the plugins/WorldGuard folder:
config.yml
Then for every world, you will find per-world configuration files:
worlds/world/config.yml
worlds/world_nether/config.yml
worlds/mining_world/config.yml
If you open up the per-world configuration files, they will be nearly empty. When you wish to override a setting, you would copy it into the world’s configuration file.
Example: Making a configuration option per-world
In the main configuration file, you may have set block-creeper-block-damage to true:
mobs:
 block-creeper-explosions: false
 block-creeper-block-damage: true
 block-wither-explosions: false
But you want to set it to false in your nether world. Open up worlds/world_nether/config.yml and replace the file with:
mobs:
 block-creeper-block-damage: false
Only the relevant line, as well as any parent sections, needs to be copied over.
Settings¶
Note
```

## WorldGuard 黑名单说明

来源：[https://worldguard.enginehub.org/en/latest/blacklist/](https://worldguard.enginehub.org/en/latest/blacklist/)

取得：HTTP 200；2026-10-19T12:56:14.290Z。

```text
Blacklist¶
The blacklist allows an action (or several) to be performed whenever a player does something (place a block, use an item, etc.). Some example applications include:
Blocking players from mining gold ore
Notifying all administrators when a diamond block is found
Sending the player a message when they place an enchantment table
An example of a blacklist file is:
# Deny lava buckets
[lava_bucket]
ignore-groups=admins,mods
on-use=deny,tell
message=Sorry, you can't use lava buckets!
# Deny some ore
[gold_ore,iron_ore]
ignore-groups=admins
on-break=deny,tell,notify
# No TNT!
```

