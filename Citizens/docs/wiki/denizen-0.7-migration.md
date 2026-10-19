---
title: Denizen / 0.7 / 迁移
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Migration
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5384
---


<a id="top"></a>

# Denizen / 0.7 / 迁移

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>~~==触发器==~~</p>
<p><s><ul><li>0.7引入了几个新核心triggers: Damage、Proximity和Location</li></ul></s></p>
<li>出于性能原因，并非所有触发器都默认打开。有关详细信息，请参阅 <a href="denizen-0.7-in-game-commands.md" title="Denizen/0.7/In Game Commands">Denizen/0.7/In_Game_Commands</a>。</li>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Commands">命令</h2></div></s></p>
<p>~~所有文本类型命令（聊天、叙述等）都必须将文本放在引号中。单人或双人都可以~~</p>
<p><s><pre> Example: - CHAT "Use double quotes if your text has an apostrophe, y'all." </pre></s></p>
<p>~~EXECUTE 还必须将命令和参数放在单引号或双引号中~~</p>
<p><s><pre> Example: - EXECUTE ASSERVER "warp someplace" </pre></s></p>
<p>~~GIVE 和 TAKE 必须以 QTY:# 或 qty:# 指定数量~~</p>
<p><s><pre> Example: - GIVE DIAMOND QTY:10</pre></s></p>
<p>~~重生不再存在。使用 TELEPORT 代替 DENIZEN 参数，这将在指定位置生成 Denizen。~~</p>
<p><s><pre> Example: - TELEPORT DENIZEN 'BOOKMARK:name' </pre></s></p>
<p>~~PLAYERTASK 不再存在。使用位置触发器</p>
<p>新闻界不再存在。使用 SWITCH 作为按钮和控制杆。</p>
<p>任何带有书签的命令都必须指定 BOOKMARK:。此外，任何带有书签的命令都可以通过指定“BOOKMARK：Denizen名称：BookmarkName”来使用其他居民的书签~~~~：如果Denizen名称中包含空格，则引号为<strong>必填</strong>~~</p>
<p><s><pre> Example: - TELEPORT DENIZEN 'BOOKMARK:bob jones:bobshouse' </pre></s></p>

