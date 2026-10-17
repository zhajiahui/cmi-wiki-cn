---
title: 指令列表
---

# 指令列表

**可使用 `/cmi checkcommand [keyword]` 按关键词查找相关命令。**

对于大多数命令，玩家在线与否没有区别。

**`[someVariable]`——必填**  
**`(someVariable)`——可选**

部分命令可通过 `?` 查看额外说明，包括所需的额外权限。例如，`/cmi alert ?` 不仅会显示用法，还会解释所需权限。

部分命令提供特殊参数 `-s`，执行后不输出消息，用于静默执行命令。玩家需要 `cmi.command.silent` 权限。

使用任何命令都需要基础权限 `cmi.command`，默认所有人都拥有该权限。

每条命令还需要对应的基础权限 `cmi.command.[commandName]`。例如，`heal` 需要 `cmi.command.heal`，但此权限只允许治疗自己。要对其他玩家执行命令，还需要额外权限，例如 `cmi.command.heal.others`。

在游戏中，将鼠标悬停在错误消息上，即可查看所需权限。

`(time)` 参数可写为：`1s`（1 秒）、`5m`（5 分钟）、`2h`（2 小时）、`3d`（3 天）、`7w`（7 周）、`1M`（1 个月）、`4y`（4 年）。可组合多个时间单位，表示更精确的时长，例如 `5h32m52s`。

命令表已更新至与 **9.2.4.5** 版本一致。随着时间推移，可能会与游戏内显示存在细微差别。

### `actionbarmsg [playerName/all] (-s:[seconds]) [message]` {#actionbarmsg}

向玩家发送操作栏消息。

`-s:[seconds]` 指定消息持续显示的时间。由于其工作方式的限制，如果设置了持续时间，而其他插件在此期间尝试显示新的操作栏消息，本消息可能会覆盖其他插件的消息。

### `afk (-p:playerName) (reason) (-s)` {#afk}

切换暂离（AFK）模式，可填写原因。

### `afkcheck [playerName/all]` {#afkcheck}

检查玩家的暂离状态。

### `air [playerName] [amount] (-s)` {#air}

设置玩家的氧气值。

### `alert [add/list/remove] [playerName] (reason) (-s)` {#alert}

在玩家登录时通知管理员。

权限：`command.alert.info.inform`——查看玩家登录提醒。

### `aliaseditor (new) (alias-cmd)` {#aliaseditor}

为一条或多条命令创建自定义别名。

更多信息见[这里](commands/custom-alias.md)。

### `anvil (playerName) (-s)` {#anvil}

打开铁砧。

### `anvilrepaircost (playerName) [amount]` {#anvilrepaircost}

设置物品的修复费用。

### `armoreffect [potioneffect]` {#armoreffect}

为盔甲附加药水效果，可同时附加多种效果。手持盔甲执行 `/cmi armoreffect`，即可打开游戏内编辑器，移除效果、添加多种效果或管理已有的效果。例如，`speed:3` 会添加 3 级速度效果，默认持续 15 秒，每隔 15 秒刷新一次。

### `armorstand (last/near)` {#armorstand}

打开盔甲架编辑器。

更多信息见[这里](armor-stand-editor.md)。

### `attachcommand [command/-clear]` {#attachcommand}

将一条或多条命令附加到物品上。

更多信息见[这里](commands/attached-commands.md)。

### `autorecharge (playerName) [exp/money/off] (-s)` {#autorecharge}

切换飞行能量自动补充。

### `back (playerName) (-s)` {#back}

传送回上次保存的位置。

### `balance (playerName)` {#balance}

查看余额。

### `baltop (playerName)` {#baltop}

查看财富排行榜。

### `ban [playerName] (reason) (-s)` {#ban}

封禁玩家。

### `banlist (-s)` {#banlist}

查看封禁列表。

### `bbroadcast (!) [message] (-s:[serverName,serverName])` {#bbroadcast}

向所有服务器的所有玩家发送特殊消息。

### `blockcycling` {#blockcycling}

循环切换方块状态。

### `blockinfo` {#blockinfo}

查看方块信息。

### `blocknbt` {#blocknbt}

显示方块的 NBT 信息。

### `book [Author/Title/Unlock] [value]` {#book}

编辑书籍。

### `bossbarmsg [playerName/all] (-sec:[seconds])(-t:[timeToKeepFor]) (-n:nameOfBar) (-p:[maxValue/current]) (-c:[color]) (-s:[1,6,10,12,20]) (-cmd:"command;;command2") (-pcmd:"command;;command2") (-a:[ticks]) [message] (-cancel:nameOfBar)` {#bossbarmsg}

向玩家发送 Boss 血条消息。

更多信息见[这里](commands/bossbarmsg-handling.md)。

### `broadcast (!) [message] (-w:[worldName,worldName]) (-r:[range]) (-c:[world;x;y;z])` {#broadcast}

向所有玩家发送特殊消息。

如果消息以 `!` 开头，就只显示消息内容，不带广播前缀。

可指定世界，仅在这些世界中广播消息。

### `burn (playerName) (time) (-s)` {#burn}

使玩家着火。

### `cartographytable (playerName) (-s)` {#cartographytable}

打开制图台。

### `charges [playerName] [add/set/take/clear/reset] (-f)` {#charges}

显示剩余的刷怪笼使用次数。

### `chat [create/join/leave/list/invite/kick/listrooms] (chatName/playerName) (-private) (-locked) (-persistent)` {#chat}

创建或加入聊天室。

`-locked` 禁止玩家离开聊天室。

`-private` 将聊天室设为仅限受聊天室创建者邀请的玩家加入。

`-persistent` 创建在服务器重启后仍会保留的聊天室。

### `chatcolor (playerName)` {#chatcolor}

选择聊天颜色。

### `checkaccount (playerName/ip)` {#checkaccount}

通过玩家名或 IP 地址查找玩家的其他账号。

### `checkban (playerName)` {#checkban}

检查玩家的封禁状态。

### `checkcommand (keyWord)` {#checkcommand}

根据关键词搜索相关命令。

### `checkexp (playerName)` {#checkexp}

查看玩家的经验情况。

### `checkperm (keyWord)` {#checkperm}

根据关键词搜索相关权限。

### `cheque (playerName) [amount]` {#cheque}

将金钱转换为支票，支票是实际物品。默认需要用纸来创建。右键点击该物品会从玩家账户中扣款。

### `clear (playerName) (item(:amount)(;data)) (-s) (+clearType)` {#clear}

清空玩家背包。

清理类型：

- `+quickbar`
- `+inventory`
- `+partinventory`
- `+weapons`
- `+armorslots`
- `+tools`
- `+armors`
- `+mainhand`
- `+offhand`

### `clearchat (self) (-s)` {#clearchat}

清除聊天记录。

权限：`cmi.command.clearchat.bypass`——不受聊天记录清理影响。

使用 `self` 参数时，只清除自己的聊天记录。

### `clearender [playerName] (-s)` {#clearender}

清空玩家的末影箱。

### `colorlimits (playerName)` {#colorlimits}

显示所有可用颜色。

### `colorpicker (hex/colorname)` {#colorpicker}

选择十六进制颜色。

### `colors (playerName)` {#colors}

显示所有可用颜色。

### `compass (targetName) (sourceName) (x) (z) (worldname) (reset) (-s)` {#compass}

将玩家的指南针指向你的位置。

示例：

```
/cmi compass Zhax
/cmi compass Zrips Zhax
/cmi compass LT_Craft 0 0 Zrips -s
/cmi compass reset Zrips
```

### `condense (itemName) (playerName) (-s)` {#condense}

将物品压缩成方块。

### `counter [join/leave/start] (t:time) (r:[range/-1]) (c:[world:x:y:z]) (msg:custom_message) (-f)` {#counter}

为周围的玩家启动计时器。

权限：

- `cmi.command.counter.force`——强制范围内的所有玩家参与计时。
- `cmi.command.counter.time`——自定义计时时长。
- `cmi.command.counter.range`——自定义范围。
- `cmi.command.counter.msg`——自定义消息。
- `cmi.command.counter.autojoin`——自动参与计时。

`-f` 强制范围内的所有玩家参与计时。

示例：

```
/cmi counter start r:30 t:7 msg:&eCustom_message -f
```

### `cplaytime (playerName)` {#cplaytime}

以 GUI 形式显示详细的游玩时间。

此命令与 `playtime` 命令相互独立，采用不同的方式记录时间，因此显示的游玩时间可能略有不同。

### `ctellraw [playerName/all] [formattedMessage]` {#ctellraw}

发送 tellraw 类型的消息。

### `ctext [cText] (playerName/all) (sourcePlayer)` {#ctext}

显示自定义文本。

更多信息见[这里](custom-text.md)。

### `cuff [playername] (true/false) (-s)` {#cuff}

限制玩家的行动。

### `customrecipe` {#customrecipe}

管理物品的自定义配方。

配方只按原料的材质类型匹配，会忽略物品名称、描述、附魔等额外数据。这是原版的行为。

### `database [action] (playerName) (dataType) (fileName)` {#database}

管理备份数据。

### `dback (playerName) (-s)` {#dback}

返回死亡位置。

### `dialogs [dialogName] (playerName) ([variableName]:value) (-s)` {#dialogs}

显示指定的对话框。

对话框的用法见[这里](commands/dialogs.md)。

### `disableenchant [enchant/id] (disable/enable)` {#disableenchant}

禁用附魔。

### `dispose (playerName)` {#dispose}

通过 GUI 丢弃不需要的物品。

### `distance (playerName) (playerName)` {#distance}

查看两点之间的距离。

### `donate [playerName] (amount)` {#donate}

将手持物品捐赠给玩家。

### `down [playerName] (-s) (max)` {#down}

向下传送一层。

使用 `max` 参数时，会尝试寻找最低的位置，而不是只向下传送一层。

### `dsign (new [name])` {#dsign}

管理动态告示牌。

更多信息见[这里](dynamic-signs.md)。

### `dye (playerName) (red,green,blue/hexCode/colorName/random/clear/rainbow/day/biome/health) (-s)` {#dye}

为皮革盔甲染色。

部分颜色是动态的，会根据特定条件更新。

### `editctext` {#editctext}

打开自定义文本编辑器。

更多信息见[这里](custom-text.md)。

### `editlocale (keyword(-s))` {#editlocale}

编辑语言文件。

某些内容可能过长，无法在聊天文本编辑器中显示，因此也无法通过此命令编辑。

### `editplaytime (playerName) [add/take/set] [amount] (-s)` {#editplaytime}

编辑玩家的游玩时间。

### `editwarnings (playerName/clearall) (clear)` {#editwarnings}

编辑玩家的警告记录。

### `editwarp (warpName) (newName)` {#editwarp}

编辑传送点。

### `effect [playername/all] [effect/clear] (duration) (multiplier) (-s) (-visual)` {#effect}

为玩家添加药水效果。使用 `clear` 移除所有效果。

`-visual` 会显示药水气泡和右上角的效果图标。

示例：

- `/cmi effect zrips nightvision 60 1`——给予 Zrips 60 秒夜视效果。
- `/cmi effect zrips nightvision +10`——为当前夜视效果增加 10 秒。
- `/cmi effect zrips nightvision -10`——从当前夜视效果中扣除 10 秒。
- `/cmi effect all health_boost 60 1`——为所有在线玩家增加 1 点生命值。

### `enchant (playerName) [enchant] [level] (-o) (-onlyvalid) (-keeponlyvalid) (-inform) (-s) (-i:[itemName(:data)]) (clear)` {#enchant}

为物品附魔。

`-o` 使用副手物品。

`-onlyvalid` 检查物品是否适用该附魔，在控制台执行时很有用。

`-inform` 通知被附魔物品的持有者，在控制台执行时很有用。

`-s` 对命令执行者静默执行。

`-i:[itemName:data]` 将附魔对象限定为指定物品。

`-keeponlyvalid` 移除物品上所有不适用于该物品的附魔。

### `ender (playerName) (playerName)` {#ender}

打开玩家的末影箱。

### `endgateway` {#endgateway}

开启或关闭末地折跃门方块的光束。

### `entityinfo` {#entityinfo}

查看实体信息。

### `entitynbt (-console)` {#entitynbt}

查看实体的 NBT 信息。

### `exp [playerName] [add/set/take/clear] [amount][%rand/10-20%][1%[min-max][[playerName]] (-s)` {#exp}

设置玩家的经验值。使用 `L` 设置经验等级。

示例：

```
/exp 10
/exp add 10
/exp set 10L
/exp take 10
/exp Zrips clear
/exp Zrips add 10
```

额外的动态参数示例：

`/exp add %rand/10-20%` 给予 10 到 20 之间的随机经验值。

`/exp take 5%[15-100][Zrips]` 按玩家当前经验值的 `5%` 扣除经验，并将扣除量限制在 `15` 到 `100` 之间。这里的 Zrips 是用于计算的参照玩家，不是被扣除经验的玩家。玩家名必须放在方括号中。未指定参照玩家时，使用目标玩家作为参照。

### `ext (playerName) (-s)` {#ext}

为玩家灭火。

### `falldistance (playerName) (number) (-s)` {#falldistance}

设置玩家的下落距离。

### `feed (playerName/all) (-s)` {#feed}

喂饱玩家。

### `findbiome (biomeName/stop/stopall)` {#findbiome}

按名称查找最近的生物群系。

### `fixchunk w [worldName] r [range in chunks] c [x:z]` {#fixchunk}

仅适用于 1.15 及更早版本的服务器。

扫描损坏的区块。

子命令：

- `stats`——显示当前扫描统计。
- `pause`——暂停扫描。
- `continue`——继续扫描。
- `stop`——停止扫描。
- `stopall`——停止当前正在进行的所有区块修复。
- `speed [amount]`——设置当前扫描速度。
- `autospeed [true/false]`——开启或关闭自动速度。
- `messages [true/false]`——开启或关闭消息输出。

示例：

```
/fixchunk w LT_Craft
/fixchunk w LT_Craft r 50 c 1024:-2048
/fixchunk w LT_Craft r g
/fixchunk fix
```

### `flightcharge (add/take/set/show/expcharge/moneycharge/recharge) (playerName) (amount) (-s))` {#flightcharge}

管理和查看飞行能量。

更多信息见[这里](extra/flight-charge.md)。

### `fly [playerName] (true/false) (-s)` {#fly}

开启或关闭玩家的飞行模式。

### `flyc (playerName) (true/false) (-s)` {#flyc}

切换飞行能量模式。

### `flyspeed (playerName) [amount] (-s)` {#flyspeed}

设置玩家的飞行速度，范围为 0 到 10。

### `gamerule (world) (gamerule) (value)` {#gamerule}

通过 GUI 管理游戏规则，或直接修改规则。

### `generateworth` {#generateworth}

自动生成可能的物品价值。

### `getbook [cTextName] (playerName)` {#getbook}

获取自定义文本（ctext）功能中的书籍。

### `give (playerName) [itemdata/hand] (playerName) (-slot:[number]) (unstack) (-s)` {#give}

给予玩家物品。

`-slot:[number]` 会尝试将物品放入指定槽位；若放置失败，则放入玩家背包中任意可用的空槽位。

更多信息见[这里](commands/icwol.md)。

### `giveall [itemname] (amount) (e|l|n|offline)` {#giveall}

给予所有玩家物品。

- 指定物品名称，或带数据值的物品 ID。
- 可选填给予的数量。
- `n`——指定物品名称。
- `l`——指定物品描述。
- `e`——指定物品附魔。
- `-s`——不显示反馈消息。
- `h`——后接玩家名，将该玩家手中的物品给予其他玩家。
- `inv`——后接玩家名，将该玩家背包中的所有物品给予其他玩家。
- `offline`——包含离线玩家。

```
cmi giveall stone 1 n &2Uber_stone l &3Stone_lore offline
cmi giveall h Zrips
cmi giveall inv Zrips
```

### `glow (playerName) [true/false/color/gui]` {#glow}

设置玩家的发光模式。

示例：`/glow Zrips red`

权限：`cmi.command.glow.[color]`——允许设置指定的发光颜色。

### `gm (playerName) [gamemode]` {#gm}

设置玩家的游戏模式。

### `god (playerName) (true/false) (-s)` {#god}

开启或关闭玩家的上帝模式。

### `grindstone (playerName) (-s)` {#grindstone}

打开砂轮。

### `groundclean (+cb) (+cm) (+ci) (+b) (+sh) (+tnt) (+all) (+fl) (+named) (-w:[worldName]) (-s)` {#groundclean}

清理服务器中不需要的物品。

- `+cm`——清理时包含矿车。
- `+cb`——清理时包含船。
- `+ci`——指定是否包含武器和盔甲。
- `+b`——向所有玩家广播清理消息。
- `+tnt`——移除已点燃的 TNT。
- `+sh`——包含潜影盒物品。掉落的潜影盒中可能装有你不想清除的物品，请留意。

### `haspermission (playerName) [permissionNode]` {#haspermission}

检查玩家是否拥有指定权限。

### `hat (playerName)` {#hat}

将物品戴在头上。

### `head [sourceName] (targetName) (-s) (amount)` {#head}

获取玩家的头颅。

### `heal [playerName/all] (healamount/healpercent) (-nofeed) (-ignoreffects) (-dontextinguish)` {#heal}

治疗玩家。

示例：

```
/cmi heal zrips
/cmi heal zrips 10
/cmi heal zrips 10%
/cmi heal all
```

### `helpop [message]` {#helpop}

向管理人员发送求助消息。

需要 `cmi.command.helpop.inform` 权限才能查看消息。

### `hideflags (playerName) [flagName/clear] (flagName)` {#hideflags}

隐藏物品的标记。

### `hologram (new [name])/addline/deleteline/editline/info/update` {#hologram}

创建或管理全息图。

更多信息见[这里](holograms.md)。

- `addline [hologramName] [text]`——直接在全息图末尾添加指定的新行。
- `deleteline [hologramName] [lineNumber]`——删除指定行。
- `editline [hologramName] [lineNumber] [text]`——用新文本修改指定行。
- `update [hologramName]`——强制更新全息图。可用于修改后未正确更新的情况，也可在未启用自动更新计时器时手动强制更新。
- `info [hologramName]`——显示指定全息图的信息。

### `hologrampages [holoName] (playerName) (next/prev/[pageNumber])` {#hologrampages}

切换全息图页面。

此命令与全息图功能相关，用法见[这里](holograms.md)。

### `home (homeName) (playerName) (whoTeleport)` {#home}

传送到家的位置。

### `homes (playerName/near:[range])` {#homes}

显示家的列表，点击即可传送。

### `hunger [playerName] [amount] (-s)` {#hunger}

设置玩家的饥饿值。

### `ic (new [name])` {#ic}

创建交互式命令。

更多信息见[这里](commands/interactive-commands.md)。

### `ifoffline [playerName] (command)` {#ifoffline}

仅在玩家离线时执行命令。

### `ifonline [playerName] (command)` {#ifonline}

仅在玩家在线时执行命令。

### `ignore (playerName/uuid/all) (-p:[playerName])` {#ignore}

忽略玩家。

`cmi.command.ignore.bypass`——绕过忽略列表。

### `importfrom [essentials/hd] [home/warp/nick/logoutlocation/money/mail]` {#importfrom}

从 Essentials、HolographicDisplays 等其他插件导入数据。

### `importoldusers` {#importoldusers}

从主世界文件夹中的 `playerdata` 文件夹导入用户。导入过程中，服务器可能出现短暂卡顿。

### `info (playerName/uuid)` {#info}

显示玩家信息。

查看玩家的 IP 地址需要 `cmi.command.info.ip` 权限。查看玩家所在国家需要将[此文件](https://www.zrips.net/wp-content/uploads/2019/02/GeoIP.dat)放在 CMI 文件夹中。

### `inv [playerName]` {#inv}

打开玩家背包。

权限：

- `cmi.command.inv.preventmodify`——禁止编辑背包。
- `cmi.invedit`——允许编辑背包。
- `cmi.command.inv.location`——显示玩家的位置。

### `invcheck (playerName) [id] (-e) (last)` {#invcheck}

以预览模式打开已保存的背包。

`-e` 以编辑模式打开背包，需要 `cmi.command.invcheck.edit` 权限才会生效。

`last` 打开最近保存的背包。

### `invlist (playerName)` {#invlist}

显示已保存的背包列表。

### `invload (sourceName) (targetName) [id/last]` {#invload}

加载已保存的背包。

`last` 加载最近保存的背包。

### `invremove (playerName) [id/all/last]` {#invremove}

移除玩家已保存的背包。

`all` 移除该玩家保存的所有背包。

`last` 移除最近保存的背包。

### `invremoveall [confirmed]` {#invremoveall}

移除所有已保存的背包。

必须填写 `confirmed` 参数，以防误删已保存的背包。

### `invsave (playerName) (id) (-s)` {#invsave}

保存背包。

### `ipban [ip/playerName] (reason) (-s)` {#ipban}

封禁玩家的 IP 地址。

`cmi.command.banip.bypass`——绕过封禁。

### `ipbanlist` {#ipbanlist}

显示完整的 IP 封禁列表，以及可能使用这些 IP 的玩家名。

### `item [itemname] (amount)` {#item}

给予自己物品。

### `itemcmdata [set/delete] (playerName) (id) (-s)` {#itemcmdata}

查看或修改物品的自定义模型数据。

### `itemframe (invisible/fixed/invulnerable/all)` {#itemframe}

管理物品展示框。

### `iteminfo (playerName)` {#iteminfo}

显示物品信息。

### `itemlore (-p:[playerName]) [linenumber/*] [remove/insert/ new lore line]` {#itemlore}

修改物品描述。

### `itemname (-p:[playerName]) [remove/your new item name]` {#itemname}

重命名物品。

### `itemnbt (playerName)` {#itemnbt}

显示物品的 NBT 信息。

### `jail [playerName] (time) (jailName) (cellId) (-s) (r:jail_reasson)` {#jail}

将玩家关入监狱一段时间。

更多信息见[这里](jail.md)。

### `jailedit` {#jailedit}

编辑监狱。

更多信息见[这里](jail.md)。

### `jaillist (jailName) (cellId)` {#jaillist}

列出所有监狱及其中被关押的玩家。

### `jump` {#jump}

跳到目标方块。

`cmi.command.jump.[amount]` 权限指定此命令允许的最大跳跃距离。

### `kick [playerName/all] (message) (-s)` {#kick}

将玩家踢出服务器，并显示自定义消息。

`cmi.command.kick.bypass`——防止被踢出。

### `kill [playerName] (-force) (damageCause) (-s) (-lightning)` {#kill}

击杀玩家。

### `killall (-monsters/-pets/-npc/-animals/-ambient/-named/-f/-lightning/-list/-m:[mobType]) (-r:range) (-s) (-w:[worldName])` {#killall}

击杀周围的生物。

更多信息见[这里](commands/kill-all.md)。

### `kit [kitName] (playerName) (-s) (-open) (-preview) (-c)` {#kit}

给予预设套装。

权限：

- `cmi.kit.[kitName]`——允许使用指定套装。
- `cmi.kit.bypass.money`——绕过金钱要求。
- `cmi.kit.bypass.exp`——绕过经验要求。
- `cmi.kit.bypass.onetimeuse`——绕过仅限使用一次的限制。

`/cmi kit [kitName] [playerName]` 将套装给予另一名玩家。

`-preview` 打开预览界面，玩家可以查看套装内的物品，但无法取出。使用 `/kitpreview` 命令也可实现此功能。

`-open` 打开包含套装物品的界面，玩家可以选择取出哪些物品。关闭界面后，上方物品栏中剩余的物品会被永久删除。使用 `/kitopen` 命令也可实现此功能。

更多信息见[这里](kits.md)。

### `kitcdreset (kitName) (playerName/all)` {#kitcdreset}

重置套装计时器。

### `kiteditor` {#kiteditor}

开始编辑套装。

更多信息见[这里](kits.md)。

### `kitusagereset (kitName) (playerName)` {#kitusagereset}

重置套装使用次数。

### `lastonline (-p:[page])` {#lastonline}

显示最近 x 分钟内上线过的玩家。

### `launch (playerName) (p:[power]) (a:[angle]) (d:[direction]) (loc:[x]:[y]:[z]) (-nodamage)` {#launch}

沿视线方向或按指定角度将玩家弹射出去。

`-nodamage` 表示被弹射的玩家落地时不受摔落伤害。

- `cmi launch`——沿视线方向弹射。
- `cmi launch p:3.2`——以 3.2 的力度弹射。
- `cmi launch p:2.5 a:25`——沿视线方向，以 25 度角、2.5 的力度弹射。
- `cmi launch Zrips d:east`——向东弹射，角度与视线相同。
- `cmi launch Zrips d:0`——向 0 度方向（南方）弹射，角度与视线相同。
- `cmi launch d:45 a:30 p:2`——向西南方向，以 30 度角、2 的力度弹射。
- `cmi launch loc:150:120:123`——将玩家弹射至目标位置。这只是尝试将玩家弹射到该位置，仍有一些限制。

### `lfix (range) (playerName) (stop/stopall)` {#lfix}

仅适用于 1.13 及更早版本的服务器。

修复周围区块的光照。

### `list` {#list}

显示在线玩家列表。

权限：

- `cmi.command.list.admin`——将玩家列入管理员组。
- `cmi.command.list.staff`——将玩家列入管理人员组。
- `cmi.command.list.hidden`——显示隐藏的玩家。
- `cmi.command.list.group[number]`——按编号将玩家列入预设组。

### `lockip (playername) [add/remove/list/clear] [ip]` {#lockip}

禁止从其他 IP 地址登录账号。

### `loom (playerName)` {#loom}

打开织布机。

### `mail [send/clear/read/sendtemp] [playerName] (time) (message)` {#mail}

发送和接收邮件。

`/cmi mail sendtemp Zrips 24h Quick reminder to vote!` 会发送一封 24 小时后过期的邮件。

### `mailall [send/clear/remove] [message]` {#mailall}

查看邮件，或向所有玩家发送邮件。

### `maintenance (true/false) (message)` {#maintenance}

设置服务器的维护模式。

`cmi.command.maintenance.bypass`——绕过维护模式。

### `maxhp [set/add/take/clear] [playerName] [amount] (-s)` {#maxhp}

设置玩家的最大生命值。

### `maxplayers [amount]` {#maxplayers}

修改服务器允许连接的最大玩家数。

权限：

`cmi.fullserver.bypass`——在服务器已满时加入。

### `me [message]` {#me}

向所有玩家发送特殊消息。

### `merchant [type] (playerName) (level)` {#merchant}

打开商人交易窗口。

### `migratedatabase` {#migratedatabase}

更换数据库系统并迁移所有数据。

### `mirror (start/stop)` {#mirror}

开始镜像放置或破坏方块。

### `mobhead [mobType] (entryNumber) (playerName) (-s)` {#mobhead}

获取生物头颅。

### `money [pay/give/take/set] [playerName/all/alloffline/allonline] [amount][%rand/1-1000%][1%[min-max]][playerName]] (-s)` {#money}

管理余额。

示例：

- `/cmi money give Zrips 100`——给予 Zrips 100 金钱。
- `/cmi money give Zrips %rand/1-1000%`——给予 Zrips 1 到 1000 之间的随机金额。
- `/cmi money take Zrips 1%`——从 Zrips 的余额中扣除其余额的 1%。
- `/cmi money take Zrips 1%[100-500]`——从 Zrips 的余额中扣除其余额的 1%，但扣除金额不少于 100，且不超过 500。
- `/cmi money take Zrips 1%[100-500][Zhax]`——从 Zrips 的余额中扣除 Zhax 余额的 1%，但扣除金额不少于 100，且不超过 500。
- `/cmi money give all 1000`——给予所有在线玩家 1000 金钱。
- `/cmi money give alloffline 1000`——给予所有玩家 1000 金钱，包括离线玩家。

### `more (playerName) (-clone/[amount])` {#more}

将物品堆叠补充到最大数量。

权限：

`cmi.command.more.oversize`——获得超出堆叠上限的物品堆叠。

### `msg [playerName] [message]` {#msg}

向玩家发送消息。

消息以 `!` 开头时，只显示消息内容，不显示发送者姓名。需要 `cmi.command.msg.clean` 权限。

消息以 `!-` 开头时，只显示消息内容，不显示发送者姓名，也不提供回复选项。需要 `cmi.command.msg.noreply` 权限。

### `mute [playerName] (time) (-s) (reason)` {#mute}

禁言玩家。

示例：

```
/cmi mute zrips 1m
/cmi mute zrips 1h
/cmi mute zrips 1h For swearing
```

时间值前可加 `+` 或 `–`，用于增加或减少现有的禁言时间。默认情况下，指定的时间就是此次禁言时长；加上这些符号后，则会在当前剩余禁言时间的基础上增加或减少。

```
/cmi mute zrips +30s
/cmi mute zrips -15m
```

### `mutechat (time) (-s) (reason)` {#mutechat}

禁止发送公共聊天消息。

示例：

```
/cmi mutechat 1m
/cmi mutechat 1h
```

### `nameplate (playerName) (-pref:[some_prefix]) (-suf:[some_suffix]) (-c:[colorCode]) (reset) (-s)` {#nameplate}

设置玩家名牌的前缀、后缀或颜色。发光效果会暂时覆盖玩家名字的颜色。

使用下划线 `_` 表示空格；占位符中的下划线要写成两个下划线 `__`。例如，要显示“hi bob”，输入 `/cmi nameplate -pref:hi_bob`；要显示占位符，输入 `/cmi nameplate -pref:%some__placeholder%`。

### `near (distance)` {#near}

查看附近有哪些玩家。

默认最大距离为 200，可通过 `cmi.command.near.max.[amount]` 权限增加。

### `nick [newNickName/off] (playerName) (-s)` {#nick}

更改玩家的名字。

更改为不同的昵称：`cmi.command.nick.different`。这允许只更改名字的颜色，而不改变名字本身。

使用 `cmi.command.nick.bypass.length` 绕过长度限制。

### `notarget (playerName) (true/false) (-s)` {#notarget}

切换不被生物锁定为目标的模式。

### `note (playerName) [add/remove/clear/list] (id/note)` {#note}

管理玩家备注。

### `openbook (cText) (playerName) (fileName.txt)` {#openbook}

打开书籍 GUI。

可选填要加载并显示的具体文件。与使用已解析的 ctext 文件相比，这种方式的效率较低，但可以显示未直接加载到内存中的自定义文本。

### `oplist` {#oplist}

查看拥有 OP 权限的玩家列表。

### `options (playerName) (option) (enable/disable/toggle/status) (-s)` {#options}

修改个人设置。

各项命令可单独使用。不带参数时，会打开 GUI，供玩家开启或关闭特定功能。

从 CMI 9.1.4.x 起，以下旧命令已整合到新的 `/options` 命令中：`togglecompass`、`toggleshiftedit`、`toggletotem`、`tagtoggle`、`socialspy`、`commandspy`、`signspy`、`msgtoggle`、`tptoggle`、`paytoggle`。

可在 `config.yml` 中进一步配置 `/options` 的 GUI 面板。

修改特定选项所需的权限为 `cmi.command.options.[visibleholograms/shiftsignedit/totembossbar/bassbarcompass/tagsound/chatspy/cmdspy/signspy/acceptingpm/acceptingtpa/acceptingmoney/chatbubble]`。玩家还需要基础命令权限 `cmi.command.options`。

占位符也作了整合：

`%cmi_user_toggle_[msg|pay|tp|compass|sospy|sispy|cospy|schest|autoflightrecharge|totem|shiftedit|tagsound]%`

`%cmi_user_togglename_[msg|pay|tp|compass|sospy|sispy|cospy|schest|autoflightrecharge|totem|shiftedit|tagsound]%`

### `panimation (variable/playerName/stopAll) (stop)` {#panimation}

显示粒子动画。更多信息见 [Wiki 页面](extra/particles.md)。

### `particlepicker (particleName)` {#particlepicker}

打开粒子选择界面。

### `patrol` {#patrol}

传送到随机玩家身边。在访问过所有玩家之前，不会重复传送到同一名玩家。

### `pay [playerName] [amount] (-s)` {#pay}

转账。

### `ping (playerName/message)` {#ping}

显示玩家的延迟。

### `placeholders (parse) (placeholder) (playerName)` {#placeholders}

列出所有占位符。

可解析占位符，查看其返回值，以及由哪个插件解析。

### `playercollision (playerName) [true/false] (-s)` {#playercollision}

设置玩家的碰撞模式。

仅适用于 1.9 及以上版本的服务器。

### `playtime (playerName)` {#playtime}

显示玩家的总游玩时间。

### `playtimetop  (page)` {#playtimetop}

显示玩家总游玩时间排行榜。

### `point (particleName) (playerName) (-self) (time) (-s:[speed])` {#point}

指向方块，绘制一条通往目标方块的粒子线。

### `portals (new/nearest/forceupdate/setlocation/enabled) (portalName) (world:x:y:z:yaw:pitch)` {#portals}

管理传送门。

更多信息见[这里](portals.md)。

### `pos (playerName)` {#pos}

显示玩家的当前位置。

### `preview [range] (innerrange)` {#preview}

适用于 1.17 及更早版本的服务器。

加载指定范围内的区块。

### `prewards (playerName)` {#prewards}

查看游玩时间奖励。

### `ptime (freeze/unfreeze/day/night/dusk/morning/realtime/reset) (playerName) (-s)` {#ptime}

控制玩家的个人时间。

示例：

```
/ptime 13:00:00
/ptime 1pm
/ptime 13
/ptime 7000ticks
/ptime Zrips 1pm
/ptime freeze
/ptime unfreeze
/ptime realtime
/ptime reset
```

### `purge (stop)` {#purge}

根据未上线天数清理世界文件夹中的玩家数据。此命令仅可从控制台执行。

### `pweather (playerName) [sun/rain/reset] (-s)` {#pweather}

控制玩家的个人天气。

### `rankdown (playerName) (rankName) (confirm) (-cmd) (-cost)` {#rankdown}

降低等级。

### `rankinfo (playerName) (rankName)` {#rankinfo}

查看自己的等级信息。

### `ranklist` {#ranklist}

列出可用等级。

### `rankset (playerName) [rankName] (-cmd) (-cost)` {#rankset}

设置玩家的等级。

`-cmd` 执行该等级升级时定义的命令。

`-cost` 扣除该等级升级所需的金钱、经验或物品，前提是配置了这些要求。

即使玩家没有足够的金钱、经验或所需物品，仍会获得该等级。

### `rankup (playerName) (rankName) (confirm)` {#rankup}

提升等级。

### `realname (playerName/nickName)` {#realname}

查看玩家的真实名字。

### `recipe (itemName) (-c)` {#recipe}

查看物品配方。

使用 `-c` 参数时，只显示由 CMI 创建的自定义配方。

### `reload` {#reload}

重载插件配置和语言文件。

### `removehome (homeName) (playerName)` {#removehome}

删除家。

### `removeuser [uuid/duplicates]` {#removeuser}

删除用户及其数据。

### `removewarp (warpName)` {#removewarp}

删除传送点。

### `repair [hand/offhand/armor/all] (playerName)` {#repair}

修复物品。

- `cmi.command.repair.hand`——允许修复主手物品。
- `cmi.command.repair.offhand`——允许修复副手物品。
- `cmi.command.repair.armor`——允许修复盔甲栏中的物品。
- `cmi.command.repair.all`——允许修复整个背包中的物品。
- `cmi.command.repair.repairshare.bypass`——允许在修复物品时不添加修复共享保护。

### `repaircost (hand/armor/all) (playerName)` {#repaircost}

设置物品的修复费用。

示例：

```
/repaircost 10
/repaircost set 10
/repaircost add 10
/repaircost take 10
/repaircost Zrips clear
/repaircost Zrips add 10
```

### `replaceblock id [blockName:data/id:data] w [blockName:data/id:data] r [range in chunks/g] y [max height]` {#replaceblock}

替换当前世界中周围的方块。

子命令：

- `pause`——暂停替换。
- `continue`——继续替换。
- `stop`——停止替换。
- `speed [amount]`——设置当前替换速度。
- `autospeed [true/false]`——开启或关闭自动速度。
- `messages [true/false]`——开启或关闭消息输出。

示例：

```
/cmi replaceblock id 52 w stone r 10
/cmi replaceblock id 52,gold_block w stone r 15 y 100
/cmi replaceblock id 52 w air r g y 100
/cmi replaceblock id iron_ore%75 w stone%90,dirt%5 r g
```

### `reply [message]` {#reply}

回复上一条消息的发送者。

### `resetback (playerName) (reason) (-death) (-s)` {#resetback}

重置玩家的返回位置。

### `resetdbfields [collumnName] (-w:[worldName]) (-p:[playerName])` {#resetdbfields}

将指定数据库列重置为默认值。

### `ride` {#ride}

骑乘目标实体。

`cmi.command.ride.[entityType]`——允许骑乘对应实体。

### `rt (playerName) (worldName) (-s)` {#rt}

传送到随机位置。

### `sameip` {#sameip}

列出从同一 IP 地址登录的玩家。

### `saturation (playerName) [amount]` {#saturation}

设置玩家的饱和度。

### `saveall (daysRange/-online)` {#saveall}

保存所有玩家的背包。

使用 `-online` 参数可仅保存在线玩家的背包。

### `saveditems [save/get/remove/list] (savedItemName) (-t:playerName) (-a:amount) (-c:category/all) (-s)` {#saveditems}

保存物品，或管理已保存的物品。

`-t:[playerName]` 指定接收物品的目标玩家。

`-c:category` 指定物品分类，可在创建物品时使用，便于管理物品。

### `sc (playerName)` {#sc}

开始复制告示牌。

如果指定了玩家名，则由目标玩家点击告示牌并复制其文字，而不是由命令发起者操作。

### `scale [set/add/take/clear] (playerName) [amount] (-s)` {#scale}

设置实体的缩放比例。

### `scan` {#scan}

在指定范围或整张地图的所有可用容器中扫描指定物品。

子命令：

- `stats`——显示当前扫描统计。
- `pause`——暂停扫描。
- `continue`——继续扫描。
- `stop`——停止扫描。
- `stopall`——停止所有正在进行的扫描。
- `speed [amount]`——设置当前扫描速度。
- `autospeed [true/false]`——开启或关闭自动速度。
- `messages [true/false]`——开启或关闭消息输出。

参数：

- `id [id:data]`
- `q [minimum quantity]`
- `r [range in chunks]`——可用 `g` 代替数字，扫描整张地图。
- `n [item name]`
- `l [item lore]`
- `h`——使用手持物品的信息。
- `e [enchantname]`
- `elvl [enchantminlevel]`
- `oversize`
- `purge`——移除找到的物品，此功能需要在配置文件中启用。

示例：

```
/scan id 52 r 30
/scan id diamond_block r g q 32
```

### `scavenge (playerName)` {#scavenge}

将物品分解为原材料，并以一定概率提取附魔。

### `schedule [scheduleName] (-updatetimer)` {#schedule}

触发计划任务。

使用 `-updatetimer` 时，会更新现有计划任务的计时器，使其在设定的时间后触发，而不是保留原来的计时。这样可以提前触发特定计划任务，同时保持正确的执行间隔。

### `se [SignLine] [Text]` {#se}

修改告示牌某一行的文字。

使用 `/n` 另起一行。

### `search` {#search}

从所有用户中搜索物品、附魔、飞行、最大生命值、游戏模式、超出堆叠上限的模式等内容。

```
id [id:data]
name [some_custom_itemname]
lore [some_custom_lore]
enchant [lowest enchant level]
potion [lowest custom potion effect level]
fly [true or false]
gm [0/1/2/3 or survival/creative/adventure/spectator]
maxhp [lowest hp player have]
god [true/false]
oversize
```

示例：

```
/search gm 1
/search id 52
/search lore Uber_lore
```

### `seen [playerName/uuid]` {#seen}

查看玩家上次在线的时间。

### `select (pos1/pos2/shift/expand/contract/clear) (amount)` {#select}

管理选区。

### `sell (all/blocks/hand/same/gui/material) (playerName) (-s)` {#sell}

出售背包中的物品。

### `sendall [serverName]` {#sendall}

将所有在线玩家发送到目标服务器。

### `server [serverName] (playerName) (-f)` {#server}

连接到 BungeeCord 服务器。

### `serverlinks` {#serverlinks}

设置服务器链接。

### `serverlist` {#serverlist}

显示服务器列表。

### `servertime` {#servertime}

显示服务器时间。

### `setenchantworth` {#setenchantworth}

设置附魔价值，供 `sell hand` 和 `scavenger` 命令使用。

### `setfirstspawn (playerName)` {#setfirstspawn}

设置首次出生点。

### `sethome (homeName) (playerName) (-p) (-l:worldName;x;y;z) (block/Material) (slotNumber) (-overwrite)` {#sethome}

设置家的位置。

`cmi.command.sethome.unlimited`——允许设置不限数量的家。

`-l:worldName;x;y;z` 为新家指定自定义位置，需要 `cmi.command.sethome.customloc` 权限。

`-p` 将家设为私有，其他玩家无法传送到这里。

`(block/Material)` 可自定义家的 GUI 图标。例如，`/sethome home block` 会使用脚下的方块作为图标；`/sethome home woodenshovel` 会使用木锹物品作为图标。

如果填写了槽位编号，就会尝试将该家放在 GUI 的指定槽位中。编号范围为 0 到 900，相当于 20 页。例如，槽位编号为 52 时，如果后面没有其他图标，该家就会显示在第一页；但如果又有一个家的槽位编号大于 55，则所有编号大于 45 的家都会移到下一页，为按钮腾出位置。`/sethome home 50` 会将家放在 GUI 的 50 号槽位。多个家使用同一槽位时，会依次排列。

拥有 `cmi.command.sethome.overwrite` 权限时，可覆盖已有家的位置。

### `setmotd [newMotd] (-s)` {#setmotd}

设置服务器的 MOTD。

### `setrt (worldName) (center:[x]:[z]) (min:[range]) (max:[range]) (square/circle) (enabled/disabled)` {#setrt}

设置随机传送范围。

### `setspawn (playerName) (true/false) (-g:[groupName]) (-rng:[range]) (-w:world,world_nether) (loc:[world;x;y;z;yaw;pitch])` {#setspawn}

设置 `spawn` 命令的传送位置。

更多信息见[这里](commands/spawn.md)。

### `setwarp [warpName] (reqPermission) (hand/head/head:[playerName]) (slot) (autoLore) (-g:[groupName]) (world;x;y;z;yaw;pitch) (-confirm)` {#setwarp}

设置传送点的位置。

示例：

- `/cmi setwarp spawn`——创建通往出生点的普通传送点。
- `/cmi setwarp spawn true`——创建传送点，使用时需要 `cmi.command.warp.[warpname]` 权限。
- `/cmi setwarp spawn hand`——创建传送点，并使用手持物品作为 GUI 中的图标。
- `/cmi setwarp spawn 13`——创建传送点，并指定其 GUI 槽位，范围为 1–54。
- `/cmi setwarp spawn true hand 13`——创建传送点，使用手持物品作为图标，槽位为 13，并要求权限。
- `/cmi setwarp spawn true hand 13 false`——与上一条相同，但不生成物品描述。

更多信息见[这里](commands/warps.md)。

### `setworth (itemname) (-s:[sellPrice])` {#setworth}

通过 GUI 修改物品价值。

### `shadowmute [playerName] (time) (-s) (reason)` {#shadowmute}

禁言玩家，但不通知其已被禁言。

### `shakeitoff (playerName) (-s)` {#shakeitoff}

让所有骑在你身上的实体下来。

### `shoot (playerName) (-t:targetPlayer) (type) (speed)` {#shoot}

发射投射物。

类型：

- `smallfireball`
- `largefirreball`
- `thrownexpbottle`
- `snowball`
- `egg`
- `witherskull`
- `arrow`
- `bullet`
- `shulker`
- `shulkerbullet`
- `trident`
- `spit`
- `llama`
- `llamaspit`

### `silence` {#silence}

屏蔽公共消息。

`cmi.command.silence.bypass`——绕过消息屏蔽。

### `silentchest` {#silentchest}

切换箱子的静音模式。

### `sit (playerName) (-persistent) (-s) (location) (on/off)` {#sit}

坐在当前位置。

`-persistent` 防止玩家被活塞推动时退出坐下状态。

### `skin [skinName/off/update] (playerName) (-s)` {#skin}

更改玩家的皮肤。

### `smite (world;x;y;z/playerName) (-safe) (-s)` {#smite}

用闪电击中地面或玩家。

可使用玩家名或位置指定落雷地点。例如 `/cmi smite Zrips` 或 `/cmi smite LtCraft;15;168;458`。

`-safe` 表示闪电不造成伤害，只播放效果。

### `smithingtable (playerName)` {#smithingtable}

打开锻造台。

### `solve [equation]` {#solve}

计算复杂算式，从基础的 `2+2` 到 `cos(1)*pi/0.4+tan(5)` 都可使用。

### `sound [sound] (-p:[pitch]) (-v:[volume]) (playerName/-all/-l:playerName) (world;x;y;z) (-r:[radius]) (-s)` {#sound}

在目标位置播放声音。

### `spawn (playerName) (-s)` {#spawn}

传送回出生点。

### `spawner [EntityType]` {#spawner}

设置刷怪笼。

### `spawnereditor` {#spawnereditor}

编辑刷怪笼。

### `spawnmob [EntityType]` {#spawnmob}

在你的位置生成实体。

用法见[这里](commands/spawnmob.md)。

### `speed (playerName) [amount] (-s)` {#speed}

设置玩家的行走或飞行速度。

### `staffmsg [message/toggle/on/off]` {#staffmsg}

向管理人员频道发送消息。

### `stats (playerName)` {#stats}

查看玩家的统计信息。

### `statsedit (playerName) [add/take/set] [statistic] (subType) [amount] (-s)` {#statsedit}

编辑玩家的统计数据。

### `status` {#status}

显示服务器状态。

### `stonecutter (playerName) (-s)` {#stonecutter}

打开切石机。

### `sudo [playerName] (command/c:[text])` {#sudo}

强制另一名玩家执行命令。

`cmi.command.sudo.bypass`——防止玩家被“捉弄”。

### `suicide [playerName] (-s)` {#suicide}

自杀。

### `switchplayerdata [sourcePlayerName/uuid] [targetPlayerName/uuid]` {#switchplayerdata}

将一名玩家的所有数据转移到另一名玩家。

使用 UUID 可更准确地转移数据，尤其是在用户名相同的情况下。

### `tablistupdate (playerName) (-s)` {#tablistupdate}

强制更新所有玩家或指定玩家的 Tab 列表。

### `tempban [playerName] [timeValue] (reason) (-s)` {#tempban}

临时封禁玩家。

时间值前可加 `+` 或 `–`，表示调整现有的封禁时间。`+` 增加时间，`–` 减少时间；如果调整后的时间不足 1 tick，就会解除封禁。

例如，`/tempban Zhax +5m -s` 会为玩家的封禁时间增加 5 分钟。重复执行会继续延长封禁时间。

### `tempipban [ip/playerName] [time] (reason) (-s)` {#tempipban}

临时封禁玩家的 IP 地址。

`cmi.command.banip.bypass`——绕过封禁。

### `tfly [playerName] (timeInSec) (-s)` {#tfly}

临时开启玩家的飞行模式，直到重新登录或时间结束。

示例：

- `tfly Zrips 30`——开启飞行模式，持续 30 秒。
- `tfly Zrips +30`——额外增加 30 秒飞行时间。
- `tfly Zrips 0`——开启飞行模式，直到重新登录。
- `tfly Zrips`——查看玩家是否开启了临时飞行模式，以及何时结束。

### `tgod [playerName] (timeInSec) (-s)` {#tgod}

临时开启玩家的上帝模式，直到重新登录或时间结束。

示例：

- `tgod Zrips 30`——开启上帝模式，持续 30 秒。
- `tgod Zrips 0`——开启上帝模式，直到重新登录。
- `tgod Zrips`——查看玩家是否拥有临时上帝模式，以及剩余时长。

### `time (time) (world) (alter [value]) (-smooth)` {#time}

控制服务器时间。

示例：

```
/day
/night
/time 13:00:00
/time 1pm
/time 13
/time 7000ticks
/time 1pm Lt_Craft
/time 1pm all
/time add 0:30
/time take 0:30
/time freeze
/time unfreeze
/time realtime
/time autorealtime start/stop
```

### `titlemsg [playerName/all] [title \n subtitle] (-in:[ticks]) (-out:[ticks]) (-keep:[ticks])` {#titlemsg}

向玩家发送标题消息。

### `toast [playerName/all] (-t:[advType]) (-icon:[material]) [message]` {#toast}

向玩家发送 toast 提示消息。

仅适用于 1.12 及以上版本的服务器。

### `top [playerName] (-s)` {#top}

传送到当前位置的最高点。

### `tp [playerName] (playerName)` {#tp}

传送到玩家的位置。

### `tpa [playerName] (playerName) (-c)` {#tpa}

请求传送到玩家的位置。

### `tpaall` {#tpaall}

请求所有在线玩家传送到你的位置。

### `tpaccept (playerName)` {#tpaccept}

接受传送请求。

### `tpahere [playerName] (playerName) (-c)` {#tpahere}

请求玩家接受传送到你的位置。

`-c` 会将玩家传送到发出请求时的位置，而不是你当前的位置。命令发送者需要 `cmi.teleport.currentlocation` 权限。

### `tpall (playerName)` {#tpall}

将所有在线玩家传送到指定位置。

### `tpallworld [worldName] (worldName;x;y;z(;yaw;pitch)) (-a)` {#tpallworld}

传送走指定世界中的所有玩家。如果从控制台执行，可指定目标位置。

示例：`/cmi tpallworld LT_Craft_nether LT_Craft;0;150;0`

`-a` 会传送所有位于已不存在世界中的玩家。例如，通过 Multiverse Core 这类插件移除自定义世界后，离线玩家仍可能位于该世界。

### `tpbypass (playername)` {#tpbypass}

绕过传送到不安全位置时的限制。

### `tpdeny (playerName)` {#tpdeny}

拒绝传送请求。

### `tphere [playerName] (playerName)` {#tphere}

将玩家传送到你的位置。

### `tpo [playerName] (playerName)` {#tpo}

强制传送到玩家的位置。

### `tpohere [playerName] (playerName)` {#tpohere}

将玩家强制传送到你的位置。

### `tpopos (-p:playerName) [x] [y] [z] (world) (pitch) (yaw) (-rng:[range])` {#tpopos}

强制传送到指定位置，并绕过可能影响该玩家的区域保护。

`-p:` 指定要传送的玩家，需要 `cmi.command.tpopos.others` 权限。

`-rng:` 以指定位置为中心，在给定半径内随机传送。

`x`、`y`、`z` 可使用相对坐标。例如，`/tpopos ~0 ~1 ~0` 会将你向上传送 1 格。

### `tppos (-p:playerName) [x] [y] [z] (world) (pitch) (yaw) (-rng:[range])` {#tppos}

传送到指定位置。

`-p:` 指定要传送的玩家，需要 `cmi.command.tppos.others` 权限。

`-rng:` 以指定位置为中心，在给定半径内随机传送。

`x`、`y`、`z` 可使用相对坐标。例如，`/tppos ~0 ~1 ~0` 会将你向上传送 1 格。

### `tps (-spikes)` {#tps}

查看服务器的 TPS 状态。

### `tree (TreeType) (-p:[playerName])` {#tree}

在视线所指的位置生成树木。

由于 Minecraft 处理此功能的方式，此命令会忽略区域保护插件。

### `trim (playerName) (-s) (clear)` {#trim}

修改盔甲纹饰。

### `unban [playerName/ip] (-s)` {#unban}

解除玩家或 IP 的封禁。

### `unbreakable (playerName) (true/false)` {#unbreakable}

将物品设为不可损坏。

### `uncondense (itemName) (playerName) (-s` {#uncondense}

将物品解压缩为更小的单位。

### `unjail [playerName] (-s)` {#unjail}

将玩家从监狱中释放。

### `unloadchunks (-f)` {#unloadchunks}

从服务器内存中卸载区块。

`-f` 强制一次性卸载所有区块。

### `unmute [playerName] (-s)` {#unmute}

解除玩家的禁言。

### `unmutechat (-s)` {#unmutechat}

解除公共聊天禁言。

### `usermeta [playerName] [add/remove/clear/list/increment] (key) (value) (-s)` {#usermeta}

管理玩家的元数据。

设置的元数据可通过 `%cmi_user_meta_[key]%` 占位符，在插件各处显示。

更多信息见[这里](commands/user-meta.md)。

### `util (removeseats/testtarget)` {#util}

管理工具。

### `vanish (playerName/list) (on/off) (-s)` {#vanish}

使玩家隐身。

### `vanishedit (playerName) (action) (true/false)` {#vanishedit}

编辑玩家的隐身模式。

### `version` {#version}

显示插件版本。

### `viewdistance [range] (playerName/worldName/reset) (view/simulation)` {#viewdistance}

仅适用于 Paper 1.20.5 及以上版本的服务器。

管理单个玩家、单个世界或全局的视距。

### `voteedit (playerName) [add/set/take/clear] [amount] (-s)` {#voteedit}

管理玩家的投票数。

示例：

```
/voteedit Zrips
/voteedit add 10
/voteedit take 10
/voteedit Zrips clear
/voteedit Zrips add 10
```

### `votes (playerName)` {#votes}

查看玩家的投票数。

### `votetop (playerName)` {#votetop}

查看投票排行榜。

### `walkspeed (playerName) [amount] (-s)` {#walkspeed}

设置玩家的行走速度，范围为 0 到 10。

### `warn [playerName] (category) (reason) (-s)` {#warn}

警告玩家。

### `warnings (playerName)` {#warnings}

查看玩家的警告记录。

### `warp (warpName) (playerName) (-s) (-g:[groupName]) (-p:[pageNumber])` {#warp}

传送到传送点。

### `warpgroups` {#warpgroups}

列出传送点分组。

### `weather (sun/rain/storm) (lock/duration) (worldName/all)` {#weather}

控制服务器天气。

示例：

```
/sun
/rain
/storm
/sun lock
/sun 120
/sun Lt_Craft
```

### `workbench (playerName) (-s)` {#workbench}

打开工作台。

### `world (normal/nether/end/1/2/3...) (playerName) (-s)` {#world}

传送到其他世界。

除基础权限外，还需要 `cmi.command.world.[worldName]` 权限。

### `worth (all/blocks/hand/materialName)` {#worth}

查看物品价值。

### `worthlist (playerName) (-missing)` {#worthlist}

查看已设置出售价格的物品列表。

---

[查看原文](https://www.zrips.net/cmi/commands/)
