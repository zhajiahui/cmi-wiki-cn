---
title: 插件冲突
source_url: https://wiki.citizensnpcs.co/Plugin_Conflict
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5555
---


<a id="top"></a>

# 插件冲突

<p>如果您被发送到此页面，则说明您在使用插件功能时遇到了问题，并且助手怀疑这是由 <strong>插件冲突</strong> 引起的。</p>
<p>本页记录了这是什么以及如何处理它。</p>
<a id="What_is_a_Plugin_Conflict?"></a><h2 id="what-is-a-plugin-conflict">什么是插件冲突？</h2>
<p>插件冲突意味着您的一个插件 e.g 存在问题。 Citizens 或 Denizen 但它可能是由服务器上的某些其他插件引起的。</p>
<p>例如，当多个插件依赖于相同的内部 Minecraft 功能时，或者在某些情况下，当外部插件调用第一个插件的 API 时，这是不应该发生的（例如，某些插件告诉 Citizens 在您不知情的情况下删除所有村民 NPCs ）。</p>
<a id="What_do_I_do_about_it?"></a><h2 id="what-do-i-do-about-it">我该怎么办？</h2>
<a id="Step_1:_Identify_the_fault"></a><h3 id="step-1-identify-the-fault">第 1 步：识别故障</h3>
<p>首先，您必须找出导致问题的插件。</p>
<p>您也许可以缩小范围 - 例如，当 Citizens 无法正确控制记分板（导致 CIT-132392 名称）时，您可以首先禁用 TAB 等记分板插件。</p>
<p>如果您只有几个插件需要测试，可以测试 1-by-1: 删除可疑插件，重新启动服务器，然后测试问题。如果问题消失，则说明该插件有问题。</p>
<p>如果您有很多插件要测试，请使用二进制 search: 删除一半插件并进行测试。如果问题消失了，则问题出在您删除的那一半中。否则，尝试没有另一半。一旦您知道它在哪一半，您就可以尝试删除另一半插件，并重复此策略，直到只有 1 个插件出现问题。</p>
<p>您可能会受益于本地测试服务器。从 Citizens 或 Denizen 开始，看看是否出现问题。如果问题消失，请开始从主服务器一一传输插件和配置，直到问题再次出现。</p>
<a id="Step_2:_Deal_with_the_conflicting_plugin"></a><h3 id="step-2-deal-with-the-conflicting-plugin">第2步：处理冲突的插件</h3>
<p>如果您尝试了所有测试，即使使用仅运行有问题的插件的空白默认服务器，您仍然遇到问题，您可以回来报告该信息。理想情况下，在此测试服务器上包含日志文件的完整副本，以帮助我们自己复制问题（以便我们可以修复它）。</p>
<p>如果您发现有问题的特定插件，</p>
<ul>
<li>告诉我们哪个插件有问题，以及您可能收集到的任何其他相关信息</li>
<li>在某些情况下，我们可能可以从那里处理它，其他时候我们会要求您向有问题的插件的开发人员报告问题。在这些情况下，我们鼓励您告诉相关开发人员您曾与我们交谈并派您到那里，最好在公共位置（例如 Spigot 论坛主题或 GitHub 问题页面）报告问题，并将我们链接到您发布的公开帖子，以便我们可以与该开发人员合作为您解决问题。</li>
</ul>

