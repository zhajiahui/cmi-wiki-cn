---
title: Denizen / 条件
source_url: https://wiki.citizensnpcs.co/Denizen/Requirements
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5386
---


<a id="top"></a>

# Denizen / 条件

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>由于 - IF { .. } 命令，从 0.9 开始不再需要这些要求，但是仍然支持它们以避免破坏旧脚本。</p>
<a id="How_To_Use_Requirements"></a><h1 id="how-to-use-requirements">如何使用需求</h1>
<p>它们写在交互脚本的顶部附近，例如 so:</p>
<div class="highlight"><pre>MyInteractScript:
    Type: Interact
    Requirements:
        Mode: 
        List:
        - FirstReq
        - SecondReq etc. etc.</pre></div>
<a id="List_Of_Requirements"></a><h1 id="list-of-requirements">要求清单</h1>
<p>附魔、标记、持有、内组、项目、isliquid、金钱、op、所有者、许可、ispowered、氧气、程序、脚本、潜行、风暴、晴天、雨天、时间、区域内</p>
<div class="highlight"><pre>- enchanted (iteminhand)
- flagged [player/npc/global] [&lt;name&gt;([&lt;#&gt;])](:&lt;value&gt;)
- holding [&lt;item&gt;] [qty:&lt;#&gt;] [exact]
- ingroup (global) [&lt;group&gt;]
- item [&lt;item&gt;] (qty:&lt;#&gt;)
- isliquid [location:&lt;location&gt;]
- money [qty:&lt;#&gt;]
- op
- owner
- permission (global) [&lt;permission&gt;]
- ispowered [location:&lt;location&gt;]
- oxygen (range:below/equals/above) [qty:&lt;#&gt;]
- procedure [&lt;script&gt;]
- script [finished/failed] [script:&lt;name&gt;]
- sneaking
- storming (????????????????????) (This req is ill-defined)
- sunny
- rainy
- time [dawn/day/dusk/night]
- inregion [name:&lt;region&gt;]</pre></div>

