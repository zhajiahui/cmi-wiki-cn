---
title: 数据存储
source_url: https://wiki.citizensnpcs.co/Data_Storage
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4949
---


<a id="top"></a>

# 数据存储

<p>Citizens2 中的数据存储通过以下两种方式之一进行处理：<a href="#saves.yml">YAML 平面文件</a> 或 NBT 文件。</p>
<a id="saves.yml"></a><h2 id="savesyml">saves.yml</h2>
<p>默认情况下使用<em>saves.yml</em>来存储创建的NPCs上的所有数据。</p>
<a id="Structure"></a><h3 id="structure">结构</h3>
<p>鼠标悬停查看 info:</p>
<div class="highlight"><pre># Citizens NPC Storage
npc:
  '0':
   name: My_First_NPC
   traits:
     age:
       age: 0
       locked: true
     spawned: true
     type: PLAYER
     owner: Steve
     lookclose: true
     location:
       world: world
       x: '92.65002360423462'
       y: '3.0'
       z: '-264.5621058817138'
       yaw: '87.90003967285156'
       pitch: '21.14999008178711'
     text:
       talk-close: true
       random-talker: true
       0: Hello, there. I'm My_First_NPC.
     waypoints:
       linear:
         points:
           '0':
             location:
               world: MyWorld
               x: 60
               y: 64
               z: 80
               pitch: 90
               yaw: 0
             delay: 0
           '1':
             location:
               world: MyWorld
               x: 65
               y: 64
               z: 82
               pitch: 45
               yaw: 0
             delay: 0
       provider: linear
</pre></div>
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
<td><a href="configuration.md" title="Configuration">配置</a> · <a href="text-syntax.md" title="Text Syntax">文本语法</a> · <a href="permissions.md" title="Permissions">权限</a> · <a href="waypoints.md" title="Waypoints">路径点</a> · 数据存储</td>
</tr>
</tbody>
</table>

