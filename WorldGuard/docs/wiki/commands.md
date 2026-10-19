---
title: 命令
source_url: https://worldguard.enginehub.org/en/latest/commands/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 命令 { #commands }

WorldGuard 提供五类命令：

- 游戏功能相关命令（`/god`、`/heal` 等）

- [区域](regions/index.md)管理

- 需要及时处理的紧急情况

- 故障排查

- WorldGuard 本身的管理（版本信息、重载配置）

所需权限节点见[权限页](permissions.md)。部分命令内置了别名，会列在同一行中。

!!! hint "提示"

    参数（如 `<player>`）外面带有 `[]` 时，表示该参数可选。输入命令时也不要输入 `<` 或 `>`。

## 游戏功能 { #gameplay }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">命令</th>
<th markdown="span">参数</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/god</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">使自己或其他玩家进入无敌状态。可额外指定 `-s`，不输出消息。</td>
</tr>
<tr>
<td markdown="span">/ungod</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">移除自己或其他玩家的无敌状态。可额外指定 `-s`，不输出消息。</td>
</tr>
<tr>
<td markdown="span">/heal</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">治疗自己或其他玩家。可额外指定 `-s`，不输出消息。</td>
</tr>
<tr>
<td markdown="span">/slay</td>
<td markdown="span">[-s] [&lt;player&gt;]</td>
<td markdown="span">杀死自己或其他玩家。可额外指定 `-s`，不输出消息。</td>
</tr>
<tr>
<td markdown="span">/locate</td>
<td markdown="span">[&lt;player&gt;]</td>
<td markdown="span">指定玩家时，让指南针指向该玩家；未指定玩家时，指向出生点。</td>
</tr>
<tr>
<td markdown="span">/stack /;</td>
<td markdown="span"></td>
<td markdown="span">整理背包并自动堆叠物品。</td>
</tr>
</tbody>
</table>

### 选择器 { #selectors }

接受玩家名称的命令支持*选择器*，但它们与大约 3 年后才出现的 Minecraft 选择器不同。

可以通过以下方式匹配玩家：

- 默认情况下，会匹配名称*以给定文字开头*的玩家

- `*` 匹配所有玩家

- `#<world>` 匹配某个世界中的所有玩家

- `#near` 匹配命令执行者附近的玩家

- `@<name>` 精确匹配玩家名称

## 区域 { #regions }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">命令</th>
<th markdown="span">参数</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/wg flushstates /wg clearstates</td>
<td markdown="span">[&lt;player&gt;]</td>
<td markdown="span">这是一个调试命令，用于清除为应用[区域旗标](regions/flags.md)而保存的玩家信息。例如，为使 `entry` 旗标正常工作，玩家每次移动时都会记录上一个所在“方块”，据此判断是否进入区域。当玩家因 `entry` 或 `exit` 旗标而被困在区域内外，尤其是在成员、权限组等发生变化后，此命令可能很有用。可选的玩家参数只重置指定玩家的状态；不提供时，则重置所有玩家的旗标状态。</td>
</tr>
<tr>
<td markdown="span">/rg bypass /rg toggle-bypass</td>
<td markdown="span">[on/off]</td>
<td markdown="span">切换区域保护绕过模式，让你忽略区域保护（禁止 PvP 的规则除外）</td>
</tr>
</tbody>
</table>

更多区域命令见[区域章节](regions/commands.md)。

## 紧急处理 { #emergency }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">命令</th>
<th markdown="span">参数</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/stopfire</td>
<td markdown="span">[&lt;world&gt;]</td>
<td markdown="span">立即停止当前世界或指定世界中的一切火焰蔓延。</td>
</tr>
<tr>
<td markdown="span">/allowfire</td>
<td markdown="span">[&lt;world&gt;]</td>
<td markdown="span">解除暂停火焰蔓延的状态。</td>
</tr>
<tr>
<td markdown="span">/stoplag /halt-activity /haltactivity</td>
<td markdown="span">[-s]</td>
<td markdown="span">移除所有世界中的全部实体，并进入一种停止所有物理事件和流体流动事件的模式。此外，每当区块加载时，也会移除其中的全部实体。此命令原本用于处理数以千计的实体或物品造成的问题。但加入此命令时，游戏中还没有可驯服的动物，实体损失并不是问题；现在情况已经不同，因此只应在极其紧急、别无他法时使用。可以提供 `-s`，使切换时不在聊天中发布公告。</td>
</tr>
<tr>
<td markdown="span">/stoplag /halt-activity /haltactivity</td>
<td markdown="span">-c [-s]</td>
<td markdown="span">禁用“停止卡顿”模式。可以提供 `-s`，使切换时不在聊天中发布公告。</td>
</tr>
<tr>
<td markdown="span">/stoplag /halt-activity /haltactivity</td>
<td markdown="span">-i</td>
<td markdown="span">显示“停止卡顿”模式的状态。</td>
</tr>
</tbody>
</table>

<a id="id1"></a>

## 故障排查 { #troubleshooting }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">命令</th>
<th markdown="span">参数</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/wg report</td>
<td markdown="span">[-p]</td>
<td markdown="span">写出一份报告文件，保存在 `plugins/WorldGuard/report.txt`，详细列出服务器环境（插件列表及其版本、世界设置）和 WorldGuard 配置。此命令便于在寻求帮助时向他人提供信息。报告不包含敏感数据。使用 `-p` 还会将报告提交到 pastebin 网站，生成可提供给他人的链接。</td>
</tr>
<tr>
<td markdown="span">/wg profile</td>
<td markdown="span">[-p] [-i &lt;milliseconds&gt;] [-t &lt;name&gt;] [&lt;minutes&gt;]</td>
<td markdown="block">

<p markdown="span">开始分析当前服务器的 CPU 使用情况，并运行指定时长；未指定时长时默认为 5 分钟。分析器基于 [WarmRoast](https://github.com/sk89q/warmroast)。</p> <p markdown="span">默认只收集负责世界 tick 的主线程数据，可以用 `-t` 按其他线程名称过滤，匹配不区分大小写；也可以指定星号（`*`）来分析所有线程，例如 `-t *`。默认采样间隔为 20 毫秒，可用 `-i` 将间隔设为 1 到 100 毫秒之间的自定义值。间隔越短，结果越准确，但性能开销越大；间隔越长，准确度和性能开销都越低。</p> <p markdown="span">使用 `-p` 还会把分析结果提交到 pastebin 网站，并生成可提供给他人的链接。推荐这样做，因为 pastebin 网站会将分析器输出排版为易于阅读的形式。</p>

</td>
</tr>
<tr>
<td markdown="span">/wg stopprofile</td>
<td markdown="span"></td>
<td markdown="span">停止当前正在运行的分析器。</td>
</tr>
<tr>
<td markdown="span">/wg debug testbreak</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">模拟“方块破坏”事件，详见下文。</td>
</tr>
<tr>
<td markdown="span">/wg debug testplace</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">模拟“方块放置”事件，详见下文。</td>
</tr>
<tr>
<td markdown="span">/wg debug testinteract</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">模拟“方块交互”事件，详见下文。</td>
</tr>
<tr>
<td markdown="span">/wg debug testdamage</td>
<td markdown="span">[-t] [-s] &lt;player&gt;</td>
<td markdown="span">模拟“实体受伤”事件，可用于测试 PvP 和 PvE，详见下文。</td>
</tr>
</tbody>
</table>

### 事件模拟 { #event-simulation }

例如，玩家因某种原因无法破坏方块，而你不想采取更大幅度的排查措施、又无法找出是哪个插件导致时，可以使用事件模拟命令。`/wg debug testbreak` 会模拟一次方块破坏，并记录是否有插件选择阻止这次虚拟的破坏操作，以及具体是哪些插件。

使用这些命令时必须指定一名玩家。该玩家是事件的*来源*。但事件目标（即被“破坏”的方块或被“攻击”的实体）默认取决于命令执行者的视角；如果指定了 `-t`，则改用来源玩家的视角。目标是该玩家准星指向的方块或实体。

命令输出中可能列出多个插件，但只有第一项最重要。例如，插件 A 阻止了操作，随后运行的插件 B 又“解除”了阻止，那么插件 A 最终不会产生影响。WorldGuard 会把最后运行的插件排在最前面。

示例

如果想查明 PvP 为何似乎被阻止，让另一名无法进行 PvP 的玩家看向你，然后执行以下命令：

```text
/wg debug testdamage -t other_player_name
```

注意，这些测试并不完全覆盖所有情况，因为 Bukkit 有时会为某些操作触发*其他*事件。例如，装满桶时会触发*装满桶事件*，而 WorldGuard 目前没有提供模拟它的方式。此外，也可能是 Minecraft 本身的功能（如冒险模式或内置出生点保护）在起作用。

使用 `-s` 可在控制台输出包含更多信息的堆栈跟踪。

!!! warning "警告"

    虽然这些是模拟事件，Minecraft 不会实际放置或破坏对应方块，但插件仍会响应它们。例如，某个插件可能允许右键点击特定标记的告示牌来传送；模拟与传送告示牌交互的事件，就可能真的使被测试的玩家传送。

## 其他 { #miscellaneous }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">命令</th>
<th markdown="span">参数</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">/wg version</td>
<td markdown="span"></td>
<td markdown="span">显示 WorldGuard 版本。</td>
</tr>
<tr>
<td markdown="span">/wg reload</td>
<td markdown="span"></td>
<td markdown="span">重载 WorldGuard 的配置、黑名单和区域数据。</td>
</tr>
<tr>
<td markdown="span">/wg running /wg queue</td>
<td markdown="span"></td>
<td markdown="span">显示 WorldGuard 正在运行的任务，例如在后台查询玩家 UUID 的任务。</td>
</tr>
</tbody>
</table>
