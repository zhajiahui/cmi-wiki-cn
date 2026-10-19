---
title: 兼容性
source_url: https://wiki.citizensnpcs.co/Compatibility
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=3858
---


<a id="top"></a>

# 兼容性

<p>Citizens 2.0.4 的已知兼容性问题</p>
<ul>
<li>Citizens 需要 CraftBukkit 1.4.5+</li>
<li>设置 pvp=false 可能会破坏 NPCs 上的左键点击，因为这被视为攻击 NPC 并且该事件不会触发。</li>
<li>在以下 circumstances: 下可以阻止敌对生物类型 NPCs 的生成</li>
<li>
<p>有一个插件以最高优先级阻止生成，插件列表：</p>
<ul>
<li>Essentials 将阻止 npc 生成</li>
<li>WorldGuard 不会阻止 npc 生成</li>
<li>MultiVerse 不会阻止 npc 生成</li>
</ul>
</li>
<li>
<p>Authme 尝试连接 Citizen2 时可能会抛出控制台错误。</p>
</li>
<li>PvPToggle 尝试连接 Citizen2 时可能会抛出控制台错误。</li>
<li>TeleportSuite 可能会抛出寻找 NPCs 的控制台错误。</li>
<li>HomeSpawnPlus 可能会阻止使用棒进行右键点击选择。</li>
<li>APIPlus 可能会阻止所有右键点击</li>
<li>PopulationDensity/GriefPrevention 可能会干扰服务器启动时 NPCs 的生成，并可能在 /reload 时复制它们。</li>
<li><a href="http://dev.bukkit.org/server-mods/heroes/">英雄</a> 已知玩家类型 NPCs 存在问题。请不要向他们发送门票，我们正在尝试与 Kainzo 合作解决此问题。</li>
<li>CityScape 使用 /npc 命令。如果安装了两个插件，请使用 /npc2 运行 Citizen2 命令。</li>
</ul>
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
<td><a href="configuration.md" title="Configuration">配置</a>  · <a href="text-syntax.md" title="Text Syntax">文本语法</a>  · <a href="permissions.md" title="Permissions">权限</a>  · <a href="waypoints.md" title="Waypoints">路径点</a>  · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

