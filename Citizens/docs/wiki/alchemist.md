---
title: Alchemist
source_url: https://wiki.citizensnpcs.co/Alchemist
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4825
---


<a id="top"></a>

# Alchemist

<p><a href="https://wiki.citizensnpcs.co/File:Alchemist.png"><img alt="" src="assets/2c66e6ccf806-Alchemist.png"/></a> </p>
<p><strong>Alchemist</strong></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>作者</strong></td>
<td>一拳</td>
</tr>
<tr>
<td><strong>版本</strong></td>
<td>1.1</td>
</tr>
<tr>
<td><strong>Citizens 构建</strong></td>
<td>2.0</td>
</tr>
<tr>
<td><strong>其他依赖项</strong></td>
<td>无</td>
</tr>
<tr>
<td><strong>下载</strong></td>
<td><a href="http://ci.citizensnpcs.co/view/Add-ons/job/Alchemist/">链接</a></td>
</tr>
<tr>
<td><strong>Description:</strong> 可定制药水配方</td>
<td></td>
</tr>
</tbody>
</table>
<p>Alchemist 是 Citizens 2.0 角色特征，赋予 NPCs 能力 to:</p>
<ul>
<li>根据预先定义的配方制作药水。</li>
<li>收取他们的服务费用。</li>
</ul>
<a id="How_to_Use"></a><h2 id="how-to-use">如何使用</h2>
<a id="General_Information"></a><h3 id="general-information">一般信息</h3>
<p>炼金术士提供了为药水创建自定义配方的能力。您可以在配置文件中自定义这些配方。提供默认配方作为示例。</p>
<p>请记住，使用此插件无法查看炼金术士当前的配方成分。这是故意的，因为您（服务器管理员）应该拥有完全的自由来决定如何显示配方。你可以使用标志、另一个插件来显示成分，或者根本不显示成分。</p>
<a id="Interaction"></a><h3 id="interaction">互动</h3>
<p>用适当的成分右键点击炼金术士会将它们从你的手中移走并将其交给炼金术士。一旦配方完全完成，炼金术士就会在其所在位置周围掉落一瓶药水。如果使用者走得太远，炼金术士将停止酿造药水，并且给予其的任何物品都将丢失。</p>
<a id="Commands"></a><h2 id="commands">命令</h2>
<p>要使用炼金术士命令，您必须选择 NPC 并且是该 NPC 的所有者。命令不需要权限节点。</p>
<table>
<thead>
<tr>
<th><strong>Alchemist 命令</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Command</td>
<td>描述</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/alchemist help</td>
<td>显示帮助菜单</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/alchemist recipe</td>
<td>显示炼金术士当前的配方</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>/alchemist recipe [name]</td>
<td>设置炼金术士当前的配方。</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<a id="Permissions"></a><h2 id="permissions">权限</h2>
<p>使用炼金术士，只需要一个权限节点。权限节点<em>alchemist.interact</em>允许玩家与炼金术士进行交互。</p>
<a id="Configuration"></a><h2 id="configuration">配置</h2>
<p>炼金术士的配置文件位于 <em>/plugins/Alchemist/config.yml</em> 中，如果不存在，则会自动生成。</p>
<a id="Default_Configuration"></a><h3 id="default-configuration">默认配置</h3>
<p>将鼠标悬停在每个部分上可查看其说明。</p>
<div class="highlight"><pre># Alchemist Configuration
recipes:
 default:
   result:
     effect: fire-resistance
     duration: 60
     amplifier: 1
     splash: false
   ingredients:
     '0':
       name: sugar
       amount: 1
     '1':
       name: glass-bottle
       amount: 1
     '2':
       name: wool
       amount: 1
       data: 6
messages:
 initialization-message: &lt;e&gt;Hello there, &lt;player&gt;. Give me what I need and I will brew you a potion!
 success-message: &lt;e&gt;I have combined the ingredients to concoct a potion of &lt;a&gt;&lt;potion&gt;&lt;e&gt;.
 cooldown-not-expired: You've already had your turn. Come back later!
cooldown-in-seconds: 60
</pre></div>
<a id="Valid_Effects"></a><h2 id="valid-effects">有效效果</h2>
<ul>
<li><em>speed</em> - 提高移动速度。</li>
<li><em>slow</em> - 降低移动速度。</li>
<li><em>fast-digging</em> - 提高挖掘速度。</li>
<li><em>slow-digging</em> - 降低挖掘速度。</li>
<li><em>increase-damage</em> - 增加造成的伤害。</li>
<li><em>heal</em> - 立即治愈玩家。</li>
<li><em>harm</em> - 立即伤害玩家。</li>
<li><em>jump</em> - 增加跳跃高度。</li>
<li><em>confusion</em> - 扭曲玩家客户端的视野。</li>
<li><em>regeneration</em> - 恢复健康。</li>
<li><em>damage-resistance</em> - 减少对玩家造成的伤害。</li>
<li><em>fire-resistance</em> - 增加对火的影响的抵抗力。</li>
<li><em>water-breathing</em> - 允许在水下呼吸。</li>
<li><em>blindness</em> - 使玩家失明。</li>
<li><em>hunger</em> - 增加饥饿感。</li>
<li><em>weakness</em> - 减少玩家造成的伤害。</li>
<li><em>poision</em> - 随着时间的推移对玩家造成伤害。</li>
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

