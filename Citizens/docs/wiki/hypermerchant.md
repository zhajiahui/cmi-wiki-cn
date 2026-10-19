---
title: HyperMerchant
source_url: https://wiki.citizensnpcs.co/HyperMerchant
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5037
---


<a id="top"></a>

# HyperMerchant

<a id="HyperMerchant"></a><h2 id="hypermerchant">HyperMerchant</h2>
<p><a href="http://dev.bukkit.org/bukkit-plugins/hypermerchant/">HyperMerchant</a> 是一个用于 HyperConomy 商店的商人 npc。</p>
<p>特点 include:</p>
<ul>
<li>
<p>一个易于使用的基于库存的 GUI，供您的玩家从 HyperConomy 商店购买和销售。</p>
</li>
<li>
<p>应该与 HyperConomy 商店权限配合得很好。</p>
</li>
<li>
<p>可切换商家下班模式。通过简单的命令暂时关闭任何商店。</p>
</li>
<li>
<p>用于更改 NPC 问候、告别、下班和拒绝服务/无权限消息的简单命令。</p>
</li>
</ul>
<p>此页面上的许多信息可能不是最新的。请访问 HyperMerchant bukkitdev 页面以获取最新信息。</p>
<a id="Where_to_get_latest_version"></a><h4 id="where-to-get-latest-version">哪里可以获得最新版本</h4>
<p>HyperMerchant 1.57-dev 是 <a href="http://dev.bukkit.org/bukkit-plugins/hypermerchant/">布基特德夫</a> 的最新版本。兼容Bukkit/Spigot 1.8。</p>
<p><a href="http://ci.citizensnpcs.co/job/HyperMerchant/">最新的开发版本</a> 在 CI 服务器上可用。</p>
<p>Bukkit的其他版本还有<a href="http://dev.bukkit.org/bukkit-plugins/hypermerchant/pages/compatibility/">兼容性指南</a>。</p>
<a id="How_to_install"></a><h4 id="how-to-install">如何安装</h4>
<p>确保您安装了 HyperConomy 的兼容版本。</p>
<p>将 HyperMerchant.jar 保存到您的插件文件夹中</p>
<a id="How_to_use"></a><h4 id="how-to-use">如何使用</h4>
<ol>
<li>已经设立了 HyperConomy 商店。</li>
<li>创建一个 npc: /create npc my_shopkeeper</li>
<li>将 npc 指定为 hypermerchant trait: /trait hypermerchant</li>
<li>将npc分配给shop: /hmerchant setshop shop-name</li>
</ol>
<p>就是这样。您现在可以通过与 my_shopkeeper 交互来打开该商店的菜单。</p>
<p>或者，您可以使用 /shopmenu 或 /remotemenu 命令打开商店的菜单</p>
<p><a href="http://dev.bukkit.org/bukkit-plugins/hypermerchant/">布基特德夫</a> 有一个简短的视频演示了大部分插件功能。</p>
<a id="Other_npc_commands"></a><h4 id="other-npc-commands">其他npc命令</h4>
<ul>
<li>/<strong>商人</strong> <em>offduty</em> - 切换 npc 下班模式。</li>
<li>/<strong>商人</strong> <em>问候语</em> 您好，欢迎来到我的店铺。 --- 指定 npc 在点击时会说的话。</li>
<li>/<strong>商人</strong> <em>告别</em> 谢谢你的钱，伙计！ --- 指定商店菜单关闭时NPC会说什么。</li>
<li>/<strong>商人</strong> <em>关闭</em> 抱歉，我正在午休。 --- 指定NPC在设置为下班模式时会说的话。</li>
<li>/<strong>商人</strong> <em>否认</em> 您不可以在此购物。 --- 指定如果玩家没有适当的权限，NPC 会说什么。</li>
<li>/<strong>商人</strong> <em>套装店</em> shop_name_here --- 指定点击 npc 时显示的商店库存。 npc 不必在商店内部，甚至不必与商店在同一个世界。</li>
</ul>
<p>上述命令均对当前选定的 npc 进行操作，除非 --id 标志为 specified:</p>
<ul>
<li>/<strong>商人</strong> <em>问候语</em> 您好，欢迎来到我的店铺。 <em>--id</em> 71</li>
</ul>
<p>或</p>
<ul>
<li>/<strong>商人</strong> <em>--id</em> 71 <em>问候语</em> 您好，欢迎来到我的店铺。</li>
</ul>
<a id="HyperMerchant_also_includes_the_following_conveniance_commands:"></a><h4 id="hypermerchant-also-includes-the-following-conveniance-commands">HyperMerchant 还包括以下便利 commands:</h4>
<ul>
<li>/<strong>远程菜单</strong> <em>[店名]</em> - 从任何地方打开商店的菜单。</li>
<li>/<strong>shopmenu</strong> - 打开您所在商店的菜单。</li>
<li>/<strong>rslist</strong> - 列出可以使用 /remotemenu 命令访问的所有商店的名称。</li>
<li>/<strong>onduty</strong> - 切换玩家商店老板是否营业。</li>
</ul>
<a id="Other_features:"></a><h4 id="other-features">其他 features:</h4>
<p>拥有商店的玩家可以被希望与他们做生意的玩家点击。
店主可以使用 /onduty 命令禁用此功能，并且可以在 config.yml 文件中禁用它。
您可以限制店主仅在其店内开展业务。</p>
<p>permissions:</p>
<div class="highlight"><pre>  hypermerchant.*:
     description: Gives access to all HyperMerchant commands
     children:
        hypermerchant.menu: true
        hypermerchant.remote: true
        hypermerchant.npc: true
        hypermerchant.manage: true
  hypermerchant.menu:
     description: Allow use of the /shopmenu command.
     default: true
  hypermerchant.npc:
     description: Allow interaction with hypermerchant npc.
     default: true
  hypermerchant.remote:
     description: Allow use of the /remotemenu command.
     default: op
  hypermerchant.manage:
     description: Allow use of the /hmerchant command.
     default: op
</pre></div>

