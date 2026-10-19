---
title: Denizen / 命令
source_url: https://wiki.citizensnpcs.co/Denizen/Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5375
---


<a id="top"></a>

# Denizen / 命令

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="List_of_commands"></a><h2 id="list-of-commands">命令列表</h2>
<p><s>&lt;big&gt;<div style="color:red">Denizen 持续更新中。此页面仅显示基本脚本命令（当有变化时我们会尝试更新页面）！</div></s></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Entity">实体</h3></div></s></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="cast">演员表</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">演员表
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[effect] (duration:#{60s}) (power:#{1}) (target(s):npc|player|n@&lt;npc.id&gt;|p@&lt;player.name&gt;|entity_name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">向目标提供药水效果，目标可以是玩家、NPC 或其他实体。找到所有有效的药水效果名称 <a class="external text" href="http://jd.bukkit.org/rb/apidocs/org/bukkit/potion/PotionEffectType.html" rel="nofollow">这里</a>.
<p>如果您不选择目标，则与此 NPC 交谈的玩家将获得药水效果。您可以通过将多个目标放在 | 之间来一次使用更多目标。人物。
</p><p>您可以选择效果的持续时间（默认为 60 秒）及其强度（默认为 1）。通常，3 的幂是药水效果的最大值，大于该值不会产生任何效果。
</p><p><br/>
<b>示例</b>
</p>
<pre>- cast blindness power:3 duration:7
</pre>
<p>在上面的例子中，与这个NPC交谈的玩家将被强烈致盲7秒。
</p>
<pre>- cast regeneration power:1 duration:10 target:p@&lt;npc.owner&gt;
</pre>
<p>在这个例子中，NPC将为其拥有者提供微弱的再生效果，持续10秒。
</p><p><br/>
</p>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Item">项目</h3></div></s></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="NPC">NPC</h3></div></s></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="assignment">作业</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">作业
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[{设置}|删除]（script:名称）
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">设置或删除 NPC 的分配。如果未指定设置或删除，则默认设置。
<p><br/>
<b>示例</b>
</p>
<pre>- assignment set "script:Evil Wizard"
- assignment remove
- assignment "script:Pet Cat"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="attack">攻击</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">攻击
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">（停止）
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使NPC攻击或停止攻击玩家。
<p><br/>
<b>示例</b>
</p>
<pre>- attack
- attack stop
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="chat">聊天</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">聊天
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[“&lt;text&gt;”]（无目标/目标：&lt;entity&gt; | ...）
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">从此 NPC 向玩家发送消息。
<p>如果在 npcid 参数中选择了不同的 NPC ID，则消息将从该 NPC 发送。如果您使用目标参数，该消息也可以发送给不同的玩家，甚至发送给另一个 NPC。
</p><p><br/>
<b>示例</b>
</p>
<pre>- chat "It's nice to see you again, &lt;player.name&gt;."
- chat "I would like to introduce you to &lt;player.name&gt;." target:n@7
- chat "Bob, do you know &lt;player.name&gt;?" target:p@Bob
- chat npcid:9 "Our enemy is giving orders to his companion." target:p@Bob
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="follow">关注</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">关注
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">（停止）
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使NPC跟随或停止跟随玩家。
<p><br/>
<b>示例</b>
</p>
<pre>- follow
- follow stop
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="look">看看</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">看看
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使NPC看向某个位置。
<p><br/>
<b>示例</b>
</p>
<pre>- look location:300,60,500,world
- look location:&lt;player.location&gt;
- look location:&lt;anchor:Lever&gt;
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="shoot">射击</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">射击
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[entity:name] (ride) (burn) (explode) (location:x,y,z,world) (script:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使 NPC 射出实体。找到所有有效的实体名称 <a class="external text" href="http://jd.bukkit.org/rb/apidocs/org/bukkit/entity/EntityType.html" rel="nofollow">这里</a>.
<p>实体可以被射向某个位置。如果没有指定位置，它们将朝着 NPC 所看的方向拍摄。您还可以选择在实体到达该位置时运行的脚本。
</p><p>此外，您可以使用ride 参数来骑乘一个实体，burn 参数可以将其点燃，explode 参数可以让它在到达该位置或被卡住时爆炸。
</p><p><b>示例</b>
</p>
<pre>- shoot entity:zombie
- shoot entity:arrow location:&lt;player.location&gt;
- shoot entity:fireball location:&lt;player.location&gt; "script:Shoot Another Fireball"
- shoot entity:minecart ride location:&lt;anchor:Rollercoaster&gt;
- shoot entity:cow ride burn explode location:&lt;anchor:Hill&gt; "script:Bovine Destruction"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="sit">坐</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">坐
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">（坐|站）（location:x，y，z，世界）
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使 NPC 坐在或站立在某个位置。
<p><br/>
<b>示例</b>
</p>
<pre>- sit location:300,65,300,world
- sit location:&lt;anchor:Chair&gt;
- stand
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="trigger">触发器</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">触发器
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[name:chat/click/damage/proximity] (state:true/false) (cooldown:&lt;#.#&gt;) (radius:&lt;#&gt;)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">启用或禁用交互触发器。
<p>使用此命令启用或禁用交互触发器，通常在 <a class="external text" href="http://wiki.citizensnpcs.com/Denizen/Types_of_Scripts#Assignment_Script" rel="nofollow">作业脚本</a> 中。</p><p><b>示例</b>
</p>
<pre>- trigger name:chat state:true
- trigger name:proximity statue:true radius:10
</pre>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Player">玩家</h3></div></s></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="feed">饲料</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">饲料
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(amt:#) (target:npc|{player})
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">填充玩家的食物栏，或者如果将 NPC 指定为目标，则填充此 NPC 的食物栏。还可以设置玩家或 NPC 的喂食量。完全装满的食物条的数量为 20。因此，1 的数量是食物条中的半个小腿。
<p><br/>
<b>示例</b>
</p>
<pre>- feed
- feed amt:15 target:npc
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="heal">治愈</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">治愈
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(amt:#) (target:npc|{player})
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">填充玩家的生命条，或者如果将 NPC 指定为目标，则填充此 NPC 的生命条。还可以设置玩家或 NPC 的治疗量。完全满的生命条的数量为 20。因此，1 的数量相当于生命条中的半颗心。
<p><br/>
<b>示例</b>
</p>
<pre>- heal
- heal amt:7 target:npc
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="narrate">叙述</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">叙述
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[“旁白文字”]（player:名称）
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">向该玩家发送消息，或者向另一玩家（如果指定）发送消息。
<p><br/>
<b>示例</b>
</p>
<pre>- narrate "A musty odor hangs in the air and you can hear the distant sound of trickling sewer water."
- narrate player:Bob "&lt;player.name&gt; has been hired to track you down!"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Script_flow">脚本流程</h3></div></s></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="anchor">锚</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">锚
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[id:name] [assume|add|remove|walkto|walknear] (range:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">假设、添加、删除和命令 NPC 行走到或行走到使用 Citizens 2 npc 命令指定的锚点附近
<p>“/npc 锚” 允许基于预定义点的动态指定路径。允许指定范围，其中有问题的 NPC 
可以步行到锚点。
</p><p><br/>
<b>示例</b>
</p>
<pre>A command having an NPC assume an Anchor:
- anchor id:postoffice assume range:20
-------------------------------------
Two commands demonstrating how one may add an anchor based on the NPC's location:
- Chat "Wow &lt;player.name&gt;, Now that I've walked to this location I am going to create an anchor point at this location so 
  I can walk back here later."
- anchor id:example_anchor add
-------------------------------------
Two commands demonstrating how one may remove a specified anchor via an NPC"
- chat "You know &lt;player.name&gt;, I actually don't think I'll ever need to return here again, I will delete this anchor point"
- anchor id:example_anchor remove
-------------------------------------
An example of a command for an NPC to walk towards a specified anchor point. Walkto has the NPC walk directly to the point; 
whereas Walknear has the npc be less precise when walking to the point:
- anchor id:Treasure_Chest walkto range:30
- anchor id:Wheat_Fields walknear
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="queue">队列</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">队列
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(queue:&lt;id&gt;) [clear/pause/resume/delay:&lt;#&gt;]
<p><b>警告：此命令已弃用，所有脚本作者都应改用 QUEUE 命令</b>
</p>
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">清空队列中所有尚未执行的命令。如果未指定队列名称，则当前队列被清空。您还可以多次使用队列参数来指定更多要清空的队列。
<p>使用此命令可停止另一个脚本中的脚本或操作中的脚本。
</p><p><b>示例</b>
</p>
<pre>- queue queue:magicalattacks clear
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="cooldown">冷却时间</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">冷却时间
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(duration:#{60s}) (全局|player:name{连接的玩家}) (script:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使该玩家在一段时间内（默认为 60 秒）不再执行此脚本。
<p>您还可以使该脚本不为其他玩家执行，或者使其在全局范围内不可用，并且您还可以选择另一个脚本来代替此脚本。
</p><p><br/>
<b>示例</b>
</p>
<pre>- cooldown
- cooldown duration:30s player:Bob "script:Offer Quest"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="define">定义</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">定义
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[&lt;id&gt;] [&lt;value&gt;]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">与标志类似，此命令将全局变量设置为任何值，以后可以使用 %id% 在任何地方回调该值。
<p><br/>
<b>示例</b>
</p>
<pre>- define "lastplayer" "&lt;player.name&gt;"
- define "player_&lt;player.name&gt;'s_home" "&lt;player.location&gt;"
- announce "%lastplayer% set their home at %player_&lt;player.name&gt;'s_home%! Go raid it!"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="determine">确定</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">确定
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[“价值”]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">该命令仅与 <a href="denizen-replaceable-tags.md" title="Denizen/Replaceable Tags">程序</a> 可更换标签。它被放入由标记运行的过程脚本中，并将标记的值设置为您选择的任何值。它通常用作 <a href="#if">如果</a> 命令或与 <a href="#random">随机的</a> command.
<p><br/>
<b>示例</b>
</p>
<pre>- if &lt;player.name&gt; == "Bob" determine "Bobby"
- if &lt;flag.p:Enemy&gt; == "Galerion" determine "the fearsome Galerion"
  else if &lt;flag.p:Enemy&gt; == "Narkon" determine "the evil Narkon"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="disengage">脱离</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">脱离
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(npcid:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">停止 <a href="#engage">参与</a> 以前在此 NPC 上使用的命令。如果指定了 npcid，则可以停用不同的 NPC。
<p><br/>
<b>示例</b>
</p>
<pre>- disengage
- disengage npcid:8
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="engage">参与</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">参与
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(duration:#) (npcid:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">暂时停用此 NPC 的触发器，使玩家无法在选定的持续时间内与其交互，或者直到 <a href="#disengage">脱离</a> 命令用于其上。如果指定了 npcid，则可以使用不同的 NPC。
<p><br/>
<b>示例</b>
</p>
<pre>- engage
- engage duration:40s npcid:7
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="fail">失败</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">失败
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(script:script_name{附加脚本}) (player:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">将该脚本或另一个脚本被该玩家或另一玩家（如果指定）失败的次数加 1。然后，您可以使用以下命令检查脚本失败的次数 <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Script_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Script Requirements (page does not exist)">脚本</a> requirement.
<p><br/>
<b>示例</b>
</p>
<pre>- fail
- fail "script:Defend the Castle" player:Bob
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="finish">完成</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">完成
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(script:script_name{附加脚本}") (player:name)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">将该脚本或另一个脚本由该玩家或另一玩家（如果已指定）完成的次数加 1。然后，您可以使用以下命令检查脚本完成的时间 <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Script_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Script Requirements (page does not exist)">脚本</a> requirement.
<p><br/>
<b>示例</b>
</p>
<pre>- finish
- finish "script:Siege the Castle" player:Bob
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="flag">旗帜</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">旗帜
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">({player}|npc|global) [name([#])](:action)[:value] (duration:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">设置标志的值，该标志是一个变量，可以使用以下命令在该脚本和其他脚本的其他位置进行检查 <a href="denizen-replaceable-tags.md#Flags" title="Denizen/Replaceable Tags">标记可替换标签</a> 或 <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Script_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Script Requirements (page does not exist)">标记的要求</a>.
<p>可以将标志放置在玩家、NPC 或全局上。放置在玩家上的标志仅适用于该玩家，而放置在 NPC 上的标志仅适用于基于其 ID 的单个 NPC，因此具有相同名称的 NPCs 具有不同的标志，因为它们具有不同的 ID。但是，全局标志适用于整个服务器，并且可以轻松地从任何脚本中读取。
</p><p>如果未指定标志的类型（玩家、npc 或全局），则默认情况下会将标志放置在玩家上；如果未指定标志的值，则默认情况下该值为“true”。
</p><p>欲了解更多信息，<a href="denizen-commands-flag.md" title="Denizen/Commands/Flag">点击这里</a>。</p><p><b>示例</b>
</p>
<pre>- flag "Finished Baker's Quest"
- flag global "Skeleton Invasion Ended"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="if">如果</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">如果
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[&lt;value&gt;] (!)(&lt;operator&gt; &lt;value&gt;) (&amp;&amp;/|| ...) [&lt;commands&gt;] (否则 &lt;commands&gt;)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">将一个值与另一个值进行比较，如果结果为 true，则将运行“if”语句内的命令，并且不会检查更多可比值。如果为假，则将比较下一个“else if”（如果有），如果为真，则将运行该“else if”中的命令，并且不会检查更多可比项。这将继续发生，直到脚本用完可比对象或到达“else”，在这种情况下，“else”内的命令将运行并且脚本将继续。
<p>欲了解更多信息，<a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Commands/If&amp;action=edit&amp;redlink=1" title="Denizen/Commands/If (page does not exist)">点击这里</a>。</p><p><b>示例</b>
</p>
<pre>- if "&lt;player.inventory.contains[1]&gt; announce "Hahaha! &lt;player.name&gt; has no stone!"
- if &lt;player.name&gt; == "davidcernat" execute as_server "ban &lt;player.name&gt;"
- if &lt;context.message.contains[Bob]&gt; announce "&lt;player.name&gt; said Bob! Smite them!"
  else if &lt;player.name.contains[Bob]&gt; announce "&lt;player.name&gt;'s name contains Bob! Smite them!"
  else {
    - announce "No mention of Bob can be found. Proceeding with life..."
    - run Life delay:0s
  }
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="log">日志</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">日志
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[&lt;text&gt;] (type:severe/info/warning/fine/finer/finest) [file:&lt;name&gt;]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">将您想要的任何文本记录到主服务器文件夹内的文件中。如果该文件不存在，它将创建它。
<p><br/>
<b>示例</b>
</p>
<pre>- log "Something happened!" "file:Denizen.log"
- log "Bob punched Joe!" "file:logs/DenizenLog.txt"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="random">随机的</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">随机的
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[#]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">运行随机选择的多个命令中的一个。
<p><br/>
<b>示例</b>
</p>
<pre>- random 3
- chat "One."
- chat "Two."
- chat "Three."
</pre>
<p>在上面的示例中，将仅运行三个聊天命令之一。
</p>
<pre>- random 2
- chat "One."
- chat "Two."
- chat "Three."
</pre>
<p>在此示例中，将显示“一”或“二”，但将始终显示“三”。
</p>
<pre>- random 3
- attack
- chat "Get out of here!"
- runtask "script:Call Reinforcements"
</pre>
<p>在这里，NPC 要么攻击玩家，告诉玩家离开，要么运行一个呼叫增援的脚本。
</p>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Server">服务器</h3></div></s></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="announce">宣布</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">宣布
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[“公告文本”] (to_ops)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">向服务器上的每个玩家发送一条消息。如果使用 to_ops 参数，则消息仅发送给操作员。
<p><br/>
<b>示例</b>
</p>
<pre>- announce "The skeleton invasion has ended."
- announce "&lt;player.name&gt; has joined the blue team!"
- announce to_ops "&lt;player.name&gt; is requesting help from operators."
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="chunkload">块加载</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">块加载
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">({add}|remove|removeall) [location:x,y,z,world] (duration:{-1s})
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">将指定位置的块加载到服务器内存中，以便它不会消失。 NPCs 如果块不保持生成状态
<p>消失。因此，此命令对于确保 NPC 生成并执行其应该执行的操作非常有用，无论玩家是否在附近
NPC 所在的块被生成。此命令允许通过指定块内的块位置将块添加到内存，通过指定块内的位置删除加载到内存的块，以及删除所有块的能力
当前已通过此命令加载到服务器内存中（removeall）。此外，还可以设置将块加载到内存中的持续时间
会自动消失；默认设置为 -1 意味着块将保持加载状态，直到再次使用 chunkload 命令
将其从内存中删除。
</p><p><b>这不会创建或删除新的或已经生成的地形块，它只是将其带入服务器的内存中，以便</b>
无论周围是否有人，NPC 都可能生成 <b></b></p><p><b>示例</b>
</p>
<pre>- chunkload add location:1000,64,1000,world duration:-1s
- chunkload add location:323,4,745,creative_world duration:10m
- chunkload remove location: 1000,64,1000,world
- chunkload removeall
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="execute">执行</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">执行
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[as_player|as_op|as_npc|as_server] ["Bukkit command"]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">代表玩家 (as_player)、玩家作为操作员 (as_op)、NPC 作为操作员 (as_npc) 或服务器 (as_server) 执行 Bukkit 命令。
<p>您可以在服务器控制台或带斜杠的聊天中使用的任何 Bukkit 命令都可以在此处使用。因此，您可以使用执行命令来使 NPCs 充当其他插件的接口。
</p><p><br/>
<b>示例</b>
</p>
<pre>- execute as_player "home"
- execute as_op "gamemode 1"
- execute as_npc "spawnmob zombie 3"
- execute as_server "jail &lt;player.name&gt;"
</pre>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="World">世界</h3></div></s></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="animatechest">动画测试</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">动画测试
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world] ({open}|close) (sound:{true}|false)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使位于指定坐标的箱子以打开或关闭的动画显示；如果不指定则默认打开。允许动画宝箱播放“打开宝箱”的声音（true）或静静地打开（false）；默认为 true。 <b>该坐标处必须有一个箱子，此命令不会生成箱子。</b>
<p><b>示例</b>
</p>
<pre>- animatechest location:1000,63,1000,world open sound:true
- animatechest location:100,74,777,world close sound:false
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="copyblock">复制块</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">复制块
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world] [to:x,y,z,world]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">只需复制一个位置上的任何类型的块，然后将其粘贴到另一个定义的位置即可。
<p><b>示例</b>
</p>
<pre>- copyblock location:204,68,12,world to:55,64,100,castle_world
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="displayitem">显示项</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">显示项
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[item_name|remove] [location:x,y,z,world] (duration:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">服务器是否在指定位置创建一个“虚拟物品”，该物品将保留在那里直到被删除。幻影物品
<p>只出现在玩家面前，不能被玩家拾取。目前“持续时间：#”设置不可靠，因此 
如果玩家希望删除显示的项目，他们应该预期必须使用“-displayitem remove”命令。
</p><p><b>示例</b>
</p>
<pre>- displayitem 10 location:77,64,2453,world duration:20s
- displayitem Stick location:&lt;player.location&gt;
- displayitem remove location:77,64,2453,world
- displayitem remove location:&lt;player.location&gt;
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="drop">掉落</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">掉落
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[item:#(:#)|item:material(:#)|xp] (qty:#{1}) (location:x,y,z,world)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">在某个位置掉落一定数量的物品或经验（如果未指定，则为 1）。您可以选择项目的 ID 或其材质。找到所有块和项目 ID <a class="external text" href="http://www.minecraftwiki.net/wiki/Data_values" rel="nofollow">这里</a> 并找到所有有效的材料名称 <a class="external text" href="http://jd.bukkit.org/rb/apidocs/org/bukkit/Material.html" rel="nofollow">这里</a>.
<p>ID 或材料后面还可以带有该物品的 <a class="external text" href="http://www.minecraftwiki.net/wiki/Data_values#Data" rel="nofollow">特殊数据值</a>，因此您可以（例如）掉落特定种类的木材或颜色的羊毛。</p><p><b>示例</b>
</p>
<pre>- drop item:38 location:500,63,500,world
- drop item:diamond qty:5 location:&lt;anchor:Treasury&gt;
- drop xp qty:30 location:&lt;anchor:Altar&gt;
- drop item:wood:3 qty:30 location:&lt;anchor:Jungle&gt;
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="strike">罢工</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">罢工
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">(no_damage) [location:x,y,z,world]
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">使闪电击中某个位置，可以选择不造成任何损坏。
<p><br/>
<b>示例</b>
</p>
<pre>- strike location:200,73,200,world
- strike location:&lt;player.location&gt;
- strike no_damage location:&lt;anchor:Mountaintop&gt;
</pre>
</td></tr></tbody>
<p></p>
<p><s><div style="display: none;"></div></s></p>
<div class="mw-heading mw-heading4"><h4 id="switch">开关</h4></div>
<p></p>
<p><s><table class="wikitable" style="font-family:courier-new; font-size:1.1em;" width="100%"></table></s></p>
<tbody><tr>
<th align="center" scope="col">开关
</th>
<th align="left" scope="col" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2em;" width="90%">[location:x,y,z,world] (state:[{toggle}|on|off]) (duration:#)
</th></tr>
<tr>
<td colspan="2" style="padding-top:1.5em; padding-bottom:1.5em; padding-left:2.2em; padding-right:2.2em;">改变指定位置的杠杆、石按钮、石板、木板、木门、铁门或活板门的状态。默认情况下，状态从打开/打开切换到关闭/关闭，然后再返回，但您可以选择将状态设置为打开或关闭。您还可以指定状态保持这种状态的持续时间。
<p><br/>
<b>示例</b>
</p>
<pre>- switch location:500,45,700,world
- switch state:on location:&lt;anchor:Secret Lever&gt; duration:30
</pre>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Creating_your_own_Denizen_command">创建您自己的 Denizen 命令</h1></div></s></p>
<p>~~Aufdemrand为0.9版本的Denizen做了一个关于如何为denizen创建新命令的教程。
在这里查看：<a href="https://www.youtube.com/watch?v=Sd7zoWT24Xw">Denizen 0.9 命令教程</a>.~~</p>

