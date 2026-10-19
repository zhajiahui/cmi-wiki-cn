---
title: Denizen / 0.7 / 交互脚本 / 交互条件
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Interact_Requirements
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5378
---


<a id="top"></a>

# Denizen / 0.7 / 交互脚本 / 交互条件

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="Requirements"></a><h2 id="requirements">条件</h2>
<p>需求为您的脚本设置了检查标准。它们提供了一种强大的方式来与 Denizen NPCs 进行多种交互。想象一下 NPCs 会在你饿的时候给你一些鱼，或者一个店主可以向你推销商品。这是使用需求可以实现的许多事情中的两个。</p>
<p>注意：0.6 中的要求在 0.7 中保持不变，但现在将称为“旧版要求”。它们将慢慢被覆盖功能的新命令所取代。新系统可以提高容错性和更好的调试，并使其他插件程序员可以轻松扩展 Denizen。请注意。此页面将随时通知您任何更改。</p>
<p><code>[] indicates required field, () indicates an optional field, | indicates alternative usage.</code></p>
<p>点击任何要求即可获取更多信息和示例用法。</p>
<a id="Player"></a><h3 id="player">玩家</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">DURABILITY</a></td>
<td>[&gt; 或 &lt; 或 =] [# 或%]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">HOLDING</a></td>
<td>[ITEM_NAME 或#:#]（数量）</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">HUNGER</a></td>
<td>[饱或饿或饿]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">ITEM</a></td>
<td>[ITEM_NAME 或#:#]（数量）</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">LEVEL</a></td>
<td>[# 或更高]  或  等级  [至少此等级 #]  [不超过此等级 #]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">姓名</a></td>
<td>[玩家姓名]  （玩家姓名）  （玩家姓名）...</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">OWNER</a></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">POTIONEFFECT</a></td>
<td>[POTION_TYPE]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">SNEAKING</a></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">WEARING</a></td>
<td>[ITEM_NAME 或 #:#]</td>
</tr>
</tbody>
</table>
<a id="World"></a><h3 id="world">世界</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">ISLIQUID</a></td>
<td>[书签：块书签]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">ISPOWERED</a></td>
<td>[书签：块书签]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">PRECIPITATING</a></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">STORMY</a></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">SUNNY</a></td>
<td></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">TIME</a></td>
<td>[白天或夜晚或黄昏或黎明或时间 0-23999]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">WORLD</a></td>
<td>[世界名称]（世界名称）（世界名称）...</td>
</tr>
</tbody>
</table>
<a id="Script"></a><h3 id="script">脚本</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">ACTIVITY</a></td>
<td>[活动名称]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">FAILED</a></td>
<td>（次数）  [脚本名称]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">FINISHED</a></td>
<td>（次数）  [脚本名称]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">FLAGGED</a></td>
<td>[FlagName:FlagValue 或 FlagName]（完全）（PLAYER 或 DENIZEN 或 GLOBAL）</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">SCRIPT</a></td>
<td>[已完成或失败或步骤]（步骤：#）（数量：#）（完全）[脚本：脚本名称]</td>
</tr>
</tbody>
</table>
<a id="Permission/Economy"></a><h3 id="permissioneconomy">许可/经济</h3>
<p>仅当您安装了 Vault 和兼容的权限/经济插件时，这些要求才有效。</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">GROUP</a></td>
<td>[群组名称]  （群组名称）  （群组名称）...</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">MONEY</a></td>
<td>[数量]</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&amp;action=edit&amp;redlink=1" title="Interact Script Requirements (page does not exist)">许可</a></td>
<td>[permission.node]</td>
</tr>
</tbody>
</table>
<a id="Negative_Requirements"></a><h3 id="negative-requirements">负面要求</h3>
<p>要求也可以是“消极”要求。在需求列表中，只需在需求前面放置一个“-”即可反转其逻辑。例如，“HOLDING IRON_SWORD”将要求玩家持有一把铁剑。 “-HOLDING IRON_SWORD”将要求玩家不持有铁剑。所有要求都有一个消极的替代方案，即使是功能可能重叠的要求，例如“-WEATHER Precipitating”和“WEATHER Sunny”，它们在技术上做同样的事情。如果有的话，它可以增加脚本的可读性。否定要求“-”不应与列表中每个要求前面带有尾随空格的“列表项 -”混淆，因为这是标准的 YAML 列表格式。参见 below:</p>
<pre> Requirements:
   Mode: All
   List:
   - -TIME Night
   - -MONEY 1000000
   - -STORMY
</pre>
<p>负面需求可以完全改变原来的例子。在这个“修改”的例子中，要触发这个脚本，时间必须是白天，当前世界的天气不能是暴风雨，并且玩家身上的货币少于 1000000 单位。</p>

