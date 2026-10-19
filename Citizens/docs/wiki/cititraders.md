---
title: CitiTraders
source_url: https://wiki.citizensnpcs.co/CitiTraders
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4007
---


<a id="top"></a>

# CitiTraders

<p>[[文件：{{{图片}}}]]  </p>
<p><strong>CitiTraders</strong></p>
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
<td>特赫比尔德</td>
</tr>
<tr>
<td><strong>版本</strong></td>
<td>RC-5</td>
</tr>
<tr>
<td><strong>Citizens 构建</strong></td>
<td>2.0</td>
</tr>
<tr>
<td><strong>其他依赖项</strong></td>
<td>Citizens 2、Vault，权限系统和经济系统。</td>
</tr>
<tr>
<td><strong>下载</strong></td>
<td><a href="http://thedemgel.com:8080/jenkins/job/CitiTraders/Recommended/artifact/target/CitiTrader-RC-5.jar">链接</a></td>
</tr>
<tr>
<td><strong>Description:</strong> Cititrader 是支持基于界面的交易的 NPCs。  <strong>问题</strong>: <a href="http://thedemgel.com:8080/jira/browse/CITITRADER">JIRA 问题</a></td>
<td></td>
</tr>
</tbody>
</table>
<p>1-21-2013 Cititraders 目前已过时，请参阅 <a href="dtltraders.md" title="DtlTraders">DtlTraders</a></p>
<a id="RELEASE_CANDIDATE"></a><h1 id="release-candidate">释放候选者</h1>
<p>CitiTraders 处于 RC 状态，这意味着虽然我觉得它接近发布，但它并不完美，如果您发现任何问题，请使用问题页面让我知道，但除此之外我觉得它几乎没有错误。
您可以从这里下载开发版本：<a href="http://thedemgel.com:8080/jenkins/job/CitiTraders/lastSuccessfulBuild/artifact/target/CitiTrader-RC-5.jar">Jenkins 开发构建</a></p>
<a id="CitiTraders"></a><h1 id="cititraders">CitiTraders</h1>
<p>CitiTraders 是一组 Citizens 2.0 特征，赋予 NPCs 能力 to:</p>
<ul>
<li>以预设价格购买和出售物品。</li>
<li>保持库存。</li>
<li>与经济插件配合使用银行帐户、所有者帐户或每个 npc 帐户。</li>
</ul>
<p>您可以在 <a href="irc://cititrader@irc.esper.net">#cititrader</a> 频道中访问我的 irc.esper.net 来提问，或提出建议，或只是交谈</p>
<p>加载视频</p>
<p>YouTube</p>
<p>YouTube 可能会收集个人数据。 <a href="https://www.youtube.com/howyoutubeworks/user-settings/privacy/">隐私政策</a></p>
<p>继续
解雇</p>
<a id="Installation"></a><h2 id="installation">安装</h2>
<ul>
<li>确保您安装了 Citizens 2、Vault 和经济插件。</li>
<li>从页面顶部的链接下载 .jar 并将其放置在 /plugins 文件夹中。</li>
<li>CitiTraders 本身不需要配置。但是，它要求您有 Vault，这是一个可以通过 Vault 访问的经济插件，并且</li>
</ul>
<a id="Commands"></a><h2 id="commands">命令</h2>
<p>有关命令的完整列表，请访问 Bukkit 页面，直到我可以更新此 Wiki</p>
<p>[<a href="http://dev.bukkit.org/server-mods/cititraders/">武吉特页面</a>]</p>
<a id="Permissions"></a><h2 id="permissions">权限</h2>
<p><a href="cititrader-permissions.md" title="Cititrader/Permissions">权限</a></p>
<a id="Creating_a_new_npc_as_a_trader"></a><h2 id="creating-a-new-npc-as-a-trader">创建一个新的NPC作为商人</h2>
<p>:   <strong>/trader create [NAME] -type [TYPE]</strong></p>
<p>[NAME] - 要创建的 NPC 的名称
[TYPE] - 要创建的 NPC 的类型（如果省略，则默认为 PLAYER）</p>
<a id="Adding_trader_to_an_existing_NPC"></a><h2 id="adding-trader-to-an-existing-npc">将商人添加到现有 NPC</h2>
<p>将商人功能添加到现有 NPCs use:</p>
<p>:   <strong><code>/trait wallet</code></strong></p>
<p>和</p>
<p>:   <strong><code>/trait stockroom</code></strong></p>
<a id="Buying_and_Selling"></a><h2 id="buying-and-selling">买卖</h2>
<p>（如果您在任何时候遇到困难并且商人没有响应，请关闭所有窗口并输入 /trader cancel）</p>
<a id="Accessing_the_storeroom_of_a_trader"></a><h3 id="accessing-the-storeroom-of-a-trader">进入商人的库房</h3>
<ol>
<li>得到一本书</li>
<li>拿着书</li>
<li>拿着书的同时右键点击您的商人</li>
<li>将物品放入商人库存中</li>
</ol>
<a id="Setting_Buy/Sell_prices"></a><h3 id="setting-buysell-prices">设置买入/卖出价格</h3>
<p>:   <strong><code>/trader sellprice &lt;amount&gt;</code></strong></p>
<p>和</p>
<p>:   <strong><code>/trader buyprice &lt;amount&gt;</code></strong></p>
<p>在执行上述任一命令后，右键点击手中有商品的商人，这将通过 <strong>这个</strong> 商人设置该商品的价格。价格不是全球性的。</p>
<a id="Buy_from_a_Trader"></a><h3 id="buy-from-a-trader">从贸易商处购买</h3>
<p>要从贸易商处购买商品，您需要 <strong>右键点击</strong> 为贸易商。这将打开一个交易（库存）窗口，其中列出了商人手头拥有的所有不同类型的物品。
这时你需要选择你想要购买的物品，在你想要购买的物品上选择<strong>左键点击</strong>，这将带你到购买窗口，这里会提供成堆的物品，但仅限于NPC有出售的物品。此时您可以通过<strong>右键点击</strong>查看该堆栈的价格，并通过<strong>左键点击</strong>购买该堆栈。</p>
<p>您可以随时点击 <strong>箭头</strong> 返回项目选择屏幕。</p>
<a id="Selling_to_a_Trader"></a><h3 id="selling-to-a-trader">卖给商人</h3>
<p>要首先向商人出售 <strong>左键点击</strong> 商人，将打开一个库存窗口，将您想要出售给商人的任何物品拖到他的窗口中。关上窗户。价格将被计算并存入您的帐户，任何他没有拿走的物品将在结束时掉落到该组中。
（这将被改变，商人获得的物品将被列出，并在掉落时消耗）</p>
<a id="Wallets"></a><h2 id="wallets">钱包</h2>
<p>设置钱包 you:</p>
<p>:   <strong><code>/trader setwallet &lt;admin|private|bank &lt;player&gt;|owner|town_bank&gt;</code></strong></p>
<a id="Admin"></a><h3 id="admin">管理员</h3>
<p>将钱包设置为管理员将创建一个 <strong>ADMIN</strong> 商店，出售的物品不会从商店中删除，资金将从玩家银行中删除，但不会存入任何地方。</p>
<p>:   <strong><code>/trader setwallet admin</code></strong></p>
<a id="Private"></a><h3 id="private">私人</h3>
<p>NPC将保存他赚的任何钱，你可以稍后提取钱。</p>
<p>:   <strong><code>/trader setwallet private</code></strong></p>
<a id="Bank"></a><h3 id="bank">银行</h3>
<p>NPC 将使用银行帐户，该银行必须由拥有 NPC 的玩家拥有。</p>
<p>:   <strong><code>/trader setwallet bank &lt;accountname&gt;</code></strong></p>
<a id="Owner"></a><h3 id="owner">业主</h3>
<p>NPC 将使用 NPC 所有者的经济账户</p>
<p>:   <strong><code>/trader setwallet owner</code></strong></p>
<a id="Town_Bank"></a><h3 id="town-bank">城镇银行</h3>
<p>NPC 将使用以下银行帐户城镇（使用 Towny 插件）。尝试分配此值的 NPC 的所有者必须是该镇的市长或助理。</p>
<p>:   <strong><code>/trader setwallet town_bank</code></strong></p>
<a id="TODO"></a><h1 id="todo">待办事项</h1>
<ul>
<li>更新此维基</li>
</ul>
<a id="Discounts"></a><h3 id="discounts">折扣</h3>
<p>将会有基于团体/玩家的折扣，它们将基于百分比。</p>
<a id="Sales_Display"></a><h3 id="sales-display">销售展示</h3>
<p>将改变销售的显示和处理方式，NPCs将在库存窗口中列出他们正在购买的物品，玩家将物品扔到库存中，该物品将立即出售。 （这个改变将触发发布阶段）</p>
<a id="Manager/Assistants"></a><h3 id="managerassistants">经理/助理</h3>
<p>添加经理和助理到商店，经理和助理将能够进货商店，并设定价格。管理人员将有权使用私人银行，稍后将考虑添加更多银行。他们会无法链接商人、链接宝箱或删除/解雇 NPCs，这些对商人的所有者仍然可用。这将允许服务器管理员设置商人，并将经理权限分配给玩家来经营商店。</p>
<a id="Rewrite_Sell_To_Player"></a><h3 id="rewrite-sell-to-player">重写卖给玩家</h3>
<p>更高效，并允许 buystack</p>

