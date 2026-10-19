---
title: Denizen / 0.7
source_url: https://wiki.citizensnpcs.co/Denizen/0.7
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5228
---


<a id="top"></a>

# Denizen / 0.7

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
<p><b>Denizen</b> 是 Citizens 的扩展，允许编写 NPCs 的脚本来处理任务、任务、玩家交互等等！</p><p><b>当前版本：</b> 0.7.6 预发布BETA</p><p><b>Developers:</b> aufdemrand</p><p><b>Source:</b> <a class="external text" href="https://github.com/aufdemrand/Denizen" rel="nofollow">吉图布</a>
</p><p><b>开发构建：</b> <a class="external text" href="http://jenkins.citizensnpcs.com/job/Denizen/" rel="nofollow">詹金斯</a>
</p><p><b>最新开发版本：</b> <a class="external text" href="http://ci.citizensnpcs.com/job/Denizen/lastSuccessfulBuild/" rel="nofollow">2.0.2</a>
</p><p><b>支持tickets:</b> <a class="external text" href="http://github.com/aufdemrand/Denizen/issues/" rel="nofollow">门票于吉图布</a>，但请先阅读本文档全文。</p><p><b>Donate:</b> 在Denizen上投入了大量的工时。您的捐款将为该项目增添很多色彩，我们随时欢迎您的捐款！您的捐款可能会帮助改造我的房子并养活我的孩子。 :) 
<a class="external text" href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=jeremy%2eschroeder%40gmail%2ecom&amp;lc=US¤cy_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted" rel="nofollow">捐赠给 aufdemrand</a> 不要忘记也向 Citizens2 项目捐款，因为没有它，这一切都是不可能的！</p><p><b>谢谢：</b> 很多人都挺身而出帮助Denizen，太棒了！特别感谢所有进行过 Beta 测试的人，特别感谢这些人：fullwall、AgentKid、aPunch、NeonMaster、Instinx、tenowg、groggluebutt、Wreyth、jrbudda、spidi，这样的名单还可以继续列下去！</p><p><b>CitizensUI:</b> 对于 GUI 界面，查看 jrbudda 的 <a href="citizensui.md" title="CitizensUI">CitizensUI</a>，它为 Citizens NPCs 以及管理脚本和其他 NPC 类型提供了接口。
<br/></p>
</div></td></tr></tbody></table>
</div>
</td></tr></tbody></table>
<p><a href="https://wiki.citizensnpcs.co/File:Denizen-Logo-Large.png"><img alt="" src="assets/294c24060a9e-Denizen-Logo-Large.png"/></a></p>
<p>加载视频</p>
<p>YouTube</p>
<p>YouTube 可能会收集个人数据。 <a href="https://www.youtube.com/howyoutubeworks/user-settings/privacy/">隐私政策</a></p>
<p>继续
解雇</p>
<p>Denizen 的一小部分。</p>
<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>这是 Denizen 0.7.6 的旧 Wiki！此处找到的信息不适用于 Denizen 的更高版本。
~~Denizen 是将 <a href="http://en.wikipedia.org/wiki/MUD">MUD风格</a> RPG Citizens 添加到服务器的好方法。 Denizen NPCs 使用带有步骤和事件的迷你脚本与玩家和世界进行交互。想象互动看门人、魔法巫师、经验训练师、银行家、会说话的城镇居民等等！它们可以以数千种不同的方式使用，从教程、探索到管理……您的想象力几乎是极限！虽然 Denizen 使用脚本，不要与 <a href="scripting.md" title="Scripting">Citizens2 核心脚本</a> 混淆，后者利用 JavaScript 和其他主要脚本语言来实现目标。相反，Denizen 使用自己的 YML“脚本语言”，该语言旨在轻松手动阅读和编辑。~~</p>
<p><s></s></p>
<div style="padding:20px; font-family:camingodos-web; font-size:110%; background-color:#EEDDEE; border-style:dotted; border-width:1px; width:55%; font-weight:500;">如果您来自 Denizen 0.6，我们已尝试编译一个 <a href="denizen-0.7-migration.md" title="Denizen/0.7/Migration">帮助迁移的列表</a> 适合需要简要了解需要更改哪些内容才能兼容的升级用户。
</div>
<p></p>
<p><s><div style="padding:10px; font-family:camingodos-web; font-size:110%;"></div></s></p>
<div class="mw-heading mw-heading3"><h3 id="How_it_works">它是如何运作的</h3></div>
<p>Denizen 是 Citizens2 的扩展，为 NPCs 和具有其中一些主要 features: 的玩家添加了令人难以置信的交互性和自动化
</p>
<ul><li><b>脚本引擎</b> 以有序且可预测的方式执行并发送所有要执行的命令；这是Denizen的主干。目前有 3 个队列，1 个用于玩家，1 个用于 Denizen，1 个用于任务。外面没什么可看的，这是Denizen的互通，但请放心，这是幕后的高性能机器！</li>
<li><b>交互脚本</b> 是 Denizen 的核心，允许玩家和 NPCs 相互交互以及与世界交互。这些是高度可定制的，具有 20 多种需求类型、40 多种脚本命令以及数千种不同的组合使用方式。 Denizen 脚本引擎还允许命令通过脚本流命令等帮助控制 Denizen 的其余部分。</li>
<li><b>活动脚本</b> 令人兴奋。想象一下约翰尼·阿普尔塞德（Johnny Appleseed）独自植树，或者简单的村民四处闲逛并进行社交活动。当然，活动可以与 Denizen 的其他功能和特性配合使用，允许以数百种方式使用活动来为您的世界增添自动化和活力。</li>
<li><b>活动安排</b> 将活动脚本向前推进了一步，允许 Denizen NPCs 根据 Minecraft 日制定每日计划，从而允许在一天中的不同时间执行某些功能。这也使得某些脚本命令能够被执行和执行。</li>
<li><b>任务脚本</b> 是可以通过多种不同方式执行的简单脚本。这些可以与活动脚本和交互脚本一起使用，但使用它们的最强大方法可能是允许您的插件使用它们（如果您是开发人员），或者使用其他也能够运行 Denizen 任务脚本的插件。</li>
<li><b>听众</b> 目前处于“实验阶段”，但已经可以像其他一样控制 Minecraft 和 bukkit 事件。如果您熟悉 C1 任务 NPC，这已经允许脚本跟踪并分配 'quest-like' 目标，例如“杀死任务”。但是，尽管许多任务插件仅限于此功能，但 Denizen 当然允许您额外使用此功能并与插件的其余部分一起使用，为极其动态和复杂的“任务脚本”腾出空间。</li>
<li><b>标志系统</b>是Denizen动态的关键。 Denizen 中已实施了复杂但易于学习的“标志/变量”系统，以帮助跟踪事件、物品、数字、玩家等。新的旗帜系统每天都在变得越来越强大......这是一个精彩脚本的关键，肯定有一两个旗帜。</li>
<li><b>可扩展的命令/要求/活动等等</b> 使得只需很少的 Java 知识即可轻松添加到 Denizen。这也使得用户可以非常轻松地通过脚本命令使用您的插件。 Denizen 也有 API 事件可供使用。</li>
<li><b>Denizen 调试器'</b> 是一种非常友好且信息丰富的测试脚本和交互的方式。命令、事件和交互都以易于阅读的格式记录，以显示脚本及其周围环境的确切进度。不用再猜测了！头痛少了！</li></ul>
<p><br/>
看起来势不可挡？停止！从小事做起！ Denizen 很简单，Denizen 很简单。但。 Denizen 很硬，Denizen 很复杂。简而言之：Denizen 就是您制作的！我们的建议？从小事做起，并以你所拥有的为基础。阅读 wiki 文章、观看 YouTube 视频、测试我们的脚本并测试一些示例脚本！在不知不觉中，您将成为 Denizen 超级用户，醉心于权力，就像我们一样！</p>
<p></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; border-style:none; font-size:110%; font-weight:500;width:100%;border-width:0px;"></div></s></p>
<div class="mw-heading mw-heading1"><h1 id="Denizen">Denizen</h1></div>
<p>如果您是 Denizen 的新手，请参阅 <a href="denizen-0.7-before-using-denizen.md" title="Denizen/0.7/Before Using Denizen">使用 Denizen 之前：入门</a>。 
<br/>如果您在运行脚本时遇到问题，请参阅 <a href="denizen-0.7-troubleshooting.md" title="Denizen/0.7/Troubleshooting">故障排查</a>.<br/>
如果您着迷，我们建议您按顺序阅读所有部分并尝试一些示例脚本！</p>
<p></p>
<p><s><table class="wikitable" style="text-align: left; border-color:white; border-style:none; vertical-align: text-top; background-color:white;"></table></s></p>
<tbody><tr style="vertical-align:top;">
<td style="width: 60%;">
<div style="vertical-align: text-top; padding:16px; border-style:none; border-color:white;font-family:camingodos-web; font-size:110%; font-weight:500;width:85%;border-width:0px;">
<div class="mw-heading mw-heading3"><h3 id="Table_of_Contents">目录</h3></div>
<ol><li><a href="denizen-0.7-before-using-denizen.md" title="Denizen/0.7/Before Using Denizen">使用 Denizen 之前和开始使用</a>
<ul><li><a href="denizen-0.7-start-up-kit.md" title="Denizen/0.7/Start-up kit">启动套件</a></li></ul></li>
<li><a href="denizen-0.7-troubleshooting.md" title="Denizen/0.7/Troubleshooting">Denizen 故障排除</a></li>
<li><a href="denizen-0.7-file-structure.md" title="Denizen/0.7/File Structure">文件结构</a>
<ul><li><a href="denizen-0.7-config.yml.md" title="Denizen/0.7/config.yml">默认config.yml</a></li></ul></li>
<li><a href="denizen-0.7-in-game-commands.md" title="Denizen/0.7/In Game Commands">在游戏和控制台命令中</a></li>
<li>编写脚本
<ul><li><a href="denizen-0.7-interact-scripts.md" title="Denizen/0.7/Interact Scripts">交互脚本简介</a>
<ul><li><a href="denizen-0.7-interact-scripts-triggers.md" title="Denizen/0.7/Interact Scripts/Triggers">互动触发器</a></li>
<li><a href="denizen-0.7-interact-scripts-interact-requirements.md" title="Denizen/0.7/Interact Scripts/Interact Requirements">交互脚本要求</a></li>
<li><a href="denizen-0.7-interact-scripts-commands.md" title="Denizen/0.7/Interact Scripts/Commands">脚本命令</a></li></ul></li>
<li><a href="denizen-0.7-task-scripts.md" title="Denizen/0.7/Task Scripts">任务脚本和任务队列</a></li>
<li><a href="denizen-0.7-activity-scripts.md" title="Denizen/0.7/Activity Scripts">活动脚本和调度程序</a>
<ul><li><a href="denizen-0.7-activity-scripts-activities.md" title="Denizen/0.7/Activity Scripts/Activities">活动和目标</a></li></ul></li></ul></li>
<li><a href="denizen-0.7-assignments.md" title="Denizen/0.7/Assignments">分配脚本</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Flags&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Flags (page does not exist)">Denizen 标志系统</a></li>
<li><a href="denizen-0.7-replaceables.md" title="Denizen/0.7/Replaceables">可更换的数据标签</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Listeners&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Listeners (page does not exist)">Denizen 监听器和事件</a></li>
<li>示例
<ul><li><a href="denizen-0.7-example-scripts-beginner-scripts.md" title="Denizen/0.7/Example Scripts/Beginner Scripts">入门脚本</a></li>
<li><a href="denizen-0.7-example-scripts-advanced-scripts.md" title="Denizen/0.7/Example Scripts/Advanced Scripts">高级脚本</a></li>
<li><a href="sentry-sentry-and-denizen.md" title="Sentry/Sentry and Denizen">Denizen 和 Sentry</a></li>
<li><a class="mw-redirect" href="sentry-builder-and-denizen.md" title="Sentry/Builder and Denizen">Denizen 和 Builder</a></li></ul></li>
<li>扩展 Denizen
<ul><li><a href="denizen-0.7-interact-scritps-custom-commands.md" title="Denizen/0.7/Interact Scritps/Custom Commands">扩展自定义命令</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Interact_Scripts/Custom_Requirements&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Interact Scripts/Custom Requirements (page does not exist)">扩展定制要求</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Interact_Scripts/Custom_Triggers&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Interact Scripts/Custom Triggers (page does not exist)">扩展自定义触发器</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Activity_Scripts/Custom_Activities&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Activity Scripts/Custom Activities (page does not exist)">扩展定制活动</a></li>
<li><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Activity_Scripts/Event_API&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Activity Scripts/Event API (page does not exist)">利用 Denizen 事件 API</a></li></ul></li>
<li>附加内容
<ul><li><a href="denizen-0.7-bonus-content-pictures.md" title="Denizen/0.7/Bonus Content/Pictures">Denizen 奖金图片</a></li></ul></li></ol>
</div>
</td>
<td style="width: 40%;">
<div style="padding:16px; vertical-align: text-top;border-color:white; border-style:none; font-family:camingodos-web; font-size:110%; font-weight:500;width:95%;border-width:0px;">
<div class="mw-heading mw-heading3"><h3 id="Sample_Scripts">示例脚本</h3></div>
<p><a href="denizen-0.7-example-scripts-beginner-scripts.md#Denizen_Basics" title="Denizen/0.7/Example Scripts/Beginner Scripts">Denizen 基础知识</a>
</p>
<ul><li><a href="denizen-0.7-example-scripts-beginner-scripts.md#Denizen_Basics" title="Denizen/0.7/Example Scripts/Beginner Scripts">点击和损坏触发器</a></li>
<li><a href="denizen-0.7-example-scripts-beginner-scripts.md#Denizen_Basics" title="Denizen/0.7/Example Scripts/Beginner Scripts">聊天和接近触发器</a></li></ul>
<p><a href="denizen-0.7-example-scripts-beginner-scripts.md#Simple,_random_conversations" title="Denizen/0.7/Example Scripts/Beginner Scripts">简单、随意的对话</a>
</p>
<ul><li><a href="denizen-0.7-example-scripts-beginner-scripts.md#A_conversation_with_RANDOM" title="Denizen/0.7/Example Scripts/Beginner Scripts">与随机的对话</a></li>
<li><a href="denizen-0.7-example-scripts-beginner-scripts.md#A_conversation_with_ZAP_RANDOM" title="Denizen/0.7/Example Scripts/Beginner Scripts">与 ZAP RANDOM 的对话</a></li>
<li><a href="denizen-0.7-example-scripts-beginner-scripts.md" title="Denizen/0.7/Example Scripts/Beginner Scripts">服务器规则</a></li>
<li><a href="denizen-0.7-example-scripts-beginner-scripts.md" title="Denizen/0.7/Example Scripts/Beginner Scripts">简单的银行柜员</a></li>
<li><a href="denizen-0.7-example-scripts-beginner-scripts.md" title="Denizen/0.7/Example Scripts/Beginner Scripts">高级银行柜员</a></li></ul>
</div>
</td>
<td style="width: 20%;">
<div style="padding:16px; vertical-align: text-top;border-color:white; border-style:none; font-family:camingodos-web; font-size:110%; font-weight:500;width:95%;">
<div class="mw-heading mw-heading3"><h3 id="Index">索引</h3></div>
<p>如果您在运行脚本时遇到问题，请参阅 <a href="denizen-0.7-troubleshooting.md" title="Denizen/0.7/Troubleshooting">Denizen/故障排除</a>。</p>
</div>
</td></tr></tbody>
<p></p>
<p><s><div class="mw-heading mw-heading3"><h3 id="Change_Log">变更日志</h3></div></s></p>
<p><s><div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;"></div></s></p>
<p>这就是改变的地方！
</p>
<p><br/>
<b>0.7.5 BETA 版本 #455</b>
</p>
<ul><li><span style="background: white; color: red"><b>新！</b></span> OWNER 要求将需要 NPC 交互的所有权。可用于只有所有者才能访问的“命令界面”。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 潜行要求要求玩家在点击时蹲下。小心与信息点击操作的冲突！可以在配置中禁用信息点击。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 队列时间标志替换可以让您在脚本条目中动态使用标志数据。例如： - 给予 &lt;FLAG:ExampleItemFlag&gt; 数量：&lt;FLAG:ExampleQtyFlag&gt;</li></ul>
<ul><li><span style="background: white; color: red"><b>实验性的！</b></span> Denizen NPCs 现在有自己的命令队列和任务活动。这允许 NPC 使用活动调度程序在一天中的特定时间执行任务。</li></ul>
<ul><li><span style="background: white; color: red"><b>实验性的！</b></span> LISTEN 命令已实现，KILL 类型已实现。 'Quester' 归还。更多类型即将推出。用法示例： - LISTEN KILL ID:UniqueId TYPE:ENTITY NAME:ZOMBIE QTY:5 SCRIPT:Finish它将要求玩家杀死 5 个僵尸。完成后，它将运行任务脚本 'FinishIt'。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 使用 &lt;*&gt; 在 EXECUTE 或对话命令中使用聊天触发文本。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 在FLAG命令中使用&lt;*&gt;来记住玩家输入。用法示例： - FLAG PLAYER_RESPONSE:&lt;*&gt;</li></ul>
<p><br/>
<b>0.7.5 BETA 版本 #440：</b>
</p>
<ul><li><span style="background: white; color: red"><b>新！</b></span> API 活动让Denizen的扩展比以往更加强大！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> RUNTASK/CANCELTASK 允许设置和取消延迟任务。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> HOLD命令可以改变Denizen NPC正在挥舞的东西。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 可替换数据，用于动态地将标志放入文本中！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> ISLIQUID 要求可以感测块书签是固体还是液体。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> IF 命令可以评估 FLAG 并运行 TASK 脚本。</li></ul>
<p><br/>
<b>0.7 BETA 版本 #125 - #280：</b>
</p>
<ul><li><span style="background: white; color: red"><b>更新了！</b></span> bug 更少！我们仍处于测试阶段，但已经进行了一些主要的代码清理！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 触发器、命令、要求和活动现在可由插件程序员扩展。参见：<a class="external text" href="http://wiki.citizensnpcs.net/Custom_Denizen_Commands" rel="nofollow">Citizens2 Wiki 上的自定义 Denizen 命令</a>。文档即将推出！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">调试模式</a>会让您看到交互和脚本执行的逻辑，帮助您比以往更快地发现脚本中的问题。我正在努力使其尽可能信息丰富且简洁，以帮助您测试脚本并获得有关行为的良好反馈。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">信息点击</a> 让您只需蹲下并点击即可查看 Denizen 统计数据和详细信息，例如脚本分配、触发器状态、活动计划和相关书签。需要 OP.. 使用这个！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 当玩家靠近时，<a href="#top">接近触发器</a> 可以触发脚本。我在之前的测试版中获得最多请求的触发器类型。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 当玩家走过位置书签时，<a href="#top">位置触发器</a> 可以触发脚本。这有点像“玩家任务位置”，但更好！ :)</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">伤害触发</a> 将左键和右键点击分开，以更好地控制交互。期待与之配套的一套全新命令！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/Assignments&amp;action=edit&amp;redlink=1" title="Denizen/Assignments (page does not exist)">脚本“覆盖”分配</a> 模式是一种全新的脚本分配方式。使用多个脚本时减少复制/粘贴，更不用说更多控制了！如果您是高级脚本用户，那么这就是为您准备的！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">宣布命令</a>可以进行全球服务器公告。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">随机命令</a> 会将命令执行留给机会。鸭鸭鹅。</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">提示命令</a> 将提示玩家当前步骤和脚本可接受的聊天触发器。语言支持即将推出！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">标志命令</a> 允许您在玩家上设置 'flags' 以存储进度、重要信息或可与 FLAG 要求一起使用的其他变量。这是巨大的！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">标志要求</a> 可能需要设置特殊标志和值才能符合脚本的条件。再说一次，这是巨大的！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">供电要求</a>可以检查块书签是否具有红石能力。好主意，本能！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> 活动引擎已经实现，这将允许您的 Denizen 自己做事情。这个概念还有很多内容，但您可以尝试一下全新的 WANDER 活动。这东西很酷，而且可以定制！</li></ul>
<ul><li><span style="background: white; color: red"><b>新！</b></span> <a href="#top">游戏内命令</a> 现在可让您轻松管理触发器、书签和调试信息。</li></ul>
<ul><li><span style="background: white; color: red"><b>更新了！</b></span> 几乎每个现有命令的扩展/统一命令语法。一旦克服了升级的痛苦，您就会对新功能大吃一惊！</li></ul>
<p><br/>
您可以在完整的 <a class="external text" href="https://github.com/aufdemrand/Denizen/commits/master" rel="nofollow">Denizen 变更日志</a> 中查看更多信息。</p>
<p></p>

