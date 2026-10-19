---
title: Multiverse-Core 权限清单
source_url: https://mvplugins.org/core/reference/permissions-list/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# Multiverse-Core 权限清单

<a id="Help-Permissions"></a><h2 id="help-permissions">帮助权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Help-Command">multiverse.help</a> - 允许用户使用 /mv 帮助</p>
<a id="Access-Permissions"></a><h2 id="access-permissions">访问权限</h2>
<p>multiverse.access.[worldname] - 允许用户使用指定的世界</p>
<p><a href="core-fundamentals-world-properties.md#World-Fees">multiverse.exempt.[worldname]</a> - 让用户免付费世界</p>
<p><a href="core-fundamentals-world-properties.md#Gamemode">mv.bypass.gamemode.[worldname]</a> - 允许用户在访问世界时绕过配置的<code>gamemode</code></p>
<p><a href="core-fundamentals-world-properties.md#Player-Limit">mv.bypass.playerlimit.[worldname]</a> - 允许用户在访问世界时绕过配置的<code>playerlimit</code></p>
<p>mv.bypass.joinlocation - 允许用户在登录服务器时绕过 config.yml 中配置的 <code>join-location</code>。</p>
<a id="Teleport-Permissions"></a><h2 id="teleport-permissions">传送权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Teleport-Command">multiverse.teleport.self.[type].[finer-permission]</a> - 允许用户将自己传送到另一个世界。</p>
<p><a href="core-fundamentals-commands-usage.md#Teleport-Command">multiverse.teleport.other.[type].[finer-permission]</a> - 允许用户将自己和他人传送到另一个世界。</p>
<p><strong>注意事项</strong>：如果<code>enforce-access</code>打开（设置为<code>true</code>），他们只能传送到他们拥有<code>multiverse.access.WORLD</code>权限的世界。默认情况下，这是 <code>false</code>，他们可以访问 <strong>ALL</strong> 世界。</p>
<a id="Teleport-types:"></a><h3 id="teleport-types">传送 types:</h3>
<ul>
<li><code>w</code> = 世界</li>
<li><code>p</code> = 传送门</li>
<li><code>a</code> = 锚</li>
<li><code>e</code> = 确切目的地（坐标）</li>
<li><code>pl</code> = 玩家</li>
<li><code>ca</code> = 大炮</li>
<li><code>b</code> = 床</li>
</ul>
<p><strong>另请参阅：</strong> <a href="core-reference-destinations.md">目的地详情</a></p>
<a id="Info-Permissions"></a><h2 id="info-permissions">信息权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Check-Command">multiverse.core.check</a> - 允许检查玩家是否可以传送到目的地</p>
<p><a href="core-fundamentals-commands-usage.md#Confirm-Command">multiverse.core.confirm</a></p>
<p><a href="core-fundamentals-commands-usage.md#Coordinate-Command">multiverse.core.coord</a></p>
<p><a href="core-fundamentals-commands-usage.md#Info-Command">multiverse.core.info</a></p>
<p><a href="core-fundamentals-commands-usage.md#Who-Command">multiverse.core.list.who</a></p>
<p><a href="core-fundamentals-commands-usage.md#Who-All-Command">multiverse.core.list.who.all</a></p>
<p><a href="core-fundamentals-commands-usage.md#List-Command">multiverse.core.list.worlds</a></p>
<p><a href="core-fundamentals-commands-usage.md#Version-Command">multiverse.core.version</a> - 允许查看已安装的 Multiverse 版本</p>
<hr/>
<a id="World-Management-Permissions"></a><h2 id="world-management-permissions">世界管理权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Create-Command">multiverse.core.create</a> - 允许用户创建世界</p>
<p><a href="core-fundamentals-commands-usage.md#Clone-Command">multiverse.core.clone</a> - 允许用户复制世界</p>
<p><a href="core-fundamentals-commands-usage.md#Import-Command">multiverse.core.import</a> - 允许用户导入世界</p>
<p><a href="core-fundamentals-commands-usage.md#Modify-Command">multiverse.core.modify</a> - 允许用户修改世界</p>
<p><a href="core-fundamentals-commands-usage.md#Regen-Command">multiverse.core.regen</a></p>
<p><a href="core-fundamentals-commands-usage.md#Remove-Command">multiverse.core.remove</a></p>
<p><a href="core-fundamentals-commands-usage.md#Load-Command">multiverse.core.load</a></p>
<p><a href="core-fundamentals-commands-usage.md#Unload-Command">multiverse.core.unload</a></p>
<p><a href="core-fundamentals-commands-usage.md#Delete-Command">multiverse.core.delete</a></p>
<a id="Spawn-Permissions"></a><h2 id="spawn-permissions">生成权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Spawn-Command">multiverse.core.spawn.other.[worldname]</a></p>
<p><a href="core-fundamentals-commands-usage.md#Spawn-Command">multiverse.core.spawn.self.[worldname]</a></p>
<p><a href="core-fundamentals-commands-usage.md#Set-Spawn-Command">multiverse.core.spawn.set</a></p>
<a id="Entities-Management-Permissions"></a><h2 id="entities-management-permissions">实体管理权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Info-Command">multiverse.core.entityspawnconfig.info</a></p>
<p><a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command">multiverse.core.entityspawnconfig.modify</a></p>
<p><a href="core-fundamentals-commands-usage.md#Purge-Entities-Command">multiverse.core.purge</a></p>
<p><a href="core-fundamentals-commands-usage.md#Purge-All-Entities-Command">multiverse.core.purgeall</a></p>
<a id="Anchor-Permissions"></a><h2 id="anchor-permissions">锚点权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Anchor-Set-Command">multiverse.core.anchor.create</a></p>
<p><a href="core-fundamentals-commands-usage.md#Anchor-List-Command">multiverse.core.anchor.list</a></p>
<p><a href="core-fundamentals-commands-usage.md#Anchor-Delete-Command">multiverse.core.anchor.delete</a></p>
<a id="World-Border-Permissions"></a><h2 id="world-border-permissions">世界边境许可</h2>
<p><a href="core-fundamentals-commands-usage.md#World-Border-Add-Command">multiverse.core.worldborder</a> - 允许使用所有 <code>/mv worldborder</code> 子命令</p>
<a id="Misc-Permissions"></a><h2 id="misc-permissions">其他权限</h2>
<p><a href="core-fundamentals-commands-usage.md#Config-Command">multiverse.core.config</a></p>
<p><a href="core-fundamentals-commands-usage.md#Dumps-Command">multiverse.core.dumps</a> - 允许上传调试信息</p>
<p><a href="core-fundamentals-commands-usage.md#Reload-Command">multiverse.core.reload</a> - 允许用户重新加载配置文件</p>
<p><a href="core-fundamentals-commands-usage.md#Debug-Command">multiverse.core.debug</a></p>

