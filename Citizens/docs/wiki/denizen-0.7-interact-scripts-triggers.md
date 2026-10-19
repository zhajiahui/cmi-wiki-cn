---
title: Denizen / 0.7 / 交互脚本 / 触发器
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Triggers
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5402
---


<a id="top"></a>

# Denizen / 0.7 / 交互脚本 / 触发器

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>Denizen 触发器通过与居民交互触发。它们在 Interact 脚本的 Steps: 节点中定义。</p>
<a id="Trigger_Types"></a><h2 id="trigger-types">触发类型</h2>
<a id="Right_Click"></a><h3 id="right-click">右键点击</h3>
<ul>
<li>右键点击 Denizen 时，<strong>点击触发</strong> 会激活。</li>
</ul>
<div class="highlight"><pre>Click Trigger:
  Script:
  - CHAT "Teehee, that tickles!"
  - EMOTE "giggles"
</pre></div>
<a id="Attack_/_Left_Click"></a><h3 id="attack-left-click">攻击/左键点击</h3>
<ul>
<li>左键点击 Denizen 时，<strong>伤害触发</strong> 会激活。如果 Denizen 禁用了损坏触发器，则这将被视为点击触发器。</li>
</ul>
<div class="highlight"><pre>Damage Trigger:
  Script:
  - CHAT "OUCH, You'll pay for that!"
  - STRIKE &lt;PLAYER&gt;
</pre></div>
<a id="Proximity"></a><h3 id="proximity">邻近性</h3>
<ul>
<li>当玩家走近 Denizen 时，<strong>接近触发</strong> 就会激活。</li>
</ul>
<div class="highlight"><pre>Proximity Trigger:
  Script:
  - CHAT 'Eek! get away, you smell bad, &lt;PLAYER&gt;.'
</pre></div>
<a id="Chat"></a><h3 id="chat">聊天</h3>
<ul>
<li>当玩家与居民聊天时，<strong>聊天触发器</strong> 会激活。可配置范围内的玩家聊天将定向到 Denizen，而不是全局聊天。聊天也遵循配置设置。单个聊天触发条目可以处理多个单词，如下所示：</li>
</ul>
<div class="highlight"><pre>Chat Trigger:
  '1':
    Trigger: The word needed to /Trigger/ is inside slashes, this whole sentence will appear to be said by the player
    Script:
    - CHAT "Good to know!"
  '2':
    Trigger: A chat trigger can also catch on any word not otherwise caught using /*/. 
    Script:
    - CHAT "I don't know what you mean, &lt;PLAYER&gt;!"
</pre></div>
<a id="Locations"></a><h3 id="locations">地点</h3>
<ul>
<li>当玩家靠近 <a href="https://wiki.citizensnpcs.co/index.php?title=Location_Bookmark&amp;action=edit&amp;redlink=1" title="Location Bookmark (page does not exist)">位置书签</a> 时，<strong>位置触发</strong> 就会激活。与聊天触发器一样，可以在一个位置触发器中定义多个位置。它们在格式上与聊天触发器类似，因为每个触发器条目可以有多个位置。</li>
</ul>
<div class="highlight"><pre>Location Trigger:
  '1':
    Trigger: TreasureRoom
    Script:
    - TELEPORT BOOKMARK:Jail
  '2':
    Trigger: BedRoom
    Script:
    - NARRATE 'You enter the bedroom of the dead man, looking for clues'
</pre></div>
<a id="Player_Death"></a><h3 id="player-death">玩家死亡</h3>
<ul>
<li><strong>玩家死亡触发</strong> 当玩家死亡时激活。默认情况下禁用此触发器。触发器：节点可用于定义玩家必须死亡才能让 Denizen 看到的半径。如果触发器：设置为 -1，则 Denizen 将尝试处理当前世界上的任何玩家死亡。</li>
</ul>
<div class="highlight"><pre>  Playerdeath Trigger:
    Radius: 50
    Script:
    - SHOUT "HA HA! &lt;PLAYER&gt; died!"

</pre></div>
<p>有关命令的完整列表，请参阅 <a href="denizen-0.7-interact-scripts-commands.md" title="Denizen/0.7/Interact Scripts/Commands">命令</a></p>

