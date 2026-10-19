---
title: Denizen / 0.7 / 任务脚本
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Task_Scripts
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5239
---


<a id="top"></a>

# Denizen / 0.7 / 任务脚本

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>任务脚本只是<a href="denizen-0.7-interact-scripts-commands.md" title="Denizen/0.7/Interact Scripts/Commands">脚本命令</a>的简单列表。它们可以通过 RUNTASK 命令、IF 命令或 TASK 活动来调用。它们对于创建在多个地方使用的一组命令非常有用。</p>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="General_layout">总体布局</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<pre>'Name of script':  
  Type: Task    
  Script:        
  - COMMAND1
  - COMMAND2
  - etc...
</pre>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="Using_the_RUNTASK_command">使用 RUNTASK 命令</h4></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>想象一下您想要检查多个来源的单个结果的场景。举例来说，您有多个“任务”，但它们都有相同的结果。您可以检查每个任务的完成情况，或者，您可以让所有任务调用任务脚本并进行检查。
</p>
<p>这是一个非常基本的示例，理论上可能非常复杂。想象力，呵呵！
</p>
<pre>'Apple Reward': 
  Type: Task    
  Script:       
  - NARRATE "You've received some APPLES. Nice!"
  - GIVE APPLE QTY:10
  - FINISH

'Apple Quest 1':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - -FINISHED Apple Reward
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT "Welcome to my house, have some apples!"
        - RUNTASK 'SCRIPT:Apple Reward'
  
'Apple Quest 2':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - -FINISHED Apple Reward
  Steps:
    '1':
      Click Trigger:
        Script:
        - CHAT "Welcome to my orchard, have some apples!"
        - RUNTASK 'SCRIPT:Apple Reward'
</pre>
<p></p>
<p><s><div class="mw-heading mw-heading4"><h4 id="Using_the_TASK_Activity">使用任务活动</h4></div></s></p>
<p>~~这是一个特殊情况，因为活动是在没有玩家的情况下进行的。因此，任何需要玩家的命令都不会在从活动调用的任务脚本中运行。
许多脚本命令都有 DENIZEN 修饰符，可以在 NPC 而不是玩家上运行命令，从 TASK 活动调用任务脚本时应始终使用这些命令。~~</p>
<p><s><pre>WalkHome: 
  Type: Task    
  Script:       
  - CHAT NOPLAYER "Welp.. time to head home!"
  - WALKTO BOOKMARK:Home

GoHomeActivity:
  Type: Activity
  Requirements:
    Mode: None
  Activities:
    List:
    - 1 TASK SCRIPT:WalkHome REPEATS:0
  </pre></s></p>
<p>回家活动：
  类型：活动
  要求：
    模式：无
  活动：
    清单：
    - 1 个任务脚本：WalkHome 重复次数：0
  </p>

