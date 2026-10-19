---
title: Denizen / 0.7 / 故障排查
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Troubleshooting
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5233
---


<a id="top"></a>

# Denizen / 0.7 / 故障排查

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s><div style="font-family:camingodos-web; font-size:100%;"></div></s></p>
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">D</span>enizen 乍一看可能有点复杂，尤其是当某些东西没有完全按照您想要的方式工作时您不知道要查找什么时。幸运的是，如果您遇到问题，有多种工具可以帮助您。</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Assignments_not_working?"><span id="Assignments_not_working.3F"></span>分配不起作用？</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>要检查 Denizen 上的分配，请使用 <tt>/denizen info</tt> 并选择 NPC 以确保已进行分配。这还显示其他重要信息，例如书签和活动。如果您是 NPC 的所有者，您也可以潜行并右键点击以查看此信息。参见：<a href="denizen-0.7-in-game-commands.md#Info-Click" title="Denizen/0.7/In Game Commands">信息点击</a></p><p>如果作业未显示，请确保您的 <tt>assignments.yml</tt> 格式正确、您已保存 assignments.yml 并且已使用 <tt>/denizen reload</tt>。另请检查 Denizen NPCs 名称的拼写。这是区分大小写的！参见：<a href="denizen-0.7-in-game-commands.md" title="Denizen/0.7/In Game Commands">重新加载命令</a></p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Trigger_not_working?"><span id="Trigger_not_working.3F"></span>触发器不工作？</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">默认情况下，Denizen NPCs 仅启用其点击触发器和聊天触发器。使用 <tt>/denizen trigger list</tt> 查看 NPC 的触发器状态。红色表示禁用。参见：  <a href="denizen-0.7-in-game-commands.md#Trigger_Toggles" title="Denizen/0.7/In Game Commands">触发命令</a>
<p><br/>
您也可能遇到插件冲突。如果您怀疑这一点，请尝试禁用除 Permissions、Citizens2 和 Denizen 之外的所有插件，看看问题是否仍然存在。</p>
</div>
<div class="mw-heading mw-heading3"><h3 id="Script_not_working_as_intended?"><span id="Script_not_working_as_intended.3F"></span>Script 未按预期工作？</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">打开 <tt>/denizen debug</tt> 并检查脚本运行时发送到控制台的信息。其中可能有一些信息可用于追踪问题，无论是失败的需求、不正确的流程逻辑、语法，还是仅仅是拼写错误。参见：  <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/In_Game_Commands&amp;action=edit&amp;redlink=1" title="Denizen/In Game Commands (page does not exist)">调试模式命令</a>
</div>
<div class="mw-heading mw-heading3"><h3 id="Still_having_problems,_what_now?"><span id="Still_having_problems.2C_what_now.3F"></span>仍然有问题，现在怎么办？</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">如果您仍然遇到问题，请检查控制台消息是否有错误，尤其是在启动时。任何插件的任何类型的错误都可能导致问题。再次利用这个机会仔细检查脚本中的间距。如果一切都失败了，请加入我们 <a class="external text" href="http://webchat.esper.net/?channels=denizen-dev" rel="nofollow">#denizen-dev 中的 EsperNet</a>.
</div>
<p></p>

