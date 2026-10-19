---
title: Depenizen
source_url: https://wiki.citizensnpcs.co/Depenizen
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5399
---


<a id="top"></a>

# Depenizen

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<a id="Depenizen:_Dependencies_for_Denizen!"></a><h1 id="depenizen-dependencies-for-denizen">Depenizen：Denizen 的依赖项！</h1>
<p>欢迎来到 Depenizen 项目！ Depenizen 是什么意思？</p>
<p>Depenizen 是一个简单的插件，其功能正如其名称 implies: 向 Denizen 添加外部插件依赖项。</p>
<p>请前往我们的 <a href="depenizen-frequently-asked-questions.md" title="Depenizen/Frequently Asked Questions">常见问题页面</a> 了解更多信息！</p>
<p><a href="https://github.com/DenizenScript/Depenizen">Depenizen Github</a></p>
<p><a href="http://ci.citizensnpcs.co/view/All/job/Depenizen/">开发构建下载</a></p>
<a id="Depenizen_V0.2"></a><h2 id="depenizen-v02">Depenizen V0.2</h2>
<p>如果您使用 0.1，您可能会注意到更新到最新版本时某些标签被破坏。这是有意为之的，对于新的 Denizen 0.9 系统来说，这几乎是不可避免的，该系统面向更多面向对象的系统。例如，之前在 Denizen 中，使用 <strong>&lt;player&gt;</strong> 将返回玩家的姓名。现在，它将返回一个 dPlayer，由“<strong>p@</strong>”表示，后跟玩家的名字。也就是说，诸如 <strong><player.faction></player.faction></strong> 之类的标签将不再返回派系名称。为此，您现在必须使用 <strong><player.faction.name></player.faction.name></strong>。</p>
<p>其他标签，例如 <strong><player.town.ismayor></player.town.ismayor></strong>，无论玩家是否是他/她的城镇的市长，都会返回，在这个系统中没有任何意义。相反，您应该使用 <strong>- 如果 <player.town.mayor> == &lt;player&gt;</player.town.mayor></strong></p>
<p>...</p>
<p><a href="depenizen-tag-list.md" title="Depenizen/Tag-List">Depenizen 标签列表</a> /// <a href="depenizen-command-list.md" title="Depenizen/Command-List">Depenizen 命令列表</a> /// <a href="depenizen-supported-plugins.md" title="Depenizen/Supported-Plugins">Depenizen 支持的插件列表</a></p>

