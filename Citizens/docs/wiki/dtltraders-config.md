---
title: DtlTraders / 配置
source_url: https://wiki.citizensnpcs.co/DtlTraders/config
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=4963
---


<a id="top"></a>

# DtlTraders / 配置

<p>为了确保你们每个人都能理解配置文件，我决定在这里解释每个配置选项，我将尝试举例说明它将如何影响您使用此插件的方式，以及如果您使用更高级的功能，它会有多大帮助。</p>
<a id="Default_config_file"></a><h2 id="default-config-file">默认配置文件</h2>
<div class="highlight"><pre>debug: critical
#locale settings
locale:
  #the choosen localization to load
  load: en
  #should the locale updated autmaticaly, (not implemented)
  auto-update: false
#logging settings
logging:
  #should transactions be logged? (false/FILE/SQL/WEB) , (not used at this moment)
  log: false
  #the foramt how transactions should be logged to FILE, (not used at this moment)
  log-format: ''
#statistics
statistics: 
  #enable or disable statistics (not implemented)
  enabled: false
  #metrics should be enabled? (not implemented)
  metrics: false
#trader types related settings
trader:
  #sets if left clicking the Trader should damage him, if set to false the trader wont be damaged and the click will be handled as ManagerMode toogling
  #when the player meets the requirements (permissions, and right-click = false)
  #it this setting is set to true, manager modes is toggled only when sneaking 
  allow-damage: false
  #item used to toggle between modes (air counts for anything)
  #transaction related settings
  transaction:
    #sets if buying and selling should be done after clicking on a item twice in a row
    double-click: false
  #manager mode related settings
  managing:
    #the starting stock when opening a trader (buy/sell)
    start-stock: sell
    #right click toggling (instead of left click, which is default from 3.0+) 
    #Attention: When PvP is disabled in the world, and the NPC is Player-Type, left click may not work!
    #if r.click toggling is enabled the item needs to be other than AIR. If not set to an item "stick" item will be used.
    right-click: false
    item: 'air'
    #special blocks used when setting prices and limits, format =&gt; 'item_id value'
    special-blocks:
    - dirt 0.01
    - wood 0.1
    - log 10
    - cobblestone 100
    - stone 10000
  #stock related settings
  stock:
    #default starting stock (if this stock is set and not empty!, this does not apply for player traders)
    start-stock: 'sell'
    #default stock size in rows, min 1, max 6 (applied on creation)
    size: 6
    #default stock name format, how should be the traders stock named by default, {npc} tag for npc name
    format: '{npc}^r''s shop'
  #wallet related settings
  wallet:
    #default wallet type for traders (if set to infinite player traders will use "owner" type instead)
    type: 'infinite'
    #initial wallet money on creation (does not apply for player traders)
    money: 0.0
  #pattern related settings
  pattern:
    #default patterns applied to each market and server trader uppon creation (array setting)
    defaults: []
    #the file where patterns are saved
    file: 'patterns.yml'
  #book item related settings
  books:
    #the file where book datas are stored
    file: 'books.yml'
    #how should be books stored? (file)
    store: 'file'
  #player trader related settings
  player:
    #limits of player traders per player
    limit: 1
    #default stock size for player traders, if set overrides the stock.size setting
    size: 2
    #default stock name format, how should be the traders stock named by default, {npc} tag for npc name, and {player} for the traders owner
    #if set overrides the stock.format setting
    format: '{npc}^r''s shop, {player}''s company'
  #ui related settings
  ui:
    #item that will "link" to sell stock
    sell: wool:1
    #item that will "link" to buy stock
    buy: wool:2
    #item that will "link" back to a basic stock
    back: wool:14
    #item that will "link" to price managing
    price: wool:15
    #item that will "link" to limit managing
    limit: wool:3
    #item that will "unlock" the stock for eiding
    lock: wool:4
    #item that will "lock" the stock (saving all changes)
    unlock: wool:5
#denizen support related settings
denizen: []
</pre></div>
<a id="Debug"></a><h2 id="debug">调试</h2>
<p>插件有时会有一个调试记录器，此功能使您和我可以更轻松地跟踪错误，如果出现错误，将此节点更改为较低的优先级值，将显示有关插件操作和行为的更多信息。 dtlTraders 调试器获得 <strong>六</strong> 日志记录级别、<strong>批评的</strong>、<strong>高</strong>、<strong>正常</strong>、<strong>低</strong>、<strong>信息</strong>、<strong>无</strong>。</p>
<p>将级别设置为 <strong>无</strong> 将使记录器完全静音，因此当出现任何问题时不会显示错误（除非情况非常严重）。</p>
<p><strong>批评的</strong> 级别设置仅显示完全破坏插件操作的错误，因此它们确实很少见，应报告给插件开发人员。</p>
<p><strong>高</strong> 级别设置显示干扰插件正在执行的操作的错误，但没有更改操作结果。</p>
<p><strong>正常</strong> 级别设置显示了所有可能导致更严重问题的情况。</p>
<p><strong>低</strong> 和 <strong>信息</strong> 级别显示几乎所有底层信息，服务器管理员不应使用这些级别，除非您需要有关插件行为的信息，否则记录器发送的数据量将使控制台无法读取。</p>
<p>此外，还有自定义日志记录级别，但仅用于特定情况。</p>
<a id="Level_relations"></a><h3 id="level-relations">层级关系</h3>
<table>
<thead>
<tr>
<th>等级</th>
<th>演出</th>
</tr>
</thead>
<tbody>
<tr>
<td>无，[假，禁用]</td>
<td>什么都没有</td>
</tr>
<tr>
<td>关键</td>
<td>关键</td>
</tr>
<tr>
<td>高</td>
<td>高、关键</td>
</tr>
<tr>
<td>正常</td>
<td>正常、高、严重</td>
</tr>
<tr>
<td>低</td>
<td>低、正常、高、严重</td>
</tr>
<tr>
<td>信息</td>
<td>信息、低、正常、高、严重</td>
</tr>
<tr>
<td>定制</td>
<td>定制</td>
</tr>
</tbody>
</table>
<a id="Locale_section"></a><h2 id="locale-section">语言部分</h2>
<p>此部分允许您选择此插件要使用的语言，以及在发现新版本时是否应自动更新。</p>
<div class="highlight"><pre>   load: en
</pre></div>
<p>该节点用于选择您要使用的语言，它首先在 <strong>语言</strong> 文件夹中查找名为 <strong>locale.&lt;target&gt;.yml</strong> 的文件，其中 <strong>&lt;target&gt;</strong> 部分是您在 <strong>负载</strong> 节点中设置的值，因此在本例中为 <strong>locale.en.yml</strong></p>
<p>如果它不存在，它将尝试在插件资源中查找该语言文件，如果第二次找不到它，则会抛出 <strong>批评的</strong> 错误，并且插件将无法正常工作。</p>
<div class="highlight"><pre>   auto-update: false
</pre></div>
<p>信息：该节点未使用！</p>
<p>将 <strong>自动更新</strong> 设置为 <strong>true</strong> 允许管理语言更新，如果发现您正在使用的语言有 <em>（语言版本较高）</em> 更新，它将自动将所有行替换为最新版本。</p>
<a id="Trader_section"></a><h2 id="trader-section">商人部分</h2>
<p>此部分中的所有设置都会影响服务器上所有商人的行为，因此更改此处的任何设置都会影响游戏中的每个商人，但是某些设置只会影响新创建的商人。</p>
<hr/>
<div class="highlight"><pre>   allow-damage: false
</pre></div>
<p>允许您更改 <strong>左键点击</strong> <em>（损坏）</em> 为商人时的行为。当设置为 <strong>false</strong> 时，它将禁用对商人造成的任何伤害，此外，它将检查玩家是否有权切换 <strong>经理模式</strong>，除非 <strong>右键点击</strong> 设置设置为 <strong>true</strong>。</p>
<p>如果将此设置设置为 <strong>true</strong>，您可能会损坏商人 <em>（如果其他公民设置也允许这样做）</em>，并且只有在 <strong>偷偷摸摸</strong> 时才能切换 <strong>经理模式</strong>。</p>
<a id="Transactions"></a><h3 id="transactions">交易</h3>
<div class="highlight"><pre>   double-click: false
</pre></div>
<p>更改购买或出售时的点击行为，默认情况下，如果设置为 <strong>false</strong>，则点击一次即可出售和购买物品，如果设置为 <strong>true</strong>，则需要 <strong>双击</strong> 物品才能执行任何操作。</p>
<a id="More_coming_soon!"></a><h3 id="more-coming-soon">更多即将推出！</h3>
<a id="denizen_section"></a><h2 id="denizen-section">居民部分</h2>

