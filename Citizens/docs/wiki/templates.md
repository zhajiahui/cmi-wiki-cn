---
title: 模板
source_url: https://wiki.citizensnpcs.co/Templates
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5660
---


<a id="top"></a>

# 模板

<p>模板可以方便地在不同 NPC 和服务器之间共享 NPC 配置。</p>
<h2 id="mw-toc-heading">目录结构</h2>
<p>模板保存在 plugins/Citizens/templates 文件夹中。</p>
<p>每个模板由一个<strong>命名空间</strong>和若干模板文件组成。命名空间就是用于将相关模板归为一组的文件夹。</p>
<h2 id="Layout">示例</h2>
<p>下面创建一个简单示例。</p>
<p>新建文件夹 plugins/Citizens/templates/awesometemplates。</p>
<p>在其中创建一个 .yml 文件。文件名可以任意设置，只用于方便整理复杂模板。这里将第一个文件命名为 info.yml。</p>
<p>将以下模板放入 info.yml：</p>
<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">towninfo:
    yaml_replace:
        replacements:
            name: Town Crier
            traits:
                type: VILLAGER
        override: true
    commands:
        on_spawn:
            - say --range 5 Hello!
</pre>
</div></td></tr></tbody></table>
<p>这会创建一个命名空间为 <em>awesometemplates</em>、模板名为 <em>towninfo</em> 的模板。在游戏中可以使用组合键 <em>awesometemplates:towninfo</em>，也可以只用模板名 <em>towninfo</em> 来引用。如果不同命名空间下可能存在同名模板，应使用完整引用。</p>
<p>现在可以使用所需模板创建 NPC：</p>
<div class="highlight"><pre><span></span><code>/npc create NPC --templates awesometemplates:towninfo
</code></pre></div>
<p>你应该会看到一个名为 Town Crier 的村民 NPC，每次生成时都会广播消息 Hello!。</p>
<h2 id="Example">其他命令</h2>
<p>可以直接复制另一个 NPC 的存档数据，例如执行 /template generate awesometemplates:towninfocopy。数据会保存到 towninfocopy.yml 文件。</p>
<p>执行 /template apply awesometemplates:towninfo，可以将模板应用到已有 NPC。</p>
<h2 id="Other_commands">参考</h2>
<p>命令事件：</p>
<ul>
<li>on_spawn：NPC 生成时。</li>
<li>on_template_apply：应用模板时。</li>
</ul>

