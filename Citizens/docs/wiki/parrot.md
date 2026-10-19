---
title: Parrot
source_url: https://wiki.citizensnpcs.co/Parrot
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=1515
---


<a id="top"></a>

# Parrot

<table>
<thead>
<tr>
<th><strong>外部角色类型！</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>此页面涉及 NPC 的类型，该类型不受 Citizens 开发团队支持。不要向他们或论坛/IRC 寻求支持，因为我们无法帮助您。相反，请查看右侧 InfoBox 的 BukkitDev 链接，了解有关如何获得对此角色类型的支持的信息。</td>
</tr>
</tbody>
</table>
<table align="right" cellpadding="0" cellspacing="3" style="border: 0; background-color: #ffffff" width="30%">
<tbody><tr>
<td style="width: 30%; vertical-align: top; border:1px solid #ccc; background-color: #ffffff">
<div style="background-color:gray; font-size:1px; height:8px; border-bottom:1px solid #ccc;"></div>
<div style="float:right; margin:8px; margin-top:5px"></div>
<div style="padding:0.5em 0.3em 0.3em 0.3em; margin:0; text-indent:0.1em; align:center; font-weight: bold; border-bottom:1px solid #aaaaaa;"><center><span class="mw-default-size" typeof="mw:Error mw:File"><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Special:Upload&amp;wpDestFile=Mimic.png" title="File:Mimic.png"><span class="mw-file-element mw-broken-media">File:Mimic.png</span></a></span><br/><br/><b>模仿者</b></center></div>
<div style="font-size:100%; padding:13px">
<table cellpadding="0" cellspacing="3" width="100%">
<tbody><tr>
<td align="left" valign="top" width="150"><b>作者</b>
</td>
<td><a href="https://wiki.citizensnpcs.co/User:Aufdemrand" title="User:Aufdemrand">奥夫德姆兰德</a>
</td></tr>
<tr>
<td><b>版本</b>
</td>
<td>0.6
</td></tr>
<tr>
<td><b>Citizens 构建</b>
</td>
<td>2.0 (#37)
</td></tr>
<tr>
<td><b>发展现状</b>
</td>
<td>开发者
</td></tr>
<tr>
<td><b>下载</b>
</td>
<td><a class="external text" href="http://dev.bukkit.org/server-mods/parrot/files/2-parrot-beta-v0-4/" rel="nofollow">链接</a>
</td></tr>
<tr>
<td><b>布基特开发公司</b>
</td>
<td><a class="external text" href="http://dev.bukkit.org/server-mods/parrot/" rel="nofollow">链接</a>
</td></tr>
<tr>
<td><b>来源</b>
</td>
<td><a class="external text" href="http://www.github.com/aufdemrand/Mimic" rel="nofollow">链接</a>
</td></tr>
<tr>
<td><b>问题</b>
</td>
<td><a class="external text" href="http://www.github.com/aufdemrand/Mimic/Issues" rel="nofollow">链接</a>
</td></tr>
<tr>
<td colspan="2"><div style="border-top:1px solid #aaaaaa;"><b>Description:</b> 一个模仿品 NPC，可用于娱乐或提供线索。</div>
</td></tr>
<tr>
<td colspan="2"><div style="border-top:1px solid #aaaaaa;"><center><code><a href="installing-character-types.md" title="Installing Character Types">Installing Character Types</a></code></center></div>
</td></tr></tbody></table>
</div>
</td></tr></tbody></table>
<p>Mimics是尝试使用Citizens2为Minecraft带来一些RPG元素。模仿者可以只是为了好玩，也可以用于寻找线索。末影龙鹦鹉，有人吗？ （开玩笑！可能不是一个好主意！）</p>
<p>模仿者随机存储在本地区域所说的消息并重复回来。模仿者还可以掌握线索、信息，并通过听到的正常聊天脱口而出，这对于任何 RPG 谜题来说都是一个重要的元素。</p>
<a id="Features"></a><h2 id="features">特点</h2>
<p>可定制的“语音”模仿类型，具有可调整的文本消息，用于定时文本和点击行为。
标配 Parrot、史莱姆模仿者和乡村白痴。您可以添加自己的！</p>
<a id="Planned_Future_Features"></a><h2 id="planned-future-features">计划的未来功能</h2>
<a id="Commands"></a><h2 id="commands">命令</h2>
<a id="Permissions"></a><h2 id="permissions">权限</h2>
<a id="Settings_(and_defaults)"></a><h2 id="settings-and-defaults">设置（和默认值）</h2>
<p>以下是带注释的标准配置。</p>
<div class="highlight"><pre># Mimic Configuration

cooldown-in-seconds: 45       # Time between each message/etc update timer. 
                              #   (Recommended 30-90)
click-cooldown-in-seconds: 5
chatter-range: 25             # Distance from Mimic needed to be to hear it.
                              #   (Recommended 10-30)
# Note: Next two lines have not yet been implemented, but still need to be set.
text-style: Normal            # Available: Sentence Case, Lower Case, Upper Case, Normal
use-smart-wrap: True          # Wraps text spanning multiple lines smartly.


# TYPES/DIALOG Setup
# You can add as many items to the list as you'd like.
# You can use &lt;text&gt; to use the mimic's texts.
# Note: &lt;text&gt; also randomly shows the mimic's clue.

voice types:
  list:               # List each voice mimic type. Case sensitive!
    - Parrot
    - Village Idiot
    - Slime Mimic

  NPC defaults:       # You can specify mimic type defaults for each npc type
                      # EntityTypes specified here will automatically apply the mimic type set alongside.
    SLIME: Slime Mimic
    CHICKEN: Parrot
    VILLAGER: Village Idiot

  # And now in detail. Note: This part needs to be indented as it's still part
  # of the types: node.  This is where you define each type. This is case sensitive!
  # When adding new types, be sure to add them to the list: node above, as well.

  Parrot:
    on click:         # Texts on click
      - "It's a parrot."
      - "You pet the parrot. *BAAAWK!*"
    texts:            # Texts that trigger randomly.
      - "A parrot squacks, '&lt;text&gt;'"
      - "'&lt;text&gt;' ...is that a parrot?"
      - "You hear a parrot nearby, '*SQUAK*!'"
      - "You hear a parrot nearby, '&lt;text&gt;'"
      - "*BRR BRR BRR* ...is that a parrot?"
      - "*BAAAWK* *BAAAWK*"   

  Village Idiot:
    on click:
      - "Oh, it's just the Village Idiot... he's an idiot."
      - "You slug the Village idiot in the arm. *OUCH!*"
      - "The Village Idiot says to you, 'text'"
    texts:
      - "'Yarharrrharr!' ...what the heck was that?"
      - "The village idiot says, '&lt;text&gt;' ...does that even make sense?"
      - "'&lt;text&gt;' says the Village Idiot, in a drunken slur."

  Slime Mimic:
    click:
      - "It's a jelly-like block of slime. Yuck!"
      - "The slime is filled with all kinds of stuff. Who knows where it has been?"
    texts:
      - "'&lt;text&gt;' ...was that a slime mimic?"
      - "You hear a slime mimic nearby, '&lt;text&gt;'"
      - "*SQUISH* *SQUISH*"
</pre></div>
<p>注意：当模仿者被创建并与之交互时，另一个部分将填充在 config.yml 中。这应该在游戏中使用命令进行配置。</p>

