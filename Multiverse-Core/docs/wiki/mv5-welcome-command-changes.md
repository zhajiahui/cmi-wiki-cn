---
title: MV5 命令变化
source_url: https://mvplugins.org/mv5/welcome/command-changes/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# MV5 命令变化

<table>
<thead>
<tr>
<th>旧的 MV4 语法</th>
<th>新的 MV5 语法</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/mv modify set &lt;property&gt; &lt;value&gt; [world]</code></td>
<td><code>/mv modify [world] set &lt;property&gt; &lt;value&gt;</code></td>
</tr>
<tr>
<td><code>/mv who [world]</code></td>
<td><code>/mv whoall</code> and <code>/mv who [world]</code></td>
</tr>
<tr>
<td><code>/mv anchor</code></td>
<td><code>/mv anchor list [--page &lt;page&gt;] [--filter &lt;filter&gt;]</code></td>
</tr>
<tr>
<td><code>/mv anchor &lt;name&gt;</code></td>
<td><code>/mv anchor set &lt;name&gt;</code></td>
</tr>
<tr>
<td><code>/mv anchor &lt;name&gt; -d</code></td>
<td><code>/mv anchor delete &lt;name&gt;</code></td>
</tr>
<tr>
<td><code>/mv gamerules [world]</code></td>
<td><code>/mv gamerule list [world] [--page &lt;page&gt;] [--filter &lt;filter&gt;]</code></td>
</tr>
<tr>
<td><code>/mv gamerule &lt;gamerule&gt; &lt;value&gt; [world]</code></td>
<td><code>/mv gamerule set &lt;gamerule&gt; &lt;value&gt; [world]</code></td>
</tr>
<tr>
<td><code>/mv purge [world/all] &lt;all/animals/monsters/mobname&gt;</code></td>
<td><code>/mv purge-all-entities &lt;spawn-categories&gt;</code></td>
</tr>
<tr>
<td><code>/mv modify set animals &lt;true/false&gt; [world]</code></td>
<td><code>/mv entity-spawn-config modify [world] animal set spawn &lt;true/false&gt;</code></td>
</tr>
<tr>
<td><code>/mv generators</code></td>
<td><code>/mv generators list</code> and <code>/mv generators info &lt;generator&gt;</code></td>
</tr>
<tr>
<td><code>/mv version -p</code></td>
<td><code>/mv dumps</code></td>
</tr>
<tr>
<td><code>/mv env</code></td>
<td><em>已删除</em></td>
</tr>
<tr>
<td><code>/mv silent</code></td>
<td><em>已删除</em></td>
</tr>
</tbody>
</table>

