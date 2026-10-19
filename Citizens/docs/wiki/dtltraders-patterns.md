---
title: DtlTraders / 模式
source_url: https://wiki.citizensnpcs.co/DtlTraders/patterns
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4604
---


<a id="top"></a>

# DtlTraders / 模式

<a id="NOTICE"></a><h2 id="notice"><strong>通知</strong></h2>
<p>模式还没有被应用到 VR 中。 3.0还没到！</p>
<a id="Overview"></a><h2 id="overview">概述</h2>
<p>每个模式都保存在位于插件主文件夹中的 <em>patterns.yml</em> 文件中。 （插件/DtlCitizensTrader）<br/>
 您可以更改配置文件中的目录。</p>
<p>patterns: 有 2 种类型</p>
<ul>
<li>
<p><em>定价模式</em><br/>
设置商品价格和定价等级。</p>
</li>
<li>
<p><em>物品图案</em><br/>
会将某些物品添加到商人的库存中，也有物品等级。</p>
</li>
</ul>
<p>即将到来的第三种模式类型为 2.6（还有很长的路要走）：</p>
<ul>
<li><em>随机模式</em>
这些将允许设置商人可以在库存中显示的最大物品（例如 20 件中的 10 件），还可以设置超时、“生成机会”、超时后将在每个物品上使用的金额和价格机会。</li>
</ul>
<p>所有模式都基于用于构建项目脚本的一种语法。这些脚本由每种模式类型使用，只是每种模式类型以不同的方式使用它。</p>
<a id="Item_syntax"></a><h2 id="item-syntax">项目语法</h2>
<p>我知道这听起来很可怕，但最好用两个词来解释它：D</p>
<p>模式中的每个项目都是由您可能使用的一些关键字和标志构建的，这里允许使用基本商人设置无法实现的许多选项，但您需要小心。</p>
<a id="Keywords"></a><h3 id="keywords">关键词</h3>
<p><strong>项目设定</strong></p>
<p><strong>关键词</strong></p>
<p><strong>价格格局</strong></p>
<p><strong>物品图案</strong></p>
<p><strong>示例</strong></p>
<p><code>ID and data</code></p>
<p><code>id[:data]</code></p>
<p><code>Looks for items with the given id and/or data, priority: 130</code></p>
<p><code>Sets the item id, and when set also the data default: required!</code></p>
<p><code>wool:14</code></p>
<p><code>Name</code></p>
<p><code>n</code></p>
<p><code>matches the item by the given name, priority: 300</code></p>
<p><code>Sets the item name, default: nothing</code></p>
<p><code>n:A Item</code></p>
<p><code>Item amount</code></p>
<p><code>a</code></p>
<p><code>Looks for items with the given amount, priority: 5</code></p>
<p><code>Sets one or more amounts for an item, default: 1</code></p>
<p><code>a:1,2,4</code></p>
<p><code>Durability</code></p>
<p><code>d</code></p>
<p><code>Looks for items with the given or higher durability, priority: 45</code></p>
<p><code>Sets the items durability, default: 0</code></p>
<p><code>d:22</code></p>
<p><code>Tier</code></p>
<p><code>t</code></p>
<p><code>Matches items only in the given item tier, priority: 25</code></p>
<p><code>not used</code></p>
<p><code>t:vip_tier</code></p>
<p><code>Color</code></p>
<p><code>c</code></p>
<p><code>matches by the given color, priority: 5, leather armor only</code></p>
<p><code>Sets the color for a leather armor item. Uses RGB values separated by ^, leather armor only</code></p>
<p><code>c:255^210^24</code></p>
<p><code>Enchants</code></p>
<p><code>e</code></p>
<p><code>Checks if the item has the same enchants, priority: 5</code></p>
<p><code>Sets enchantments for an item, default: none</code></p>
<p><code>e:smite/3</code></p>
<p><code>Stored enchants</code></p>
<p><code>se</code></p>
<p><code>Checks if the item has the same stored enchants, priority: 5</code></p>
<p><code>Sets enchantments for a enchanted book item, default: none, enchanted book only</code></p>
<p><code>se:smite/7</code></p>
<p><code>Price</code></p>
<p><code>p</code></p>
<p><code>Sets the price for each matching item, overriding lower priority matches</code></p>
<p><code>Sets the price for the given item, default: pattern price</code></p>
<p><code>p:12.22</code></p>
<p><code>Multiplier</code></p>
<p><code>m</code></p>
<p><code>Sets the multiplier for each matching item, overriding lower priority matches</code></p>
<p><code>Sets the multiplier for the given item, default: pattern multiplier</code></p>
<p><code>m:0.9</code></p>
<p><code>Firework</code></p>
<p><code>f</code></p>
<p><code>not used</code></p>
<p><code>Sets firework data for a firework item, firework only</code></p>
<p><code>---</code></p>
<p><code>Global limit</code></p>
<p><code>gl</code></p>
<p><code>not used</code></p>
<p><code>Sets a limit for this item, default: none</code></p>
<p><code>gl:limit/timeout</code></p>
<p><code>Player limit</code></p>
<p><code>pl</code></p>
<p><code>not used</code></p>
<p><code>Sets a limit for each player for this item, default: none</code></p>
<p><code>pl:limit/timeout</code></p>
<p><code>Slot</code></p>
<p><code>s</code></p>
<p><code>Not used</code></p>
<p><code>Sets the slot for the item, default: first empty</code></p>
<p><code>s:22</code></p>
<hr/>
<a id="Flags"></a><h3 id="flags">旗帜</h3>
<p><strong>物品标志</strong></p>
<p><strong>旗帜</strong></p>
<p><strong>物品图案</strong></p>
<p><code>Item Lore</code></p>
<p><code>lore</code></p>
<p><code>This flag allows you to add lores to your item. It needs always to be set on the end of a item definition and needs to end with :. If used always supply a lore. How it should look like will be shown later.</code></p>
<p><code>Stack price</code></p>
<p><code>sp</code></p>
<p><code>The price calculated for this item, is always applied to the whole stack, not to each item. example:  price = 3$ | amount = 2 | without sp: 2*3$ = 6$ | with sp: 3$, so 1.5$ for each</code></p>
<p><code>Pattern multiplier</code></p>
<p><code>pm or !pm</code></p>
<p><code>Forces to use or to ignore pattern multiplier matches</code></p>
<hr/>
<a id="Basic_syntax"></a><h3 id="basic-syntax">基本语法</h3>
<hr/>
<a id="All_patterns"></a><h4 id="all-patterns">所有图案</h4>
<p>每个模式都以一个名称开头，您将在游戏中使用该名称将它们分配给您的商人。该名称可以任意长，只是您只能使用字母、数字并使用此字符 <code>**_**</code> 而不是空格。</p>
<p>此外，现在的每个模式都需要指定一个类型，以便模式加载器知道如何读取它。
目前只有2种型号，<strong>价格</strong>和<strong>项目</strong>。我认为这是显而易见的。</p>
<p>除了类型节点之外，所有模式都有 3 个附加 nodes:“全部”、“卖出”、“买入”。这些节点将条目应用于出售和购买股票，或仅应用于其中之一。</p>
<p>空图案例如：</p>
<pre> pattern_name:
   type: pattern_type
   all:
   - ...
   sell:
   - ...
   buy:
   - ...
</pre>
<hr/>
<p>模式中的每个条目都具有相同的语法，如下所示，并且应该始终像 this: 那样完成</p>
<p><code>id[:data] [keywords...] [flags...] [n:...] [lore:]</code></p>
<p>如示例所示，最好的方法是在 ID 之后设置所有关键字，然后设置标志。</p>
<p>该规则有两个例外。</p>
<p><strong>姓名</strong> 关键字最好在最后使用，因为您无需担心它将任何其他关键字或标志解释为项目名称部分。但如果你愿意，你不需要将其设置在最后，只需在项目名称后面设置 <strong>记住总是添加两个空格</strong> 即可。 <em>（该示例表明，随着 <strong>传说</strong> 旗）</em></p>
<p><strong>传说</strong> 标志需要始终位于末尾，这是 <strong>YAML</strong> 语法要求，这将使我们能够轻松地向项目添加知识。</p>
<p>将项目添加到模式中非常简单，只需键入它们的名称或 ID 以及数据（如果需要），所有其他值都有其默认值或行为，因此您不必担心可能会忘记为项目设置某些内容，从而破坏模式。</p>
<p><strong>Examples:</strong></p>
<p><code>wool:14</code> - 将向贸易商库存添加红色羊毛块。</p>
<p><code>wool s:3 n:My white wool</code> - 将向贸易商库存添加羊毛块，位于插槽 3，名为 <strong>我的白羊毛</strong>。</p>
<p><code>276 d:80% e:smite/2 p:1000</code> - 将为贸易商库存添加一把钻石剑，打击等级为2，价格为1000，耐用性为80%。</p>
<a id="Price_patterns"></a><h4 id="price-patterns">价格模式</h4>
<p>一般来说，价格模式允许您为商人的库存商品设置价格和乘数。价格模式中的每个项目条目都被视为匹配模式，这将用于匹配商人库存中的项目并设置其价格和乘数。</p>
<p>每场比赛可能有不同的优先级，rule: 较高的优先级获胜。</p>
<p>最简单且最常用的是将这些模式作为全球价格文件。因此，您可以为游戏中的每个项目设置所有价格，然后将此模式添加到每个商人中。现在您唯一需要做的就是将商品添加到他的库存中，仅此而已。不再设置价格：P 价格将为每个玩家自动设置。</p>
<p>由于还可以在这些模式中创建 <strong>等级</strong>，因此您可以创建价格较低的 VIP 组（只需设置层级的乘数即可轻松完成）。要应用某个级别的价格，玩家需要拥有该级别 <strong>“使用”</strong> 的权限。</p>
<p>假设我们对游戏中的所有物品采用价格模式（从现在开始将其命名为 "global-prices"），并且我们希望将除日志之外的所有物品的乘数设置为 <strong>0.9</strong>：</p>
<pre> - ...
 // because we just set the multiplier, it will be set for all items in this pattern, priority match is equal to 0
 - m:0.9
 // here we add additional information to match items with id 17 (logs), and because this match is higher (equals 130), it will override the 0.9 global multiplier for logs
 - 17 m:1.0
</pre>
<p>另一种价格模式例如：</p>
<pre> price_pattern:
   type: price
   all:
   - m:1.0
   - dirt p:0.55
   - wool p:4.42 
   sell:
   - m:1.0
   - log p:3.33
   - wool m:1.1
   buy:
   - wool m:0.9
</pre>
<p>此模式将设置泥土和羊毛块的买卖价格，并且仅设置原木的出售价格。我们还告诉该模式对所有物品使用 <strong>1.0</strong> 的乘数，但羊毛除外，在（向玩家）出售 <strong>1.1</strong> 时获得乘数，而出售给商人的基本价格类似于 <strong>0.9</strong>。</p>
<p>只有这样你才能比旧系统有更多的可能性:P</p>
<a id="Tiers"></a><h5 id="tiers">层级</h5>
<a id="Tier_tags_(whats_the_difference?)"></a><h5 id="tier-tags-whats-the-difference">等级标签（有什么区别？）</h5>
<a id="Advanced_matching"></a><h5 id="advanced-matching">高级匹配</h5>
<a id="Matching_informations"></a><h5 id="matching-informations">匹配信息</h5>
<p>可以匹配哪些标签和项目信息可以在开头的表格中找到，还提供了信息，当使用特定关键字时优先级如何增长。</p>
<p>因为这不是发布版本，所以匹配系统将会有很多变化。随时欢迎任何想法：）</p>
<a id="Item_patterns"></a><h4 id="item-patterns">物品图案</h4>
<p>Soon.</p>
<a id="Lores"></a><h5 id="lores">洛雷斯</h5>
<p>很快：）</p>
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
<td>配置</td>
<td><a href="http://wiki.citizensnpcs.com/DtlTraders/Commands">命令</a></td>
</tr>
<tr>
<td>用途</td>
<td><a href="http://wiki.citizensnpcs.com/DtlTraders/patterns">图案</a></td>
</tr>
<tr>
<td>NPC 类型</td>
<td></td>
</tr>
</tbody>
</table>

