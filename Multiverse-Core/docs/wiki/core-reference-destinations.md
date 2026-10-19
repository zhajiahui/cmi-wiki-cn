---
title: 传送目的地
source_url: https://mvplugins.org/core/reference/destinations/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 传送目的地

<a id="Index"></a><h2 id="index">索引</h2>
<ul>
<li><a href="#World-Destinations">世界目的地</a></li>
<li><a href="#Anchor-Destinations">锚点目的地</a></li>
<li><a href="#Exact-Destinations">确切的目的地</a></li>
<li><a href="#Player-Destinations">玩家目的地</a></li>
<li><a href="#Cannon-Destinations">加农炮目的地</a></li>
<li><a href="#Bed-Destinations">床位目的地</a></li>
<li><a href="#Portal-Destinations">传送门目的地</a></li>
</ul>
<a id="Destination-Permissions"></a><h2 id="destination-permissions">目的地权限</h2>
<p>目的地需要使用 <a href="core-fundamentals-commands-usage.md#Teleport-Command"><code>/mvtp</code></a> 传送到的权限。默认情况下，您需要 <code>multiverse.teleport.self.&lt;destination&gt;</code> 和 <code>multiverse.teleport.self.&lt;destination&gt;.&lt;world&gt;</code>。可以使用 <a href="core-reference-configuration-file.md">config.yml</a> 中的 <code>use-finer-teleport-permissions</code> 配置选项将其更改为仅需要 <code>multiverse.teleport.self.&lt;destination&gt;</code> 权限。从 MV4 迁移到 MV5 时，此选项设置为 <code>false</code>，但对于新安装的插件，此选项设置为 <code>true</code>。</p>
<a id="World-Destinations"></a><h2 id="world-destinations">世界目的地</h2>
<p>全球目的地可以以 <code>w:</code> 为前缀，但这不是必需的，除非您包含方向。如果没有找到目的地的前缀，则假定它是一个世界。您还可以添加一个方向来在世界中生成玩家，就像传送门一样。</p>
<a id="Examples"></a><h3 id="examples">示例</h3>
<ul>
<li><code>/mvtp world</code></li>
<li><code>/mvtp w:world</code></li>
<li><code>/mvtp w:world:se</code></li>
</ul>
<a id="Permissions"></a><h3 id="permissions">权限</h3>
<p><code>multiverse.teleport.self.w</code>
<code>multiverse.teleport.other.w</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.w.&lt;worldname&gt;</code></p>
<a id="Anchor-Destinations"></a><h2 id="anchor-destinations">锚点目的地</h2>
<p>如果您有经常要去的地方，应该使用 <a href="core-how-to-manage-anchors.md">锚</a>。首先使用 <code>/mv anchor set &lt;name&gt;</code> 命令创建 <a href="core-how-to-manage-anchors.md">锚</a>，然后您可以在任何采用目标的命令中使用它。</p>
<a id="Examples"></a><h3 id="examples_1">示例</h3>
<p><code>/mvtp a:myplace</code></p>
<a id="Permissions"></a><h3 id="permissions_1">权限</h3>
<p><code>multiverse.teleport.self.a</code>
<code>multiverse.teleport.other.a</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.a.&lt;anchorname&gt;</code></p>
<a id="Exact-Destinations"></a><h2 id="exact-destinations">确切的目的地</h2>
<p>如果您确切地知道某人应该在哪里生成，那么确切的目的地很有用，但它们很难设置，因为需要输入很多内容！幸运的是，设置精确目的地的一个简单方法是使用：<code>/mvp modify destination e:@here</code>，这会将目的地设置为当前位置的精确目的地，<strong>包括你正在寻找的地方</strong>。如果您希望人们看到您的精彩创作，这非常棒！还支持相对位置，因此您可以使用 <code>~,~1,~</code> 在当前玩家坐标上方一个方块处生成玩家。</p>
<a id="Examples"></a><h3 id="examples_2">示例</h3>
<p><code>/mvtp e:world:0,0,0</code><br/>
<code>/mvtp e:world:0,0,0:0:0</code>
<code>/mvtp e:world:~,~,~</code><br/>
<code>/mvtp e:world:~,~1,~:0:0</code></p>
<a id="Permissions"></a><h3 id="permissions_2">权限</h3>
<p><code>multiverse.teleport.self.e</code>
<code>multiverse.teleport.other.e</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.e.&lt;worldname&gt;</code></p>
<a id="Player-Destinations"></a><h2 id="player-destinations">玩家目的地</h2>
<p>玩家目的地正如他们听起来的那样，他们总是会将您传送到 <em>具体的</em> 玩家！如果该玩家不在线，您将无法传送，或者如果您正在使用传送门，它将表现得好像它处于非活动状态。如果玩家尝试传送到自己身边，什么也不会发生。</p>
<a id="Examples"></a><h3 id="examples_3">示例</h3>
<p><code>/mvtp pl:fernferret</code></p>
<a id="Permissions"></a><h3 id="permissions_3">权限</h3>
<p><code>multiverse.teleport.self.pl</code>
<code>multiverse.teleport.other.pl</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.pl.&lt;playername&gt;</code></p>
<a id="Cannon-Destinations"></a><h2 id="cannon-destinations">加农炮目的地</h2>
<p>对于 Cannon Destinations，您必须记住的是 <strong>你永远不会看到大炮</strong>。这有效地定义了具有速度的目的地。它可能类似于 TNT 爆炸产生的推动力。它看起来也有点像你在以某种方式弹射，因此得名 <strong>加农炮</strong>！</p>
<div class="admonition note">
<p>大炮目的地的速度太高（&gt;40~）可能会导致失败。 <code>spigot.yml</code>中的<code>moved-wrongly-threshold</code>和<code>moved-too-quickly-multiplier</code>可以增加，e.g。 <code>.inf</code> 将它们设置为无穷大，从而有效地禁用它们。然而，即使具有这些高阈值，非常高的速度也可能会触发其他故障，例如缓慢的块加载或网络不同步。</p>
</div>
<a id="Examples"></a><h3 id="examples_4">示例</h3>
<p><code>/mvtp ca:world:x,y,z:pitch:yaw:speed</code>
<code>/mvtp ca:world:-22.48,63.00,-34.43:-7.15:44.40:10</code></p>
<a id="Permissions"></a><h3 id="permissions_4">权限</h3>
<p><code>multiverse.teleport.self.ca</code>
<code>multiverse.teleport.other.ca</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.ca.&lt;worldname&gt;</code></p>
<a id="Bed-Destinations"></a><h2 id="bed-destinations">床位目的地</h2>
<p>将玩家带到指定玩家死亡后将生成的床上。对于自己的玩家床位置，请使用 <code>playerbed</code>。</p>
<a id="Examples"></a><h3 id="examples_5">示例</h3>
<p><code>/mvtp b:playername</code>
<code>/mvtp b:playerbed</code> - 将玩家传送到他们自己的床上。</p>
<a id="Permissions"></a><h3 id="permissions_5">权限</h3>
<p><code>multiverse.teleport.self.b</code>
<code>multiverse.teleport.other.b</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.pl.&lt;playername&gt;</code></p>
<a id="Portal-Destinations"></a><h2 id="portal-destinations">传送门目的地</h2>
<div class="admonition note">
<p class="admonition-title">注意事项</p>
<p>需要 <a href="https://mvplugins.org/portals/">Multiverse-Portals</a></p>
</div>
<p>传送门目标类型将玩家传送到指定的传送门。它们仅在您安装了 <a href="https://mvplugins.org/portals/">Multiverse-Portals</a> 后才可用。如果您希望玩家在被放置到目的地时面向不同的方向，您可以添加以下任何一个冒号（如下所示两次）<code>n,e,s,w,ne,nw,se,sw</code>（或使用全名：<code>north,east,south,west,northeast,northwest,southeast,southwest</code>）</p>
<a id="Examples"></a><h3 id="examples_6">示例</h3>
<p><code>/mvtp p:portal</code><br/>
<code>/mvtp p:portal:n</code><br/>
<code>/mvtp p:portal:sw</code></p>
<a id="Special-case"></a><h3 id="special-case">特殊情况</h3>
<p>当您位于传送门中的 <em>站立</em>（假设为 <code>PortalB</code>）时，如果您想将另一个传送门（<code>PortalA</code>）的目的地设置为 <strong>该传送门的中心面向圆形方向</strong>，则只需使用 <code>/mvp modify destination e:@here</code> 即可。这会将所选 <em>来源</em> 传送门 (<code>PortalA</code>) 的目的地设置为您在 <em>加号</em> 基本方向 (<code>p:portal:se</code>) 中站立的传送门。这使得无需任何查找即可轻松设置传送门方向！</p>
<a id="Permissions"></a><h3 id="permissions_6">权限</h3>
<p><code>multiverse.teleport.self.p</code>
<code>multiverse.teleport.other.p</code></p>
<p>如果启用更精细的权限：<code>multiverse.teleport.self.p.&lt;portalname&gt;</code></p>

