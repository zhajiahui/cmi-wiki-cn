---
title: DtlTraders / 钱包
source_url: https://wiki.citizensnpcs.co/DtlTraders/wallets
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=3978
---


<a id="top"></a>

# DtlTraders / 钱包

<a id="Overview"></a><h2 id="overview">概述</h2>
<p>钱包是一种让商家看起来更加现实的方式，它可以为商家提供预先确定的交易金额。它们还可以让您更好地控制服务器经济。此外，它们是玩家管理自己创建的商人账户余额的唯一方式。</p>
<a id="Wallet_types"></a><h2 id="wallet-types">钱包类型</h2>
<p>目前有七种钱包类型为supported:</p>
<ul>
<li><strong>无限</strong>（仅限管理员）- 商人拥有无限的资金。</li>
<li><strong>NPC</strong> - 商人有自己独立的钱包，除非他能负担得起，否则无法购买物品。商人的所有者可以在他和商人之间转移资金。</li>
<li><strong>owner</strong> - 允许商人直接使用其所有者的游戏内货币。商人进行的任何交易都会影响该玩家的余额。</li>
<li><strong>bank</strong> - 商人使用指定的银行账户。您必须是该银行的所有者才能使用此功能。</li>
</ul>
<p>重要提示：不再支持此钱包，它们将通过另一个插件添加，对此感到抱歉</p>
<ul>
<li><strong>SimpleClans</strong> - 商人使用指定部落的银行账户。必须提供部落标签。</li>
<li><strong>Factions</strong> - 商人使用指定派系的银行账户。必须提供派系标签。</li>
<li><strong>Towny</strong> - 商人使用指定城镇的银行账户。必须提供城镇标签。</li>
</ul>
<a id="Setting_the_wallet_type"></a><h2 id="setting-the-wallet-type">设置钱包类型</h2>
<p>设置钱包类型 use:  </p>
<p>/Trader wallet [钱包类型] [银行名称 <em>或</em> 部落/派系/城镇标签]</p>
<p>当不提供参数时，命令返回当前的钱包类型。</p>
<a id="Managing_a_wallet"></a><h2 id="managing-a-wallet">管理钱包</h2>
<p>要管理 NPC 钱包类型的商人，请使用以下 commands:  </p>
<p>/商人余额<br/>
/商人提现 &lt;amount&gt;<br/>
/商人保证金 &lt;amount&gt; <em>（此命令的修复将包含在 v2.3.0 Beta 中）</em></p>
<p>注意：命令将在当前选择的 NPC 上执行。</p>

