---
title: Denizen / 可替换标签
source_url: https://wiki.citizensnpcs.co/Denizen/Replaceable_Tags
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5225
---


<a id="top"></a>

# Denizen / 可替换标签

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="Flags"></a><h2 id="flags">旗帜</h2>
<table>
<thead>
<tr>
<th>~~{</th>
<th>类=“维基表”宽度=“100%”边框=“1”</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td>宽度=“30%”</td>
</tr>
<tr>
<td></td>
<td>返回附加到服务器的标志的值。注意：在 0.9 中，更推荐使用 <server.flag[flag_name]></server.flag[flag_name]></td>
</tr>
<tr>
<td></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td><flag.n:flag_name></flag.n:flag_name></td>
</tr>
<tr>
<td></td>
<td>返回附加到当前 NPC 的标志的值。注意：在 0.9 中，更推荐使用 <npc.flag[flag_name]></npc.flag[flag_name]></td>
</tr>
<tr>
<td></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td><flag.p:flag_name></flag.p:flag_name></td>
</tr>
<tr>
<td></td>
<td>返回附加到当前玩家的标志的值。注意：在 0.9 中，更推荐使用 <player.flag[flag_name]></player.flag[flag_name]></td>
</tr>
<tr>
<td></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td><player[player_name].flag[flag_name]></player[player_name].flag[flag_name]></td>
</tr>
<tr>
<td></td>
<td>返回另一个玩家的标志值。</td>
</tr>
<tr>
<td></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td><player.flag[flag_name]>.isexpired&gt;</player.flag[flag_name]></td>
</tr>
<tr>
<td></td>
<td>如果标志的持续时间已过期，则返回 true 或 false。</td>
</tr>
<tr>
<td></td>
<td>}~~</td>
</tr>
</tbody>
</table>
<p><s><div class="mw-heading mw-heading2"><h2 id="Location">地点</h2></div></s></p>
<p>~~所有位置标签都需要坐标。您可以在方括号 [] 中添加标签，也可以自己指定确切的位置。例如，您可以使用~~</p>
<p><s><pre>&lt;location[&lt;npc.location&gt;].biome.temperature&gt;</pre></s></p>
<p>~~获取NPC所在位置的温度。~~</p>
<p><s><table border="1" class="wikitable" width="100%"></table></s></p>
<tbody><tr>
<td width="30%">&lt;location[x,y,z,world].biome.formatted&gt;
</td>
<td>坐标处生物群系的格式化名称。
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].biome.humidity&gt;
</td>
<td>坐标处的当前湿度。
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].biome.temperature&gt;
</td>
<td>坐标处的当前温度。
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].distance[x,y,z,world]&gt;
</td>
<td>2 个坐标之间的距离。
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].formatted&gt;
</td>
<td>坐标采用更易于阅读的格式。
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].is_liquid&gt;
</td>
<td>坐标处的方块是否是液体。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;location[x,y,z,world].light&gt;
</td>
<td>坐标处的光照水平。
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="NPC">NPC</h2></div></s></p>
<p>~~注意：您可以参考一个NPC除了 中的那个之外当前脚本使用 <npc[npc_id]>...例如， <npc[2].id> （这将是完全无用的）会返回'2'.~~</npc[2].id></npc[npc_id]></p>
<p><s><table border="1" class="wikitable" width="100%"></table></s></p>
<tbody><tr>
<td width="30%">&lt;npc.flag[flag_name]&gt;
</td>
<td>返回附加到 NPC 的标志的值。
</td></tr>
<tr>
<td>&lt;npc.id&gt;
</td>
<td>NPC的ID号。
</td></tr>
<tr>
<td>&lt;npc.location&gt;
</td>
<td>NPC 的坐标。 [x,y,z,世界]
</td></tr>
<tr>
<td>&lt;npc.location.previous_location&gt;
</td>
<td>NPC 所在的最后位置。
</td></tr>
<tr>
<td>&lt;npc.location.standing_on&gt;
</td>
<td>NPC 所在的 Bukkit 块名称。
</td></tr>
<tr>
<td>&lt;npc.location.standing_on_display&gt;
</td>
<td>NPC 所在的格式化块名称。
</td></tr>
<tr>
<td>&lt;npc.location.world&gt;
</td>
<td>NPC 所在世界的名称。
</td></tr>
<tr>
<td>&lt;npc.location.world_spawn&gt;
</td>
<td>NPC 当前所在世界的出生点坐标。
</td></tr>
<tr>
<td>&lt;npc.location.x&gt;
</td>
<td>NPC 所在的 x 坐标。
</td></tr>
<tr>
<td>&lt;npc.location.y&gt;
</td>
<td>NPC 所在的 y 坐标。
</td></tr>
<tr>
<td>&lt;npc.location.z&gt;
</td>
<td>NPC 所在的 z 坐标。
</td></tr>
<tr>
<td>&lt;npc.name&gt;
</td>
<td>NPC 的名称。
</td></tr>
<tr>
<td>&lt;npc.name.nickname&gt;
</td>
<td>NPC 的昵称。
</td></tr>
<tr>
<td>&lt;npc.owner&gt;
</td>
<td>NPC 的所有者。
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Player">玩家</h2></div></s></p>
<p>~~注意：您可以通过使用引用除当前脚本中的玩家之外的玩家 <player[player_name]>...例如， <player[morphan1].name> （这将完全无用）将返回“Morphan1”。~~</player[morphan1].name></player[player_name]></p>
<p><s><table border="1" class="wikitable" width="100%"></table></s></p>
<tbody><tr>
<td width="30%">&lt;player.chat_history&gt;
</td>
<td>玩家发送的最后一条消息。
</td></tr>
<tr>
<td>&lt;player.chat_history[X]&gt;
</td>
<td>玩家 X 次前发送的消息。
</td></tr>
<tr>
<td>&lt;player.equipment.boots&gt;
</td>
<td>球员所穿球鞋的 Bukkit 名称。也可用于胸甲、护腿和头盔。
</td></tr>
<tr>
<td>&lt;player.equipment.boots.formatted&gt;
</td>
<td>球员所穿球鞋的格式化名称。也可用于胸甲、护腿和头盔。
</td></tr>
<tr>
<td>&lt;player.flag[flag_name]&gt;
</td>
<td>返回附加到玩家的标志的值。
</td></tr>
<tr>
<td>&lt;player.health&gt;
</td>
<td>玩家的生命值，1-20。每个数字都是半颗心。
</td></tr>
<tr>
<td>&lt;player.health.formatted&gt;
</td>
<td>玩家的格式化健康状况。可能是健康的、擦伤的、受伤的、重伤的、甚至死亡的。
</td></tr>
<tr>
<td>&lt;player.health.percentage&gt;
</td>
<td>玩家的生命值百分比。
</td></tr>
<tr>
<td>&lt;player.inventory.contains.display[display_name]&gt;
</td>
<td>检查玩家的库存中是否包含具有在铁砧上选择的名称的物品。您还可以添加 .qty[X] 来检查玩家是否拥有 X 数量的物品。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.inventory.contains[item_id]&gt;
</td>
<td>检查玩家的库存中是否包含物品。您还可以添加 .qty[X] 来检查玩家是否拥有 X 数量的物品。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.food_level&gt;
</td>
<td>玩家的食物等级，1-20。每个数字都是饥饿栏上食物的一半。
</td></tr>
<tr>
<td>&lt;player.food_level.formatted&gt;
</td>
<td>玩家格式化的食物等级。可以是健康的、干渴的、饥饿的、饥饿的。
</td></tr>
<tr>
<td>&lt;player.food_level.percentage&gt;
</td>
<td>玩家的食物水平以百分比表示。
</td></tr>
<tr>
<td>&lt;player.group[group_name]&gt;
</td>
<td>通过 Vault 检查玩家是否在组中。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.group[group_name].global&gt;&gt;
</td>
<td>通过 Vault 检查玩家是否在全局组中。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.enchantments&gt;
</td>
<td>玩家手中物品的附魔列表。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.enchantments_with_level&gt;
</td>
<td>玩家手中物品的附魔列表及其等级。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.enchantments_with_level_only&gt;
</td>
<td>玩家手中物品的附魔等级列表。
</td></tr>
<tr>
<td>&lt;player.item_in_hand&gt;
</td>
<td>包含玩家手中物品的所有详细信息。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.data&gt;
</td>
<td>玩家持有的物品的材质数据。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.display&gt;
</td>
<td>在铁砧上为玩家所持有的物品选择的名称。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.durability&gt;
</td>
<td>玩家持有的物品的耐用性。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.id&gt;
</td>
<td>玩家持有的方块或物品的 ID。所有块和项目 ID 均位于 <a class="external text" href="http://www.minecraftwiki.net/wiki/Data_values" rel="nofollow">这里</a>。</td></tr>
<tr>
<td>&lt;player.item_in_hand.lore&gt;
</td>
<td>玩家手中物品的知识列表。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.max_stack&gt;
</td>
<td>玩家所持有物品的一个库存栏位中可以拥有的最大数量。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.material&gt;
</td>
<td>Bukkit 玩家手中物品的材质名称。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.material.formatted&gt;
</td>
<td>玩家手中物品的格式化材质名称。
</td></tr>
<tr>
<td>&lt;player.item_in_hand.qty&gt;
</td>
<td>玩家持有的物品的当前库存槽数量。
</td></tr>
<tr>
<td>&lt;player.is_banned&gt;
</td>
<td>玩家是否被禁止。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.is_online&gt;
</td>
<td>玩家是否在线。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.is_op&gt;
</td>
<td>玩家是否是操作员。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.location&gt;
</td>
<td>玩家的坐标。 [x,y,z,世界]
</td></tr>
<tr>
<td>&lt;player.location.bed_spawn&gt;
</td>
<td>玩家最后睡过的床的坐标（如果有）。
</td></tr>
<tr>
<td>&lt;player.location.cursor_on[X]&gt;
</td>
<td>玩家光标所在方块的位置，在 X 范围内。
</td></tr>
<tr>
<td>&lt;player.location.standing_on&gt;
</td>
<td>玩家所站立的 Bukkit 方块名称。
</td></tr>
<tr>
<td>&lt;player.location.standing_on.formatted&gt;
</td>
<td>玩家所站立的格式化方块名称。
</td></tr>
<tr>
<td>&lt;player.location.world&gt;
</td>
<td>玩家所在世界的名称。
</td></tr>
<tr>
<td>&lt;player.location.world_spawn&gt;
</td>
<td>玩家当前所在世界的出生点坐标。
</td></tr>
<tr>
<td>&lt;player.location.x&gt;
</td>
<td>玩家所在的 x 坐标。
</td></tr>
<tr>
<td>&lt;player.location.y&gt;
</td>
<td>玩家所在的 y 坐标。
</td></tr>
<tr>
<td>&lt;player.location.z&gt;
</td>
<td>玩家所在的 z 坐标。
</td></tr>
<tr>
<td>&lt;player.money&gt;
</td>
<td>该玩家帐户中的金额。需要 Vault 和经济插件。
</td></tr>
<tr>
<td>&lt;player.name&gt;
</td>
<td>玩家的名字。
</td></tr>
<tr>
<td>&lt;player.name.display&gt;
</td>
<td>玩家的显示名称。 （聊天中显示的那个。）
</td></tr>
<tr>
<td>&lt;player.mcmmo.level[skill_name]&gt;
</td>
<td>玩家当前的 McMMO 技能等级。
</td></tr>
<tr>
<td>&lt;player.money&gt;
</td>
<td>玩家有多少钱，以数字表示。 （0.0、1.5、2.25 等）
</td></tr>
<tr>
<td>&lt;player.money.asint&gt;
</td>
<td>玩家有多少钱，以整数表示。 （0、1、2 等）
</td></tr>
<tr>
<td>&lt;player.money.currency&gt;
</td>
<td>该服务器经济插件中设置的货币。
</td></tr>
<tr>
<td>&lt;player.money.currency.plural&gt;
</td>
<td>该服务器经济插件中设置的货币，采用复数形式。
<p>示例：美元、英镑、硬币
</p>
</td></tr>
<tr>
<td>&lt;player.money.currency.singular&gt;
</td>
<td>该服务器经济插件中设置的货币，以其单一形式。
<p>示例：美元、英镑、硬币
</p>
</td></tr>
<tr>
<td>&lt;player.script[script_name].failed&gt;
</td>
<td>检查玩家的脚本是否失败。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.script[script_name].finished&gt;
</td>
<td>检查玩家是否已完成脚本。可以是真的也可以是假的。
</td></tr>
<tr>
<td>&lt;player.time&gt;
</td>
<td>玩家的时间（以刻度为单位），从 0 到 23999。要快速查看不同刻度值在现实生活中的含义，请查看 <a class="external text" href="http://media-mcw.cursecdn.com/b/bc/Day_Night_Clock_24h.png" rel="nofollow">这里</a>。</td></tr>
<tr>
<td>&lt;player.time.period&gt;
</td>
<td>该玩家的时间段。可以是“白天”或“夜晚”。
</td></tr>
<tr>
<td>&lt;player.xp&gt;
</td>
<td>玩家的总经验。
</td></tr>
<tr>
<td>&lt;player.xp.level&gt;
</td>
<td>玩家当前的经验等级。
</td></tr>
<tr>
<td>&lt;player.weather&gt;
</td>
<td>该玩家世界当前的天气。如果有暴风雨，则为“storming”；如果天气晴朗且是白天，则为“sunny”；如果天气晴朗且是夜间，则为“clear”。
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Util">效用</h2></div></s></p>
<p><s><table border="1" class="wikitable" width="100%"></table></s></p>
<tbody><tr>
<td width="30%">&lt;util.random.int[1].to[50]&gt;
</td>
<td>返回下限（第一个数字）和上限（第二个数字）之间的随机数。
</td></tr>
<tr>
<td width="30%">&lt;util.random.uuid&gt;
</td>
<td>返回一个随机的“uuid”，对于启动新队列很有用。
</td></tr>
<tr>
<td width="30%">&lt;util.substr[string]&gt;
</td>
<td>返回字符串的子字符串。
</td></tr>
</tbody>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Math_Tags">数学标签</h2></div></s></p>
<p>~~数学标签是 Denizen 的一个有用部分，顾名思义，它允许您在内部执行数学运算。</p>
<p>这是一般语法，其中包含空格以提高可读性。 （您的实际脚本中不应包含空格。如果必须，请将其放在“引号”中）~~</p>
<p><s><pre>&lt;m: firstThing + secondThing&gt; 
//Now, all together,
&lt;m:firstThing+secondThing&gt;
</pre></s></p>
<p>~~当然，+并不是唯一可以使用的数学运算符。还可以 use:</p>
<p>减号和模数：（- 和%）</p>
<p>除法和乘法：（/和*）~~</p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Text">文字</h2></div></s></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Colors">颜色</h3></div></s></p>
<p><s><table border="1" class="wikitable" width="25%"></table></s></p>
<tbody><tr>
<td width="60%">&lt;aqua&gt;
</td>
<td style="background-color:#55FFFF">
</td></tr>
<tr>
<td>&lt;black&gt;
</td>
<td style="background-color:black">
</td></tr>
<tr>
<td>&lt;blue&gt;
</td>
<td style="background-color:#5555FF">
</td></tr>
<tr>
<td>&lt;dark_aqua&gt;
</td>
<td style="background-color:#00AAAA">
</td></tr>
<tr>
<td>&lt;dark_blue&gt;
</td>
<td style="background-color:#0000AA">
</td></tr>
<tr>
<td>&lt;dark_gray&gt;
</td>
<td style="background-color:#555555">
</td></tr>
<tr>
<td>&lt;dark_green&gt;
</td>
<td style="background-color:#00AA00">
</td></tr>
<tr>
<td>&lt;dark_purple&gt;
</td>
<td style="background-color:#AA00AA">
</td></tr>
<tr>
<td>&lt;dark_red&gt;
</td>
<td style="background-color:#AA0000">
</td></tr>
<tr>
<td>&lt;gold&gt;
</td>
<td style="background-color:#FFAA00">
</td></tr>
<tr>
<td>&lt;gray&gt;
</td>
<td style="background-color:#AAAAAA">
</td></tr>
<tr>
<td>&lt;green&gt;
</td>
<td style="background-color:#55FF55">
</td></tr>
<tr>
<td>&lt;light_purple&gt;
</td>
<td style="background-color:#FF55FF">
</td></tr>
<tr>
<td>&lt;red&gt;
</td>
<td style="background-color:#FF5555">
</td></tr>
<tr>
<td>&lt;white&gt;
</td>
<td style="background-color:white">
</td></tr>
<tr>
<td>&lt;yellow&gt;
</td>
<td style="background-color:#FFFF55">
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Special_Characters">特殊字符</h3></div></s></p>
<p><s><table border="1" class="wikitable" width="25%"></table></s></p>
<tbody><tr>
<td width="60%">&lt;&amp;nl&gt;
</td>
<td>新线
</td></tr>
<tr>
<td>&lt;&amp;cm&gt;
</td>
<td>,
</td></tr>
<tr>
<td>&lt;&amp;ss&gt;
</td>
<td>§
</td></tr>
<tr>
<td>&lt;&amp;sq&gt;
</td>
<td>'
</td></tr>
<tr>
<td>&lt;&amp;dq&gt;
</td>
<td>"
</td></tr>
<tr>
<td>&lt;&amp;co&gt;
</td>
<td>:
</td></tr>
<tr>
<td>&lt;&amp;rb&gt;
</td>
<td>]
</td></tr>
<tr>
<td>&lt;&amp;lb&gt;
</td>
<td>[
</td></tr>
<tr>
<td>&lt;&amp;rc&gt;
</td>
<td>}
</td></tr>
<tr>
<td>&lt;&amp;lc&gt;
</td>
<td>{
</td></tr>
<tr>
<td>&lt;&amp;ns&gt;
</td>
<td>#
</td></tr>
</tbody>
<p></p>
<p><s><div class="mw-heading mw-heading2"><h2 id="Pssst...">Pssst...</h2></div></s></p>
<p>~~<a href="http://pastebin.com/KBADLinZ">http://pastebin.com/KBADLinZ</a><br/>
以下是它们的摘要:)<br/>-Jeebs~~</p>

