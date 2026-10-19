---
title: CitizensUI
source_url: https://wiki.citizensnpcs.co/CitizensUI
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=3510
---


<a id="top"></a>

# CitizensUI

<p><a href="https://wiki.citizensnpcs.co/index.php?title=Special:Upload&amp;wpDestFile=CitizensUI.png" title="File:CitizensUI.png">File:CitizensUI.png</a> </p>
<p><strong>CitizensUI</strong></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>作者</strong></td>
<td>杰布达</td>
</tr>
<tr>
<td><strong>版本</strong></td>
<td>0.8.0</td>
</tr>
<tr>
<td><strong>Citizens 构建</strong></td>
<td>2.0 开发版本 #318</td>
</tr>
<tr>
<td><strong>其他依赖项</strong></td>
<td>Citizens 至少 2 个。</td>
</tr>
<tr>
<td><strong>下载</strong></td>
<td><a href="https://github.com/jrbudda/CitizensUI/downloads">链接</a></td>
</tr>
<tr>
<td><strong>Description:</strong> CitizensUI 是 .NET 图形用户界面，适用于 minecraft/bukkit 插件 Citizens2 和相关角色插件。</td>
<td></td>
</tr>
</tbody>
</table>
<p>CitizensUI 是 .NET 图形用户界面，适用于 minecraft/bukkit 插件 Citizens2 和相关角色插件。</p>
<p>Features:</p>
<ul>
<li>没有YAML要处理！</li>
<li>从游戏外部创建、编辑、复制和删除 Citizens 2.0 NPCs。</li>
<li>编辑 Citizens 2.0 <a href="characters.md" title="Characters">特征</a> <a href="sentry.md" title="Sentry">Sentry</a>、<a href="denizen.md" title="Denizen">Denizen</a> 和 <a href="cititraders.md" title="CitiTraders">CitiTraders</a> 选项。</li>
<li>创建和编辑 <a href="denizen.md" title="Denizen">Denizen</a> 脚本和作业。</li>
<li>从方便的下拉列表中选择您的要求、命令、项目、颜色和脚本。</li>
<li>将带有颜色的大块文本添加到本地脚本中，并可以选择行间等待。</li>
</ul>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="ChangeLog"></a><h2 id="changelog">变更日志</h2>
<ul>
<li>9/4/2012 (0.8.0) 完全支持 Denizen 活动脚本和分配。修复了一些 UI 怪癖。支持最新的 Cititraders。</li>
<li>9/2/2012 (0.7.4.2) 更改文本编码以支持扩展字符...也许吧。如果您遇到问题，请使用以前的版本并告诉我。</li>
<li>9/2/2012 (0.7.4.1) 对基本面板进行重大更新，支持 Citizens 版本中的新格式。支持 Cititraders“仅限所有者”模式。错误修正</li>
<li>2012 年 8 月 28 日：Denizen 命令和要求的语法更新。添加了默认活动字段。最新 Sentry 的更新。</li>
<li>2012 年 8 月 17 日：对 Denizen 活动进行错误修复和初步支持。 v0.7.3.2</li>
<li>2012 年 8 月 5 日：CitizensUI 现在支持 Sentry。 v0.7.2</li>
<li>2012 年 8 月 1 日：CitizensUI 现在支持 CitiTraders。 v0.7.1</li>
<li>2012 年 7 月 29 日：CitizensUI 0.7 目前仅与 Citizen2 build 249+ 和 Denizen build 223+ 兼容</li>
</ul>
<a id="Compatibility"></a><h2 id="compatibility">兼容性</h2>
<p>如果您的文件是使用早于 223 的 Citizen2 版本创建的，Citizens UI 将为您将它们转换为新的文件格式。</p>
<p>下载支持的插件 这里：</p>
<ul>
<li><a href="http://ci.citizensnpcs.net/job/Citizens2/">Citizens2</a></li>
<li><a href="denizen.md" title="Denizen">Denizen</a></li>
<li><a href="cititraders.md" title="CitiTraders">CitiTraders</a></li>
<li><a href="sentry.md" title="Sentry">Sentry</a></li>
</ul>
<a id="Installation"></a><h2 id="installation">安装</h2>
<p>至 install:</p>
<ul>
<li>您将需要 .NET Framework 3.5。通常这意味着 Windows，但 <a href="http://www.mono-project.com/Main_Page">单声道</a> 可能能够在其他平台上运行。</li>
<li>从 <a href="#top">下载</a> 页面打开最新的 zip 文件</li>
<li>将内容提取到您选择的目录。</li>
<li>运行CitizensUI.exe</li>
<li>第一次运行该程序时，它会提示您选择我的世界服务器的“插件”目录。</li>
<li>点击“加载”，它将加载 Citizens saves.yml 和 Denizen assignments.yml 中的数据以及 Denizen 脚本文件夹中的所有文件。</li>
</ul>
<p>添加和编辑让您满意。</p>
<p>完成后，点击“保存”，这将备份并覆盖以前存在的文件。</p>
<p>从服务器重新加载您的公民和居民。您创建的任何新 NPCs 都必须生成才能设置其位置。</p>
<a id="Options"></a><h2 id="options">选项</h2>
<p>Denizen 脚本可以保存在3个ways:中</p>
<ul>
<li>每个脚本 1 个文件。</li>
<li>每个 NPC 1 个文件。这还将为未分配和多重分配的脚本创建一个文件。</li>
<li>1 个包含所有脚本的文件。这是默认设置。</li>
</ul>
<a id="Known_Limitations"></a><h2 id="known-limitations">已知限制</h2>
<ul>
<li>脚本命令和需求数据未进行语法验证。显示了每个命令的正确语法，由您决定正确格式化数据。</li>
<li>尚不完全支持 Alchemist 和 Blacksmith。</li>
<li>无法编辑 npc 位置或路径点。</li>
<li>不加载或列出居民书签</li>
</ul>
<a id="Issues"></a><h2 id="issues">问题</h2>
<p>请报告问题 <a href="https://github.com/jrbudda/CitizensUI/issues">在 github 上</a></p>
<p><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=JVBJLN5HJJS52&amp;lc=US&amp;item_name=jrbudda¤cy_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted">捐赠给jrbudda</a></p>

