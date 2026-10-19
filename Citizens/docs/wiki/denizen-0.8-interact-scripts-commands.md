---
title: Denizen / 0.8 / 交互脚本 / 命令
source_url: https://wiki.citizensnpcs.co/Denizen/0.8/Interact_Scripts/Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5401
---


<a id="top"></a>

# Denizen / 0.8 / 交互脚本 / 命令

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>交互脚本命令用于使 Denizen 在交互脚本中执行操作。它们以 <a href="yaml.md" title="YAML">YAML</a> 序列写入 <a href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Interact_Scripts/Triggers&amp;action=edit&amp;redlink=1" title="Denizen/Interact Scripts/Triggers (page does not exist)">交互触发</a> 的脚本节点下。序列中的单个条目包含命令和修饰符。某些命令没有可用的修饰符。</p>
<a id="Syntax"></a><h3 id="syntax">语法</h3>
<p>语法对于正确执行非常重要。</p>
<ul>
<li>在命令名称前面放置插入符号 ^ 会导致该命令忽略命令之间正常的 0.5 秒延迟。</li>
<li>命令必须大写（i.e CHAT 不是聊天）</li>
<li>修饰符不区分大小写。</li>
<li><strong>[括号]</strong> 中的修饰符是 <strong>必填</strong>，用于执行命令。 [A或B]表示需要<em>要么</em> A或B。</li>
<li><strong>（括号）</strong> 中的修饰符是可选的，通常会更改命令的默认行为。</li>
<li>采用值的修饰符的形式为 MODIFIER:VALUE。</li>
<li>如果修饰符的 VALUE 包含空格（例如 NPC 或脚本名称），则必须将整个修饰符放在引号中。</li>
</ul>
<p>: : 示例：<code>- TELEPORT BOOKMARK:Bob:Bobshouse</code> 可以，但 <code>- TELEPORT 'BOOKMARK:Bob Jones:Bobshouse'</code> 需要引号才能正常运行。</p>
<p>Example:</p>
<div class="highlight"><pre>Some Trigger:
  Script:
  - COMMAND1 MODIFIER1 MODIFIER2:VALUE
  - COMMAND2 'MODIFIER1:Value With Spaces'
  - ^COMMAND3 'This will run instantly after COMMAND2'
</pre></div>
<a id="List_of_Commands"></a><h3 id="list-of-commands">命令列表</h3>
<a id="Script_Flow"></a><h4 id="script-flow">脚本流程</h4>
<p>这些命令对世界没有外部影响，但可以控制 Denizen 内的脚本流程。虽然不是必需的，但除了 WAIT 之外，通常建议将它们作为即时命令运行，以确保向玩家提供流畅的脚本反馈。</p>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>COOLDOWN</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[# 或 DURATION:#] (GLOBAL) ('SCRIPT: 脚本名称')
</th></tr>
<tr>
<td colspan="3">设置此脚本的冷却时间。默认为当前运行的脚本和交互的玩家。在脚本冷却之前，不会选择再次运行。需要指定带或不带 DURATION: 修饰符名称的秒数。
<p>Modifiers:
</p>
<ul><li>GLOBAL 使脚本对所有人都可用，而不仅仅是交互的玩家。</li>
<li>脚本：将冷却时间设置为不同的脚本。</li></ul>
<p><b>用法示例</b>
</p>
<pre>- COOLDOWN 60
- COOLDOWN GLOBAL 100
- COOLDOWN 'SCRIPT:A Different Script' 600
- COOLDOWN DURATION:15
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>DISENGAGE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（NPCID：#）
</th></tr>
<tr>
<td colspan="3"><p>允许再次与 <tt>ENGAGED</tt> Denizen 进行交互，它是 <tt>ENGAGE</tt> 命令的对应项。还可以指定不同Denizen的NPCID</p>
<p><b>用法示例</b>
</p>
<pre>- ENGAGE
- (Other Commands)
- DISENGAGE

- DISENGAGE NPCID:7
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>ENGAGE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（持续时间：#）（NPCID：#）
</th></tr>
<tr>
<td colspan="3"><p>阻止玩家交互触发 NPC。如果长脚本需要玩家监听或观看一系列事件，并且您不希望玩家在执行这些命令时能够进行交互，则这可能很有用。与 <tt>DURATION</tt> 或 <tt>DISENGAGE</tt> 一起使用。 <tt>DURATION</tt> 将在指定的秒数后自动 <tt>DISENGAGE</tt>。如果不包含 <code>NPCID</code>，则使用 Denizen 触发。请记住：<tt>ENGAGED</tt>期间，不会触发任何脚本，所以要勤于使用！</p>
<p><b>用法示例</b>
</p>
<pre>- ENGAGE
- (Other Commands)
- DISENGAGE

- ENGAGE DURATION:12 
- ENGAGE NPCID:2</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FAIL</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">('脚本：脚本名称')
</th></tr>
<tr>
<td colspan="3"><p>将脚本标记为 'Failed' 以检查是否符合 <tt>FAILED</tt> 要求。这与 <tt>FINISH</tt> 命令相同，只是跟踪 'fails'。同样，这有点像脚本的内置标志，并且行为很像计数器，即。您可以多次使用 <tt>FAIL</tt> 脚本，它会跟踪总数，除非 <tt>RESET</tt>。注意：一个脚本可以同时是 'finished' 和 'failed'，这两个命令独立工作。</p>
<p><b>用法示例</b>
</p>
<pre>- FAIL
- FAIL 'SCRIPT:Magic Feathers'</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FINISH</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">('脚本：脚本名称')
</th></tr>
<tr>
<td colspan="3"><p>将脚本标记为 'Finished' 以检查是否符合 <tt>FINISHED</tt> 要求。这有点像脚本的内置标志，并且行为很像计数器，即。您可以多次使用 <tt>FINISH</tt> 一个脚本，它会跟踪总数，除非 <tt>RESET</tt>。</p>
<p><b>用法示例</b>
</p>
<pre>- FINISH
- FINISH 'SCRIPT:Another Script'</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FLAG</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['标志名称'或'标志名称:标志值'或'标志名称:++'或'标志名称:--'] (PLAYER或DENIZEN或GLOBAL) (DURATION:#)
</th></tr>
<tr>
<td colspan="3"><p>需要上述参数之一。 <tt>FLAG</tt> 默认将变量或 'flags' 存储到玩家。这可用于跟踪可根据 FLAGGED 要求进行检查的信息。该命令的使用很简单，可以通过 3 种不同的方式使用。可以仅使用标志名称来设置布尔（真/假）值。如果设置，则值为 <tt>TRUE</tt>。当<tt>RESET</tt>时，就是<tt>FALSE</tt>。 <tt>FLAG</tt> 还可以设置整数（或数字）变量，并通过相应地使用 <tt>++</tt> 和 <tt>--</tt> 参数轻松地增加或减少它们。该命令还可以存储字符串值，请参见下面的示例。如果在持续时间内标志未更改，则使用 <tt>DURATION</tt> 会将标志值恢复为之前的值。使用 PLAYER 修饰符将在玩家上设置标志（这是默认行为）。使用 DENIZEN 修改器将在 Denizen 而不是玩家上设置一个标志。使用 GLOBAL 修饰符将设置一个独立于玩家或 Denizen 的标志。</p>
<p><b>用法示例</b>
</p>
<pre>- FLAG 'Sample Boolean Flag'
- FLAG Alignment:++
- FLAG Alignment:--
- FLAG 'Active Item:60 Feathers'
- FLAG WorldBossDead GLOBAL
- FLAG HasHealingFlag DURATION:180
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>中频
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(EXACTLY) (PLAYER or DENIZEN or GLOBAL) (-)[FLAG:Name or FLAG:Name:Value] (IS_NUMBER) ['SCRIPT:Script Run When Condition Met'] (QUEUE:TRIGGER or QUEUE:TASK) (APPEND) (ELSE 'SCRIPT:Script Run When Condition Not Met')
</th></tr>
<tr>
<td colspan="3">检查 FLAG 的值，如果满足条件则运行 TASK 脚本。默认情况下，任务脚本将在交互脚本继续之前运行。
<p>Modifiers:
</p>
<ul><li>EXACTLY - 对于整数标志，仅当值完全匹配时才满足 IF 条件。默认情况下，如果标志的值大于或等于其检查的值 i.e，则满足条件。 IF 'FLAG:AGE:13' 对于年龄至少为 13 的任何年龄都会通过，但 IF EXACTLY 'FLAG:AGE:13' 仅在年龄为 13 时才会通过。</li>
<li>玩家 - 检查此玩家上设置的标志（这是默认行为）</li>
<li>DENIZEN - 检查 Denizen 本身设置的 DENIZEN 标志，而不是该玩家上的标志</li>
<li>GLOBAL - 检查 GLOBAL 标志而不是该玩家上的标志</li>
<li>IS_NUMBER - 仅当标志的值为整数或双精度时才满足 IF 条件。</li>
<li>APPEND - 在此脚本完成后运行任务，而不是在下一个命令之前运行。</li>
<li>QUEUE - 指定在哪个队列中运行命令，默认为执行队列类型。</li>
<li>ELSE - 选择一个 TASK 脚本在不满足 IF 条件时运行。</li></ul>
<p><b>用法示例</b>
</p>
<pre>- IF FLAG:BossDead SCRIPT:Reward APPEND
- IF EXACTLY FLAG:Stage:4 SCRIPT:Stage4Instructions
- IF 'FLAG:AGE:13' 'SCRIPT:Meets Minimum Age' ELSE 'SCRIPT:Does Not Meet Minimum Age'
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RANDOM</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[#]
</th></tr>
<tr>
<td colspan="3">选择要从脚本中接下来的 # 行运行的单个命令并丢弃其余命令。
<p><b>用法示例</b>
</p>
<pre>- CHAT "I'm going to say the name of an animal"
- RANDOM 3
- CHAT "Cow"
- CHAT "Zebra"
- CHAT "Elephant"
- CHAT "Wasn't that fun?"
</pre>
</td></tr></tbody></table>
<a id="Server"></a><h4 id="server">服务器</h4>
<table align="left" class="wikitable collapsible collapsed" style="background:aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>EXECUTE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ASPLAYER or ASSERVER or ASNPC] ["command and arguments"]
</th></tr>
<tr>
<td colspan="3"><p>运行 Minecraft/Bukkit 命令。指定 <tt>ASPLAYER、ASSERVER 或 ASNPC</tt> 定义应如何执行命令。如果 Denizen NPC 是人型 NPC，ASNPC 将在 Denizen 交互时运行命令，暂时授予 OP 权限。运行 ASSERVER 将作为控制台命令运行，而运行 ASPLAYER 将仅作为玩家运行该命令。指定命令和参数时，不必使用游戏中运行命令时通常使用的“/”。您还可以使用 &lt;PLAYER&gt;、&lt;WORLD&gt; 或 &lt;NPCID&gt; 作为命令参数内的变量。</p>
<p><b>用法示例</b>
</p>
<pre>EXECUTE ASSERVER 'gamemode &lt;PLAYER&gt; 2'
EXECUTE ASNPC 'toggledownfall'
EXECUTE ASPLAYER 'spawn'</pre>
</td></tr></tbody></table>
<a id="Speech"></a><h4 id="speech">演讲</h4>
<p>这些命令向互动的玩家（通常是周围的旁观者）显示一些文本。文本命令还具有一些自动格式化功能，例如确保长消息中不会截断任何单词，以及应用颜色代码。参见：<a href="color-codes.md" title="Color Codes">Denizen 颜色代码</a>。 NPCs 和玩家对话的格式可以在 <a href="https://wiki.citizensnpcs.co/index.php?title=Denizen/config.yml&amp;action=edit&amp;redlink=1" title="Denizen/config.yml (page does not exist)">Denizen/config.yml</a> 中自定义。</p>
<ul>
<li>所有语音命令 <strong>需要报价</strong>（单 (' ') 或双 (" ")）文本周围。如果您的文本中有撇号（'），则您 <strong>必须</strong> 使用双引号（“”）！！</li>
</ul>
<p>您可以使用各种占位符来填写特定信息。基本款 are:</p>
<ul>
<li>&lt;NPC&gt; - 居民的名字。</li>
<li>&lt;PLAYER&gt; - 交互玩家的名字</li>
<li>&lt;DISPLAYNAME&gt; - 交互玩家的显示名称</li>
<li>&lt;HEALTH&gt; - 交互玩家的健康状况</li>
<li>&lt;WORLD&gt; - Denizen 的世界的名称</li>
</ul>
<p>如果在文本命令上使用 NOPLAYER 修饰符，则 &lt;PLAYER&gt;、&lt;DISPLAYNAME&gt; 和 &lt;HEALTH&gt; 标记不可用。</p>
<p>所有可用占位符的列表可以在 <a href="replaceables.md" title="Replaceables">可替换标签</a> 中找到。</p>
<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>ANNOUNCE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['要宣布的文字。']
</th></tr>
<tr>
<td colspan="3">将文本作为严重公告发送给所有玩家，无论他们在世界上的位置如何。对于任何类型的管理脚本都特别有用。
<p><b>用法示例</b>
</p>
<pre>- ANNOUNCE "&lt;PLAYER&gt; has found a secret!"
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>CHAT</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[“聊天文本。”] (NPCID:#) (NOPLAYER)
</th></tr>
<tr>
<td colspan="3">使 Denizen 与玩家对话。这是Denizen中的标准聊天机制。您还可以通过指定 Denizen 的 C2 NPCID 来更改进行通话的 NPC。如果您不希望 Denizen NPC 直接与玩家对话，请使用 <tt>NOPLAYER</tt> argument.
<p><b>用法示例</b>
</p>
<pre>- CHAT NOPLAYER "Here ye, hear ye!"
- CHAT "Hello there, children!"
- CHAT NPCID:6 'I only supply tools to builders!'
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>NARRATE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[“要叙述的文字。”]
</th></tr>
<tr>
<td colspan="3">向玩家显示一条没有发件人信息的消息。
<p><b>用法示例</b>
</p>
<pre>- NARRATE "There is a small mailbox here."
</pre>
</td></tr></tbody></table>
<a id="Denizen_Interaction"></a><h4 id="denizen-interaction">Denizen 互动</h4>
<p>Denizen 交互命令旨在通过允许在脚本期间对移动和动作进行精细控制来帮助使 Denizen 栩栩如生。这些并不是为了让 Denizen 进行连续的移动和动作，而是应该通过 <a href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Activity_Scripts/Activities&amp;action=edit&amp;redlink=1" title="Denizen/Activity Scripts/Activities (page does not exist)">活动</a> 来完成。</p>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>PAUSE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（持续时间：#）
</th></tr>
<tr>
<td colspan="3">导致 Denizen 停止任何路径或活动。对于在交互过程中将其保持在适当的位置很有用。
<p>Modifiers:
</p>
<ul><li>DURATION:</li></ul>
<dl><dd><dl><dd>在指定的秒数后自动恢复。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- PAUSE
- PAUSE DURATION:30
</pre>
</td></tr></tbody></table>
<a id="World_Interaction"></a><h4 id="world-interaction">世界互动</h4>
<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>DROP</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ID or ID:Data or MATERIAL or MATERIAL:Data or XP] (QTY:#) (BOOKMARK:LocationBookmark)
</th></tr>
<tr>
<td colspan="3">将项目放置在 Denizen 的位置或位置书签（如果指定）处。
<p><b>用法示例</b>
</p>
<pre>- DROP DIAMOND QTY:3
- DROP 18:3 QTY:1 BOOKMARK:LargeTree
- DROP XP QTY:10
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>听杀
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[TYPE:GROUP or TYPE:PLAYER or TYPE:ENTITY or TYPE:NPC] [NAME:Name or NPCID:#] (QTY:#) [SCRIPT:Task Script] (ID:Name)
</th></tr>
<tr>
<td colspan="3">此命令启动 Denizen 监听玩家杀死指定数量的指定目标，然后运行任务脚本。指定组名称、玩家名称或名称时，请使用 NAME:Name 修饰符 <a href="types.md" title="Types">实体类型</a> （如“僵尸”）。使用 TYPE:NPC 时使用 NPCID:# 修饰符。
<p>可选修饰符：
</p>
<ul><li>QTY：运行脚本前，玩家必须击杀的目标数量。</li>
<li>区域： - 玩家必须位于世界守卫区域，击杀数才算。</li></ul>
<p><b>用法示例</b>
</p>
<pre>- LISTEN KILL TYPE:ENTITY NAME:ZOMBIE QTY:5 SCRIPT:ZombieReward
- LISTEN KILL ID:BossListener TYPE:NPC NPCID:12 'SCRIPT:Kill Boss Reward'
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>监听块
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[TYPE:BREAK or TYPE:BUILD or TYPE:COLLECT] (QTY:#) [BLOCKS:Item Names] (REGION:WorldGuardRegion) [SCRIPT:Task Script] [ID:Name]
</th></tr>
<tr>
<td colspan="3">此命令启动 Denizen 侦听玩家与给定数量的块进行交互，然后运行任务脚本。
<p>可选修饰符：
</p>
<ul><li>QTY：- 玩家必须“做”才能完成的事情数量，默认 1。</li>
<li>区域： - 玩家必须位于世界守卫区域才能进行交互计数。</li></ul>
<p><b>用法示例</b>
</p>
<pre>- LISTEN BLOCK TYPE:BREAK BLOCKS:sand|stone|stonebrick QTY:5 SCRIPT:BlockFinished
- LISTEN BLOCK ID:BuildListner TYPE:BUILD 'SCRIPT:Kill Boss Reward' REGION:KillRegion
</pre>
</td></tr></tbody></table>
<table>
<thead>
<tr>
<th></th>
<th>SWITCH</th>
<th>[LOCATION:x,y,z,world] (STATE:ON</th>
</tr>
</thead>
<tbody>
<tr>
<td>OFF</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="Player_Interaction"></a><h4 id="player-interaction">玩家互动</h4>
<p>这些命令默认会影响交互的玩家。大多数都有修饰符来影响执行 Denizen。</p>
<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>CAST</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[SpellName] (DURATION:#) (POWER:#) (NPC:#) (PLAYER:PlayerName)
</th></tr>
<tr>
<td colspan="3">给予指定目标药水效果。  <a href="alchemist.md#Valid_Effects" title="Alchemist"> 有效药水名称与 Alchemist 的相同。</a>
<p>Modifiers:
</p>
<ul><li>持续时间：#</li></ul>
<dl><dd><dl><dd>效果持续时间，以秒为单位。默认值为 60。</dd></dl></dd></dl>
<ul><li>电源：#</li></ul>
<dl><dd><dl><dd>效果的级别，通常为1-5。默认值为 1。</dd></dl></dd></dl>
<ul><li>NPC:#</li></ul>
<dl><dd><dl><dd>施放效果的 NPC，而不是交互的玩家。使用 NPC id 进行指定。</dd></dl></dd></dl>
<ul><li>PLAYER:PlayerName</li></ul>
<dl><dd><dl><dd>要对其施放效果的玩家，而不是交互的玩家。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- CAST SPELL:confusion DURATION:300 POWER:3
- CAST SPELL:speed
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>FEED</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（金额：#）
</th></tr>
<tr>
<td colspan="3">为互动的玩家提供食物。提供食物和饱和度。
<p>修饰符：
AMOUNT：喂食量。默认值为 20。
<b>用法示例</b></p>
<pre>- FEED
- FEED 5
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HEAL</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（居民）（金额：#）
</th></tr>
<tr>
<td colspan="3">治愈互动的玩家。
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>治疗 Denizen 而不是玩家。</dd></dl></dd></dl>
<ul><li>AMOUNT:</li></ul>
<dl><dd><dl><dd>治愈量，不会超过最大治愈量。如果未指定，则默认为完全治疗。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- HEAL
- HEAL DENIZEN AMOUNT:1
</pre>
</td></tr></tbody></table>

