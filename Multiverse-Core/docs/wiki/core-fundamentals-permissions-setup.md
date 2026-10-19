---
title: 权限设置
source_url: https://mvplugins.org/core/fundamentals/permissions-setup/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 权限设置

<div class="admonition tip">
<p class="admonition-title">能直接获得所有权限吗？</p>
<p>完整权限清单见<a href="core-reference-permissions-list.md">权限列表页</a>。</p>
</div>
<a id="Multiverse-支持的权限插件"></a><a id="Multiverse-Permissions-Plugin-Support"></a><h2 id="multiverse">Multiverse 支持的权限插件</h2>
<p>Multiverse 支持任何遵循 SuperPerms Bukkit Permissions API 的权限插件。目前主要使用 <a href="https://luckperms.net/">LuckPerms</a>，也可以选择其他插件。</p>
<a id="Multiverse-世界权限"></a><a id="Multiverse-World-Permissions"></a><h2 id="multiverse_1">Multiverse 世界权限</h2>
<p>Multiverse 允许通过权限控制谁能进入各个世界。创建世界或将世界导入 Multiverse-Core 时，插件会自动创建 <code>multiverse.access.[worldname]</code> 权限。玩家_拥有_ <code>multiverse.access.[worldname]</code> 时，才能进入对应世界。</p>
<div class="admonition note">
<p class="admonition-title">注意</p>
<p>使用此权限前，必须在 Multiverse 的 <a href="core-reference-configuration-file.md"><code>config.yml</code></a> 中<strong>启用</strong> <code>enforceaccess</code>。如果 <code>enforceaccess</code> 为 <code>false</code>，_任何人_都能进入_任何_世界，<strong>所有世界访问权限都会被忽略</strong>。</p>
</div>
<p>授予用户 <code>multiverse.access.*</code> 后，他就能进入所有世界。</p>
<a id="Multiverse-权限"></a><a id="Multiverse-Permissions"></a><h3 id="multiverse_2">Multiverse 权限</h3>
<p><code>multiverse.*</code> 可以授予用户所有 Multiverse 权限。如果只是希望他能访问所有世界，使用 <code>multiverse.access.*</code> 即可。</p>
<a id="在游戏中设置权限"></a><a id="Setting-Permissions-in-game"></a><h2 id="_1">在游戏中设置权限</h2>
<p>如果执行 /命令 时因权限不足而失败，Multiverse 会显示该命令所需的权限节点。这样就省去了查找权限的时间，也方便管理员根据需要当场为权限组添加权限。例如，执行 <a href="core-fundamentals-commands-usage.md#List-Command"><code>/mvlist</code></a> 时没有权限，插件会提示需要 <code>multiverse.world.list</code>。执行：</p>
<div class="admonition note">
<p class="admonition-title">注意</p>
<p>下面的命令使用 <a href="https://luckperms.net/">LuckPerms</a>。如果使用其他权限插件，请改用相应命令。</p>
</div>
<div class="highlight"><pre>/lp &lt;group/user&gt; &lt;group name or username&gt; permission set multiverse.core.list true
</pre></div>
<p>例如：</p>
<div class="highlight"><pre>/lp group admin permission set multiverse.core.list true
</pre></div>
<p>这样会把权限添加到 admin 组，该组就能使用对应命令。MV 的命令和权限很多，按实际需要逐项添加有时更方便。</p>
<a id="设置-OP"></a><a id="Setting-OP's"></a><h2 id="op">设置 OP</h2>
<p>OP 默认拥有所有设为 true 的 Multiverse 权限。因此，让管理员成为 OP 是授予全部 Multiverse 权限最直接的方法，但并不一定适合所有服务器。</p>
<div class="admonition warning">
<p class="admonition-title">OP 可能影响部分功能！</p>
<p>OP 拥有_所有_权限，其中也包括 <code>mv.bypass.gamemode.*</code>，因此会绕过 Multiverse 的游戏模式管理。使用 OP 时请留意这一点。</p>
</div>
<a id="访问权限操作记录示例"></a><a id="Sample-Access-Permissions-Transcript"></a><h2 id="_2">访问权限操作记录示例</h2>
<p>许多人不太容易理解访问权限如何生效。下面是原作者 @FernFerret 在测试服上的实际聊天与操作记录，内容如实记录了当时的情况。<code>&gt;</code> 表示在控制台输入的命令。</p>
<div class="highlight"><pre>11:18:38 [INFO] [world2]&lt;fernferret&gt; I do not have multiverse.core.list.worlds, I can't see any worlds
&gt;perm player setperm fernferret multiverse.core.list.worlds true
11:18:59 [INFO] Player fernferret now has multiverse.core.list.worlds = true.
11:19:15 [INFO] [world2]&lt;fernferret&gt; cool. I can see the world list, but there are 0 worlds listed
&gt;perm player setperm fernferret multiverse.access.world true
11:19:32 [INFO] Player fernferret now has multiverse.access.world = true.
11:19:42 [INFO] [world2]&lt;fernferret&gt; sweet. Now I can see the world 'world'
11:20:08 [INFO] [world2]&lt;fernferret&gt; I can't TP there though, I don't have *any* multiverse.teleport.X perm nodes
&gt;perm player setperm fernferret multiverse.teleport.self.* true
11:20:26 [INFO] Player fernferret now has multiverse.teleport.self.* = true.
11:20:38 [INFO] [world]&lt;fernferret&gt; woo I'm in 'world'
11:20:54 [INFO] [world]&lt;fernferret&gt; now I can't tp to 'world' again, i need the spawn.self perm...
&gt;perm player setperm fernferret multiverse.core.spawn.self true
11:21:05 [INFO] Player fernferret now has multiverse.core.spawn.self = true.
11:21:18 [INFO] [world]&lt;fernferret&gt; woo! now i'm at spawn!!!!!!111!
11:21:31 [INFO] [world]&lt;fernferret&gt; but I can't go back to world2...
11:21:34 [INFO] [world]&lt;fernferret&gt; I need some perms!
&gt;perm player setperm fernferret multiverse.access.world2 true
11:21:44 [INFO] Player fernferret now has multiverse.access.world2 = true.
11:21:56 [INFO] [world2]&lt;fernferret&gt; hellz yea!!!!111! world2!!
11:24:05 [INFO] [world2]&lt;fernferret&gt; hmm ok, let's not give me the exact teleport perm... i'll test now!
11:24:15 [INFO] [world]&lt;fernferret&gt; ow...
11:24:20 [INFO] [world]&lt;fernferret&gt; i'm underground somewhere
11:24:25 [INFO] [world]&lt;fernferret&gt; the exact perm is dangerous
&gt;perm player setperm fernferret multiverse.teleport.self.e false
11:24:40 [INFO] Player fernferret now has multiverse.teleport.self.e = false.
11:24:51 [INFO] [world]&lt;fernferret&gt; I went back to spawn
11:25:26 [INFO] [world]&lt;fernferret&gt; ok. I gave myself the false exact perm
11:25:36 [INFO] [world]&lt;fernferret&gt; but that gets checked _after_ the higher perm
11:25:48 [INFO] [world]&lt;fernferret&gt; so I  need to deny myself the parent, and just give myself the child perms
&gt;perm player setperm fernferret multiverse.teleport.self.* false
11:26:14 [INFO] Player fernferret now has multiverse.teleport.self.* = false.
11:26:24 [INFO] [world]&lt;fernferret&gt; ok. I have no tp perms again.
11:26:35 [INFO] [world]&lt;fernferret&gt; now i'll _just_ give myself the ones I want, world and player
&gt;perm player setperm fernferret multiverse.teleport.self.w true
11:26:41 [INFO] Player fernferret now has multiverse.teleport.self.w = true.
&gt;perm player setperm fernferret multiverse.teleport.self.pl true
11:26:47 [INFO] Player fernferret now has multiverse.teleport.self.pl = true.
11:26:55 [INFO] [world]&lt;fernferret&gt; oh, and cannon! cannons are awesome!
&gt;perm player setperm fernferret multiverse.teleport.self.ca true
11:27:00 [INFO] Player fernferret now has multiverse.teleport.self.ca = true.
11:27:15 [INFO] [world]&lt;fernferret&gt; weeeeeeeeeeeee (shot out of cannon)
</pre></div>

