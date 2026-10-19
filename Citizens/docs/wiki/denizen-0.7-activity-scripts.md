---
title: Denizen / 0.7 / 活动脚本
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5242
---


<a id="top"></a>

# Denizen / 0.7 / 活动脚本

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>~~活动脚本包含一组活动。
活动是 Denizen 可以执行的连续操作，赋予其生命。流浪、收集小麦、开采区块，这些都是可能的活动~~</p>
<p><s><div class="mw-heading mw-heading4"><h4 id="General_layout_of_an_Activity_Script">活动脚本的总体布局</h4></div></s></p>
<p><s></s></p>
<pre>'Name of script':   # Name Node
  Type: Activity    # Type Node
  Requirements:     # Requirements Node
    Mode: ...
    List: 
    - ...
    - ...
  Activities:       # Activities Node
    List:
     - ...
     - ...
</pre>
<div class="mw-heading mw-heading2"><h2 id="About">关于</h2></div>
<p>活动脚本定义了 Denizen 可以同时执行的一组活动。
</p>
<p>每个活动都分配有一个目标优先级，该目标优先级指示在任何给定时间哪个活动将处于活动状态。如果某个 Activity 无法完成，则会使用下一个较低优先级的 Activity 来代替。
</p>
<p>活动脚本。
</p>
<pre>'Citizen':
  Type: Activity
  Requirements:
    Mode: None
  Activities:
    List:
    - 1 WANDER DELAY:12 RADIUS:10 SPEED:.75 FILTER:COBBLESTONE,GRAVEL,WOOL
</pre>
<div class="mw-heading mw-heading2"><h2 id="Assigning">分配</h2></div>
<p></p>
<p>~~参见<a href="denizen-0.7-assignments.md#Activity_Assignment" title="Denizen/0.7/Assignments">Denizen/0.7/作业#Activity_Assignment</a>~~</p>

