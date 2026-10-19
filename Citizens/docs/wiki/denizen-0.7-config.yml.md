---
title: Denizen / 0.7 / config.yml
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/config.yml
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5385
---


<a id="top"></a>

# Denizen / 0.7 / config.yml

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s></s></p>
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">时间</span>he config.yml 是旋钮和控制杆的位置，用于控制Denizen 及其脚本引擎。我们采取了尽可能多的机会来确保内置功能尽可能可定制。这包括允许调整低级居民功能，例如交互延迟的长度，到诸如文本格式之类的高级事物。</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Denizen_config.yml">Denizen config.yml</h3></div>
<div style="margin-right:2.0em;padding:10px; font-family:camingodos-web; font-size:110%;">Denizen config.yml 包含用于更改 Denizen 的默认行为和外观的节点。 
<p>可以随时使用 /denizen reload 将该文件从磁盘重新加载到 Denizen 内存。 config.yml 中的某些更改可能需要重新启动服务器。这包括interact_delay_in_ticks，但不限于该配置节点。
</p><p>更改 Denizen defaults:
</p>
<ul><li>打开位于plugins\Denizen\目录中的config.yml。</li>
<li>编辑默认值，保存文件，然后从游戏内或控制台调用 /denizen reload。 Denizen 将提醒您重新加载成功。</li></ul>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Default_config.yml">默认config.yml</h3></div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:850px; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> 默认 Denizen config.yml</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:850px; height:300px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;">{{{2}}}</div></td></tr></tbody></table>
</div>
<p></p>

