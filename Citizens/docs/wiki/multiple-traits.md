---
title: 多个特征
source_url: https://wiki.citizensnpcs.co/Multiple_Traits
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=1989
---


<a id="top"></a>

# 多个特征

<p>所有 Citizens 2.0 行为均由特征决定。</p>
<p>特征可以应用于 NPCs 并将以特定方式处理事件和交互。</p>
<p>最酷的是 NPC 可以分配多个特征。包括多个 <a href="characters.md" title="Characters">性格</a> 特征。</p>
<p><a href="https://wiki.citizensnpcs.co/index.php?title=Wallet&amp;action=edit&amp;redlink=1" title="Wallet (page does not exist)">钱包</a> 特征就是一个例子。这个特性允许NPC拥有和使用经济货币。此特征本身无用，但当 NPC 也被分配了 <a href="denizen.md" title="Denizen">Denizen</a> 或 <a href="trader.md" title="Trader">交易员</a> 特征时，该特征有效。</p>
<p><a href="characters.md" title="Characters">角色类型</a>实际上只是复杂的特征。</p>
<p>分配多个 <a href="characters.md" title="Characters">角色类型</a> 特征可以产生强大的结果，但也可能产生潜在的冲突。</p>
<p>具有 <a href="denizen.md" title="Denizen">Denizen</a> 特征的 NPCs 应使用该特征的命令来打开和关闭可能导致冲突的特定交互。</p>
<p>例如，如果您想使用 Denizen <a href="https://wiki.citizensnpcs.co/index.php?title=Activities&amp;action=edit&amp;redlink=1" title="Activities (page does not exist)">活动</a> 来制作一个 <a href="blacksmith.md" title="Blacksmith">Blacksmith</a> 在整个城镇中徘徊来指示他的运动，您可能需要在 <a href="denizen.md" title="Denizen">Denizen</a> 特征中关闭 <a href="https://wiki.citizensnpcs.co/index.php?title=Click_Triggers&amp;action=edit&amp;redlink=1" title="Click Triggers (page does not exist)">点击触发器</a>，以便右键点击 <a href="blacksmith.md" title="Blacksmith">Blacksmith</a> 将执行正确的操作<a href="blacksmith.md" title="Blacksmith">Blacksmith</a> 命令并且不会触发任何 <a href="denizen.md" title="Denizen">Denizen</a> 脚本。</p>
<p>使用命令</p>
<p>:   <strong>/trait [traitname]</strong></p>
<p>将为选定的 NPC 打开和关闭特征。</p>

