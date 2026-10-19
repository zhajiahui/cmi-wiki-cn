---
title: Denizen / 0.7 / 交互脚本 / 命令
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5391
---


<a id="top"></a>

# Denizen / 0.7 / 交互脚本 / 命令

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
<p>CANCELTASK</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['脚本：脚本名称']
</th></tr>
<tr>
<td colspan="3">使用 RUNTASK DELAY 取消为交互玩家安排的任务
<p><b>用法示例</b>
</p>
<pre>- CANCELTASK SCRIPT:RaceEnd
</pre>
</td></tr></tbody></table>
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
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RESET</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[FINISHED or FAILED or FLAG:FlagName] ('SCRIPT:Name of Script')
</th></tr>
<tr>
<td colspan="3"><p>将指定脚本的 FINISHED 或 FAILED 计数设置为 0，或将指定的布尔标志设置为 False。请记住：脚本和标志名称区分大小写！</p>
<p><b>用法示例</b>
</p>
<pre>- RESET FINISHED 'SCRIPT:Magic Feathers'
- RESET FLAG:SomeFlag
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RUNTASK</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['脚本：脚本名称'] (DELAY:#) (NPCID:#)
</th></tr>
<tr>
<td colspan="3">在交互玩家上以 Denizen 的身份运行 TASK 脚本。
<p>Modifiers:
</p>
<ul><li>DELAY 在运行任务之前等待此秒数。特定于交互玩家。如果该玩家已待处理此任务，则会取消该任务并在新的延迟后重新应用。</li>
<li>NPCID 作为不同的 Denizen 运行任务。</li></ul>
<p><b>用法示例</b>
</p>
<pre>- RUNTASK 'SCRIPT:Apple Reward'
- RUNTASK SCRIPT:RaceEnd DELAY:60
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WAIT</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[秒数] (队列:任务) (队列:触发)
</th></tr>
<tr>
<td colspan="3"><p>将队列暂停指定的秒数。如果不指定<tt>QUEUE</tt>，则使用发送队列。例如，如果命令是从交互（触发）脚本发送的，则将保留的队列是“触发队列”。当同时使用任务脚本和交互脚本时，在高级使用情况下可能很有用。</p>
<p><b>用法示例</b>
</p>
<pre>- WAIT 6
- WAIT 30 QUEUE:TASK</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>ZAP</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（步骤#）（'脚本：脚本名称'）（持续时间：#）（随机：#-#）
</th></tr>
<tr>
<td colspan="3"><p>确实是一个非常强大的命令。这就是脚本执行其步骤的方式。它不会自动完成，相反，您可以决定如何前进。单独使用 ZAP 只会让玩家前进到脚本中的下一步。注意：Denizen 不会检查该步骤是否存在，因此您可以在覆盖脚本分配中利用它。如果使用整数，则将使用该步骤。</p>
<p>指定 <tt>SCRIPT</tt> 来更改特定脚本中玩家的活动步骤。如果未指定，则使用触发脚本。 <tt>DURATION</tt> 可以设置为提供某种自动 "DEZAP"，在特定秒数后恢复后退，除非在该持续时间内发生了另一个 ZAP 命令。这可以用作 'timeout' 之类的。 <tt>RANDOM</tt> 可用于让玩家有机会选择前进的步骤。如果包含一个整数，则将随机选择步骤 1 到所选数字。如果使用两个整数，您还可以使用数字范围。</p>
<p><b>用法示例</b>
</p>
<pre>- ZAP
- ZAP 5
- ZAP RANDOM:6
- ZAP RANDOM:3-6 DURATION:60
- ZAP 6 'SCRIPT:Another Script'
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
<p>以下命令需要 [<a href="http://dev.bukkit.org/server-mods/vault/">Vault</a>] 和有效的权限系统。</p>
<table align="left" class="wikitable collapsible collapsed" style="background: aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>PERMISS</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[permission.node or 'GROUP:Group Name'] (WORLD) ('WORLD:World Name')
</th></tr>
<tr>
<td colspan="3"><p>如果您的权限系统支持，则为玩家提供一个权限节点或添加一个组。注意：您不应同时包含权限节点和组。如果您指定 <tt>WORLD</tt> 参数，它将仅将权限节点/组应用于当前世界。您也可以使用 <tt>WORLD:worldName</tt> 指定世界。</p>
<p><b>用法示例</b>
</p>
<pre>- PERMISS modifyworld.*
- PERMISS GROUP:HillsideEnemy
- PERMISS citizens.* WORLD:testworld
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background: aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>REFUSE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[permission.node or 'GROUP:Group Name'] (WORLD) ('WORLD:World Name')
</th></tr>
<tr>
<td colspan="3">如果您的权限系统支持，则从玩家中删除权限节点或组。注意：您不应同时包含权限节点和组。如果您指定一个 <tt>WORLD</tt> 参数，它将仅删除当前世界的权限节点/组。您也可以指定一个世界 <tt>WORLD:worldName</tt>。一般来说，但是您可以使用以下命令添加权限或组 <tt>PERMISS</tt>，您应该在删除时执行相同的操作 <tt>REFUSE</tt>.
<p><b>用法示例</b>
</p>
<pre>- REFUSE modifyworld.*
- REFUSE GROUP:HillsideEnemy
- REFUSE citizens.* WORLD:testworld
</pre>
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
<p>EMOTE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">['要表达表情的文本。'] (NPCID:#)
</th></tr>
<tr>
<td colspan="3">让我们用Denizen NPC 来表达一下情感。例如，类似于 IRC 中的 /me 命令。对于向玩家描述 NPC Denizen 可能需要什么，或者 NPC Denizen 的感觉可能很有用。 <tt>NPCID</tt> 可以指定更改 Denizen NPC 执行“表情”。
<p><b>用法示例</b>
</p>
<pre>- EMOTE 'is looking a bit nervous.'
- EMOTE NPCID:82 'thinks you should ask a few questions.'
- EMOTE "could use a stiff drink."
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HINT</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（短）
</th></tr>
<tr>
<td colspan="3">如果从带有聊天触发器的交互脚本步骤调用，这将输出玩家可以说的所有可能的内容的列表，以激活聊天触发器。
<p>Modifiers:
</p>
<ul><li>SHORT</li></ul>
<dl><dd><dl><dd>Denizen 只会说出触发词列表，而不是完整的句子。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- HINT
- HINT SHORT
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
<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>SHOUT</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[“聊天文本。”] (NPCID:#) (NOPLAYER)
</th></tr>
<tr>
<td colspan="3">向附近的玩家喊出文字。旁观者可以听到 NPC Denizen 喊叫的范围比标准的更大 <tt>CHAT</tt>，因此它也具有一定的技术优势。 <tt>NPCID</tt> 可以指定。使用 <tt>NOPLAYER</tt> 说话时会放弃对玩家的引用。不过，如果需要，您仍然可以参考 &lt;PLAYER&gt;。请参阅下面的示例了解使用方法。
<p><b>用法示例</b>
</p>
<pre>- SHOUT "EEEK! a spider!"
- SHOUT NOPLAYER "&lt;PLAYER&gt; is a thief! Get him!"
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lavender;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WHISPER</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[“耳语文本。”] (NPCID:#) (NOPLAYER)
</th></tr>
<tr>
<td colspan="3">向玩家耳语文本。实际上只是聊天的替代方案。默认情况下，旁观者无法听到 NPC 对交互玩家的耳语。与 <tt>CHAT</tt> 命令，可以指定NPCID。使用 NOPLAYER 也是可能的，因为它在某些情况下可能有用。但remember:默认情况下，旁观者无法看到NPC Denizen低语的实际文本。这可以在 <a class="mw-redirect" href="config.yml.md" title="Config.yml">config.yml</a>.
<p><b>用法示例</b>
</p>
<pre>- WHISPER "The password is.. 42."
- WHISPER NPCID:2 "Hey, I didn't want to blurt this out so everyone could hear, but..."
</pre>
</td></tr></tbody></table>
<a id="Denizen_Interaction"></a><h4 id="denizen-interaction">Denizen 互动</h4>
<p>Denizen 交互命令旨在通过允许在脚本期间对移动和动作进行精细控制来帮助使 Denizen 栩栩如生。这些并不是为了让 Denizen 进行连续的移动和动作，而是应该通过 <a href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Activity_Scripts/Activities&amp;action=edit&amp;redlink=1" title="Denizen/Activity Scripts/Activities (page does not exist)">活动</a> 来完成。</p>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HOLD</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ID or ID:Data or MATERIAL or MATERIAL:Data]
</th></tr>
<tr>
<td colspan="3">使 Denizen 持有特定的块或项目。
<p><b>用法示例</b>
</p>
<pre>- HOLD IRON_PICKAXE
- HOLD 98:3
</pre>
</td></tr></tbody></table>
<table>
<thead>
<tr>
<th></th>
<th>LOOK</th>
<th>[DIRECTION or BOOKMARK:BookamrkName or 'BOOKMARK:Denizen Name:BookmarkName' or CLOSE or AWAY] (NPCID:#) (DURATION:#)</th>
</tr>
</thead>
<tbody>
<tr>
<td>此命令控制 NPC Denizen 的查看位置。它需要“方向”、“书签”或“看起来接近”特征状态。有效 directions: 上、下、左、右、北、南、东、西、AT 和后。向后看或向后看以玩家的位置作为参考。 AT 将看着玩家，BACK 将目光从玩家身上移开。使用关闭</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
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
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RESUME</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">
</th></tr>
<tr>
<td colspan="3">取消先前的 PAUSE 命令。
<p><b>用法示例</b>
</p>
<pre>- RESUME
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>RETURN</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（速度：#）
</th></tr>
<tr>
<td colspan="3">让居民走回到调用 WALKTO 或 WALK 之前所在的位置。如果设置，将恢复 NPC 路径。
<p>Modifiers:
</p>
<ul><li>SPEED：是移动速度，一般应该在0.1到1.5之间</li></ul>
<p><b>用法示例</b>
</p>
<pre>- WALKTO BOOKMARK:Somewhere
- RETURN
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WALK</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(前进:#) (北:#) (南:#) (东:#) (西:#) (上:#) (下:#) (X:#) (Y:#) (Z:#) (速度:#)
</th></tr>
<tr>
<td colspan="3">使居民从当前位置走一段距离。  中断任何当前移动，并暂停 NPC 路径（如果处于活动状态）。所有提供的方向都添加到一个动作中。接受小数和负值。
<p>Modifiers:
</p>
<ul><li>SPEED：是移动速度，一般应该在0.1到1.5之间</li>
<li>FORWARD：使 Denizen 朝当前面向的任何方向行走。结合“LOOK CLOSE”和一个负值可以直接离开玩家。</li>
<li>+X 与 EAST 相同</li>
<li>+Y 与 UP 相同</li>
<li>+Z 与北相同</li></ul>
<p><b>用法示例</b>
</p>
<pre>- WALK NORTH;4 EAST:2.5
- WALK FORWARD:1
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:mintcream;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WALKTO</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[BOOKMARK:LocationBookmark or 'BOOKMARK:DenizenName:LocationBookmark' or PLAYER]  (SPEED:#)
</th></tr>
<tr>
<td colspan="3">使居民走到指定的位置书签，或互动的玩家。中断任何当前运动，并暂停 NPC 路径（如果处于活动状态）。
<p>Modifiers:
</p>
<ul><li>SPEED：是移动速度，一般应该在0.1到1.5之间</li></ul>
<p><b>用法示例</b>
</p>
<pre>- WALKTO PLAYER
- WALKTO 'BOOKMARK:Gary:GarysHouse'
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
<li>ID： - 杀死侦听器的名称；如果没有它，侦听器将采用完成后运行的脚本的名称。</li></ul>
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
<p>SPAWN</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[ENTITY_TYPE] (QTY:#) (BOOKMARK:LocationBookmark) ('BOOKMARK:Denizen Name:LocationBookmark') (SPREAD:#) ('EFFECT:[POTION_EFFECT] [LEVEL]') ('OPTION:[OPTIONS]')
</th></tr>
<tr>
<td colspan="3">生成指定数量的实体。如果位置书签丢失，它们将在 Denizen 附近生成。
<p>Modifiers:
</p>
<ul><li>传播：[#] 增加怪物可以生成的区域的“传播”。</li>
<li>'EFFECT:[POTION_EFFECT] [LEVEL]' 在怪物生成时对它施加药水效果。</li>
<li>'OPTION:OptionName OptionsValue' 将标志应用于 Mob。注意：仅适用于可以接受旗帜的生物。
<ul><li>有效选项名称 are:
<ul><li>通电、鞍具、婴儿、“职业 [PROFESSION_TYPE]”、剪毛、“彩色 [DYE_COLOR]”、愤怒”)
<ul><li>CREEPER 可以有 POWERED</li>
<li>猪可以有鞍</li>
<li>猪、羊、牛、村民、鸡、山猫和狼都可以生宝宝</li>
<li>村民可以有职业
<ul><li>有效的职业类型：农民、图书管理员、牧师、铁匠、屠夫</li></ul></li>
<li>羊可以剪毛和染色</li>
<li>WOLF 和 PIG_ZOMBIE 可以生气</li></ul></li></ul></li></ul></li></ul>
<p><b>用法示例</b>
</p>
<pre>- SPAWN BOAT
- SPAWN QTY:3 COW BOOKMARK:Cage
- SPAWN VILLAGER 'BOOKMARK:El Notcho:Gate'
- SPAWN QTY:10 PIG_ZOMBIE SPREAD:5
- SPAWN QTY:25 ZOMBIE SPREAD:20 'EFFECT:INCREASE_DAMAGE 2'
- SPAWN QTY:2 SHEEP 'OPTION:COLORED RED'
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>STRIKE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DENIZEN) (BOOKMARK:LocationBookmark) ('BOOKMARK:Denizen 名称:LocationBookmark') (NODAMAGE) (NPCID:#)
</th></tr>
<tr>
<td colspan="3">闪电就在你的指尖。
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>代替玩家向 Denizen 的位置发出闪电。</dd></dl></dd></dl>
<ul><li>位置书签</li></ul>
<dl><dd><dl><dd>击中地点书签而不是玩家的闪电。</dd></dl></dd></dl>
<ul><li>NPCID：#</li></ul>
<dl><dd><dl><dd>在指定NPC的位置进行闪电（使用npc id）</dd></dl></dd></dl>
<ul><li>NODAMAGE</li></ul>
<dl><dd><dl><dd>闪电只是装饰性的，不会造成任何损害。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- STRIKE
- STRIKE BOOKMARK:BigTree
- STRIKE DENIZEN NODAMAGE
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>SWITCH</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[BOOKMARK:BlockBookmark] or [BOOKMARK:DenizenName:BlockBookmark] (DURATION:#)
</th></tr>
<tr>
<td colspan="3">该命令将在指定的位置激活按钮、开关或压力板 <b>块</b> bookmark.
<p>Modifiers:
</p>
<ul><li>持续时间：#</li></ul>
<dl><dd><dl><dd>将在指定的秒数后再次切换设备。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- SWITCH BOOKMARK:LightSwitch DURATION:30
- SWITCH BOOKMARK:Jimbo:JimbosButton 
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:lightgoldenrodyellow;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WEATHER</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[SUNNY or STORMY or PRECIPITATING]
</th></tr>
<tr>
<td colspan="3">将Denizen的世界天气更改为指定类型。
<p><b>用法示例</b>
</p>
<pre>- WEATHER SUNNY
</pre>
</td></tr></tbody></table>
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
<p>GIVE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[MONEY or XP or HEROESEXP or ID or ID:Data or MATERIAL or MATERIAL:Data] (QTY:#)
</th></tr>
<tr>
<td colspan="3">
<p>给玩家一些东西。如果未指定 QTY:，则默认值为 1。您还可以使用 'XP' 给予 Minecraft XP。
使用 HEROSEXP 类型将为玩家（或英雄）带来探索体验。注意：这需要您的服务器上安装 HEROES！
<b>用法示例</b></p>
<pre>- GIVE MONEY QTY:10
- GIVE 17:2 QTY:3
- GIVE LEAVES:2
- GIVE HEROESEXP QTY:25
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>HARM</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">（居民）（金额：#）
</th></tr>
<tr>
<td colspan="3">伤害互动玩家。
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>伤害的是 Denizen 而不是玩家。</dd></dl></dd></dl>
<ul><li>AMOUNT:</li></ul>
<dl><dd><dl><dd>如果没有指定，伤害量默认为 1 点。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- HARM AMOUNT:5
- HARM DENIZEN
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
<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>TAKE</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[MONEY or ITEMINHAND or ID or ID:Data or MATERIAL or MATERIAL:Data] (QTY:#)
</th></tr>
<tr>
<td colspan="3">
<p>从玩家那里拿走一些东西。如果未指定 QTY:，则默认值为 1。
</p><p><b>用法示例</b>
</p>
<pre>- TAKE MONEY QTY:1000
- TAKE 17:2 QTY:1
- TAKE LOG:2
- TAKE ITEMINHAND
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:palegreen;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>TELEPORT</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(DENIZEN)  [BOOKMARK:LocationBookmark or 'BOOKMARK:Denizen Name:LocationBookmark']
</th></tr>
<tr>
<td colspan="3">将与玩家或居民进行交互的传送到指定的书签。
<p>Modifiers:
</p>
<ul><li>DENIZEN</li></ul>
<dl><dd><dl><dd>传送 Denizen 而不是玩家。</dd></dl></dd></dl>
<p><b>用法示例</b>
</p>
<pre>- TELEPORT BOOKMARK:FarAwayPlace
- TELEPORT DENIZEN 'BOOKMARK:Jim:JimsBasement'
</pre>
</td></tr></tbody></table>

