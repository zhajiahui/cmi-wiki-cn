---
title: Denizen / 0.7 / 文件结构
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/File_Structure
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5235
---


<a id="top"></a>

# Denizen / 0.7 / 文件结构

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://one.denizenscript.com/denizen/cmds/">元文档</a>。</p>
<p>如果您想要完整的教程来帮助您进行设置，请查看 youtube 上的 <a href="https://one.denizenscript.com/denizen/cmds/denizen/vids">教程视频</a> 或 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p><s></s></p>
<div style="float:right;margin-left:2.0em; padding:10px; padding-bottom:20px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-20px; margin-left:-10px;">F</span>ile 中的 Denizen 结构很重要，因为它需要使用几个不同的 YML 文件才能正常运行，所以让我们首先回顾一下文件结构。有关每个文件的更多详细信息，请参阅下文。本节可能看起来很臃肿，但请阅读它以更好地理解文件结构，因为您将经常使用它们！</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="denizen.jar">denizen.jar</h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">我们收到了一些关于 Denizen JAR 文件放置位置的问题，特别是来自 Citizens 1.2 的前用户，其中 Citizens 类型位于一个特殊文件夹中。 Citizens2 或 Denizen 的情况并非如此。它应该像任何其他 bukkit 插件一样对待，并放置在您的 craftbukkit/plugins/ 文件夹中。请注意，虽然很多插件会自动生成一个文件夹来配合它，但 Denizen 不会，这应该手动创建并填充，或者通过复制 <a href="denizen-0.7-start-up-kit.md" title="Denizen/0.7/Start-up kit">启动套件</a> 带有示例 .yml 配置文件和脚本。
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="config.yml">config.yml</h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<figure class="mw-halign-right" typeof="mw:File"><a class="mw-file-description" href="https://wiki.citizensnpcs.co/File:Figure_1_-_Denizen_file_structure.png" title="Denizen File Structure"><img alt="Denizen File Structure" class="mw-file-element" decoding="async" height="331" src="assets/58c77bc5a9e6-Figure_1_-_Denizen_file_structure.png" width="450"/></a>&lt;figcaption&gt;Denizen 文件结构</figure>
<p>Denizen config.yml 包含用于更改 Denizen 的库存行为和外观的节点。您可以使用 config.yml 覆盖默认值。 
</p><p>使用 <tt>/denizen reload</tt> 可以随时将该文件从磁盘重新加载到 Denizen 内存。 config.yml 中的某些更改可能需要重新启动服务器。这包括 <tt>交互延迟时间</tt>，但不限于该配置节点。</p><p>有关所有可用选项的库存副本和说明，请参阅：<a href="denizen-0.7-config.yml.md" title="Denizen/0.7/config.yml">Denizen/0.7/config.yml</a>。</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="assignments.yml">assignments.yml</h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">您可以在此 YML 中定义 Denizen NPCs 的所有选项和信息。本文档将对此进行进一步解释，但此文件中最常见的信息是 [交互脚本分配]、[活动脚本计划] 和 [自定义交互文本]。
<p>可以随时使用 <code>/denizen reload</code> 将该文件从磁盘重新加载到 Denizen 内存中</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="saves.yml"><span style="background: white; color: red">saves.yml</span></h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">该文件不适合手动编辑，Denizen 将根据需要自动创建并填充该文件。它存储重要信息，例如玩家进度、标志、Denizen 位置和块书签、活动脚本进度等。如果您绝对需要手动进行更改，最好停止服务器，进行编辑，然后重新启动服务器，因为 Denizen 会不断写入此文件，这将覆盖您所做的任何更改。
<p>至 reiterate: 该文件会在进程进行和服务器停止时定期自动保存，并且只能在服务器关闭或 Denizen 禁用时手动编辑。
</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="read-only-scripts.yml"><span style="background: white; color: red">read-only-scripts.yml</span></h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">这是 Denizen 创建的另一个文件，不应手动编辑。这是 Denizen 从中读取的脚本文件夹中包含的文件的组合。
<p>该文件在服务器重新启动时填充，或使用 <code>/denizen reload</code> 命令填充。</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading4"><h4 id="/scripts/_folder"><span id=".2Fscripts.2F_folder"></span>/脚本/文件夹</h4></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">Denizen 将从该文件夹读取所有脚本信息。在服务器负载或 <code>/denizen reload</code>，文件被合并并放入read-only-scripts.yml中以供Denizen读取。这可以更好地维护脚本的组织，因为脚本的数量很容易达到三位数。 
<p>plugins/Denizen/scripts/ 文件夹中的文件可以随意命名，只要它们以 <code>.yml</code> 结尾即可。确保不要在文件之间重复脚本名称，因为这会导致问题。脚本文件夹中的所有脚本都合并到<code>read-only-scripts.yml</code>中，因此如果两个脚本命名相同，就会出现问题。</p>
</div>
<p></p>
<p>~~__~~</p>

