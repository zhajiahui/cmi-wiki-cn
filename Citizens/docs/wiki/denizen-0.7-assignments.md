---
title: Denizen / 0.7 / 脚本分配
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Assignments
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5241
---


<a id="top"></a>

# Denizen / 0.7 / 脚本分配

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s><div style="font-family:museo-sans; font-size:110%;"></div></s></p>
<div class="mw-heading mw-heading2"><h2 id="Interact_Assignment">互动作业</h2></div>
<p>在 Denizen 可以运行脚本之前，需要先对其进行分配。 
</p>
<p>分配在 <b><code>plugins\Denizen\assignments.yml </code></b> 中定义</p>
<p>该 yaml 文件包含一个名为“Denizens”的节点，每个 Denizen 在该节点下都有自己的条目。
</p>
<p>作业必须手工完成。我们推荐一个好的文本编辑器，例如 [<a class="external text" href="http://notepad-plus-plus.org/" rel="nofollow">Notepad++</a>]</p>
<p>这是一个非常基本的示例，将单个 <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Interact_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/Interact Scripts (page does not exist)">交互脚本</a> 分配给名为 Steve 的 Denizen。</p>
<pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
</pre>
<p>让我们来分解一下。 
</p>
<p>如果您不熟悉 yaml，请首先阅读 <a href="yaml.md" title="YAML">这个</a>，然后注意“Interact Scripts：”包含 yaml <b>清单</b>。列表中的每个项目都带有前缀“-”。缩进和间距很重要。</p>
<p>此作业适用于名为 <code>'Steve'</code> 的居民。 <span style="background: white; color: red">Denizen NPC 名称区分大小写！</span> 涉及此 NPC 的触发器（例如 <code>'Click Trigger'</code>）现在将尝试调用名为 <code>'Daytime in the City'</code> 的脚本。</p>
<p>名称前面的 <code>10</code> 是 <b>脚本优先级</b>，在分配多个脚本时很有用。</p>
<p>如果您想将相同的脚本分配给另一个 NPC，您可以创建另一个条目，例如 this:
</p>
<pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
  'Bob':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
</pre>
<p>现在鲍勃和史蒂夫都分配了这个脚本。
</p>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Multiple_Scripts">多个脚本</h4></div>
<p>Denizens 动态的关键在于他们能够在不同情况下处理多个脚本。可以为居民分配多个具有不同要求的交互脚本，根据玩家、NPC 和世界条件改变他们的行为。
</p>
<p>重要的是要记住 that:
</p>
<p><b>对于与 Denizen 的每次交互：一个，并且仅选择运行一个脚本。</b>
</p>
<p>选择哪个脚本是基于几个 factors: 
</p>
<ul><li>每个脚本的<b><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Interact_Scripts/Interact_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/Interact Scripts/Interact Requirements (page does not exist)">条件</a></b></li>
<li>每个脚本作业的 <b>优先级</b></li>
<li><b>触发器</b> 是在该玩家的脚本活动步骤中定义的。 （高级用法参见<a href="#Overlay_Assignment_Mode">#Overlay分配模式</a>）</li></ul>
<p>现在忽略最后一项，该过程类似于 this:
</p>
<p>Denizen 引擎从最高优先级开始并向最低优先级努力，检查每个脚本的要求。
选择第一个找到的符合要求的脚本。
</p>
<p>让我们看一个例子。 
</p>
<pre>---- assignments.yml ----

Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 0 Regular Joe
    - 10 Joe the Builder  

---- script.yml ----

'Regular Joe':
  Type: Interact   
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - CHAT "Hello &lt;PLAYER&gt;! I supply builders only!"

'Joe the Builder':
  Type: Interact  
  Requirements:
    Mode: All
    List:
    - PERMISSION modifyworld.*
  Steps:
    1:
      Click Trigger:
        Script:
        - ENGAGE
        - CHAT "Hello &lt;PLAYER&gt; the Builder! Take this shovel!"
        - GIVE WOOD_SPADE QTY:1
        - FINISH
        - DISENGAGE
</pre>
<p>Denizen 现在已为 <code>Steve</code> 分配了两个脚本。在玩家交互时，将按照优先级降序检查两个脚本是否满足要求。由于“Regular Joe”脚本根本没有任何要求，因此它总是会在优先级较低的脚本之前被选中。这就是为什么您可以在本示例中看到我们将其优先级设置为 0。</p>
<p>如果两个脚本的优先级都是 0 怎么办？在这种情况下，将选择列表中出现的第一个脚本。最好为每个分配的脚本赋予不同的优先级，以避免任何混淆。
</p>
<div class="mw-heading mw-heading4"><h4 id="Overlay_Assignment_Mode">叠加分配模式</h4></div>
<p><span style="background: white; color: red">高级用法！</span> 覆盖脚本分配是 0.7 中的新增功能，通过多个脚本交互开启了一系列新的可能性。这是完全可选的，如果您是第一次使用，则可能应该忽略它，而当您开始掌握 Denizen 脚本时，请重新访问。</p>
<p>通常，无论是否存在实际匹配的触发器，都会选择运行需求匹配的脚本。如果玩家的活动步骤上不存在匹配的触发器，则不会发生任何事情或显示一些默认文本，具体取决于触发器的类型。
</p>
<p>通过覆盖分配，<b>定义的触发器成为选择要求的一部分。</b></p>
<p>分配有此选项的脚本将选择 <b>从不</b> 作为它无法处理的触发器类型。这样可以轻松添加仅处理一种触发器类型的脚本分配，而无需将其混搭到现有脚本中。</p>
<dl><dd><dl><dd>要将脚本指定为“叠加”，请将 ^ 直接放在脚本名称前面。</dd></dl></dd></dl>
<p>示例 time:
</p>
<pre>---- assignments.yml ----

Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 0 Proximity Joe
    - 10 ^Regular Joe
    - 20 ^Joe the Builder  

---- script.yml ----
'Proximity Joe':
  Type: Interact
  Requirements:
    Mode: None
  Steps:
    1:
      Proximity Trigger:
        Script:
        - CHAT "Nice to see you, &lt;PLAYER&gt;!"

'Regular Joe':
  Type: Interact  
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - CHAT "Hello &lt;PLAYER&gt;! I supply builders only!"

'Joe the Builder':
  Type: Trigger   
  Requirements:
    Mode: All
    List:
    - PERMISSION modifyworld.*
  Steps:
    1:
      Click Trigger:
        Script:
        - ENGAGE
        - CHAT "Hello &lt;PLAYER&gt; the Builder! Take this shovel!"
        - GIVE WOOD_SPADE QTY:1
        - FINISH
        - DISENGAGE
</pre>
<p>现在，上一个示例中的 2 个脚本将仅被选择用于“点击”交互，而新的 0 优先级脚本将被选择用于任何交互。 
</p>
<p>让我们看看在几个不同的场景中会发生什么。
</p>
<p><b>第一个场景</b>
假设玩家点击，没有权限“modifyworld.*”，因此只有两个脚本满足要求：“Regular Joe”和“Proximity Joe”。发生了什么应该是很明显的。 “Regular Joe”具有更高的优先级，因此点击触发器将使用该脚本。玩家将看到“玩家您好！我只提供建造者！”。这是唯一的触发因素，对吗？错误的。这将我们带入下一个场景。</p>
<p><b>第二个场景</b>
触发 Denizen NPC 的第一件事实际上是接近触发器。在常规分配情况下，在与第一个场景相同的权限情况下，“常规乔”将击败“邻近乔”，并且由于“常规乔”中没有邻近触发器，因此不会触发任何脚本。但这是一个叠加作业。由于脚本“Regular Joe”中没有接近触发器，因此下一个可用脚本“Proximity Joe”将尝试触发。我们这里有什么？接近触发！玩家会看到“很高兴见到你，玩家！”。</p>
<p><b>第三种情况</b>
玩家触发接近触发器。玩家拥有权限“modifyworld.*”，因此最高匹配的脚本是“Joe the Builder”，因为它的优先级为 30。但是该脚本没有接近触发器，因此检查行中的下一个脚本。当然，“普通乔”也没有接近触发器！由于“Joe the Builder”和“Regular Joe”都是叠加分配，我们回到“Proximity Joe”触发，提醒玩家“很高兴见到你，玩家！”。</p>
<p>您现在看到 Denizen 脚本引擎的可能性了吗？我喜欢它！
</p>
<p>简单的事情，对吧？为了让您的牙齿湿润，请看一下这个使用标志和魔法的附加示例情况:)
<a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Example_Scripts/Advanced_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/Example Scripts/Advanced Scripts (page does not exist)">高级脚本</a></p>
<p><br/>
</p>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="Default_Texts">默认文本</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>除了处理脚本分配之外，还可以在 assignments.yml 的 Denizens 节点中声明一些其他内容。在文本节点下，您可以定义单个聊天行，如果未找到匹配的脚本，将为 3 个核心触发器类型中的每一个显示该聊天行。点击、损坏和聊天。此外，当 Denizen 已投入使用或其交互冷却未完成时，可以定义一条消息。
</p>
<p>此处的设置将覆盖 <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/config.yml&amp;action=edit&amp;redlink=1" title="Denizen/config.yml (page does not exist)">Denizen/config.yml</a> 中针对此 Denizen 的默认设置。</p>
<pre>---- assignments.yml ----
Denizens: 
  Castle Guard: 
    Interact Scripts: 
      - 10 Guard Script
      - 20 Elite Guard
      - 30 Quest for Guard
    Texts: 
      No Click Trigger: Don't poke, me, &lt;PLAYER&gt;!
      No Damage Trigger: Ouch! you lookin' to get smacked?
      No Chat Trigger: Eh, what's that?
      Denizen Unavailable: I'm busy right now.
</pre>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Activity_Assignment">活动分配</h2></div></s></p>
<p>~~活动脚本分配给 Denizens 的方式与交互脚本非常相似。
这里的区别是对于每个脚本你必须指定一个时间来加载脚本。~~</p>
<p><s><pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
    Scheduled Activities:
    - 12:00 Wander_aimlessly
</pre></s></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Default_Activity">默认活动</h3></div></s></p>
<p>~~如果您计划只为 Denizen 进行一项活动，则可以使用“默认活动：”而不是使用调度程序。使用此功能时，活动设置为“Spawn”。您还可以使用调度程序，它将覆盖默认的活动~~</p>
<p><s><pre>---- assignments.yml ----
Denizens:                         
  'Steve':                        
    Interact Scripts:                      
    - 10 Daytime in the City  
    Scheduled Activities:
    - 12:00 Go_home
    Default Activity: Wander_Around
</pre></s></p>

