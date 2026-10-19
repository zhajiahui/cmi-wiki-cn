---
title: DtlTraders / 基础用法
source_url: https://wiki.citizensnpcs.co/DtlTraders/basics
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4956
---


<a id="top"></a>

# DtlTraders / 基础用法

<p>本教程将向您展示如何创建一个类似<strong>管理店</strong>的交易员、如何更改他的股票以及管理交易员时应该注意的事项。我将向您展示与 <strong>经理模式</strong> 及其 <strong>子模式</strong> 有关的一些异常和行为。我还将向您展示如何更改配置以帮助您设置价格。</p>
<a id="Creating_a_trader"></a><h2 id="creating-a-trader">创建商人</h2>
<p>您可以通过两种不同的方式创建商人，第一种是使用 <strong>/trader create &lt;name&gt;</strong> 命令，或公民 <strong>/trait trader</strong> 的特征分配命令。</p>
<p>什么时候应该使用这些命令？
一般来说，<strong>创造</strong> 命令会创建一个具有给定名称的新 NPC，准备好在下次点击时进行编辑，而 <strong>特征</strong> 命令应该在现有的 NPCs 上使用，因此，如果您有一个 NPC 走很长的路径，则无需从头开始设置他的路径。</p>
<p>让我们创建一个新的商人，这样我们就可以管理他而不必担心任何错误。</p>
<p>让我们创建一个名为 <strong>主厨奥托</strong> 的商人，我们还将创建 <strong>奥托</strong>，使其标题为金色。</p>
<p><code>/trader create &amp;6Chef &amp;rOtto</code></p>
<p>如您所见，我们使用 <strong>&amp;</strong> 字符来告诉下一个数字或字符是颜色代码，其中 <strong>&amp;6</strong> 表示 <strong><em>黄金</em></strong>，<strong>&amp;r</strong> 用于 <strong>重置任何格式</strong>，因此只有 <em>标题</em> 有颜色。所有颜色代码均列于[|此处]。</p>
<p>在这个命令之后，我们的npc站在我们面前，我们得到了三个messages:</p>
<p><code>You created a new trader: Chef Otto  
Manager mode enabled for: Chef Otto  
Sell Stock managing toggled</code></p>
<p>每次您使用此命令 <strong>创建一个新的商人</strong> 时，它都会为您和 <strong>解锁卖出股票</strong> 提供 <strong>自动切换至管理员模式</strong>。解锁库存可以更改内容。</p>
<p>现在我们只需要在商人上输入 <strong>右键点击</strong> 即可进入本教程的下一部分:)</p>
<a id="First_opening_and_manager_mode_introduction"></a><h3 id="first-opening-and-manager-mode-introduction">首次开启及经理模式介绍</h3>
<p>创建商人后，第一次打开商人，看起来就像一个空箱子，底部只有一根 <strong>黄色</strong> 羊毛。现在我们只需将要出售给玩家的每件物品拖到库存中即可。您可以选择任何您想要的项目，该插件支持具有所有自定义属性的所有项目。</p>
<p>：---
：例如，让我们将 <strong>饼干</strong> 和 <strong>面包</strong> 放入库存中。
：---</p>
<p>添加所有要出售的物品后，只需点击黄色羊毛即可。它将<strong>锁</strong>库存，保存所有项目并更新旧项目，并切换到综合管理部分。</p>
<p>现在底部有 4 种不同的羊毛，选项为 <em>（从左到右）</em>：</p>
<ol>
<li><strong>库存解锁</strong> - 允许更改内容及其布局</li>
<li><strong>限额管理</strong> - 仍未添加</li>
<li><strong>价格管理</strong> - 允许为库存商品设置价格</li>
<li><strong>股票转换</strong> - 显示当前库存，点击切换到其他库存后，此按钮始终可见（解锁库存除外）</li>
</ol>
<a id="Add,_edit_and_remove_items"></a><h3 id="add-edit-and-remove-items">添加、编辑和删除项目</h3>
<p>请注意，每个项目的插槽位置都没有改变，因此您放置项目的位置它将保留在那里。
当您想要更改库存中的商品时，您始终需要在库存解锁时进行。</p>
<p>您可以添加和删除物品，只需将它们拖入或拖出商人库存即可，您在这里可以做的唯一额外的事情是将物品移动到不同的插槽。</p>
<p><strong>重要！</strong> 请勿更改您要在此 <strong>部分</strong> 中出售的金额，否则该商品的所有设置和价格都将丢失。稍后将讨论如何做到这一点。</p>
<p>：---
：所以我们的库存中有 <strong>饼干</strong> 和 <strong>面包</strong>
：假设我们忘记了我们还想向玩家出售一些 <strong>炖菜</strong>。所以我们需要解锁库存，添加商品并锁定库存。
：---</p>
<a id="Setting_prices"></a><h3 id="setting-prices">设定价格</h3>
<p>管理价格也只需点击项目即可完成，但您也可以使用命令来完成此操作。但现在我将解释如何使用 GUI 来执行此操作。</p>
<p>当物品没有任何价格时，它会显示价格设置为 <strong>无</strong>，显示此类物品，但玩家无法向商人购买或出售这些物品，就像库存中不存在一样。如果您忘记设置价格，这可以防止意外地向玩家免费提供物品。您还可以使用此功能制作一个小型信息台，只需向商人添加带有准备好的描述的项目即可。点击商人将打开包含这些物品的库存。</p>
<p>用 <strong>空的</strong> 光标点击项目也会显示其当前值。</p>
<p>但如何更改价格呢？很简单，只需从库存中取出任何物品，例如 <strong>镐</strong>，当您将光标放在该物品上，将 <strong>左键点击</strong> 放在库存中的任何物品上时，您会注意到一条聊天消息，告诉您该物品的新价格是多少。</p>
<p>：但是加 1 就很搞笑了！定价10000需要很长时间！</p>
<p>那么我们来介绍一些 rules:</p>
<ol>
<li><strong>左键点击</strong> 一件 <strong>总是</strong> 加价</li>
<li><strong>右键点击</strong> 商品 <strong>总是</strong> 降低价格，价格不会低于 <strong>0.00</strong> 等于 <strong>免费物品</strong>。</li>
<li>除配置中定义的特殊块外，每个项目的值为 1。</li>
<li>具有不同价值的特殊块有一个显示该块价值的描述，例如，点击一块石头会改变价格 <strong>10000</strong></li>
<li>如果您用于更改价格的商品可以叠加，则价格更改的计算方式如下：<strong><em>块值</em></strong> * <strong><em>堆叠数量</em></strong></li>
</ol>
<p>为了向您展示这是如何工作的，这里有一些示例（使用默认配置）：</p>
<ul>
<li><strong>3块羊毛</strong> =&gt; 1 * 3 = 3</li>
<li><strong>1 镐</strong> =&gt; 1 * 1 = 1</li>
<li><strong>10块鹅卵石</strong> =&gt; 10 * 100 = 1000</li>
<li><strong>23块泥土</strong> =&gt; 0.01 * 23 = 0.23</li>
</ul>
<p>默认特价blocks:</p>
<ol>
<li><strong>泥土</strong> = 0.01</li>
<li><strong>木头</strong> = 0.1</li>
<li><strong>日志</strong> = 10</li>
<li><strong>鹅卵石</strong> = 100</li>
<li><strong>石头</strong> = 10000</li>
</ol>
<p>：---
：现在让我们为我们的商品设置价格，<strong>苹果</strong> = 2.12，<strong>面包</strong> = 5.30，<strong>炖菜</strong> = 8.99，然后点击 <strong>回来</strong> 按钮。
：---</p>
<a id="Multiple_amounts"></a><h3 id="multiple-amounts">多个金额</h3>
<p>这个管理部分可以让玩家购买物品变得更容易。考虑这样一种情况，当玩家想要购买 64 条面包时，点击该物品 64 次会让他发疯，我们如何解决这个问题？我们可以将相同的商品添加到库存中并为其设置价格，但这需要使用新的插槽，有时我们想要出售大量商品，这种方法会浪费插槽。</p>
<p>那么我们该怎么办呢？</p>
<p>为了解决此问题，有一项功能允许打开包含所售商品的自定义金额的 <strong>子库存</strong>。要打开 <strong>子库存</strong>，您只需 <strong>左移点击</strong> 您要配置的项目即可。</p>
<p>现在，当我们打开该窗口时，您可以注意到第一个槽位是您添加到库存中的数量，在这里您可以更改项目的基本数量，而不会丢失为该项目设置的任何配置。</p>
<p>在此添加任何其他金额将自动为每个玩家启用 <strong>子库存</strong>。从现在开始，<strong>左键点击</strong> 该物品将始终打开子库存，而 <strong>右键点击</strong> 将使用基本金额进行交易，因此如果玩家只想购买基本金额，则无需打开子库存。</p>
<p><strong>注意！</strong> 例如，如果您将 10 个苹果添加到镐的库存量中，它只会读取数量并将其添加到允许出售 10 个镐的配置中，该插件会将它们添加到 1 堆中，因为任何工具的 <strong>最大堆叠数量</strong> 都等于 <strong>1</strong>，因此需要 10 个免费插槽来购买此物品。来自构建 #411 或 #3（新项目）</p>
<p>：---
：因为我们的玩家喜欢吃苹果，所以让我们添加一些额外的数量 10、16、20、32 和 64，然后点击 <strong>回来</strong> 按钮。
：---</p>
<a id="StackPrice_and_NoStack_flags"></a><h3 id="stackprice-and-nostack-flags">StackPrice 和 NoStack 标志</h3>
<p>除了 <strong>多个金额</strong> 功能之外，还有两个可以在商人库存中的项目上设置或删除的标志。</p>
<p><strong>堆栈价格</strong> 标志改变了商品价格的计算方式，默认情况下，如果将 <strong>1</strong> 的价格设置为 5 个商品的堆栈，则将花费 <strong>5</strong>，但是使用堆栈价格标志，在经理模式下设置的整个价格将设置为堆栈，因此 <strong>5 件商品 1 件</strong>。</p>
<p><strong>无堆栈</strong> 标志当前已禁用</p>

