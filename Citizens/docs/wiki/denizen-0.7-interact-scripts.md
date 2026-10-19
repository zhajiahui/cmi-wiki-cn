---
title: Denizen / 0.7 / 交互脚本
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5238
---


<a id="top"></a>

# Denizen / 0.7 / 交互脚本

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Interact_Scripts">交互脚本</h2></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>脚本在plugins/Denizen/scripts/文件夹中定义。该目录中的任何 .yml 文件都将加载到 Denizen 中。出于本网站的示例目的，引用了 script.yml，但同样，jimbobjoe.yml 或“skeeter the cat.yml”也将起到相同的作用。
</p>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="General_layout_of_an_Interact_Script">Interact 脚本的总体布局</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>下面这个小 'outline' 显示了交互脚本的总体布局。请记住：对于 YML，间距非常重要。如果您在处理任何 YML 文件时在控制台中收到 <code>SnakeYML</code> 错误，则 99% 的情况是因为间距错误或缺少“:”冒号。 YAML 教程可能会令人生畏，但 Essentials wiki 上的 <a class="external text" href="http://ess.khhq.net/wiki/YAML_Tutorial" rel="nofollow">这个小教程</a> 对于基本 YAML 非常有用，这是 Denizens 使用的范围。</p>
<pre>'Name of script':   # Name Node
  Type: Interact    # Type Node
  Requirements:     # Requirements Node
    Mode: ...
    List: 
    - ...
    - ...
  Steps:            # Steps Node
   1:               # Step Node
    Some Trigger:   # Trigger Node
      Trigger: ...
      Script:     # Script Node
        - ...
        - ...
     Another Trigger:
      Script:
        - ...
        - ...
</pre>
<p>有关要求和步骤中内容的信息，请继续阅读。上面显示的只是正确间距的轮廓，而不是有效的脚本！让我们看一下下面的几个小脚本。
</p>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="A_few_small_scripts">一些小脚本</h4></div></s></p>
<p>~~...只是为了了解一些使用脚本的基本方法。本文档的其余部分将详细介绍每个部分的具体情况。所描述的某些功能可能需要额外阅读。</p>
<p>下面的脚本是留下提示的一个巧妙的小方法。当玩家靠近时，此脚本将触发 NPC 看着目标，同时与玩家进行简短的对话。~~</p>
<p><s><pre>"A Hint in the Sky":
  Type: Interact   
  Requirements:
    Mode: None
  Steps:
    1:
      Proximity Trigger:
        Script:
        - ^COOLDOWN 15
        - LOOK CLOSE
        - ^CHAT "Look up there! What could that possibly be used for?"
        - LOOK BOOKMARK:upthere DURATION:10
        - WAIT 1
        - CHAT "If only I could figure out how to make it, I can't find any stairs!"
</pre></s></p>
<p>~~下面是一个好人的脚本，他将在夜间帮助冒险家。请记住，交互脚本仅为 Denizen NPC... 玩家交互定义一组规则。想象一下下一个脚本与一些活动相结合，使 Denizen NPC 扩大范围并在某些树林中漫步。~~</p>
<p><s><pre>"Night-time Helper":
  Type: Interact
  Requirements:
    Mode: All
    List:
    - TIME NIGHT
  Steps:
    1:
      Click Trigger:
        Script:
        - ^ZAP DURATION:60
        - ENGAGE DURATION: 5
        - LOOK CLOSE DURATION:5
        - CHAT "It's dark out here, man!"
        - CHAT "You really gotta watch out for those Zombies... they're all over the place!"
    2:
      Click Trigger:
        Script:
        - ^COOLDOWN 3600
        - LOOK CLOSE DURATION:5
        - CHAT "You again, eh? Hey man.. you need some torches?"
        - WAIT 1
        - GIVE TORCH QTY:12
</pre></s></p>
<p>~~脚本还可以开始冒险的故事情节，所有这些都由脚本协同工作激活，这要归功于 FLAG、FAIL 和 FINISH 命令。下面这个小脚本可能是一个任务的开始，如果使用得当，会有两种不同的结果。~~</p>
<p><s><div class="mw-heading mw-heading4"><h4 id="Name_Node">名称节点</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>该节点非常不言自明，但这里有一些需要记住的事情。
</p>
<ul><li>名称，就像节点一样区分大小写！ <code>'This script name'</code> 与 <code>'THIS SCRIPT NAME'</code> 不同。</li>
<li>包含空格的名称应使用单引号或双引号引起来。即：<code>"This script":</code> 或 <code>'This script':</code> 是可以接受的。</li>
<li>如果名称中包含单引号，则必须在其周围使用双引号，或者 'escape' 将引号与另一个引号一起使用。即：<code>"John's Script":</code> 或 <code>'John''s Script':</code></li></ul>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="Type_Node">类型节点</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>让我们Denizen和您轻松了解脚本的类型。对于交互脚本，如本节所述，请使用 <code>TYPE: INTERACT</code>。作为参考，还有 TASK 脚本和 ACTIVITY 脚本，它们在相应的部分中进行了介绍。</p>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="Requirements_Node">需求节点</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>该节点设置玩家获得脚本资格的规则。使用需求时您应该了解几个不同的选项。对于例如：
</p>
<p><code>
</code></p>
<p><code></code></p>
<pre> Requirements:
   Mode: All
   List:
   - TIME Night
   - MONEY 1000000
   - STORMY
</pre>
<p><p><code></code>
</p><p>当然，这将是一个很难获得的脚本。触发的时间必须是晚上，玩家需要一百万单位的货币，而且天气必须是暴风雨，但这显示了需求的灵活性。首先是“模式”。目前有三种不同的类型。其次是需求类型，如果适用的话带有参数。</p>
<p></p><p><br/>
</p></p>
<div class="mw-heading mw-heading5"><h5 id="Requirements_Mode">需求模式</h5></div>
<div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p><code>[] indicates required field.</code>
</p>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="17%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:white; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>ALL
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">    要求满足列出的所有要求。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="17%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:white; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>任何#
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">    要求满足总要求中指定数量的要求。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="17%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:white; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>NONE
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">    无需满足任何要求。也没有必要有一个 <tt>LIST</tt> 节点如果使用 <tt>NONE</tt>.
 </div>
</td></tr></tbody></table>
</div>
</div>
<div class="mw-heading mw-heading5"><h5 id="Requirements">条件</h5></div>
<div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>Denizen 有各种各样的要求可供您使用。如需完整列表以及有关这些要求的信息，
参见：<a href="denizen-0.7-interact-scripts-interact-requirements.md" title="Denizen/0.7/Interact Scripts/Interact Requirements">Denizen/0.7/交互脚本/交互要求</a></p><p>请记住，插件程序员甚至您也可以轻松扩展需求！<br/>
参见：<a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Interact_Scripts/Custom_Interact_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Interact Scripts/Custom Interact Requirements (page does not exist)">Denizen/0.7/交互脚本/自定义交互要求</a></p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="Steps_Node">步骤节点</h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;">
<p>每个脚本可以有多个步骤，每个步骤都有多个触发器。玩家对于脚本只能进行 1 步。当选择运行脚本时，系统会查询 Denizen 保存的内容，以查看玩家是否已完成任何步骤。如果未找到条目，则玩家从步骤 1 开始。 
</p><p>下面是一个充分利用步骤的 s 脚本示例。请注意，ZAP 命令是将玩家从一步移动到下一步的命令，它不是自动的！
</p>
<pre>'Welcome to Harbortown':
  Type: Interact
  Requirements:
    Mode: NONE
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT "What's your name, stranger?"
      Chat Trigger:
        '1':
          Trigger: My name is /&lt;PLAYER&gt;/.
          Script:
          - CHAT "Ah ha, your name sounds familiar!"
          - CHAT "Are you from around this area?"
          - ZAP
    '2':
      Click Trigger:
        Script:
        - HINT
      Chat Trigger:
        '1':
          Trigger: /Yes/, I grew up in Harbortown!
          Script:
          - CHAT "I thought so, welcome back! 
            Have you heard about Tom the Taylor? 
            Isn't that just horrible?"
          - ZAP 3 
        '2':
          Trigger: /No/, you must be mistaken. 
          Script:
          - CHAT "Oh, sorry about that." 
          - CHAT "Hey, if you're looking for some work, 
            Bill the Baker is understaffed! 
            This is the bakery's busy season."
          - ZAP 4
    '3':
      Click Trigger:
        Script:
        - CHAT "I wonder if Tom the Taylor is doing any better."
        - NARRATE "Perhaps you should check on Tom the Taylor."
    '4':
      Click Trigger:
        Script:
        - CHAT "Oh, nice to see you again &lt;PLAYER&gt;!"
        - CHAT "Have you stopped by the bakery?"
</pre>
</div>
<ul><li>有关可用触发器的列表，请参阅 <a href="denizen-0.7-interact-scripts-triggers.md" title="Denizen/0.7/Interact Scripts/Triggers">触发器</a></li>
<li>有关可用命令的列表，请参阅 <a href="denizen-0.7-interact-scripts-commands.md" title="Denizen/0.7/Interact Scripts/Commands">命令</a></li></ul>
<div class="mw-heading mw-heading2"><h2 id="Assigning">分配</h2></div>
<p>见<a href="denizen-0.7-assignments.md#Interact_Assignment" title="Denizen/0.7/Assignments">Denizen/0.7/Assignments#Interact_Assignment</a></p>
<p><br/>
</p>
<p></p>

