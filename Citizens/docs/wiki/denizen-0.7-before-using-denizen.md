---
title: Denizen / 0.7 / 使用 Denizen 之前
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Before_Using_Denizen
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5232
---


<a id="top"></a>

# Denizen / 0.7 / 使用 Denizen 之前

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s><div style="font-family:camingodos-web;"></div></s></p>
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">瓦</span>欢迎来到Denizen！伟大的冒险正在等待着，但是让我们先了解一下基础知识。在此页面上您会发现安装 Denizen 的说明、各种文件用途的描述以及其全部内容的简要概述。</p>
</div>
<div class="mw-heading mw-heading3"><h3 id="Getting_Started">入门</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">Denizen 处于测试阶段！预计会有一些错误！如果您遇到问题， <a href="denizen-0.7-in-game-commands.md#Debug_Mode" title="Denizen/0.7/In Game Commands"><code>/denizen debug</code></a> 是你的朋友！我们总是愿意提供帮助 <a class="external text" href="irc://irc.esper.net" rel="nofollow">EsperNET 上的 #denizen-dev</a> 以及。如果您确实遇到除错误命令语法之外的任何错误，请将其报告给 <a class="external text" href="http://www.github.com/aufdemrand/Denizen/issues" rel="nofollow">Denizens 的 Github 问题页面</a>.
<p>Denizen 不是拖放类型的插件。事实上，除非您向 NPCs 分配和定义脚本，否则 Denizen 不会执行任何操作。它是高度可定制的。随着新的 <a class="external text" href="http://scripts.citizensnpcs.com%7CScript" rel="nofollow">存储库</a> 的开发，我们希望会有各种各样的预烘焙脚本您可以轻松下载并自定义到您的服务器，但也许 Denizen 最令人兴奋的部分是编写您自己的脚本的能力。为了编写出色的脚本，您可能需要阅读整个 wiki 页面并跳出框框思考！ IRC 周围总是有人提供帮助和提供建议，但请不要询问基础知识，除非您先在这里咨询过。</p><p>一些 Denizen 命令和要求 <b>REQUIRE</b> 您必须安装其他插件，例如 <a class="external text" href="http://dev.bukkit.org/server-mods/vault/" rel="nofollow">Vault</a>兼容的权限系统和经济系统。如果这些命令涉及金钱或权限，您很可能需要 Vault 才能使用它。我们还准备发布英雄和 mcMMO 的命令/要求包，敬请期待！</p><p>首次使用Denizen最简单的方法是下载<a href="denizen-0.7-start-up-kit.md" title="Denizen/0.7/Start-up kit">启动套件</a>。这包括默认配置文件、示例脚本和示例分配以帮助您入门。仍然建议您尽可能多地阅读 wiki，以正确利用 Denizen 的强大功能和灵活性。</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Down_and_dirty">又脏又低</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>现在，您可能只想了解如何添加自定义内容，对吗？这是一个快速、简单的演练，帮助您启动并运行您的第一个定制 NPC。首先，您应该拥有 <a href="denizen-0.7-start-up-kit.md" title="Denizen/0.7/Start-up kit">启动套件</a>，或者至少有一个现有的 assignments.yml 和 script.yml。这些是您将在本演练中添加到的文件。请记住：这些文件应放置在您的服务器文件夹中，使其类似于 <a href="#top">文件结构</a> 中提到的格式。一切就绪后，启动您的服务器。</p><p><br/>
<b>1:</b> 使用C2命令创建一个NPC，创建一个新的NPC，并分配一个特征。在此示例中我们将使用 Notch。另请参阅：<a href="commands.md" title="Commands">/NPC Commands</a>。</p>
<pre>/npc create Notch --trait denizen</pre>
<p>注意：如果使用现有的 NPC，您也可以使用 <tt>/trait denizen</tt>。</p><p><br/>
<b>2:</b> 为 Notch 创建脚本。另请参阅：<a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Writing_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Writing Scripts (page does not exist)">编写 Denizen 脚本</a>。 <br/>
在 <tt>插件/Denizen/脚本/</tt> 中创建一个名为 <tt>缺口 Cookies.yml</tt> 的新文件。接下来，复制下面小脚本的内容。如果您知道秘密单词，此脚本会向 Notch 发出一个小的随机问候，并附上一个“复活节彩蛋”惊喜。</p>
<pre>'Notch Greeting':
  Type: Interact
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - RANDOM 3
        - CHAT 'I Like Cookies!'
        - CHAT 'MMmm.. cookies are my favorite!'
        - CHAT 'Cocoa and Wheat make me freak!'
      Chat Trigger:
        1:
          Trigger: 'I love /cookie/s!'
          Script: 
          - CHAT 'Me too!'
          - EMOTE 'gives &lt;PLAYER&gt; some cookies.'
          - GIVE COOKIE QTY:6
          - ZAP 2
    2:
      Click Trigger:
        Script:
        - CHAT 'How were the cookies?'
</pre>
<p><br/>
<b>3:</b> 分配一些脚本。另请参阅：<a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Assigning_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Assigning Scripts (page does not exist)">分配 Denizen 脚本</a>。 <br/>
打开您的 assignments.yml。如果不存在，请在 <tt>/plugins/Denizen</tt> 文件夹中创建它。将以下内容插入到您的 YML 文件中。如果 <tt>Denizens:</tt> 不在本文档的顶部，请创建它。</p>
<pre>Denizens:
  # ...
    # ...
  Notch:
    Interact Scripts:
    - 10 Notch Greeting
    Texts:
      No Click Trigger: Stop poking me!
      Denizen Unavailable: Sorry! Busy eating cookies!
      No Chat Trigger: I only understand cookies.
</pre>
<p>这段文字为 Notch 提供了一些针对特定情况的简单消息。它还分配我们刚刚在上一节中编写的 Notch Cookies 脚本。
</p><p><br/>
<b>4:</b> 重新加载 Denizen。另请参阅：<a href="denizen-0.7-in-game-commands.md" title="Denizen/0.7/In Game Commands">Denizen 重新加载</a>。 <br/>
这将确保信息已被获取。首先，在控制台或您的 Minecraft 客户端中，输入 <tt>/denizen reload</tt>。这将重新加载 assignments.yml、config.yml、saves.yml、重新连接脚本并执行一些对象清理等操作。这是检查控制台是否有任何错误的好时机。如果找到，请前往 <a href="denizen-0.7-troubleshooting.md" title="Denizen/0.7/Troubleshooting">故障排查</a>。</p><p><br/>
<b>5:</b> 检查 Denizen NPC 状态。另请参阅：<a href="denizen-0.7-in-game-commands.md#Info-Click" title="Denizen/0.7/In Game Commands">信息点击</a>。 <br/>
信息-通过蹲下并右键点击 Denizen NPC 来点击它。这将输出几页信息，显示 Citizens2 NPC 统计信息、当前 Interact 脚本、触发器状态、书签等。在我们的示例中，Notch 应在 <tt>缺口饼干</tt> 的 Interact Scripts 下有一个条目。</p><p><br/>
<b>6:</b> 点击缺口！表演剧本。就是这么简单！前往Notch并聊天'cookie'以获得超级秘密特别惊喜。</p><p><br/>
<i>Note:</i> 这似乎是最好的时机，如果您使用的任何交互脚本有 'proximity'、'location' 或“损坏触发器”，则必须根据 NPC 打开这些脚本。它们默认处于关闭状态，以保持尽可能高的性能。有关详细信息，请参阅 <a href="denizen-0.7-in-game-commands.md" title="Denizen/0.7/In Game Commands">游戏内命令</a>。</p><p>准备好深入了解了吗？以 <a href="denizen-0.7-interact-scripts.md" title="Denizen/0.7/Interact Scripts">Denizen/0.7/Interact_Scripts</a> 或 <a href="denizen-0.7-activity-scripts.md" title="Denizen/0.7/Activity Scripts">Denizen/0.7/Activity_Scripts</a> 开头</p>
</div>
<p></p>

