---
title: 占位符
source_url: https://mvplugins.org/core/reference/placeholders/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 占位符

<p>Multiverse 5增加了对<a href="https://www.spigotmc.org/resources/placeholderapi.6245/">PlaceholderAPI</a>的官方支持。这意味着您可以访问许多其他也支持 PAPI 的插件中的世界属性。不要再使用 ecloud 版本了！要启用它，请确保在配置文件中设置 <code>register-papi-hook: true</code>。</p>
<a id="Format"></a><h2 id="format">格式</h2>
<p>所有占位符都遵循 <code>%multiverse-core_&lt;placeholder&gt;_&lt;optional world&gt;%</code> 的格式，其中占位符是世界属性，并且可以选择省略世界，然后它将使用玩家当前的世界。</p>
<a id="Migrating-from-v4-to-v5"></a><h2 id="migrating-from-v4-to-v5">从 v4 迁移到 v5</h2>
<p>如果您从 v4（ecloud 版本）迁移，则占位符格式会发生变化。一般来说，所有前缀都从<code>%multiverse_xxx%</code>更改为<code>%multiverse-core_xxx%</code>。还可能存在一些细微的文本格式差异，特别是对于 <code>time</code> 占位符。</p>
<a id="Big-list-o'-placeholders"></a><h2 id="big-list-o-placeholders">占位符大列表</h2>
<p>如果需要的话，这些也可以在最后添加一个世界，如前所述。</p>
<ul>
<li><code>%multiverse-core_alias%</code></li>
<li><code>%multiverse-core_animalspawn%</code></li>
<li><code>%multiverse-core_autoheal%</code></li>
<li><code>%multiverse-core_blacklist%</code></li>
<li><code>%multiverse-core_currency%</code></li>
<li><code>%multiverse-core_difficulty%</code></li>
<li><code>%multiverse-core_entryfee%</code></li>
<li><code>%multiverse-core_environment%</code></li>
<li><code>%multiverse-core_flight%</code></li>
<li><code>%multiverse-core_gamemode%</code></li>
<li><code>%multiverse-core_generators%</code></li>
<li><code>%multiverse-core_hunger%</code></li>
<li><code>%multiverse-core_isloaded%</code></li>
<li><code>%multiverse-core_key%</code> — 世界命名空间键 (e.g.<code>minecraft:overworld</code>、<code>myplugin:myworld</code>)</li>
<li><code>%multiverse-core_meta_&lt;key&gt;%</code> — 按键的 <a href="core-how-to-world-meta.md">世界元</a> 值 (e.g.<code>%multiverse-core_meta_category%</code>)</li>
<li><code>%multiverse-core_monstersspawn%</code></li>
<li><code>%multiverse-core_name%</code></li>
<li><code>%multiverse-core_playercount%</code></li>
<li><code>%multiverse-core_playerlimit%</code></li>
<li><code>%multiverse-core_price%</code></li>
<li><code>%multiverse-core_pvp%</code></li>
<li><code>%multiverse-core_seed%</code></li>
<li><code>%multiverse-core_time%</code>（以刻度为单位）</li>
<li><code>%multiverse-core_time_12h%</code></li>
<li><code>%multiverse-core_time_24h%</code></li>
<li><code>%multiverse-core_time_&lt;format&gt;</code>（e.g.<a href="https://www.digitalocean.com/community/tutorials/java-simpledateformat-java-date-format#patterns">格式</a>为<code>HH:mm:ss</code>、<code>hh:mm:ss a</code>）</li>
<li><code>%multiverse-core_type%</code></li>
<li><code>%multiverse-core_weather%</code></li>
</ul>
<div class="admonition info">
<p>如果任何参数（例如世界名称）包含下划线，请将其用双引号引起来。例如：<code>%multiverse-core_playercount_"world_nether"%</code>。</p>
</div>

