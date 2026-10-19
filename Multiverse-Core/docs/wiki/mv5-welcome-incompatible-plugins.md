---
title: 不兼容的插件
source_url: https://mvplugins.org/mv5/welcome/incompatible-plugins/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 不兼容的插件

<p>Multiverse 5 完全改变了插件的内部结构，因此它与依赖旧 MV4 api 的现有第 3 方插件不兼容。 </p>
<p><em><strong>我们强烈建议您更新插件以使用 <a href="https://mvplugins.org/core/developers/developer-api-starter">新的 MV5 API</a>.</strong></em></p>
<p>但不要害怕！我们创建了一个旧版兼容性插件来简化这种过渡。然而，这只是暂时的，当我们退出 alpha 阶段时，我们强烈鼓励开发人员更新他们的插件以使用更新后的 MV5 的 api。您可以下载兼容性插件这里： </p>
<p>https://modrinth.com/plugin/multiverse-legacy-api </p>
<a id="Tested-working-plugins"></a><h3 id="tested-working-plugins">经过测试的工作插件</h3>
<ul>
<li>留在原地</li>
<li>不和谐SRV</li>
<li>生态</li>
<li>动力图-Multiverse</li>
<li>野蛮死亡宝箱</li>
<li>BentoBox（v3.3.5 或更高版本）</li>
<li>火车车</li>
</ul>
<a id="Not-working-plugins"></a><h3 id="not-working-plugins">插件不工作</h3>
<p>目前还没有关于安装旧版 api 后已知不兼容的任何插件的报告。如果您遇到任何问题，请通过 <a href="https://discord.gg/NZtfKky">不和谐</a> 与我们联系！</p>
<a id="Implemented-v4-API-classes"></a><h3 id="implemented-v4-api-classes">实施了 v4 API 类</h3>
<div class="highlight"><pre>[Multiverse-Core]
- MVPlugin
- Core
- MultiverseWorld
- MVWorldManager
- MVRespawnEvent
- MVWorldDeleteEvent
- AnchorManager
- MVDestination
- DestinationFactory
- MVPlayerTouchedPortalEvent
- MVTeleportEvent
- AnchorManager

[Multiverse-Inventories]
- GameModeChangeShareHandlingEvent
- WorldChangeShareHandlingEvent
- WorldGroupManager
- WorldGroup

[Multiverse-Portals]
- MVPortalEvent
- MVPortal
- PortalManager
- PortalLocation
- MultiverseRegion
</pre></div>

