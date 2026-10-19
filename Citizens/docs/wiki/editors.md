---
title: 编辑器
source_url: https://wiki.citizensnpcs.co/Editors
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5017
---


<a id="top"></a>

# 编辑器

<p>编辑器用于以简单的方式进一步编辑 NPCs。这些事情被认为太复杂而不需要只是编辑命令。在所有编辑器中，您必须键入一次关联命令才能进入编辑器，然后再次键入才能退出编辑器。 <strong>您一次只能使用一个编辑器。</strong></p>
<a id="Text_Editor"></a><h2 id="text-editor">文本编辑器</h2>
<p>命令：/npc 文本</p>
<p>编辑 NPC 的文本很简单。按照游戏中的说明添加、编辑和删除 NPCs 中的文本。 NPC 是“随机说话者”，意味着它将重复其文本列表中的随机短语。如果“random”为 false，它将线性循环文本。通过输入“close”来更改其近距离说话者设置将切换 NPC 当玩家进入 5 个方块内时是否说话。如果 close 为 false，则 NPC 仅在点击可配置通话项目时才会通话。如果 close 为 true，则只有当玩家靠近时它才会说话。</p>
<p><strong>请注意，玩家需要 citizens.npc.talk 权限才能听到 NPCs！</strong></p>
<p>重要 note: 在聊天中输入“退出”以关闭编辑器！</p>
<p>另请参阅 <a href="text-syntax.md" title="Text Syntax">文本语法</a></p>
<a id="Waypoint_Editor"></a><h2 id="waypoint-editor">航点编辑器</h2>
<p>命令：/npc路径</p>
<p>请参阅 <a href="waypoints.md" title="Waypoints">路径点</a> 页面了解更多信息。</p>
<a id="Equipment_Editor"></a><h2 id="equipment-editor">装备编辑</h2>
<p>命令：/npc装备</p>
<p>装备是 NPCs 上的盔甲、持有物品和其他可见特征。仅某些 NPC 类型可以编辑其设备。</p>
<a id="Generic"></a><h3 id="generic">通用</h3>
<p>随着 1.4.5 中新生物装备的更新，此处未列出的任何生物都将默认为人类装备风格。请注意，该装备可能无法在所有生物上正确显示，因为有些生物不支持它。</p>
<a id="Humans_(regular_NPCs)"></a><h3 id="humans-regular-npcs">人类（常规 NPCs）</h3>
<p>人类NPCs可以修改他们的盔甲和持有的物品。要为 NPC 提供护甲，请右键点击手中有护甲的护甲。装甲放置在NPC的身上。之前在 NPC 上的任何物品或盔甲都将被移除并掉落到地面上。要将盔甲放置在 NPC 的手中，<em>蹲下</em> 并右键点击。要清除所有物品，请右键点击手上没有物品的NPC。</p>
<a id="Endermen"></a><h3 id="endermen">末影人</h3>
<p>Enderman NPCs 可以修改其携带的材料。末影人唯一有效的材料可以容纳的是块 - 大多数项目不会出现在客户端上。请注意，某些 "utility" 块如路标、蠹鱼客户端上也出现<em>不</em>。在手上没有物品的情况下点击即可移除末影人 NPC 上的方块。</p>
<a id="Sheep"></a><h3 id="sheep">羊</h3>
<p>绵羊 NPCs 可以修改羊毛颜色和剪毛状态。要剪切，请像平常一样用剪刀右键点击。要取消对羊 NPC 的剪毛，请再次用剪刀点击它。要更改羊毛颜色，请点击带有染料的羊 NPC。点击手中除染料以外的任何东西都会将羊 NPC 变成白色并将染料滴在地上。</p>
<a id="Pigs"></a><h3 id="pigs">猪</h3>
<p>Pig NPCs 可以添加和移除马鞍。只需右键点击手上有马鞍的猪 NPC 即可。点击手中的任何其他物品都会从猪 NPC 上取下马鞍。</p>
<a id="Clientside_Issues"></a><h3 id="clientside-issues">客户端问题</h3>
<p>某些设备编辑器存在已知的客户端问题。如果您遇到问题，很可能是客户端问题。尝试重新登录，如有必要，重新启动服务器。如果您仍然认为问题存在，请报告问题 <a href="http://issues.citizensnpcs.net">这里</a>。</p>
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
<td><a href="installation.md" title="Installation">安装</a>  · <a href="frequently-asked-questions.md" title="Frequently Asked Questions">常见问题</a>  · <a href="commands.md" title="Commands">命令</a>  · 编辑  · <a href="characters.md" title="Characters">角色类型</a>  · <a href="https://wiki.citizensnpcs.co/API" title="API">API</a>  ·</td>
</tr>
<tr>
<td><a href="category-configuration.md" title="Category:Configuration">配置</a></td>
<td><a href="configuration.md" title="Configuration">配置</a>  · <a href="text-syntax.md" title="Text Syntax">文本语法</a>  · <a href="permissions.md" title="Permissions">权限</a>  · <a href="waypoints.md" title="Waypoints">路径点</a>  · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

