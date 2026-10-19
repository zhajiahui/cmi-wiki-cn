---
title: Denizen / 触发器
source_url: https://wiki.citizensnpcs.co/Denizen/Triggers
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5223
---


<a id="top"></a>

# Denizen / 触发器

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>~~触发器允许NPCs对玩家的动作做出反应，例如与NPC聊天，点击NPC，攻击NPC，或者只是在NPC附近行走。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="How_To_Make_A_trigger">如何制作触发器</h1></div></s></p>
<p>~~首先，必须启用trigger:</p>
<p>您只需运行以下命令即可启用它们命令<a href="denizen-commands.md#trigger">- 触发</a>~~</p>
<p><s><pre>- trigger [name:chat/click/damage/proximity] (state:true/false) (cooldown:&lt;#.#&gt;) (radius:&lt;#&gt;)</pre></s></p>
<p>~~这通常在 <a href="denizen-types-of-scripts.md#Assignment_Script">作业脚本 - 作业时</a> 中完成，但也可以在其他任何地方完成。</p>
<p>然后您必须制作一个 <a href="denizen-types-of-scripts.md#Interact_Scripts">交互脚本</a> 并包含触发器以进行反应。</p>
<p>您还可以使用分配脚本操作“点击时”、“进入接近时”和“退出接近时”。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Chat_Trigger">聊天触发器</h1></div></s></p>
<p>~~一个聊天触发器写成so:~~</p>
<p><s><pre>            chat Trigger:
                '1':
                    Trigger: "/Hello/ there npc!"
                    Script:
                    - CHAT "Hello, &lt;player.name&gt;!"
                '2':
                    Trigger: "/Bye/ npc!"
                    Script:
                    - CHAT "Goodbye, &lt;player.name&gt;!"
                '3':
                    Trigger: /REGEX:.+/
                    Script:
                    - CHAT "I don't know what &lt;player.chat_history&gt; is!"</pre></s></p>
<p>~~任何包含/Message/的消息都会激活触发器的该部分。</p>
<p>您还可以包括任何<a href="http://en.wikipedia.org/wiki/Regular_expression">正则表达式</a> 通过在其前面添加 REGEX:~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Click_Trigger">点击触发</h1></div></s></p>
<p><s><pre>            click Trigger:
                Script:
                - CHAT "Hehe, that tickles!"</pre></s></p>
<p>~~当玩家右键点击 NPC 时会发生点击触发器。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Damage_Trigger">伤害触发</h1></div></s></p>
<p><s><pre>            Damage Trigger:
                Script:
                - CHAT "Ow! That hurt, &lt;player.name&gt;!"</pre></s></p>
<p>~~当玩家右键点击 NPC 时会发生点击触发器。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Proximity_Trigger">接近触发</h1></div></s></p>
<p><s><pre>            Proximity Trigger:
                entry:
                    Script:
                    - CHAT "Hello there, &lt;player.name&gt;!
                exit:
                    Script:
                    - CHAT "Goodbye, &lt;player.name&gt;!"
                move:
                    Script:
                    - CHAT "This is optional and will spam you =D"
</pre></s></p>
<p>~~当玩家进入或离开 - 触发命令定义的半径时，接近会触发火灾。~~</p>

