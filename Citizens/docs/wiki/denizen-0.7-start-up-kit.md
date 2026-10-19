---
title: Denizen / 0.7 / 入门套件
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Start-up_kit
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5377
---


<a id="top"></a>

# Denizen / 0.7 / 入门套件

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>默认情况下，Denizen 是全新安装的。一种简单的启动方法是安装启动套件，如此处所述。您可能需要首先查看 <a href="denizen-0.7-before-using-denizen.md#Down_and_dirty" title="Denizen/0.7/Before Using Denizen">入门：低落和肮脏</a> 部分的分步操作，该部分逐步安装示例脚本和作业。该入门工具包尝试更详细地介绍一些预加载的内容。</p>
<a id="Download_the_Kit"></a><h3 id="download-the-kit">下载套件</h3>
<p>该启动项目包含快速使用 Denizen 所需的一切。在 zip 文件中，您将找到一个名为“Denizen”的文件夹。将此文件夹提取到您的 /plugins/ 目录。确保您安装了最新的 Denizen jar，然后启动服务器或调用</p>
<div class="highlight"><pre>/denizen reload
</pre></div>
<p>套件 contains:</p>
<ul>
<li>预配置的 <a href="denizen-0.7-config.yml.md" title="Denizen/0.7/config.yml">config.yml</a></li>
<li>用于 2 个 NPCs（Steve 和 Jill）的预配置 assignments.yml</li>
<li>包含 2 个交互脚本的文件 (Steve Scripts.yml)</li>
<li>包含 2 个活动脚本的文件（活动 Scripts.yml）</li>
</ul>
<a id="Download"></a><h2 id="download">下载</h2>
<p><strong><a href="https://github.com/downloads/jrbudda/Denizen/Start-up%20Kit%200.74.zip">在此下载</a></strong></p>
<a id="How_to_use"></a><h2 id="how-to-use">如何使用</h2>
<p>该套件定义了 2 NPCs 的分配。一位名叫“史蒂夫”，一位名叫“吉尔”。
要创建 NPC，请使用 /npc create 命令。</p>
<div class="highlight"><pre>/npc create Steve --trait denizen
</pre></div>
<p>史蒂夫现在准备出发了。同样，让吉尔：</p>
<div class="highlight"><pre> /npc create Jill --trait denizen
</pre></div>
<p>分配是按名称完成的，因此这些居民现在功能齐全。要进行测试，请致电 /denizen info。您应该看到 assignments.yml 中定义的分配的脚本和活动。</p>
<p>要开始学习，请在记事本 ++ 等优秀文本编辑器中打开脚本或作业文件，请参阅 <a href="yaml.md" title="YAML">YAML</a>
这些文件带有注释以帮助您入门。</p>

