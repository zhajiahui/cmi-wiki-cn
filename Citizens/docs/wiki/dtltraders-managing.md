---
title: DtlTraders / 管理
source_url: https://wiki.citizensnpcs.co/DtlTraders/managing
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=3148
---


<a id="top"></a>

# DtlTraders / 管理

<a id="Introduction"></a><h2 id="introduction">介绍</h2>
<p>管理商人本质上就是改变其变量。 npc交易员的几个方面都可以通过这种方式来控制。每种商人类型的管理都不同，因为每种商人都有自己的功能，而且工作方式也不同。</p>
<p>到目前为止，仅执行了基本命令，但未来的更新中将包含更多命令。目前仅使用命令还无法完全管理商人。</p>
<a id="Server_trader"></a><h2 id="server-trader">服务器商人</h2>
<a id="Features"></a><h4 id="features">特点</h4>
<ol>
<li>买入和卖出选项卡（每个选项卡最多 51 个）</li>
<li>全球限制</li>
<li>玩家限制（目前不起作用，将在未来的更新中修复）</li>
<li>可以为每个项目或每个项目堆栈设置价格</li>
<li>物品可以以多种可定制的堆叠尺寸出售</li>
<li>六种不同的钱包类型</li>
</ol>
<a id="Stock_managing"></a><h4 id="stock-managing">背包管理</h4>
<p><strong>添加项目</strong></p>
<p>要将商品添加到 <em>服务器商人</em> 库存中，只需从库存中拖放该商品即可。就是这样。<br/>
每次更改后都会保存购买/销售选项卡布局，因此项目将始终出现在它们添加到的插槽中。这使您可以按照您想要的任何方式安排所提供的商品。</p>
<p><strong>编辑项目</strong></p>
<p>如果您想重新定位商人库存中已有的商品，只需将其拖到新位置即可。项目信息被保留，唯一会改变的是它的位置。  </p>
<p><strong>删除项目</strong></p>
<p>要删除某个物品，使其无法再出售/购买，只需将其拖放到您的库存中即可。  </p>
<p><strong>在卖出和买入选项卡之间切换</strong><br/>
在商人库存的右下角有几个不同颜色的羊毛块（可以在配置文件中更改为您想要的任何内容）。最右边的按钮在出售和购买物品之间切换。当您成功切换选项卡时，将会出现一条消息。</p>
<a id="Price_managing"></a><h4 id="price-managing">价格管理</h4>
<p><strong>启用价格管理</strong><br/>
添加的项目没有分配价格。为了能够设置它，您必须点击黑色羊毛（如果更改为其他东西，则为中间的羊毛）。要退出价格编辑模式，只需再次点击即可。</p>
<p><strong>检查当前价格</strong><br/>
要查看商品的当前价格，只需使用 <strong>空的</strong> 光标点击它即可。</p>
<p><strong>改变价格</strong><br/>
价格值的变化取决于：</p>
<ol>
<li><strong>互动类型</strong></li>
<li>右键点击降低价格</li>
<li>左键点击增加价格</li>
<li><strong>使用的物品</strong></li>
<li>木材计为 * 0.01</li>
<li>log 计数为 * 0.1</li>
<li>泥土计为 * 10</li>
<li>鹅卵石算作 * 100</li>
<li>上面未列出的项目算作 * 1</li>
</ol>
<p>Examples:</p>
<div class="highlight"><pre>   A single click with a block of drit increases the price by 10
   Ten clicks with a block of soul sand increase the price by 10
   One right click with 10 blocks of dirt deacreases the price by 100 
</pre></div>
<p><strong>价格模式（将在2.0版本中添加）</strong></p>
<p>价格模式允许您创建多个定价配置文件并在它们之间快速切换。此外，如果定价模式处于活动状态，则添加配置文件中包含的任何项目都会自动设置其价格。您仍然可以手动更改价格。</p>
<a id="Stack_price"></a><h4 id="stack-price">堆栈价格</h4>
<p>要在一次销售多个商品时轻松设置所需的价格，您可以打开堆叠价格设置。通常，您只需设置单个商品的价格，它就会乘以堆栈中的商品数量。上述选项使您可以直接控制最终价格，因此当您想要将价格设置为特定数字时，无需使用分数。</p>
<p>要将价格应用于整个堆栈而不是单个项目，只需 <strong>右键点击</strong> 项目。</p>
<p><strong><em>警告</em></strong>：叠加价格和金额选择菜单不能同时使用。这将在不久的将来得到改变。</p>
<a id="Global_limits"></a><h4 id="global-limits">全球限制</h4>
<p>限制用于控制在给定时间范围内可以购买的商品数量。购买物品会减少限制计数器，当其达到零时，将不再提供该物品。当设定的时间过去后，限制计数器将重置回其原始值，并且可以再次购买该物品。</p>
<p>要限制提供的物品数量，请点击蓝色羊毛</p>
<ol>
<li>右键点击降低限制</li>
<li>左键点击提高限制</li>
<li>Shift 右键点击可减少重置限制所需的时间</li>
<li>左移点击会增加重置限制所需的时间</li>
</ol>
<a id="Player_Limits"></a><h4 id="player-limits">玩家限制</h4>
<p>玩家限制的作用与上述相同。唯一的区别是该限制是针对每个玩家单独应用的，而不是全局效果。</p>
<p>目前尚未实施玩家限制。</p>
<a id="Navigation"></a><h2 id="navigation">导航</h2>
<table>
<thead>
<tr>
<th><strong>DtlTraders</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>用途</td>
<td><a href="http://wiki.citizensnpcs.com/DtlTraders/managing">管理</a></td>
</tr>
<tr>
<td>配置</td>
<td><a href="http://wiki.citizensnpcs.com/DtlTraders/config">配置</a></td>
</tr>
<tr>
<td>NPC 类型</td>
<td><a href="http://wiki.citizensnpcs.com/DtlTraders/traders">贸易商</a></td>
</tr>
</tbody>
</table>

