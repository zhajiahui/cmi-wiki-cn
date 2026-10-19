---
title: 路径点
source_url: https://wiki.citizensnpcs.co/Waypoints
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5550
---


<a id="top"></a>

# 路径点

<p>NPCs 可以给出路径点以在其之间进行寻路。</p>
<p>航点由航点提供商创建。您可以使用 /waypoint provider [provider] 命令更改提供程序。</p>
<p>当前提供商 are:</p>
<p>线性（默认）- 按顺序将 NPC 发送到每个存储的航路点。</p>
<p>徘徊 - NPC 随机徘徊。</p>
<p>引导 - 航点分为目的地航点和辅助航点。目标航路点是随机选择的，并使用辅助航路点作为指导进行路径选择。例如在城市中巡逻 NPCs 时很有用，您希望它们大致沿着道路行驶。</p>
<a id="Waypoint_triggers"></a><h2 id="waypoint-triggers">航路点触发器</h2>
<p>对于线性和引导路径点提供程序，可以添加触发器以在某些路径点暂停 NPC、更改其速度或在路径点说一些话。通过在航路点编辑器中输入“触发器”可以找到更多信息。</p>
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
<td><a href="configuration.md" title="Configuration">配置</a> · <a href="text-syntax.md" title="Text Syntax">文本语法</a> · <a href="permissions.md" title="Permissions">权限</a> · 航点 · <a href="data-storage.md" title="Data Storage">数据存储</a></td>
</tr>
</tbody>
</table>

