---
title: 文本语法
source_url: https://wiki.citizensnpcs.co/Text_Syntax
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5500
---


<a id="top"></a>

# 文本语法

<p>Citizens 中的配置语法很简单。如果可能，将解析并替换箭头括号 -- <code>&lt;&gt;</code> -- 内的节点。以下是您可以使用的可用节点。</p>
<a id="Chat_Colors"></a><h2 id="chat-colors">聊天颜色</h2>
<p>使用聊天颜色字符与任何其他插件相同。例如，<code>&amp;a</code> 会给您绿色。</p>
<p><strong>颜色参考</strong></p>
<p>0——黑色</p>
<p>1 -- 深蓝色</p>
<p>2 -- 深绿色</p>
<p>3 -- 青色</p>
<p>4 -- 深红色</p>
<p>5 -- 紫色</p>
<p>6 -- 黄金</p>
<p>7 -- 浅灰色</p>
<p>8 -- 灰色</p>
<p>9 -- 蓝色</p>
<p>一——绿色</p>
<p>b——水</p>
<p>c——玫瑰红</p>
<p>d——浅紫色</p>
<p>e——黄色</p>
<p>f——白色</p>
<p><strong>格式参考</strong></p>
<p>k——混淆</p>
<p>l——粗体</p>
<p>m——删除线</p>
<p>n——下划线</p>
<p>o——斜体</p>
<p>r——重置</p>
<p><a href="https://www.digminecraft.com/lists/color_list_pc.php">替代颜色/格式参考页</a></p>
<p>您还可以在 Minecraft 1.16+ 中使用十六进制颜色，使用 Spigot 的语法 - <code>&amp;x&amp;f&amp;f&amp;0&amp;0&amp;e&amp;e</code> 或 Essentials 的语法 - <code>&amp;#ff00ee</code>（两个示例产生相同的粉红色/洋红色）。</p>
<p>您也可以使用 <a href="https://docs.adventure.kyori.net/minimessage/format.html">MiniMessage</a>。</p>
<a id="Special"></a><h2 id="special">特别</h2>
<p>您可以使用 <code>&lt;br&gt;</code> 在文本行中间创建换行符。</p>
<a id="Other"></a><h2 id="other">其他</h2>
<p>您还可以在配置文件中使用其他节点。其中一些不适用于某些配置设置，因此请谨慎使用。未来将根据需要添加更多内容。</p>
<a id="NPC_Nodes"></a><h3 id="npc-nodes">NPC 节点</h3>
<p><code>&lt;npc&gt;</code> -- NPC 的名称</p>
<p><code>&lt;id&gt;</code> -- NPC 的 ID</p>
<p><code>&lt;owner&gt;</code> -- NPC 的所有者</p>
<a id="Player_Nodes"></a><h3 id="player-nodes">玩家节点</h3>
<p><code>&lt;player&gt;</code> -- 玩家姓名</p>
<p><code>&lt;world&gt;</code> -- 玩家的世界</p>
<p><code>&lt;nearest_player&gt;</code> -- 最接近 NPC 的玩家姓名</p>
<a id="Extra_Nodes"></a><h3 id="extra-nodes">额外节点</h3>
<p><code>&lt;random_player&gt;</code> -- 随机在线玩家名称</p>
<p><code>&lt;random_npc&gt;</code> -- 随机 NPC 名称</p>
<p><code>&lt;random_npc_id&gt;</code> -- 随机 NPC ID</p>
<a id="PlaceholderAPI"></a><h2 id="placeholderapi">PlaceholderAPI</h2>
<p>如果您的服务器上安装了 <a href="https://www.spigotmc.org/resources/placeholderapi.6245/">PlaceholderAPI</a>，则可以在 NPCs 上使用 PAPI 占位符，并在支持 PAPI 的任何地方使用特定的 Citizens PAPI 占位符。</p>
<a id="External_Placeholders_on_NPCs"></a><h3 id="external-placeholders-on-npcs">NPCs 上的外部占位符</h3>
<p>您可以使用任何 PAPI 占位符，就像在 NPC 文本或命令中的其他地方使用它们一样，以及 NPC 名称/全息图/等中的非玩家占位符。 <a href="frequently-asked-questions.md">有关非玩家限制的更多详细信息，请参阅常见问题解答</a>.</p>
<a id="Citizens_Placeholders"></a><h3 id="citizens-placeholders">Citizens 占位符</h3>
<p><code>%citizens_selected_npc_name%</code> -- 玩家选择的NPC 的名称。</p>
<p><code>%citizens_selected_npc_id%</code> -- 玩家选择的NPC的ID。</p>
<table>
<thead>
<tr>
<th>快速导航</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="category-usage.md" title="Category:Usage">用途</a></td>
<td><a href="installation.md" title="Installation">安装</a>  · <a href="frequently-asked-questions.md" title="Frequently Asked Questions">常见问题</a>  · <a href="commands.md" title="Commands">命令</a>  · <a href="editors.md" title="Editors">编辑器</a>  · <a href="characters.md" title="Characters">角色类型</a>  · <a href="https://wiki.citizensnpcs.co/API" title="API">API</a>  ·</td>
</tr>
<tr>
<td><a href="category-configuration.md" title="Category:Configuration">配置</a></td>
<td><a href="configuration.md" title="Configuration">配置</a>  · 文本语法  · <a href="permissions.md" title="Permissions">权限</a>  · <a href="waypoints.md" title="Waypoints">路径点</a>  · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

