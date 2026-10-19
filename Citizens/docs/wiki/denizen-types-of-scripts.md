---
title: Denizen / 脚本类型
source_url: https://wiki.citizensnpcs.co/Denizen/Types_of_Scripts
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5222
---


<a id="top"></a>

# Denizen / 脚本类型

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>~~在Denizen中，有多种不同类型的脚本，每种脚本都有不同的用途。在编写脚本时，您将需要使用其中的几个，因此了解它们很重要！~~</p>
<p>~~（注意：页面正在建设中！还有很多内容不只是这里列出的！）~~</p>
<p>~~类型：交互、书籍、项目、实体、任务、作业、过程、世界、格式、库存~~</p>
<p>~~另外：此页面上的所有示例脚本都可以协同工作...~~</p>
<p>~~要查看它们全部工作，请将它们全部添加到您的服务器并将“MyAssignmentScript”分配给 NPC，然后右键点击它。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Assignment_Script">作业脚本</h1></div></s></p>
<p><s><pre>MyAssignmentScript:
    type: assignment
    actions:
        on assignment:
        - chat "I has been assigned!"
        - trigger name:proximity state:true</pre></s></p>
<p>~~分配脚本是任何 NPC 需要的第一个脚本 - 它列出了 NPC 所做的一切！</p>
<p>最重要的用途之一是“on assignment:”操作，该操作在将脚本分配给 NPC 时运行，您通常在其中启用触发器并运行其他重要命令。</p>
<p>您可以通过 adding: 链接交互脚本~~</p>
<p><s><pre>    Interact Scripts:
    - 10 MyInteractScript
</pre></s></p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Interact_Scripts">交互脚本</h1></div></s></p>
<p><s><pre>MyInteractScript:
    type: Interact
    Steps:
        '1':
            Proximity trigger:
                Entry:
                    Script:
                    - chat "Hi there, &lt;player.name&gt;!"
                    - run mytask
</pre></s></p>
<p>~~交互脚本控制当玩家触发接近、点击、聊天或伤害等触发器时 NPC 的操作。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Item_Scripts">项目脚本</h1></div></s></p>
<p><s><pre>myitem:
    type: item
    material: wool:3
    recipe:
    - air|air|air
    - dirt|wool|dirt
    - air|air|air
</pre></s></p>
<p>~~项目脚本保存自定义项目的数据。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="World_Scripts">世界脚本</h1></div></s></p>
<p><s><pre>formatybit:
  type: world
  events:
    on formattybit command:
    - narrate format:formatdemo "Hello, I'm a well-formatted narrate, caused by a world event '/formattybit' command!"
    - determine fulfilled
</pre></s></p>
<p>~~世界脚本运行世界事件。~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Task_Scripts">任务脚本</h1></div></s></p>
<p><s><pre>mytask:
    type: task
    script:
    - chat "Here, a book for you!"
    - give myfancybook
</pre></s></p>
<p>~~任务脚本包含由其他脚本使用命令 - run (taskscriptname) 运行的随机脚本~~</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Book_Scripts">书籍脚本</h1></div></s></p>
<p><s><pre>myfancybook:
    type: book
    title: My Fancy Book
    author: NotNotch
    text:
    - This is my book. There are many like it, but this one is mine!
    - Many &lt;n&gt;new &lt;n&gt; lines!
    - &lt;p&gt;Paragraphs, &lt;p&gt;too!
</pre></s></p>
<p>~~书籍脚本保存有关复杂书籍项目的信息。</p>
<p>text: 类别中的每一行都是一个新页面。</p>
<p>在脚本中定义一本书后，您可以使用 - Give (bookname)~~ 将其提供给任何可运行脚本中的玩家</p>
<p><s><div class="mw-heading mw-heading1"><h1 id="Format_Scripts">设置脚本格式</h1></div></s></p>
<p><s><pre>formatdemo:
  type: format
  format: "&lt;&amp;f&gt;[&lt;&amp;b&gt;Message&lt;&amp;f&gt;- &lt;&amp;2&gt;&lt;text&gt;&lt;&amp;f&gt;]"
</pre></s></p>
<p><s><div class="mw-heading mw-heading1"><h1 id="CommandScripts">命令脚本</h1></div></s></p>
<p><s><pre>my custom command:
  type: command
  name: formatbit
  script:
  - narrate format:formatdemo "Hello, I'm a well-formatted narrate, caused by a command script '/formatbit' command!"
</pre></s></p>
<p>~~世界脚本运行世界事件。~~</p>

