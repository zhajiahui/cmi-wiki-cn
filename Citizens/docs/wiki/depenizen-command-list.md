---
title: Depenizen / 命令清单
source_url: https://wiki.citizensnpcs.co/Depenizen/Command-List
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5388
---


<a id="top"></a>

# Depenizen / 命令清单

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>注意：从 0.8 开始，所有 Denizen 命令都允许 player:&lt;name&gt; 和/或 npc:&lt;id&gt; 参数。</p>
<a id="BattleNight"></a><h1 id="battlenight">战斗之夜</h1>
<div class="highlight"><pre>	- bn add
	- bn kick
	- bn start
	- bn end
</pre></div>
<a id="mcMMO"></a><h1 id="mcmmo">多网络MMO</h1>
<div class="highlight"><pre>	- mcmmo add [levels/xp] (skill:&lt;skill&gt;) (party:&lt;party&gt;)
	- mcmmo remove [levels/xp] (skill:&lt;skill&gt;) (party:&lt;party&gt;)
	- mcmmo set [levels/xp/xprate/vampirism/hardcore/leader] (skill:&lt;skill&gt;) (party:&lt;party&gt;) (state:{toggle}/true/false)
</pre></div>
<a id="Towny"></a><h1 id="towny">镇</h1>
<div class="highlight"><pre>	- towny add [resident/money/town/nation/townblock/bonus/plot/outpost] (&lt;town&gt;) (&lt;location&gt;) (&lt;nation&gt;) (qty:&lt;#&gt;)
	- towny remove [resident/money/town/nation/townblock/plot/outpost] (&lt;town&gt;) (&lt;location&gt;) (&lt;nation&gt;) (qty:&lt;#&gt;)
	- towny set [name:&lt;name&gt;/capital/open/public/mayor/surname/title/rank/board/war/maxsize/taxes/tag/spawn/perm/relation] (state:{toggle}/true/false) (&lt;town&gt;) (&lt;nation&gt;)
</pre></div>
<a id="Jobs"></a><h1 id="jobs">工作机会</h1>
<div class="highlight"><pre>	- jobs promote [&lt;job&gt;] [&lt;#&gt;]
	- jobs demote [&lt;job&gt;] [&lt;#&gt;]
	- jobs join [&lt;job&gt;]
	- jobs quit [&lt;job&gt;]
</pre></div>

