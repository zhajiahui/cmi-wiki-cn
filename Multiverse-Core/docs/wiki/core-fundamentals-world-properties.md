---
title: 世界属性
source_url: https://mvplugins.org/core/fundamentals/world-properties/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 世界属性

<p>以下是可以使用 <a href="core-fundamentals-commands-usage.md#Modify-Command">修改命令</a> 在游戏中设置的世界的各种属性。它们也可以设置在 <code>worlds.yml</code> 但 <strong>通常您不必编辑此文件</strong> 中。不过，如果您是高级用户，则可以。这是一个用 yaml 编写的典型插件配置文件，遵循与正常情况相同的语法。</p>
<a id="Index"></a><h2 id="index">索引</h2>
<ul>
<li><a href="#Adjust-Spawn">调整生成</a></li>
<li><a href="#Alias">别名</a></li>
<li><a href="#Allow-Advancement-Grant">允许授予进度</a></li>
<li><a href="#Allow-Flight">允许飞行</a></li>
<li><a href="#Anchor-Respawn">重生锚重生</a></li>
<li><a href="#Auto-Heal">自动治疗</a></li>
<li><a href="#Auto-Load">自动加载</a></li>
<li><a href="#Bed-Respawn">床重生</a></li>
<li><a href="#Difficulty">难度</a></li>
<li><a href="#Entity-Spawn-Config">实体生成配置</a></li>
<li><a href="#Environment">环境</a></li>
<li><a href="#Gamemode">游戏模式</a></li>
<li><a href="#Generators">生成器</a></li>
<li><a href="#Hunger">饥饿值</a></li>
<li><a href="#Keep-Spawn-in-Memory">保持出生点区块加载</a></li>
<li><a href="#Player-Limit">玩家限制</a></li>
<li><a href="#Portal-Form">门架成型</a></li>
<li><a href="#PVP">PVP</a></li>
<li><a href="#Respawn-World">重生世界</a></li>
<li><a href="#Scale">缩放</a></li>
<li><a href="#Seed">种子</a></li>
<li><a href="#Weather">天气</a></li>
<li><a href="#World-Blacklist">世界黑名单</a></li>
<li><a href="#World-Fees">世界费用</a></li>
<li><a href="#World-Visibility">世界可见性</a></li>
</ul>
<a id="Adjust-Spawn"></a><h2 id="adjust-spawn">调整生成</h2>
<p>默认情况下，Multiverse 将修复在不良位置记录的出生点。默认情况下，Minecraft 服务器使用类似 <code>getTopBlock()</code> 方法，并将出生点的 <code>Y</code> 坐标设置在地面中间的某个位置。直接传送玩家通常也不安全，因此 Multiverse 将搜索最近的安全位置。</p>
<p>有时这并不理想。如果您不希望 multiverse 执行此操作，只需打开此变量即可。如果您在不安全的位置（熔岩坑上方）设置出生点，Multiverse 将自动为您禁用此变量。</p>
<p>如果您想在导入世界时设置此变量，只需将 <code>-n</code> 添加到 <code>/mv create</code> 或 <code>/mv import</code> 命令中即可：</p>
<div class="highlight"><pre>/mv create spaceworld normal -g NullTerrainGenerator -n
</pre></div>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>adjust-spawn: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set adjust-spawn true</code><br/>
<code>/mv modify [world] set adjust-spawn false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Alias"></a><h2 id="alias">别名</h2>
<p>世界别名允许您以不同于文件夹名称的方式命名世界。这可以让你为你的世界选择奇特的名称，同时保持文件夹的美观和整洁。如果您的别名包含空格，则必须将其用引号引起来，例如：<code>"My World"</code>。</p>
<p>别名属性还可以包括颜色和样式。当您的用户通过 <a href="core-fundamentals-commands-usage.md#List-Command"><code>/mv list</code></a> 或 <a href="core-fundamentals-commands-usage.md#Who-Command"><code>/mv who</code></a> 聊天时，世界将显示颜色和样式。它还可用于聊天插件中的占位符（参见 <a href="core-reference-placeholders.md">我们的占位符</a>）</p>
<p><img alt="Example of world aliases with color" src="assets/867349695ac4-world-with-color.png"/></p>
<a id="Example:-Set-alias-to-Fern-World-(green)"></a><h3 id="example-set-alias-to-fern-world-green">示例：将别名设置为 <em>蕨类植物世界</em>（绿色）</h3>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set alias "&amp;aFern World"</code></p>
<p><strong>在config:</strong></p>
<div class="highlight"><pre>alias: "&amp;aFern World"
</pre></div>
<div class="admonition warning">
<p>尽管没有强制执行，但强烈建议 <strong>不</strong> 对多个世界使用相同的别名。这可能会给玩家和管理员带来困惑。</p>
<p>如果您想用相同的名称/类别标记多个世界，请考虑使用元数据键。请参阅 <a href="core-how-to-world-meta.md">世界元数据</a> 了解更多信息。</p>
</div>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Allow-Advancement-Grant"></a><h2 id="allow-advancement-grant">允许授予进度</h2>
<div class="admonition note">
<p>此世界属性仅适用于 PaperMC 服务器。</p>
</div>
<p>设置玩家的行为是否会在这个世界上带来相关的进步。这对于您不想向玩家授予进步的大厅世界非常有用。然而，这并不等于各世界独立进度。为此，请参阅 Multiverse-Inventories 可选进度共享。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>allow-advancement-grant: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set allow-advancement-grant false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Allow-Flight"></a><h2 id="allow-flight">允许飞行</h2>
<p>Multiverse 具有对每个世界禁用飞行的基本支持。默认情况下，此设置为 true，这将允许飞行。设置为 false 以禁用飞行。注意：这不会影响创造模式。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>allow-flight: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set allow-flight false</code><br/>
<code>/mv modify [world] set allow-flight true</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Anchor-Respawn"></a><h2 id="anchor-respawn">重生锚重生</h2>
<p>如果 <code>anchor-respawn</code> 设置为 true，玩家将能够在这个世界的重生锚点重生。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>anchor-respawn: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set anchor-respawn false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Auto-Heal"></a><h2 id="auto-heal">自动治疗</h2>
<p>如果你的<a href="#Difficulty">难度</a>设置为<code>peaceful</code>，默认情况下，玩家将恢复生命值。如果您不希望它们这样做，只需将此变量设置为 false 即可。此设置对 <a href="#Difficulty">难度</a> 大于 <code>peaceful</code> 或 <code>0</code> 的世界没有影响。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>auto-heal: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set auto-heal true</code><br/>
<code>/mv modify [world] set auto-heal false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Auto-Load"></a><h2 id="auto-load">自动加载</h2>
<p>告诉 Multiverse 在启动时自动加载这个世界。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>auto-load: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set auto-load false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Bed-Respawn"></a><h2 id="bed-respawn">床重生</h2>
<p>如果 <code>bed-respawn</code> 设置为 true，玩家将能够在这个世界的床上重生。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>bed-respawn: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set bed-respawn false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Difficulty"></a><h2 id="difficulty">难度</h2>
<p>允许您设置给定世界的难度。所有可能的值为：<code>0, 1, 2, 3, peaceful, easy, normal, hard</code>。请记住，只有 4 个困难，我们只是让您使用 int 或 string 来设置它。它们始终以整数形式存储在配置中。</p>
<p><strong>Type:</strong><br/>
<code>String</code> 或 <code>Integer</code></p>
<p><strong>Example:</strong><br/>
<code>difficulty: 1</code></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set difficulty 1</code><br/>
<code>/mv modify [world] set difficulty easy</code><br/>
<code>/mv modify [world] set difficulty hard</code><br/>
<code>/mv modify [world] set difficulty peaceful</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Entity-Spawn-Config"></a><h2 id="entity-spawn-config">实体生成配置</h2>
<p>Multiverse 允许您控制每个 <a href="https://jd.papermc.io/paper/26.1.2/org/bukkit/entity/SpawnCategory.html">生成类别</a> 每个世界的实体生成。有关完整命令参考，请参阅 <a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Info-Command">实体生成配置命令</a>。</p>
<a id="Spawn-Categories"></a><h3 id="spawn-categories">生成类别</h3>
<table>
<thead>
<tr>
<th>类别</th>
<th>示例</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>monster</code></td>
<td>僵尸、骷髅、苦力怕、女巫等</td>
</tr>
<tr>
<td><code>animal</code></td>
<td>牛、猪、鸡、乌龟、黾等</td>
</tr>
<tr>
<td><code>water_animal</code></td>
<td>鱿鱼、海豚</td>
</tr>
<tr>
<td><code>water_ambient</code></td>
<td>鳕鱼、三文鱼、热带鱼、河豚等</td>
</tr>
<tr>
<td><code>water_underground_creature</code></td>
<td>发光鱿鱼</td>
</tr>
<tr>
<td><code>ambient</code></td>
<td>蝙蝠</td>
</tr>
<tr>
<td><code>axolotl</code></td>
<td>蝾螈</td>
</tr>
<tr>
<td><code>misc</code></td>
<td>盔甲架、船、物品架等</td>
</tr>
</tbody>
</table>
<a id="Properties"></a><h3 id="properties">属性</h3>
<p>每个生成类别都有以下可配置的 properties:</p>
<h4 id="spawn">生成</h4>
<p>是否允许该类别的实体在世界中生成。 <code>exceptions</code> 列表按实体类型反转此值。</p>
<p><strong>Type:</strong> <code>boolean</code><br/>
<strong>Default:</strong> <code>true</code></p>
<h4 id="exceptions">例外情况</h4>
<p>否定 <code>spawn</code> 值的实体类型列表。如果 <code>spawn</code> 是 <code>false</code> 并且类型在此列表中，则生成该类型 <strong>会</strong>。如果 <code>spawn</code> 是 <code>true</code> 并且类型在此列表中，则生成该类型 <strong>不会</strong>。</p>
<p><strong>Type:</strong> <code>List&lt;EntityType&gt;</code></p>
<h4 id="tick-rate">滴答率</h4>
<p>此类别的每次生成尝试之间有多少个刻度。</p>
<p><strong>Type:</strong> <code>Integer</code><br/>
<strong>特价values:</strong><br/>
<code>@unset</code> — Multiverse 不会覆盖服务器默认值<br/>
<code>@bukkit</code> — 使用 Bukkit 的默认值</p>
<h4 id="spawn-limit">生成限制</h4>
<p>世界上一次可以存在的此类实体的最大数量。</p>
<p><strong>Type:</strong> <code>Integer</code><br/>
<strong>特价values:</strong><br/>
<code>@unset</code> — Multiverse 不会覆盖服务器默认值<br/>
<code>@bukkit</code> — 使用 Bukkit 的默认值</p>
<a id="YAML-Config"></a><h3 id="yaml-config">YAML 配置</h3>
<p>在 <code>worlds.yml</code> 中，生成设置存储在每个世界的 <code>spawning</code> 键下：</p>
<div class="highlight"><pre>spawning:
  monster:
    spawn: true
    tick-rate: '@unset'
    spawn-limit: '@unset'
    exceptions: []
  animal:
    spawn: true
    tick-rate: '@unset'
    spawn-limit: '@unset'
    exceptions: []
</pre></div>
<a id="EXAMPLE:-A-world-with-ONLY-pigs:"></a><h4 id="example-a-world-with-only-pigs">示例：只有 pigs: 的世界</h4>
<div class="highlight"><pre>spawning:
  animal:
    spawn: false
    exceptions:
    - PIG
</pre></div>
<p>您应该将其读作“动物 <strong>不能</strong> 为猪生成 <strong>除了</strong>”。</p>
<a id="EXAMPLE:-A-world-with-NO-creepers:"></a><h4 id="example-a-world-with-no-creepers">示例：没有 creepers: 的世界</h4>
<div class="highlight"><pre>spawning:
  monster:
    spawn: true
    exceptions:
    - CREEPER
</pre></div>
<p>您应该将其读作“怪物 <strong>可以</strong> 为苦力怕生成 <strong>除了</strong>”。</p>
<a id="In-Game-Usage"></a><h3 id="in-game-usage">游戏中的使用</h3>
<p>使用<code>/mv entity-spawn-config modify [world] &lt;category&gt; &lt;action&gt; &lt;property&gt; [value]</code>：</p>
<p><a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] monster set spawn false</code></a> — 禁用怪物生成。<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] animal set spawn true</code></a> — 启用动物生成。<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] monster add exceptions CREEPER</code></a> — 将 <code>CREEPER</code> 添加到怪物例外列表中。<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] monster remove exceptions CREEPER</code></a> — 从怪物例外列表中删除 <code>CREEPER</code>。<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] monster reset exceptions</code></a> — 清除怪物例外列表。<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] animal set tick-rate 400</code></a> — 将动物蜱率设置为 400.<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Modify-Command"><code>/mv entity-spawn-config modify [world] axolotl set spawn-limit 10</code></a> — 每个世界限制蝾螈数量为 10 只。<br/>
<a href="core-fundamentals-commands-usage.md#Entity-Spawn-Config-Info-Command"><code>/mv entity-spawn-config info [world]</code></a> — 显示世界的所有生成配置。</p>
<div class="admonition note">
<p>无论 <code>spawn</code> 设置如何，怪物都不会在 <a href="#Difficulty">难度</a> 设置为 <code>peaceful</code> 的世界中生成。</p>
</div>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Environment"></a><h2 id="environment">环境</h2>
<p>这个世界所处的环境类型。目前可以是 <code>NETHER</code>、<code>THE_END</code> 和 <code>NORMAL</code>。您 <strong>不应该</strong> 在配置中更改此值。</p>
<p><strong>Type:</strong><br/>
<code>String</code></p>
<p><strong>Example:</strong><br/>
<code>environment: NORMAL</code></p>
<p><strong>游戏中的用法：</strong><br/>
<a href="core-fundamentals-commands-usage.md#Create-Command"><code>/mv create myworld normal</code></a><br/>
<a href="core-fundamentals-commands-usage.md#Import-Command"><code>/mv import mynether nether</code></a></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Gamemode"></a><h2 id="gamemode">游戏模式</h2>
<p>允许您设置特定世界的模式类型。有关管理每个世界库存的更多信息，请参阅 <a href="https://mvplugins.org/inventories">Multiverse-Inventories</a>。</p>
<p>如果你想让某些玩家忽略世界中设置的游戏模式，有一个特殊的permission:</p>
<div class="highlight"><pre>mv.bypass.gamemode.[*|WORLDNAME]
</pre></div>
<p>此权限位于不同的根命名空间下，因为默认情况下它是关闭的。</p>
<p><strong>Type:</strong><br/>
<code>String</code></p>
<p><strong>Example:</strong><br/>
<code>gamemode: SURVIVAL</code></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set gamemode survival</code><br/>
<code>/mv modify [world] set gamemode creative</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Generators"></a><h2 id="generators">生成器</h2>
<p>Multiverse 2 允许您通过 <a href="core-reference-custom-generator-plugins.md">自定义生成器插件</a> 使用自定义世界生成器。此行包含多元宇宙正确加载您的世界所需的信息。除非您知道自己在做什么，否则您 <strong>不应该</strong> 会触及此值。</p>
<p>该值可能存在也可能不存在。没关系。</p>
<p><strong>类型</strong>:<br/>
<code>String</code></p>
<p><strong>Example:</strong><br/>
<code>generator: BukkitFullOfMoon</code></p>
<p><strong>游戏中的用法：</strong><br/>
<a href="core-fundamentals-commands-usage.md#Create-Command"><code>/mv create moon NORMAL --generator BukkitFullOfMoon</code></a></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Hunger"></a><h2 id="hunger">饥饿值</h2>
<p>允许您在每个世界中启用或禁用饥饿消耗。</p>
<p><strong>类型</strong>:
<code>Boolean</code></p>
<p><strong>Example:</strong>
<code>hunger: true</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set hunger true</code><br/>
<code>/mv modify [world] set hunger false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Keep-Spawn-in-Memory"></a><h2 id="keep-spawn-in-memory">保持出生点区块加载</h2>
<p>关闭后，Bukkit 不会在内存中保持此世界的出生点区块加载，因此在没有玩家登录时可以减少服务器的内存占用。</p>
<div class="admonition note">
<p>此功能已在 1.21.9+ 中被 Minecraft 删除。将其设置为 <code>true</code> 对运行 1.21.9 或更高版本的服务器没有影响。</p>
</div>
<p><strong>Type:</strong><br/>
<code>boolean</code></p>
<p><strong>Example:</strong><br/>
<code>keep-spawn-in-memory: true</code></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set keep-spawn-in-memory false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Player-Limit"></a><h2 id="player-limit">玩家限制</h2>
<p>Multiverse 能够设置世界中允许的最大玩家数量。默认情况下，限制设置为 <code>-1</code> 表示无限制。该设置是指定允许多少玩家。</p>
<p>玩家可以通过以下权限绕过此限制：
<code>mv.bypass.playerlimit.*</code> 适用于所有世界。
<code>mv.bypass.playerlimit.NAME</code> 适用于特定世界。</p>
<p><strong>类型</strong>:
<code>Integer</code></p>
<p><strong>Example:</strong>
<code>player-limit: -1</code></p>
<p><strong>游戏中的用法：</strong>
<code>/mv modify [world] set player-limit 10</code><br/>
<code>/mv modify [world] set player-limit -1</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Portal-Form"></a><h2 id="portal-form">传送门生成</h2>
<p>Multiverse 允许您控制是否允许用户创建传送门。</p>
<p>允许传送门形成必须是 <code>NONE</code>、<code>ALL</code>、<code>NETHER</code> 或 <code>END</code>。</p>
<p><strong>类型</strong>
<code>String</code></p>
<p><strong>示例</strong>:
<code>portal-form: ALL</code></p>
<p><strong>游戏中的使用</strong>:
<code>/mv modify [world] set portal-form none</code><br/>
<code>/mv modify [world] set portal-form nether</code></p>
<p>结果是相当不言自明的。当玩家尝试创建对世界禁用的传送门时，他们将收到一条消息，通知他们这是不允许的。</p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="PVP"></a><h2 id="pvp">PVP</h2>
<p>玩家在这个世界上是否可以互相伤害。如果设置为 <code>true</code>，则可以。</p>
<p><strong>Type:</strong><br/>
<code>boolean</code></p>
<p><strong>Example:</strong><br/>
<code>pvp: true</code></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set pvp false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Respawn-World"></a><h2 id="respawn-world">重生世界</h2>
<p>当这个世界发生重生事件时，你将重生到的世界。这个值可以和这个世界一样。</p>
<p>重生事件包括：
- 死在世界上
- 击败末影龙后使用末日中的出口传送门（这算作重生事件，因此在末地世界中设置 <code>respawn-world</code> 可以控制玩家击败末影龙后着陆的位置）</p>
<p><strong>Type:</strong><br/>
<code>String</code></p>
<p><strong>Example:</strong></p>
<div class="highlight"><pre>respawn-world: "hellplanet"
</pre></div>
<p><strong>NOTE:</strong> 如果您看到 <code>temprespawn</code> 值，则可以将其删除。它在迁移器的早期版本中得到了延续。</p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify &lt;death world&gt; set respawn-world &lt;respawn-world&gt;</code><br/>
<code>/mv modify survival set respawn-world hub</code> — 在生存中死亡时在中心重生<br/>
<code>/mv modify world_the_end set respawn-world world</code> — 击败末影龙后将玩家送回主世界</p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Scale"></a><h2 id="scale">缩放</h2>
<p>使用 Multiverse-NetherPortals 时的世界缩放。设置此值对除 Multiverse-NetherPortals 之外的任何内容都没有影响。请参阅 <a href="https://mvplugins.org/netherportals/fundamentals/basic-usage">Multiverse-NetherPortals 文档</a> 了解其工作原理。</p>
<p><strong>Type:</strong><br/>
<code>double</code></p>
<p><strong>NOTE:</strong> 如果您看到 <code>scaling</code> 值，则可以将其删除。它在迁移器的早期版本中被保留，现在的值是 <code>scale</code>。</p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set scale 1.2</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Seed"></a><h2 id="seed">种子</h2>
<p>这个世界的种子。除非您知道这样做的后果，否则请勿更改（<strong>WILL</strong> 会导致区块错误！）。</p>
<p><strong>Type:</strong><br/>
<code>String</code></p>
<p><strong>Example:</strong><br/>
<code>seed: 'gargamel'</code></p>
<p><strong>游戏中的用法：</strong><br/>
<strong>该命令不能在游戏中使用。你无法改变生成世界的种子。</strong></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="Weather"></a><h2 id="weather">天气</h2>
<p>如果该值为真，则世界将发生天气事件，如果为假，则不会。如果你想关闭当前的风暴，只需输入<code>/mv modify [world] set allow-weather false</code>，等待天气消退，然后输入<code>/mv modify [world] set allow-weather true</code>。</p>
<p><strong>Type:</strong><br/>
<code>boolean</code></p>
<p><strong>Example:</strong><br/>
<code>allow-weather: true</code></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set allow-weather false</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="World-Blacklist"></a><h2 id="world-blacklist">世界黑名单</h2>
<p>世界黑名单允许您指定 <strong>不能去</strong> 从指定世界进入的世界。例如，如果您将 <code>world_gold</code> 添加到 <code>world</code> 的 <code>worldblacklist</code>，则玩家可以从 <code>world</code> 传送到 <code>world_gold</code>，但不能返回。</p>
<p><strong>Type:</strong><br/>
<code>List&lt;String&gt;</code></p>
<p><strong>Example:</strong>
<div class="highlight"><pre>worldblacklist:
- world_fish
- world_dog
</pre></div></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] add world-blacklist &lt;world_to_block&gt;</code> - 将世界添加到黑名单<br/>
<code>/mv modify [world] remove world-blacklist &lt;world_to_block&gt;</code> - 从黑名单中删除世界</p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="World-Fees"></a><h2 id="world-fees">世界费用</h2>
<p>您可以向用户收取进入各个世界的费用。最酷的部分是您不必使用经济插件！您可以简单地使用Minecraft物品！</p>
<a id="Enabled"></a><h3 id="enabled">启用</h3>
<p>该世界的入场费是否有效。</p>
<p><strong>Type:</strong><br/>
<code>boolean</code></p>
<p><strong>Example:</strong><br/>
<code>entry-fee.enabled: false</code></p>
<a id="Amount-vs.-Currency"></a><h3 id="amount-vs-currency">金额与货币</h3>
<p><code>amount</code> 字段是您要向人员收费的 <strong>多少</strong>。这可以是整数或双精度数。 （1 或 1.75）</p>
<p><code>currency</code> 字段是您要向人员收费的 <strong>什么</strong>。这是材质名称（e.g.<code>DIRT</code>），如果您想使用经济插件中的虚拟货币，则为 <code>@vault-economy</code>。</p>
<a id="EXAMPLE:-Charging-5-Dirt-to-enter-a-world"></a><h3 id="example-charging-5-dirt-to-enter-a-world">示例：充入 5 个泥土即可进入世界</h3>
<div class="highlight"><pre>entry-fee:
  enabled: true
  amount: 5
  currency: DIRT
</pre></div>
<a id="EXAMPLE:-Charging-$13.75-to-enter-a-world"></a><h3 id="example-charging-1375-to-enter-a-world">示例：收费 13.75 美元进入一个世界</h3>
<p><strong>NOTE:</strong> 您必须安装有效的经济插件（例如，<a href="https://essentialsx.net/">EssentialsX</a>）以及<a href="https://www.spigotmc.org/resources/vault.34315/">Vault</a>才能使用经济货币（<code>@vault-economy</code>）。</p>
<div class="highlight"><pre>entry-fee:
  enabled: true
  amount: 13.75
  currency: '@vault-economy'
</pre></div>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set entryfee-enabled true</code> - 启用世界入场费<br/>
<code>/mv modify [world] set entryfee-currency DIRT</code> - 将物品货币设置为泥土<br/>
<code>/mv modify [world] set entryfee-currency @vault-economy</code> - 将货币设置为 Vault 经济货币<br/>
<code>/mv modify [world] set entryfee-amount 5</code> - 需要 5 个已配置货币</p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>
<a id="World-Visibility"></a><h2 id="world-visibility">世界可见性</h2>
<p>此属性允许您拥有一个存在但不显示在列表中的世界。当用户从这个世界聊天时，如果<code>worldnameprefix</code>设置为<code>true</code>并且隐藏，他们的聊天将显示没有世界前缀。</p>
<p><strong>Type:</strong><br/>
<code>Boolean</code></p>
<p><strong>Example:</strong><br/>
<code>hidden: false</code></p>
<p><strong>游戏中的用法：</strong><br/>
<code>/mv modify [world] set hidden true</code></p>
<p><a href="#top">↑ 返回顶部 ↑</a></p>

