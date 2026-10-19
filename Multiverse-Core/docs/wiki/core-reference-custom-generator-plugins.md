---
title: 自定义生成器插件
source_url: https://mvplugins.org/core/reference/custom-generator-plugins/
source_kind: official-wiki
translation_review: reviewed
source_version: 5.8.1; official Wiki snapshot 2026-10-19 @d571cd29a391ce3affe2a21d9f68c4c275a6f33e
---


<a id="top"></a>

# 自定义生成器插件

<p>在这里您将找到开源生成器插件的列表。此列表并不详尽，任何生成器插件都可以与 Multiverse 配合使用。我们也不隶属于任何这些插件。</p>
<a id="How-to-use-generator-plugins-with-Multiverse"></a><h2 id="how-to-use-generator-plugins-with-multiverse">如何使用 Multiverse 生成器插件</h2>
<ol>
<li>将生成器的 jar 放在您的插件文件夹中。</li>
<li>启动你的服务器</li>
<li>使用 <a href="core-fundamentals-commands-usage.md#Generators-Command">生成器命令</a>。这将验证生成器是否正确加载。您应该看到它的名称 appear:
   <div class="highlight"><pre>/mv generators
====[ Multiverse Generator List ]====
VoidGenerator
SkylandsPlus
</pre></div></li>
<li>然后只需使用 create 命令即可通过生成器创建世界。
   <div class="highlight"><pre>/mv create voidworld normal --generator VoidGenerator
</pre></div></li>
<li>有些生成器允许您指定 ID 来自定义世界如何生成。例如，VoidGenerator 允许您指定生物群系，如下所示。
   <div class="highlight"><pre>/mv create coldworld normal --generator VoidGenerator:FROZEN_OCEAN
</pre></div></li>
</ol>
<a id="Terra"></a><h2 id="terra"><a href="https://modrinth.com/plugin/terra">Terra</a></h2>
<p><strong>描述</strong>：Terra 是一款极其强大的数据驱动世界生成器。它允许您完全按照您的规格创建一个世界，而无需了解 Java。</p>
<p><strong>作者</strong>: <a href="https://modrinth.com/user/dfsek">德夫塞克</a></p>
<p><strong>吉图布</strong>：https://github.com/PolyhedralDev/Terra</p>
<p><strong>不和谐</strong>：https://discord.com/invite/PXUEbbF</p>
<a id="Terraform-Generator"></a><h2 id="terraform-generator"><a href="https://www.spigotmc.org/resources/terraformgenerator-1-18-2-1-21-4.75132/">Terraform Generator</a></h2>
<p><strong>描述</strong>：TerraformGenerator 是一个世界生成器插件，旨在提供增强的原版感觉。</p>
<p><strong>作者</strong>: <a href="https://www.spigotmc.org/resources/authors/hex_27.23764/">十六进制_27</a></p>
<p><strong>GitHub</strong>：https://github.com/Hex27/TerraformGenerator</p>
<p><strong>不和谐</strong>: https://discord.gg/yW7JcqM</p>
<a id="VoidGen"></a><h2 id="voidgen"><a href="https://www.spigotmc.org/resources/fork-of-voidgen-1-21-3-supported.121721/">VoidGen</a></h2>
<p><strong>描述</strong>：多合一超轻量虚空世界生成器</p>
<p><strong>作者</strong>: <a href="https://www.spigotmc.org/resources/authors/niconekouwu.1963482/">尼科内库乌</a></p>
<p><strong>维基百科</strong>：https://github.com/NicoNekoDev/VoidGen/blob/master/docs/tutorial.md</p>
<p><strong>GitHub</strong>: https://github.com/NicoNekoDev/VoidGen</p>
<a id="CleanroomGenerator"></a><h2 id="cleanroomgenerator"><a href="https://dev.bukkit.org/projects/cleanroomgenerator">CleanroomGenerator</a></h2>
<p><strong>描述</strong>：生成一个漂亮的平坦景观，用于建造任何你想要的东西！</p>
<p><strong>作者</strong>: <a href="https://github.com/NVX">NVX</a></p>
<p><strong>维基百科</strong>：https://github.com/nvx/CleanroomGenerator/wiki</p>
<p><strong>GitHub</strong>: https://github.com/nvx/CleanroomGenerator</p>

