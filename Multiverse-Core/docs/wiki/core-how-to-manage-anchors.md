---
title: 传送锚点
source_url: https://mvplugins.org/core/how-to/manage-anchors/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 传送锚点

<a id="Introduction"></a><h2 id="introduction">介绍</h2>
<p>锚点是您可以保存并从服务器上的任何位置传送到的指定位置。它们的工作方式为 <a href="core-reference-destinations.md">目的地类型</a> — 在锚点名称前加上 <code>a:</code> 前缀，以便在接受目的地的任何地方使用锚点名称，包括 <a href="core-fundamentals-commands-usage.md#Teleport-Command"><code>/mv tp</code></a> 和 <a href="https://mvplugins.org/portals/">Multiverse-Portals</a>。</p>
<p>与世界生成或坐标不同，锚点是 <strong>与世界无关的</strong>：单个锚点可以指向任何世界中的任何位置。</p>
<a id="Creating-an-Anchor"></a><h2 id="creating-an-anchor">创建锚点</h2>
<p>走到你要保存的位置，然后run:</p>
<div class="highlight"><pre>/mv anchor set &lt;name&gt;
</pre></div>
<p>例如：</p>
<div class="highlight"><pre>/mv anchor set lobby
</pre></div>
<p>锚点保存在您当前的位置，包括面向方向。</p>
<p><strong>Permission:</strong> <code>multiverse.core.anchor.create</code></p>
<a id="Listing-Anchors"></a><h2 id="listing-anchors">列出锚点</h2>
<p>查看所有已保存的 anchors:</p>
<div class="highlight"><pre>/mv anchor list
</pre></div>
<p><strong>Permission:</strong> <code>multiverse.core.anchor.list</code></p>
<a id="Teleporting-to-an-Anchor"></a><h2 id="teleporting-to-an-anchor">传送到锚点</h2>
<p>将 <code>a:</code> 目标前缀与任何 teleport 命令一起使用：</p>
<div class="highlight"><pre>/mv tp a:&lt;name&gt;
/mv tp a:lobby
</pre></div>
<p>您还可以在 <a href="https://mvplugins.org/portals/">Multiverse-Portals</a> 或 <a href="https://mvplugins.org/signportals/">Multiverse-SignPortals</a> 中使用锚点作为传送门目标。</p>
<p><strong>Permission:</strong> <code>multiverse.teleport.self.a.*</code>（或更细粒度的 <code>multiverse.teleport.self.a.&lt;anchor-name&gt;</code>）</p>
<a id="Deleting-an-Anchor"></a><h2 id="deleting-an-anchor">删除锚点</h2>
<div class="highlight"><pre>/mv anchor delete &lt;name&gt;
</pre></div>
<p>例如：</p>
<div class="highlight"><pre>/mv anchor delete lobby
</pre></div>
<p><strong>Permission:</strong> <code>multiverse.core.anchor.delete</code></p>
<a id="Permission-Summary"></a><h2 id="permission-summary">权限摘要</h2>
<table>
<thead>
<tr>
<th>权限</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>multiverse.core.anchor.create</code></td>
<td>创建或覆盖锚点</td>
</tr>
<tr>
<td><code>multiverse.core.anchor.list</code></td>
<td>列出所有锚点</td>
</tr>
<tr>
<td><code>multiverse.core.anchor.delete</code></td>
<td>删除锚点</td>
</tr>
<tr>
<td><code>multiverse.teleport.self.a.*</code></td>
<td>将自己传送到任意锚点</td>
</tr>
<tr>
<td><code>multiverse.teleport.self.a.&lt;name&gt;</code></td>
<td>将自己传送到特定的锚点</td>
</tr>
<tr>
<td><code>multiverse.teleport.other.a.*</code></td>
<td>将其他人传送到任意锚点</td>
</tr>
</tbody>
</table>

