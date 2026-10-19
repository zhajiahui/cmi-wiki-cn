---
title: Depenizen / 标签清单
source_url: https://wiki.citizensnpcs.co/Depenizen/Tag-List
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5389
---


<a id="top"></a>

# Depenizen / 标签清单

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="BattleNight"></a><h1 id="battlenight">战斗之夜</h1>
<div class="highlight"><pre>	&lt;player.bn.class&gt;						-&gt; Name of player's chosen battle class
	&lt;player.bn.inbattle&gt;					-&gt; True/false is player in a battle?

	&lt;battle.arena&gt;							-&gt; Name of arena current battle is taking place in
	&lt;battle.inprogress&gt;						-&gt; True/false is a battle taking place?
	&lt;battle.timeremaining&gt;					-&gt; Time remaining for current battle to end
</pre></div>
<a id="Factions"></a><h1 id="factions">派系</h1>
<div class="highlight"><pre>	&lt;player.faction&gt; 						-&gt; The player's faction, as a dFaction

    // Note the 's' in 'factions' for these tags!
	&lt;player.factions.role&gt; 		            -&gt; Role of player within their faction
	&lt;player.factions.title&gt; 			    -&gt; Title of player within their faction
	&lt;player.factions.power&gt; 				-&gt; Player's power

	&lt;faction@facName.balance&gt; 			    -&gt; Balance of specified faction
	&lt;faction@facName.home&gt; 				    -&gt; Location of specified factions's spawn point
	&lt;faction@facName.isopen&gt; 			    -&gt; True/false is specified faction open?
	&lt;faction@facName.ispeaceful&gt; 		    -&gt; True/false is specified faction peaceful?
	&lt;faction@facName.ispermanent&gt;           -&gt; True/false is specified faction permanent?
	&lt;faction@facName.leader&gt; 		    	-&gt; Name of specified faction's leader
	&lt;faction@facName.playercount&gt; 	        -&gt; Amount of players within specified faction
	&lt;faction@facName.power&gt; 			    -&gt; Amount of specified faction's power
	&lt;faction@facName.relation[&lt;faction&gt;]&gt;	-&gt; Evaluates to enemies, allies, or neutral with another faction
	&lt;faction@facName.size&gt; 			        -&gt; Amount of land specified faction has claimed
</pre></div>
<a id="mcMMO"></a><h1 id="mcmmo">多网络MMO</h1>
<div class="highlight"><pre>	&lt;player.mcmmo.level&gt;					-&gt; Overall skill level of player
	&lt;player.mcmmo.level[&lt;skill&gt;]&gt;			-&gt; Skill level of a specific skill
	&lt;player.mcmmo.party&gt;					-&gt; Name of player's party
	&lt;player.mcmmo.rank&gt;						-&gt; Overall mctop player ranking
	&lt;player.mcmmo.rank[&lt;skill&gt;]&gt;			-&gt; Rank of player in a specific skill
	&lt;player.mcmmo.xp[&lt;skill&gt;]&gt;				-&gt; Amount of player's xp for a skill
	&lt;player.mcmmo.xp[&lt;skill&gt;].tonextlevel&gt;	-&gt; XP required for player to advance to skill's next level

	&lt;party[party_name].leader&gt;				-&gt; Name of the specified party's leader
    &lt;party[&lt;party&gt;].playercount&gt;            -&gt; The number of players in the specified party

</pre></div>
<a id="Towny"></a><h1 id="towny">镇</h1>
<div class="highlight"><pre>	&lt;player.town&gt; 							-&gt; The player's town, as a dTown
    &lt;player.nation&gt; 						-&gt; The player's nation, as a dNation

	&lt;town@townName.balance&gt; 				-&gt; Balance of specified town
	&lt;town@townName.board&gt; 				    -&gt; Board message of specified town
	&lt;town@townName.isopen&gt; 				    -&gt; True/false is specified town open?
	&lt;town@townName.ispublic&gt; 				-&gt; True/false is specified town public?
	&lt;town@townName.mayor&gt;                   -&gt; Name of specified town's mayor
	&lt;town@townName.nation&gt; 				    -&gt; Nation specified town belongs to
	&lt;town@townName.playercount&gt; 			-&gt; Population size of specified town
	&lt;town@townName.size&gt; 					-&gt; Amount of land specified town has claimed
	&lt;town@townName.spawn&gt; 			    	-&gt; Location of specified town's spawn point
	&lt;town@townName.tag&gt; 					-&gt; Tag of specified town
	&lt;town@townName.taxes&gt; 			    	-&gt; Tax amount of specified town

	&lt;nation@natName.balance&gt; 				-&gt; Balance of specified nation
	&lt;nation@natName.capital&gt; 				-&gt; Name of specified nation's capital town
	&lt;nation@natName.king&gt; 			    	-&gt; Name of specified nation's king
	&lt;nation@natName.isneutral&gt; 		    	-&gt; True/false is nation neutral?
	&lt;nation@natName.playercount&gt; 			-&gt; Amount of players within specified nation
	&lt;nation@natName.relation[&lt;nation&gt;]&gt;	    -&gt; Evaluates to enemies, allies, or neutral with another nation
	&lt;nation@natName.tag&gt; 					-&gt; Tag of specified nation
	&lt;nation@natName.taxes&gt; 			    	-&gt; Tax amount of specified nation
	&lt;nation@natName.towncount&gt; 		    	-&gt; Amount of towns within specified nation

	&lt;l@location.town&gt;		                -&gt; Town that has claimed specified location

</pre></div>
<a id="Jobs"></a><h1 id="jobs">工作机会</h1>
<div class="highlight"><pre>    &lt;player.jobs[&lt;jobName&gt;]&gt;                -&gt; The dJob of that player's specified job
    &lt;player.jobs[&lt;jobName&gt;].xp&gt;             -&gt; Current XP of the player in a certain job
    &lt;player.jobs[&lt;jobName&gt;].xp.max&gt;         -&gt; The maximum XP the player can have in a certain job
    &lt;player.jobs[&lt;jobName&gt;].xp.level&gt;       -&gt; Current level for a certain job

    &lt;job@jobName.description&gt;               -&gt; Job description
    &lt;job@jobName.name&gt;                      -&gt; The name of a job
    &lt;job@jobName.name.short&gt;                -&gt; The shortened name of a job
    &lt;job@jobName.color&gt;                     -&gt; The name of the chat color of the job
</pre></div>

