**cmi setspawn (playerName) (true/false) (-g:[groupName]) (-rng:[range]) (-w:world,world_nether)**  
使用所需权限：cmi.command.setspawn

设置玩家执行 /cmi spawn 命令时前往的出生点，或死亡后的重生位置。  
设置出生点需要 cmi.command.setspawn 权限。

`cmi setspawn`

(true/false) — 设置 /cmi spawn 命令使用的玩家出生点；设为 true 时，也将其用作玩家死亡后的重生点。本命令也包含上一个示例的作用。

`cmi setspawn true`

(-g:[groupName]) — 为指定权限组设置 /cmi spawn 命令使用的玩家出生点；设为 true 时，也将其用作该组玩家死亡后的重生点。这时需要将以下两个权限赋予对应权限组。  
– cmi.spawngroup.[groupName]  
– cmi.respawngroup.[groupName]（指定死亡后前往的出生点；缺少此权限时，使用主出生点）。

`cmi setspawn true -g:Moderator`

(-rng:[range]) — 根据给定范围随机确定玩家的出生位置。这样可以将玩家分散在一片区域内，避免玩家重叠。本命令也包含上一个示例的作用。

`cmi setspawn true -g:Moderator -rng:5`

(-w:world,world_nether) — 根据玩家所在的世界指定出生点。在此示例中，只有玩家位于 world 或 world_nether 世界时才会使用这个出生点。可以与权限组设置结合使用。

`cmi setspawn true -rng:5 -w:world,world_nether`

## 补充说明与重生

- 自动重生：无需点击死亡界面上的重生按钮。  
  **cmi.autorespawn** 权限允许玩家立即返回出生点。
- 将其他玩家传送到出生点需要 **cmi.command.spawn.others** 权限。
- 可以在配置文件中为出生点启用 BlackListedItems。启用后，如果玩家背包中有黑名单物品，就会阻止其传送；**cmi.teleport.bypassblacklist** 权限可以绕过这项限制。
- 如果指定世界不在 Specific 列表中，可以定义重生位置的优先顺序。
- 可用的重生位置：

`PriorityOrder:`  
`- anchor`  
`- spawn`  
`- bedLocation`  
`- homeLocation`  
`- worldSpawn`

\# **Spawn** 是用 /cmi setspawn 命令预先设置的出生点，该位置的 RespawnLocation 应设为 true。   
\# **bedLocation** 是通过与床交互设置的位置；BedInteraction 应设为 false，玩家需要 cmi.bedhome 权限才能设置床的位置。   
\# **homeLocation** 是玩家设置的、使用默认名称（Home）的家；如果不存在，则在可用的情况下使用列表中的第一个家。   
\# **worldSpawn** 是该世界预设的出生点，属于世界的默认出生点，并非 CMI 设置的位置。   
\# **anchor** 是通过与重生锚交互设置的位置。通常只在下界死亡时使用，其他情况下使用床的位置。   
\# **warp! [warpName]** 可以指定任意有效的传送点，将玩家传送过去，并绕过该传送点的所有使用条件。

可以用 **/cmi setfirstspawn (playerName)** 命令设置玩家首次进入服务器时的出生点。

*记得设置[原版](https://minecraft.fandom.com/wiki/Commands/spawnpoint)出生点；如果使用 Multiverse-Core 之类的世界管理插件，可能还需要执行 /mvsetspawn。*

## 命令、权限与占位符

命令：

```text
> cmi checkcommand spawn
 --------------------------------------------------
/cmi setfirstspawn (playerName)
/cmi spawn (playerName) (-s)
/cmi setspawn (playerName) (true/false) (-g:[groupName]) (-rng:[range]) (-w:world,world_nether) (loc:[world;x;y;z;yaw;pitch])
>
```

权限：

```text
> cmi checkperm spawn
 --------------------------------------------------
cmi.respawngroup.[respawngroup] - Defines player individual respawn point
cmi.spawngroup.[spawngroup] - Defines player individual spawn point
cmi.command.setwarp - Sets warp location
cmi.command.spawn.others - Teleports back to spawn location
cmi.command.spawn - Teleports back to spawn location
cmi.autorespawn - Allows to respawn automatically
cmi.spawnonjoin.bypass - Allows to bypass spawnOnJoin option
cmi.command.setspawn - Sets spawn command teleport point
cmi.command.setfirstspawn - Sets first spawn point
>
```

占位符：

```text
There are no placeholders for this feature.
```
