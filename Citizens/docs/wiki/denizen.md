---
title: Denizen
source_url: https://wiki.citizensnpcs.co/Denizen
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5220
---


<a id="top"></a>

# Denizen

<table cellpadding="0" cellspacing="3" style="border: 0; background-color: #ffffff" width="275">
<tbody><tr>
<td style="width: 275; vertical-align: top; border:1px solid #ccc; background-color: #ffffff">
<div style="background-color:#aaa; font-size:1px; height:8px; border-bottom:1px solid #ccc;"></div>
<div style="float:right; margin:8px; margin-top:5px"></div>
<div style="padding:0.5em 0.3em 0.3em 0.3em; margin:0; text-indent:0.1em; font-weight: bold; border-bottom:1px solid #aaaaaa;"><b> </b></div>
<div style="font-size:100%; padding:3px">
<table cellpadding="0" cellspacing="3" width="100%">
<tbody><tr>
<td align="left" valign="top" width="100%">
<figure class="mw-default-size mw-halign-center" typeof="mw:File"><a class="mw-file-description" href="https://wiki.citizensnpcs.co/File:Denizen.png"><img class="mw-file-element" decoding="async" height="88" src="assets/2d980f38bc28-Denizen.png" width="296"/></a>&lt;figcaption&gt;</figure>
<div class="padded" style="padding: 19px; font-family:camingodos-web; font-size:110%;">
<p><b>Denizen</b> 是 Citizens 的扩展，允许编写 NPCs 的脚本来处理任务、任务、玩家交互等等！它作为一个全功能的 Minecraft 服务器脚本系统运行！</p><p><b>当前 version:</b> 1.x.x 发布</p><p><b>原创者：</b> aufdemrand</p><p><b>开发主管：</b> mcmonkey
</p><p><b>上一页 developers:</b> 大卫·塞纳特、Jeebiss、Morphan1、Xenmai、Mergu</p><p><b>Source:</b> <a class="external text" href="https://github.com/DenizenScript/Denizen-For-Bukkit" rel="nofollow">吉图布</a>
</p><p><b>Spigot 发布：</b> <a class="external text" href="https://www.spigotmc.org/resources/denizen.21039/" rel="nofollow">Spigot</a>
</p><p><b>最新发布build:</b> <a class="external text" href="http://ci.citizensnpcs.co/view/All/job/Denizen/" rel="nofollow">1.x.x构建</a>
</p><p><b>最新开发build:</b> <a class="external text" href="http://ci.citizensnpcs.co/view/All/job/Denizen_Developmental/" rel="nofollow">1.x.x开发构建</a>
</p><p><b>Citizens build:</b> <a class="external text" href="http://ci.citizensnpcs.co/job/Citizens2/" rel="nofollow">2.x.x</a>
</p><p><b>支持tickets:</b> <a class="external text" href="http://github.com/DenizenScript/Denizen-For-Bukkit/issues/" rel="nofollow">门票于吉图布</a>
</p><p><b>Discord:</b> <a class="external text" href="https://discord.gg/Q6pZGSR" rel="nofollow">Denizen不和谐</a>
</p><p><b>感谢you:</b> 很多人都站出来帮忙解决Denizen，太棒了！特别感谢所有进行过 Beta 测试的人，并对这些人表示衷心的感谢：fullwall、AgentKid、aPunch、Instinx、tenowg、groggluebutt、Wreyth、jrbudda、spidi，...这个名单还可以继续下去！
<br/></p>
</div></td></tr></tbody></table>
</div>
</td></tr></tbody></table>
<p><a href="https://wiki.citizensnpcs.co/File:Denizen-Logo-Large.png"><img alt="" src="assets/294c24060a9e-Denizen-Logo-Large.png"/></a></p>
<p>~~这个Wiki应该算是Denizen的快速参考指南/学习工具。~~</p>
<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>~~Denizen 是一个强大的引擎，可以通过脚本编写自己的插件。这也是将复杂的交互式角色扮演 NPCs 添加到服务器的好方法。 Denizen NPCs 使用带有步骤和事件的脚本与玩家和世界进行交互。想象一下互动的看门人、神奇的巫师、经验培训师、银行家、会说话的城镇居民等等！它们可以以数千种不同的方式使用，从教程、探索到管理……您的想象力几乎是极限！ Denizen 使用自己的基于 YAML 的脚本语言，旨在轻松手动阅读和编辑~~</p>
<p><s></s></p>
<div class="mw-heading mw-heading3"><h3 id="Table_of_Contents">目录</h3></div>
<ol><li><a href="denizen-introduction.md" title="Denizen/Introduction">介绍</a></li>
<li><a href="denizen-types-of-scripts.md" title="Denizen/Types of Scripts">脚本类型</a></li>
<li><a href="denizen-triggers.md" title="Denizen/Triggers">NPC 交互脚本触发器</a></li>
<li><a href="denizen-commands.md" title="Denizen/Commands">命令</a></li>
<li><a href="denizen-replaceable-tags.md" title="Denizen/Replaceable Tags">可替换标签</a></li>
<li><a href="denizen-additional-traits.md" title="Denizen/Additional Traits">附加特征</a></li>
<li><a href="denizen-script-samples.md" title="Denizen/Script Samples">脚本示例</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Other&amp;action=edit&amp;redlink=1" title="Denizen/Other (page does not exist)">其他页面</a></li></ol>
<p><br/>
</p>
<p></p>
<p><s></s></p>
<div class="mw-heading mw-heading3"><h3 id="How_it_works">它是如何运作的</h3></div>
<p>Denizen 是 Citizens2 的扩展，为 NPCs 和具有其中一些主要 features: 的玩家添加了令人难以置信的交互性和自动化
</p>
<ul><li><b>脚本引擎</b> 以有序且可预测的方式执行并发送所有要执行的命令；这是Denizen的主干。外面没什么可看的，这是Denizen的互通，但请放心，这是幕后的高性能机器！</li>
<li><b>分配和交互脚本</b> 是 Denizen 的核心，允许玩家和 NPCs 相互交互以及与世界交互。这些是高度可定制的，具有 20 多种需求类型、90 多种脚本命令以及数千种不同的组合使用方式。 Denizen 脚本引擎还允许命令通过脚本流命令等帮助控制 Denizen 的其余部分。</li>
<li><b>任务脚本</b> 是可以通过多种不同方式执行的简单脚本。这些可以与任何其他脚本类型一起使用，但使用它们的最强大方法可能是允许您的插件使用它们（如果您是开发人员），或者使用其他也能够运行 Denizen 任务脚本的插件。</li>
<li><b>世界脚本</b> 是当世界各地发生随机事件时调用 Denizen 命令的脚本 - 任何事情，甚至是玩家挖掘一个区块，以及一个单独的脚本让他们捡起掉落的物品！借助世界脚本的力量，熟练的用户可以只使用 Denizen 脚本来制作整个服务器插件！</li>
<li><b>听众</b> 目前处于“实验阶段”，但已经可以像其他一样控制 Minecraft 和 bukkit 事件。如果您熟悉 C1 任务 NPC，这已经允许脚本跟踪并分配 'quest-like' 目标，例如“杀死任务”。但是，尽管许多任务插件仅限于此功能，但 Denizen 当然允许您额外使用此功能并与插件的其余部分一起使用，为极其动态和复杂的“任务脚本”腾出空间。</li>
<li><b>标志系统</b>是Denizen动态的关键。 Denizen 中已实施了复杂但易于学习的“标志/变量”系统，以帮助跟踪事件、物品、数字、玩家等。新的旗帜系统每天都在变得更加强大……这是一个精彩脚本的关键，肯定有一两个旗帜。</li>
<li><b>可扩展的命令/要求/活动等等</b> 使得只需很少的 Java 知识即可轻松添加到 Denizen。这也使得用户可以非常轻松地通过脚本命令使用您的插件。 Denizen 也有 API 事件可供使用。</li>
<li><b>Denizen 调试器</b> 是一种非常友好且信息丰富的测试脚本和交互的方式。命令、事件和交互都以易于阅读的格式记录，以显示脚本及其周围环境的确切进度。不用再猜测了！头痛少了！</li>
<li><b>关于 YML 的说明</b> 大多数情况下，当服主使用 YML 时，他们会编辑现有配置。在Denizen中，需要经常“添加”附加内容。请注意间距，切勿使用制表符。您可以使用 <a class="external text" href="https://discord.gg/Q6pZGSR" rel="nofollow">我们的不和谐小组</a> 中的 ChatBot 来检查您的 YML 文件，也可以使用 <a class="external text" href="http://yaml-online-parser.appspot.com/" rel="nofollow">这个在线 YAML 解析器。</a>（ChatBot 还可以做更多事情！只需进入 <a class="external text" href="https://discord.gg/Q6pZGSR" rel="nofollow">我们的不和谐小组</a> 并输入 <b>！帮助</b>）</li>
<li><b>关于 YAML 的附加说明</b> Denizen不再使用纯粹的YAML，而是使用自己的自定义解析代码。可用的 YAML 解析器并不完美，只有上面提到的 IRC 上的 ChatBot 目前有 <b>!d脚本</b> 检查器。</li></ul>
<p><br/>
</p>
<p></p>
<p>~~看起来很厉害吗？停下来！从小事做起！ Denizen 很容易，Denizen 很简单。但是。 Denizen 很难，Denizen 很复杂。只需 put: Denizen 就是您制作的！我们的建议？从小事做起，并以你所拥有的为基础。阅读 wiki 文章、观看 YouTube 视频、测试我们的脚本并测试一些示例脚本！不知不觉中，你就会成为 Denizen 的超级用户，为权力所陶醉，就像我们一样！~~</p>
<p>（旧版 0.7 wiki 找到 <a href="denizen-0.7.md">这里</a>）</p>

