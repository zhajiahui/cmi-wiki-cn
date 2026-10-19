---
title: Citizens 插件介绍来源
source_kind: plugin-overview
translation_review: reviewed
---

# Citizens 插件介绍来源

核对日期：2026-10-19。介绍对应版本：`2.0.43-SNAPSHOT (build 4210)`。以下为本次直接读取的官方文档及官方仓库片段；网页仅整理空白和换行，源码摘录可能选自不同位置。

## Citizens 官方 Jenkins build 4210

来源：[https://ci.citizensnpcs.co/job/Citizens2/4210/](https://ci.citizensnpcs.co/job/Citizens2/4210/)

取得：HTTP 200；2026-10-19T12:56:14.292Z。

```text
Success #4210 (Jun 20, 2026, 3:31:52 PM)
Started 4 mo 0 days ago
 Took 2 min 48 sec
 Build Artifacts Citizens-2.0.43-b4210.jar 4.16 MiB  view 
 Started by upstream project CitizensAPI build number 1370
originally caused by:
 Started by GitHub push by fullwall
 (2 times)
 Revision: 3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2
Repository: https://github.com/CitizensDev/Citizens2.gitorigin/master
Module Builds
 citizens 3 sec 
 citizens-main 1 min 30 sec 
 citizens-parent 2.4 sec 
 citizens-v1_10_R1 (didn’t run)
```

## Citizens 官方简介

来源：[https://wiki.citizensnpcs.co/Main_Page](https://wiki.citizensnpcs.co/Main_Page)

取得：HTTP 200；2026-10-19T12:47:01.747Z。

```text
Citizens is a Minecraft server plugin that utilizes the Bukkit API. It adds various Non-Player Character (NPC) functionality. Citizens also features an easy-to-use API for plugin developers. 
Downloads: Downloads
```

## Citizens build 4210 的 plugin.yml

来源：[https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/resources/plugin.yml](https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/resources/plugin.yml)

取得：HTTP 200；2026-10-19T12:56:46.149Z。

```text
name: Citizens
authors: [fullwall]
softdepend: [Vault, PlaceholderAPI, WorldGuard, packetevents, Denizen]
loadbefore: [Denizen]
version: ${project.version} (build ${BUILD_NUMBER})
main: net.citizensnpcs.Citizens
website: https://www.citizensnpcs.co
api-version: "1.13"
folia-supported: true
libraries:
  - ch.ethz.globis.phtree:phtree:2.8.2
  - org.joml:joml:1.10.9
  - it.unimi.dsi:fastutil:8.5.16
  - team.unnamed:mocha:3.0.0  
commands:
  trait: 
    description: Trait commands
    permission: citizens.trait.help 
  citizens: 
    description: Administration commands
    permission: citizens.citizens.help
  npc: 
    description: Basic commands for all NPC-related things
    permission: citizens.npc.help
  template:
    aliases: [tpl]
    description: Template commands
    permission: citizens.templates.help
  waypoints:
    aliases: [wp]
    description: Waypoint commands
    permission: citizens.waypoints.help
```

## Citizens 官方安装说明

来源：[https://wiki.citizensnpcs.co/Installation](https://wiki.citizensnpcs.co/Installation)

取得：HTTP 200；2026-10-19T12:48:39.370Z。

```text
Installing Citizens 2.0 is easy. It is like installing any other Bukkit plugin. If you don't know how to do that, see below.
Installing Citizens 2.0
Download Citizens here.
Place the Citizens 2.0 jar in your /plugins directory.
Download any desired Trait plugins and place these in the /plugins directory as well.
Reload or restart your server. Citizens 2 will create a plugins/Citizens folder and a config.yml file.
Configure Citizens to your liking with config.yml. See the Configuration page for more help.
Reload or restart your server.
Start creating and editing NPCs!
Be sure to set Permissions so your players can interact with NPCs.
Note that players need the citizens.npc.talk permission to hear NPCs!
Quick Navigation
Usage
Installation  · Frequently Asked Questions  · Commands  · Editors  · Characters  · API  · 

Last modified on 8 March 2022.
```

## Citizens build 4210 NPC 命令与删除分支

来源：[https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/commands/NPCCommands.java](https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/commands/NPCCommands.java)

取得：HTTP 200；2026-10-19T12:56:46.151Z。

包含方法注解和 remove() 方法内选择性摘录的检查语句，片段并非连续。

```text
@Command(
            aliases = { "npc" },
            usage = "create [name] ((-b(aby),u(nspawned),s(ilent),t(emporary),c(enter),p(acket)) --at [x,y,z,world] --type [type] --item (item) --trait ['trait1, trait2...'] --model [model name] --nameplate [true|false|hover] --temporaryduration [duration] --registry [registry name]",
            desc = "",
            flags = "bustpc",
            modifiers = { "create" },
            min = 2,
            permission = "citizens.npc.create")

@Command(
            aliases = { "npc" },
            usage = "list (page) (-a[ll]) --owner [owner] --type [type] --registry [name] --tag [tag] --filter [filter expression]",
            desc = "",
            flags = "a",
            modifiers = { "list" },
            min = 1,
            max = 2,
            permission = "citizens.npc.list")

@Command(
            aliases = { "npc" },
            usage = "lookclose --range [range] --filter [filter] -r[ealistic looking] --randomlook [true|false] --perplayer [true|false] --randomswitchtargets [true|false] --randompitchrange [min,max] --randomyawrange [min,max] --disablewhennavigating [true|false] --targetnpcs [true|false]",
            desc = "",
            modifiers = { "lookclose", "look" },
            min = 1,
            max = 1,
            flags = "r",
            permission = "citizens.npc.lookclose")

@Command(
            aliases = { "npc" },
            usage = "remove|rem (all|id|name| --owner [owner] | --eid [entity uuid] | --world [world])",
            desc = "",
            modifiers = { "remove", "rem" },
            min = 1,
            max = 2)

@Command(
            aliases = { "npc" },
            usage = "select|sel [id|name] (--range range) (--registry [name])",
            desc = "",
            modifiers = { "select", "sel" },
            min = 1,
            max = 2,
            permission = "citizens.npc.select")

@Command(
            aliases = { "npc" },
            usage = "skin (-e(xport) -c(lear) -l(atest) -s(kull) -b(edrock) -u(rl)) [name] (or --url [url] --file [file] (-s(lim)) or -t [uuid/name] [data] [signature])",
            desc = "",
            modifiers = { "skin" },
            min = 1,
            max = 4,
            flags = "clusbet",
            permission = "citizens.npc.skin")

@Command(
            aliases = { "npc" },
            usage = "tp (-e(xact))",
            desc = "",
            modifiers = { "tp", "teleport" },
            min = 1,
            max = 1,
            flags = "e",
            permission = "citizens.npc.tp")

@Command(
            aliases = { "npc" },
            usage = "tphere (cursor) -c(enter) -f(ront)",
            desc = "",
            flags = "cf",
            modifiers = { "tphere", "tph", "move" },
            min = 1,
            max = 2,
            permission = "citizens.npc.tphere")

                if (!rem.getOrAddTrait(Owner.class).isOwnedBy(sender)) {
                if (uuid != null && rem.getOrAddTrait(Owner.class).isOwnedBy(uuid)
                        || rem.getOrAddTrait(Owner.class).isOwnedBy(owner)) {
                if (loc != null && rem.getOrAddTrait(Owner.class).isOwnedBy(sender) && loc.getWorld() != null
                    && npc.getOrAddTrait(Owner.class).isOwnedBy(sender)) {
                if (!sender.hasPermission("citizens.admin.remove.all") && !sender.hasPermission("citizens.admin"))
                    throw new NoPermissionsException();
                    if (!(sender instanceof ConsoleCommandSender) && !npc1.getOrAddTrait(Owner.class).isOwnedBy(sender))
                        throw new CommandException(CommandMessages.MUST_BE_OWNER);
                    if (!sender.hasPermission("citizens.npc.remove") && !sender.hasPermission("citizens.admin"))
                        throw new NoPermissionsException();
        if (!(sender instanceof ConsoleCommandSender) && !npc.getOrAddTrait(Owner.class).isOwnedBy(sender))
            throw new CommandException(CommandMessages.MUST_BE_OWNER);
        if (!sender.hasPermission("citizens.npc.remove") && !sender.hasPermission("citizens.admin"))
            throw new NoPermissionsException();
```

## Citizens build 4210 管理命令

来源：[https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/commands/AdminCommands.java](https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/commands/AdminCommands.java)

取得：HTTP 200；2026-10-19T12:57:11.611Z。

```text
@Command(aliases = { "citizens" }, desc = "", max = 0, permission = "citizens.admin")

@Command(
            aliases = { "citizens" },
            usage = "reload",
            desc = "",
            modifiers = { "reload", "load" },
            min = 1,
            max = 1,
            permission = "citizens.admin")

@Command(
            aliases = { "citizens" },
            usage = "save",
            desc = "",
            modifiers = { "save" },
            min = 1,
            max = 1,
            permission = "citizens.admin")
```

## Citizens 命令 Wiki

来源：[https://wiki.citizensnpcs.co/Commands](https://wiki.citizensnpcs.co/Commands)

取得：HTTP 200；2026-10-19T12:47:01.752Z。

```text
/citizens reload 
 citizens.admin 
 Reload Citizens

/citizens save 
 citizens.admin 
 Save NPCs and configuration

/npc create 
 [name] ((-b(aby),u(nspawned),s(ilent),t(emporary),c(enter),p(acket)) --at [x,y,z,world] --type [type] --item (item) --trait ['trait1, trait2...'] --model [model name] --nameplate [true|false|hover] --temporaryduration [duration] --registry [registry name] 
 Create a new NPC

/npc list 
 (page) ((-a) --owner (owner) --type (type) --char (char) --registry (name)) 
 List NPCs

/npc lookclose 
 --range [range] --filter [filter] -r[ealistic looking] --randomlook [true|false] --perplayer [true|false] --randomswitchtargets [true|false] --randompitchrange [min,max] --randomyawrange [min,max] --disablewhennavigating [true|false] --targetnpcs [true|false] 
 Toggle whether a NPC will look when a player is near

/npc remove 
 (all|id|name| --owner [owner] | --eid [entity uuid] | --world [world]) 
 Remove a NPC

/npc select 
 [id|name] (--range range) (--registry [name]) 
 Select a NPC with the given ID or name

/npc skin 
 (-e(xport) -c(lear) -l(atest) -s(kull) -b(edrock)) [name] (or --url [url] --file [file] (-s(lim)) or -t [uuid/name] [data] [signature]) 
 Sets an NPC's skin name. Use -l to set the skin to always update to the latest

/npc tp 
 (-e(xact)) 
 Teleport in front of an NPC

/npc tphere 
 (cursor) -c(enter) -f(ront) 
 Teleport a NPC to your location
```

## Citizens build 4210 原生设置注释

来源：[https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/Settings.java](https://github.com/CitizensDev/Citizens2/blob/3ecde1a60c438ef6ebd268cc07de3aa66e61d7c2/main/src/main/java/net/citizensnpcs/Settings.java)

取得：HTTP 200；2026-10-19T12:57:11.613Z。

```text
"The default MOVEMENT distance in blocks where the NPC will move to before considering a path finished<br>Note: this is different from the PATHFINDING distance which is specified by path-distance-margin",
                "npc.pathfinding.default-distance-margin", 1),
                "Default maximum number of NPCs owned by a single player (give the citizens ignore-limits permission to skip this check)",
                "npc.limits.default-limit", 10),
                "Default PATHFINDING distance in blocks where the NPC will consider pathfinding complete<br>Note: this is different from the MOVEMENT distance, which is specified by the distance-margin<br>Set to 0 if you want to try pathfind exactly to the target destination",
                "npc.pathfinding.default-path-distance-margin", 0),
```

## Citizens 配置 Wiki 的距离单位示例

来源：[https://wiki.citizensnpcs.co/Configuration](https://wiki.citizensnpcs.co/Configuration)

取得：HTTP 200；2026-10-19T12:47:01.755Z。

```text
default-distance-margin: 2 # the distance from the goal to stop early while moving along a path measured in blocks squared
 default-path-distance-margin: 1 # the distance from the goal to stop early while finding a path measured in blocks
 update-path-rate: 20 # how often to update the path in ticks, typically for entity targeting
 maximum-new-pathfinder-iterations: 10000 # the maximum number of blocks to search while pathfinding using the new pathfinder
```

