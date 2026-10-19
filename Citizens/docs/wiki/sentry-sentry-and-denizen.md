---
title: Sentry / Sentry 与 Denizen
source_url: https://wiki.citizensnpcs.co/Sentry/Sentry_and_Denizen
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5411
---


<a id="top"></a>

# Sentry / Sentry 与 Denizen

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><a href="sentry.md" title="Sentry">Sentry</a> 旨在与 Denizen 结合使用，以实现高级交互和脚本编写。</p>
<a id="Scripted_Death"></a><h2 id="scripted-death">脚本化的死亡</h2>
<a id="Interact_Triggers"></a><h3 id="interact-triggers">互动触发器</h3>
<p>Sentry 向 <a href="denizen.md" title="Denizen">Denizen</a> 添加了 2 个新触发器、2 个新命令和多个操作，可与 Sentry-Denizens 一起使用。</p>
<p>Npc死亡触发器</p>
<p>Npcdeath 触发器的工作原理与任何其他 <a href="denizen.md" title="Denizen">Denizen</a> 触发器类似。当 Sentry-Denizen 受到足够的伤害来杀死它时，它会被调用。触发器将为参与杀死 NPC 的每个玩家运行一次，因为它最后一次处于完全健康状态。如果 NPC 死于小怪或环境，则脚本将不会运行。</p>
<p>Npcdeathowner 触发器</p>
<p>当 NPC 死亡时，也会调用 Npcdeathowner 触发器，但如果所有者是在线玩家，则在 NPC 的所有者上运行触发器。无论死亡原因是什么，都会执行此操作。</p>
<p><strong>以下命令之一应始终是死亡触发器的最后一步。否则Sentry-Denizen将停止做任何事情，陷入不死状态。</strong></p>
<a id="Commands"></a><h3 id="commands">命令</h3>
<p>模具命令</p>
<p>当您的脚本完成后调用此函数来完成 Sentry-Denizen 并使其消失。
注意：在非哨兵 Denizen 上调用 DIE 命令可能会引发错误。</p>
<p>实时命令</p>
<p>调用此函数可将 Sentry-Denizen 重置为正常的 Sentry 活动。对于战斗中的演讲和“Boss 阶段”很有用。这不会治愈 Sentry，它将保留其致命一击之前的生命值。如果需要，请使用 Denizen HEAL DENIZEN 命令。</p>
<p>使用 LIVE PEACE 也会导致 NPC 放弃其当前目标。</p>
<p>注意：在非哨兵 Denizen 上调用 LIVE 命令可能会引发错误。</p>
<p>这是 Npcdeath Trigger 和 DIE 的完整示例。</p>
<table class="wikitable collapsible collapsed">
<tbody><tr>
<th>NpcDeath 触发器和 DIE 命令示例脚本。
</th></tr>
<tr>
<td><pre>

GuardDeath: 
  Type: Interact
  Requirements: 
    Mode: None 
    List:
  Steps: 
    1: 
      Npcdeath Trigger: 
        script:
          - CHAT "ARARRRRRGRGGRRH!"   
          - DROP DIAMOND
          - DIE
</pre>
</td></tr></tbody></table>
<a id="Actions"></a><h3 id="actions">行动</h3>
<p>Sentry 提供以下可简称为 scripts: 的 Action</p>
<ul>
<li>死亡时</li>
<li>实体死亡</li>
<li>玩家死亡时</li>
<li>因故死亡</li>
<li>其中 CAUSE 为 <a href="http://jd.bukkit.org/rb/apidocs/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html#enum_constant_detail%7Cany">损坏原因</a>（i.e。死于熔岩）</li>
<li>关于死亡 by LIVINGENTITY</li>
<li>其中 LIVINGENTITY 是实体类型的名称（即 被僵尸死亡）</li>
</ul>
<a id="Criminal_System"></a><h2 id="criminal-system">刑事系统</h2>
<p>几个<a href="multiple-traits.md" title="Multiple Traits">Sentry-居民</a>就可以用来创建城镇犯罪系统。</p>
<p>假设你有一个冒险服务器，有一个名为 <strong>山坡</strong> 的城镇，里面有店主、守卫、铁匠等。</p>
<p>创建一些 Sentry-居民来充当您城镇的警察部队。将每个 Sentry 设置为目标名为 Hillside_Enemy 的 <a href="#top">GROUP</a>。</p>
<p>现在创建一个 <a href="denizen.md" title="Denizen">Denizen</a> 脚本来处理玩家的攻击行为。让我们使用 3 击系统。这个相同的脚本将对其分配到的所有 NPCs 执行，并且每个玩家的步骤都是相同的，因此我们可以使用 1 个具有多个步骤的脚本，每个罢工一个。这是一个例子：</p>
<p>脚本因与当前 Denizen 不兼容而被删除</p>
<p>您可以看到我们已将脚本“Hillside_Aggression”分配给所有名为城镇守卫、店主鲍勃或史蒂夫市长的 NPCs。</p>
<p>如果玩家攻击其中任何一个 NPCs，他们将收到警告消息并继续下一步，如果他们到达步骤 3，他们将被放入 Sentry 敌对组织 Hillside_Enemy。</p>
<p>：奖励：如果店主和市长也被设置为哨兵，他们会保卫自己！ （关闭报复，这样他们就不会立即攻击）</p>
<p>最后一步将脚本重置为步骤 1，但只要玩家是 Hillside_Enemy 的成员，脚本就不会运行。</p>
<p>这只是一个基本示例，可以通过多种方式进行扩展，使用 <a href="denizen.md" title="Denizen">Denizen</a> 中的命令您可以：</p>
<ul>
<li>一段时间后原谅玩家（将玩家从hillside_enemy组中删除）</li>
</ul>
<p>: : （您可以使用 PEX 持续时间选项自动执行此操作）</p>
<ul>
<li>
<p>为玩家创建一个赢得宽恕的任务。</p>
</li>
<li>
<p>如果希尔赛德的骚扰继续下去，就会在其他城镇制造敌意。</p>
</li>
<li>
<p>等等等等</p>
</li>
</ul>
<a id="Hire-able_Bodyguards"></a><h2 id="hire-able-bodyguards">可雇佣保镖</h2>
<p>所以你在你的生存服务器上被踢了，把一些来之不易的绿宝石花在一个会为你守护你的家伙身上不是很好吗？现在你可以了！</p>
<p>让我们看看如何使用<a href="denizen.md" title="Denizen">Denizen</a>来制作可雇佣的保镖。</p>
<p><strong>对于 Denizen 0.9 版本，请参阅此 <a href="http://scripts.citizensnpcs.co/view/ta8m4c">http://scripts.citizensnpcs.co/view/ta8m4c</a></strong></p>
<p>这里我们有一个名为“雇佣兵领袖”的 NPC。把他安置在方便的地方。根据您服务器的权限系统，您可能需要假装雇佣兵首领是玩家，并授予他访问 /npc 和 /sentry 命令的权限。 （需要测试）</p>
<p>在这个简单的例子中，我们给了他一个脚本，要求玩家有 500 经济货币。我们还给了他一个默认文本，告诉玩家当他有更多的时候再回来。您可以使用另一个脚本对此进行扩展，但目前已经足够了。</p>
<p>如果玩家有钱，当他右键点击时，雇佣兵会问他是否需要保镖。如果玩家回答是。 NPC 将使用服务器命令创建 Sentry 并将其分配给玩家。在这个例子中，Sentry的重生设置为-1，这意味着如果保镖死了，它就永远死了，玩家需要再买一个。</p>
<p>这就是全部内容了。您可以在许多 ways: 中对此进行扩展</p>
<ul>
<li>创建“模板”哨兵并使用 /npc 副本创建保镖，而不是从头开始构建新的 npc。</li>
<li>具有更好统计数据的保镖的价格更高。</li>
<li>限制玩家一次只能有一名后卫。</li>
<li>提供远程或近战守卫。</li>
<li>将保镖也设置为<a href="denizen.md" title="Denizen">Denizen</a>并响应玩家命令。 （将名称更改为通用名称，以便您可以预先分配脚本）</li>
</ul>
<p>需要注意的是，Denizen 脚本是以玩家为中心的。 Sentry-Denizen会记住所有对其死亡做出贡献的玩家。将为每个玩家运行一个单独的脚本。因此，最好不要像示例中那样使用 DROP 命令，因为这会为每个玩家掉落 1 颗钻石。使用 GIVE 命令，每个玩家将直接收到奖励。</p>
<p>这又是一个简单的例子，但可能是 expanded:</p>
<ul>
<li>使用FLAG或FINISH命令来统计玩家杀死这个NPC的次数</li>
<li>在需要多名玩家击倒的任务开始时生成一个超级强悍的首领 NPC。每个玩家都可以因帮助杀死它而被标记。</li>
<li>当 NPC 死亡时，为玩家提供重要的任务提示。</li>
<li>重新审视 <a href="#Criminal_System">#刑事系统</a> 示例并对谋杀进行惩罚。</li>
</ul>

