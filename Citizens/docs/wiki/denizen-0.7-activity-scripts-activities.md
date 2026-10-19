---
title: Denizen / 0.7 / 活动脚本 / 活动
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts/Activities
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5379
---


<a id="top"></a>

# Denizen / 0.7 / 活动脚本 / 活动

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<table align="left" class="wikitable collapsible collapsed" style="background:aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WANDER</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(半径:#) (延迟:#) (速度:#) (过滤器:#:#,#:#..) (书签:书签名称)
</th></tr>
<tr>
<td colspan="3">导致Denizen漫无目的地徘徊。有许多选项可以指定范围和面积。
<p>Modifiers:
</p>
<ul><li>半径：徘徊的半径。</li>
<li>DELAY：动作之间的时间（以秒为单位）。</li>
<li>速度：徘徊时的行走速度。</li>
<li>过滤器：允许 Denizen 漫游到的块 ID 或名称</li>
<li>书签：可供漫步的位置书签</li></ul>
<p><b>用法示例</b>
</p>
<pre>   - 1 WANDER DELAY:12 RADIUS:10 SPEED:.75 FILTER:COBBLESTONE,GRAVEL,5
</pre>
</td></tr></tbody></table>
<table align="left" class="wikitable collapsible collapsed" style="background:aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>TASK</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[SCRIPT:ScriptNAme] (REPEATS:#) (DELAY:#) (DURATION:#)
</th></tr>
<tr>
<td colspan="3">运行一个 <a href="denizen-0.7-task-scripts.md" title="Denizen/0.7/Task Scripts">任务脚本</a> repeatedly.
<p>Modifiers:
</p>
<ul><li>SCRIPT：要运行的任务脚本。请注意，不会有与此脚本关联的“玩家”，因此某些命令将不起作用。</li>
<li>REPEATS：重复任务的次数。默认情况下，脚本会重复运行，直到分配新活动为止。</li>
<li>DELAY：重复之间等待的秒数。</li>
<li>DURATION：任务运行时暂停其他活动的秒数。</li></ul>
<p><b>用法示例</b>
</p>
<pre>  - 1 TASK SCRIPT:WalkHome REPEATS:0
  - 1 TASK SCRIPT:ComplainAboutThings DELAY:10 DURATION:1

</pre>
</td></tr></tbody></table>

