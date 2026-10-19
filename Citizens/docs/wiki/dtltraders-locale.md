---
title: DtlTraders / 语言
source_url: https://wiki.citizensnpcs.co/DtlTraders/locale
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4144
---


<a id="top"></a>

# DtlTraders / 语言

<a id="Locale_incoming_with_version_2.5"></a><h2 id="locale-incoming-with-version-25">版本 2.5 引入语言</h2>
<a id="General_changes"></a><h3 id="general-changes">一般变化</h3>
<p>一般来说，整个语言系统都发生了变化。
这使我能够创建一个自我更新的语言，因此，如果您在默认的英文版本中运行该插件，则不再需要关心语言，它会在需要时自行更新:)</p>
<p>另外，翻译语言应该更容易，每个键现在都以非常明显的方式命名：P
减少了关键字的数量，但从现在开始，语言中出现了更多消息</p>
<ol>
<li>所有旧消息均已重命名，因此更加明显</li>
<li>许多关键字被删除</li>
<li>将传说添加到语言文件中</li>
</ol>
<a id="Updating"></a><h3 id="updating">更新中</h3>
<p>当语言要自我更新时，它会将所有旧消息 <strong>备份</strong> 放入同一语言文件中的 <strong>备份</strong> 树中，因此没有消息会随着更新而消失。
但是，如果要对某个语言进行多次更新，则先前更新的备份就会丢失。</p>
<p>另外，在创建 <strong>翻译的语言</strong> 时，请始终记住为要创建语言的版本设置 <strong>版本</strong> 标记</p>
<a id="Latest_build_changes"></a><h3 id="latest-build-changes">最新构建更改</h3>
<p>该文件告诉更新程序哪些更改适用于过时的语言文件。
根据定义中是否存在 <strong>新的</strong> 键，它将 <strong>添加</strong> 或 <strong>改变</strong> 指定的语言条目。</p>
<p>example:</p>
<div class="highlight"><pre>  player-trader:
    keyword: Player Trader
    new: trader-player
</pre></div>
<p>将查找 <strong>玩家商人</strong> 关键字，将其保存到备份树中，并使用给定值添加一个名称为 <strong>新的</strong> 的新键。</p>
<p>该文件将在发布版本之后的任何下一个版本中被清除。</p>
<div class="highlight"><pre>messages: 
  denizen-item-hint:
    message: '{item}: {price}'
  trader-transaction-success: 
    message: ^6You {action} ^3{amount} ^6for ^3{price}
  error-argument-invalid:
    message: '^6Invalid argument was supplied: ^3{argument}'
  plugin-command-message: 
    message: '^6== dtlTraders ^3{version} ^6=='
  error-npc-not-selected:
    message: '^6You did not selected any trader'
  wallet-balance: 
    message: '^6Wallet balance: ^3{amount}'
  wallet-deposit: 
    message: ^6Deposited ^3{amount} 
  wallet-deposit-fail: 
    message: 'You dont have enought money' 
  wallet-withdraw: 
    message: ^6Withdrawed ^3{amount} 
  wallet-withdraw-fail: 
    message: '^6Is there enough money to withdraw from this wallet?' 
  wallet-invalid: 
    message: ^6You can not use this command on this wallet type
  pattern-save-success: 
    message: ^6Successfuly created ^3{pattern} ^6pattern
  pattern-save-fail-exists: 
    message: ^6This pattern already exists {pattern}
  error-command-invalid: 
    message: '^6This command is invalid'
  banker-created: 
    message: '^6You created a new banker: {banker}'
  trader-created:
    message: '^6You created a new trader: {trader}'
keywords: 
  bought:
    keyword: Bought
  sold: 
    keyword: Sold
  type: 
    keyword: Type
  server-trader:
    keyword: Server Trader
    new: trader-server
  player-trader:
    keyword: Player Trader
    new: trader-player
  market-trader:
    keyword: Market Trader
    new: trader-market
  banker-type: 
    keyword: Banker type
  banker-private: 
    keyword: Private Banker
  banker-money:
    keyword: Money Banker
lores: 
  manage-price: 
    name: ^r^6Price management
    lore:
    - ^7Click to toggle price managing
  manage-buy-limit: 
    name: ^r^6Buy limit management
    lore:
    - ^7Allows to set amounts you 
    - ^7want to buy from players
</pre></div>
<a id="Release_locale_file_(atm_latest_build_version)"></a><h3 id="release-locale-file-atm-latest-build-version">发布语言文件（atm 最新构建版本）</h3>
<div class="highlight"><pre>ver: 1.0.5
messages:
  plugin-reload: ^6Successfuly reloaded ^3dtlTraders
  plugin-command-message: '^6== dtlTraders ^3{version} ^6=='
  error-nopermission: ^6You dont have permissions to do this
  error-nopermission-creative: ^6You dont have permissions to do this while in ^3creative mode
  error-command-invalid: '^6This command is invalid'
  error-argument-missing: '^6Argument is missing: {argument}'
  error-argument-invalid: '^6Invalid argument was supplied: ^3{argument}'
  error-npc-not-selected: '^6You did not selected any trader'
  trader-manage-toggle: ^6Toggled ^3{mode} ^6management
  trader-created: '^6You created a new trader: {trader}'
  trader-stock-item-select: ^6Item selected
  trader-stock-item-add: ^6Item added
  trader-stock-item-update: ^6Item updated
  trader-stock-item-remove: ^6Item removed
  trader-transaction-success: ^3You bought/sold an item
  trader-transaction-failed-limit: ^6Limit for that item has been reached
  trader-transaction-failed-inventory: ^6You dont got enough place in your inventory
  trader-transaction-failed-money: ^6Someone does not have enough money
  managermode-enabled: ^6Manager mode enabled for ^3{npc}
  managermode-disabled: ^6Manager mode disabled for ^3{npc}
  wallet-balance: '^6Wallet balance: ^3{amount}'
  wallet-deposit: ^6Deposited ^3{amount} 
  wallet-deposit-fail: 'You dont have enought money' 
  wallet-withdraw: ^6Withdrawed ^3{amount} 
  wallet-withdraw-fail: '^6Is there enough money to withdraw from this wallet?' 
  wallet-invalid: ^6You can not use this command on this wallet type
  pattern-save-success: ^6Successfuly created ^3{pattern} ^6pattern
  pattern-save-fail-exists: ^6This pattern already exists ^3{pattern}
  banker-created: '^6You created a new banker: {banker}'
  banker-tab-switch: ^6Switched to ^3{tab}
  banker-deposit-success: ^6Item deposited
  banker-withdraw-success: ^6Item withdrawed 
  banker-tab-buy-success: ^6Bought a new tab
  banker-tab-select-item: ^6Select a new tab item
  banker-tab-select-item-success: ^6New item was set
  banker-tab-select-item-canceled: ^6Selecting was aborted
  denizen-item-hint: '{item}: {price}'
  key-change: '^6Changed {key}: ^3{value}'
  key-value: '^6{key}: ^3{value}'
keywords:
  manage-global-limit: Global limit
  manage-player-limit: Player Limit
  manage-stock: Stock
  manage-price: Price
  price: Price
  owner: Owner
  wallet: Wallet
  stack-price: Stack price
  enabled: Enabled
  disabled: Disabled
  tab-price: Tab price
  trader-type: Trader type
  trader-server: Server Trader
  trader-player: Player Trader
  trader-market: Market Trader
  banker-type: Banker type
  banker-private: Private Banker
  banker-money: Money Banker
lores:
  player-inventory:
    lore:
    - '^7Unit price: ^6{unit}'
    - '^7Stack price: ^6{stack}'
    - ^7Click to sell
  trader-inventory-sell:
    lore:
    - '^7Price: ^6{price}'
    - ^7Click to buy
  trader-inventory-buy:
    lore:
    - '^7Price: ^6{price}'
  sell-tab:
    name: ^r^6Sell stock
    lore:
    - ^7Click to switch to buy stock
  buy-tab:
    name: ^r^6Buy stock
    lore:
    - ^7Click to switch to sell stock
  manage-price: 
    name: ^r^6Price management
    lore:
    - ^7Click to toggle price managing
  manage-global-limit: 
    name: ^r^6Global limit management
    lore:
    - ^7Click to toggle global limit managing
  manage-player-limit: 
    name: ^r^6Player limit management
    lore:
    - ^7Click to toggle player limit managing
  manage-buy-limit: 
    name: ^r^6Buy limit management
    lore:
    - ^7Allows to set amounts you 
    - ^7want to buy from players
  return: 
    name: ^r^6Return
    lore:
    - ^7Return to stock management
  amounts-return: 
    name: 'Back to stock'
</pre></div>
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
<tr>
<td>Denizen 支持</td>
<td></td>
</tr>
</tbody>
</table>

