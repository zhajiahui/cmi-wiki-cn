---
title: Denizen / 0.7 / 可替换标签
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Replaceables
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5240
---


<a id="top"></a>

# Denizen / 0.7 / 可替换标签

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<p>可替换的数据标签可用于动态地将标志和值放入文本和命令中。
</p>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Flag_Replaceables">标记可更换件</h3></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:ghostwhite; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;FLAG.PLAYER:Name:fallback&gt; 或 &lt;FLAG.P:Name:fallback&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  在玩家上设置的 FLAG 值，如果未找到 FLAG，则使用可选的“后备”值。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:ghostwhite; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;FLAG.DENIZEN:Name:fallback&gt; 或 &lt;FLAG.D:Name:fallback&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  Denizen 上设置的 FLAG 值，如果未找到 FLAG，则使用可选的“后备”值。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:ghostwhite; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;FLAG.GLOBAL:Name:fallback&gt; 或 &lt;FLAG.G:Name:fallback&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  全局设置的 FLAG 值，如果未找到 FLAG，则使用可选的“后备”值。
 </div>
</td></tr></tbody></table>
</div>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Chat_Input_Replaceable">聊天输入可更换</h3></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lightcyan; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;*&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  包含玩家在当前步骤中使用的聊天触发器的值。与其他可替换项不同，它目前只能在语音命令和 FLAG 命令中使用。
 </div>
</td></tr></tbody></table>
</div>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Player_Replaceables">球员可更换</h3></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;DISPLAYNAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  与 Denizen、i.e 交互的玩家的显示名称。名称包括颜色。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;HEALTH&gt; 或 &lt;PLAYER.HEALTH&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家的生命值，从 0 到 20。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER&gt; 或 &lt;PLAYER.NAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家的名字。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.BOOTS&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  球员所穿靴子的材质。如果玩家没有佩戴任何装备，则为“FALSE”。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.CHESTPLATE&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家佩戴的胸甲的材质。如果玩家没有佩戴任何装备，则为“FALSE”。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.EXP&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家的总经验。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.EXP_TO_NEXT_LEVEL&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家达到下一级别所必须获得的经验。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.FOOD_LEVEL&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家的食物等级，从 0 到 20。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.HELM&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家佩戴的头盔的材质。如果玩家没有佩戴任何装备，则为“FALSE”。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.ID&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家手中物品的ID。如果玩家的手是空的，则为“0”。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.MATERIAL&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家手中物品的材质。如果玩家的手是空的，则为“AIR”。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.NAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家手中物品的名称。目前不起作用。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.ITEM_IN_HAND.QTY&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家手中物品的数量。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.KILLER&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  这名玩家的最后一个杀手的名字。目前不起作用。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.LEGGINGS&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家所穿紧身裤的材质。如果玩家没有佩戴任何装备，则为“FALSE”。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.MONEY&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家拥有的金钱数量。仅当您安装了 Vault 和兼容的权限/经济插件时，此可替换项才有效。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:lavender; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;PLAYER.WORLD&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  玩家所在世界的名称。
 </div>
</td></tr></tbody></table>
</div>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Denizen_Replaceables">Denizen 可更换件</h3></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:museo-sans; font-size:110%;"></div></s></p>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:papayawhip; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;NPC&gt; 或 &lt;DENIZEN.NAME&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  名称为Denizen。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:papayawhip; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;NPCID&gt; 或 &lt;DENIZEN.NPCID&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  Denizen的ID。
 </div>
</td></tr></tbody></table>
</div>
<div style="padding:3px;">
<table cellpadding="0" style="border-style:dashed; width:95%; border-width:1px; padding:6px;">
<tbody><tr>
<td width="30%"><div style="border-width: 1px; margin-top:4px; vertical-align:center; border-style: dotted; margin-bottom:5px; background-color:papayawhip; font-weight:400; text-align:center; font-family:droid-sans-mono; font-size:100%;">
<p>&lt;WORLD&gt;
</p>
</div>
</td>
<td><div style="border-width: 0px; vertical-align:center;margin-top:4px; border-style: dotted; margin-bottom:5px; text-align:left; margin-left:10px; font-weight:500; font-family:droid-sans-mono; font-size:80%;">  Denizen 所在世界的名称。
 </div>
</td></tr></tbody></table>
</div>
<p></p>

