---
title: 自定义世界创建
source_url: https://mvplugins.org/core/how-to/customise-world-creation/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 自定义世界创建

<a id="Creating-worlds-with-a-namespaced-key"></a><h2 id="creating-worlds-with-a-namespaced-key">使用命名空间键创建世界</h2>
<p>默认情况下，世界名称是纯字符串，例如 <code>survival</code> 或 <code>my_world</code>。从 v5.7 开始，您还可以提供 <strong>命名空间键</strong>（格式为 <code>namespace:key</code>）作为世界名称，这为世界提供了独立于其文件夹名称的稳定标识符。默认情况下，命名空间为 <code>minecraft</code>，因此在 <code>minecraft</code> 命名空间（e.g.<code>minecraft:survival</code>）下仍支持旧的普通名称作为键。</p>
<div class="highlight"><pre>/mv create myplugin:pvp_arena normal
</pre></div>
<p>任何包含 <code>:</code> 的字符串都被视为命名空间键。命名空间和键均遵循Minecraft的标识符规则（小写字母、数字、<code>_</code>、<code>-</code>、<code>.</code>）。</p>
<div class="admonition note">
<p class="admonition-title">注意事项</p>
<p>只有 Paper 允许创建/导入世界作为自定义命名空间 i.e。它不以 <code>minecraft:</code> 开头</p>
</div>
<a id="Where-is-the-world-folder,-and-what's-the-world-name?"></a><h3 id="where-is-the-world-folder-and-whats-the-world-name">世界文件夹在哪里，世界名称是什么？</h3>
<p>文件夹位置取决于您的服务器软件和 version:</p>
<p><strong>Paper 26.1+</strong> — 所有世界都存储在 <code>&lt;level-name&gt;/dimensions/&lt;namespace&gt;/&lt;key&gt;/</code>.<br/>
例如， <code>myplugin:pvp_arena</code> 在服务器上 <code>level-name=world</code> 生活 at:
<div class="highlight"><pre>world/dimensions/myplugin/pvp_arena/
</pre></div>
原版尺寸遵循相同的 layout:
|命名空间键 |文件夹|
|---|---|
| <code>minecraft:overworld</code> | <code>world/dimensions/minecraft/overworld/</code> |
| <code>minecraft:the_nether</code> | <code>world/dimensions/minecraft/the_nether/</code> |
| <code>minecraft:the_end</code> | <code>world/dimensions/minecraft/the_end/</code> |</p>
<p>至于世界名称，那些具有默认命名空间（i.e.，以<code>minecraft:</code>开头）的将仅保留键的后半部分作为世界名称，就像以前一样。默认世界仍将命名为 <code>&lt;world&gt;</code>、<code>&lt;world&gt;_nether</code> 和 <code>&lt;world&gt;_the_end</code>（按照您的 <code>level-name</code> 命名）。为了确保自定义命名空间键世界不会产生重复的世界名称，Paper 选择通过将 <code>:</code> 替换为 <code>_</code> 来进行格式化。例如，<code>myplugin:pvp_arena</code> 将使用 <code>myplugin_pvp_arena</code> 作为世界名称。这将允许您拥有具有 2 个不同命名空间的 <code>pvp_arena</code> 键。</p>
<hr/>
<p><strong>Spigot / 旧版 Paper</strong> — 世界作为文件夹存储在服务器根目录中。命名空间被完全忽略；仅将关键部分（<code>:</code>之后的部分）用作<strong>文件夹和世界名称</strong>：
|命名空间键 |文件夹|世界名称 |
|---|---|
| <code>myplugin:pvp_arena</code> | <code>pvp_arena/</code> | <code>pvp_arena</code> |
| <code>minecraft:overworld</code> | <code>world/</code> | <code>world</code> |
| <code>minecraft:the_nether</code> | <code>world_nether/</code> | <code>world_nether</code> |
| <code>minecraft:the_end</code> | <code>world_the_end/</code> | <code>world_the_end</code> |</p>
<hr/>
<p>您可以使用 <code>/mv info</code> 或通过 <code>%multiverse-core_key%</code>/<code>%multiverse-core_name%</code> 占位符查找世界的键和名称。</p>
<a id="Creating-a-flat/superflat-world"></a><h2 id="creating-a-flatsuperflat-world">创建一个平坦/超平坦的世界</h2>
<p>创建一个非常基本的平坦世界的命令：<code>/mv create &lt;world-name&gt; normal --world-type flat</code></p>
<div class="admonition note">
<p class="admonition-title">注意事项</p>
<p>请注意，环境必须是 <code>normal</code>。</p>
</div>
<a id="Customizing-superflat-world"></a><h3 id="customizing-superflat-world">定制超平坦世界</h3>
<p>您可以使用 <code>--generator-settings</code> 标志自定义超平坦世界的图层和生物群系。该标志的值为 JSON 字符串，用于定义图层和生物群系。例如，要创建一个包含一层石头、一层草和一层海晶灯的平坦世界，可以使用以下命令：</p>
<div class="highlight"><pre>/mv create flat normal --world-type flat --generator-settings {"layers":[{"block":"stone","height":1},{"block":"grass_block","height":1},{"block":"sea_lantern","height":1}],"biome":"plains"}
</pre></div>
<a id="Creating-a-void-world"></a><h2 id="creating-a-void-world">创造一个虚空世界</h2>
<p>虚空世界是完全空的世界，没有方块或地形（除了单个出生点）。在Minecraft中创建虚空世界主要有两种方法。</p>
<a id="Method-1:-Using-flat-world-with-THE_VOID-biome"></a><a id="Method-1:-Using-flat-world-with-THEVOID-biome"></a><h3 id="method-1-using-flat-world-with-the_void-biome">方法 1：使用 THE_VOID 生物群系的平坦世界</h3>
<p>通过使用介绍的<code>--generator-settings</code>旗帜，您可以用<code>the_void</code>生物群系创建一个平坦的世界。这将创建一个除了 33x33 石头平台之外完全空的世界。您可以使用以下命令来创建一个虚空世界：</p>
<div class="highlight"><pre>/mv create thevoid normal --world-type flat --generator-settings {"layers":[{"block":"air","height":1}],"biome":"the_void","features":true}
</pre></div>
<a id="Method-2:-Using-void-generator-plugin"></a><h3 id="method-2-using-void-generator-plugin">方法2：使用void生成器插件</h3>
<p>首先，安装这个VoiGen生成器plugin: https://www.spigotmc.org/resources/fork-of-voidgen-1-21-3-supported.121721/</p>
<p>创建一个虚空世界如下图所示。有关虚空世界的更多自定义选项，请参阅 https://github.com/NicoNekoDev/VoidGen/wiki/Parameters。
<div class="highlight"><pre>/mv create &lt;worldname&gt; normal --generator VoidGen --world-type flat
</pre></div></p>
<p>如果要导入一个世界，并希望新生成的区块也保持虚空地形：<div class="highlight"><pre>/mv import &lt;worldname&gt; normal --generator VoidGen --world-type flat
</pre></div></p>
<div class="admonition note">
<p class="admonition-title">注意事项</p>
<p>Multiverse 团队不隶属于 void gen 插件。这只是为想要创建虚空世界的用户提供的一个选项。</p>
</div>
<a id="Single-biome-worlds"></a><h2 id="single-biome-worlds">单一生物群系世界</h2>
<p>您可以使用以下方法创建一个具有单一生物群系的世界 <code>--biome</code> 标志。例如，要创建一个只有沙漠生物群系的正常世界，您可以使用以下 command:
<div class="highlight"><pre>/mv import &lt;worldname&gt; normal --biome @single:desert
</pre></div></p>
<p>所有生物群系均可在 这里： https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/block/Biome.html 中找到（请注意，某些生物群系在某些 Minecraft 版本中可能不可用）</p>

