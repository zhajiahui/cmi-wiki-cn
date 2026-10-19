---
title: DtlTraders / Denizen / 触发器
source_url: https://wiki.citizensnpcs.co/DtlTraders/denizen/triggers
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=3426
---


<a id="top"></a>

# DtlTraders / Denizen / 触发器

<a id="Introduction"></a><h2 id="introduction">介绍</h2>
<a id="Current_triggers"></a><h3 id="current-triggers">当前触发器</h3>
<p>到目前为止，共有 3 个居民触发器（版本 1.9.6），但我们将添加更多触发器并扩展其功能。
当玩家成功交易（出售/购买）物品时，将调用每个触发器。</p>
<p>此外，每个触发器都会自动向每个玩家添加 <em>交易项目</em> 标志以及购买/出售的物品。此行为将在发布版本中改变。</p>
<a id="Incoming_features"></a><h3 id="incoming-features">传入功能</h3>
<p>每个触发器都会查找 <em>预定义标志</em>，您可以使用它来获取交易结果（SUCCESS/NOMONEY/NOSPACE/LIMIT）、交易中使用的项目及其金额。 <em>（欢迎任何建议）</em></p>
<p>也许我还会添加一种管理商人事件的方法，让您取消正在进行的交易、更改价格、更改金额，但这只是一个早期概念，因此将添加 10%。</p>
<p>要让触发器设置标志，您需要将其值设置为 &lt;set&gt;</p>
<p>支持的标志将由触发器本身设置。</p>
<ol>
<li>TransactionItem:&lt;set&gt;</li>
<li>TransactionItemAmount:&lt;set&gt;</li>
<li>TransactionResult:&lt;set&gt;</li>
</ol>
<p>此处列出了将添加的触发器</p>
<ol>
<li>TransactionCanceled（当玩家关闭交易窗口时或执行 <em>TRADER_交易取消</em> 命令时调用）</li>
</ol>
<p>默认情况下每个触发器都是禁用的，因此您需要切换它们才能使用。</p>
<a id="Sample"></a><h3 id="sample">样品</h3>
<p>以下是如何使用这些触发器和 <strong>商人模式</strong> 根据商人售出的 <em>钻石</em> 数量创建简单的 <em>折扣触发</em> 的简短示例。 <a href="http://scripts.citizensnpcs.com/view/lm66cf">样品</a>。</p>

