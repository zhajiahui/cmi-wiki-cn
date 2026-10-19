---
title: Denizen / 附加特征
source_url: https://wiki.citizensnpcs.co/Denizen/Additional_Traits
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5358
---


<a id="top"></a>

# Denizen / 附加特征

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>~~您可以通过启用各种特征来添加更多 Denizen 功能。~~</p>
<p>~~只需选择NPC并执行doing即可添加特征~~</p>
<p><s><pre>/trait &lt;traitname&gt;</pre></s></p>
<p>~~EG~~</p>
<p><s><pre>/trait mobprox</pre></s></p>
<p>~~并再次使用相同的命令删除它们~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Mobprox_Trait">Mobprox特征</h1></div></s></p>
<p>~~Mobprox 是“Mob Proximity”的缩写。它启用了 <a href="http://wiki.citizensnpcs.com/Denizen/Triggers#Proximity_Trigger">接近触发</a>-like 功能，但针对的是小怪而不是玩家。</p>
<p>当分配特征时，假设NPC分配了一个Denizen脚本。~~</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Actions">Mobprox 行动</h2></div></s></p>
<p>~~ mobprox 特征将在 Denizen script: 上触发以下操作 ~~</p>
<p><s><pre>on mob enter proximity:
on mob exit proximity:
on mob move proximity:
on &lt;mobname&gt; enter proximity:
on &lt;mobname&gt; exit proximity:
on &lt;mobname&gt; move proximity:
</pre></s></p>
<p>每当 <strong>任何</strong> 生物执行该动作时，~~"mob" 动作就会触发。</p>
<p>每当 <strong>特定的生物</strong> 执行操作时，&lt;mobname&gt; 操作就会触发。</p>
<p>&lt;mobname&gt;是生物的名字，EG“僵尸”或“苦力怕”。</p>
<p>当生物进入范围时，“进入”动作就会触发。如果怪物走出去又回来，它会再次开火。</p>
<p>当生物离开范围时，“退出”动作就会触发。如果怪物进出，它会再次开火。</p>
<p>每当生物处于范围内并继续处于范围内时，“移动”动作就会触发。这并不一定意味着生物真的搬走了。</p>
<p>请注意，这些操作不会立即运行，最多可能需要 2 秒才能调用。 （通常会快一点）</p>
<p>另请注意，如果范围内有多个实体，有时会几乎同时调用多个操作。~~</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Tags">Mobprox标签</h2></div></s></p>
<p>~~在每个操作中，您可以使用 <a href="http://wiki.citizensnpcs.com/Denizen/Replaceable_Tags">可更换标签</a> "&lt;context.entity&gt;" （包含 &lt;&gt; 后，不需要引号）来引用相关生物。</p>
<p>您可以使用标签通过 if 命令检查匹配的详细信息，例如~~</p>
<p><s><pre>- if &lt;context.entity.entity_type&gt; == "creeper" CommandHere
</pre></s></p>
<p>~~或类似的。</p>
<p>对于 mobprox 特征非常有用的一个标签是 <entity.can_see[&lt;entity&gt;]> - 你可以用这个通过doing:检查实体是否对NPC可见~~</entity.can_see[&lt;entity&gt;]></p>
<p><s><pre>- if &lt;npc.can_see[&lt;context.entity&gt;]&gt; CommandHere
</pre></s></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Flags">Mobprox 标志</h2></div></s></p>
<p>~~此外，您可以使用 NPC flags: 修改 mobprox 行为</p>
<p>MobProx 范围：~~</p>
<p><s><ul><li>标志名称为“mobprox_range”</li></ul></s></p>
<li>默认设置为 10</li>
<li>可以是任意整数，但建议不要超过 100</li>
<li>请记住，这是立方范围，而不是球面范围。意思是，如果范围是 10，并且生物在左边 9 个方块和前面 9 个方块，它仍然被认为在范围内。</li>
<p></p>
<p>~~是否接受NPC小怪作为mobprox triggers:~~</p>
<p><s><ul><li>标志名称为“mobprox_acceptnpcs”</li></ul></s></p>
<li>默认设置为 false</li>
<li>可以是真的也可以是假的。 true 表示 NPC 生物或真实生物会触发 mobprox 动作， false 表示只有真正的非 NPC 生物才会触发 mobprox 动作。</li>
<li>请记住，如果您希望 NPCs 在它们靠近时进行交互，有比 mobprox 操作更好的方法。仅当您希望 NPC 生物与真实生物完全相同时才将其设置为 true。</li>
<p></p>
<p>~~MobProx行动火timing:~~</p>
<p><s><ul><li>标志名称是“mobprox_timer”</li></ul></s></p>
<li>默认设置为 4</li>
<li>可以是任何整数，但建议在 1 到 10 之间。</li>
<li>请记住，1 表示每半秒开火一次，2 表示每秒开火一次，4 表示每两秒开火一次，依此类推。</li>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Example">Mobprox 示例</h2></div></s></p>
<p>~~例如，创建一个 NPC 并使用“/npc allocate --set mobproxexample”分配下面的脚本，然后使用“/trait mobprox”启用该特征~~</p>
<p><s><pre>'mobproxexample':
    type: assignment
    actions:
        on assignment:
        - flag npc mobprox_range:20
        - flag npc mobprox_acceptnpcs:false
        - trigger name:click state:true
        on mob enter proximity:
        - if &lt;context.entity.entity_type&gt; != "creeper" {
          - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Here's a mob! It's a &lt;context.entity.entity_type&gt;!"
          - if &lt;context.entity.can_see[&lt;npc&gt;]&gt; == false
            announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; I can't see it though &lt;&amp;co&gt;("
          }
        on mob exit proximity:
        - if &lt;context.entity.entity_type&gt; != "creeper"
          announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Goodbye, &lt;context.entity.entity_type&gt;!"
        on creeper enter proximity:
        - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Aahh! Creeper! Die creeper!"
        on creeper exit proximity:
        - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Oh good, the creeper's gone!"
        on creeper move proximity:
        # Note: don't use player-type npc. or player. can_see, always use context.entity.can_see
        # Due to a bug in Bukkit
        - if &lt;context.entity.can_see[&lt;npc&gt;]&gt; == true {
          - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; I cast lightning on you, creeper!"
          - strike &lt;context.entity.location&gt;
          }
    interact scripts:
    - 10 mobproxexample_interact

mobproxexample_interact:
    type: interact
    steps:
        1:
            click trigger:
                script:
                - chat target:&lt;player&gt; "Hello, I'm a mob researcher! I'm looking for interesting mobs to classify!"
                - chat target:&lt;player&gt; "But I'm deathly afraid of creepers! Luckily a wizard taught me a spell to cast lightning!"</pre></s></p>
<p>mobproxexample_interact:
    type: 互动
    steps:
        1：
            点击trigger:
                script:
                - 聊天 target:&lt;player&gt; “你好，我是一名生物研究员！我正在寻找有趣的生物进行分类！”
                - 聊天 target:&lt;player&gt; “但我非常害怕苦力怕！幸运的是，一个巫师教了我一个施展闪电的咒语！”</p>

