---
title: 世界入场费
source_url: https://mvplugins.org/core/how-to/setup-entry-fee/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 世界入场费

<p>Multiverse 允许您向玩家收取进入世界的入场费。您可以对物品或虚拟货币进行收费（通过 <a href="https://www.spigotmc.org/resources/vault.34315/">Vault</a> + 经济插件）。</p>
<a id="Setting-an-entry-fee"></a><h2 id="setting-an-entry-fee">设置入场费</h2>
<p>使用 <code>/mv modify</code> 配置三个入场费属性：</p>
<a id="Enable/disable-the-fee"></a><h3 id="enabledisable-the-fee">启用/禁用费用</h3>
<div class="highlight"><pre>/mv modify [world] set entryfee-enabled true
/mv modify [world] set entryfee-enabled false
</pre></div>
<a id="Set-the-amount"></a><h3 id="set-the-amount">设定金额</h3>
<div class="highlight"><pre>/mv modify [world] set entryfee-amount &lt;amount&gt;
</pre></div>
<a id="Set-the-currency"></a><h3 id="set-the-currency">设置货币</h3>
<p>对于 <strong>项目</strong>，使用 Minecraft 材料名称：</p>
<div class="highlight"><pre>/mv modify [world] set entryfee-currency DIRT
</pre></div>
<p>对于 <strong>虚拟货币</strong>（需要 <a href="https://www.spigotmc.org/resources/vault.34315/">Vault</a> 和兼容的经济插件，例如 <a href="https://essentialsx.net/">EssentialsX</a>）：</p>
<div class="highlight"><pre>/mv modify [world] set entryfee-currency @vault-economy
</pre></div>
<a id="Example:-Charge-5-Dirt-to-enter-FernWorld"></a><h2 id="example-charge-5-dirt-to-enter-fernworld">示例：充入 5 块泥土即可进入 FernWorld</h2>
<div class="highlight"><pre>/mv modify FernWorld set entryfee-enabled true
/mv modify FernWorld set entryfee-amount 5
/mv modify FernWorld set entryfee-currency DIRT
</pre></div>
<a id="Example:-Charge-$13.75-to-enter-VIPWorld"></a><h2 id="example-charge-1375-to-enter-vipworld">示例：收费 13.75 美元进入 VIPWorld</h2>
<div class="highlight"><pre>/mv modify VIPWorld set entryfee-enabled true
/mv modify VIPWorld set entryfee-amount 13.75
/mv modify VIPWorld set entryfee-currency @vault-economy
</pre></div>
<a id="Exempting-players"></a><h2 id="exempting-players">豁免球员</h2>
<p>要免除选手或团体支付报名费，请授予 permission:</p>
<div class="highlight"><pre>multiverse.exempt.[worldname]
</pre></div>
<p>例如，<code>multiverse.exempt.VIPWorld</code>可以让玩家免费进入VIPWorld。</p>
<a id="YAML-reference"></a><h2 id="yaml-reference">YAML参考</h2>
<p>入场费设置存储在每个世界下的<code>worlds.yml</code>中：</p>
<div class="highlight"><pre>entry-fee:
  enabled: true
  amount: 5
  currency: DIRT
</pre></div>
<p>完整参考请参见 <a href="core-fundamentals-world-properties.md#World-Fees">世界地产</a>。</p>

