---
title: 配置
source_url: https://worldedit.enginehub.org/en/latest/config/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 配置 { #configuration }

WorldEdit 主要通过命令操作，但也有一些配置选项，可改变或限制命令与工具的行为。

## 配置文件 { #configuration-files }

安装 WorldEdit 并运行过服务器后，会生成主配置文件；具体位置取决于所用平台。

### Bukkit 服务器 { #bukkit-server }

Bukkit 版 WorldEdit 的配置位于服务器根目录下的 `plugins/WorldEdit/config.yml`。

Bukkit 使用的 YAML 格式对语法错误十分敏感。必须用 4 个空格缩进，使用制表符会破坏文件，同时还应遵守 YAML 语法。不熟悉 YAML 时，可以用[这样的在线校验器](https://yaml-online-parser.appspot.com/)检查配置，确认没有报错。

### Forge/Fabric { #forge-fabric }

NeoForge/Fabric 的配置位于 `config/worldedit/worldedit.properties`。服务器上相对于服务器根目录，即主服务器 .jar 所在目录；单人游戏中则位于“.minecraft”文件夹。

### Sponge 服务器 { #sponge-server }

Sponge 服务器，包括 SpongeForge 和 SpongeVanilla，配置位于 `config/worldedit/worldedit.conf`。

## 设置 { #settings }

!!! note "注意"

    各底层平台经常处于不同开发阶段，因此并非所有设置都能在所有平台生效。如果发现此类情况，请[告知我们](support.md)。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">defaultLocale</td>
<td markdown="span">default</td>
<td markdown="span">翻译默认使用的语言区域，默认跟随系统语言。</td>
</tr>
<tr>
<td markdown="span">profile</td>
<td markdown="span">false</td>
<td markdown="span">每次操作后是否输出修改方块数量和耗时。</td>
</tr>
<tr>
<td markdown="span">traceUnflushedSessions</td>
<td markdown="span">false</td>
<td markdown="span">编辑操作未正确完成时显示调试消息。</td>
</tr>
<tr>
<td markdown="span">disallowedBlocks</td>
<td markdown="span">&lt;list of blocks&gt;</td>
<td markdown="span">禁止用于方块模式的方块列表，主要是受到物理影响后会脱落的方块，避免一次生成数以千计的掉落物，造成严重卡顿或服务器崩溃。</td>
</tr>
<tr>
<td markdown="span">defaultChangeLimit</td>
<td markdown="span">-1</td>
<td markdown="span">单次操作默认可修改的方块数量。</td>
</tr>
<tr>
<td markdown="span">maxChangeLimit</td>
<td markdown="span">-1</td>
<td markdown="span">方块修改数量上限，在游戏内通过 `//limit` 设置</td>
</tr>
<tr>
<td markdown="span">defaultMaxPolygonalPoints</td>
<td markdown="span">-1</td>
<td markdown="span">多边形选区默认可使用的点数（`//sel poly`），-1 表示使用最大值</td>
</tr>
<tr>
<td markdown="span">maxPolygonalPoints</td>
<td markdown="span">20</td>
<td markdown="span">多边形选区可使用的最大点数，适用于 `//sel poly`；拥有 `worldedit.limit.unrestricted` 时使用</td>
</tr>
<tr>
<td markdown="span">defaultMaxPolyhedronPoints</td>
<td markdown="span">-1</td>
<td markdown="span">多面体选区默认可使用的点数（`//sel convex`），-1 表示使用最大值</td>
</tr>
<tr>
<td markdown="span">maxPolyhedronPoints</td>
<td markdown="span">20</td>
<td markdown="span">多面体选区可使用的最大点数，适用于 `//sel convex`；拥有 `worldedit.limit.unrestricted` 时使用</td>
</tr>
<tr>
<td markdown="span">snapshotRepo</td>
<td markdown="span"></td>
<td markdown="span">非空时，指定查找快照的目录名称</td>
</tr>
<tr>
<td markdown="span">snapshotsExperimental</td>
<td markdown="span">false</td>
<td markdown="span">设为 true 时使用新的快照代码，欢迎试用并报告缺陷！</td>
</tr>
<tr>
<td markdown="span">maxRadius</td>
<td markdown="span">-1</td>
<td markdown="span">接受半径参数的命令所允许的最大半径</td>
</tr>
<tr>
<td markdown="span">maxSuperPickaxeSize</td>
<td markdown="span">5</td>
<td markdown="span">超级镐工具的最大大小</td>
</tr>
<tr>
<td markdown="span">maxBrushRadius</td>
<td markdown="span">6</td>
<td markdown="span">笔刷的最大大小</td>
</tr>
<tr>
<td markdown="span">logCommands</td>
<td markdown="span">false</td>
<td markdown="span">是否记录更详细的命令使用信息。</td>
</tr>
<tr>
<td markdown="span">logFile</td>
<td markdown="span"></td>
<td markdown="span">logCommands 为 true 时，日志写入的文件。</td>
</tr>
<tr>
<td markdown="span">logFormat</td>
<td markdown="span">[%1$tY-%1$tm-%1$td %1$tH:%1$tM:%1$tS %4$s]: %5$s%6$s%n</td>
<td markdown="span">命令日志格式</td>
</tr>
<tr>
<td markdown="span">wandItem</td>
<td markdown="span">minecraft:wooden_axe</td>
<td markdown="span">默认用于选择区域的物品，现有会话的设置可覆盖它。设为 -1 表示没有默认物品。</td>
</tr>
<tr>
<td markdown="span">superPickaxeDrop</td>
<td markdown="span">true</td>
<td markdown="span">单方块超级镐模式破坏方块时是否掉落物品</td>
</tr>
<tr>
<td markdown="span">superPickaxeManyDrop</td>
<td markdown="span">true</td>
<td markdown="span">多方块超级镐模式破坏方块时是否掉落物品</td>
</tr>
<tr>
<td markdown="span">useInventory</td>
<td markdown="span">false</td>
<td markdown="span">要求玩家背包中有相应物品才能编辑，此选项支持不完善，不推荐使用</td>
</tr>
<tr>
<td markdown="span">useInventoryOverride</td>
<td markdown="span">false</td>
<td markdown="span">允许通过权限节点绕过上面的设置</td>
</tr>
<tr>
<td markdown="span">useInventoryCreativeOverride</td>
<td markdown="span">false</td>
<td markdown="span">允许创造模式绕过上面的设置</td>
</tr>
<tr>
<td markdown="span">navigationUseGlass</td>
<td markdown="span">true</td>
<td markdown="span">玩家处于半空时，`/up` 和 `/ceil` 是否在脚下放置玻璃供其站立</td>
</tr>
<tr>
<td markdown="span">navigationWand</td>
<td markdown="span">minecraft:compass</td>
<td markdown="span">导航工具的默认物品，可通过左键和右键使用 `/jumpto` 与 `/thru`；现有会话设置可覆盖它。设为 -1 表示没有默认物品。</td>
</tr>
<tr>
<td markdown="span">navigationWandMaxDistance</td>
<td markdown="span">50</td>
<td markdown="span">导航工具查找传送目标方块时的最大射线检测距离</td>
</tr>
<tr>
<td markdown="span">scriptTimeout</td>
<td markdown="span">3000</td>
<td markdown="span">CraftScript 被终止前允许运行的最长时间</td>
</tr>
<tr>
<td markdown="span">calculationTimeout</td>
<td markdown="span">100</td>
<td markdown="span">表达式被终止前默认允许运行的时间</td>
</tr>
<tr>
<td markdown="span">maxCalculationTimeout</td>
<td markdown="span">300</td>
<td markdown="span">表达式被终止前允许的最长运行时间，游戏内用 `//timeout` 修改</td>
</tr>
<tr>
<td markdown="span">allowedDataCycleBlocks</td>
<td markdown="span"></td>
<td markdown="span">非空时，指定方块数据循环切换工具可作用的方块白名单</td>
</tr>
<tr>
<td markdown="span">saveDir</td>
<td markdown="span">schematics</td>
<td markdown="span">保存原理图的目录，相对于 worldedit 文件夹</td>
</tr>
<tr>
<td markdown="span">scriptsDir</td>
<td markdown="span">craftscripts</td>
<td markdown="span">查找 CraftScript 的目录</td>
</tr>
<tr>
<td markdown="span">allowSymlinks</td>
<td markdown="span">false</td>
<td markdown="span">是否允许上述目录使用符号链接，便于多个服务器共享</td>
</tr>
<tr>
<td markdown="span">butcherDefaultRadius</td>
<td markdown="span">-1</td>
<td markdown="span">`/butcher` 的默认半径，-1 表示无限</td>
</tr>
<tr>
<td markdown="span">butcherMaxRadius</td>
<td markdown="span">-1</td>
<td markdown="span">`/butcher` 的最大半径</td>
</tr>
<tr>
<td markdown="span">serverSideCUI</td>
<td markdown="span">true</td>
<td markdown="span">是否允许使用 `//drawsel`</td>
</tr>
<tr>
<td markdown="span">defaultVerticalHeight</td>
<td markdown="span">256</td>
<td markdown="span">接受可选高度参数的命令所使用的高度。</td>
</tr>
<tr>
<td markdown="span">extendedYLimit</td>
<td markdown="span">false</td>
<td markdown="span">设为 true 时使用较慢但不受边界限制的位置表示。通常只有使用扩展高度上限的模组时才需要。</td>
</tr>
</tbody>
</table>
