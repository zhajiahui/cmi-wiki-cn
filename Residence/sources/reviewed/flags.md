领地标志的默认设置位于 `flags.yml`，用于控制各标志是否可用，以及新建领地时的默认值。标志名称不可修改，也不可翻译；只能开启或关闭该标志的使用。

下面这些命令与 `/res lists` 不同，执行后立即生效。

- `/res check [ResidenceName] [FlagName] [PlayerName]`：检查领地的通用标志，或该领地中某位玩家的标志。例如，执行 `/res check MyResidence tp` 检查是否允许传送；如果已设置，会收到类似提示：`Flag tp applies to player zrips for residence MyResidence, value = True`。
- `/res clearflags [ResidenceName]`：移除领地当前设置的全部标志。
- `/res flags`：在聊天窗口列出可为领地或玩家设置的标志。不带参数执行 `/res set` 会打开图形界面，可用鼠标左键、右键设置标志。
- `/res gset [GroupName] [FlagName] [true/false/remove]`：为不同权限组设置标志。
- `/res lset [blacklist/ignorelist] [Material]`：在领地的黑名单或忽略列表中添加、移除一种材料，也就是方块。玩家需要知道该选项接受哪些方块。
- `/res lset info`：列出领地的黑名单和忽略列表设置。
- `/res pdel [ResidenceName] [PlayerName]`：移除玩家及其在领地中的标志。玩家仍在领地内时，此命令不会将其踢出。
- `/res pset [PlayerName] [FlagName_] [true/false/remove]`：为不同玩家设置标志。
- `/res reset [ResidenceName]`：将领地的所有标志恢复为默认值。需要从默认状态重新排查设置时，可以使用此命令。
- `/res set [ResidenceName] [FlagName] [true/false/remove]`：设置领地标志。站在领地内时，可以省略领地名称。在 `config.yml` 中开启图形界面选项后，不带参数执行 `/res set` 会打开界面，可用鼠标左键、右键设置标志。

## 预设标志列表命令

这组命令定义创建领地时可使用的标志列表。列表 `[ListName]` 中针对 `[PlayerName]` 或 `[GroupName]` 的设置，要在执行 `/res lists apply` 后才会应用到领地。

- `/res lists`：不带参数时，显示可用选项，用于修改领地、玩家或权限组的预设标志权限列表。
- `/res lists add [ListName]`：创建标志权限列表。
- `/res lists remove [ListName]`：删除标志权限列表。
- `/res lists apply [ListName] [ResidenceName]`：将列表应用到已有领地。同名标志会被指定列表中的设置覆盖。
- `/res lists set [ListName] [FlagName] [true/false/remove]`：在列表中开启、关闭或移除一个标志。
- `/res lists pset [ListName] [PlayerName] [FlagName] [true/false/remove]`：在列表中开启、关闭或移除某位玩家的标志。
- `/res lists gset [ListName] [GroupName] [FlagName] [true/false/remove]`：在列表中开启、关闭或移除某个权限组的标志。原文指出，悬停提示错误地显示了 `/res lists view` 的帮助。
- `/res lists view [ListName]`：查看列表中的所有标志权限。

## 标志值和示例

- `true`：允许该操作。
- `false`：禁止该操作。
- `enable`：允许使用该功能。这类标志始终需要再设置一个标志。
- `disable`：禁止使用该功能。这类标志始终需要再设置一个标志。
- `remove`：移除领地中的这项标志设置，无论原来的值是什么。

允许所有玩家在领地内建造，添加 `build` 标志：

`/res set Z-Castle build true`

允许指定玩家在领地内建造，添加 `build` 标志：

`/res pset Z-Castle johndoe build true`

移除某位玩家在领地内的全部标志：

`/res pset Z-Castle johndoe removeall`

## 标志列表

| 标志名称 | 作用 |
| --- | --- |
| `anvil` | 允许或禁止使用铁砧。 |
| `admin` | 给予玩家修改领地标志的权限。 |
| `animalkilling` | 允许或禁止击杀动物。 |
| `animals` | 允许或禁止动物生成。 |
| `anvilbreak` | 允许或禁止领地内的铁砧损坏。 |
| `backup` | 设为 true 时恢复区域原来的样子，需要 WorldEdit。 |
| `bank` | 允许或禁止向领地银行存款、取款。 |
| `bed` | 允许或禁止使用床。 |
| `beacon` | 允许或禁止与信标交互。 |
| `brew` | 允许或禁止使用酿造台。 |
| `build` | 允许或禁止建造。 |
| `burn` | 允许或禁止领地内的生物燃烧。 |
| `button` | 允许或禁止使用按钮。 |
| `cake` | 允许或禁止吃蛋糕。 |
| `canimals` | 允许或禁止自定义方式生成动物。 |
| `chorustp` | 允许或禁止通过紫颂果传送进入领地。 |
| `chat` | 允许加入领地聊天室。 |
| `cmonsters` | 允许或禁止自定义方式生成怪物。 |
| `commandblock` | 允许或禁止与命令方块交互。 |
| `command` | 允许或禁止在领地内使用命令。 |
| `container` | 允许或禁止使用熔炉、箱子、发射器等容器。 |
| `coords` | 隐藏领地坐标。 |
| `craft` | 给予 table、enchant、brew 标志。 |
| `creeper` | 允许或禁止苦力怕爆炸。 |
| `dragongrief` | 防止末影龙破坏方块。 |
| `day` | 将领地内的时间设为白天。 |
| `dye` | 允许或禁止给羊染色。 |
| `damage` | 允许或禁止领地内的所有实体伤害。 |
| `decay` | 允许或禁止领地内的树叶腐烂。 |
| `destroy` | 单独控制是否允许破坏方块，优先于 build 标志。 |
| `dryup` | 防止土地干涸。 |
| `diode` | 允许或禁止使用红石中继器。 |
| `door` | 允许或禁止使用门和活板门。 |
| `egg` | 允许或禁止与龙蛋交互。 |
| `enchant` | 允许或禁止使用附魔台。 |
| `explode` | 允许或禁止领地内发生爆炸。 |
| `enderpearl` | 允许或禁止使用末影珍珠传送进入领地。 |
| `fallinprotection` | 防止下落的方块进入领地。 |
| `falldamage` | 保护玩家免受摔落伤害。 |
| `feed` | 设为 true 时，为领地内的玩家补充饱食度。 |
| `friendlyfire` | 允许或禁止友军伤害。 |
| `fireball` | 允许或禁止领地内的火球。 |
| `firespread` | 允许或禁止火焰蔓延。 |
| `flowinprotection` | 允许或禁止液体流入领地。 |
| `flow` | 允许或禁止液体流动。 |
| `flowerpot` | 允许或禁止与花盆交互。 |
| `grow` | 允许或禁止植物生长。 |
| `glow` | 玩家进入领地时获得发光效果。 |
| `hotfloor` | 防止岩浆块造成伤害。 |
| `hidden` | 在 list 和 listall 命令的结果中隐藏领地。 |
| `hook` | 允许或禁止用钓鱼竿钩住实体。 |
| `healing` | 设为 true 时，为领地内的玩家恢复生命值。 |
| `iceform` | 防止结冰。 |
| `icemelt` | 防止冰融化。 |
| `ignite` | 允许或禁止点火。 |
| `itemdrop` | 允许或禁止丢弃物品。 |
| `itempickup` | 允许或禁止捡起物品。 |
| `jump2` | 允许跳到 2 格高。 |
| `jump3` | 允许跳到 3 格高。 |
| `keepinv` | 玩家死亡后保留背包。 |
| `keepexp` | 玩家死亡后保留经验。 |
| `lavaflow` | 允许或禁止熔岩流动，优先于 flow 标志。 |
| `leash` | 允许或禁止使用拴绳牵引动物。 |
| `lever` | 允许或禁止使用拉杆。 |
| `mobexpdrop` | 防止生物死亡时掉落经验。 |
| `mobitemdrop` | 防止生物死亡时掉落物品。 |
| `mobkilling` | 允许或禁止击杀生物。 |
| `monsters` | 允许或禁止怪物生成。 |
| `move` | 允许或禁止在领地内移动。 |
| `nanimals` | 允许或禁止动物自然生成。 |
| `nmonsters` | 允许或禁止怪物自然生成。 |
| `night` | 将领地内的时间设为夜晚。 |
| `nofly` | 允许或禁止在领地内飞行。 |
| `fly` | 切换领地内玩家的飞行状态。 |
| `nomobs` | 防止怪物进入领地。 |
| `note` | 允许或禁止使用音符盒。 |
| `nodurability` | 防止物品损失耐久度。 |
| `overridepvp` | 覆盖任何插件的 PvP 保护。 |
| `pressure` | 允许或禁止使用压力板。 |
| `piston` | 允许或禁止活塞推动、拉动领地内的方块。 |
| `pistonprotection` | 开启或关闭活塞将方块移入、移出领地的行为。 |
| `place` | 单独控制是否允许放置方块，优先于 build 标志。 |
| `pvp` | 允许或禁止领地内的 PvP。 |
| `rain` | 将领地内的天气设为下雨。 |
| `redstone` | 给予 lever、diode、button、pressure、note 标志。 |
| `respawn` | 自动让玩家重生。 |
| `riding` | 防止骑马。 |
| `shoot` | 允许或禁止在区域内发射投射物。 |
| `sun` | 将领地内的天气设为晴天。 |
| `shop` | 将领地加入专门的领地商店列表。 |
| `snowtrail` | 防止雪傀儡留下雪迹。 |
| `spread` | 防止方块蔓延。 |
| `snowball` | 防止雪球击退。 |
| `sanimals` | 允许或禁止通过刷怪笼或刷怪蛋生成动物。 |
| `shear` | 允许或禁止给羊剪毛。 |
| `smonsters` | 允许或禁止通过刷怪笼或刷怪蛋生成怪物。 |
| `subzone` | 允许玩家在领地内创建子领地。 |
| `title` | 显示或隐藏进入、离开领地时的消息。 |
| `table` | 允许或禁止使用工作台。 |
| `tnt` | 允许或禁止 TNT 爆炸。 |
| `tp` | 允许或禁止传送到领地。 |
| `trade` | 允许或禁止在领地内与村民交易。 |
| `trample` | 允许或禁止踩坏农作物。 |
| `trusted` | 给予 build、use、move、container、tp 标志。 |
| `use` | 允许或禁止使用门、拉杆、按钮等。 |
| `vehicledestroy` | 允许或禁止破坏载具。 |
| `witherspawn` | 允许或禁止生成凋灵。 |
| `phantomspawn` | 允许或禁止生成幻翼。 |
| `witherdamage` | 允许或禁止凋灵造成伤害。 |
| `witherdestruction` | 允许或禁止凋灵破坏方块。 |
| `waterflow` | 允许或禁止水流动，优先于 flow 标志。 |
| `wspeed1` | 将领地内玩家的行走速度改为 %1。 |
| `wspeed2` | 将领地内玩家的行走速度改为 %1。 |
