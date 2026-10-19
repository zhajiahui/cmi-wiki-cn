---
title: MoxieNPC
source_url: https://wiki.citizensnpcs.co/MoxieNPC
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4462
---


<a id="top"></a>

# MoxieNPC

<table cellpadding="0" cellspacing="3" style="border: 0; background-color: #ffffff" width="275">
<tbody><tr>
<td style="width: 275; vertical-align: top; border:1px solid #ccc; background-color: #ffffff">
<div style="background-color:#aaa; font-size:1px; height:8px; border-bottom:1px solid #ccc;"></div>
<div style="float:right; margin:8px; margin-top:5px"></div>
<div style="padding:0.5em 0.3em 0.3em 0.3em; margin:0; text-indent:0.1em; font-weight: bold; border-bottom:1px solid #aaaaaa;"><b> </b></div>
<div style="font-size:100%; padding:3px">
<table cellpadding="0" cellspacing="3" width="100%">
<tbody><tr>
<td align="left" valign="top" width="100%">
<figure class="mw-halign-center" typeof="mw:File/Frameless"><a class="mw-file-description" href="https://wiki.citizensnpcs.co/File:Moxienpclogo.jpg" title="image"><img alt="image" class="mw-file-element" decoding="async" height="133" src="assets/16dde4772496-Moxienpclogo.jpg" width="260"/></a>&lt;figcaption&gt;图片</figure>
<div class="padded" style="padding: 19px; font-family:camingodos-web; font-size:110%;">
<p><b>MoxieNPC</b> 是 MoxieSkills 的扩展，允许服务器向玩家出售能力和技能 XP。</p><p><b>当前版本：</b> 1.5 发布</p><p><b>Developers:</b> x3nec</p><p><b>Source:</b> <a class="external text" href="https://github.com/x3nec/MoxieNPC" rel="nofollow">吉图布</a>
</p><p><b>最新版本：</b> <a class="external text" href="http://dev.bukkit.org/server-mods/moxienpc/files/3-moxie-npc-v1-5/" rel="nofollow">布基特开发公司</a>
</p><p><b>支持tickets:</b> <a class="external text" href="http://dev.bukkit.org/server-mods/moxienpc/tickets/" rel="nofollow">BukkitDev 上的门票</a>
</p><p><b>感谢 to:</b> aufdemrand 用于此信息框！
<br/></p>
</div></td></tr></tbody></table>
</div>
</td></tr></tbody></table>
<p><a href="https://wiki.citizensnpcs.co/File:Moxienpclogo.jpg" title="image"><img alt="image" src="assets/16dde4772496-Moxienpclogo.jpg"/></a></p>
<p>图像</p>
<a id="What_Is_It?"></a><h3 id="what-is-it">它是什么？</h3>
<p>MoxieNPC 是 <a href="http://dev.bukkit.org/server-mods/moxieskills">莫西技能</a> 的扩展，允许管理员设置 NPC 商店而不是标志商店。为了使该插件运行，您需要在服务器上运行 <a href="http://dev.bukkit.org/server-mods/citizens">Citizens 2.0</a> 和 <a href="http://dev.bukkit.org/server-mods/moxieskills">莫西技能</a>。</p>
<hr/>
<a id="How_To_Use_It"></a><h3 id="how-to-use-it">如何使用</h3>
<p>MoxieNPC 不是一个独立的插件 - 它是从 Citizens 2.0 扩展的角色特征。因此，为了使用它，您必须首先创建一个NPC，然后执行'/trait moxienpc'。完成后，您可以继续按照以下说明进行操作。</p>
<ul>
<li>要向玩家出售能力，该能力必须在 abilities.yml 文件中将可购买设置为 true（对于 MoxieSkills|RPG）</li>
<li>要将 XP 出售给玩家，技能的拼写必须正确。 N.B。请记住，您指定的成本仅为 1 XP。</li>
<li>为了了解如何使用MoxieNPCs，只需在游戏中输入/mnpc，并使用Citizens选择的MoxieNPC，就这么简单！</li>
<li>MoxieNPC 是可以交谈的，因此玩家只需右键点击它们即可给出指示！</li>
</ul>
<hr/>
<a id="Permissions"></a><h3 id="permissions">权限</h3>
<div class="highlight"><pre>  moxienpc.usenpc.ability - Buy abilities from the NPC shop.
  moxienpc.makenpc.ability - Add abilities to sell at NPC shop.
  moxienpc.usenpc.xp - Buy skills XP from the NPC shop.
  moxienpc.makenpc.xp - Add skills XP to sell at NPC shop.
</pre></div>

