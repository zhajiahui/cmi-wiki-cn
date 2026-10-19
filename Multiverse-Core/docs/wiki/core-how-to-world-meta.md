---
title: 世界元数据
source_url: https://mvplugins.org/core/how-to/world-meta/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 世界元数据

<p>世界元数据允许您将任意键值字符串数据附加到任何 Multiverse 世界。它与世界其他配置一起存储在 <code>worlds.yml</code> 中，并且可以通过命令和 <a href="core-reference-placeholders.md">PlaceholderAPI</a> 完全访问。</p>
<p>常见用途包括：
- 用类别或类型标记世界，以便在聊天插件或记分牌中使用
- 存储世界的颜色代码（参见下面的 <a href="#world-colour">世界色彩</a>）
- 跟踪服务器所需的任何非内置世界属性的自定义属性</p>
<a id="Viewing-meta"></a><h2 id="viewing-meta">查看元数据数据</h2>
<p>列出 world: 的所有元数据条目</p>
<div class="highlight"><pre>/mv meta info [world] [--page &lt;page&gt;] [--filter &lt;filter&gt;]
</pre></div>
<ul>
<li><code>[world]</code> — 待检验的世界。默认为您当前的游戏世界。从控制台需要。</li>
<li><code>--page</code> / <code>--filter</code> — 分页和过滤，与其他列表命令相同。</li>
</ul>
<a id="Examples"></a><h3 id="examples">示例</h3>
<ul>
<li><code>/mv meta info</code> — 显示当前世界的元数据</li>
<li><code>/mv meta info survival</code> — 显示名为 <code>survival</code> 的世界的元</li>
</ul>
<a id="Permission"></a><h3 id="permission">权限</h3>
<p><code>multiverse.core.meta.info</code></p>
<a id="Setting-a-meta-value"></a><h2 id="setting-a-meta-value">设置元数据值</h2>
<div class="highlight"><pre>/mv meta modify [world] set &lt;key&gt; &lt;value&gt;
</pre></div>
<ul>
<li><code>[world]</code>——要修改的世界。默认为您当前的游戏世界。</li>
<li><code>&lt;key&gt;</code> — 元数据键。可以是任何不带空格的字符串。</li>
<li><code>&lt;value&gt;</code> — 要存储的值。</li>
</ul>
<a id="Examples"></a><h3 id="examples_1">示例</h3>
<ul>
<li><code>/mv meta modify survival set category pvp</code> — 标签 <code>survival</code> 和 <code>category=pvp</code></li>
<li><code>/mv meta modify lobby set max-players 50</code></li>
</ul>
<a id="Permission"></a><h3 id="permission_1">权限</h3>
<p><code>multiverse.core.meta.modify</code></p>
<a id="Removing-a-meta-value"></a><h2 id="removing-a-meta-value">删除元数据值</h2>
<div class="highlight"><pre>/mv meta modify [world] remove &lt;key&gt;
</pre></div>
<a id="Examples"></a><h3 id="examples_2">示例</h3>
<ul>
<li><code>/mv meta modify survival remove category</code> — 从 <code>survival</code> 中删除 <code>category</code> 键</li>
</ul>
<a id="Permission"></a><h3 id="permission_2">权限</h3>
<p><code>multiverse.core.meta.modify</code></p>
<a id="Using-meta-in-PlaceholderAPI"></a><h2 id="using-meta-in-placeholderapi">在 PlaceholderAPI 中使用元</h2>
<p>可以使用 format: 作为占位符访问世界元数据值</p>
<div class="highlight"><pre>%multiverse-core_meta_&lt;key&gt;%
%multiverse-core_meta_&lt;key&gt;_&lt;world&gt;%
</pre></div>
<p>例如，如果您设置 <code>/mv meta modify survival set category pvp</code>，则可以使用以下命令将其显示在其他位置：</p>
<div class="highlight"><pre>%multiverse-core_meta_category%
</pre></div>
<p>如果键包含下划线（e.g.<code>my_key</code>），则将其按原样写入占位符 - 保留键中的下划线：</p>
<div class="highlight"><pre>%multiverse-core_meta_my_key%
</pre></div>
<div class="admonition note">
<p class="admonition-title">注意事项</p>
<p>如果请求的元数据键在世界中不存在，则占位符返回空字符串（或 <code>null</code>，具体取决于您的 <code>invalid-papi-format-returns-blank</code> 配置设置）。</p>
</div>
<a id="World-colour"></a><h2 id="world-colour">世界色彩</h2>
<p>在Multiverse v4中，世界有一个专用的<code>world-colour</code>属性。这在 v5 中被删除 - 相反，使用 <a href="core-fundamentals-world-properties.md#Alias">别名</a> 属性，它直接支持颜色代码（e.g.<code>&amp;aGreen World</code>）。</p>
<p>如果您需要将世界的颜色代码公开为独立占位符以在其他插件中使用，您可以将其存储为元 value:</p>
<div class="highlight"><pre>/mv meta modify survival set colour &amp;a
</pre></div>
<p>然后在聊天插件或记分牌中引用它 as:</p>
<div class="highlight"><pre>%multiverse-core_meta_colour%
</pre></div>
<a id="Storage"></a><h2 id="storage">存储</h2>
<p>元数据存储在 <code>worlds.yml</code> 中的每个世界条目下：</p>
<div class="highlight"><pre>minecraft:overworld:
  meta:
    category: survival
    colour: "&amp;a"
</pre></div>
<div class="admonition warning">
<p class="admonition-title">直接编辑配置</p>
<p>我们不建议手动编辑 <code>worlds.yml</code> 的 <code>meta</code> 部分。 YAML对缩进和引号敏感，格式错误会导致<code>worlds.yml</code>加载失败，可能会丢失您所有的世界配置。请改用 <code>/mv meta modify</code> 命令 — 它安全且无需重新加载即可立即生效。</p>
<p>如果必须直接编辑文件，请先备份，然后运行 <code>/mv reload</code>。</p>
</div>

