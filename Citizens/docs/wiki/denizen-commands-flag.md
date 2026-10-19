---
title: Denizen / 命令 / Flag 命令
source_url: https://wiki.citizensnpcs.co/Denizen/Commands/Flag
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5394
---


<a id="top"></a>

# Denizen / 命令 / Flag 命令

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="Introduction"></a><h2 id="introduction">介绍</h2>
<p>标志是可以通过使用标志可替换标签或标记的需求在脚本和其他脚本中的任何位置进行检查的变量。
可以将标志放置在玩家、NPC 或全局上。放置在玩家身上的标志仅适用于该玩家，而放置在 NPC 上的标志仅适用于基于其 ID 的个人 NPC，因此具有相同名称的 NPCs 具有不同的标志，因为它们具有不同的 ID。但是，全局标志适用于整个服务器，并且可以轻松地从任何脚本中读取。</p>
<p>设置标志后，您可以随时使用 <a href="denizen-replaceable-tags.md#Flags" title="Denizen/Replaceable Tags">可更换标签</a> 之一将其回调。</p>
<a id="The_flag_command"></a><h1 id="the-flag-command">标志命令</h1>
<p>首先，您需要实际设置一个标志。您可以通过使用来做到这一点</p>
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>- 旗帜（{玩家}</td>
</tr>
</tbody>
</table>
<p>如果未指定标志的类型（玩家、npc 或全局），则默认情况下会将标志放置在玩家上；如果未指定标志的值，则默认情况下该值为“true”。</p>
<p>...对你来说太多了吗？让我们放慢速度。</p>
<a id="The_Basics"></a><h3 id="the-basics">基础知识</h3>
<p>要开始使用标志，您必须首先了解基础知识。这意味着您可以学习 4 种类型的标志 use: 布尔值、字符串、整数/双精度数和列表。</p>
<a id="Boolean"></a><h4 id="boolean">布尔值</h4>
<p>您需要的第一个、最常用、最基本的标志（除了默认标志之外）是布尔标志。布尔值是表示 true 或 false 的变量。</p>
<p>您可以使用以下方法将布尔标志设置为 true</p>
<div class="highlight"><pre>- flag "RandomFlag"</pre></div>
<p>...就是这样。这会自动将附加到与脚本交互的玩家的名为 RandomFlag 的标志设置为“true”。
您可以通过简单地将其设置为 false</p>
<div class="highlight"><pre>- flag "RandomFlag:false"</pre></div>
<p>这种类型的标志对于 'if' 语句很有帮助。有关更多信息，请参阅 <a href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Commands/If&amp;action=edit&amp;redlink=1" title="Denizen/Commands/If (page does not exist)">这里</a>。</p>
<a id="String"></a><h4 id="string">字符串</h4>
<p>让我们继续前进。您在旅途中需要的第二个最重要的标志可能是字符串标志。字符串是代表可以随时更改的单词或短语的变量。</p>
<p>例如，</p>
<div class="highlight"><pre>- flag "RandomFlag:Blah something whatever"</pre></div>
<p>会将与脚本交互的玩家的标志“RandomFlag”设置为“Blah Something What What”。</p>
<p>请记住，您还可以通过指定“npc”或“global”将该标志附加到正在运行脚本的 NPC 或服务器本身。这将在高级部分中介绍。</p>
<a id="Integer/Doubles"></a><h4 id="integerdoubles">整数/双精度数</h4>
<p>进入下一步...整数和双精度数！如果您对数学有所了解，您可能已经知道整数只是表示“整数”的一种奇特方式。从这个意义上说，双精度数只是带小数的数字。 （非整数。）</p>
<p>标志可以通过使用类似于......的东西来保存诸如此类的数字。</p>
<div class="highlight"><pre>- flag "IntegerFlag:3"
- flag "DoubleFlag:5.2"</pre></div>
<a id="Lists"></a><h4 id="lists">列表</h4>
<p>如果您想在一个地方存储大量对象，那么标志列表是最佳选择。</p>
<p>为此，您可以使用 Flag 命令的添加和删除功能，例如 so:</p>
<div class="highlight"><pre>### To add to a Flag list...
- flag "FlagList:-&gt;:&lt;player&gt;"
### To remove from a Flag list...
- flag "FlagList:&lt;-:&lt;player&gt;"</pre></div>
<a id="Usage_inside_scripts"></a><h1 id="usage-inside-scripts">脚本内部的使用</h1>
<a id="Checking_if_a_flag_exists"></a><h2 id="checking-if-a-flag-exists">检查标志是否存在</h2>
<p>在新的 0.9 开发版本中，您现在可以检查标志是否存在。</p>
<a id="With_the_If_command"></a><h3 id="with-the-if-command">使用 If 命令</h3>
<p>要使用 If 命令执行此操作，只需检查标志是否为空，如下所示 例如：</p>
<div class="highlight"><pre>- if &lt;player.flag[flag_to_check]&gt; == null narrate 'flag is null!'
  else narrate "&lt;player.flag[flag_to_check]&gt;"</pre></div>
<a id="With_Requirements"></a><h3 id="with-requirements">有要求</h3>
<p><strong>注意：要求已被弃用，取而代之的是 If 命令。</strong></p>
<p>要按照要求执行此操作，您可以使用 following: 中的任何一个</p>
<div class="highlight"><pre>### To check if the flag EXISTS (Whether or not it has no value doesn't matter.)
- flagged FlagName
### To check if the flag DOES NOT EXIST (The flag must not have had a value at any point in time.)
- -flagged FlagName
### To check if the flag is NULL (If the flag has no value or doesn't exist.)
- flagged FlagName:null</pre></div>
<a id="Mathematical_calculations"></a><h2 id="mathematical-calculations">数学计算</h2>
<p>数字标志（Integer、Double...）可用于计算。您可以使用 <m:> 标记或直接在标记后面添加操作（不同类型操作中的示例）。</m:></p>
<a id="Addition"></a><h3 id="addition">加法</h3>
<p>要将标志和数字添加在一起，只需使用 <code>add[]</code>。
示例：</p>
<div class="highlight"><pre>&lt;player.flag[money].add[2]&gt;</pre></div>
<a id="Subtraction"></a><h3 id="subtraction">减法</h3>
<p>要减去标志的值，只需使用 <code>sub[]</code>。
示例：</p>
<div class="highlight"><pre>&lt;player.flag[money].sub[10]&gt;</pre></div>
<a id="Multiplication_2"></a><h3 id="multiplication">乘法</h3>
<p>要乘以标志的值，只需使用 <code>mul[]</code>。
示例：</p>
<div class="highlight"><pre>&lt;player.flag[money].mul[1.25]&gt;</pre></div>
<a id="Multiplication_2"></a><h3 id="multiplication_1">乘法</h3>
<p>要将标志除以某物，请使用 <code>div[]</code>。
示例：</p>
<div class="highlight"><pre>&lt;player.flag[money].div[1.25]&gt;</pre></div>
<a id="Mod"></a><h3 id="mod">模组</h3>
<p>Denizen 还允许您对两个数字进行取模！只需使用<code>mod[]</code>即可。
示例：</p>
<div class="highlight"><pre>&lt;player.flag[money].mod[3]&gt;</pre></div>

