---
title: Denizen / 0.7 / 颜色代码
source_url: https://wiki.citizensnpcs.co/Denizen/0.7/Color_Codes
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5403
---


<a id="top"></a>

# Denizen / 0.7 / 颜色代码

<p>有关特定功能（例如单个命令或标签）的更多最新信息和完整详细信息，请查看 <a href="https://meta.denizenscript.com/">元文档</a>。</p>
<p>如果您需要完整的教程来帮助您进行设置，请访问 <a href="https://guide.denizenscript.com/">初学者指南</a> 文本网站。</p>
<p>如果您需要快速帮助，请访问我们的 <a href="https://discord.gg/Q6pZGSR">不和谐组</a>。</p>
<p>此 wiki 已过时，请查看教程视频/指南、元文档或 Discord 小组（均在上面链接）以获取最新信息！</p>
<p>Denizen 提供了几种不同的选项来为文本着色。以下字符与颜色代码结合将更改文本的颜色或格式</p>
<div class="highlight"><pre>§# - the standard minecraft color marker.
\u00167# - an alternate way to make a §
%%# - A denizen replacement for §, more compatible with various text encoding schemes, and easier to type ;)
Note: If using SpoutPlugin/Spoutcraft, you can also use &amp;#
</pre></div>
<p>The format codes available are</p>
<div class="highlight"><pre>0 	Black
1 	Dark Blue
2 	Dark Green
3 	Dark Aqua
4 	Dark Red
5 	Dark Purple
6 	Gold
7 	Gray
8 	Dark Gray
9 	Blue
A 	Green
B 	Aqua
C 	Red
D 	Light Purple
E 	Yellow
F 	White
K 	Magic
L 	Bold
M 	Strike through
N 	Underline
O 	Italic
R 	Reset 
</pre></div>
<p>Examples:</p>
<div class="highlight"><pre>- CHAT "§aThis text is red."
- CHAT "%%aThis text is green."
- NARRATE "%%nThis is underlined but %%rThis is not."
</pre></div>

